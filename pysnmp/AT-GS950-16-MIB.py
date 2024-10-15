# SNMP MIB module (AT-GS950-16-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-GS950-16-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:12 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(lldpXdot1RemPortVlanId,
 lldpXdot1RemProtoVlanSupported,
 lldpXdot1RemProtocolId,
 lldpXdot1RemVlanName) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-MIB",
    "lldpXdot1RemPortVlanId",
    "lldpXdot1RemProtoVlanSupported",
    "lldpXdot1RemProtocolId",
    "lldpXdot1RemVlanName")

(lldpXdot3RemLinkAggStatus,
 lldpXdot3RemMaxFrameSize,
 lldpXdot3RemPortOperMauType,
 lldpXdot3RemPowerClass) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT3-MIB",
    "lldpXdot3RemLinkAggStatus",
    "lldpXdot3RemMaxFrameSize",
    "lldpXdot3RemPortOperMauType",
    "lldpXdot3RemPowerClass")

(lldpLocPortId,
 lldpLocPortNum,
 lldpRemChassisId,
 lldpRemManAddr,
 lldpRemPortId,
 lldpRemSysName,
 lldpStatsRemTablesAgeouts,
 lldpStatsRemTablesDeletes,
 lldpStatsRemTablesDrops,
 lldpStatsRemTablesInserts) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpLocPortId",
    "lldpLocPortNum",
    "lldpRemChassisId",
    "lldpRemManAddr",
    "lldpRemPortId",
    "lldpRemSysName",
    "lldpStatsRemTablesAgeouts",
    "lldpStatsRemTablesDeletes",
    "lldpStatsRemTablesDrops",
    "lldpStatsRemTablesInserts")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(TimeFilter,
 ZeroBasedCounter32) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter",
    "ZeroBasedCounter32")

(SnmpAdminString,
 SnmpEngineID,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

(SnmpTagValue,
 snmpTargetParamsName) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue",
    "snmpTargetParamsName")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

at_GS95016v3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166)
)
at_GS95016v3.setRevisions(
        ("2012-02-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class L2snmpLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("authNoPriv", 4),
          ("authPriv", 5),
          ("noAuthNoPriv", 3),
          ("v1", 1),
          ("v2c", 2))
    )



class PortLaMode(Integer32, TextualConvention):
    status = "current"
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
          ("lacp", 1),
          ("manual", 2))
    )



class LacpKey(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LacpState(Bits, TextualConvention):
    status = "current"


class PaeControlledPortStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )



class AuthenticMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localServer", 2),
          ("remoteServer", 1))
    )



class PermissionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



class IfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("outbound", 1))
    )



class DscpOrAny(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class InetAddressIPv4(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class InetAddressIPv6(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x%4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )



class InetAddressDNS(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d4"


class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



class VlanIndex(Unsigned32, TextualConvention):
    status = "current"


class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_L2Snmp_ObjectIdentity = ObjectIdentity
l2Snmp = _L2Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1)
)
_SysSnmpUser_ObjectIdentity = ObjectIdentity
sysSnmpUser = _SysSnmpUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1)
)
_SysSnmpUserTable_Object = MibTable
sysSnmpUserTable = _SysSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sysSnmpUserTable.setStatus("current")
_SysSnmpUserEntry_Object = MibTableRow
sysSnmpUserEntry = _SysSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1, 1, 1)
)
sysSnmpUserEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnmpUserName"),
)
if mibBuilder.loadTexts:
    sysSnmpUserEntry.setStatus("current")


class _SysSnmpUserName_Type(SnmpAdminString):
    """Custom type sysSnmpUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpUserName_Type.__name__ = "SnmpAdminString"
_SysSnmpUserName_Object = MibTableColumn
sysSnmpUserName = _SysSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1, 1, 1, 1),
    _SysSnmpUserName_Type()
)
sysSnmpUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpUserName.setStatus("current")
_SysSnmpUserAuthProtocol_Type = AutonomousType
_SysSnmpUserAuthProtocol_Object = MibTableColumn
sysSnmpUserAuthProtocol = _SysSnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1, 1, 1, 2),
    _SysSnmpUserAuthProtocol_Type()
)
sysSnmpUserAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpUserAuthProtocol.setStatus("current")
_SysSnmpUserPrivProtocol_Type = AutonomousType
_SysSnmpUserPrivProtocol_Object = MibTableColumn
sysSnmpUserPrivProtocol = _SysSnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1, 1, 1, 3),
    _SysSnmpUserPrivProtocol_Type()
)
sysSnmpUserPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpUserPrivProtocol.setStatus("current")
_SysSnmpUserStatus_Type = RowStatus
_SysSnmpUserStatus_Object = MibTableColumn
sysSnmpUserStatus = _SysSnmpUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 1, 1, 1, 4),
    _SysSnmpUserStatus_Type()
)
sysSnmpUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpUserStatus.setStatus("current")
_SysSnmpGroup_ObjectIdentity = ObjectIdentity
sysSnmpGroup = _SysSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2)
)
_SysSnmpGroupTable_Object = MibTable
sysSnmpGroupTable = _SysSnmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysSnmpGroupTable.setStatus("current")
_SysSnmpGroupEntry_Object = MibTableRow
sysSnmpGroupEntry = _SysSnmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2, 1, 1)
)
sysSnmpGroupEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnmpSecurityModel"),
    (0, "AT-GS950-16-MIB", "sysSnmpSecurityName"),
)
if mibBuilder.loadTexts:
    sysSnmpGroupEntry.setStatus("current")
_SysSnmpSecurityModel_Type = SnmpSecurityModel
_SysSnmpSecurityModel_Object = MibTableColumn
sysSnmpSecurityModel = _SysSnmpSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2, 1, 1, 1),
    _SysSnmpSecurityModel_Type()
)
sysSnmpSecurityModel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpSecurityModel.setStatus("current")


class _SysSnmpSecurityName_Type(SnmpAdminString):
    """Custom type sysSnmpSecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpSecurityName_Type.__name__ = "SnmpAdminString"
_SysSnmpSecurityName_Object = MibTableColumn
sysSnmpSecurityName = _SysSnmpSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2, 1, 1, 2),
    _SysSnmpSecurityName_Type()
)
sysSnmpSecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpSecurityName.setStatus("current")


class _SysSnmpGroupName_Type(SnmpAdminString):
    """Custom type sysSnmpGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpGroupName_Type.__name__ = "SnmpAdminString"
_SysSnmpGroupName_Object = MibTableColumn
sysSnmpGroupName = _SysSnmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2, 1, 1, 3),
    _SysSnmpGroupName_Type()
)
sysSnmpGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpGroupName.setStatus("current")
_SysSnmpGroupStatus_Type = RowStatus
_SysSnmpGroupStatus_Object = MibTableColumn
sysSnmpGroupStatus = _SysSnmpGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 2, 1, 1, 4),
    _SysSnmpGroupStatus_Type()
)
sysSnmpGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpGroupStatus.setStatus("current")
_SysSnmpGroupAccess_ObjectIdentity = ObjectIdentity
sysSnmpGroupAccess = _SysSnmpGroupAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3)
)
_SysSnmpGroupAccessTable_Object = MibTable
sysSnmpGroupAccessTable = _SysSnmpGroupAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sysSnmpGroupAccessTable.setStatus("current")
_SysSnmpGroupAccessEntry_Object = MibTableRow
sysSnmpGroupAccessEntry = _SysSnmpGroupAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1)
)
sysSnmpGroupAccessEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnmpaccessGroupIndex"),
    (0, "AT-GS950-16-MIB", "sysSnmpaccessSecurityModel"),
    (0, "AT-GS950-16-MIB", "sysSnmpaccessSecurityLevel"),
)
if mibBuilder.loadTexts:
    sysSnmpGroupAccessEntry.setStatus("current")


class _SysSnmpaccessGroupIndex_Type(SnmpAdminString):
    """Custom type sysSnmpaccessGroupIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpaccessGroupIndex_Type.__name__ = "SnmpAdminString"
_SysSnmpaccessGroupIndex_Object = MibTableColumn
sysSnmpaccessGroupIndex = _SysSnmpaccessGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 1),
    _SysSnmpaccessGroupIndex_Type()
)
sysSnmpaccessGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpaccessGroupIndex.setStatus("current")
_SysSnmpaccessSecurityModel_Type = SnmpSecurityModel
_SysSnmpaccessSecurityModel_Object = MibTableColumn
sysSnmpaccessSecurityModel = _SysSnmpaccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 2),
    _SysSnmpaccessSecurityModel_Type()
)
sysSnmpaccessSecurityModel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpaccessSecurityModel.setStatus("current")
_SysSnmpaccessSecurityLevel_Type = SnmpSecurityLevel
_SysSnmpaccessSecurityLevel_Object = MibTableColumn
sysSnmpaccessSecurityLevel = _SysSnmpaccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 3),
    _SysSnmpaccessSecurityLevel_Type()
)
sysSnmpaccessSecurityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpaccessSecurityLevel.setStatus("current")


class _SysSnmpaccessReadViewName_Type(SnmpAdminString):
    """Custom type sysSnmpaccessReadViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysSnmpaccessReadViewName_Type.__name__ = "SnmpAdminString"
_SysSnmpaccessReadViewName_Object = MibTableColumn
sysSnmpaccessReadViewName = _SysSnmpaccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 4),
    _SysSnmpaccessReadViewName_Type()
)
sysSnmpaccessReadViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpaccessReadViewName.setStatus("current")


class _SysSnmpaccessWriteViewName_Type(SnmpAdminString):
    """Custom type sysSnmpaccessWriteViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysSnmpaccessWriteViewName_Type.__name__ = "SnmpAdminString"
_SysSnmpaccessWriteViewName_Object = MibTableColumn
sysSnmpaccessWriteViewName = _SysSnmpaccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 5),
    _SysSnmpaccessWriteViewName_Type()
)
sysSnmpaccessWriteViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpaccessWriteViewName.setStatus("current")


class _SysSnmpaccessNotifyViewName_Type(SnmpAdminString):
    """Custom type sysSnmpaccessNotifyViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysSnmpaccessNotifyViewName_Type.__name__ = "SnmpAdminString"
_SysSnmpaccessNotifyViewName_Object = MibTableColumn
sysSnmpaccessNotifyViewName = _SysSnmpaccessNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 6),
    _SysSnmpaccessNotifyViewName_Type()
)
sysSnmpaccessNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpaccessNotifyViewName.setStatus("current")
_SysSnmpaccessStatus_Type = RowStatus
_SysSnmpaccessStatus_Object = MibTableColumn
sysSnmpaccessStatus = _SysSnmpaccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 3, 1, 1, 7),
    _SysSnmpaccessStatus_Type()
)
sysSnmpaccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpaccessStatus.setStatus("current")
_SysSnmpViewTree_ObjectIdentity = ObjectIdentity
sysSnmpViewTree = _SysSnmpViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4)
)
_SysSnmpViewTreeTable_Object = MibTable
sysSnmpViewTreeTable = _SysSnmpViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sysSnmpViewTreeTable.setStatus("current")
_SysSnmpViewTreeEntry_Object = MibTableRow
sysSnmpViewTreeEntry = _SysSnmpViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1, 1)
)
sysSnmpViewTreeEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnmpviewTreeName"),
    (0, "AT-GS950-16-MIB", "sysSnmpviewTreeSubtree"),
)
if mibBuilder.loadTexts:
    sysSnmpViewTreeEntry.setStatus("current")


class _SysSnmpviewTreeName_Type(SnmpAdminString):
    """Custom type sysSnmpviewTreeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpviewTreeName_Type.__name__ = "SnmpAdminString"
_SysSnmpviewTreeName_Object = MibTableColumn
sysSnmpviewTreeName = _SysSnmpviewTreeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1, 1, 1),
    _SysSnmpviewTreeName_Type()
)
sysSnmpviewTreeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpviewTreeName.setStatus("current")
_SysSnmpviewTreeSubtree_Type = ObjectIdentifier
_SysSnmpviewTreeSubtree_Object = MibTableColumn
sysSnmpviewTreeSubtree = _SysSnmpviewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1, 1, 2),
    _SysSnmpviewTreeSubtree_Type()
)
sysSnmpviewTreeSubtree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpviewTreeSubtree.setStatus("current")


class _SysSnmpviewTreeMask_Type(OctetString):
    """Custom type sysSnmpviewTreeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysSnmpviewTreeMask_Type.__name__ = "OctetString"
_SysSnmpviewTreeMask_Object = MibTableColumn
sysSnmpviewTreeMask = _SysSnmpviewTreeMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1, 1, 3),
    _SysSnmpviewTreeMask_Type()
)
sysSnmpviewTreeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpviewTreeMask.setStatus("current")


class _SysSnmpviewTreeType_Type(Integer32):
    """Custom type sysSnmpviewTreeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_SysSnmpviewTreeType_Type.__name__ = "Integer32"
_SysSnmpviewTreeType_Object = MibTableColumn
sysSnmpviewTreeType = _SysSnmpviewTreeType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1, 1, 4),
    _SysSnmpviewTreeType_Type()
)
sysSnmpviewTreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpviewTreeType.setStatus("current")
_SysSnmpviewTreeStatus_Type = RowStatus
_SysSnmpviewTreeStatus_Object = MibTableColumn
sysSnmpviewTreeStatus = _SysSnmpviewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 4, 1, 1, 5),
    _SysSnmpviewTreeStatus_Type()
)
sysSnmpviewTreeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpviewTreeStatus.setStatus("current")
_SysSnmpCommunity_ObjectIdentity = ObjectIdentity
sysSnmpCommunity = _SysSnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5)
)
_SysSnmpCommunityTable_Object = MibTable
sysSnmpCommunityTable = _SysSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sysSnmpCommunityTable.setStatus("current")
_SysSnmpCommunityEntry_Object = MibTableRow
sysSnmpCommunityEntry = _SysSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5, 1, 1)
)
sysSnmpCommunityEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnmpsnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    sysSnmpCommunityEntry.setStatus("current")


class _SysSnmpsnmpCommunityIndex_Type(SnmpAdminString):
    """Custom type sysSnmpsnmpCommunityIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpsnmpCommunityIndex_Type.__name__ = "SnmpAdminString"
_SysSnmpsnmpCommunityIndex_Object = MibTableColumn
sysSnmpsnmpCommunityIndex = _SysSnmpsnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5, 1, 1, 1),
    _SysSnmpsnmpCommunityIndex_Type()
)
sysSnmpsnmpCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpsnmpCommunityIndex.setStatus("current")


class _SysSnmpsnmpCommunityName_Type(SnmpAdminString):
    """Custom type sysSnmpsnmpCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpsnmpCommunityName_Type.__name__ = "SnmpAdminString"
_SysSnmpsnmpCommunityName_Object = MibTableColumn
sysSnmpsnmpCommunityName = _SysSnmpsnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5, 1, 1, 2),
    _SysSnmpsnmpCommunityName_Type()
)
sysSnmpsnmpCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpsnmpCommunityName.setStatus("current")


class _SysSnmpsnmpCommunityPolicy_Type(SnmpAdminString):
    """Custom type sysSnmpsnmpCommunityPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpsnmpCommunityPolicy_Type.__name__ = "SnmpAdminString"
_SysSnmpsnmpCommunityPolicy_Object = MibTableColumn
sysSnmpsnmpCommunityPolicy = _SysSnmpsnmpCommunityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5, 1, 1, 3),
    _SysSnmpsnmpCommunityPolicy_Type()
)
sysSnmpsnmpCommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpsnmpCommunityPolicy.setStatus("current")
_SysSnmpsnmpCommunityStatus_Type = RowStatus
_SysSnmpsnmpCommunityStatus_Object = MibTableColumn
sysSnmpsnmpCommunityStatus = _SysSnmpsnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 5, 1, 1, 4),
    _SysSnmpsnmpCommunityStatus_Type()
)
sysSnmpsnmpCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpsnmpCommunityStatus.setStatus("current")
_SysSnmpTrapManager_ObjectIdentity = ObjectIdentity
sysSnmpTrapManager = _SysSnmpTrapManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6)
)
_SysSnmpTrapManagerTable_Object = MibTable
sysSnmpTrapManagerTable = _SysSnmpTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sysSnmpTrapManagerTable.setStatus("current")
_SysSnmpTrapManagerEntry_Object = MibTableRow
sysSnmpTrapManagerEntry = _SysSnmpTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6, 1, 1)
)
sysSnmpTrapManagerEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnmpsnmpTrapManagerName"),
)
if mibBuilder.loadTexts:
    sysSnmpTrapManagerEntry.setStatus("current")


class _SysSnmpsnmpTrapManagerName_Type(SnmpAdminString):
    """Custom type sysSnmpsnmpTrapManagerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysSnmpsnmpTrapManagerName_Type.__name__ = "SnmpAdminString"
_SysSnmpsnmpTrapManagerName_Object = MibTableColumn
sysSnmpsnmpTrapManagerName = _SysSnmpsnmpTrapManagerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6, 1, 1, 1),
    _SysSnmpsnmpTrapManagerName_Type()
)
sysSnmpsnmpTrapManagerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnmpsnmpTrapManagerName.setStatus("current")
_SysSnmpsnmpTrapManagerAddress_Type = TAddress
_SysSnmpsnmpTrapManagerAddress_Object = MibTableColumn
sysSnmpsnmpTrapManagerAddress = _SysSnmpsnmpTrapManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6, 1, 1, 2),
    _SysSnmpsnmpTrapManagerAddress_Type()
)
sysSnmpsnmpTrapManagerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpsnmpTrapManagerAddress.setStatus("current")
_SysSnmpsnmpTrapManagerSecurityLevel_Type = L2snmpLevel
_SysSnmpsnmpTrapManagerSecurityLevel_Object = MibTableColumn
sysSnmpsnmpTrapManagerSecurityLevel = _SysSnmpsnmpTrapManagerSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6, 1, 1, 3),
    _SysSnmpsnmpTrapManagerSecurityLevel_Type()
)
sysSnmpsnmpTrapManagerSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpsnmpTrapManagerSecurityLevel.setStatus("current")
_SysSnmpsnmpTrapManagerStatus_Type = RowStatus
_SysSnmpsnmpTrapManagerStatus_Object = MibTableColumn
sysSnmpsnmpTrapManagerStatus = _SysSnmpsnmpTrapManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 6, 1, 1, 4),
    _SysSnmpsnmpTrapManagerStatus_Type()
)
sysSnmpsnmpTrapManagerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnmpsnmpTrapManagerStatus.setStatus("current")
_SysSnmpEngineID_Type = SnmpEngineID
_SysSnmpEngineID_Object = MibScalar
sysSnmpEngineID = _SysSnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 7),
    _SysSnmpEngineID_Type()
)
sysSnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpEngineID.setStatus("current")


class _SnmpGlobalState_Type(Integer32):
    """Custom type snmpGlobalState based on Integer32"""
    defaultValue = 1

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


_SnmpGlobalState_Type.__name__ = "Integer32"
_SnmpGlobalState_Object = MibScalar
snmpGlobalState = _SnmpGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 1, 8),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")
_L2Radius_ObjectIdentity = ObjectIdentity
l2Radius = _L2Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25)
)
_SysRadiusExtClient_ObjectIdentity = ObjectIdentity
sysRadiusExtClient = _SysRadiusExtClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1)
)
_SysRadiusExtServerTable_Object = MibTable
sysRadiusExtServerTable = _SysRadiusExtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3)
)
if mibBuilder.loadTexts:
    sysRadiusExtServerTable.setStatus("current")
_SysRadiusExtServerEntry_Object = MibTableRow
sysRadiusExtServerEntry = _SysRadiusExtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1)
)
sysRadiusExtServerEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysRadiusExtServerIndex"),
)
if mibBuilder.loadTexts:
    sysRadiusExtServerEntry.setStatus("current")
_SysRadiusExtServerIndex_Type = InterfaceIndex
_SysRadiusExtServerIndex_Object = MibTableColumn
sysRadiusExtServerIndex = _SysRadiusExtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 1),
    _SysRadiusExtServerIndex_Type()
)
sysRadiusExtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusExtServerIndex.setStatus("current")
_SysRadiusExtServerAddress_Type = IpAddress
_SysRadiusExtServerAddress_Object = MibTableColumn
sysRadiusExtServerAddress = _SysRadiusExtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 2),
    _SysRadiusExtServerAddress_Type()
)
sysRadiusExtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusExtServerAddress.setStatus("current")
_SysRadiusExtServerSharedSecret_Type = DisplayString
_SysRadiusExtServerSharedSecret_Object = MibTableColumn
sysRadiusExtServerSharedSecret = _SysRadiusExtServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 4),
    _SysRadiusExtServerSharedSecret_Type()
)
sysRadiusExtServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusExtServerSharedSecret.setStatus("current")


class _SysRadiusExtServerResponseTime_Type(Integer32):
    """Custom type sysRadiusExtServerResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SysRadiusExtServerResponseTime_Type.__name__ = "Integer32"
_SysRadiusExtServerResponseTime_Object = MibTableColumn
sysRadiusExtServerResponseTime = _SysRadiusExtServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 6),
    _SysRadiusExtServerResponseTime_Type()
)
sysRadiusExtServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusExtServerResponseTime.setStatus("current")


class _SysRadiusExtServerMaximumRetransmission_Type(Integer32):
    """Custom type sysRadiusExtServerMaximumRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SysRadiusExtServerMaximumRetransmission_Type.__name__ = "Integer32"
_SysRadiusExtServerMaximumRetransmission_Object = MibTableColumn
sysRadiusExtServerMaximumRetransmission = _SysRadiusExtServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 7),
    _SysRadiusExtServerMaximumRetransmission_Type()
)
sysRadiusExtServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusExtServerMaximumRetransmission.setStatus("current")


class _SysRadiusExtServerAuthPortNum_Type(Integer32):
    """Custom type sysRadiusExtServerAuthPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysRadiusExtServerAuthPortNum_Type.__name__ = "Integer32"
_SysRadiusExtServerAuthPortNum_Object = MibTableColumn
sysRadiusExtServerAuthPortNum = _SysRadiusExtServerAuthPortNum_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 8),
    _SysRadiusExtServerAuthPortNum_Type()
)
sysRadiusExtServerAuthPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusExtServerAuthPortNum.setStatus("current")
_SysRadiusExtServerEntryStatus_Type = RowStatus
_SysRadiusExtServerEntryStatus_Object = MibTableColumn
sysRadiusExtServerEntryStatus = _SysRadiusExtServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 9),
    _SysRadiusExtServerEntryStatus_Type()
)
sysRadiusExtServerEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysRadiusExtServerEntryStatus.setStatus("current")


class _SysRadiusExtServerAccPort_Type(Integer32):
    """Custom type sysRadiusExtServerAccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysRadiusExtServerAccPort_Type.__name__ = "Integer32"
_SysRadiusExtServerAccPort_Object = MibTableColumn
sysRadiusExtServerAccPort = _SysRadiusExtServerAccPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 25, 1, 3, 1, 10),
    _SysRadiusExtServerAccPort_Type()
)
sysRadiusExtServerAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusExtServerAccPort.setStatus("current")
_L2Cfa_ObjectIdentity = ObjectIdentity
l2Cfa = _L2Cfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27)
)
__pysmi_if_ObjectIdentity = ObjectIdentity
_pysmi_if = __pysmi_if_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1)
)
_IfMaxInterfaces_Type = InterfaceIndex
_IfMaxInterfaces_Object = MibScalar
ifMaxInterfaces = _IfMaxInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 1),
    _IfMaxInterfaces_Type()
)
ifMaxInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMaxInterfaces.setStatus("deprecated")
_IfMaxPhysInterfaces_Type = InterfaceIndex
_IfMaxPhysInterfaces_Object = MibScalar
ifMaxPhysInterfaces = _IfMaxPhysInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 2),
    _IfMaxPhysInterfaces_Type()
)
ifMaxPhysInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMaxPhysInterfaces.setStatus("deprecated")
_IfAvailableIndex_Type = InterfaceIndex
_IfAvailableIndex_Object = MibScalar
ifAvailableIndex = _IfAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 3),
    _IfAvailableIndex_Type()
)
ifAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAvailableIndex.setStatus("current")
_IfMainTable_Object = MibTable
ifMainTable = _IfMainTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4)
)
if mibBuilder.loadTexts:
    ifMainTable.setStatus("current")
_IfMainEntry_Object = MibTableRow
ifMainEntry = _IfMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1)
)
ifMainEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifMainEntry.setStatus("current")
_IfMainIndex_Type = InterfaceIndex
_IfMainIndex_Object = MibTableColumn
ifMainIndex = _IfMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 1),
    _IfMainIndex_Type()
)
ifMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifMainIndex.setStatus("current")


class _IfMainType_Type(Integer32):
    """Custom type ifMainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              9,
              23,
              24,
              32,
              38,
              49,
              84,
              92,
              108,
              114,
              118,
              131,
              134,
              135,
              136,
              150,
              161,
              166)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("async", 84),
          ("atmSubInterface", 134),
          ("ethernetCsmacd", 6),
          ("frameRelay", 32),
          ("frameRelayMPI", 92),
          ("hdlc", 118),
          ("ieee8023ad", 161),
          ("ipOverAtm", 114),
          ("iso88025TokenRing", 9),
          ("l2macvlan", 135),
          ("l3ipvlan", 136),
          ("miox25", 38),
          ("mpls", 166),
          ("mplsTunnel", 150),
          ("ppp", 23),
          ("pppMultilinkBundle", 108),
          ("rfc877x25", 5),
          ("softwareLoopback", 24),
          ("tunnel", 131))
    )


_IfMainType_Type.__name__ = "Integer32"
_IfMainType_Object = MibTableColumn
ifMainType = _IfMainType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 2),
    _IfMainType_Type()
)
ifMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainType.setStatus("current")
_IfMainMtu_Type = Integer32
_IfMainMtu_Object = MibTableColumn
ifMainMtu = _IfMainMtu_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 3),
    _IfMainMtu_Type()
)
ifMainMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainMtu.setStatus("current")


class _IfMainAdminStatus_Type(Integer32):
    """Custom type ifMainAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_IfMainAdminStatus_Type.__name__ = "Integer32"
_IfMainAdminStatus_Object = MibTableColumn
ifMainAdminStatus = _IfMainAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 4),
    _IfMainAdminStatus_Type()
)
ifMainAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainAdminStatus.setStatus("current")


class _IfMainOperStatus_Type(Integer32):
    """Custom type ifMainOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_IfMainOperStatus_Type.__name__ = "Integer32"
_IfMainOperStatus_Object = MibTableColumn
ifMainOperStatus = _IfMainOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 5),
    _IfMainOperStatus_Type()
)
ifMainOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainOperStatus.setStatus("current")


class _IfMainEncapType_Type(Integer32):
    """Custom type ifMainEncapType based on Integer32"""
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
        *(("cudNlpid", 4),
          ("cudNlpidSnap", 5),
          ("ethernetV2", 8),
          ("llcSnap", 6),
          ("nlpid", 2),
          ("nlpidSnap", 3),
          ("other", 1),
          ("vcMultiplexed", 7))
    )


_IfMainEncapType_Type.__name__ = "Integer32"
_IfMainEncapType_Object = MibTableColumn
ifMainEncapType = _IfMainEncapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 6),
    _IfMainEncapType_Type()
)
ifMainEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainEncapType.setStatus("current")


class _IfMainBrgPortType_Type(Integer32):
    """Custom type ifMainBrgPortType based on Integer32"""
    defaultValue = 8

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
        *(("customerBridgePort", 8),
          ("customerEdgePort", 4),
          ("customerNetworkPortPortBased", 2),
          ("customerNetworkPortStagged", 3),
          ("propCustomerEdgePort", 5),
          ("propCustomerNetworkPort", 6),
          ("propProviderNetworkPort", 7),
          ("providerNetworkPort", 1))
    )


_IfMainBrgPortType_Type.__name__ = "Integer32"
_IfMainBrgPortType_Object = MibTableColumn
ifMainBrgPortType = _IfMainBrgPortType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 7),
    _IfMainBrgPortType_Type()
)
ifMainBrgPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainBrgPortType.setStatus("current")
_IfMainRowStatus_Type = RowStatus
_IfMainRowStatus_Object = MibTableColumn
ifMainRowStatus = _IfMainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 4, 1, 8),
    _IfMainRowStatus_Type()
)
ifMainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainRowStatus.setStatus("current")
_IfIpTable_Object = MibTable
ifIpTable = _IfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5)
)
if mibBuilder.loadTexts:
    ifIpTable.setStatus("current")
_IfIpEntry_Object = MibTableRow
ifIpEntry = _IfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1)
)
ifIpEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifIpEntry.setStatus("current")


class _IfIpAddrAllocMethod_Type(Integer32):
    """Custom type ifIpAddrAllocMethod based on Integer32"""
    defaultValue = 4

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
        *(("dynamic", 3),
          ("manual", 1),
          ("negotiation", 2),
          ("none", 4))
    )


_IfIpAddrAllocMethod_Type.__name__ = "Integer32"
_IfIpAddrAllocMethod_Object = MibTableColumn
ifIpAddrAllocMethod = _IfIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1, 1),
    _IfIpAddrAllocMethod_Type()
)
ifIpAddrAllocMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddrAllocMethod.setStatus("current")


class _IfIpAddr_Type(IpAddress):
    """Custom type ifIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IfIpAddr_Object = MibTableColumn
ifIpAddr = _IfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1, 2),
    _IfIpAddr_Type()
)
ifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddr.setStatus("current")
_IfIpSubnetMask_Type = IpAddress
_IfIpSubnetMask_Object = MibTableColumn
ifIpSubnetMask = _IfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1, 3),
    _IfIpSubnetMask_Type()
)
ifIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpSubnetMask.setStatus("current")
_IfIpBroadcastAddr_Type = IpAddress
_IfIpBroadcastAddr_Object = MibTableColumn
ifIpBroadcastAddr = _IfIpBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1, 4),
    _IfIpBroadcastAddr_Type()
)
ifIpBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpBroadcastAddr.setStatus("current")


class _IfIpForwardingEnable_Type(TruthValue):
    """Custom type ifIpForwardingEnable based on TruthValue"""


_IfIpForwardingEnable_Object = MibTableColumn
ifIpForwardingEnable = _IfIpForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1, 5),
    _IfIpForwardingEnable_Type()
)
ifIpForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpForwardingEnable.setStatus("current")


class _IfIpAddrAllocProtocol_Type(Integer32):
    """Custom type ifIpAddrAllocProtocol based on Integer32"""
    defaultValue = 2

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
        *(("bootp", 3),
          ("dhcp", 2),
          ("none", 0),
          ("rarp", 1))
    )


_IfIpAddrAllocProtocol_Type.__name__ = "Integer32"
_IfIpAddrAllocProtocol_Object = MibTableColumn
ifIpAddrAllocProtocol = _IfIpAddrAllocProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 5, 1, 6),
    _IfIpAddrAllocProtocol_Type()
)
ifIpAddrAllocProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddrAllocProtocol.setStatus("current")
_IfIvrTable_Object = MibTable
ifIvrTable = _IfIvrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 8)
)
if mibBuilder.loadTexts:
    ifIvrTable.setStatus("current")
_IfIvrEntry_Object = MibTableRow
ifIvrEntry = _IfIvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 8, 1)
)
ifIvrEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifIvrEntry.setStatus("current")
_IfIvrBridgedIface_Type = TruthValue
_IfIvrBridgedIface_Object = MibTableColumn
ifIvrBridgedIface = _IfIvrBridgedIface_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 8, 1, 1),
    _IfIvrBridgedIface_Type()
)
ifIvrBridgedIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIvrBridgedIface.setStatus("current")


class _IfSetMgmtVlanList_Type(OctetString):
    """Custom type ifSetMgmtVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfSetMgmtVlanList_Type.__name__ = "OctetString"
_IfSetMgmtVlanList_Object = MibScalar
ifSetMgmtVlanList = _IfSetMgmtVlanList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 9),
    _IfSetMgmtVlanList_Type()
)
ifSetMgmtVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSetMgmtVlanList.setStatus("current")


class _IfResetMgmtVlanList_Type(OctetString):
    """Custom type ifResetMgmtVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfResetMgmtVlanList_Type.__name__ = "OctetString"
_IfResetMgmtVlanList_Object = MibScalar
ifResetMgmtVlanList = _IfResetMgmtVlanList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 10),
    _IfResetMgmtVlanList_Type()
)
ifResetMgmtVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifResetMgmtVlanList.setStatus("current")
_IfSecondaryIpAddressTable_Object = MibTable
ifSecondaryIpAddressTable = _IfSecondaryIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 11)
)
if mibBuilder.loadTexts:
    ifSecondaryIpAddressTable.setStatus("current")
_IfSecondaryIpAddressEntry_Object = MibTableRow
ifSecondaryIpAddressEntry = _IfSecondaryIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 11, 1)
)
ifSecondaryIpAddressEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "ifMainIndex"),
    (0, "AT-GS950-16-MIB", "ifSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    ifSecondaryIpAddressEntry.setStatus("current")
_IfSecondaryIpAddress_Type = IpAddress
_IfSecondaryIpAddress_Object = MibTableColumn
ifSecondaryIpAddress = _IfSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 11, 1, 1),
    _IfSecondaryIpAddress_Type()
)
ifSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifSecondaryIpAddress.setStatus("current")
_IfSecondaryIpSubnetMask_Type = IpAddress
_IfSecondaryIpSubnetMask_Object = MibTableColumn
ifSecondaryIpSubnetMask = _IfSecondaryIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 11, 1, 2),
    _IfSecondaryIpSubnetMask_Type()
)
ifSecondaryIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecondaryIpSubnetMask.setStatus("current")
_IfSecondaryIpBroadcastAddr_Type = IpAddress
_IfSecondaryIpBroadcastAddr_Object = MibTableColumn
ifSecondaryIpBroadcastAddr = _IfSecondaryIpBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 11, 1, 3),
    _IfSecondaryIpBroadcastAddr_Type()
)
ifSecondaryIpBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecondaryIpBroadcastAddr.setStatus("current")
_IfSecondaryIpRowStatus_Type = RowStatus
_IfSecondaryIpRowStatus_Object = MibTableColumn
ifSecondaryIpRowStatus = _IfSecondaryIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 1, 11, 1, 4),
    _IfSecondaryIpRowStatus_Type()
)
ifSecondaryIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifSecondaryIpRowStatus.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 27, 4)
)
_L2Rmon_ObjectIdentity = ObjectIdentity
l2Rmon = _L2Rmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 44)
)


class _SysRmonEnableStatus_Type(Integer32):
    """Custom type sysRmonEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sysRmondisabled", 2),
          ("sysRmonenabled", 1))
    )


_SysRmonEnableStatus_Type.__name__ = "Integer32"
_SysRmonEnableStatus_Object = MibScalar
sysRmonEnableStatus = _SysRmonEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 44, 2),
    _SysRmonEnableStatus_Type()
)
sysRmonEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRmonEnableStatus.setStatus("current")


class _SysRmonHwStatsSupp_Type(Integer32):
    """Custom type sysRmonHwStatsSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_SysRmonHwStatsSupp_Type.__name__ = "Integer32"
_SysRmonHwStatsSupp_Object = MibScalar
sysRmonHwStatsSupp = _SysRmonHwStatsSupp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 44, 3),
    _SysRmonHwStatsSupp_Type()
)
sysRmonHwStatsSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRmonHwStatsSupp.setStatus("current")


class _SysRmonHwHistorySupp_Type(Integer32):
    """Custom type sysRmonHwHistorySupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_SysRmonHwHistorySupp_Type.__name__ = "Integer32"
_SysRmonHwHistorySupp_Object = MibScalar
sysRmonHwHistorySupp = _SysRmonHwHistorySupp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 44, 4),
    _SysRmonHwHistorySupp_Type()
)
sysRmonHwHistorySupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRmonHwHistorySupp.setStatus("current")


class _SysRmonHwAlarmSupp_Type(Integer32):
    """Custom type sysRmonHwAlarmSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_SysRmonHwAlarmSupp_Type.__name__ = "Integer32"
_SysRmonHwAlarmSupp_Object = MibScalar
sysRmonHwAlarmSupp = _SysRmonHwAlarmSupp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 44, 5),
    _SysRmonHwAlarmSupp_Type()
)
sysRmonHwAlarmSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRmonHwAlarmSupp.setStatus("current")


class _SysRmonHwEventSupp_Type(Integer32):
    """Custom type sysRmonHwEventSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_SysRmonHwEventSupp_Type.__name__ = "Integer32"
_SysRmonHwEventSupp_Object = MibScalar
sysRmonHwEventSupp = _SysRmonHwEventSupp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 44, 9),
    _SysRmonHwEventSupp_Type()
)
sysRmonHwEventSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRmonHwEventSupp.setStatus("current")
_L2La_ObjectIdentity = ObjectIdentity
l2La = _L2La_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63)
)
_SysLaSystem_ObjectIdentity = ObjectIdentity
sysLaSystem = _SysLaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1)
)


class _SysLaSystemControl_Type(Integer32):
    """Custom type sysLaSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("start", 1))
    )


_SysLaSystemControl_Type.__name__ = "Integer32"
_SysLaSystemControl_Object = MibScalar
sysLaSystemControl = _SysLaSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 1),
    _SysLaSystemControl_Type()
)
sysLaSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaSystemControl.setStatus("current")


class _SysLaStatus_Type(Integer32):
    """Custom type sysLaStatus based on Integer32"""
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


_SysLaStatus_Type.__name__ = "Integer32"
_SysLaStatus_Object = MibScalar
sysLaStatus = _SysLaStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 2),
    _SysLaStatus_Type()
)
sysLaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaStatus.setStatus("current")


class _SysLaTraceOption_Type(Integer32):
    """Custom type sysLaTraceOption based on Integer32"""
    defaultValue = 0


_SysLaTraceOption_Object = MibScalar
sysLaTraceOption = _SysLaTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 3),
    _SysLaTraceOption_Type()
)
sysLaTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaTraceOption.setStatus("current")
_SysLaMaxPortsPerPortChannel_Type = Integer32
_SysLaMaxPortsPerPortChannel_Object = MibScalar
sysLaMaxPortsPerPortChannel = _SysLaMaxPortsPerPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 4),
    _SysLaMaxPortsPerPortChannel_Type()
)
sysLaMaxPortsPerPortChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaMaxPortsPerPortChannel.setStatus("current")
_SysLaMaxPortChannels_Type = Integer32
_SysLaMaxPortChannels_Object = MibScalar
sysLaMaxPortChannels = _SysLaMaxPortChannels_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 5),
    _SysLaMaxPortChannels_Type()
)
sysLaMaxPortChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaMaxPortChannels.setStatus("current")


class _SysLaOperStatus_Type(Integer32):
    """Custom type sysLaOperStatus based on Integer32"""
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


_SysLaOperStatus_Type.__name__ = "Integer32"
_SysLaOperStatus_Object = MibScalar
sysLaOperStatus = _SysLaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 6),
    _SysLaOperStatus_Type()
)
sysLaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaOperStatus.setStatus("current")
_SysLaActorSystemID_Type = MacAddress
_SysLaActorSystemID_Object = MibScalar
sysLaActorSystemID = _SysLaActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 1, 7),
    _SysLaActorSystemID_Type()
)
sysLaActorSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaActorSystemID.setStatus("current")
_SysLaPortChannel_ObjectIdentity = ObjectIdentity
sysLaPortChannel = _SysLaPortChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2)
)
_SysLaPortChannelTable_Object = MibTable
sysLaPortChannelTable = _SysLaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1)
)
if mibBuilder.loadTexts:
    sysLaPortChannelTable.setStatus("current")
_SysLaPortChannelEntry_Object = MibTableRow
sysLaPortChannelEntry = _SysLaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1)
)
sysLaPortChannelEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysLaPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    sysLaPortChannelEntry.setStatus("current")
_SysLaPortChannelIfIndex_Type = InterfaceIndex
_SysLaPortChannelIfIndex_Object = MibTableColumn
sysLaPortChannelIfIndex = _SysLaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 1),
    _SysLaPortChannelIfIndex_Type()
)
sysLaPortChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLaPortChannelIfIndex.setStatus("current")
_SysLaPortChannelGroup_Type = LacpKey
_SysLaPortChannelGroup_Object = MibTableColumn
sysLaPortChannelGroup = _SysLaPortChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 2),
    _SysLaPortChannelGroup_Type()
)
sysLaPortChannelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaPortChannelGroup.setStatus("current")
_SysLaPortChannelAdminMacAddress_Type = MacAddress
_SysLaPortChannelAdminMacAddress_Object = MibTableColumn
sysLaPortChannelAdminMacAddress = _SysLaPortChannelAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 3),
    _SysLaPortChannelAdminMacAddress_Type()
)
sysLaPortChannelAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortChannelAdminMacAddress.setStatus("current")


class _SysLaPortChannelMacSelection_Type(Integer32):
    """Custom type sysLaPortChannelMacSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("force", 2))
    )


_SysLaPortChannelMacSelection_Type.__name__ = "Integer32"
_SysLaPortChannelMacSelection_Object = MibTableColumn
sysLaPortChannelMacSelection = _SysLaPortChannelMacSelection_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 4),
    _SysLaPortChannelMacSelection_Type()
)
sysLaPortChannelMacSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortChannelMacSelection.setStatus("current")
_SysLaPortChannelMode_Type = PortLaMode
_SysLaPortChannelMode_Object = MibTableColumn
sysLaPortChannelMode = _SysLaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 5),
    _SysLaPortChannelMode_Type()
)
sysLaPortChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaPortChannelMode.setStatus("current")
_SysLaPortChannelPortCount_Type = Integer32
_SysLaPortChannelPortCount_Object = MibTableColumn
sysLaPortChannelPortCount = _SysLaPortChannelPortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 6),
    _SysLaPortChannelPortCount_Type()
)
sysLaPortChannelPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaPortChannelPortCount.setStatus("current")
_SysLaPortChannelActivePortCount_Type = Integer32
_SysLaPortChannelActivePortCount_Object = MibTableColumn
sysLaPortChannelActivePortCount = _SysLaPortChannelActivePortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 7),
    _SysLaPortChannelActivePortCount_Type()
)
sysLaPortChannelActivePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaPortChannelActivePortCount.setStatus("current")


class _SysLaPortChannelSelectionPolicy_Type(Integer32):
    """Custom type sysLaPortChannelSelectionPolicy based on Integer32"""
    defaultValue = 3

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
        *(("ipDst", 5),
          ("ipSrc", 4),
          ("ipSrcDst", 6),
          ("macDst", 2),
          ("macSrc", 1),
          ("macSrcDst", 3),
          ("vlanId", 7))
    )


_SysLaPortChannelSelectionPolicy_Type.__name__ = "Integer32"
_SysLaPortChannelSelectionPolicy_Object = MibTableColumn
sysLaPortChannelSelectionPolicy = _SysLaPortChannelSelectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 8),
    _SysLaPortChannelSelectionPolicy_Type()
)
sysLaPortChannelSelectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortChannelSelectionPolicy.setStatus("current")


class _SysLaPortChannelDefaultPortIndex_Type(InterfaceIndexOrZero):
    """Custom type sysLaPortChannelDefaultPortIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_SysLaPortChannelDefaultPortIndex_Object = MibTableColumn
sysLaPortChannelDefaultPortIndex = _SysLaPortChannelDefaultPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 2, 1, 1, 9),
    _SysLaPortChannelDefaultPortIndex_Type()
)
sysLaPortChannelDefaultPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortChannelDefaultPortIndex.setStatus("current")
_SysLaPort_ObjectIdentity = ObjectIdentity
sysLaPort = _SysLaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3)
)
_SysLaPortTable_Object = MibTable
sysLaPortTable = _SysLaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1)
)
if mibBuilder.loadTexts:
    sysLaPortTable.setStatus("current")
_SysLaPortEntry_Object = MibTableRow
sysLaPortEntry = _SysLaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1)
)
sysLaPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysLaPortIndex"),
)
if mibBuilder.loadTexts:
    sysLaPortEntry.setStatus("current")
_SysLaPortIndex_Type = InterfaceIndex
_SysLaPortIndex_Object = MibTableColumn
sysLaPortIndex = _SysLaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 1),
    _SysLaPortIndex_Type()
)
sysLaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLaPortIndex.setStatus("current")
_SysLaPortMode_Type = PortLaMode
_SysLaPortMode_Object = MibTableColumn
sysLaPortMode = _SysLaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 2),
    _SysLaPortMode_Type()
)
sysLaPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortMode.setStatus("current")


class _SysLaPortBundleState_Type(Integer32):
    """Custom type sysLaPortBundleState based on Integer32"""
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
        *(("down", 2),
          ("standby", 1),
          ("upInBndl", 0),
          ("upIndividual", 3))
    )


_SysLaPortBundleState_Type.__name__ = "Integer32"
_SysLaPortBundleState_Object = MibTableColumn
sysLaPortBundleState = _SysLaPortBundleState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 3),
    _SysLaPortBundleState_Type()
)
sysLaPortBundleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaPortBundleState.setStatus("current")
_SysLaPortActorResetAdminState_Type = LacpState
_SysLaPortActorResetAdminState_Object = MibTableColumn
sysLaPortActorResetAdminState = _SysLaPortActorResetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 4),
    _SysLaPortActorResetAdminState_Type()
)
sysLaPortActorResetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortActorResetAdminState.setStatus("current")


class _SysLaPortAggregateWaitTime_Type(TimeTicks):
    """Custom type sysLaPortAggregateWaitTime based on TimeTicks"""
    defaultValue = 2


_SysLaPortAggregateWaitTime_Object = MibTableColumn
sysLaPortAggregateWaitTime = _SysLaPortAggregateWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 5),
    _SysLaPortAggregateWaitTime_Type()
)
sysLaPortAggregateWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortAggregateWaitTime.setStatus("current")
_SysLaPortPartnerResetAdminState_Type = LacpState
_SysLaPortPartnerResetAdminState_Object = MibTableColumn
sysLaPortPartnerResetAdminState = _SysLaPortPartnerResetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 6),
    _SysLaPortPartnerResetAdminState_Type()
)
sysLaPortPartnerResetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortPartnerResetAdminState.setStatus("current")


class _SysLaPortActorAdminPort_Type(Integer32):
    """Custom type sysLaPortActorAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLaPortActorAdminPort_Type.__name__ = "Integer32"
_SysLaPortActorAdminPort_Object = MibTableColumn
sysLaPortActorAdminPort = _SysLaPortActorAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 7),
    _SysLaPortActorAdminPort_Type()
)
sysLaPortActorAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortActorAdminPort.setStatus("current")
_SysLaPortRestoreMtu_Type = Integer32
_SysLaPortRestoreMtu_Object = MibTableColumn
sysLaPortRestoreMtu = _SysLaPortRestoreMtu_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 8),
    _SysLaPortRestoreMtu_Type()
)
sysLaPortRestoreMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLaPortRestoreMtu.setStatus("current")


class _SysLaPortSelectAggregator_Type(Integer32):
    """Custom type sysLaPortSelectAggregator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_SysLaPortSelectAggregator_Type.__name__ = "Integer32"
_SysLaPortSelectAggregator_Object = MibTableColumn
sysLaPortSelectAggregator = _SysLaPortSelectAggregator_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 63, 3, 1, 1, 9),
    _SysLaPortSelectAggregator_Type()
)
sysLaPortSelectAggregator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLaPortSelectAggregator.setStatus("current")
_L2Pnac_ObjectIdentity = ObjectIdentity
l2Pnac = _L2Pnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64)
)
_SysPnacPaeSystem_ObjectIdentity = ObjectIdentity
sysPnacPaeSystem = _SysPnacPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1)
)


class _SysPnacSystemControl_Type(Integer32):
    """Custom type sysPnacSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("start", 1))
    )


_SysPnacSystemControl_Type.__name__ = "Integer32"
_SysPnacSystemControl_Object = MibScalar
sysPnacSystemControl = _SysPnacSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 1),
    _SysPnacSystemControl_Type()
)
sysPnacSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacSystemControl.setStatus("current")
_SysPnacAuthenticServer_Type = AuthenticMethod
_SysPnacAuthenticServer_Object = MibScalar
sysPnacAuthenticServer = _SysPnacAuthenticServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 3),
    _SysPnacAuthenticServer_Type()
)
sysPnacAuthenticServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacAuthenticServer.setStatus("current")
_SysPnacNasId_Type = DisplayString
_SysPnacNasId_Object = MibScalar
sysPnacNasId = _SysPnacNasId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 4),
    _SysPnacNasId_Type()
)
sysPnacNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacNasId.setStatus("current")
_SysPnacPaePortTable_Object = MibTable
sysPnacPaePortTable = _SysPnacPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5)
)
if mibBuilder.loadTexts:
    sysPnacPaePortTable.setStatus("current")
_SysPnacPaePortEntry_Object = MibTableRow
sysPnacPaePortEntry = _SysPnacPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1)
)
sysPnacPaePortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysPnacPaePortNumber"),
)
if mibBuilder.loadTexts:
    sysPnacPaePortEntry.setStatus("current")
_SysPnacPaePortNumber_Type = InterfaceIndex
_SysPnacPaePortNumber_Object = MibTableColumn
sysPnacPaePortNumber = _SysPnacPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 1),
    _SysPnacPaePortNumber_Type()
)
sysPnacPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysPnacPaePortNumber.setStatus("current")
_SysPnacPaePortStatus_Type = PaeControlledPortStatus
_SysPnacPaePortStatus_Object = MibTableColumn
sysPnacPaePortStatus = _SysPnacPaePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 6),
    _SysPnacPaePortStatus_Type()
)
sysPnacPaePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPnacPaePortStatus.setStatus("current")


class _SysPnacPaeMultiAuthEnable_Type(Integer32):
    """Custom type sysPnacPaeMultiAuthEnable based on Integer32"""
    defaultValue = 2

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


_SysPnacPaeMultiAuthEnable_Type.__name__ = "Integer32"
_SysPnacPaeMultiAuthEnable_Object = MibTableColumn
sysPnacPaeMultiAuthEnable = _SysPnacPaeMultiAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 7),
    _SysPnacPaeMultiAuthEnable_Type()
)
sysPnacPaeMultiAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacPaeMultiAuthEnable.setStatus("current")
_SysPnacPaeProtocolMode_Type = Integer32
_SysPnacPaeProtocolMode_Object = MibTableColumn
sysPnacPaeProtocolMode = _SysPnacPaeProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 8),
    _SysPnacPaeProtocolMode_Type()
)
sysPnacPaeProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacPaeProtocolMode.setStatus("current")


class _SysPnacPaePiggybackMode_Type(Integer32):
    """Custom type sysPnacPaePiggybackMode based on Integer32"""
    defaultValue = 2

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


_SysPnacPaePiggybackMode_Type.__name__ = "Integer32"
_SysPnacPaePiggybackMode_Object = MibTableColumn
sysPnacPaePiggybackMode = _SysPnacPaePiggybackMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 9),
    _SysPnacPaePiggybackMode_Type()
)
sysPnacPaePiggybackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacPaePiggybackMode.setStatus("current")


class _SysPnacPaeVlanAssignment_Type(Integer32):
    """Custom type sysPnacPaeVlanAssignment based on Integer32"""
    defaultValue = 2

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


_SysPnacPaeVlanAssignment_Type.__name__ = "Integer32"
_SysPnacPaeVlanAssignment_Object = MibTableColumn
sysPnacPaeVlanAssignment = _SysPnacPaeVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 10),
    _SysPnacPaeVlanAssignment_Type()
)
sysPnacPaeVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacPaeVlanAssignment.setStatus("current")


class _SysPnacPaeSecureVlan_Type(Integer32):
    """Custom type sysPnacPaeSecureVlan based on Integer32"""
    defaultValue = 2

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


_SysPnacPaeSecureVlan_Type.__name__ = "Integer32"
_SysPnacPaeSecureVlan_Object = MibTableColumn
sysPnacPaeSecureVlan = _SysPnacPaeSecureVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 5, 1, 11),
    _SysPnacPaeSecureVlan_Type()
)
sysPnacPaeSecureVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacPaeSecureVlan.setStatus("current")


class _SysPnacModuleOperStatus_Type(Integer32):
    """Custom type sysPnacModuleOperStatus based on Integer32"""
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


_SysPnacModuleOperStatus_Type.__name__ = "Integer32"
_SysPnacModuleOperStatus_Object = MibScalar
sysPnacModuleOperStatus = _SysPnacModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 1, 6),
    _SysPnacModuleOperStatus_Type()
)
sysPnacModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPnacModuleOperStatus.setStatus("current")
_SysPnacAuthServer_ObjectIdentity = ObjectIdentity
sysPnacAuthServer = _SysPnacAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3)
)
_SysPnacASUserConfigTable_Object = MibTable
sysPnacASUserConfigTable = _SysPnacASUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1)
)
if mibBuilder.loadTexts:
    sysPnacASUserConfigTable.setStatus("current")
_SysPnacASUserConfigEntry_Object = MibTableRow
sysPnacASUserConfigEntry = _SysPnacASUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1)
)
sysPnacASUserConfigEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysPnacASUserConfigUserName"),
)
if mibBuilder.loadTexts:
    sysPnacASUserConfigEntry.setStatus("current")


class _SysPnacASUserConfigUserName_Type(OctetString):
    """Custom type sysPnacASUserConfigUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 115),
    )


_SysPnacASUserConfigUserName_Type.__name__ = "OctetString"
_SysPnacASUserConfigUserName_Object = MibTableColumn
sysPnacASUserConfigUserName = _SysPnacASUserConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 1),
    _SysPnacASUserConfigUserName_Type()
)
sysPnacASUserConfigUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysPnacASUserConfigUserName.setStatus("current")
_SysPnacASUserConfigPassword_Type = DisplayString
_SysPnacASUserConfigPassword_Object = MibTableColumn
sysPnacASUserConfigPassword = _SysPnacASUserConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 2),
    _SysPnacASUserConfigPassword_Type()
)
sysPnacASUserConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacASUserConfigPassword.setStatus("current")
_SysPnacASUserConfigAuthProtocol_Type = Unsigned32
_SysPnacASUserConfigAuthProtocol_Object = MibTableColumn
sysPnacASUserConfigAuthProtocol = _SysPnacASUserConfigAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 3),
    _SysPnacASUserConfigAuthProtocol_Type()
)
sysPnacASUserConfigAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPnacASUserConfigAuthProtocol.setStatus("current")
_SysPnacASUserConfigAuthTimeout_Type = Unsigned32
_SysPnacASUserConfigAuthTimeout_Object = MibTableColumn
sysPnacASUserConfigAuthTimeout = _SysPnacASUserConfigAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 4),
    _SysPnacASUserConfigAuthTimeout_Type()
)
sysPnacASUserConfigAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacASUserConfigAuthTimeout.setStatus("current")
_SysPnacASUserConfigPortList_Type = PortList
_SysPnacASUserConfigPortList_Object = MibTableColumn
sysPnacASUserConfigPortList = _SysPnacASUserConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 5),
    _SysPnacASUserConfigPortList_Type()
)
sysPnacASUserConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacASUserConfigPortList.setStatus("current")
_SysPnacASUserConfigPermission_Type = PermissionType
_SysPnacASUserConfigPermission_Object = MibTableColumn
sysPnacASUserConfigPermission = _SysPnacASUserConfigPermission_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 6),
    _SysPnacASUserConfigPermission_Type()
)
sysPnacASUserConfigPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacASUserConfigPermission.setStatus("current")
_SysPnacASUserConfigDynamicVlanID_Type = Unsigned32
_SysPnacASUserConfigDynamicVlanID_Object = MibTableColumn
sysPnacASUserConfigDynamicVlanID = _SysPnacASUserConfigDynamicVlanID_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 7),
    _SysPnacASUserConfigDynamicVlanID_Type()
)
sysPnacASUserConfigDynamicVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacASUserConfigDynamicVlanID.setStatus("current")
_SysPnacASUserConfigRowStatus_Type = RowStatus
_SysPnacASUserConfigRowStatus_Object = MibTableColumn
sysPnacASUserConfigRowStatus = _SysPnacASUserConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 3, 1, 1, 8),
    _SysPnacASUserConfigRowStatus_Type()
)
sysPnacASUserConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysPnacASUserConfigRowStatus.setStatus("current")
_SysGuestVlan_ObjectIdentity = ObjectIdentity
sysGuestVlan = _SysGuestVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 4)
)
_SysPnacGuestVlanTable_Object = MibTable
sysPnacGuestVlanTable = _SysPnacGuestVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 4, 1)
)
if mibBuilder.loadTexts:
    sysPnacGuestVlanTable.setStatus("current")
_SysPnacGuestVlanEntry_Object = MibTableRow
sysPnacGuestVlanEntry = _SysPnacGuestVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 4, 1, 1)
)
sysPnacGuestVlanEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysPnacPaePortNo"),
)
if mibBuilder.loadTexts:
    sysPnacGuestVlanEntry.setStatus("current")


class _SysPnacPaePortNo_Type(Integer32):
    """Custom type sysPnacPaePortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysPnacPaePortNo_Type.__name__ = "Integer32"
_SysPnacPaePortNo_Object = MibTableColumn
sysPnacPaePortNo = _SysPnacPaePortNo_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 4, 1, 1, 1),
    _SysPnacPaePortNo_Type()
)
sysPnacPaePortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPnacPaePortNo.setStatus("current")
_SysPnacGuestVlanId_Type = Integer32
_SysPnacGuestVlanId_Object = MibTableColumn
sysPnacGuestVlanId = _SysPnacGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 64, 4, 1, 1, 2),
    _SysPnacGuestVlanId_Type()
)
sysPnacGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPnacGuestVlanId.setStatus("current")
_L2System_ObjectIdentity = ObjectIdentity
l2System = _L2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81)
)
_SysSystemInfo_ObjectIdentity = ObjectIdentity
sysSystemInfo = _SysSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1)
)


class _SysSwitchName_Type(DisplayString):
    """Custom type sysSwitchName based on DisplayString"""
    defaultValue = OctetString("SysName")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysSwitchName_Type.__name__ = "DisplayString"
_SysSwitchName_Object = MibScalar
sysSwitchName = _SysSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 1),
    _SysSwitchName_Type()
)
sysSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSwitchName.setStatus("current")


class _SysHardwareVersion_Type(DisplayString):
    """Custom type sysHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysHardwareVersion_Type.__name__ = "DisplayString"
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 2),
    _SysHardwareVersion_Type()
)
sysHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersion.setStatus("current")


class _SysFirmwareVersion_Type(DisplayString):
    """Custom type sysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysFirmwareVersion_Type.__name__ = "DisplayString"
_SysFirmwareVersion_Object = MibScalar
sysFirmwareVersion = _SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 3),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("current")


class _SysDefaultIpAddrCfgMode_Type(Integer32):
    """Custom type sysDefaultIpAddrCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 1))
    )


_SysDefaultIpAddrCfgMode_Type.__name__ = "Integer32"
_SysDefaultIpAddrCfgMode_Object = MibScalar
sysDefaultIpAddrCfgMode = _SysDefaultIpAddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 4),
    _SysDefaultIpAddrCfgMode_Type()
)
sysDefaultIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultIpAddrCfgMode.setStatus("current")
_SysDefaultIpAddr_Type = IpAddress
_SysDefaultIpAddr_Object = MibScalar
sysDefaultIpAddr = _SysDefaultIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 5),
    _SysDefaultIpAddr_Type()
)
sysDefaultIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultIpAddr.setStatus("current")
_SysDefaultIpSubnetMask_Type = IpAddress
_SysDefaultIpSubnetMask_Object = MibScalar
sysDefaultIpSubnetMask = _SysDefaultIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 6),
    _SysDefaultIpSubnetMask_Type()
)
sysDefaultIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultIpSubnetMask.setStatus("current")


class _SysRestart_Type(TruthValue):
    """Custom type sysRestart based on TruthValue"""


_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 9),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysConfigSaveOption_Type(Integer32):
    """Custom type sysConfigSaveOption based on Integer32"""
    defaultValue = 4

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
        *(("flashSave", 2),
          ("noSave", 1),
          ("remoteSave", 3),
          ("startupConfig", 4))
    )


_SysConfigSaveOption_Type.__name__ = "Integer32"
_SysConfigSaveOption_Object = MibScalar
sysConfigSaveOption = _SysConfigSaveOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 10),
    _SysConfigSaveOption_Type()
)
sysConfigSaveOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigSaveOption.setStatus("current")
_SysConfigSaveIpAddr_Type = IpAddress
_SysConfigSaveIpAddr_Object = MibScalar
sysConfigSaveIpAddr = _SysConfigSaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 11),
    _SysConfigSaveIpAddr_Type()
)
sysConfigSaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigSaveIpAddr.setStatus("current")


class _SysConfigSaveFileName_Type(DisplayString):
    """Custom type sysConfigSaveFileName based on DisplayString"""
    defaultValue = OctetString("iss.conf")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysConfigSaveFileName_Type.__name__ = "DisplayString"
_SysConfigSaveFileName_Object = MibScalar
sysConfigSaveFileName = _SysConfigSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 12),
    _SysConfigSaveFileName_Type()
)
sysConfigSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigSaveFileName.setStatus("current")


class _SysInitiateConfigSave_Type(TruthValue):
    """Custom type sysInitiateConfigSave based on TruthValue"""


_SysInitiateConfigSave_Object = MibScalar
sysInitiateConfigSave = _SysInitiateConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 13),
    _SysInitiateConfigSave_Type()
)
sysInitiateConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitiateConfigSave.setStatus("current")


class _SysConfigSaveStatus_Type(Integer32):
    """Custom type sysConfigSaveStatus based on Integer32"""
    defaultValue = 4

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
        *(("notInitiated", 4),
          ("saveFailed", 3),
          ("saveInProgress", 1),
          ("saveSuccessful", 2))
    )


_SysConfigSaveStatus_Type.__name__ = "Integer32"
_SysConfigSaveStatus_Object = MibScalar
sysConfigSaveStatus = _SysConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 14),
    _SysConfigSaveStatus_Type()
)
sysConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigSaveStatus.setStatus("current")


class _SysConfigRestoreOption_Type(Integer32):
    """Custom type sysConfigRestoreOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestore", 1),
          ("restore", 2))
    )


_SysConfigRestoreOption_Type.__name__ = "Integer32"
_SysConfigRestoreOption_Object = MibScalar
sysConfigRestoreOption = _SysConfigRestoreOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 15),
    _SysConfigRestoreOption_Type()
)
sysConfigRestoreOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigRestoreOption.setStatus("current")
_SysRemoteConfigRestoreIpAddr_Type = IpAddress
_SysRemoteConfigRestoreIpAddr_Object = MibScalar
sysRemoteConfigRestoreIpAddr = _SysRemoteConfigRestoreIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 16),
    _SysRemoteConfigRestoreIpAddr_Type()
)
sysRemoteConfigRestoreIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRemoteConfigRestoreIpAddr.setStatus("current")


class _SysConfigRestoreFileName_Type(DisplayString):
    """Custom type sysConfigRestoreFileName based on DisplayString"""
    defaultValue = OctetString("iss.conf")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysConfigRestoreFileName_Type.__name__ = "DisplayString"
_SysConfigRestoreFileName_Object = MibScalar
sysConfigRestoreFileName = _SysConfigRestoreFileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 17),
    _SysConfigRestoreFileName_Type()
)
sysConfigRestoreFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigRestoreFileName.setStatus("current")


class _SysInitiateRemoteConfigRestore_Type(TruthValue):
    """Custom type sysInitiateRemoteConfigRestore based on TruthValue"""


_SysInitiateRemoteConfigRestore_Object = MibScalar
sysInitiateRemoteConfigRestore = _SysInitiateRemoteConfigRestore_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 18),
    _SysInitiateRemoteConfigRestore_Type()
)
sysInitiateRemoteConfigRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitiateRemoteConfigRestore.setStatus("current")


class _SysConfigRestoreStatus_Type(Integer32):
    """Custom type sysConfigRestoreStatus based on Integer32"""
    defaultValue = 4

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
        *(("notInitiated", 4),
          ("restoreFailed", 3),
          ("restoreInprogress", 1),
          ("restoreSuccessful", 2))
    )


_SysConfigRestoreStatus_Type.__name__ = "Integer32"
_SysConfigRestoreStatus_Object = MibScalar
sysConfigRestoreStatus = _SysConfigRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 19),
    _SysConfigRestoreStatus_Type()
)
sysConfigRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigRestoreStatus.setStatus("current")
_SysDlFirmwareFromIp_Type = IpAddress
_SysDlFirmwareFromIp_Object = MibScalar
sysDlFirmwareFromIp = _SysDlFirmwareFromIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 20),
    _SysDlFirmwareFromIp_Type()
)
sysDlFirmwareFromIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDlFirmwareFromIp.setStatus("current")


class _SysDlFirmwareName_Type(DisplayString):
    """Custom type sysDlFirmwareName based on DisplayString"""
    defaultValue = OctetString("firmware.hex")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysDlFirmwareName_Type.__name__ = "DisplayString"
_SysDlFirmwareName_Object = MibScalar
sysDlFirmwareName = _SysDlFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 21),
    _SysDlFirmwareName_Type()
)
sysDlFirmwareName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDlFirmwareName.setStatus("current")
_SysInitiateDlFirmware_Type = TruthValue
_SysInitiateDlFirmware_Object = MibScalar
sysInitiateDlFirmware = _SysInitiateDlFirmware_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 22),
    _SysInitiateDlFirmware_Type()
)
sysInitiateDlFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitiateDlFirmware.setStatus("current")


class _SysLoggingOption_Type(Integer32):
    """Custom type sysLoggingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("file", 2))
    )


_SysLoggingOption_Type.__name__ = "Integer32"
_SysLoggingOption_Object = MibScalar
sysLoggingOption = _SysLoggingOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 23),
    _SysLoggingOption_Type()
)
sysLoggingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoggingOption.setStatus("current")
_SysUploadLogFileToIp_Type = IpAddress
_SysUploadLogFileToIp_Object = MibScalar
sysUploadLogFileToIp = _SysUploadLogFileToIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 24),
    _SysUploadLogFileToIp_Type()
)
sysUploadLogFileToIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUploadLogFileToIp.setStatus("current")


class _SysLogFileName_Type(DisplayString):
    """Custom type sysLogFileName based on DisplayString"""
    defaultValue = OctetString("iss.log")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysLogFileName_Type.__name__ = "DisplayString"
_SysLogFileName_Object = MibScalar
sysLogFileName = _SysLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 25),
    _SysLogFileName_Type()
)
sysLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFileName.setStatus("current")
_SysInitiateUlLogFile_Type = TruthValue
_SysInitiateUlLogFile_Object = MibScalar
sysInitiateUlLogFile = _SysInitiateUlLogFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 26),
    _SysInitiateUlLogFile_Type()
)
sysInitiateUlLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitiateUlLogFile.setStatus("current")


class _SysSysContact_Type(DisplayString):
    """Custom type sysSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_SysSysContact_Type.__name__ = "DisplayString"
_SysSysContact_Object = MibScalar
sysSysContact = _SysSysContact_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 29),
    _SysSysContact_Type()
)
sysSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSysContact.setStatus("current")


class _SysSysLocation_Type(DisplayString):
    """Custom type sysSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_SysSysLocation_Type.__name__ = "DisplayString"
_SysSysLocation_Object = MibScalar
sysSysLocation = _SysSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 30),
    _SysSysLocation_Type()
)
sysSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSysLocation.setStatus("current")


class _SysLoginAuthentication_Type(Integer32):
    """Custom type sysLoginAuthentication based on Integer32"""
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
          ("remoteRadius", 2),
          ("remoteTacacs", 3))
    )


_SysLoginAuthentication_Type.__name__ = "Integer32"
_SysLoginAuthentication_Object = MibScalar
sysLoginAuthentication = _SysLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 31),
    _SysLoginAuthentication_Type()
)
sysLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginAuthentication.setStatus("current")


class _SysSwitchBaseMacAddress_Type(MacAddress):
    """Custom type sysSwitchBaseMacAddress based on MacAddress"""
    defaultHexValue = "000102030405"


_SysSwitchBaseMacAddress_Object = MibScalar
sysSwitchBaseMacAddress = _SysSwitchBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 32),
    _SysSwitchBaseMacAddress_Type()
)
sysSwitchBaseMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSwitchBaseMacAddress.setStatus("current")


class _SysSwitchDate_Type(DisplayString):
    """Custom type sysSwitchDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_SysSwitchDate_Type.__name__ = "DisplayString"
_SysSwitchDate_Object = MibScalar
sysSwitchDate = _SysSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 34),
    _SysSwitchDate_Type()
)
sysSwitchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwitchDate.setStatus("current")


class _SysHttpPort_Type(Integer32):
    """Custom type sysHttpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysHttpPort_Type.__name__ = "Integer32"
_SysHttpPort_Object = MibScalar
sysHttpPort = _SysHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 37),
    _SysHttpPort_Type()
)
sysHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHttpPort.setStatus("current")


class _SysHttpStatus_Type(Integer32):
    """Custom type sysHttpStatus based on Integer32"""
    defaultValue = 1

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


_SysHttpStatus_Type.__name__ = "Integer32"
_SysHttpStatus_Object = MibScalar
sysHttpStatus = _SysHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 38),
    _SysHttpStatus_Type()
)
sysHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHttpStatus.setStatus("current")


class _SysDefaultVlanId_Type(Integer32):
    """Custom type sysDefaultVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysDefaultVlanId_Type.__name__ = "Integer32"
_SysDefaultVlanId_Object = MibScalar
sysDefaultVlanId = _SysDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 41),
    _SysDefaultVlanId_Type()
)
sysDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultVlanId.setStatus("current")


class _SysWebAutoTimeoutInterval_Type(Integer32):
    """Custom type sysWebAutoTimeoutInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 3600),
    )


_SysWebAutoTimeoutInterval_Type.__name__ = "Integer32"
_SysWebAutoTimeoutInterval_Object = MibScalar
sysWebAutoTimeoutInterval = _SysWebAutoTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 42),
    _SysWebAutoTimeoutInterval_Type()
)
sysWebAutoTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysWebAutoTimeoutInterval.setStatus("current")


class _SysCliAutoTimeoutInterval_Type(Integer32):
    """Custom type sysCliAutoTimeoutInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18000),
    )


_SysCliAutoTimeoutInterval_Type.__name__ = "Integer32"
_SysCliAutoTimeoutInterval_Object = MibScalar
sysCliAutoTimeoutInterval = _SysCliAutoTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 43),
    _SysCliAutoTimeoutInterval_Type()
)
sysCliAutoTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCliAutoTimeoutInterval.setStatus("current")


class _SysCpuPolicerStatus_Type(Integer32):
    """Custom type sysCpuPolicerStatus based on Integer32"""
    defaultValue = 1

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


_SysCpuPolicerStatus_Type.__name__ = "Integer32"
_SysCpuPolicerStatus_Object = MibScalar
sysCpuPolicerStatus = _SysCpuPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 44),
    _SysCpuPolicerStatus_Type()
)
sysCpuPolicerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCpuPolicerStatus.setStatus("current")


class _SysLedEcoModeStatus_Type(Integer32):
    """Custom type sysLedEcoModeStatus based on Integer32"""
    defaultValue = 1

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


_SysLedEcoModeStatus_Type.__name__ = "Integer32"
_SysLedEcoModeStatus_Object = MibScalar
sysLedEcoModeStatus = _SysLedEcoModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 45),
    _SysLedEcoModeStatus_Type()
)
sysLedEcoModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLedEcoModeStatus.setStatus("current")


class _SysPowerSavingEnable_Type(Integer32):
    """Custom type sysPowerSavingEnable based on Integer32"""
    defaultValue = 1

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


_SysPowerSavingEnable_Type.__name__ = "Integer32"
_SysPowerSavingEnable_Object = MibScalar
sysPowerSavingEnable = _SysPowerSavingEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 62),
    _SysPowerSavingEnable_Type()
)
sysPowerSavingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPowerSavingEnable.setStatus("current")


class _SysDhcpAutoConfiguration_Type(Integer32):
    """Custom type sysDhcpAutoConfiguration based on Integer32"""
    defaultValue = 2

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


_SysDhcpAutoConfiguration_Type.__name__ = "Integer32"
_SysDhcpAutoConfiguration_Object = MibScalar
sysDhcpAutoConfiguration = _SysDhcpAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 63),
    _SysDhcpAutoConfiguration_Type()
)
sysDhcpAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpAutoConfiguration.setStatus("current")


class _SysAsyVLANEnable_Type(Integer32):
    """Custom type sysAsyVLANEnable based on Integer32"""
    defaultValue = 1

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


_SysAsyVLANEnable_Type.__name__ = "Integer32"
_SysAsyVLANEnable_Object = MibScalar
sysAsyVLANEnable = _SysAsyVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 64),
    _SysAsyVLANEnable_Type()
)
sysAsyVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAsyVLANEnable.setStatus("current")


class _IssCosEnable_Type(Integer32):
    """Custom type issCosEnable based on Integer32"""
    defaultValue = 1

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


_IssCosEnable_Type.__name__ = "Integer32"
_IssCosEnable_Object = MibScalar
issCosEnable = _IssCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 65),
    _IssCosEnable_Type()
)
issCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issCosEnable.setStatus("current")


class _SysTrapEnable_Type(Integer32):
    """Custom type sysTrapEnable based on Integer32"""
    defaultValue = 1

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


_SysTrapEnable_Type.__name__ = "Integer32"
_SysTrapEnable_Object = MibScalar
sysTrapEnable = _SysTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 66),
    _SysTrapEnable_Type()
)
sysTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapEnable.setStatus("current")


class _SysFDResetStateEnable_Type(Integer32):
    """Custom type sysFDResetStateEnable based on Integer32"""
    defaultValue = 1

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


_SysFDResetStateEnable_Type.__name__ = "Integer32"
_SysFDResetStateEnable_Object = MibScalar
sysFDResetStateEnable = _SysFDResetStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 67),
    _SysFDResetStateEnable_Type()
)
sysFDResetStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFDResetStateEnable.setStatus("current")


class _SysFDRInputPw_Type(DisplayString):
    """Custom type sysFDRInputPw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysFDRInputPw_Type.__name__ = "DisplayString"
_SysFDRInputPw_Object = MibScalar
sysFDRInputPw = _SysFDRInputPw_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 1, 68),
    _SysFDRInputPw_Type()
)
sysFDRInputPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFDRInputPw.setStatus("current")
_SysConfigControl_ObjectIdentity = ObjectIdentity
sysConfigControl = _SysConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2)
)
_SysConfigCtrlTable_Object = MibTable
sysConfigCtrlTable = _SysConfigCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 1)
)
if mibBuilder.loadTexts:
    sysConfigCtrlTable.setStatus("current")
_SysConfigCtrlEntry_Object = MibTableRow
sysConfigCtrlEntry = _SysConfigCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 1, 1)
)
sysConfigCtrlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysConfigCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysConfigCtrlEntry.setStatus("current")


class _SysConfigCtrlIndex_Type(Integer32):
    """Custom type sysConfigCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysConfigCtrlIndex_Type.__name__ = "Integer32"
_SysConfigCtrlIndex_Object = MibTableColumn
sysConfigCtrlIndex = _SysConfigCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 1, 1, 1),
    _SysConfigCtrlIndex_Type()
)
sysConfigCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysConfigCtrlIndex.setStatus("current")


class _SysConfigCtrlEgressStatus_Type(Integer32):
    """Custom type sysConfigCtrlEgressStatus based on Integer32"""
    defaultValue = 1

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


_SysConfigCtrlEgressStatus_Type.__name__ = "Integer32"
_SysConfigCtrlEgressStatus_Object = MibTableColumn
sysConfigCtrlEgressStatus = _SysConfigCtrlEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 1, 1, 2),
    _SysConfigCtrlEgressStatus_Type()
)
sysConfigCtrlEgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigCtrlEgressStatus.setStatus("current")


class _SysConfigCtrlStatsCollection_Type(Integer32):
    """Custom type sysConfigCtrlStatsCollection based on Integer32"""
    defaultValue = 1

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


_SysConfigCtrlStatsCollection_Type.__name__ = "Integer32"
_SysConfigCtrlStatsCollection_Object = MibTableColumn
sysConfigCtrlStatsCollection = _SysConfigCtrlStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 1, 1, 3),
    _SysConfigCtrlStatsCollection_Type()
)
sysConfigCtrlStatsCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigCtrlStatsCollection.setStatus("current")


class _SysConfigCtrlStatus_Type(Integer32):
    """Custom type sysConfigCtrlStatus based on Integer32"""
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


_SysConfigCtrlStatus_Type.__name__ = "Integer32"
_SysConfigCtrlStatus_Object = MibTableColumn
sysConfigCtrlStatus = _SysConfigCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 1, 1, 4),
    _SysConfigCtrlStatus_Type()
)
sysConfigCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigCtrlStatus.setStatus("current")
_SysPortCtrlTable_Object = MibTable
sysPortCtrlTable = _SysPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2)
)
if mibBuilder.loadTexts:
    sysPortCtrlTable.setStatus("current")
_SysPortCtrlEntry_Object = MibTableRow
sysPortCtrlEntry = _SysPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1)
)
sysPortCtrlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysPortCtrlEntry.setStatus("current")


class _SysPortCtrlIndex_Type(Integer32):
    """Custom type sysPortCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysPortCtrlIndex_Type.__name__ = "Integer32"
_SysPortCtrlIndex_Object = MibTableColumn
sysPortCtrlIndex = _SysPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 1),
    _SysPortCtrlIndex_Type()
)
sysPortCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysPortCtrlIndex.setStatus("current")


class _SysPortCtrlMode_Type(Integer32):
    """Custom type sysPortCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("noNegotiation", 2))
    )


_SysPortCtrlMode_Type.__name__ = "Integer32"
_SysPortCtrlMode_Object = MibTableColumn
sysPortCtrlMode = _SysPortCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 2),
    _SysPortCtrlMode_Type()
)
sysPortCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlMode.setStatus("current")


class _SysPortCtrlDuplex_Type(Integer32):
    """Custom type sysPortCtrlDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_SysPortCtrlDuplex_Type.__name__ = "Integer32"
_SysPortCtrlDuplex_Object = MibTableColumn
sysPortCtrlDuplex = _SysPortCtrlDuplex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 3),
    _SysPortCtrlDuplex_Type()
)
sysPortCtrlDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlDuplex.setStatus("current")


class _SysPortCtrlSpeed_Type(Integer32):
    """Custom type sysPortCtrlSpeed based on Integer32"""
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
        *(("hundredMBPS", 2),
          ("oneGB", 3),
          ("tenGB", 4),
          ("tenMBPS", 1))
    )


_SysPortCtrlSpeed_Type.__name__ = "Integer32"
_SysPortCtrlSpeed_Object = MibTableColumn
sysPortCtrlSpeed = _SysPortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 4),
    _SysPortCtrlSpeed_Type()
)
sysPortCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlSpeed.setStatus("current")


class _SysPortCtrlFlowControl_Type(Integer32):
    """Custom type sysPortCtrlFlowControl based on Integer32"""
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


_SysPortCtrlFlowControl_Type.__name__ = "Integer32"
_SysPortCtrlFlowControl_Object = MibTableColumn
sysPortCtrlFlowControl = _SysPortCtrlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 5),
    _SysPortCtrlFlowControl_Type()
)
sysPortCtrlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlFlowControl.setStatus("current")


class _SysPortCtrlMDI_Type(Integer32):
    """Custom type sysPortCtrlMDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_SysPortCtrlMDI_Type.__name__ = "Integer32"
_SysPortCtrlMDI_Object = MibTableColumn
sysPortCtrlMDI = _SysPortCtrlMDI_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 10),
    _SysPortCtrlMDI_Type()
)
sysPortCtrlMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlMDI.setStatus("current")


class _IssJumboFramePerPortEnable_Type(Integer32):
    """Custom type issJumboFramePerPortEnable based on Integer32"""
    defaultValue = 2

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


_IssJumboFramePerPortEnable_Type.__name__ = "Integer32"
_IssJumboFramePerPortEnable_Object = MibTableColumn
issJumboFramePerPortEnable = _IssJumboFramePerPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 11),
    _IssJumboFramePerPortEnable_Type()
)
issJumboFramePerPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issJumboFramePerPortEnable.setStatus("current")


class _IssJumboFramePerPortMtu_Type(Integer32):
    """Custom type issJumboFramePerPortMtu based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 10000),
    )


_IssJumboFramePerPortMtu_Type.__name__ = "Integer32"
_IssJumboFramePerPortMtu_Object = MibTableColumn
issJumboFramePerPortMtu = _IssJumboFramePerPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 12),
    _IssJumboFramePerPortMtu_Type()
)
issJumboFramePerPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issJumboFramePerPortMtu.setStatus("current")


class _SysPortCtrlEAPPassThrough_Type(Integer32):
    """Custom type sysPortCtrlEAPPassThrough based on Integer32"""
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


_SysPortCtrlEAPPassThrough_Type.__name__ = "Integer32"
_SysPortCtrlEAPPassThrough_Object = MibTableColumn
sysPortCtrlEAPPassThrough = _SysPortCtrlEAPPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 13),
    _SysPortCtrlEAPPassThrough_Type()
)
sysPortCtrlEAPPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlEAPPassThrough.setStatus("current")


class _SysPortCtrlBPDUPassThrough_Type(Integer32):
    """Custom type sysPortCtrlBPDUPassThrough based on Integer32"""
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


_SysPortCtrlBPDUPassThrough_Type.__name__ = "Integer32"
_SysPortCtrlBPDUPassThrough_Object = MibTableColumn
sysPortCtrlBPDUPassThrough = _SysPortCtrlBPDUPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 2, 2, 1, 14),
    _SysPortCtrlBPDUPassThrough_Type()
)
sysPortCtrlBPDUPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlBPDUPassThrough.setStatus("current")
_SysMirror_ObjectIdentity = ObjectIdentity
sysMirror = _SysMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3)
)


class _SysMirrorStatus_Type(Integer32):
    """Custom type sysMirrorStatus based on Integer32"""
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


_SysMirrorStatus_Type.__name__ = "Integer32"
_SysMirrorStatus_Object = MibScalar
sysMirrorStatus = _SysMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorToPort_Type = Integer32
_SysMirrorToPort_Object = MibScalar
sysMirrorToPort = _SysMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 2),
    _SysMirrorToPort_Type()
)
sysMirrorToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorToPort.setStatus("current")
_SysMirrorCtrlTable_Object = MibTable
sysMirrorCtrlTable = _SysMirrorCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 3)
)
if mibBuilder.loadTexts:
    sysMirrorCtrlTable.setStatus("current")
_SysMirrorCtrlEntry_Object = MibTableRow
sysMirrorCtrlEntry = _SysMirrorCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 3, 1)
)
sysMirrorCtrlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysMirrorCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysMirrorCtrlEntry.setStatus("current")


class _SysMirrorCtrlIndex_Type(Integer32):
    """Custom type sysMirrorCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysMirrorCtrlIndex_Type.__name__ = "Integer32"
_SysMirrorCtrlIndex_Object = MibTableColumn
sysMirrorCtrlIndex = _SysMirrorCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 3, 1, 1),
    _SysMirrorCtrlIndex_Type()
)
sysMirrorCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysMirrorCtrlIndex.setStatus("current")


class _SysMirrorCtrlIngressMirroring_Type(Integer32):
    """Custom type sysMirrorCtrlIngressMirroring based on Integer32"""
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


_SysMirrorCtrlIngressMirroring_Type.__name__ = "Integer32"
_SysMirrorCtrlIngressMirroring_Object = MibTableColumn
sysMirrorCtrlIngressMirroring = _SysMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 3, 1, 2),
    _SysMirrorCtrlIngressMirroring_Type()
)
sysMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlIngressMirroring.setStatus("current")


class _SysMirrorCtrlEgressMirroring_Type(Integer32):
    """Custom type sysMirrorCtrlEgressMirroring based on Integer32"""
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


_SysMirrorCtrlEgressMirroring_Type.__name__ = "Integer32"
_SysMirrorCtrlEgressMirroring_Object = MibTableColumn
sysMirrorCtrlEgressMirroring = _SysMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 3, 1, 3),
    _SysMirrorCtrlEgressMirroring_Type()
)
sysMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlEgressMirroring.setStatus("current")


class _SysMirrorCtrlStatus_Type(Integer32):
    """Custom type sysMirrorCtrlStatus based on Integer32"""
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


_SysMirrorCtrlStatus_Type.__name__ = "Integer32"
_SysMirrorCtrlStatus_Object = MibTableColumn
sysMirrorCtrlStatus = _SysMirrorCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 3, 3, 1, 4),
    _SysMirrorCtrlStatus_Type()
)
sysMirrorCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMirrorCtrlStatus.setStatus("current")
_SysRateControl_ObjectIdentity = ObjectIdentity
sysRateControl = _SysRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 4)
)
_SysRateCtrlTable_Object = MibTable
sysRateCtrlTable = _SysRateCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 4, 1)
)
if mibBuilder.loadTexts:
    sysRateCtrlTable.setStatus("current")
_SysRateCtrlEntry_Object = MibTableRow
sysRateCtrlEntry = _SysRateCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 4, 1, 1)
)
sysRateCtrlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysRateCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysRateCtrlEntry.setStatus("current")


class _SysRateCtrlIndex_Type(Integer32):
    """Custom type sysRateCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysRateCtrlIndex_Type.__name__ = "Integer32"
_SysRateCtrlIndex_Object = MibTableColumn
sysRateCtrlIndex = _SysRateCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 4, 1, 1, 1),
    _SysRateCtrlIndex_Type()
)
sysRateCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysRateCtrlIndex.setStatus("current")


class _SysRateCtrlEgressLimitValue_Type(Integer32):
    """Custom type sysRateCtrlEgressLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SysRateCtrlEgressLimitValue_Type.__name__ = "Integer32"
_SysRateCtrlEgressLimitValue_Object = MibTableColumn
sysRateCtrlEgressLimitValue = _SysRateCtrlEgressLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 4, 1, 1, 5),
    _SysRateCtrlEgressLimitValue_Type()
)
sysRateCtrlEgressLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRateCtrlEgressLimitValue.setStatus("current")


class _SysRateCtrlIngressLimitValue_Type(Integer32):
    """Custom type sysRateCtrlIngressLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SysRateCtrlIngressLimitValue_Type.__name__ = "Integer32"
_SysRateCtrlIngressLimitValue_Object = MibTableColumn
sysRateCtrlIngressLimitValue = _SysRateCtrlIngressLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 4, 1, 1, 7),
    _SysRateCtrlIngressLimitValue_Type()
)
sysRateCtrlIngressLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRateCtrlIngressLimitValue.setStatus("current")
_SysIpAuthMgr_ObjectIdentity = ObjectIdentity
sysIpAuthMgr = _SysIpAuthMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7)
)


class _SysIpAuthMgrStatus_Type(Integer32):
    """Custom type sysIpAuthMgrStatus based on Integer32"""
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


_SysIpAuthMgrStatus_Type.__name__ = "Integer32"
_SysIpAuthMgrStatus_Object = MibScalar
sysIpAuthMgrStatus = _SysIpAuthMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 1),
    _SysIpAuthMgrStatus_Type()
)
sysIpAuthMgrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAuthMgrStatus.setStatus("current")
_SysIpAuthMgrTable_Object = MibTable
sysIpAuthMgrTable = _SysIpAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2)
)
if mibBuilder.loadTexts:
    sysIpAuthMgrTable.setStatus("current")
_SysIpAuthMgrEntry_Object = MibTableRow
sysIpAuthMgrEntry = _SysIpAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1)
)
sysIpAuthMgrEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysIpAuthMgrIpAddr"),
    (0, "AT-GS950-16-MIB", "sysIpAuthMgrIpMask"),
)
if mibBuilder.loadTexts:
    sysIpAuthMgrEntry.setStatus("current")
_SysIpAuthMgrIpAddr_Type = IpAddress
_SysIpAuthMgrIpAddr_Object = MibTableColumn
sysIpAuthMgrIpAddr = _SysIpAuthMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1, 1),
    _SysIpAuthMgrIpAddr_Type()
)
sysIpAuthMgrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysIpAuthMgrIpAddr.setStatus("current")
_SysIpAuthMgrIpMask_Type = IpAddress
_SysIpAuthMgrIpMask_Object = MibTableColumn
sysIpAuthMgrIpMask = _SysIpAuthMgrIpMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1, 2),
    _SysIpAuthMgrIpMask_Type()
)
sysIpAuthMgrIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysIpAuthMgrIpMask.setStatus("current")
_SysIpAuthMgrPortList_Type = PortList
_SysIpAuthMgrPortList_Object = MibTableColumn
sysIpAuthMgrPortList = _SysIpAuthMgrPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1, 3),
    _SysIpAuthMgrPortList_Type()
)
sysIpAuthMgrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAuthMgrPortList.setStatus("current")
_SysIpAuthMgrVlanList_Type = OctetString
_SysIpAuthMgrVlanList_Object = MibTableColumn
sysIpAuthMgrVlanList = _SysIpAuthMgrVlanList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1, 4),
    _SysIpAuthMgrVlanList_Type()
)
sysIpAuthMgrVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAuthMgrVlanList.setStatus("current")


class _SysIpAuthMgrAllowedServices_Type(Integer32):
    """Custom type sysIpAuthMgrAllowedServices based on Integer32"""
    defaultHexValue = 31


_SysIpAuthMgrAllowedServices_Object = MibTableColumn
sysIpAuthMgrAllowedServices = _SysIpAuthMgrAllowedServices_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1, 6),
    _SysIpAuthMgrAllowedServices_Type()
)
sysIpAuthMgrAllowedServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAuthMgrAllowedServices.setStatus("current")
_SysIpAuthMgrRowStatus_Type = RowStatus
_SysIpAuthMgrRowStatus_Object = MibTableColumn
sysIpAuthMgrRowStatus = _SysIpAuthMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 7, 2, 1, 7),
    _SysIpAuthMgrRowStatus_Type()
)
sysIpAuthMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysIpAuthMgrRowStatus.setStatus("current")
_SysStormControl_ObjectIdentity = ObjectIdentity
sysStormControl = _SysStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12)
)
_SysStormCtrlTable_Object = MibTable
sysStormCtrlTable = _SysStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1)
)
if mibBuilder.loadTexts:
    sysStormCtrlTable.setStatus("current")
_SysStormCtrlEntry_Object = MibTableRow
sysStormCtrlEntry = _SysStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1)
)
sysStormCtrlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysStormCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysStormCtrlEntry.setStatus("current")


class _SysStormCtrlIndex_Type(Integer32):
    """Custom type sysStormCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysStormCtrlIndex_Type.__name__ = "Integer32"
_SysStormCtrlIndex_Object = MibTableColumn
sysStormCtrlIndex = _SysStormCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1, 1),
    _SysStormCtrlIndex_Type()
)
sysStormCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysStormCtrlIndex.setStatus("current")


class _SysDlfOnOff_Type(Integer32):
    """Custom type sysDlfOnOff based on Integer32"""
    defaultValue = 1

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


_SysDlfOnOff_Type.__name__ = "Integer32"
_SysDlfOnOff_Object = MibTableColumn
sysDlfOnOff = _SysDlfOnOff_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1, 2),
    _SysDlfOnOff_Type()
)
sysDlfOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDlfOnOff.setStatus("current")


class _SysBroadcastOnOff_Type(Integer32):
    """Custom type sysBroadcastOnOff based on Integer32"""
    defaultValue = 1

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


_SysBroadcastOnOff_Type.__name__ = "Integer32"
_SysBroadcastOnOff_Object = MibTableColumn
sysBroadcastOnOff = _SysBroadcastOnOff_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1, 3),
    _SysBroadcastOnOff_Type()
)
sysBroadcastOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBroadcastOnOff.setStatus("current")


class _SysMulticastOnOff_Type(Integer32):
    """Custom type sysMulticastOnOff based on Integer32"""
    defaultValue = 1

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


_SysMulticastOnOff_Type.__name__ = "Integer32"
_SysMulticastOnOff_Object = MibTableColumn
sysMulticastOnOff = _SysMulticastOnOff_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1, 4),
    _SysMulticastOnOff_Type()
)
sysMulticastOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMulticastOnOff.setStatus("current")


class _SysStormCtrlThreshold_Type(Integer32):
    """Custom type sysStormCtrlThreshold based on Integer32"""
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
        *(("disable", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_SysStormCtrlThreshold_Type.__name__ = "Integer32"
_SysStormCtrlThreshold_Object = MibTableColumn
sysStormCtrlThreshold = _SysStormCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1, 5),
    _SysStormCtrlThreshold_Type()
)
sysStormCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysStormCtrlThreshold.setStatus("current")
_SysStormCtrlRowStatus_Type = RowStatus
_SysStormCtrlRowStatus_Object = MibTableColumn
sysStormCtrlRowStatus = _SysStormCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 12, 1, 1, 6),
    _SysStormCtrlRowStatus_Type()
)
sysStormCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysStormCtrlRowStatus.setStatus("current")
_SysLBDdetect_ObjectIdentity = ObjectIdentity
sysLBDdetect = _SysLBDdetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22)
)


class _SysLBDStateEnable_Type(Integer32):
    """Custom type sysLBDStateEnable based on Integer32"""
    defaultValue = 2

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


_SysLBDStateEnable_Type.__name__ = "Integer32"
_SysLBDStateEnable_Object = MibScalar
sysLBDStateEnable = _SysLBDStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 1),
    _SysLBDStateEnable_Type()
)
sysLBDStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDStateEnable.setStatus("current")


class _SysLBDInterval_Type(Integer32):
    """Custom type sysLBDInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SysLBDInterval_Type.__name__ = "Integer32"
_SysLBDInterval_Object = MibScalar
sysLBDInterval = _SysLBDInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 2),
    _SysLBDInterval_Type()
)
sysLBDInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDInterval.setStatus("current")


class _SysLBDRecoverTime_Type(Integer32):
    """Custom type sysLBDRecoverTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_SysLBDRecoverTime_Type.__name__ = "Integer32"
_SysLBDRecoverTime_Object = MibScalar
sysLBDRecoverTime = _SysLBDRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 3),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 4)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 4, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")


class _SysLBDCtrlIndex_Type(Integer32):
    """Custom type sysLBDCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysLBDCtrlIndex_Type.__name__ = "Integer32"
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 4, 1, 1),
    _SysLBDCtrlIndex_Type()
)
sysLBDCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDCtrlIndex.setStatus("current")


class _SysLBDPortStatus_Type(Integer32):
    """Custom type sysLBDPortStatus based on Integer32"""
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


_SysLBDPortStatus_Type.__name__ = "Integer32"
_SysLBDPortStatus_Object = MibTableColumn
sysLBDPortStatus = _SysLBDPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 4, 1, 2),
    _SysLBDPortStatus_Type()
)
sysLBDPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDPortStatus.setStatus("current")


class _SysLBDPortLoopStatus_Type(Integer32):
    """Custom type sysLBDPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("normal", 1))
    )


_SysLBDPortLoopStatus_Type.__name__ = "Integer32"
_SysLBDPortLoopStatus_Object = MibTableColumn
sysLBDPortLoopStatus = _SysLBDPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 22, 4, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysUserAuthMgr_ObjectIdentity = ObjectIdentity
sysUserAuthMgr = _SysUserAuthMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 30)
)
_SysUserAuthMgrTable_Object = MibTable
sysUserAuthMgrTable = _SysUserAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 30, 1)
)
if mibBuilder.loadTexts:
    sysUserAuthMgrTable.setStatus("current")
_SysUserAuthMgrEntry_Object = MibTableRow
sysUserAuthMgrEntry = _SysUserAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 30, 1, 1)
)
sysUserAuthMgrEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysUserAuthMgrId"),
)
if mibBuilder.loadTexts:
    sysUserAuthMgrEntry.setStatus("current")


class _SysUserAuthMgrId_Type(Integer32):
    """Custom type sysUserAuthMgrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysUserAuthMgrId_Type.__name__ = "Integer32"
_SysUserAuthMgrId_Object = MibTableColumn
sysUserAuthMgrId = _SysUserAuthMgrId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 30, 1, 1, 1),
    _SysUserAuthMgrId_Type()
)
sysUserAuthMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserAuthMgrId.setStatus("current")


class _SysUserAuthMgrName_Type(OctetString):
    """Custom type sysUserAuthMgrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysUserAuthMgrName_Type.__name__ = "OctetString"
_SysUserAuthMgrName_Object = MibTableColumn
sysUserAuthMgrName = _SysUserAuthMgrName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 30, 1, 1, 2),
    _SysUserAuthMgrName_Type()
)
sysUserAuthMgrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserAuthMgrName.setStatus("current")
_SysUserAuthMgrRowStatus_Type = RowStatus
_SysUserAuthMgrRowStatus_Object = MibTableColumn
sysUserAuthMgrRowStatus = _SysUserAuthMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 81, 30, 1, 1, 3),
    _SysUserAuthMgrRowStatus_Type()
)
sysUserAuthMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysUserAuthMgrRowStatus.setStatus("current")
_L2Dfs_ObjectIdentity = ObjectIdentity
l2Dfs = _L2Dfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83)
)
_SysDfsMIBObjects_ObjectIdentity = ObjectIdentity
sysDfsMIBObjects = _SysDfsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1)
)
_SysDfsMFClassifier_ObjectIdentity = ObjectIdentity
sysDfsMFClassifier = _SysDfsMFClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2)
)
_SysDfsMultiFieldClfrTable_Object = MibTable
sysDfsMultiFieldClfrTable = _SysDfsMultiFieldClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysDfsMultiFieldClfrTable.setStatus("current")
_SysDfsMultiFieldClfrEntry_Object = MibTableRow
sysDfsMultiFieldClfrEntry = _SysDfsMultiFieldClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2, 1, 1)
)
sysDfsMultiFieldClfrEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysDfsMultiFieldClfrId"),
)
if mibBuilder.loadTexts:
    sysDfsMultiFieldClfrEntry.setStatus("current")


class _SysDfsMultiFieldClfrId_Type(Integer32):
    """Custom type sysDfsMultiFieldClfrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysDfsMultiFieldClfrId_Type.__name__ = "Integer32"
_SysDfsMultiFieldClfrId_Object = MibTableColumn
sysDfsMultiFieldClfrId = _SysDfsMultiFieldClfrId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2, 1, 1, 1),
    _SysDfsMultiFieldClfrId_Type()
)
sysDfsMultiFieldClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDfsMultiFieldClfrId.setStatus("current")
_SysDfsMultiFieldClfrFilterId_Type = Unsigned32
_SysDfsMultiFieldClfrFilterId_Object = MibTableColumn
sysDfsMultiFieldClfrFilterId = _SysDfsMultiFieldClfrFilterId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2, 1, 1, 2),
    _SysDfsMultiFieldClfrFilterId_Type()
)
sysDfsMultiFieldClfrFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsMultiFieldClfrFilterId.setStatus("current")


class _SysDfsMultiFieldClfrFilterType_Type(Integer32):
    """Custom type sysDfsMultiFieldClfrFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipfilter", 2),
          ("macfilter", 1))
    )


_SysDfsMultiFieldClfrFilterType_Type.__name__ = "Integer32"
_SysDfsMultiFieldClfrFilterType_Object = MibTableColumn
sysDfsMultiFieldClfrFilterType = _SysDfsMultiFieldClfrFilterType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2, 1, 1, 3),
    _SysDfsMultiFieldClfrFilterType_Type()
)
sysDfsMultiFieldClfrFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsMultiFieldClfrFilterType.setStatus("current")
_SysDfsMultiFieldClfrStatus_Type = RowStatus
_SysDfsMultiFieldClfrStatus_Object = MibTableColumn
sysDfsMultiFieldClfrStatus = _SysDfsMultiFieldClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 2, 1, 1, 4),
    _SysDfsMultiFieldClfrStatus_Type()
)
sysDfsMultiFieldClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDfsMultiFieldClfrStatus.setStatus("current")
_SysDfsClassifier_ObjectIdentity = ObjectIdentity
sysDfsClassifier = _SysDfsClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3)
)
_SysDfsClfrTable_Object = MibTable
sysDfsClfrTable = _SysDfsClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sysDfsClfrTable.setStatus("current")
_SysDfsClfrEntry_Object = MibTableRow
sysDfsClfrEntry = _SysDfsClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1, 1)
)
sysDfsClfrEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysDfsClfrId"),
)
if mibBuilder.loadTexts:
    sysDfsClfrEntry.setStatus("current")


class _SysDfsClfrId_Type(Integer32):
    """Custom type sysDfsClfrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysDfsClfrId_Type.__name__ = "Integer32"
_SysDfsClfrId_Object = MibTableColumn
sysDfsClfrId = _SysDfsClfrId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1, 1, 1),
    _SysDfsClfrId_Type()
)
sysDfsClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDfsClfrId.setStatus("current")


class _SysDfsClfrMFClfrId_Type(Integer32):
    """Custom type sysDfsClfrMFClfrId based on Integer32"""
    defaultValue = 0


_SysDfsClfrMFClfrId_Object = MibTableColumn
sysDfsClfrMFClfrId = _SysDfsClfrMFClfrId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1, 1, 2),
    _SysDfsClfrMFClfrId_Type()
)
sysDfsClfrMFClfrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsClfrMFClfrId.setStatus("current")


class _SysDfsClfrInProActionId_Type(Integer32):
    """Custom type sysDfsClfrInProActionId based on Integer32"""
    defaultValue = 0


_SysDfsClfrInProActionId_Object = MibTableColumn
sysDfsClfrInProActionId = _SysDfsClfrInProActionId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1, 1, 3),
    _SysDfsClfrInProActionId_Type()
)
sysDfsClfrInProActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsClfrInProActionId.setStatus("current")


class _SysDfsClfrOutProActionId_Type(Integer32):
    """Custom type sysDfsClfrOutProActionId based on Integer32"""
    defaultValue = 0


_SysDfsClfrOutProActionId_Object = MibTableColumn
sysDfsClfrOutProActionId = _SysDfsClfrOutProActionId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1, 1, 4),
    _SysDfsClfrOutProActionId_Type()
)
sysDfsClfrOutProActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsClfrOutProActionId.setStatus("current")
_SysDfsClfrStatus_Type = RowStatus
_SysDfsClfrStatus_Object = MibTableColumn
sysDfsClfrStatus = _SysDfsClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 3, 1, 1, 5),
    _SysDfsClfrStatus_Type()
)
sysDfsClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDfsClfrStatus.setStatus("current")
_SysDfsInProfileAction_ObjectIdentity = ObjectIdentity
sysDfsInProfileAction = _SysDfsInProfileAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4)
)
_SysDfsInProfileActionTable_Object = MibTable
sysDfsInProfileActionTable = _SysDfsInProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sysDfsInProfileActionTable.setStatus("current")
_SysDfsInProfileActionEntry_Object = MibTableRow
sysDfsInProfileActionEntry = _SysDfsInProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1, 1)
)
sysDfsInProfileActionEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysDfsInProfileActionId"),
)
if mibBuilder.loadTexts:
    sysDfsInProfileActionEntry.setStatus("current")


class _SysDfsInProfileActionId_Type(Integer32):
    """Custom type sysDfsInProfileActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysDfsInProfileActionId_Type.__name__ = "Integer32"
_SysDfsInProfileActionId_Object = MibTableColumn
sysDfsInProfileActionId = _SysDfsInProfileActionId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1, 1, 1),
    _SysDfsInProfileActionId_Type()
)
sysDfsInProfileActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDfsInProfileActionId.setStatus("current")
_SysDfsInProfileActionFlag_Type = Unsigned32
_SysDfsInProfileActionFlag_Object = MibTableColumn
sysDfsInProfileActionFlag = _SysDfsInProfileActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1, 1, 2),
    _SysDfsInProfileActionFlag_Type()
)
sysDfsInProfileActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsInProfileActionFlag.setStatus("current")
_SysDfsInProfileActionNewPrio_Type = Unsigned32
_SysDfsInProfileActionNewPrio_Object = MibTableColumn
sysDfsInProfileActionNewPrio = _SysDfsInProfileActionNewPrio_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1, 1, 3),
    _SysDfsInProfileActionNewPrio_Type()
)
sysDfsInProfileActionNewPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsInProfileActionNewPrio.setStatus("current")
_SysDfsInProfileActionDscp_Type = DscpOrAny
_SysDfsInProfileActionDscp_Object = MibTableColumn
sysDfsInProfileActionDscp = _SysDfsInProfileActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1, 1, 6),
    _SysDfsInProfileActionDscp_Type()
)
sysDfsInProfileActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsInProfileActionDscp.setStatus("current")
_SysDfsInProfileActionStatus_Type = RowStatus
_SysDfsInProfileActionStatus_Object = MibTableColumn
sysDfsInProfileActionStatus = _SysDfsInProfileActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 4, 1, 1, 7),
    _SysDfsInProfileActionStatus_Type()
)
sysDfsInProfileActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDfsInProfileActionStatus.setStatus("current")
_SysDfsOutProfileAction_ObjectIdentity = ObjectIdentity
sysDfsOutProfileAction = _SysDfsOutProfileAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5)
)
_SysDfsOutProfileActionTable_Object = MibTable
sysDfsOutProfileActionTable = _SysDfsOutProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sysDfsOutProfileActionTable.setStatus("current")
_SysDfsOutProfileActionEntry_Object = MibTableRow
sysDfsOutProfileActionEntry = _SysDfsOutProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5, 1, 1)
)
sysDfsOutProfileActionEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysDfsOutProfileActionId"),
)
if mibBuilder.loadTexts:
    sysDfsOutProfileActionEntry.setStatus("current")


class _SysDfsOutProfileActionId_Type(Integer32):
    """Custom type sysDfsOutProfileActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysDfsOutProfileActionId_Type.__name__ = "Integer32"
_SysDfsOutProfileActionId_Object = MibTableColumn
sysDfsOutProfileActionId = _SysDfsOutProfileActionId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5, 1, 1, 1),
    _SysDfsOutProfileActionId_Type()
)
sysDfsOutProfileActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDfsOutProfileActionId.setStatus("current")
_SysDfsOutProfileActionFlag_Type = Unsigned32
_SysDfsOutProfileActionFlag_Object = MibTableColumn
sysDfsOutProfileActionFlag = _SysDfsOutProfileActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5, 1, 1, 2),
    _SysDfsOutProfileActionFlag_Type()
)
sysDfsOutProfileActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsOutProfileActionFlag.setStatus("current")
_SysDfsOutProfileActionMID_Type = Integer32
_SysDfsOutProfileActionMID_Object = MibTableColumn
sysDfsOutProfileActionMID = _SysDfsOutProfileActionMID_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5, 1, 1, 4),
    _SysDfsOutProfileActionMID_Type()
)
sysDfsOutProfileActionMID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsOutProfileActionMID.setStatus("current")
_SysDfsOutProfileActionStatus_Type = RowStatus
_SysDfsOutProfileActionStatus_Object = MibTableColumn
sysDfsOutProfileActionStatus = _SysDfsOutProfileActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 5, 1, 1, 5),
    _SysDfsOutProfileActionStatus_Type()
)
sysDfsOutProfileActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDfsOutProfileActionStatus.setStatus("current")
_SysDfsMeter_ObjectIdentity = ObjectIdentity
sysDfsMeter = _SysDfsMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 6)
)
_SysDfsMeterTable_Object = MibTable
sysDfsMeterTable = _SysDfsMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sysDfsMeterTable.setStatus("current")
_SysDfsMeterEntry_Object = MibTableRow
sysDfsMeterEntry = _SysDfsMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 6, 1, 1)
)
sysDfsMeterEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysDfsMeterId"),
)
if mibBuilder.loadTexts:
    sysDfsMeterEntry.setStatus("current")


class _SysDfsMeterId_Type(Integer32):
    """Custom type sysDfsMeterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysDfsMeterId_Type.__name__ = "Integer32"
_SysDfsMeterId_Object = MibTableColumn
sysDfsMeterId = _SysDfsMeterId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 6, 1, 1, 1),
    _SysDfsMeterId_Type()
)
sysDfsMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDfsMeterId.setStatus("current")
_SysDfsMeterRefreshCount_Type = Unsigned32
_SysDfsMeterRefreshCount_Object = MibTableColumn
sysDfsMeterRefreshCount = _SysDfsMeterRefreshCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 6, 1, 1, 3),
    _SysDfsMeterRefreshCount_Type()
)
sysDfsMeterRefreshCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsMeterRefreshCount.setStatus("current")
_SysDfsMeterStatus_Type = RowStatus
_SysDfsMeterStatus_Object = MibTableColumn
sysDfsMeterStatus = _SysDfsMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 6, 1, 1, 4),
    _SysDfsMeterStatus_Type()
)
sysDfsMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDfsMeterStatus.setStatus("current")
_SysDfsEnterpriseCoSqAlgorithm_ObjectIdentity = ObjectIdentity
sysDfsEnterpriseCoSqAlgorithm = _SysDfsEnterpriseCoSqAlgorithm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 8)
)
_SysDfsCoSqAlgorithmTable_Object = MibTable
sysDfsCoSqAlgorithmTable = _SysDfsCoSqAlgorithmTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 8, 1)
)
if mibBuilder.loadTexts:
    sysDfsCoSqAlgorithmTable.setStatus("current")
_SysDfsCoSqAlgorithmEntry_Object = MibTableRow
sysDfsCoSqAlgorithmEntry = _SysDfsCoSqAlgorithmEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 8, 1, 1)
)
sysDfsCoSqAlgorithmEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysDfsPortId"),
)
if mibBuilder.loadTexts:
    sysDfsCoSqAlgorithmEntry.setStatus("current")


class _SysDfsPortId_Type(Integer32):
    """Custom type sysDfsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SysDfsPortId_Type.__name__ = "Integer32"
_SysDfsPortId_Object = MibTableColumn
sysDfsPortId = _SysDfsPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 8, 1, 1, 1),
    _SysDfsPortId_Type()
)
sysDfsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDfsPortId.setStatus("current")


class _SysDfsCoSqAlgorithm_Type(Integer32):
    """Custom type sysDfsCoSqAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("weightedRoundRobin", 3))
    )


_SysDfsCoSqAlgorithm_Type.__name__ = "Integer32"
_SysDfsCoSqAlgorithm_Object = MibTableColumn
sysDfsCoSqAlgorithm = _SysDfsCoSqAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 83, 1, 8, 1, 1, 2),
    _SysDfsCoSqAlgorithm_Type()
)
sysDfsCoSqAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDfsCoSqAlgorithm.setStatus("current")
_L2Syslog_ObjectIdentity = ObjectIdentity
l2Syslog = _L2Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89)
)
_SysSyslogGeneralGroup_ObjectIdentity = ObjectIdentity
sysSyslogGeneralGroup = _SysSyslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1)
)


class _SysSyslogLogging_Type(Integer32):
    """Custom type sysSyslogLogging based on Integer32"""
    defaultValue = 1

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


_SysSyslogLogging_Type.__name__ = "Integer32"
_SysSyslogLogging_Object = MibScalar
sysSyslogLogging = _SysSyslogLogging_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 1),
    _SysSyslogLogging_Type()
)
sysSyslogLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogLogging.setStatus("current")


class _SysSyslogTimeStamp_Type(Integer32):
    """Custom type sysSyslogTimeStamp based on Integer32"""
    defaultValue = 1

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


_SysSyslogTimeStamp_Type.__name__ = "Integer32"
_SysSyslogTimeStamp_Object = MibScalar
sysSyslogTimeStamp = _SysSyslogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 2),
    _SysSyslogTimeStamp_Type()
)
sysSyslogTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogTimeStamp.setStatus("current")


class _SysSyslogSysBuffers_Type(Integer32):
    """Custom type sysSyslogSysBuffers based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_SysSyslogSysBuffers_Type.__name__ = "Integer32"
_SysSyslogSysBuffers_Object = MibScalar
sysSyslogSysBuffers = _SysSyslogSysBuffers_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 4),
    _SysSyslogSysBuffers_Type()
)
sysSyslogSysBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogSysBuffers.setStatus("current")


class _SysSyslogClearLog_Type(TruthValue):
    """Custom type sysSyslogClearLog based on TruthValue"""


_SysSyslogClearLog_Object = MibScalar
sysSyslogClearLog = _SysSyslogClearLog_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 5),
    _SysSyslogClearLog_Type()
)
sysSyslogClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogClearLog.setStatus("current")
_SysSyslogConfigTable_Object = MibTable
sysSyslogConfigTable = _SysSyslogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 6)
)
if mibBuilder.loadTexts:
    sysSyslogConfigTable.setStatus("current")
_SysSyslogConfigEntry_Object = MibTableRow
sysSyslogConfigEntry = _SysSyslogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 6, 1)
)
sysSyslogConfigEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSyslogConfigModule"),
)
if mibBuilder.loadTexts:
    sysSyslogConfigEntry.setStatus("current")


class _SysSyslogConfigModule_Type(Integer32):
    """Custom type sysSyslogConfigModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysSyslogConfigModule_Type.__name__ = "Integer32"
_SysSyslogConfigModule_Object = MibTableColumn
sysSyslogConfigModule = _SysSyslogConfigModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 6, 1, 1),
    _SysSyslogConfigModule_Type()
)
sysSyslogConfigModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSyslogConfigModule.setStatus("current")


class _SysSyslogConfigLogLevel_Type(Integer32):
    """Custom type sysSyslogConfigLogLevel based on Integer32"""
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
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_SysSyslogConfigLogLevel_Type.__name__ = "Integer32"
_SysSyslogConfigLogLevel_Object = MibTableColumn
sysSyslogConfigLogLevel = _SysSyslogConfigLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 6, 1, 2),
    _SysSyslogConfigLogLevel_Type()
)
sysSyslogConfigLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogConfigLogLevel.setStatus("current")


class _SysSyslogFacility_Type(Integer32):
    """Custom type sysSyslogFacility based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184))
    )


_SysSyslogFacility_Type.__name__ = "Integer32"
_SysSyslogFacility_Object = MibScalar
sysSyslogFacility = _SysSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 1, 7),
    _SysSyslogFacility_Type()
)
sysSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogFacility.setStatus("current")
_SysSyslogLogs_ObjectIdentity = ObjectIdentity
sysSyslogLogs = _SysSyslogLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 2)
)
_SysSyslogLogSrvAddr_Type = IpAddress
_SysSyslogLogSrvAddr_Object = MibScalar
sysSyslogLogSrvAddr = _SysSyslogLogSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 89, 2, 1),
    _SysSyslogLogSrvAddr_Type()
)
sysSyslogLogSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSyslogLogSrvAddr.setStatus("current")
_L2Security_ObjectIdentity = ObjectIdentity
l2Security = _L2Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95)
)
_SysPortSecurity_ObjectIdentity = ObjectIdentity
sysPortSecurity = _SysPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95, 1)
)
_SysPortSecurityTable_Object = MibTable
sysPortSecurityTable = _SysPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95, 1, 1)
)
if mibBuilder.loadTexts:
    sysPortSecurityTable.setStatus("current")
_SysPortSecurityEntry_Object = MibTableRow
sysPortSecurityEntry = _SysPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95, 1, 1, 1)
)
sysPortSecurityEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysPortSecurityIndex"),
)
if mibBuilder.loadTexts:
    sysPortSecurityEntry.setStatus("current")


class _SysPortSecurityIndex_Type(Integer32):
    """Custom type sysPortSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysPortSecurityIndex_Type.__name__ = "Integer32"
_SysPortSecurityIndex_Object = MibTableColumn
sysPortSecurityIndex = _SysPortSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95, 1, 1, 1, 1),
    _SysPortSecurityIndex_Type()
)
sysPortSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysPortSecurityIndex.setStatus("current")


class _SysPortSecurityState_Type(Integer32):
    """Custom type sysPortSecurityState based on Integer32"""
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


_SysPortSecurityState_Type.__name__ = "Integer32"
_SysPortSecurityState_Object = MibTableColumn
sysPortSecurityState = _SysPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95, 1, 1, 1, 2),
    _SysPortSecurityState_Type()
)
sysPortSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortSecurityState.setStatus("current")
_SysPortSecurityMLA_Type = Integer32
_SysPortSecurityMLA_Object = MibTableColumn
sysPortSecurityMLA = _SysPortSecurityMLA_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 95, 1, 1, 1, 3),
    _SysPortSecurityMLA_Type()
)
sysPortSecurityMLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortSecurityMLA.setStatus("current")
_L2Ssl_ObjectIdentity = ObjectIdentity
l2Ssl = _L2Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96)
)
_SysSslGeneralGroup_ObjectIdentity = ObjectIdentity
sysSslGeneralGroup = _SysSslGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 1)
)


class _SysSslSecureHttpStatus_Type(Integer32):
    """Custom type sysSslSecureHttpStatus based on Integer32"""
    defaultValue = 2

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


_SysSslSecureHttpStatus_Type.__name__ = "Integer32"
_SysSslSecureHttpStatus_Object = MibScalar
sysSslSecureHttpStatus = _SysSslSecureHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 1, 2),
    _SysSslSecureHttpStatus_Type()
)
sysSslSecureHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSslSecureHttpStatus.setStatus("current")


class _SysSslPort_Type(Integer32):
    """Custom type sysSslPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysSslPort_Type.__name__ = "Integer32"
_SysSslPort_Object = MibScalar
sysSslPort = _SysSslPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 1, 3),
    _SysSslPort_Type()
)
sysSslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSslPort.setStatus("current")
_SysSslTrace_Type = Integer32
_SysSslTrace_Object = MibScalar
sysSslTrace = _SysSslTrace_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 1, 4),
    _SysSslTrace_Type()
)
sysSslTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSslTrace.setStatus("current")
_SysSslCiphers_ObjectIdentity = ObjectIdentity
sysSslCiphers = _SysSslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 2)
)


class _SysSslCipherList_Type(Integer32):
    """Custom type sysSslCipherList based on Integer32"""
    defaultValue = 0


_SysSslCipherList_Object = MibScalar
sysSslCipherList = _SysSslCipherList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 2, 1),
    _SysSslCipherList_Type()
)
sysSslCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSslCipherList.setStatus("current")


class _SysSslDefaultCipherList_Type(TruthValue):
    """Custom type sysSslDefaultCipherList based on TruthValue"""


_SysSslDefaultCipherList_Object = MibScalar
sysSslDefaultCipherList = _SysSslDefaultCipherList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 96, 2, 2),
    _SysSslDefaultCipherList_Type()
)
sysSslDefaultCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSslDefaultCipherList.setStatus("current")
_L2Ssh_ObjectIdentity = ObjectIdentity
l2Ssh = _L2Ssh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97)
)
_SysSshGeneralGroup_ObjectIdentity = ObjectIdentity
sysSshGeneralGroup = _SysSshGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97, 1)
)


class _SysSshVersionCompatibility_Type(TruthValue):
    """Custom type sysSshVersionCompatibility based on TruthValue"""


_SysSshVersionCompatibility_Object = MibScalar
sysSshVersionCompatibility = _SysSshVersionCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97, 1, 1),
    _SysSshVersionCompatibility_Type()
)
sysSshVersionCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshVersionCompatibility.setStatus("current")


class _SysSshCipherList_Type(Integer32):
    """Custom type sysSshCipherList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SysSshCipherList_Type.__name__ = "Integer32"
_SysSshCipherList_Object = MibScalar
sysSshCipherList = _SysSshCipherList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97, 1, 2),
    _SysSshCipherList_Type()
)
sysSshCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshCipherList.setStatus("current")


class _SysSshMacList_Type(Integer32):
    """Custom type sysSshMacList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SysSshMacList_Type.__name__ = "Integer32"
_SysSshMacList_Object = MibScalar
sysSshMacList = _SysSshMacList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97, 1, 3),
    _SysSshMacList_Type()
)
sysSshMacList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshMacList.setStatus("current")
_SysSshTrace_Type = Integer32
_SysSshTrace_Object = MibScalar
sysSshTrace = _SysSshTrace_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97, 1, 4),
    _SysSshTrace_Type()
)
sysSshTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshTrace.setStatus("current")


class _SysSshStatus_Type(TruthValue):
    """Custom type sysSshStatus based on TruthValue"""


_SysSshStatus_Object = MibScalar
sysSshStatus = _SysSshStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 97, 1, 5),
    _SysSshStatus_Type()
)
sysSshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshStatus.setStatus("current")
_L2Sntp_ObjectIdentity = ObjectIdentity
l2Sntp = _L2Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99)
)
_SysSntpGeneralGroup_ObjectIdentity = ObjectIdentity
sysSntpGeneralGroup = _SysSntpGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1)
)


class _SysSntpStatus_Type(Integer32):
    """Custom type sysSntpStatus based on Integer32"""
    defaultValue = 1

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


_SysSntpStatus_Type.__name__ = "Integer32"
_SysSntpStatus_Object = MibScalar
sysSntpStatus = _SysSntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1, 1),
    _SysSntpStatus_Type()
)
sysSntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpStatus.setStatus("current")
_SysSntpPollInterval_Type = Integer32
_SysSntpPollInterval_Object = MibScalar
sysSntpPollInterval = _SysSntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1, 2),
    _SysSntpPollInterval_Type()
)
sysSntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpPollInterval.setStatus("current")
_SysSntpTimeSeconds_Type = Integer32
_SysSntpTimeSeconds_Object = MibScalar
sysSntpTimeSeconds = _SysSntpTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1, 3),
    _SysSntpTimeSeconds_Type()
)
sysSntpTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTimeSeconds.setStatus("current")
_SysSntpPrimarySrvAddr_Type = IpAddress
_SysSntpPrimarySrvAddr_Object = MibScalar
sysSntpPrimarySrvAddr = _SysSntpPrimarySrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1, 4),
    _SysSntpPrimarySrvAddr_Type()
)
sysSntpPrimarySrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpPrimarySrvAddr.setStatus("current")
_SysSntpSecondSrvAddr_Type = IpAddress
_SysSntpSecondSrvAddr_Object = MibScalar
sysSntpSecondSrvAddr = _SysSntpSecondSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1, 5),
    _SysSntpSecondSrvAddr_Type()
)
sysSntpSecondSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpSecondSrvAddr.setStatus("current")
_SysSntpTimeZoneMappingIndex_Type = Integer32
_SysSntpTimeZoneMappingIndex_Object = MibScalar
sysSntpTimeZoneMappingIndex = _SysSntpTimeZoneMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 1, 6),
    _SysSntpTimeZoneMappingIndex_Type()
)
sysSntpTimeZoneMappingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTimeZoneMappingIndex.setStatus("current")
_SysSntpTzGroup_ObjectIdentity = ObjectIdentity
sysSntpTzGroup = _SysSntpTzGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2)
)


class _SysSntpTzDSTStatus_Type(Integer32):
    """Custom type sysSntpTzDSTStatus based on Integer32"""
    defaultValue = 1

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


_SysSntpTzDSTStatus_Type.__name__ = "Integer32"
_SysSntpTzDSTStatus_Object = MibScalar
sysSntpTzDSTStatus = _SysSntpTzDSTStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 1),
    _SysSntpTzDSTStatus_Type()
)
sysSntpTzDSTStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTStatus.setStatus("current")
_SysSntpTzMinutesWest_Type = Integer32
_SysSntpTzMinutesWest_Object = MibScalar
sysSntpTzMinutesWest = _SysSntpTzMinutesWest_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 2),
    _SysSntpTzMinutesWest_Type()
)
sysSntpTzMinutesWest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzMinutesWest.setStatus("current")
_SysSntpTzDSTStartMon_Type = Integer32
_SysSntpTzDSTStartMon_Object = MibScalar
sysSntpTzDSTStartMon = _SysSntpTzDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 3),
    _SysSntpTzDSTStartMon_Type()
)
sysSntpTzDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTStartMon.setStatus("current")
_SysSntpTzDSTStartDay_Type = Integer32
_SysSntpTzDSTStartDay_Object = MibScalar
sysSntpTzDSTStartDay = _SysSntpTzDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 4),
    _SysSntpTzDSTStartDay_Type()
)
sysSntpTzDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTStartDay.setStatus("current")
_SysSntpTzDSTStartHour_Type = Integer32
_SysSntpTzDSTStartHour_Object = MibScalar
sysSntpTzDSTStartHour = _SysSntpTzDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 5),
    _SysSntpTzDSTStartHour_Type()
)
sysSntpTzDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTStartHour.setStatus("current")
_SysSntpTzDSTStartMinute_Type = Integer32
_SysSntpTzDSTStartMinute_Object = MibScalar
sysSntpTzDSTStartMinute = _SysSntpTzDSTStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 6),
    _SysSntpTzDSTStartMinute_Type()
)
sysSntpTzDSTStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTStartMinute.setStatus("current")
_SysSntpTzDSTEndMon_Type = Integer32
_SysSntpTzDSTEndMon_Object = MibScalar
sysSntpTzDSTEndMon = _SysSntpTzDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 7),
    _SysSntpTzDSTEndMon_Type()
)
sysSntpTzDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTEndMon.setStatus("current")
_SysSntpTzDSTEndDay_Type = Integer32
_SysSntpTzDSTEndDay_Object = MibScalar
sysSntpTzDSTEndDay = _SysSntpTzDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 8),
    _SysSntpTzDSTEndDay_Type()
)
sysSntpTzDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTEndDay.setStatus("current")
_SysSntpTzDSTEndHour_Type = Integer32
_SysSntpTzDSTEndHour_Object = MibScalar
sysSntpTzDSTEndHour = _SysSntpTzDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 9),
    _SysSntpTzDSTEndHour_Type()
)
sysSntpTzDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTEndHour.setStatus("current")
_SysSntpTzDSTEndMinute_Type = Integer32
_SysSntpTzDSTEndMinute_Object = MibScalar
sysSntpTzDSTEndMinute = _SysSntpTzDSTEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 10),
    _SysSntpTzDSTEndMinute_Type()
)
sysSntpTzDSTEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTEndMinute.setStatus("current")


class _SysSntpTzDSTForwardOffset_Type(Integer32):
    """Custom type sysSntpTzDSTForwardOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("halfHour", 30),
          ("oneHour", 60))
    )


_SysSntpTzDSTForwardOffset_Type.__name__ = "Integer32"
_SysSntpTzDSTForwardOffset_Object = MibScalar
sysSntpTzDSTForwardOffset = _SysSntpTzDSTForwardOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 99, 2, 11),
    _SysSntpTzDSTForwardOffset_Type()
)
sysSntpTzDSTForwardOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSntpTzDSTForwardOffset.setStatus("current")
_L2Dscp_ObjectIdentity = ObjectIdentity
l2Dscp = _L2Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100)
)
_SysDscpMIBObjects_ObjectIdentity = ObjectIdentity
sysDscpMIBObjects = _SysDscpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1)
)


class _SysDscpEnable_Type(Integer32):
    """Custom type sysDscpEnable based on Integer32"""
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


_SysDscpEnable_Type.__name__ = "Integer32"
_SysDscpEnable_Object = MibScalar
sysDscpEnable = _SysDscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 1),
    _SysDscpEnable_Type()
)
sysDscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpEnable.setStatus("current")
_SysDscpTypeGroup_ObjectIdentity = ObjectIdentity
sysDscpTypeGroup = _SysDscpTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2)
)


class _SysDscpType01_Type(Integer32):
    """Custom type sysDscpType01 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType01_Type.__name__ = "Integer32"
_SysDscpType01_Object = MibScalar
sysDscpType01 = _SysDscpType01_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 1),
    _SysDscpType01_Type()
)
sysDscpType01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType01.setStatus("current")


class _SysDscpType02_Type(Integer32):
    """Custom type sysDscpType02 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType02_Type.__name__ = "Integer32"
_SysDscpType02_Object = MibScalar
sysDscpType02 = _SysDscpType02_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 2),
    _SysDscpType02_Type()
)
sysDscpType02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType02.setStatus("current")


class _SysDscpType03_Type(Integer32):
    """Custom type sysDscpType03 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType03_Type.__name__ = "Integer32"
_SysDscpType03_Object = MibScalar
sysDscpType03 = _SysDscpType03_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 3),
    _SysDscpType03_Type()
)
sysDscpType03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType03.setStatus("current")


class _SysDscpType04_Type(Integer32):
    """Custom type sysDscpType04 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType04_Type.__name__ = "Integer32"
_SysDscpType04_Object = MibScalar
sysDscpType04 = _SysDscpType04_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 4),
    _SysDscpType04_Type()
)
sysDscpType04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType04.setStatus("current")


class _SysDscpType05_Type(Integer32):
    """Custom type sysDscpType05 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType05_Type.__name__ = "Integer32"
_SysDscpType05_Object = MibScalar
sysDscpType05 = _SysDscpType05_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 5),
    _SysDscpType05_Type()
)
sysDscpType05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType05.setStatus("current")


class _SysDscpType06_Type(Integer32):
    """Custom type sysDscpType06 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType06_Type.__name__ = "Integer32"
_SysDscpType06_Object = MibScalar
sysDscpType06 = _SysDscpType06_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 6),
    _SysDscpType06_Type()
)
sysDscpType06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType06.setStatus("current")


class _SysDscpType07_Type(Integer32):
    """Custom type sysDscpType07 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType07_Type.__name__ = "Integer32"
_SysDscpType07_Object = MibScalar
sysDscpType07 = _SysDscpType07_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 7),
    _SysDscpType07_Type()
)
sysDscpType07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType07.setStatus("current")


class _SysDscpType08_Type(Integer32):
    """Custom type sysDscpType08 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType08_Type.__name__ = "Integer32"
_SysDscpType08_Object = MibScalar
sysDscpType08 = _SysDscpType08_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 8),
    _SysDscpType08_Type()
)
sysDscpType08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType08.setStatus("current")


class _SysDscpType09_Type(Integer32):
    """Custom type sysDscpType09 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType09_Type.__name__ = "Integer32"
_SysDscpType09_Object = MibScalar
sysDscpType09 = _SysDscpType09_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 9),
    _SysDscpType09_Type()
)
sysDscpType09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType09.setStatus("current")


class _SysDscpType10_Type(Integer32):
    """Custom type sysDscpType10 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType10_Type.__name__ = "Integer32"
_SysDscpType10_Object = MibScalar
sysDscpType10 = _SysDscpType10_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 10),
    _SysDscpType10_Type()
)
sysDscpType10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType10.setStatus("current")


class _SysDscpType11_Type(Integer32):
    """Custom type sysDscpType11 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType11_Type.__name__ = "Integer32"
_SysDscpType11_Object = MibScalar
sysDscpType11 = _SysDscpType11_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 11),
    _SysDscpType11_Type()
)
sysDscpType11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType11.setStatus("current")


class _SysDscpType12_Type(Integer32):
    """Custom type sysDscpType12 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType12_Type.__name__ = "Integer32"
_SysDscpType12_Object = MibScalar
sysDscpType12 = _SysDscpType12_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 12),
    _SysDscpType12_Type()
)
sysDscpType12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType12.setStatus("current")


class _SysDscpType13_Type(Integer32):
    """Custom type sysDscpType13 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType13_Type.__name__ = "Integer32"
_SysDscpType13_Object = MibScalar
sysDscpType13 = _SysDscpType13_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 13),
    _SysDscpType13_Type()
)
sysDscpType13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType13.setStatus("current")


class _SysDscpType14_Type(Integer32):
    """Custom type sysDscpType14 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType14_Type.__name__ = "Integer32"
_SysDscpType14_Object = MibScalar
sysDscpType14 = _SysDscpType14_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 14),
    _SysDscpType14_Type()
)
sysDscpType14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType14.setStatus("current")


class _SysDscpType15_Type(Integer32):
    """Custom type sysDscpType15 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType15_Type.__name__ = "Integer32"
_SysDscpType15_Object = MibScalar
sysDscpType15 = _SysDscpType15_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 15),
    _SysDscpType15_Type()
)
sysDscpType15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType15.setStatus("current")


class _SysDscpType16_Type(Integer32):
    """Custom type sysDscpType16 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType16_Type.__name__ = "Integer32"
_SysDscpType16_Object = MibScalar
sysDscpType16 = _SysDscpType16_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 16),
    _SysDscpType16_Type()
)
sysDscpType16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType16.setStatus("current")


class _SysDscpType17_Type(Integer32):
    """Custom type sysDscpType17 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType17_Type.__name__ = "Integer32"
_SysDscpType17_Object = MibScalar
sysDscpType17 = _SysDscpType17_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 17),
    _SysDscpType17_Type()
)
sysDscpType17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType17.setStatus("current")


class _SysDscpType18_Type(Integer32):
    """Custom type sysDscpType18 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType18_Type.__name__ = "Integer32"
_SysDscpType18_Object = MibScalar
sysDscpType18 = _SysDscpType18_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 18),
    _SysDscpType18_Type()
)
sysDscpType18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType18.setStatus("current")


class _SysDscpType19_Type(Integer32):
    """Custom type sysDscpType19 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType19_Type.__name__ = "Integer32"
_SysDscpType19_Object = MibScalar
sysDscpType19 = _SysDscpType19_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 19),
    _SysDscpType19_Type()
)
sysDscpType19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType19.setStatus("current")


class _SysDscpType20_Type(Integer32):
    """Custom type sysDscpType20 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType20_Type.__name__ = "Integer32"
_SysDscpType20_Object = MibScalar
sysDscpType20 = _SysDscpType20_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 20),
    _SysDscpType20_Type()
)
sysDscpType20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType20.setStatus("current")


class _SysDscpType21_Type(Integer32):
    """Custom type sysDscpType21 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType21_Type.__name__ = "Integer32"
_SysDscpType21_Object = MibScalar
sysDscpType21 = _SysDscpType21_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 21),
    _SysDscpType21_Type()
)
sysDscpType21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType21.setStatus("current")


class _SysDscpType22_Type(Integer32):
    """Custom type sysDscpType22 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType22_Type.__name__ = "Integer32"
_SysDscpType22_Object = MibScalar
sysDscpType22 = _SysDscpType22_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 22),
    _SysDscpType22_Type()
)
sysDscpType22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType22.setStatus("current")


class _SysDscpType23_Type(Integer32):
    """Custom type sysDscpType23 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType23_Type.__name__ = "Integer32"
_SysDscpType23_Object = MibScalar
sysDscpType23 = _SysDscpType23_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 23),
    _SysDscpType23_Type()
)
sysDscpType23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType23.setStatus("current")


class _SysDscpType24_Type(Integer32):
    """Custom type sysDscpType24 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType24_Type.__name__ = "Integer32"
_SysDscpType24_Object = MibScalar
sysDscpType24 = _SysDscpType24_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 24),
    _SysDscpType24_Type()
)
sysDscpType24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType24.setStatus("current")


class _SysDscpType25_Type(Integer32):
    """Custom type sysDscpType25 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType25_Type.__name__ = "Integer32"
_SysDscpType25_Object = MibScalar
sysDscpType25 = _SysDscpType25_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 25),
    _SysDscpType25_Type()
)
sysDscpType25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType25.setStatus("current")


class _SysDscpType26_Type(Integer32):
    """Custom type sysDscpType26 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType26_Type.__name__ = "Integer32"
_SysDscpType26_Object = MibScalar
sysDscpType26 = _SysDscpType26_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 26),
    _SysDscpType26_Type()
)
sysDscpType26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType26.setStatus("current")


class _SysDscpType27_Type(Integer32):
    """Custom type sysDscpType27 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType27_Type.__name__ = "Integer32"
_SysDscpType27_Object = MibScalar
sysDscpType27 = _SysDscpType27_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 27),
    _SysDscpType27_Type()
)
sysDscpType27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType27.setStatus("current")


class _SysDscpType28_Type(Integer32):
    """Custom type sysDscpType28 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType28_Type.__name__ = "Integer32"
_SysDscpType28_Object = MibScalar
sysDscpType28 = _SysDscpType28_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 28),
    _SysDscpType28_Type()
)
sysDscpType28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType28.setStatus("current")


class _SysDscpType29_Type(Integer32):
    """Custom type sysDscpType29 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType29_Type.__name__ = "Integer32"
_SysDscpType29_Object = MibScalar
sysDscpType29 = _SysDscpType29_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 29),
    _SysDscpType29_Type()
)
sysDscpType29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType29.setStatus("current")


class _SysDscpType30_Type(Integer32):
    """Custom type sysDscpType30 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType30_Type.__name__ = "Integer32"
_SysDscpType30_Object = MibScalar
sysDscpType30 = _SysDscpType30_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 30),
    _SysDscpType30_Type()
)
sysDscpType30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType30.setStatus("current")


class _SysDscpType31_Type(Integer32):
    """Custom type sysDscpType31 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType31_Type.__name__ = "Integer32"
_SysDscpType31_Object = MibScalar
sysDscpType31 = _SysDscpType31_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 31),
    _SysDscpType31_Type()
)
sysDscpType31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType31.setStatus("current")


class _SysDscpType32_Type(Integer32):
    """Custom type sysDscpType32 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType32_Type.__name__ = "Integer32"
_SysDscpType32_Object = MibScalar
sysDscpType32 = _SysDscpType32_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 32),
    _SysDscpType32_Type()
)
sysDscpType32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType32.setStatus("current")


class _SysDscpType33_Type(Integer32):
    """Custom type sysDscpType33 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType33_Type.__name__ = "Integer32"
_SysDscpType33_Object = MibScalar
sysDscpType33 = _SysDscpType33_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 33),
    _SysDscpType33_Type()
)
sysDscpType33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType33.setStatus("current")


class _SysDscpType34_Type(Integer32):
    """Custom type sysDscpType34 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType34_Type.__name__ = "Integer32"
_SysDscpType34_Object = MibScalar
sysDscpType34 = _SysDscpType34_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 34),
    _SysDscpType34_Type()
)
sysDscpType34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType34.setStatus("current")


class _SysDscpType35_Type(Integer32):
    """Custom type sysDscpType35 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType35_Type.__name__ = "Integer32"
_SysDscpType35_Object = MibScalar
sysDscpType35 = _SysDscpType35_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 35),
    _SysDscpType35_Type()
)
sysDscpType35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType35.setStatus("current")


class _SysDscpType36_Type(Integer32):
    """Custom type sysDscpType36 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType36_Type.__name__ = "Integer32"
_SysDscpType36_Object = MibScalar
sysDscpType36 = _SysDscpType36_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 36),
    _SysDscpType36_Type()
)
sysDscpType36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType36.setStatus("current")


class _SysDscpType37_Type(Integer32):
    """Custom type sysDscpType37 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType37_Type.__name__ = "Integer32"
_SysDscpType37_Object = MibScalar
sysDscpType37 = _SysDscpType37_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 37),
    _SysDscpType37_Type()
)
sysDscpType37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType37.setStatus("current")


class _SysDscpType38_Type(Integer32):
    """Custom type sysDscpType38 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType38_Type.__name__ = "Integer32"
_SysDscpType38_Object = MibScalar
sysDscpType38 = _SysDscpType38_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 38),
    _SysDscpType38_Type()
)
sysDscpType38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType38.setStatus("current")


class _SysDscpType39_Type(Integer32):
    """Custom type sysDscpType39 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType39_Type.__name__ = "Integer32"
_SysDscpType39_Object = MibScalar
sysDscpType39 = _SysDscpType39_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 39),
    _SysDscpType39_Type()
)
sysDscpType39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType39.setStatus("current")


class _SysDscpType40_Type(Integer32):
    """Custom type sysDscpType40 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType40_Type.__name__ = "Integer32"
_SysDscpType40_Object = MibScalar
sysDscpType40 = _SysDscpType40_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 40),
    _SysDscpType40_Type()
)
sysDscpType40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType40.setStatus("current")


class _SysDscpType41_Type(Integer32):
    """Custom type sysDscpType41 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType41_Type.__name__ = "Integer32"
_SysDscpType41_Object = MibScalar
sysDscpType41 = _SysDscpType41_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 41),
    _SysDscpType41_Type()
)
sysDscpType41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType41.setStatus("current")


class _SysDscpType42_Type(Integer32):
    """Custom type sysDscpType42 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType42_Type.__name__ = "Integer32"
_SysDscpType42_Object = MibScalar
sysDscpType42 = _SysDscpType42_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 42),
    _SysDscpType42_Type()
)
sysDscpType42.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType42.setStatus("current")


class _SysDscpType43_Type(Integer32):
    """Custom type sysDscpType43 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType43_Type.__name__ = "Integer32"
_SysDscpType43_Object = MibScalar
sysDscpType43 = _SysDscpType43_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 43),
    _SysDscpType43_Type()
)
sysDscpType43.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType43.setStatus("current")


class _SysDscpType44_Type(Integer32):
    """Custom type sysDscpType44 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType44_Type.__name__ = "Integer32"
_SysDscpType44_Object = MibScalar
sysDscpType44 = _SysDscpType44_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 44),
    _SysDscpType44_Type()
)
sysDscpType44.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType44.setStatus("current")


class _SysDscpType45_Type(Integer32):
    """Custom type sysDscpType45 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType45_Type.__name__ = "Integer32"
_SysDscpType45_Object = MibScalar
sysDscpType45 = _SysDscpType45_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 45),
    _SysDscpType45_Type()
)
sysDscpType45.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType45.setStatus("current")


class _SysDscpType46_Type(Integer32):
    """Custom type sysDscpType46 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType46_Type.__name__ = "Integer32"
_SysDscpType46_Object = MibScalar
sysDscpType46 = _SysDscpType46_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 46),
    _SysDscpType46_Type()
)
sysDscpType46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType46.setStatus("current")


class _SysDscpType47_Type(Integer32):
    """Custom type sysDscpType47 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType47_Type.__name__ = "Integer32"
_SysDscpType47_Object = MibScalar
sysDscpType47 = _SysDscpType47_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 47),
    _SysDscpType47_Type()
)
sysDscpType47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType47.setStatus("current")


class _SysDscpType48_Type(Integer32):
    """Custom type sysDscpType48 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType48_Type.__name__ = "Integer32"
_SysDscpType48_Object = MibScalar
sysDscpType48 = _SysDscpType48_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 48),
    _SysDscpType48_Type()
)
sysDscpType48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType48.setStatus("current")


class _SysDscpType49_Type(Integer32):
    """Custom type sysDscpType49 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType49_Type.__name__ = "Integer32"
_SysDscpType49_Object = MibScalar
sysDscpType49 = _SysDscpType49_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 49),
    _SysDscpType49_Type()
)
sysDscpType49.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType49.setStatus("current")


class _SysDscpType50_Type(Integer32):
    """Custom type sysDscpType50 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType50_Type.__name__ = "Integer32"
_SysDscpType50_Object = MibScalar
sysDscpType50 = _SysDscpType50_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 50),
    _SysDscpType50_Type()
)
sysDscpType50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType50.setStatus("current")


class _SysDscpType51_Type(Integer32):
    """Custom type sysDscpType51 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType51_Type.__name__ = "Integer32"
_SysDscpType51_Object = MibScalar
sysDscpType51 = _SysDscpType51_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 51),
    _SysDscpType51_Type()
)
sysDscpType51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType51.setStatus("current")


class _SysDscpType52_Type(Integer32):
    """Custom type sysDscpType52 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType52_Type.__name__ = "Integer32"
_SysDscpType52_Object = MibScalar
sysDscpType52 = _SysDscpType52_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 52),
    _SysDscpType52_Type()
)
sysDscpType52.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType52.setStatus("current")


class _SysDscpType53_Type(Integer32):
    """Custom type sysDscpType53 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType53_Type.__name__ = "Integer32"
_SysDscpType53_Object = MibScalar
sysDscpType53 = _SysDscpType53_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 53),
    _SysDscpType53_Type()
)
sysDscpType53.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType53.setStatus("current")


class _SysDscpType54_Type(Integer32):
    """Custom type sysDscpType54 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType54_Type.__name__ = "Integer32"
_SysDscpType54_Object = MibScalar
sysDscpType54 = _SysDscpType54_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 54),
    _SysDscpType54_Type()
)
sysDscpType54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType54.setStatus("current")


class _SysDscpType55_Type(Integer32):
    """Custom type sysDscpType55 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType55_Type.__name__ = "Integer32"
_SysDscpType55_Object = MibScalar
sysDscpType55 = _SysDscpType55_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 55),
    _SysDscpType55_Type()
)
sysDscpType55.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType55.setStatus("current")


class _SysDscpType56_Type(Integer32):
    """Custom type sysDscpType56 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType56_Type.__name__ = "Integer32"
_SysDscpType56_Object = MibScalar
sysDscpType56 = _SysDscpType56_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 56),
    _SysDscpType56_Type()
)
sysDscpType56.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType56.setStatus("current")


class _SysDscpType57_Type(Integer32):
    """Custom type sysDscpType57 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType57_Type.__name__ = "Integer32"
_SysDscpType57_Object = MibScalar
sysDscpType57 = _SysDscpType57_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 57),
    _SysDscpType57_Type()
)
sysDscpType57.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType57.setStatus("current")


class _SysDscpType58_Type(Integer32):
    """Custom type sysDscpType58 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType58_Type.__name__ = "Integer32"
_SysDscpType58_Object = MibScalar
sysDscpType58 = _SysDscpType58_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 58),
    _SysDscpType58_Type()
)
sysDscpType58.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType58.setStatus("current")


class _SysDscpType59_Type(Integer32):
    """Custom type sysDscpType59 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType59_Type.__name__ = "Integer32"
_SysDscpType59_Object = MibScalar
sysDscpType59 = _SysDscpType59_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 59),
    _SysDscpType59_Type()
)
sysDscpType59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType59.setStatus("current")


class _SysDscpType60_Type(Integer32):
    """Custom type sysDscpType60 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType60_Type.__name__ = "Integer32"
_SysDscpType60_Object = MibScalar
sysDscpType60 = _SysDscpType60_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 60),
    _SysDscpType60_Type()
)
sysDscpType60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType60.setStatus("current")


class _SysDscpType61_Type(Integer32):
    """Custom type sysDscpType61 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType61_Type.__name__ = "Integer32"
_SysDscpType61_Object = MibScalar
sysDscpType61 = _SysDscpType61_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 61),
    _SysDscpType61_Type()
)
sysDscpType61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType61.setStatus("current")


class _SysDscpType62_Type(Integer32):
    """Custom type sysDscpType62 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType62_Type.__name__ = "Integer32"
_SysDscpType62_Object = MibScalar
sysDscpType62 = _SysDscpType62_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 62),
    _SysDscpType62_Type()
)
sysDscpType62.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType62.setStatus("current")


class _SysDscpType63_Type(Integer32):
    """Custom type sysDscpType63 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType63_Type.__name__ = "Integer32"
_SysDscpType63_Object = MibScalar
sysDscpType63 = _SysDscpType63_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 63),
    _SysDscpType63_Type()
)
sysDscpType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType63.setStatus("current")


class _SysDscpType64_Type(Integer32):
    """Custom type sysDscpType64 based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_SysDscpType64_Type.__name__ = "Integer32"
_SysDscpType64_Object = MibScalar
sysDscpType64 = _SysDscpType64_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 100, 1, 2, 64),
    _SysDscpType64_Type()
)
sysDscpType64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDscpType64.setStatus("current")
_L2Snoop_ObjectIdentity = ObjectIdentity
l2Snoop = _L2Snoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105)
)
_SysSnoopInst_ObjectIdentity = ObjectIdentity
sysSnoopInst = _SysSnoopInst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2)
)
_SysSnoopInstanceGlobalTable_Object = MibTable
sysSnoopInstanceGlobalTable = _SysSnoopInstanceGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 1)
)
if mibBuilder.loadTexts:
    sysSnoopInstanceGlobalTable.setStatus("current")
_SysSnoopInstanceGlobalEntry_Object = MibTableRow
sysSnoopInstanceGlobalEntry = _SysSnoopInstanceGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 1, 1)
)
sysSnoopInstanceGlobalEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnoopInstanceGlobalInstId"),
)
if mibBuilder.loadTexts:
    sysSnoopInstanceGlobalEntry.setStatus("current")


class _SysSnoopInstanceGlobalInstId_Type(Integer32):
    """Custom type sysSnoopInstanceGlobalInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysSnoopInstanceGlobalInstId_Type.__name__ = "Integer32"
_SysSnoopInstanceGlobalInstId_Object = MibTableColumn
sysSnoopInstanceGlobalInstId = _SysSnoopInstanceGlobalInstId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 1, 1, 1),
    _SysSnoopInstanceGlobalInstId_Type()
)
sysSnoopInstanceGlobalInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopInstanceGlobalInstId.setStatus("current")


class _SysSnoopInstanceGlobalSystemControl_Type(Integer32):
    """Custom type sysSnoopInstanceGlobalSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("start", 1))
    )


_SysSnoopInstanceGlobalSystemControl_Type.__name__ = "Integer32"
_SysSnoopInstanceGlobalSystemControl_Object = MibTableColumn
sysSnoopInstanceGlobalSystemControl = _SysSnoopInstanceGlobalSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 1, 1, 3),
    _SysSnoopInstanceGlobalSystemControl_Type()
)
sysSnoopInstanceGlobalSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopInstanceGlobalSystemControl.setStatus("current")
_SysSnoopInstanceConfigTable_Object = MibTable
sysSnoopInstanceConfigTable = _SysSnoopInstanceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2)
)
if mibBuilder.loadTexts:
    sysSnoopInstanceConfigTable.setStatus("current")
_SysSnoopInstanceConfigEntry_Object = MibTableRow
sysSnoopInstanceConfigEntry = _SysSnoopInstanceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1)
)
sysSnoopInstanceConfigEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnoopInstanceConfigInstId"),
    (0, "AT-GS950-16-MIB", "sysSnoopInetAddressType"),
)
if mibBuilder.loadTexts:
    sysSnoopInstanceConfigEntry.setStatus("current")


class _SysSnoopInstanceConfigInstId_Type(Integer32):
    """Custom type sysSnoopInstanceConfigInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysSnoopInstanceConfigInstId_Type.__name__ = "Integer32"
_SysSnoopInstanceConfigInstId_Object = MibTableColumn
sysSnoopInstanceConfigInstId = _SysSnoopInstanceConfigInstId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 1),
    _SysSnoopInstanceConfigInstId_Type()
)
sysSnoopInstanceConfigInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopInstanceConfigInstId.setStatus("current")
_SysSnoopInetAddressType_Type = InetAddressType
_SysSnoopInetAddressType_Object = MibTableColumn
sysSnoopInetAddressType = _SysSnoopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 2),
    _SysSnoopInetAddressType_Type()
)
sysSnoopInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopInetAddressType.setStatus("current")


class _SysSnoopStatus_Type(Integer32):
    """Custom type sysSnoopStatus based on Integer32"""
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


_SysSnoopStatus_Type.__name__ = "Integer32"
_SysSnoopStatus_Object = MibTableColumn
sysSnoopStatus = _SysSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 3),
    _SysSnoopStatus_Type()
)
sysSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopStatus.setStatus("current")


class _SysSnoopRouterPortPurgeInterval_Type(Integer32):
    """Custom type sysSnoopRouterPortPurgeInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_SysSnoopRouterPortPurgeInterval_Type.__name__ = "Integer32"
_SysSnoopRouterPortPurgeInterval_Object = MibTableColumn
sysSnoopRouterPortPurgeInterval = _SysSnoopRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 5),
    _SysSnoopRouterPortPurgeInterval_Type()
)
sysSnoopRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopRouterPortPurgeInterval.setStatus("current")


class _SysSnoopPortPurgeInterval_Type(Integer32):
    """Custom type sysSnoopPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 1225),
    )


_SysSnoopPortPurgeInterval_Type.__name__ = "Integer32"
_SysSnoopPortPurgeInterval_Object = MibTableColumn
sysSnoopPortPurgeInterval = _SysSnoopPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 6),
    _SysSnoopPortPurgeInterval_Type()
)
sysSnoopPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopPortPurgeInterval.setStatus("current")


class _SysSnoopReportForwardInterval_Type(Integer32):
    """Custom type sysSnoopReportForwardInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SysSnoopReportForwardInterval_Type.__name__ = "Integer32"
_SysSnoopReportForwardInterval_Object = MibTableColumn
sysSnoopReportForwardInterval = _SysSnoopReportForwardInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 7),
    _SysSnoopReportForwardInterval_Type()
)
sysSnoopReportForwardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopReportForwardInterval.setStatus("current")


class _SysSnoopRetryCount_Type(Integer32):
    """Custom type sysSnoopRetryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysSnoopRetryCount_Type.__name__ = "Integer32"
_SysSnoopRetryCount_Object = MibTableColumn
sysSnoopRetryCount = _SysSnoopRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 8),
    _SysSnoopRetryCount_Type()
)
sysSnoopRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopRetryCount.setStatus("current")


class _SysSnoopGrpQueryInterval_Type(Integer32):
    """Custom type sysSnoopGrpQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysSnoopGrpQueryInterval_Type.__name__ = "Integer32"
_SysSnoopGrpQueryInterval_Object = MibTableColumn
sysSnoopGrpQueryInterval = _SysSnoopGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 9),
    _SysSnoopGrpQueryInterval_Type()
)
sysSnoopGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopGrpQueryInterval.setStatus("current")


class _SysSnoopReportFwdOnAllPorts_Type(Integer32):
    """Custom type sysSnoopReportFwdOnAllPorts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allports", 1),
          ("rtrports", 2))
    )


_SysSnoopReportFwdOnAllPorts_Type.__name__ = "Integer32"
_SysSnoopReportFwdOnAllPorts_Object = MibTableColumn
sysSnoopReportFwdOnAllPorts = _SysSnoopReportFwdOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 10),
    _SysSnoopReportFwdOnAllPorts_Type()
)
sysSnoopReportFwdOnAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopReportFwdOnAllPorts.setStatus("current")


class _SysSnoopOperStatus_Type(Integer32):
    """Custom type sysSnoopOperStatus based on Integer32"""
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


_SysSnoopOperStatus_Type.__name__ = "Integer32"
_SysSnoopOperStatus_Object = MibTableColumn
sysSnoopOperStatus = _SysSnoopOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 12),
    _SysSnoopOperStatus_Type()
)
sysSnoopOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopOperStatus.setStatus("current")


class _SysSnoopSendQueryOnTopoChange_Type(Integer32):
    """Custom type sysSnoopSendQueryOnTopoChange based on Integer32"""
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


_SysSnoopSendQueryOnTopoChange_Type.__name__ = "Integer32"
_SysSnoopSendQueryOnTopoChange_Object = MibTableColumn
sysSnoopSendQueryOnTopoChange = _SysSnoopSendQueryOnTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 13),
    _SysSnoopSendQueryOnTopoChange_Type()
)
sysSnoopSendQueryOnTopoChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopSendQueryOnTopoChange.setStatus("current")


class _SysSnoopQuerierQueryInterval_Type(Integer32):
    """Custom type sysSnoopQuerierQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_SysSnoopQuerierQueryInterval_Type.__name__ = "Integer32"
_SysSnoopQuerierQueryInterval_Object = MibTableColumn
sysSnoopQuerierQueryInterval = _SysSnoopQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 2, 2, 1, 16),
    _SysSnoopQuerierQueryInterval_Type()
)
sysSnoopQuerierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopQuerierQueryInterval.setStatus("current")
_SysSnoopVlan_ObjectIdentity = ObjectIdentity
sysSnoopVlan = _SysSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3)
)
_SysSnoopVlanMcastMacFwdTable_Object = MibTable
sysSnoopVlanMcastMacFwdTable = _SysSnoopVlanMcastMacFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1)
)
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdTable.setStatus("current")
_SysSnoopVlanMcastMacFwdEntry_Object = MibTableRow
sysSnoopVlanMcastMacFwdEntry = _SysSnoopVlanMcastMacFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1, 1)
)
sysSnoopVlanMcastMacFwdEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnoopVlanMcastMacFwdInstId"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanMcastMacFwdVlanId"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanMcastMacFwdInetAddressType"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanMcastMacFwdGroupAddress"),
)
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdEntry.setStatus("current")


class _SysSnoopVlanMcastMacFwdInstId_Type(Integer32):
    """Custom type sysSnoopVlanMcastMacFwdInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysSnoopVlanMcastMacFwdInstId_Type.__name__ = "Integer32"
_SysSnoopVlanMcastMacFwdInstId_Object = MibTableColumn
sysSnoopVlanMcastMacFwdInstId = _SysSnoopVlanMcastMacFwdInstId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1, 1, 1),
    _SysSnoopVlanMcastMacFwdInstId_Type()
)
sysSnoopVlanMcastMacFwdInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdInstId.setStatus("current")


class _SysSnoopVlanMcastMacFwdVlanId_Type(Integer32):
    """Custom type sysSnoopVlanMcastMacFwdVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysSnoopVlanMcastMacFwdVlanId_Type.__name__ = "Integer32"
_SysSnoopVlanMcastMacFwdVlanId_Object = MibTableColumn
sysSnoopVlanMcastMacFwdVlanId = _SysSnoopVlanMcastMacFwdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1, 1, 2),
    _SysSnoopVlanMcastMacFwdVlanId_Type()
)
sysSnoopVlanMcastMacFwdVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdVlanId.setStatus("current")
_SysSnoopVlanMcastMacFwdInetAddressType_Type = InetAddressType
_SysSnoopVlanMcastMacFwdInetAddressType_Object = MibTableColumn
sysSnoopVlanMcastMacFwdInetAddressType = _SysSnoopVlanMcastMacFwdInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1, 1, 3),
    _SysSnoopVlanMcastMacFwdInetAddressType_Type()
)
sysSnoopVlanMcastMacFwdInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdInetAddressType.setStatus("current")
_SysSnoopVlanMcastMacFwdGroupAddress_Type = MacAddress
_SysSnoopVlanMcastMacFwdGroupAddress_Object = MibTableColumn
sysSnoopVlanMcastMacFwdGroupAddress = _SysSnoopVlanMcastMacFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1, 1, 4),
    _SysSnoopVlanMcastMacFwdGroupAddress_Type()
)
sysSnoopVlanMcastMacFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdGroupAddress.setStatus("current")
_SysSnoopVlanMcastMacFwdPortList_Type = PortList
_SysSnoopVlanMcastMacFwdPortList_Object = MibTableColumn
sysSnoopVlanMcastMacFwdPortList = _SysSnoopVlanMcastMacFwdPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 1, 1, 5),
    _SysSnoopVlanMcastMacFwdPortList_Type()
)
sysSnoopVlanMcastMacFwdPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopVlanMcastMacFwdPortList.setStatus("current")
_SysSnoopVlanRouterTable_Object = MibTable
sysSnoopVlanRouterTable = _SysSnoopVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 3)
)
if mibBuilder.loadTexts:
    sysSnoopVlanRouterTable.setStatus("current")
_SysSnoopVlanRouterEntry_Object = MibTableRow
sysSnoopVlanRouterEntry = _SysSnoopVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 3, 1)
)
sysSnoopVlanRouterEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnoopVlanRouterInstId"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanRouterVlanId"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanRouterInetAddressType"),
)
if mibBuilder.loadTexts:
    sysSnoopVlanRouterEntry.setStatus("current")


class _SysSnoopVlanRouterInstId_Type(Integer32):
    """Custom type sysSnoopVlanRouterInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysSnoopVlanRouterInstId_Type.__name__ = "Integer32"
_SysSnoopVlanRouterInstId_Object = MibTableColumn
sysSnoopVlanRouterInstId = _SysSnoopVlanRouterInstId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 3, 1, 1),
    _SysSnoopVlanRouterInstId_Type()
)
sysSnoopVlanRouterInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanRouterInstId.setStatus("current")


class _SysSnoopVlanRouterVlanId_Type(Integer32):
    """Custom type sysSnoopVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysSnoopVlanRouterVlanId_Type.__name__ = "Integer32"
_SysSnoopVlanRouterVlanId_Object = MibTableColumn
sysSnoopVlanRouterVlanId = _SysSnoopVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 3, 1, 2),
    _SysSnoopVlanRouterVlanId_Type()
)
sysSnoopVlanRouterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanRouterVlanId.setStatus("current")
_SysSnoopVlanRouterInetAddressType_Type = InetAddressType
_SysSnoopVlanRouterInetAddressType_Object = MibTableColumn
sysSnoopVlanRouterInetAddressType = _SysSnoopVlanRouterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 3, 1, 3),
    _SysSnoopVlanRouterInetAddressType_Type()
)
sysSnoopVlanRouterInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanRouterInetAddressType.setStatus("current")
_SysSnoopVlanRouterPortList_Type = PortList
_SysSnoopVlanRouterPortList_Object = MibTableColumn
sysSnoopVlanRouterPortList = _SysSnoopVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 3, 1, 4),
    _SysSnoopVlanRouterPortList_Type()
)
sysSnoopVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopVlanRouterPortList.setStatus("current")
_SysSnoopVlanFilterTable_Object = MibTable
sysSnoopVlanFilterTable = _SysSnoopVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4)
)
if mibBuilder.loadTexts:
    sysSnoopVlanFilterTable.setStatus("current")
_SysSnoopVlanFilterEntry_Object = MibTableRow
sysSnoopVlanFilterEntry = _SysSnoopVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1)
)
sysSnoopVlanFilterEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnoopVlanFilterInstId"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanFilterVlanId"),
    (0, "AT-GS950-16-MIB", "sysSnoopVlanFilterInetAddressType"),
)
if mibBuilder.loadTexts:
    sysSnoopVlanFilterEntry.setStatus("current")


class _SysSnoopVlanFilterInstId_Type(Integer32):
    """Custom type sysSnoopVlanFilterInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysSnoopVlanFilterInstId_Type.__name__ = "Integer32"
_SysSnoopVlanFilterInstId_Object = MibTableColumn
sysSnoopVlanFilterInstId = _SysSnoopVlanFilterInstId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 1),
    _SysSnoopVlanFilterInstId_Type()
)
sysSnoopVlanFilterInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanFilterInstId.setStatus("current")


class _SysSnoopVlanFilterVlanId_Type(Integer32):
    """Custom type sysSnoopVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysSnoopVlanFilterVlanId_Type.__name__ = "Integer32"
_SysSnoopVlanFilterVlanId_Object = MibTableColumn
sysSnoopVlanFilterVlanId = _SysSnoopVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 2),
    _SysSnoopVlanFilterVlanId_Type()
)
sysSnoopVlanFilterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanFilterVlanId.setStatus("current")
_SysSnoopVlanFilterInetAddressType_Type = InetAddressType
_SysSnoopVlanFilterInetAddressType_Object = MibTableColumn
sysSnoopVlanFilterInetAddressType = _SysSnoopVlanFilterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 3),
    _SysSnoopVlanFilterInetAddressType_Type()
)
sysSnoopVlanFilterInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopVlanFilterInetAddressType.setStatus("current")


class _SysSnoopVlanSnoopStatus_Type(Integer32):
    """Custom type sysSnoopVlanSnoopStatus based on Integer32"""
    defaultValue = 1

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


_SysSnoopVlanSnoopStatus_Type.__name__ = "Integer32"
_SysSnoopVlanSnoopStatus_Object = MibTableColumn
sysSnoopVlanSnoopStatus = _SysSnoopVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 4),
    _SysSnoopVlanSnoopStatus_Type()
)
sysSnoopVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopVlanSnoopStatus.setStatus("current")


class _SysSnoopVlanOperatingVersion_Type(Integer32):
    """Custom type sysSnoopVlanOperatingVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_SysSnoopVlanOperatingVersion_Type.__name__ = "Integer32"
_SysSnoopVlanOperatingVersion_Object = MibTableColumn
sysSnoopVlanOperatingVersion = _SysSnoopVlanOperatingVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 5),
    _SysSnoopVlanOperatingVersion_Type()
)
sysSnoopVlanOperatingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopVlanOperatingVersion.setStatus("current")


class _SysSnoopVlanFastLeave_Type(Integer32):
    """Custom type sysSnoopVlanFastLeave based on Integer32"""
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


_SysSnoopVlanFastLeave_Type.__name__ = "Integer32"
_SysSnoopVlanFastLeave_Object = MibTableColumn
sysSnoopVlanFastLeave = _SysSnoopVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 7),
    _SysSnoopVlanFastLeave_Type()
)
sysSnoopVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopVlanFastLeave.setStatus("current")


class _SysSnoopVlanQuerier_Type(Integer32):
    """Custom type sysSnoopVlanQuerier based on Integer32"""
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


_SysSnoopVlanQuerier_Type.__name__ = "Integer32"
_SysSnoopVlanQuerier_Object = MibTableColumn
sysSnoopVlanQuerier = _SysSnoopVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 8),
    _SysSnoopVlanQuerier_Type()
)
sysSnoopVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopVlanQuerier.setStatus("current")


class _SysSnoopVlanCfgQuerier_Type(Integer32):
    """Custom type sysSnoopVlanCfgQuerier based on Integer32"""
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


_SysSnoopVlanCfgQuerier_Type.__name__ = "Integer32"
_SysSnoopVlanCfgQuerier_Object = MibTableColumn
sysSnoopVlanCfgQuerier = _SysSnoopVlanCfgQuerier_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 9),
    _SysSnoopVlanCfgQuerier_Type()
)
sysSnoopVlanCfgQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopVlanCfgQuerier.setStatus("current")


class _SysSnoopVlanQueryInterval_Type(Integer32):
    """Custom type sysSnoopVlanQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_SysSnoopVlanQueryInterval_Type.__name__ = "Integer32"
_SysSnoopVlanQueryInterval_Object = MibTableColumn
sysSnoopVlanQueryInterval = _SysSnoopVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 10),
    _SysSnoopVlanQueryInterval_Type()
)
sysSnoopVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopVlanQueryInterval.setStatus("current")
_SysSnoopVlanRtrPortList_Type = PortList
_SysSnoopVlanRtrPortList_Object = MibTableColumn
sysSnoopVlanRtrPortList = _SysSnoopVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 11),
    _SysSnoopVlanRtrPortList_Type()
)
sysSnoopVlanRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnoopVlanRtrPortList.setStatus("current")
_SysSnoopVlanRowStatus_Type = RowStatus
_SysSnoopVlanRowStatus_Object = MibTableColumn
sysSnoopVlanRowStatus = _SysSnoopVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 3, 4, 1, 12),
    _SysSnoopVlanRowStatus_Type()
)
sysSnoopVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysSnoopVlanRowStatus.setStatus("current")
_SysSnoopStats_ObjectIdentity = ObjectIdentity
sysSnoopStats = _SysSnoopStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4)
)
_SysSnoopStatsTable_Object = MibTable
sysSnoopStatsTable = _SysSnoopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1)
)
if mibBuilder.loadTexts:
    sysSnoopStatsTable.setStatus("current")
_SysSnoopStatsEntry_Object = MibTableRow
sysSnoopStatsEntry = _SysSnoopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1)
)
sysSnoopStatsEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "sysSnoopStatsInstId"),
    (0, "AT-GS950-16-MIB", "sysSnoopStatsVlanId"),
    (0, "AT-GS950-16-MIB", "sysSnoopStatsInetAddressType"),
)
if mibBuilder.loadTexts:
    sysSnoopStatsEntry.setStatus("current")


class _SysSnoopStatsInstId_Type(Integer32):
    """Custom type sysSnoopStatsInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysSnoopStatsInstId_Type.__name__ = "Integer32"
_SysSnoopStatsInstId_Object = MibTableColumn
sysSnoopStatsInstId = _SysSnoopStatsInstId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 1),
    _SysSnoopStatsInstId_Type()
)
sysSnoopStatsInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopStatsInstId.setStatus("current")


class _SysSnoopStatsVlanId_Type(Integer32):
    """Custom type sysSnoopStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysSnoopStatsVlanId_Type.__name__ = "Integer32"
_SysSnoopStatsVlanId_Object = MibTableColumn
sysSnoopStatsVlanId = _SysSnoopStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 2),
    _SysSnoopStatsVlanId_Type()
)
sysSnoopStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopStatsVlanId.setStatus("current")
_SysSnoopStatsInetAddressType_Type = InetAddressType
_SysSnoopStatsInetAddressType_Object = MibTableColumn
sysSnoopStatsInetAddressType = _SysSnoopStatsInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 3),
    _SysSnoopStatsInetAddressType_Type()
)
sysSnoopStatsInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysSnoopStatsInetAddressType.setStatus("current")
_SysSnoopStatsRxGenQueries_Type = Counter32
_SysSnoopStatsRxGenQueries_Object = MibTableColumn
sysSnoopStatsRxGenQueries = _SysSnoopStatsRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 4),
    _SysSnoopStatsRxGenQueries_Type()
)
sysSnoopStatsRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsRxGenQueries.setStatus("current")
_SysSnoopStatsRxGrpQueries_Type = Counter32
_SysSnoopStatsRxGrpQueries_Object = MibTableColumn
sysSnoopStatsRxGrpQueries = _SysSnoopStatsRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 5),
    _SysSnoopStatsRxGrpQueries_Type()
)
sysSnoopStatsRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsRxGrpQueries.setStatus("current")
_SysSnoopStatsRxAsmReports_Type = Counter32
_SysSnoopStatsRxAsmReports_Object = MibTableColumn
sysSnoopStatsRxAsmReports = _SysSnoopStatsRxAsmReports_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 7),
    _SysSnoopStatsRxAsmReports_Type()
)
sysSnoopStatsRxAsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsRxAsmReports.setStatus("current")
_SysSnoopStatsRxAsmLeaves_Type = Counter32
_SysSnoopStatsRxAsmLeaves_Object = MibTableColumn
sysSnoopStatsRxAsmLeaves = _SysSnoopStatsRxAsmLeaves_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 15),
    _SysSnoopStatsRxAsmLeaves_Type()
)
sysSnoopStatsRxAsmLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsRxAsmLeaves.setStatus("current")
_SysSnoopStatsTxGenQueries_Type = Counter32
_SysSnoopStatsTxGenQueries_Object = MibTableColumn
sysSnoopStatsTxGenQueries = _SysSnoopStatsTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 16),
    _SysSnoopStatsTxGenQueries_Type()
)
sysSnoopStatsTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsTxGenQueries.setStatus("current")
_SysSnoopStatsTxGrpQueries_Type = Counter32
_SysSnoopStatsTxGrpQueries_Object = MibTableColumn
sysSnoopStatsTxGrpQueries = _SysSnoopStatsTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 17),
    _SysSnoopStatsTxGrpQueries_Type()
)
sysSnoopStatsTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsTxGrpQueries.setStatus("current")
_SysSnoopStatsTxAsmReports_Type = Counter32
_SysSnoopStatsTxAsmReports_Object = MibTableColumn
sysSnoopStatsTxAsmReports = _SysSnoopStatsTxAsmReports_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 18),
    _SysSnoopStatsTxAsmReports_Type()
)
sysSnoopStatsTxAsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsTxAsmReports.setStatus("current")
_SysSnoopStatsTxAsmLeaves_Type = Counter32
_SysSnoopStatsTxAsmLeaves_Object = MibTableColumn
sysSnoopStatsTxAsmLeaves = _SysSnoopStatsTxAsmLeaves_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 20),
    _SysSnoopStatsTxAsmLeaves_Type()
)
sysSnoopStatsTxAsmLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsTxAsmLeaves.setStatus("current")
_SysSnoopStatsDroppedPkts_Type = Counter32
_SysSnoopStatsDroppedPkts_Object = MibTableColumn
sysSnoopStatsDroppedPkts = _SysSnoopStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 105, 4, 1, 1, 21),
    _SysSnoopStatsDroppedPkts_Type()
)
sysSnoopStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnoopStatsDroppedPkts.setStatus("current")
_L2Bridge_ObjectIdentity = ObjectIdentity
l2Bridge = _L2Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116)
)
_Dot1dNotifications_ObjectIdentity = ObjectIdentity
dot1dNotifications = _Dot1dNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 0)
)
_Dot1dBase_ObjectIdentity = ObjectIdentity
dot1dBase = _Dot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1)
)
_Dot1dBaseTable_Object = MibTable
dot1dBaseTable = _Dot1dBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dBaseTable.setStatus("current")
_Dot1dBaseEntry_Object = MibTableRow
dot1dBaseEntry = _Dot1dBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 1, 1)
)
dot1dBaseEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBaseContextId"),
)
if mibBuilder.loadTexts:
    dot1dBaseEntry.setStatus("current")


class _Dot1dBaseContextId_Type(Integer32):
    """Custom type dot1dBaseContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dBaseContextId_Type.__name__ = "Integer32"
_Dot1dBaseContextId_Object = MibTableColumn
dot1dBaseContextId = _Dot1dBaseContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 1, 1, 1),
    _Dot1dBaseContextId_Type()
)
dot1dBaseContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dBaseContextId.setStatus("current")
_Dot1dBaseBridgeAddress_Type = MacAddress
_Dot1dBaseBridgeAddress_Object = MibTableColumn
dot1dBaseBridgeAddress = _Dot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 1, 1, 2),
    _Dot1dBaseBridgeAddress_Type()
)
dot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseBridgeAddress.setStatus("current")
_Dot1dBaseNumPorts_Type = Integer32
_Dot1dBaseNumPorts_Object = MibTableColumn
dot1dBaseNumPorts = _Dot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 1, 1, 3),
    _Dot1dBaseNumPorts_Type()
)
dot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseNumPorts.setStatus("current")


class _Dot1dBaseType_Type(Integer32):
    """Custom type dot1dBaseType based on Integer32"""
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
        *(("sourcerouteonly", 3),
          ("srt", 4),
          ("transparentonly", 2),
          ("unknown", 1))
    )


_Dot1dBaseType_Type.__name__ = "Integer32"
_Dot1dBaseType_Object = MibTableColumn
dot1dBaseType = _Dot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 1, 1, 4),
    _Dot1dBaseType_Type()
)
dot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseType.setStatus("current")
_Dot1dBasePortTable_Object = MibTable
dot1dBasePortTable = _Dot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2)
)
if mibBuilder.loadTexts:
    dot1dBasePortTable.setStatus("current")
_Dot1dBasePortEntry_Object = MibTableRow
dot1dBasePortEntry = _Dot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2, 1)
)
dot1dBasePortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dBasePortEntry.setStatus("current")


class _Dot1dBasePort_Type(Integer32):
    """Custom type dot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dBasePort_Type.__name__ = "Integer32"
_Dot1dBasePort_Object = MibTableColumn
dot1dBasePort = _Dot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2, 1, 1),
    _Dot1dBasePort_Type()
)
dot1dBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dBasePort.setStatus("current")
_Dot1dBasePortIfIndex_Type = Integer32
_Dot1dBasePortIfIndex_Object = MibTableColumn
dot1dBasePortIfIndex = _Dot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2, 1, 2),
    _Dot1dBasePortIfIndex_Type()
)
dot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortIfIndex.setStatus("current")
_Dot1dBasePortCircuit_Type = ObjectIdentifier
_Dot1dBasePortCircuit_Object = MibTableColumn
dot1dBasePortCircuit = _Dot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2, 1, 3),
    _Dot1dBasePortCircuit_Type()
)
dot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortCircuit.setStatus("current")
_Dot1dBasePortDelayExceededDiscards_Type = Counter32
_Dot1dBasePortDelayExceededDiscards_Object = MibTableColumn
dot1dBasePortDelayExceededDiscards = _Dot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2, 1, 4),
    _Dot1dBasePortDelayExceededDiscards_Type()
)
dot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortDelayExceededDiscards.setStatus("current")
_Dot1dBasePortMtuExceededDiscards_Type = Counter32
_Dot1dBasePortMtuExceededDiscards_Object = MibTableColumn
dot1dBasePortMtuExceededDiscards = _Dot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 1, 2, 1, 5),
    _Dot1dBasePortMtuExceededDiscards_Type()
)
dot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortMtuExceededDiscards.setStatus("current")
_L2Dot1dStp_ObjectIdentity = ObjectIdentity
l2Dot1dStp = _L2Dot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2)
)
_Dot1dStpTable_Object = MibTable
dot1dStpTable = _Dot1dStpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dStpTable.setStatus("current")
_Dot1dStpEntry_Object = MibTableRow
dot1dStpEntry = _Dot1dStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1)
)
dot1dStpEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dStpContextId"),
)
if mibBuilder.loadTexts:
    dot1dStpEntry.setStatus("current")


class _Dot1dStpContextId_Type(Integer32):
    """Custom type dot1dStpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStpContextId_Type.__name__ = "Integer32"
_Dot1dStpContextId_Object = MibTableColumn
dot1dStpContextId = _Dot1dStpContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 1),
    _Dot1dStpContextId_Type()
)
dot1dStpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dStpContextId.setStatus("current")


class _Dot1dStpProtocolSpecification_Type(Integer32):
    """Custom type dot1dStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_Dot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_Dot1dStpProtocolSpecification_Object = MibTableColumn
dot1dStpProtocolSpecification = _Dot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 2),
    _Dot1dStpProtocolSpecification_Type()
)
dot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpProtocolSpecification.setStatus("current")


class _Dot1dStpPriority_Type(Integer32):
    """Custom type dot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStpPriority_Type.__name__ = "Integer32"
_Dot1dStpPriority_Object = MibTableColumn
dot1dStpPriority = _Dot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 3),
    _Dot1dStpPriority_Type()
)
dot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPriority.setStatus("current")
_Dot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Dot1dStpTimeSinceTopologyChange_Object = MibTableColumn
dot1dStpTimeSinceTopologyChange = _Dot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 4),
    _Dot1dStpTimeSinceTopologyChange_Type()
)
dot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTimeSinceTopologyChange.setStatus("current")
_Dot1dStpTopChanges_Type = Counter32
_Dot1dStpTopChanges_Object = MibTableColumn
dot1dStpTopChanges = _Dot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 5),
    _Dot1dStpTopChanges_Type()
)
dot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTopChanges.setStatus("current")
_Dot1dStpDesignatedRoot_Type = BridgeId
_Dot1dStpDesignatedRoot_Object = MibTableColumn
dot1dStpDesignatedRoot = _Dot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 6),
    _Dot1dStpDesignatedRoot_Type()
)
dot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpDesignatedRoot.setStatus("current")
_Dot1dStpRootCost_Type = Integer32
_Dot1dStpRootCost_Object = MibTableColumn
dot1dStpRootCost = _Dot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 7),
    _Dot1dStpRootCost_Type()
)
dot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootCost.setStatus("current")
_Dot1dStpRootPort_Type = Integer32
_Dot1dStpRootPort_Object = MibTableColumn
dot1dStpRootPort = _Dot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 8),
    _Dot1dStpRootPort_Type()
)
dot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootPort.setStatus("current")
_Dot1dStpMaxAge_Type = Timeout
_Dot1dStpMaxAge_Object = MibTableColumn
dot1dStpMaxAge = _Dot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 9),
    _Dot1dStpMaxAge_Type()
)
dot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpMaxAge.setStatus("current")
_Dot1dStpHelloTime_Type = Timeout
_Dot1dStpHelloTime_Object = MibTableColumn
dot1dStpHelloTime = _Dot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 10),
    _Dot1dStpHelloTime_Type()
)
dot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHelloTime.setStatus("current")
_Dot1dStpHoldTime_Type = Integer32
_Dot1dStpHoldTime_Object = MibTableColumn
dot1dStpHoldTime = _Dot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 11),
    _Dot1dStpHoldTime_Type()
)
dot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHoldTime.setStatus("current")
_Dot1dStpForwardDelay_Type = Timeout
_Dot1dStpForwardDelay_Object = MibTableColumn
dot1dStpForwardDelay = _Dot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 12),
    _Dot1dStpForwardDelay_Type()
)
dot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpForwardDelay.setStatus("current")


class _Dot1dStpBridgeMaxAge_Type(Timeout):
    """Custom type dot1dStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Dot1dStpBridgeMaxAge_Type.__name__ = "Timeout"
_Dot1dStpBridgeMaxAge_Object = MibTableColumn
dot1dStpBridgeMaxAge = _Dot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 13),
    _Dot1dStpBridgeMaxAge_Type()
)
dot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeMaxAge.setStatus("current")


class _Dot1dStpBridgeHelloTime_Type(Timeout):
    """Custom type dot1dStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_Dot1dStpBridgeHelloTime_Type.__name__ = "Timeout"
_Dot1dStpBridgeHelloTime_Object = MibTableColumn
dot1dStpBridgeHelloTime = _Dot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 14),
    _Dot1dStpBridgeHelloTime_Type()
)
dot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeHelloTime.setStatus("current")


class _Dot1dStpBridgeForwardDelay_Type(Timeout):
    """Custom type dot1dStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Dot1dStpBridgeForwardDelay_Type.__name__ = "Timeout"
_Dot1dStpBridgeForwardDelay_Object = MibTableColumn
dot1dStpBridgeForwardDelay = _Dot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 1, 1, 15),
    _Dot1dStpBridgeForwardDelay_Type()
)
dot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeForwardDelay.setStatus("current")
_Dot1dStpPortTable_Object = MibTable
dot1dStpPortTable = _Dot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2)
)
if mibBuilder.loadTexts:
    dot1dStpPortTable.setStatus("current")
_Dot1dStpPortEntry_Object = MibTableRow
dot1dStpPortEntry = _Dot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1)
)
dot1dStpPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    dot1dStpPortEntry.setStatus("current")


class _Dot1dStpPort_Type(Integer32):
    """Custom type dot1dStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dStpPort_Type.__name__ = "Integer32"
_Dot1dStpPort_Object = MibTableColumn
dot1dStpPort = _Dot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 1),
    _Dot1dStpPort_Type()
)
dot1dStpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dStpPort.setStatus("current")


class _Dot1dStpPortPriority_Type(Integer32):
    """Custom type dot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1dStpPortPriority_Type.__name__ = "Integer32"
_Dot1dStpPortPriority_Object = MibTableColumn
dot1dStpPortPriority = _Dot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 2),
    _Dot1dStpPortPriority_Type()
)
dot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPriority.setStatus("current")


class _Dot1dStpPortState_Type(Integer32):
    """Custom type dot1dStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Dot1dStpPortState_Type.__name__ = "Integer32"
_Dot1dStpPortState_Object = MibTableColumn
dot1dStpPortState = _Dot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 3),
    _Dot1dStpPortState_Type()
)
dot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortState.setStatus("current")


class _Dot1dStpPortEnable_Type(Integer32):
    """Custom type dot1dStpPortEnable based on Integer32"""
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


_Dot1dStpPortEnable_Type.__name__ = "Integer32"
_Dot1dStpPortEnable_Object = MibTableColumn
dot1dStpPortEnable = _Dot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 4),
    _Dot1dStpPortEnable_Type()
)
dot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortEnable.setStatus("current")


class _Dot1dStpPortPathCost_Type(Integer32):
    """Custom type dot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dStpPortPathCost_Type.__name__ = "Integer32"
_Dot1dStpPortPathCost_Object = MibTableColumn
dot1dStpPortPathCost = _Dot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 5),
    _Dot1dStpPortPathCost_Type()
)
dot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPathCost.setStatus("current")
_Dot1dStpPortDesignatedRoot_Type = BridgeId
_Dot1dStpPortDesignatedRoot_Object = MibTableColumn
dot1dStpPortDesignatedRoot = _Dot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 6),
    _Dot1dStpPortDesignatedRoot_Type()
)
dot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedRoot.setStatus("current")
_Dot1dStpPortDesignatedCost_Type = Integer32
_Dot1dStpPortDesignatedCost_Object = MibTableColumn
dot1dStpPortDesignatedCost = _Dot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 7),
    _Dot1dStpPortDesignatedCost_Type()
)
dot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedCost.setStatus("current")
_Dot1dStpPortDesignatedBridge_Type = BridgeId
_Dot1dStpPortDesignatedBridge_Object = MibTableColumn
dot1dStpPortDesignatedBridge = _Dot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 8),
    _Dot1dStpPortDesignatedBridge_Type()
)
dot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedBridge.setStatus("current")


class _Dot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type dot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Dot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Dot1dStpPortDesignatedPort_Object = MibTableColumn
dot1dStpPortDesignatedPort = _Dot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 9),
    _Dot1dStpPortDesignatedPort_Type()
)
dot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedPort.setStatus("current")
_Dot1dStpPortForwardTransitions_Type = Counter32
_Dot1dStpPortForwardTransitions_Object = MibTableColumn
dot1dStpPortForwardTransitions = _Dot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 2, 1, 10),
    _Dot1dStpPortForwardTransitions_Type()
)
dot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortForwardTransitions.setStatus("current")
_Dot1dStpExtTable_Object = MibTable
dot1dStpExtTable = _Dot1dStpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 3)
)
if mibBuilder.loadTexts:
    dot1dStpExtTable.setStatus("current")
_Dot1dStpExtEntry_Object = MibTableRow
dot1dStpExtEntry = _Dot1dStpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dStpExtEntry.setStatus("current")


class _Dot1dStpVersion_Type(Integer32):
    """Custom type dot1dStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_Dot1dStpVersion_Type.__name__ = "Integer32"
_Dot1dStpVersion_Object = MibTableColumn
dot1dStpVersion = _Dot1dStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 3, 1, 1),
    _Dot1dStpVersion_Type()
)
dot1dStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpVersion.setStatus("current")


class _Dot1dStpTxHoldCount_Type(Integer32):
    """Custom type dot1dStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1dStpTxHoldCount_Type.__name__ = "Integer32"
_Dot1dStpTxHoldCount_Object = MibTableColumn
dot1dStpTxHoldCount = _Dot1dStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 3, 1, 2),
    _Dot1dStpTxHoldCount_Type()
)
dot1dStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpTxHoldCount.setStatus("current")


class _Dot1dStpPathCostDefault_Type(Integer32):
    """Custom type dot1dStpPathCostDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_Dot1dStpPathCostDefault_Type.__name__ = "Integer32"
_Dot1dStpPathCostDefault_Object = MibTableColumn
dot1dStpPathCostDefault = _Dot1dStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 3, 1, 3),
    _Dot1dStpPathCostDefault_Type()
)
dot1dStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPathCostDefault.setStatus("current")
_Dot1dStpExtPortTable_Object = MibTable
dot1dStpExtPortTable = _Dot1dStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4)
)
if mibBuilder.loadTexts:
    dot1dStpExtPortTable.setStatus("current")
_Dot1dStpExtPortEntry_Object = MibTableRow
dot1dStpExtPortEntry = _Dot1dStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dot1dStpExtPortEntry.setStatus("current")
_Dot1dStpPortProtocolMigration_Type = TruthValue
_Dot1dStpPortProtocolMigration_Object = MibTableColumn
dot1dStpPortProtocolMigration = _Dot1dStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4, 1, 1),
    _Dot1dStpPortProtocolMigration_Type()
)
dot1dStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortProtocolMigration.setStatus("current")
_Dot1dStpPortAdminEdgePort_Type = TruthValue
_Dot1dStpPortAdminEdgePort_Object = MibTableColumn
dot1dStpPortAdminEdgePort = _Dot1dStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4, 1, 2),
    _Dot1dStpPortAdminEdgePort_Type()
)
dot1dStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortAdminEdgePort.setStatus("current")
_Dot1dStpPortOperEdgePort_Type = TruthValue
_Dot1dStpPortOperEdgePort_Object = MibTableColumn
dot1dStpPortOperEdgePort = _Dot1dStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4, 1, 3),
    _Dot1dStpPortOperEdgePort_Type()
)
dot1dStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortOperEdgePort.setStatus("current")


class _Dot1dStpPortAdminPointToPoint_Type(Integer32):
    """Custom type dot1dStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_Dot1dStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_Dot1dStpPortAdminPointToPoint_Object = MibTableColumn
dot1dStpPortAdminPointToPoint = _Dot1dStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4, 1, 4),
    _Dot1dStpPortAdminPointToPoint_Type()
)
dot1dStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortAdminPointToPoint.setStatus("current")
_Dot1dStpPortOperPointToPoint_Type = TruthValue
_Dot1dStpPortOperPointToPoint_Object = MibTableColumn
dot1dStpPortOperPointToPoint = _Dot1dStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 2, 4, 1, 5),
    _Dot1dStpPortOperPointToPoint_Type()
)
dot1dStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortOperPointToPoint.setStatus("current")
_Dot1dSr_ObjectIdentity = ObjectIdentity
dot1dSr = _Dot1dSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 3)
)
_Dot1dTp_ObjectIdentity = ObjectIdentity
dot1dTp = _Dot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4)
)
_Dot1dTpTable_Object = MibTable
dot1dTpTable = _Dot1dTpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 1)
)
if mibBuilder.loadTexts:
    dot1dTpTable.setStatus("current")
_Dot1dTpEntry_Object = MibTableRow
dot1dTpEntry = _Dot1dTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 1, 1)
)
dot1dTpEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBaseContextId"),
)
if mibBuilder.loadTexts:
    dot1dTpEntry.setStatus("current")
_Dot1dTpLearnedEntryDiscards_Type = Counter32
_Dot1dTpLearnedEntryDiscards_Object = MibTableColumn
dot1dTpLearnedEntryDiscards = _Dot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 1, 1, 1),
    _Dot1dTpLearnedEntryDiscards_Type()
)
dot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpLearnedEntryDiscards.setStatus("current")


class _Dot1dTpAgingTime_Type(Integer32):
    """Custom type dot1dTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_Dot1dTpAgingTime_Type.__name__ = "Integer32"
_Dot1dTpAgingTime_Object = MibTableColumn
dot1dTpAgingTime = _Dot1dTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 1, 1, 2),
    _Dot1dTpAgingTime_Type()
)
dot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTpAgingTime.setStatus("current")
_Dot1dTpFdbTable_Object = MibTable
dot1dTpFdbTable = _Dot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 2)
)
if mibBuilder.loadTexts:
    dot1dTpFdbTable.setStatus("current")
_Dot1dTpFdbEntry_Object = MibTableRow
dot1dTpFdbEntry = _Dot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 2, 1)
)
dot1dTpFdbEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBaseContextId"),
    (0, "AT-GS950-16-MIB", "dot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    dot1dTpFdbEntry.setStatus("current")
_Dot1dTpFdbAddress_Type = MacAddress
_Dot1dTpFdbAddress_Object = MibTableColumn
dot1dTpFdbAddress = _Dot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 2, 1, 1),
    _Dot1dTpFdbAddress_Type()
)
dot1dTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dTpFdbAddress.setStatus("current")
_Dot1dTpFdbPort_Type = Integer32
_Dot1dTpFdbPort_Object = MibTableColumn
dot1dTpFdbPort = _Dot1dTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 2, 1, 2),
    _Dot1dTpFdbPort_Type()
)
dot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbPort.setStatus("current")


class _Dot1dTpFdbStatus_Type(Integer32):
    """Custom type dot1dTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_Dot1dTpFdbStatus_Type.__name__ = "Integer32"
_Dot1dTpFdbStatus_Object = MibTableColumn
dot1dTpFdbStatus = _Dot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 2, 1, 3),
    _Dot1dTpFdbStatus_Type()
)
dot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbStatus.setStatus("current")
_Dot1dTpPortTable_Object = MibTable
dot1dTpPortTable = _Dot1dTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3)
)
if mibBuilder.loadTexts:
    dot1dTpPortTable.setStatus("current")
_Dot1dTpPortEntry_Object = MibTableRow
dot1dTpPortEntry = _Dot1dTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3, 1)
)
dot1dTpPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpPortEntry.setStatus("current")


class _Dot1dTpPort_Type(Integer32):
    """Custom type dot1dTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dTpPort_Type.__name__ = "Integer32"
_Dot1dTpPort_Object = MibTableColumn
dot1dTpPort = _Dot1dTpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3, 1, 1),
    _Dot1dTpPort_Type()
)
dot1dTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dTpPort.setStatus("current")
_Dot1dTpPortMaxInfo_Type = Integer32
_Dot1dTpPortMaxInfo_Object = MibTableColumn
dot1dTpPortMaxInfo = _Dot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3, 1, 2),
    _Dot1dTpPortMaxInfo_Type()
)
dot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortMaxInfo.setStatus("current")
_Dot1dTpPortInFrames_Type = Counter32
_Dot1dTpPortInFrames_Object = MibTableColumn
dot1dTpPortInFrames = _Dot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3, 1, 3),
    _Dot1dTpPortInFrames_Type()
)
dot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInFrames.setStatus("current")
_Dot1dTpPortOutFrames_Type = Counter32
_Dot1dTpPortOutFrames_Object = MibTableColumn
dot1dTpPortOutFrames = _Dot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3, 1, 4),
    _Dot1dTpPortOutFrames_Type()
)
dot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortOutFrames.setStatus("current")
_Dot1dTpPortInDiscards_Type = Counter32
_Dot1dTpPortInDiscards_Object = MibTableColumn
dot1dTpPortInDiscards = _Dot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 3, 1, 5),
    _Dot1dTpPortInDiscards_Type()
)
dot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInDiscards.setStatus("current")
_Dot1dTpHCPortTable_Object = MibTable
dot1dTpHCPortTable = _Dot1dTpHCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 5)
)
if mibBuilder.loadTexts:
    dot1dTpHCPortTable.setStatus("current")
_Dot1dTpHCPortEntry_Object = MibTableRow
dot1dTpHCPortEntry = _Dot1dTpHCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 5, 1)
)
dot1dTpHCPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpHCPortEntry.setStatus("current")
_Dot1dTpHCPortInFrames_Type = Counter64
_Dot1dTpHCPortInFrames_Object = MibTableColumn
dot1dTpHCPortInFrames = _Dot1dTpHCPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 5, 1, 1),
    _Dot1dTpHCPortInFrames_Type()
)
dot1dTpHCPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpHCPortInFrames.setStatus("current")
_Dot1dTpHCPortOutFrames_Type = Counter64
_Dot1dTpHCPortOutFrames_Object = MibTableColumn
dot1dTpHCPortOutFrames = _Dot1dTpHCPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 5, 1, 2),
    _Dot1dTpHCPortOutFrames_Type()
)
dot1dTpHCPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpHCPortOutFrames.setStatus("current")
_Dot1dTpHCPortInDiscards_Type = Counter64
_Dot1dTpHCPortInDiscards_Object = MibTableColumn
dot1dTpHCPortInDiscards = _Dot1dTpHCPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 5, 1, 3),
    _Dot1dTpHCPortInDiscards_Type()
)
dot1dTpHCPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpHCPortInDiscards.setStatus("current")
_Dot1dTpPortOverflowTable_Object = MibTable
dot1dTpPortOverflowTable = _Dot1dTpPortOverflowTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 6)
)
if mibBuilder.loadTexts:
    dot1dTpPortOverflowTable.setStatus("current")
_Dot1dTpPortOverflowEntry_Object = MibTableRow
dot1dTpPortOverflowEntry = _Dot1dTpPortOverflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 6, 1)
)
dot1dTpPortOverflowEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpPortOverflowEntry.setStatus("current")
_Dot1dTpPortInOverflowFrames_Type = Counter32
_Dot1dTpPortInOverflowFrames_Object = MibTableColumn
dot1dTpPortInOverflowFrames = _Dot1dTpPortInOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 6, 1, 1),
    _Dot1dTpPortInOverflowFrames_Type()
)
dot1dTpPortInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInOverflowFrames.setStatus("current")
_Dot1dTpPortOutOverflowFrames_Type = Counter32
_Dot1dTpPortOutOverflowFrames_Object = MibTableColumn
dot1dTpPortOutOverflowFrames = _Dot1dTpPortOutOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 6, 1, 2),
    _Dot1dTpPortOutOverflowFrames_Type()
)
dot1dTpPortOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortOutOverflowFrames.setStatus("current")
_Dot1dTpPortInOverflowDiscards_Type = Counter32
_Dot1dTpPortInOverflowDiscards_Object = MibTableColumn
dot1dTpPortInOverflowDiscards = _Dot1dTpPortInOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 4, 6, 1, 3),
    _Dot1dTpPortInOverflowDiscards_Type()
)
dot1dTpPortInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInOverflowDiscards.setStatus("current")
_Dot1dStatic_ObjectIdentity = ObjectIdentity
dot1dStatic = _Dot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5)
)
_Dot1dStaticTable_Object = MibTable
dot1dStaticTable = _Dot1dStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 1)
)
if mibBuilder.loadTexts:
    dot1dStaticTable.setStatus("current")
_Dot1dStaticEntry_Object = MibTableRow
dot1dStaticEntry = _Dot1dStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 1, 1)
)
dot1dStaticEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBaseContextId"),
    (0, "AT-GS950-16-MIB", "dot1dStaticAddress"),
    (0, "AT-GS950-16-MIB", "dot1dStaticReceivePort"),
)
if mibBuilder.loadTexts:
    dot1dStaticEntry.setStatus("current")
_Dot1dStaticAddress_Type = MacAddress
_Dot1dStaticAddress_Object = MibTableColumn
dot1dStaticAddress = _Dot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 1, 1, 1),
    _Dot1dStaticAddress_Type()
)
dot1dStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dStaticAddress.setStatus("current")


class _Dot1dStaticReceivePort_Type(Integer32):
    """Custom type dot1dStaticReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStaticReceivePort_Type.__name__ = "Integer32"
_Dot1dStaticReceivePort_Object = MibTableColumn
dot1dStaticReceivePort = _Dot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 1, 1, 2),
    _Dot1dStaticReceivePort_Type()
)
dot1dStaticReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dStaticReceivePort.setStatus("current")
_Dot1dStaticRowStatus_Type = RowStatus
_Dot1dStaticRowStatus_Object = MibTableColumn
dot1dStaticRowStatus = _Dot1dStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 1, 1, 3),
    _Dot1dStaticRowStatus_Type()
)
dot1dStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dStaticRowStatus.setStatus("current")


class _Dot1dStaticStatus_Type(Integer32):
    """Custom type dot1dStaticStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1dStaticStatus_Type.__name__ = "Integer32"
_Dot1dStaticStatus_Object = MibTableColumn
dot1dStaticStatus = _Dot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 1, 1, 4),
    _Dot1dStaticStatus_Type()
)
dot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStaticStatus.setStatus("current")
_Dot1dStaticAllowedToGoTable_Object = MibTable
dot1dStaticAllowedToGoTable = _Dot1dStaticAllowedToGoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 2)
)
if mibBuilder.loadTexts:
    dot1dStaticAllowedToGoTable.setStatus("current")
_Dot1dStaticAllowedToGoEntry_Object = MibTableRow
dot1dStaticAllowedToGoEntry = _Dot1dStaticAllowedToGoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 2, 1)
)
dot1dStaticAllowedToGoEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBaseContextId"),
    (0, "AT-GS950-16-MIB", "dot1dStaticAddress"),
    (0, "AT-GS950-16-MIB", "dot1dStaticReceivePort"),
    (0, "AT-GS950-16-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dStaticAllowedToGoEntry.setStatus("current")
_Dot1dStaticAllowedIsMember_Type = TruthValue
_Dot1dStaticAllowedIsMember_Object = MibTableColumn
dot1dStaticAllowedIsMember = _Dot1dStaticAllowedIsMember_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 5, 2, 1, 1),
    _Dot1dStaticAllowedIsMember_Type()
)
dot1dStaticAllowedIsMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStaticAllowedIsMember.setStatus("current")
_Dot1dPBridge_ObjectIdentity = ObjectIdentity
dot1dPBridge = _Dot1dPBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6)
)
_Dot1dMIBObjects_ObjectIdentity = ObjectIdentity
dot1dMIBObjects = _Dot1dMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1)
)
_Dot1dExtBase_ObjectIdentity = ObjectIdentity
dot1dExtBase = _Dot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1)
)
_Dot1dExtBaseTable_Object = MibTable
dot1dExtBaseTable = _Dot1dExtBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dExtBaseTable.setStatus("current")
_Dot1dExtBaseEntry_Object = MibTableRow
dot1dExtBaseEntry = _Dot1dExtBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 1, 1)
)
dot1dExtBaseEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBridgeContextId"),
)
if mibBuilder.loadTexts:
    dot1dExtBaseEntry.setStatus("current")


class _Dot1dBridgeContextId_Type(Integer32):
    """Custom type dot1dBridgeContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dBridgeContextId_Type.__name__ = "Integer32"
_Dot1dBridgeContextId_Object = MibTableColumn
dot1dBridgeContextId = _Dot1dBridgeContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 1, 1, 1),
    _Dot1dBridgeContextId_Type()
)
dot1dBridgeContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dBridgeContextId.setStatus("current")


class _Dot1dDeviceCapabilities_Type(Bits):
    """Custom type dot1dDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1dExtendedFilteringServices", 0),
          ("dot1dLocalVlanCapable", 7),
          ("dot1dTrafficClasses", 1),
          ("dot1qConfigurablePvidTagging", 6),
          ("dot1qHybridCapable", 5),
          ("dot1qIVLCapable", 3),
          ("dot1qSVLCapable", 4),
          ("dot1qStaticEntryIndividualPort", 2))
    )

_Dot1dDeviceCapabilities_Type.__name__ = "Bits"
_Dot1dDeviceCapabilities_Object = MibTableColumn
dot1dDeviceCapabilities = _Dot1dDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 1, 1, 2),
    _Dot1dDeviceCapabilities_Type()
)
dot1dDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dDeviceCapabilities.setStatus("current")


class _Dot1dTrafficClassesEnabled_Type(TruthValue):
    """Custom type dot1dTrafficClassesEnabled based on TruthValue"""


_Dot1dTrafficClassesEnabled_Object = MibTableColumn
dot1dTrafficClassesEnabled = _Dot1dTrafficClassesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 1, 1, 3),
    _Dot1dTrafficClassesEnabled_Type()
)
dot1dTrafficClassesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTrafficClassesEnabled.setStatus("current")


class _Dot1dGmrpStatus_Type(EnabledStatus):
    """Custom type dot1dGmrpStatus based on EnabledStatus"""


_Dot1dGmrpStatus_Object = MibTableColumn
dot1dGmrpStatus = _Dot1dGmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 1, 1, 4),
    _Dot1dGmrpStatus_Type()
)
dot1dGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dGmrpStatus.setStatus("current")
_Dot1dPortCapabilitiesTable_Object = MibTable
dot1dPortCapabilitiesTable = _Dot1dPortCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot1dPortCapabilitiesTable.setStatus("current")
_Dot1dPortCapabilitiesEntry_Object = MibTableRow
dot1dPortCapabilitiesEntry = _Dot1dPortCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dPortCapabilitiesEntry.setStatus("current")


class _Dot1dPortCapabilities_Type(Bits):
    """Custom type dot1dPortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1qConfigurableAcceptableFrameTypes", 1),
          ("dot1qDot1qTagging", 0),
          ("dot1qIngressFiltering", 2))
    )

_Dot1dPortCapabilities_Type.__name__ = "Bits"
_Dot1dPortCapabilities_Object = MibTableColumn
dot1dPortCapabilities = _Dot1dPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 1, 2, 1, 1),
    _Dot1dPortCapabilities_Type()
)
dot1dPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortCapabilities.setStatus("current")
_Dot1dPriority_ObjectIdentity = ObjectIdentity
dot1dPriority = _Dot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2)
)
_Dot1dPortPriorityTable_Object = MibTable
dot1dPortPriorityTable = _Dot1dPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dPortPriorityTable.setStatus("current")
_Dot1dPortPriorityEntry_Object = MibTableRow
dot1dPortPriorityEntry = _Dot1dPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dPortPriorityEntry.setStatus("current")


class _Dot1dPortDefaultUserPriority_Type(Integer32):
    """Custom type dot1dPortDefaultUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dPortDefaultUserPriority_Type.__name__ = "Integer32"
_Dot1dPortDefaultUserPriority_Object = MibTableColumn
dot1dPortDefaultUserPriority = _Dot1dPortDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 1, 1, 1),
    _Dot1dPortDefaultUserPriority_Type()
)
dot1dPortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortDefaultUserPriority.setStatus("current")


class _Dot1dPortNumTrafficClasses_Type(Integer32):
    """Custom type dot1dPortNumTrafficClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot1dPortNumTrafficClasses_Type.__name__ = "Integer32"
_Dot1dPortNumTrafficClasses_Object = MibTableColumn
dot1dPortNumTrafficClasses = _Dot1dPortNumTrafficClasses_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 1, 1, 2),
    _Dot1dPortNumTrafficClasses_Type()
)
dot1dPortNumTrafficClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortNumTrafficClasses.setStatus("current")
_Dot1dUserPriorityRegenTable_Object = MibTable
dot1dUserPriorityRegenTable = _Dot1dUserPriorityRegenTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1dUserPriorityRegenTable.setStatus("current")
_Dot1dUserPriorityRegenEntry_Object = MibTableRow
dot1dUserPriorityRegenEntry = _Dot1dUserPriorityRegenEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 2, 1)
)
dot1dUserPriorityRegenEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBasePort"),
    (0, "AT-GS950-16-MIB", "dot1dUserPriority"),
)
if mibBuilder.loadTexts:
    dot1dUserPriorityRegenEntry.setStatus("current")


class _Dot1dUserPriority_Type(Integer32):
    """Custom type dot1dUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dUserPriority_Type.__name__ = "Integer32"
_Dot1dUserPriority_Object = MibTableColumn
dot1dUserPriority = _Dot1dUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 2, 1, 1),
    _Dot1dUserPriority_Type()
)
dot1dUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dUserPriority.setStatus("current")


class _Dot1dRegenUserPriority_Type(Integer32):
    """Custom type dot1dRegenUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dRegenUserPriority_Type.__name__ = "Integer32"
_Dot1dRegenUserPriority_Object = MibTableColumn
dot1dRegenUserPriority = _Dot1dRegenUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 2, 1, 2),
    _Dot1dRegenUserPriority_Type()
)
dot1dRegenUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dRegenUserPriority.setStatus("current")
_Dot1dTrafficClassTable_Object = MibTable
dot1dTrafficClassTable = _Dot1dTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot1dTrafficClassTable.setStatus("current")
_Dot1dTrafficClassEntry_Object = MibTableRow
dot1dTrafficClassEntry = _Dot1dTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 3, 1)
)
dot1dTrafficClassEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBasePort"),
    (0, "AT-GS950-16-MIB", "dot1dTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    dot1dTrafficClassEntry.setStatus("current")


class _Dot1dTrafficClassPriority_Type(Integer32):
    """Custom type dot1dTrafficClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dTrafficClassPriority_Type.__name__ = "Integer32"
_Dot1dTrafficClassPriority_Object = MibTableColumn
dot1dTrafficClassPriority = _Dot1dTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 3, 1, 1),
    _Dot1dTrafficClassPriority_Type()
)
dot1dTrafficClassPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dTrafficClassPriority.setStatus("current")


class _Dot1dTrafficClass_Type(Integer32):
    """Custom type dot1dTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dTrafficClass_Type.__name__ = "Integer32"
_Dot1dTrafficClass_Object = MibTableColumn
dot1dTrafficClass = _Dot1dTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 3, 1, 2),
    _Dot1dTrafficClass_Type()
)
dot1dTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTrafficClass.setStatus("current")
_Dot1dPortOutboundAccessPriorityTable_Object = MibTable
dot1dPortOutboundAccessPriorityTable = _Dot1dPortOutboundAccessPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dot1dPortOutboundAccessPriorityTable.setStatus("current")
_Dot1dPortOutboundAccessPriorityEntry_Object = MibTableRow
dot1dPortOutboundAccessPriorityEntry = _Dot1dPortOutboundAccessPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 4, 1)
)
dot1dPortOutboundAccessPriorityEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBasePort"),
    (0, "AT-GS950-16-MIB", "dot1dRegenUserPriority"),
)
if mibBuilder.loadTexts:
    dot1dPortOutboundAccessPriorityEntry.setStatus("current")


class _Dot1dPortOutboundAccessPriority_Type(Integer32):
    """Custom type dot1dPortOutboundAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dPortOutboundAccessPriority_Type.__name__ = "Integer32"
_Dot1dPortOutboundAccessPriority_Object = MibTableColumn
dot1dPortOutboundAccessPriority = _Dot1dPortOutboundAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 2, 4, 1, 1),
    _Dot1dPortOutboundAccessPriority_Type()
)
dot1dPortOutboundAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortOutboundAccessPriority.setStatus("current")
_Dot1dGarp_ObjectIdentity = ObjectIdentity
dot1dGarp = _Dot1dGarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 3)
)
_Dot1dPortGarpTable_Object = MibTable
dot1dPortGarpTable = _Dot1dPortGarpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGarpTable.setStatus("current")
_Dot1dPortGarpEntry_Object = MibTableRow
dot1dPortGarpEntry = _Dot1dPortGarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGarpEntry.setStatus("current")


class _Dot1dPortGarpJoinTime_Type(TimeInterval):
    """Custom type dot1dPortGarpJoinTime based on TimeInterval"""
    defaultValue = 20


_Dot1dPortGarpJoinTime_Object = MibTableColumn
dot1dPortGarpJoinTime = _Dot1dPortGarpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 3, 1, 1, 1),
    _Dot1dPortGarpJoinTime_Type()
)
dot1dPortGarpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpJoinTime.setStatus("current")


class _Dot1dPortGarpLeaveTime_Type(TimeInterval):
    """Custom type dot1dPortGarpLeaveTime based on TimeInterval"""
    defaultValue = 60


_Dot1dPortGarpLeaveTime_Object = MibTableColumn
dot1dPortGarpLeaveTime = _Dot1dPortGarpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 3, 1, 1, 2),
    _Dot1dPortGarpLeaveTime_Type()
)
dot1dPortGarpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpLeaveTime.setStatus("current")


class _Dot1dPortGarpLeaveAllTime_Type(TimeInterval):
    """Custom type dot1dPortGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_Dot1dPortGarpLeaveAllTime_Object = MibTableColumn
dot1dPortGarpLeaveAllTime = _Dot1dPortGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 1, 3, 1, 1, 3),
    _Dot1dPortGarpLeaveAllTime_Type()
)
dot1dPortGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpLeaveAllTime.setStatus("current")
_Dot1dConformance_ObjectIdentity = ObjectIdentity
dot1dConformance = _Dot1dConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2)
)
_Dot1dGroups_ObjectIdentity = ObjectIdentity
dot1dGroups = _Dot1dGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1)
)
_Dot1dCompliances_ObjectIdentity = ObjectIdentity
dot1dCompliances = _Dot1dCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 2)
)
_Dot1qQBridge_ObjectIdentity = ObjectIdentity
dot1qQBridge = _Dot1qQBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7)
)
_Dot1qMIBObjects_ObjectIdentity = ObjectIdentity
dot1qMIBObjects = _Dot1qMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1)
)
_Dot1qBase_ObjectIdentity = ObjectIdentity
dot1qBase = _Dot1qBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1)
)
_Dot1qBaseTable_Object = MibTable
dot1qBaseTable = _Dot1qBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1qBaseTable.setStatus("current")
_Dot1qBaseEntry_Object = MibTableRow
dot1qBaseEntry = _Dot1qBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1)
)
dot1qBaseEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
)
if mibBuilder.loadTexts:
    dot1qBaseEntry.setStatus("current")


class _Dot1qVlanContextId_Type(Integer32):
    """Custom type dot1qVlanContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qVlanContextId_Type.__name__ = "Integer32"
_Dot1qVlanContextId_Object = MibTableColumn
dot1qVlanContextId = _Dot1qVlanContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1, 1),
    _Dot1qVlanContextId_Type()
)
dot1qVlanContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanContextId.setStatus("current")


class _Dot1qVlanVersionNumber_Type(Integer32):
    """Custom type dot1qVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_Dot1qVlanVersionNumber_Type.__name__ = "Integer32"
_Dot1qVlanVersionNumber_Object = MibTableColumn
dot1qVlanVersionNumber = _Dot1qVlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1, 2),
    _Dot1qVlanVersionNumber_Type()
)
dot1qVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanVersionNumber.setStatus("current")
_Dot1qMaxVlanId_Type = VlanId
_Dot1qMaxVlanId_Object = MibTableColumn
dot1qMaxVlanId = _Dot1qMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1, 3),
    _Dot1qMaxVlanId_Type()
)
dot1qMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qMaxVlanId.setStatus("current")
_Dot1qMaxSupportedVlans_Type = Unsigned32
_Dot1qMaxSupportedVlans_Object = MibTableColumn
dot1qMaxSupportedVlans = _Dot1qMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1, 4),
    _Dot1qMaxSupportedVlans_Type()
)
dot1qMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qMaxSupportedVlans.setStatus("current")
_Dot1qNumVlans_Type = Unsigned32
_Dot1qNumVlans_Object = MibTableColumn
dot1qNumVlans = _Dot1qNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1, 5),
    _Dot1qNumVlans_Type()
)
dot1qNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qNumVlans.setStatus("current")


class _Dot1qGvrpStatus_Type(Integer32):
    """Custom type dot1qGvrpStatus based on Integer32"""
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


_Dot1qGvrpStatus_Type.__name__ = "Integer32"
_Dot1qGvrpStatus_Object = MibTableColumn
dot1qGvrpStatus = _Dot1qGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 1, 1, 1, 6),
    _Dot1qGvrpStatus_Type()
)
dot1qGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qGvrpStatus.setStatus("current")
_Dot1qTp_ObjectIdentity = ObjectIdentity
dot1qTp = _Dot1qTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2)
)
_Dot1qFdbTable_Object = MibTable
dot1qFdbTable = _Dot1qFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1qFdbTable.setStatus("current")
_Dot1qFdbEntry_Object = MibTableRow
dot1qFdbEntry = _Dot1qFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 1, 1)
)
dot1qFdbEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    dot1qFdbEntry.setStatus("current")
_Dot1qFdbId_Type = Unsigned32
_Dot1qFdbId_Object = MibTableColumn
dot1qFdbId = _Dot1qFdbId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 1, 1, 1),
    _Dot1qFdbId_Type()
)
dot1qFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qFdbId.setStatus("current")
_Dot1qFdbDynamicCount_Type = Counter32
_Dot1qFdbDynamicCount_Object = MibTableColumn
dot1qFdbDynamicCount = _Dot1qFdbDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 1, 1, 2),
    _Dot1qFdbDynamicCount_Type()
)
dot1qFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qFdbDynamicCount.setStatus("current")
_Dot1qTpFdbTable_Object = MibTable
dot1qTpFdbTable = _Dot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1qTpFdbTable.setStatus("current")
_Dot1qTpFdbEntry_Object = MibTableRow
dot1qTpFdbEntry = _Dot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 2, 1)
)
dot1qTpFdbEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qFdbId"),
    (0, "AT-GS950-16-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    dot1qTpFdbEntry.setStatus("current")
_Dot1qTpFdbAddress_Type = MacAddress
_Dot1qTpFdbAddress_Object = MibTableColumn
dot1qTpFdbAddress = _Dot1qTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 2, 1, 1),
    _Dot1qTpFdbAddress_Type()
)
dot1qTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbAddress.setStatus("current")


class _Dot1qTpFdbPort_Type(Integer32):
    """Custom type dot1qTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qTpFdbPort_Type.__name__ = "Integer32"
_Dot1qTpFdbPort_Object = MibTableColumn
dot1qTpFdbPort = _Dot1qTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 2, 1, 2),
    _Dot1qTpFdbPort_Type()
)
dot1qTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbPort.setStatus("current")


class _Dot1qTpFdbStatus_Type(Integer32):
    """Custom type dot1qTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_Dot1qTpFdbStatus_Type.__name__ = "Integer32"
_Dot1qTpFdbStatus_Object = MibTableColumn
dot1qTpFdbStatus = _Dot1qTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 2, 1, 3),
    _Dot1qTpFdbStatus_Type()
)
dot1qTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbStatus.setStatus("current")
_Dot1qTpFdbPw_Type = Unsigned32
_Dot1qTpFdbPw_Object = MibTableColumn
dot1qTpFdbPw = _Dot1qTpFdbPw_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 2, 2, 1, 4),
    _Dot1qTpFdbPw_Type()
)
dot1qTpFdbPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbPw.setStatus("current")
_Dot1qStatic_ObjectIdentity = ObjectIdentity
dot1qStatic = _Dot1qStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3)
)
_Dot1qStaticUnicastTable_Object = MibTable
dot1qStaticUnicastTable = _Dot1qStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1qStaticUnicastTable.setStatus("current")
_Dot1qStaticUnicastEntry_Object = MibTableRow
dot1qStaticUnicastEntry = _Dot1qStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 1, 1)
)
dot1qStaticUnicastEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qFdbId"),
    (0, "AT-GS950-16-MIB", "dot1qStaticUnicastAddress"),
    (0, "AT-GS950-16-MIB", "dot1qStaticUnicastReceivePort"),
)
if mibBuilder.loadTexts:
    dot1qStaticUnicastEntry.setStatus("current")
_Dot1qStaticUnicastAddress_Type = MacAddress
_Dot1qStaticUnicastAddress_Object = MibTableColumn
dot1qStaticUnicastAddress = _Dot1qStaticUnicastAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 1, 1, 1),
    _Dot1qStaticUnicastAddress_Type()
)
dot1qStaticUnicastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qStaticUnicastAddress.setStatus("current")


class _Dot1qStaticUnicastReceivePort_Type(Integer32):
    """Custom type dot1qStaticUnicastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qStaticUnicastReceivePort_Type.__name__ = "Integer32"
_Dot1qStaticUnicastReceivePort_Object = MibTableColumn
dot1qStaticUnicastReceivePort = _Dot1qStaticUnicastReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 1, 1, 2),
    _Dot1qStaticUnicastReceivePort_Type()
)
dot1qStaticUnicastReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qStaticUnicastReceivePort.setStatus("current")
_Dot1qStaticUnicastRowStatus_Type = RowStatus
_Dot1qStaticUnicastRowStatus_Object = MibTableColumn
dot1qStaticUnicastRowStatus = _Dot1qStaticUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 1, 1, 3),
    _Dot1qStaticUnicastRowStatus_Type()
)
dot1qStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qStaticUnicastRowStatus.setStatus("current")


class _Dot1qStaticUnicastStatus_Type(Integer32):
    """Custom type dot1qStaticUnicastStatus based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1qStaticUnicastStatus_Type.__name__ = "Integer32"
_Dot1qStaticUnicastStatus_Object = MibTableColumn
dot1qStaticUnicastStatus = _Dot1qStaticUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 1, 1, 4),
    _Dot1qStaticUnicastStatus_Type()
)
dot1qStaticUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticUnicastStatus.setStatus("current")
_Dot1qStaticAllowedToGoTable_Object = MibTable
dot1qStaticAllowedToGoTable = _Dot1qStaticAllowedToGoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot1qStaticAllowedToGoTable.setStatus("current")
_Dot1qStaticAllowedToGoEntry_Object = MibTableRow
dot1qStaticAllowedToGoEntry = _Dot1qStaticAllowedToGoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 2, 1)
)
dot1qStaticAllowedToGoEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qFdbId"),
    (0, "AT-GS950-16-MIB", "dot1qStaticUnicastAddress"),
    (0, "AT-GS950-16-MIB", "dot1qStaticUnicastReceivePort"),
    (0, "AT-GS950-16-MIB", "dot1qTpPort"),
)
if mibBuilder.loadTexts:
    dot1qStaticAllowedToGoEntry.setStatus("current")
_Dot1qStaticAllowedIsMember_Type = TruthValue
_Dot1qStaticAllowedIsMember_Object = MibTableColumn
dot1qStaticAllowedIsMember = _Dot1qStaticAllowedIsMember_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 2, 1, 1),
    _Dot1qStaticAllowedIsMember_Type()
)
dot1qStaticAllowedIsMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticAllowedIsMember.setStatus("current")


class _Dot1qTpPort_Type(Integer32):
    """Custom type dot1qTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1qTpPort_Type.__name__ = "Integer32"
_Dot1qTpPort_Object = MibTableColumn
dot1qTpPort = _Dot1qTpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 2, 1, 2),
    _Dot1qTpPort_Type()
)
dot1qTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qTpPort.setStatus("current")
_Dot1qStaticMulticastTable_Object = MibTable
dot1qStaticMulticastTable = _Dot1qStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dot1qStaticMulticastTable.setStatus("current")
_Dot1qStaticMulticastEntry_Object = MibTableRow
dot1qStaticMulticastEntry = _Dot1qStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 3, 1)
)
dot1qStaticMulticastEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qVlanIndex"),
    (0, "AT-GS950-16-MIB", "dot1qStaticMulticastAddress"),
    (0, "AT-GS950-16-MIB", "dot1qStaticMulticastReceivePort"),
)
if mibBuilder.loadTexts:
    dot1qStaticMulticastEntry.setStatus("current")
_Dot1qStaticMulticastAddress_Type = MacAddress
_Dot1qStaticMulticastAddress_Object = MibTableColumn
dot1qStaticMulticastAddress = _Dot1qStaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 3, 1, 1),
    _Dot1qStaticMulticastAddress_Type()
)
dot1qStaticMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qStaticMulticastAddress.setStatus("current")


class _Dot1qStaticMulticastReceivePort_Type(Integer32):
    """Custom type dot1qStaticMulticastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qStaticMulticastReceivePort_Type.__name__ = "Integer32"
_Dot1qStaticMulticastReceivePort_Object = MibTableColumn
dot1qStaticMulticastReceivePort = _Dot1qStaticMulticastReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 3, 1, 2),
    _Dot1qStaticMulticastReceivePort_Type()
)
dot1qStaticMulticastReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qStaticMulticastReceivePort.setStatus("current")
_Dot1qStaticMulticastRowStatus_Type = RowStatus
_Dot1qStaticMulticastRowStatus_Object = MibTableColumn
dot1qStaticMulticastRowStatus = _Dot1qStaticMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 3, 1, 3),
    _Dot1qStaticMulticastRowStatus_Type()
)
dot1qStaticMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qStaticMulticastRowStatus.setStatus("current")


class _Dot1qStaticMulticastStatus_Type(Integer32):
    """Custom type dot1qStaticMulticastStatus based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1qStaticMulticastStatus_Type.__name__ = "Integer32"
_Dot1qStaticMulticastStatus_Object = MibTableColumn
dot1qStaticMulticastStatus = _Dot1qStaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 3, 1, 4),
    _Dot1qStaticMulticastStatus_Type()
)
dot1qStaticMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastStatus.setStatus("current")
_Dot1qStaticMcastPortTable_Object = MibTable
dot1qStaticMcastPortTable = _Dot1qStaticMcastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dot1qStaticMcastPortTable.setStatus("current")
_Dot1qStaticMcastPortEntry_Object = MibTableRow
dot1qStaticMcastPortEntry = _Dot1qStaticMcastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 4, 1)
)
dot1qStaticMcastPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qVlanIndex"),
    (0, "AT-GS950-16-MIB", "dot1qStaticMulticastAddress"),
    (0, "AT-GS950-16-MIB", "dot1qStaticMulticastReceivePort"),
    (0, "AT-GS950-16-MIB", "dot1qTpPort"),
)
if mibBuilder.loadTexts:
    dot1qStaticMcastPortEntry.setStatus("current")


class _Dot1qStaticMcastPort_Type(Integer32):
    """Custom type dot1qStaticMcastPort based on Integer32"""
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
        *(("addForbidden", 2),
          ("addMember", 1),
          ("delForbidden", 4),
          ("delMember", 3))
    )


_Dot1qStaticMcastPort_Type.__name__ = "Integer32"
_Dot1qStaticMcastPort_Object = MibTableColumn
dot1qStaticMcastPort = _Dot1qStaticMcastPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 4, 1, 1),
    _Dot1qStaticMcastPort_Type()
)
dot1qStaticMcastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMcastPort.setStatus("current")
_Dot1qVlanIndex_Type = VlanIndex
_Dot1qVlanIndex_Object = MibTableColumn
dot1qVlanIndex = _Dot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 3, 4, 1, 2),
    _Dot1qVlanIndex_Type()
)
dot1qVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanIndex.setStatus("current")
_Dot1qVlan_ObjectIdentity = ObjectIdentity
dot1qVlan = _Dot1qVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4)
)
_Dot1qVlanNumDeletesTable_Object = MibTable
dot1qVlanNumDeletesTable = _Dot1qVlanNumDeletesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot1qVlanNumDeletesTable.setStatus("current")
_Dot1qVlanNumDeletesEntry_Object = MibTableRow
dot1qVlanNumDeletesEntry = _Dot1qVlanNumDeletesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 1, 1)
)
dot1qVlanNumDeletesEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
)
if mibBuilder.loadTexts:
    dot1qVlanNumDeletesEntry.setStatus("current")
_Dot1qVlanNumDeletes_Type = Counter32
_Dot1qVlanNumDeletes_Object = MibTableColumn
dot1qVlanNumDeletes = _Dot1qVlanNumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 1, 1, 1),
    _Dot1qVlanNumDeletes_Type()
)
dot1qVlanNumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanNumDeletes.setStatus("current")
_Dot1qVlanCurrentTable_Object = MibTable
dot1qVlanCurrentTable = _Dot1qVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot1qVlanCurrentTable.setStatus("current")
_Dot1qVlanCurrentEntry_Object = MibTableRow
dot1qVlanCurrentEntry = _Dot1qVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 2, 1)
)
dot1qVlanCurrentEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qVlanTimeMark"),
    (0, "AT-GS950-16-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanCurrentEntry.setStatus("current")
_Dot1qVlanTimeMark_Type = TimeFilter
_Dot1qVlanTimeMark_Object = MibTableColumn
dot1qVlanTimeMark = _Dot1qVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 2, 1, 1),
    _Dot1qVlanTimeMark_Type()
)
dot1qVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanTimeMark.setStatus("current")
_Dot1qVlanFdbId_Type = Unsigned32
_Dot1qVlanFdbId_Object = MibTableColumn
dot1qVlanFdbId = _Dot1qVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 2, 1, 2),
    _Dot1qVlanFdbId_Type()
)
dot1qVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanFdbId.setStatus("current")


class _Dot1qVlanStatus_Type(Integer32):
    """Custom type dot1qVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_Dot1qVlanStatus_Type.__name__ = "Integer32"
_Dot1qVlanStatus_Object = MibTableColumn
dot1qVlanStatus = _Dot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 2, 1, 3),
    _Dot1qVlanStatus_Type()
)
dot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanStatus.setStatus("current")
_Dot1qVlanCreationTime_Type = TimeTicks
_Dot1qVlanCreationTime_Object = MibTableColumn
dot1qVlanCreationTime = _Dot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 2, 1, 4),
    _Dot1qVlanCreationTime_Type()
)
dot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCreationTime.setStatus("current")
_Dot1qVlanEgressPortTable_Object = MibTable
dot1qVlanEgressPortTable = _Dot1qVlanEgressPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dot1qVlanEgressPortTable.setStatus("current")
_Dot1qVlanEgressPortEntry_Object = MibTableRow
dot1qVlanEgressPortEntry = _Dot1qVlanEgressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 3, 1)
)
dot1qVlanEgressPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qVlanTimeMark"),
    (0, "AT-GS950-16-MIB", "dot1qVlanIndex"),
    (0, "AT-GS950-16-MIB", "dot1qTpPort"),
)
if mibBuilder.loadTexts:
    dot1qVlanEgressPortEntry.setStatus("current")


class _Dot1qVlanCurrentEgressPort_Type(Integer32):
    """Custom type dot1qVlanCurrentEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Dot1qVlanCurrentEgressPort_Type.__name__ = "Integer32"
_Dot1qVlanCurrentEgressPort_Object = MibTableColumn
dot1qVlanCurrentEgressPort = _Dot1qVlanCurrentEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 3, 1, 1),
    _Dot1qVlanCurrentEgressPort_Type()
)
dot1qVlanCurrentEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCurrentEgressPort.setStatus("current")
_Dot1qVlanStaticTable_Object = MibTable
dot1qVlanStaticTable = _Dot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dot1qVlanStaticTable.setStatus("current")
_Dot1qVlanStaticEntry_Object = MibTableRow
dot1qVlanStaticEntry = _Dot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 4, 1)
)
dot1qVlanStaticEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanStaticEntry.setStatus("current")


class _Dot1qVlanStaticName_Type(SnmpAdminString):
    """Custom type dot1qVlanStaticName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot1qVlanStaticName_Type.__name__ = "SnmpAdminString"
_Dot1qVlanStaticName_Object = MibTableColumn
dot1qVlanStaticName = _Dot1qVlanStaticName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 4, 1, 1),
    _Dot1qVlanStaticName_Type()
)
dot1qVlanStaticName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStaticName.setStatus("current")
_Dot1qVlanStaticRowStatus_Type = RowStatus
_Dot1qVlanStaticRowStatus_Object = MibTableColumn
dot1qVlanStaticRowStatus = _Dot1qVlanStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 4, 1, 2),
    _Dot1qVlanStaticRowStatus_Type()
)
dot1qVlanStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStaticRowStatus.setStatus("current")
_Dot1qVlanStaticPortConfigTable_Object = MibTable
dot1qVlanStaticPortConfigTable = _Dot1qVlanStaticPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 5)
)
if mibBuilder.loadTexts:
    dot1qVlanStaticPortConfigTable.setStatus("current")
_Dot1qVlanStaticPortConfigEntry_Object = MibTableRow
dot1qVlanStaticPortConfigEntry = _Dot1qVlanStaticPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 5, 1)
)
dot1qVlanStaticPortConfigEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanContextId"),
    (0, "AT-GS950-16-MIB", "dot1qVlanIndex"),
    (0, "AT-GS950-16-MIB", "dot1qTpPort"),
)
if mibBuilder.loadTexts:
    dot1qVlanStaticPortConfigEntry.setStatus("current")


class _Dot1qVlanStaticPort_Type(Integer32):
    """Custom type dot1qVlanStaticPort based on Integer32"""
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
        *(("addForbidden", 3),
          ("addTagged", 1),
          ("addUntagged", 2),
          ("delForbidden", 6),
          ("delTagged", 4),
          ("delUntagged", 5))
    )


_Dot1qVlanStaticPort_Type.__name__ = "Integer32"
_Dot1qVlanStaticPort_Object = MibTableColumn
dot1qVlanStaticPort = _Dot1qVlanStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 5, 1, 1),
    _Dot1qVlanStaticPort_Type()
)
dot1qVlanStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanStaticPort.setStatus("current")
_Dot1qPortVlanTable_Object = MibTable
dot1qPortVlanTable = _Dot1qPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7)
)
if mibBuilder.loadTexts:
    dot1qPortVlanTable.setStatus("current")
_Dot1qPortVlanEntry_Object = MibTableRow
dot1qPortVlanEntry = _Dot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1)
)
dot1qPortVlanEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1qPortVlanEntry.setStatus("current")


class _Dot1qPvid_Type(VlanIndex):
    """Custom type dot1qPvid based on VlanIndex"""
    defaultValue = 1


_Dot1qPvid_Object = MibTableColumn
dot1qPvid = _Dot1qPvid_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 1),
    _Dot1qPvid_Type()
)
dot1qPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPvid.setStatus("current")


class _Dot1qPortAcceptableFrameTypes_Type(Integer32):
    """Custom type dot1qPortAcceptableFrameTypes based on Integer32"""
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
        *(("admitAll", 1),
          ("admitOnlyUntaggedAndPriorityTagged", 3),
          ("admitOnlyVlanTagged", 2))
    )


_Dot1qPortAcceptableFrameTypes_Type.__name__ = "Integer32"
_Dot1qPortAcceptableFrameTypes_Object = MibTableColumn
dot1qPortAcceptableFrameTypes = _Dot1qPortAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 2),
    _Dot1qPortAcceptableFrameTypes_Type()
)
dot1qPortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortAcceptableFrameTypes.setStatus("current")


class _Dot1qPortIngressFiltering_Type(TruthValue):
    """Custom type dot1qPortIngressFiltering based on TruthValue"""


_Dot1qPortIngressFiltering_Object = MibTableColumn
dot1qPortIngressFiltering = _Dot1qPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 3),
    _Dot1qPortIngressFiltering_Type()
)
dot1qPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortIngressFiltering.setStatus("current")


class _Dot1qPortGvrpStatus_Type(EnabledStatus):
    """Custom type dot1qPortGvrpStatus based on EnabledStatus"""


_Dot1qPortGvrpStatus_Object = MibTableColumn
dot1qPortGvrpStatus = _Dot1qPortGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 4),
    _Dot1qPortGvrpStatus_Type()
)
dot1qPortGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortGvrpStatus.setStatus("current")
_Dot1qPortGvrpFailedRegistrations_Type = Counter32
_Dot1qPortGvrpFailedRegistrations_Object = MibTableColumn
dot1qPortGvrpFailedRegistrations = _Dot1qPortGvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 5),
    _Dot1qPortGvrpFailedRegistrations_Type()
)
dot1qPortGvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qPortGvrpFailedRegistrations.setStatus("current")
_Dot1qPortGvrpLastPduOrigin_Type = MacAddress
_Dot1qPortGvrpLastPduOrigin_Object = MibTableColumn
dot1qPortGvrpLastPduOrigin = _Dot1qPortGvrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 6),
    _Dot1qPortGvrpLastPduOrigin_Type()
)
dot1qPortGvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qPortGvrpLastPduOrigin.setStatus("current")


class _Dot1qPortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type dot1qPortRestrictedVlanRegistration based on TruthValue"""


_Dot1qPortRestrictedVlanRegistration_Object = MibTableColumn
dot1qPortRestrictedVlanRegistration = _Dot1qPortRestrictedVlanRegistration_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 7, 1, 4, 7, 1, 7),
    _Dot1qPortRestrictedVlanRegistration_Type()
)
dot1qPortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortRestrictedVlanRegistration.setStatus("current")
_L2Mst_ObjectIdentity = ObjectIdentity
l2Mst = _L2Mst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118)
)
_Dot1sMst_ObjectIdentity = ObjectIdentity
dot1sMst = _Dot1sMst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1)
)
_Dot1sMstTable_Object = MibTable
dot1sMstTable = _Dot1sMstTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3)
)
if mibBuilder.loadTexts:
    dot1sMstTable.setStatus("current")
_Dot1sMstEntry_Object = MibTableRow
dot1sMstEntry = _Dot1sMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1)
)
dot1sMstEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sMstContextId"),
)
if mibBuilder.loadTexts:
    dot1sMstEntry.setStatus("current")


class _Dot1sMstContextId_Type(Integer32):
    """Custom type dot1sMstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1sMstContextId_Type.__name__ = "Integer32"
_Dot1sMstContextId_Object = MibTableColumn
dot1sMstContextId = _Dot1sMstContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 1),
    _Dot1sMstContextId_Type()
)
dot1sMstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1sMstContextId.setStatus("current")


class _Dot1sSystemControl_Type(Integer32):
    """Custom type dot1sSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("start", 1))
    )


_Dot1sSystemControl_Type.__name__ = "Integer32"
_Dot1sSystemControl_Object = MibTableColumn
dot1sSystemControl = _Dot1sSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 2),
    _Dot1sSystemControl_Type()
)
dot1sSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sSystemControl.setStatus("current")
_Dot1sModuleStatus_Type = EnabledStatus
_Dot1sModuleStatus_Object = MibTableColumn
dot1sModuleStatus = _Dot1sModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 3),
    _Dot1sModuleStatus_Type()
)
dot1sModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sModuleStatus.setStatus("current")


class _Dot1sMaxMstInstanceNumber_Type(Integer32):
    """Custom type dot1sMaxMstInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Dot1sMaxMstInstanceNumber_Type.__name__ = "Integer32"
_Dot1sMaxMstInstanceNumber_Object = MibTableColumn
dot1sMaxMstInstanceNumber = _Dot1sMaxMstInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 4),
    _Dot1sMaxMstInstanceNumber_Type()
)
dot1sMaxMstInstanceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMaxMstInstanceNumber.setStatus("current")
_Dot1sNoOfMstiSupported_Type = Integer32
_Dot1sNoOfMstiSupported_Object = MibTableColumn
dot1sNoOfMstiSupported = _Dot1sNoOfMstiSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 5),
    _Dot1sNoOfMstiSupported_Type()
)
dot1sNoOfMstiSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sNoOfMstiSupported.setStatus("current")


class _Dot1sMaxHopCount_Type(Integer32):
    """Custom type dot1sMaxHopCount based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Dot1sMaxHopCount_Type.__name__ = "Integer32"
_Dot1sMaxHopCount_Object = MibTableColumn
dot1sMaxHopCount = _Dot1sMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 6),
    _Dot1sMaxHopCount_Type()
)
dot1sMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMaxHopCount.setStatus("current")
_Dot1sBrgAddress_Type = MacAddress
_Dot1sBrgAddress_Object = MibTableColumn
dot1sBrgAddress = _Dot1sBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 7),
    _Dot1sBrgAddress_Type()
)
dot1sBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sBrgAddress.setStatus("current")
_Dot1sCistRoot_Type = BridgeId
_Dot1sCistRoot_Object = MibTableColumn
dot1sCistRoot = _Dot1sCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 8),
    _Dot1sCistRoot_Type()
)
dot1sCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistRoot.setStatus("current")
_Dot1sCistRegionalRoot_Type = BridgeId
_Dot1sCistRegionalRoot_Object = MibTableColumn
dot1sCistRegionalRoot = _Dot1sCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 9),
    _Dot1sCistRegionalRoot_Type()
)
dot1sCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistRegionalRoot.setStatus("current")
_Dot1sCistRootCost_Type = Integer32
_Dot1sCistRootCost_Object = MibTableColumn
dot1sCistRootCost = _Dot1sCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 10),
    _Dot1sCistRootCost_Type()
)
dot1sCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistRootCost.setStatus("current")
_Dot1sCistRegionalRootCost_Type = Integer32
_Dot1sCistRegionalRootCost_Object = MibTableColumn
dot1sCistRegionalRootCost = _Dot1sCistRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 11),
    _Dot1sCistRegionalRootCost_Type()
)
dot1sCistRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistRegionalRootCost.setStatus("current")
_Dot1sCistRootPort_Type = Integer32
_Dot1sCistRootPort_Object = MibTableColumn
dot1sCistRootPort = _Dot1sCistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 12),
    _Dot1sCistRootPort_Type()
)
dot1sCistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistRootPort.setStatus("current")


class _Dot1sCistBridgePriority_Type(Integer32):
    """Custom type dot1sCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Dot1sCistBridgePriority_Type.__name__ = "Integer32"
_Dot1sCistBridgePriority_Object = MibTableColumn
dot1sCistBridgePriority = _Dot1sCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 13),
    _Dot1sCistBridgePriority_Type()
)
dot1sCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistBridgePriority.setStatus("current")


class _Dot1sCistBridgeMaxAge_Type(Timeout):
    """Custom type dot1sCistBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Dot1sCistBridgeMaxAge_Type.__name__ = "Timeout"
_Dot1sCistBridgeMaxAge_Object = MibTableColumn
dot1sCistBridgeMaxAge = _Dot1sCistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 14),
    _Dot1sCistBridgeMaxAge_Type()
)
dot1sCistBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistBridgeMaxAge.setStatus("current")


class _Dot1sCistBridgeForwardDelay_Type(Timeout):
    """Custom type dot1sCistBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Dot1sCistBridgeForwardDelay_Type.__name__ = "Timeout"
_Dot1sCistBridgeForwardDelay_Object = MibTableColumn
dot1sCistBridgeForwardDelay = _Dot1sCistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 15),
    _Dot1sCistBridgeForwardDelay_Type()
)
dot1sCistBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistBridgeForwardDelay.setStatus("current")
_Dot1sCistHoldTime_Type = Integer32
_Dot1sCistHoldTime_Object = MibTableColumn
dot1sCistHoldTime = _Dot1sCistHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 16),
    _Dot1sCistHoldTime_Type()
)
dot1sCistHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistHoldTime.setStatus("current")
_Dot1sCistMaxAge_Type = Timeout
_Dot1sCistMaxAge_Object = MibTableColumn
dot1sCistMaxAge = _Dot1sCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 17),
    _Dot1sCistMaxAge_Type()
)
dot1sCistMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistMaxAge.setStatus("current")
_Dot1sCistForwardDelay_Type = Timeout
_Dot1sCistForwardDelay_Object = MibTableColumn
dot1sCistForwardDelay = _Dot1sCistForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 18),
    _Dot1sCistForwardDelay_Type()
)
dot1sCistForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistForwardDelay.setStatus("current")
_Dot1sMstpUpCount_Type = Counter32
_Dot1sMstpUpCount_Object = MibTableColumn
dot1sMstpUpCount = _Dot1sMstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 19),
    _Dot1sMstpUpCount_Type()
)
dot1sMstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstpUpCount.setStatus("current")
_Dot1sMstpDownCount_Type = Counter32
_Dot1sMstpDownCount_Object = MibTableColumn
dot1sMstpDownCount = _Dot1sMstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 20),
    _Dot1sMstpDownCount_Type()
)
dot1sMstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstpDownCount.setStatus("current")


class _Dot1sPathCostDefaultType_Type(Integer32):
    """Custom type dot1sPathCostDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_Dot1sPathCostDefaultType_Type.__name__ = "Integer32"
_Dot1sPathCostDefaultType_Object = MibTableColumn
dot1sPathCostDefaultType = _Dot1sPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 21),
    _Dot1sPathCostDefaultType_Type()
)
dot1sPathCostDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sPathCostDefaultType.setStatus("current")


class _Dot1sTrace_Type(Integer32):
    """Custom type dot1sTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1sTrace_Type.__name__ = "Integer32"
_Dot1sTrace_Object = MibTableColumn
dot1sTrace = _Dot1sTrace_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 22),
    _Dot1sTrace_Type()
)
dot1sTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sTrace.setStatus("current")


class _Dot1sDebug_Type(Integer32):
    """Custom type dot1sDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_Dot1sDebug_Type.__name__ = "Integer32"
_Dot1sDebug_Object = MibTableColumn
dot1sDebug = _Dot1sDebug_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 23),
    _Dot1sDebug_Type()
)
dot1sDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sDebug.setStatus("current")


class _Dot1sForceProtocolVersion_Type(Integer32):
    """Custom type dot1sForceProtocolVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_Dot1sForceProtocolVersion_Type.__name__ = "Integer32"
_Dot1sForceProtocolVersion_Object = MibTableColumn
dot1sForceProtocolVersion = _Dot1sForceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 24),
    _Dot1sForceProtocolVersion_Type()
)
dot1sForceProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sForceProtocolVersion.setStatus("current")


class _Dot1sTxHoldCount_Type(Integer32):
    """Custom type dot1sTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1sTxHoldCount_Type.__name__ = "Integer32"
_Dot1sTxHoldCount_Object = MibTableColumn
dot1sTxHoldCount = _Dot1sTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 25),
    _Dot1sTxHoldCount_Type()
)
dot1sTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sTxHoldCount.setStatus("current")


class _Dot1sMstiConfigIdSel_Type(Integer32):
    """Custom type dot1sMstiConfigIdSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1sMstiConfigIdSel_Type.__name__ = "Integer32"
_Dot1sMstiConfigIdSel_Object = MibTableColumn
dot1sMstiConfigIdSel = _Dot1sMstiConfigIdSel_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 26),
    _Dot1sMstiConfigIdSel_Type()
)
dot1sMstiConfigIdSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiConfigIdSel.setStatus("current")


class _Dot1sMstiRegionName_Type(OctetString):
    """Custom type dot1sMstiRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot1sMstiRegionName_Type.__name__ = "OctetString"
_Dot1sMstiRegionName_Object = MibTableColumn
dot1sMstiRegionName = _Dot1sMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 27),
    _Dot1sMstiRegionName_Type()
)
dot1sMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiRegionName.setStatus("current")


class _Dot1sMstiRegionVersion_Type(Integer32):
    """Custom type dot1sMstiRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1sMstiRegionVersion_Type.__name__ = "Integer32"
_Dot1sMstiRegionVersion_Object = MibTableColumn
dot1sMstiRegionVersion = _Dot1sMstiRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 28),
    _Dot1sMstiRegionVersion_Type()
)
dot1sMstiRegionVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiRegionVersion.setStatus("current")


class _Dot1sMstiConfigDigest_Type(OctetString):
    """Custom type dot1sMstiConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot1sMstiConfigDigest_Type.__name__ = "OctetString"
_Dot1sMstiConfigDigest_Object = MibTableColumn
dot1sMstiConfigDigest = _Dot1sMstiConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 29),
    _Dot1sMstiConfigDigest_Type()
)
dot1sMstiConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiConfigDigest.setStatus("current")
_Dot1sBufferOverFlowCount_Type = Counter32
_Dot1sBufferOverFlowCount_Object = MibTableColumn
dot1sBufferOverFlowCount = _Dot1sBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 30),
    _Dot1sBufferOverFlowCount_Type()
)
dot1sBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sBufferOverFlowCount.setStatus("current")
_Dot1sMemAllocFailureCount_Type = Counter32
_Dot1sMemAllocFailureCount_Object = MibTableColumn
dot1sMemAllocFailureCount = _Dot1sMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 31),
    _Dot1sMemAllocFailureCount_Type()
)
dot1sMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMemAllocFailureCount.setStatus("current")
_Dot1sRegionConfigChangeCount_Type = Counter32
_Dot1sRegionConfigChangeCount_Object = MibTableColumn
dot1sRegionConfigChangeCount = _Dot1sRegionConfigChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 32),
    _Dot1sRegionConfigChangeCount_Type()
)
dot1sRegionConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sRegionConfigChangeCount.setStatus("current")


class _Dot1sCistBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type dot1sCistBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_Dot1sCistBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_Dot1sCistBridgeRoleSelectionSemState_Object = MibTableColumn
dot1sCistBridgeRoleSelectionSemState = _Dot1sCistBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 33),
    _Dot1sCistBridgeRoleSelectionSemState_Type()
)
dot1sCistBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistBridgeRoleSelectionSemState.setStatus("current")
_Dot1sCistTimeSinceTopologyChange_Type = TimeTicks
_Dot1sCistTimeSinceTopologyChange_Object = MibTableColumn
dot1sCistTimeSinceTopologyChange = _Dot1sCistTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 34),
    _Dot1sCistTimeSinceTopologyChange_Type()
)
dot1sCistTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistTimeSinceTopologyChange.setStatus("current")
_Dot1sCistTopChanges_Type = Counter32
_Dot1sCistTopChanges_Object = MibTableColumn
dot1sCistTopChanges = _Dot1sCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 35),
    _Dot1sCistTopChanges_Type()
)
dot1sCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistTopChanges.setStatus("current")
_Dot1sCistNewRootBridgeCount_Type = Counter32
_Dot1sCistNewRootBridgeCount_Object = MibTableColumn
dot1sCistNewRootBridgeCount = _Dot1sCistNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 36),
    _Dot1sCistNewRootBridgeCount_Type()
)
dot1sCistNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistNewRootBridgeCount.setStatus("current")
_Dot1sCistHelloTime_Type = Timeout
_Dot1sCistHelloTime_Object = MibTableColumn
dot1sCistHelloTime = _Dot1sCistHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 37),
    _Dot1sCistHelloTime_Type()
)
dot1sCistHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistHelloTime.setStatus("current")


class _Dot1sCistBridgeHelloTime_Type(Timeout):
    """Custom type dot1sCistBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_Dot1sCistBridgeHelloTime_Type.__name__ = "Timeout"
_Dot1sCistBridgeHelloTime_Object = MibTableColumn
dot1sCistBridgeHelloTime = _Dot1sCistBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 38),
    _Dot1sCistBridgeHelloTime_Type()
)
dot1sCistBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistBridgeHelloTime.setStatus("current")


class _Dot1sCistDynamicPathcostCalculation_Type(TruthValue):
    """Custom type dot1sCistDynamicPathcostCalculation based on TruthValue"""


_Dot1sCistDynamicPathcostCalculation_Object = MibTableColumn
dot1sCistDynamicPathcostCalculation = _Dot1sCistDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 39),
    _Dot1sCistDynamicPathcostCalculation_Type()
)
dot1sCistDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistDynamicPathcostCalculation.setStatus("current")


class _Dot1sContextName_Type(DisplayString):
    """Custom type dot1sContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot1sContextName_Type.__name__ = "DisplayString"
_Dot1sContextName_Object = MibTableColumn
dot1sContextName = _Dot1sContextName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 3, 1, 40),
    _Dot1sContextName_Type()
)
dot1sContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sContextName.setStatus("current")
_Dot1sMstiBridgeTable_Object = MibTable
dot1sMstiBridgeTable = _Dot1sMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4)
)
if mibBuilder.loadTexts:
    dot1sMstiBridgeTable.setStatus("current")
_Dot1sMstiBridgeEntry_Object = MibTableRow
dot1sMstiBridgeEntry = _Dot1sMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1)
)
dot1sMstiBridgeEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sMstContextId"),
    (0, "AT-GS950-16-MIB", "dot1sMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    dot1sMstiBridgeEntry.setStatus("current")


class _Dot1sMstiInstanceIndex_Type(Integer32):
    """Custom type dot1sMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Dot1sMstiInstanceIndex_Type.__name__ = "Integer32"
_Dot1sMstiInstanceIndex_Object = MibTableColumn
dot1sMstiInstanceIndex = _Dot1sMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 1),
    _Dot1sMstiInstanceIndex_Type()
)
dot1sMstiInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1sMstiInstanceIndex.setStatus("current")
_Dot1sMstiBridgeRegionalRoot_Type = BridgeId
_Dot1sMstiBridgeRegionalRoot_Object = MibTableColumn
dot1sMstiBridgeRegionalRoot = _Dot1sMstiBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 2),
    _Dot1sMstiBridgeRegionalRoot_Type()
)
dot1sMstiBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiBridgeRegionalRoot.setStatus("current")


class _Dot1sMstiBridgePriority_Type(Integer32):
    """Custom type dot1sMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Dot1sMstiBridgePriority_Type.__name__ = "Integer32"
_Dot1sMstiBridgePriority_Object = MibTableColumn
dot1sMstiBridgePriority = _Dot1sMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 3),
    _Dot1sMstiBridgePriority_Type()
)
dot1sMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiBridgePriority.setStatus("current")
_Dot1sMstiRootCost_Type = Integer32
_Dot1sMstiRootCost_Object = MibTableColumn
dot1sMstiRootCost = _Dot1sMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 4),
    _Dot1sMstiRootCost_Type()
)
dot1sMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiRootCost.setStatus("current")
_Dot1sMstiRootPort_Type = Integer32
_Dot1sMstiRootPort_Object = MibTableColumn
dot1sMstiRootPort = _Dot1sMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 5),
    _Dot1sMstiRootPort_Type()
)
dot1sMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiRootPort.setStatus("current")
_Dot1sMstiTimeSinceTopologyChange_Type = TimeTicks
_Dot1sMstiTimeSinceTopologyChange_Object = MibTableColumn
dot1sMstiTimeSinceTopologyChange = _Dot1sMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 6),
    _Dot1sMstiTimeSinceTopologyChange_Type()
)
dot1sMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiTimeSinceTopologyChange.setStatus("current")
_Dot1sMstiTopChanges_Type = Counter32
_Dot1sMstiTopChanges_Object = MibTableColumn
dot1sMstiTopChanges = _Dot1sMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 7),
    _Dot1sMstiTopChanges_Type()
)
dot1sMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiTopChanges.setStatus("current")
_Dot1sMstiNewRootBridgeCount_Type = Counter32
_Dot1sMstiNewRootBridgeCount_Object = MibTableColumn
dot1sMstiNewRootBridgeCount = _Dot1sMstiNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 8),
    _Dot1sMstiNewRootBridgeCount_Type()
)
dot1sMstiNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiNewRootBridgeCount.setStatus("current")


class _Dot1sMstiBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type dot1sMstiBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_Dot1sMstiBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_Dot1sMstiBridgeRoleSelectionSemState_Object = MibTableColumn
dot1sMstiBridgeRoleSelectionSemState = _Dot1sMstiBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 9),
    _Dot1sMstiBridgeRoleSelectionSemState_Type()
)
dot1sMstiBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiBridgeRoleSelectionSemState.setStatus("current")
_Dot1sInstanceUpCount_Type = Counter32
_Dot1sInstanceUpCount_Object = MibTableColumn
dot1sInstanceUpCount = _Dot1sInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 10),
    _Dot1sInstanceUpCount_Type()
)
dot1sInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sInstanceUpCount.setStatus("current")
_Dot1sInstanceDownCount_Type = Counter32
_Dot1sInstanceDownCount_Object = MibTableColumn
dot1sInstanceDownCount = _Dot1sInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 11),
    _Dot1sInstanceDownCount_Type()
)
dot1sInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sInstanceDownCount.setStatus("current")
_Dot1sOldDesignatedRoot_Type = BridgeId
_Dot1sOldDesignatedRoot_Object = MibTableColumn
dot1sOldDesignatedRoot = _Dot1sOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 4, 1, 12),
    _Dot1sOldDesignatedRoot_Type()
)
dot1sOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sOldDesignatedRoot.setStatus("current")
_Dot1sVlanInstanceMappingTable_Object = MibTable
dot1sVlanInstanceMappingTable = _Dot1sVlanInstanceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5)
)
if mibBuilder.loadTexts:
    dot1sVlanInstanceMappingTable.setStatus("current")
_Dot1sVlanInstanceMappingEntry_Object = MibTableRow
dot1sVlanInstanceMappingEntry = _Dot1sVlanInstanceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1)
)
dot1sVlanInstanceMappingEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sMstContextId"),
    (0, "AT-GS950-16-MIB", "dot1sInstanceIndex"),
)
if mibBuilder.loadTexts:
    dot1sVlanInstanceMappingEntry.setStatus("current")


class _Dot1sInstanceIndex_Type(Integer32):
    """Custom type dot1sInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Dot1sInstanceIndex_Type.__name__ = "Integer32"
_Dot1sInstanceIndex_Object = MibTableColumn
dot1sInstanceIndex = _Dot1sInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 1),
    _Dot1sInstanceIndex_Type()
)
dot1sInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1sInstanceIndex.setStatus("current")
_Dot1sMapVlanIndex_Type = VlanId
_Dot1sMapVlanIndex_Object = MibTableColumn
dot1sMapVlanIndex = _Dot1sMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 2),
    _Dot1sMapVlanIndex_Type()
)
dot1sMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMapVlanIndex.setStatus("current")
_Dot1sUnMapVlanIndex_Type = VlanId
_Dot1sUnMapVlanIndex_Object = MibTableColumn
dot1sUnMapVlanIndex = _Dot1sUnMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 3),
    _Dot1sUnMapVlanIndex_Type()
)
dot1sUnMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sUnMapVlanIndex.setStatus("current")


class _Dot1sSetVlanList_Type(OctetString):
    """Custom type dot1sSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Dot1sSetVlanList_Type.__name__ = "OctetString"
_Dot1sSetVlanList_Object = MibTableColumn
dot1sSetVlanList = _Dot1sSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 4),
    _Dot1sSetVlanList_Type()
)
dot1sSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sSetVlanList.setStatus("current")


class _Dot1sResetVlanList_Type(OctetString):
    """Custom type dot1sResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Dot1sResetVlanList_Type.__name__ = "OctetString"
_Dot1sResetVlanList_Object = MibTableColumn
dot1sResetVlanList = _Dot1sResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 5),
    _Dot1sResetVlanList_Type()
)
dot1sResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sResetVlanList.setStatus("current")


class _Dot1sInstanceVlanMapped_Type(OctetString):
    """Custom type dot1sInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot1sInstanceVlanMapped_Type.__name__ = "OctetString"
_Dot1sInstanceVlanMapped_Object = MibTableColumn
dot1sInstanceVlanMapped = _Dot1sInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 6),
    _Dot1sInstanceVlanMapped_Type()
)
dot1sInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sInstanceVlanMapped.setStatus("current")


class _Dot1sInstanceVlanMapped2k_Type(OctetString):
    """Custom type dot1sInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot1sInstanceVlanMapped2k_Type.__name__ = "OctetString"
_Dot1sInstanceVlanMapped2k_Object = MibTableColumn
dot1sInstanceVlanMapped2k = _Dot1sInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 7),
    _Dot1sInstanceVlanMapped2k_Type()
)
dot1sInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sInstanceVlanMapped2k.setStatus("current")


class _Dot1sInstanceVlanMapped3k_Type(OctetString):
    """Custom type dot1sInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot1sInstanceVlanMapped3k_Type.__name__ = "OctetString"
_Dot1sInstanceVlanMapped3k_Object = MibTableColumn
dot1sInstanceVlanMapped3k = _Dot1sInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 8),
    _Dot1sInstanceVlanMapped3k_Type()
)
dot1sInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sInstanceVlanMapped3k.setStatus("current")


class _Dot1sInstanceVlanMapped4k_Type(OctetString):
    """Custom type dot1sInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot1sInstanceVlanMapped4k_Type.__name__ = "OctetString"
_Dot1sInstanceVlanMapped4k_Object = MibTableColumn
dot1sInstanceVlanMapped4k = _Dot1sInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 5, 1, 9),
    _Dot1sInstanceVlanMapped4k_Type()
)
dot1sInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sInstanceVlanMapped4k.setStatus("current")
_Dot1sCistPortTable_Object = MibTable
dot1sCistPortTable = _Dot1sCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6)
)
if mibBuilder.loadTexts:
    dot1sCistPortTable.setStatus("current")
_Dot1sCistPortEntry_Object = MibTableRow
dot1sCistPortEntry = _Dot1sCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1)
)
dot1sCistPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sCistPort"),
)
if mibBuilder.loadTexts:
    dot1sCistPortEntry.setStatus("current")


class _Dot1sCistPort_Type(Integer32):
    """Custom type dot1sCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1sCistPort_Type.__name__ = "Integer32"
_Dot1sCistPort_Object = MibTableColumn
dot1sCistPort = _Dot1sCistPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 1),
    _Dot1sCistPort_Type()
)
dot1sCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1sCistPort.setStatus("current")


class _Dot1sCistPortPathCost_Type(Integer32):
    """Custom type dot1sCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Dot1sCistPortPathCost_Type.__name__ = "Integer32"
_Dot1sCistPortPathCost_Object = MibTableColumn
dot1sCistPortPathCost = _Dot1sCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 2),
    _Dot1sCistPortPathCost_Type()
)
dot1sCistPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortPathCost.setStatus("current")


class _Dot1sCistPortPriority_Type(Integer32):
    """Custom type dot1sCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Dot1sCistPortPriority_Type.__name__ = "Integer32"
_Dot1sCistPortPriority_Object = MibTableColumn
dot1sCistPortPriority = _Dot1sCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 3),
    _Dot1sCistPortPriority_Type()
)
dot1sCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortPriority.setStatus("current")
_Dot1sCistPortDesignatedRoot_Type = BridgeId
_Dot1sCistPortDesignatedRoot_Object = MibTableColumn
dot1sCistPortDesignatedRoot = _Dot1sCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 4),
    _Dot1sCistPortDesignatedRoot_Type()
)
dot1sCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortDesignatedRoot.setStatus("current")
_Dot1sCistPortDesignatedBridge_Type = BridgeId
_Dot1sCistPortDesignatedBridge_Object = MibTableColumn
dot1sCistPortDesignatedBridge = _Dot1sCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 5),
    _Dot1sCistPortDesignatedBridge_Type()
)
dot1sCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortDesignatedBridge.setStatus("current")


class _Dot1sCistPortDesignatedPort_Type(OctetString):
    """Custom type dot1sCistPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Dot1sCistPortDesignatedPort_Type.__name__ = "OctetString"
_Dot1sCistPortDesignatedPort_Object = MibTableColumn
dot1sCistPortDesignatedPort = _Dot1sCistPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 6),
    _Dot1sCistPortDesignatedPort_Type()
)
dot1sCistPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortDesignatedPort.setStatus("current")


class _Dot1sCistPortAdminP2P_Type(Integer32):
    """Custom type dot1sCistPortAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_Dot1sCistPortAdminP2P_Type.__name__ = "Integer32"
_Dot1sCistPortAdminP2P_Object = MibTableColumn
dot1sCistPortAdminP2P = _Dot1sCistPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 7),
    _Dot1sCistPortAdminP2P_Type()
)
dot1sCistPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortAdminP2P.setStatus("current")
_Dot1sCistPortOperP2P_Type = TruthValue
_Dot1sCistPortOperP2P_Object = MibTableColumn
dot1sCistPortOperP2P = _Dot1sCistPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 8),
    _Dot1sCistPortOperP2P_Type()
)
dot1sCistPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortOperP2P.setStatus("current")
_Dot1sCistPortAdminEdgeStatus_Type = TruthValue
_Dot1sCistPortAdminEdgeStatus_Object = MibTableColumn
dot1sCistPortAdminEdgeStatus = _Dot1sCistPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 9),
    _Dot1sCistPortAdminEdgeStatus_Type()
)
dot1sCistPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortAdminEdgeStatus.setStatus("current")
_Dot1sCistPortOperEdgeStatus_Type = TruthValue
_Dot1sCistPortOperEdgeStatus_Object = MibTableColumn
dot1sCistPortOperEdgeStatus = _Dot1sCistPortOperEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 10),
    _Dot1sCistPortOperEdgeStatus_Type()
)
dot1sCistPortOperEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortOperEdgeStatus.setStatus("current")
_Dot1sCistPortProtocolMigration_Type = TruthValue
_Dot1sCistPortProtocolMigration_Object = MibTableColumn
dot1sCistPortProtocolMigration = _Dot1sCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 11),
    _Dot1sCistPortProtocolMigration_Type()
)
dot1sCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortProtocolMigration.setStatus("current")


class _Dot1sCistPortState_Type(Integer32):
    """Custom type dot1sCistPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_Dot1sCistPortState_Type.__name__ = "Integer32"
_Dot1sCistPortState_Object = MibTableColumn
dot1sCistPortState = _Dot1sCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 12),
    _Dot1sCistPortState_Type()
)
dot1sCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortState.setStatus("current")


class _Dot1sCistForcePortState_Type(Integer32):
    """Custom type dot1sCistForcePortState based on Integer32"""
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


_Dot1sCistForcePortState_Type.__name__ = "Integer32"
_Dot1sCistForcePortState_Object = MibTableColumn
dot1sCistForcePortState = _Dot1sCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 13),
    _Dot1sCistForcePortState_Type()
)
dot1sCistForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistForcePortState.setStatus("current")
_Dot1sCistPortForwardTransitions_Type = Counter32
_Dot1sCistPortForwardTransitions_Object = MibTableColumn
dot1sCistPortForwardTransitions = _Dot1sCistPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 14),
    _Dot1sCistPortForwardTransitions_Type()
)
dot1sCistPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortForwardTransitions.setStatus("current")
_Dot1sCistPortRxMstBpduCount_Type = Counter32
_Dot1sCistPortRxMstBpduCount_Object = MibTableColumn
dot1sCistPortRxMstBpduCount = _Dot1sCistPortRxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 15),
    _Dot1sCistPortRxMstBpduCount_Type()
)
dot1sCistPortRxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRxMstBpduCount.setStatus("current")
_Dot1sCistPortRxRstBpduCount_Type = Counter32
_Dot1sCistPortRxRstBpduCount_Object = MibTableColumn
dot1sCistPortRxRstBpduCount = _Dot1sCistPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 16),
    _Dot1sCistPortRxRstBpduCount_Type()
)
dot1sCistPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRxRstBpduCount.setStatus("current")
_Dot1sCistPortRxConfigBpduCount_Type = Counter32
_Dot1sCistPortRxConfigBpduCount_Object = MibTableColumn
dot1sCistPortRxConfigBpduCount = _Dot1sCistPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 17),
    _Dot1sCistPortRxConfigBpduCount_Type()
)
dot1sCistPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRxConfigBpduCount.setStatus("current")
_Dot1sCistPortRxTcnBpduCount_Type = Counter32
_Dot1sCistPortRxTcnBpduCount_Object = MibTableColumn
dot1sCistPortRxTcnBpduCount = _Dot1sCistPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 18),
    _Dot1sCistPortRxTcnBpduCount_Type()
)
dot1sCistPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRxTcnBpduCount.setStatus("current")
_Dot1sCistPortTxMstBpduCount_Type = Counter32
_Dot1sCistPortTxMstBpduCount_Object = MibTableColumn
dot1sCistPortTxMstBpduCount = _Dot1sCistPortTxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 19),
    _Dot1sCistPortTxMstBpduCount_Type()
)
dot1sCistPortTxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortTxMstBpduCount.setStatus("current")
_Dot1sCistPortTxRstBpduCount_Type = Counter32
_Dot1sCistPortTxRstBpduCount_Object = MibTableColumn
dot1sCistPortTxRstBpduCount = _Dot1sCistPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 20),
    _Dot1sCistPortTxRstBpduCount_Type()
)
dot1sCistPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortTxRstBpduCount.setStatus("current")
_Dot1sCistPortTxConfigBpduCount_Type = Counter32
_Dot1sCistPortTxConfigBpduCount_Object = MibTableColumn
dot1sCistPortTxConfigBpduCount = _Dot1sCistPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 21),
    _Dot1sCistPortTxConfigBpduCount_Type()
)
dot1sCistPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortTxConfigBpduCount.setStatus("current")
_Dot1sCistPortTxTcnBpduCount_Type = Counter32
_Dot1sCistPortTxTcnBpduCount_Object = MibTableColumn
dot1sCistPortTxTcnBpduCount = _Dot1sCistPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 22),
    _Dot1sCistPortTxTcnBpduCount_Type()
)
dot1sCistPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortTxTcnBpduCount.setStatus("current")
_Dot1sCistPortInvalidMstBpduRxCount_Type = Counter32
_Dot1sCistPortInvalidMstBpduRxCount_Object = MibTableColumn
dot1sCistPortInvalidMstBpduRxCount = _Dot1sCistPortInvalidMstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 23),
    _Dot1sCistPortInvalidMstBpduRxCount_Type()
)
dot1sCistPortInvalidMstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortInvalidMstBpduRxCount.setStatus("current")
_Dot1sCistPortInvalidRstBpduRxCount_Type = Counter32
_Dot1sCistPortInvalidRstBpduRxCount_Object = MibTableColumn
dot1sCistPortInvalidRstBpduRxCount = _Dot1sCistPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 24),
    _Dot1sCistPortInvalidRstBpduRxCount_Type()
)
dot1sCistPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortInvalidRstBpduRxCount.setStatus("current")
_Dot1sCistPortInvalidConfigBpduRxCount_Type = Counter32
_Dot1sCistPortInvalidConfigBpduRxCount_Object = MibTableColumn
dot1sCistPortInvalidConfigBpduRxCount = _Dot1sCistPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 25),
    _Dot1sCistPortInvalidConfigBpduRxCount_Type()
)
dot1sCistPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortInvalidConfigBpduRxCount.setStatus("current")
_Dot1sCistPortInvalidTcnBpduRxCount_Type = Counter32
_Dot1sCistPortInvalidTcnBpduRxCount_Object = MibTableColumn
dot1sCistPortInvalidTcnBpduRxCount = _Dot1sCistPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 26),
    _Dot1sCistPortInvalidTcnBpduRxCount_Type()
)
dot1sCistPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortInvalidTcnBpduRxCount.setStatus("current")


class _Dot1sCistPortTransmitSemState_Type(Integer32):
    """Custom type dot1sCistPortTransmitSemState based on Integer32"""
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
        *(("idle", 5),
          ("transmitconfig", 2),
          ("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitrstp", 4),
          ("transmittcn", 3))
    )


_Dot1sCistPortTransmitSemState_Type.__name__ = "Integer32"
_Dot1sCistPortTransmitSemState_Object = MibTableColumn
dot1sCistPortTransmitSemState = _Dot1sCistPortTransmitSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 27),
    _Dot1sCistPortTransmitSemState_Type()
)
dot1sCistPortTransmitSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortTransmitSemState.setStatus("current")


class _Dot1sCistPortReceiveSemState_Type(Integer32):
    """Custom type dot1sCistPortReceiveSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("receive", 1))
    )


_Dot1sCistPortReceiveSemState_Type.__name__ = "Integer32"
_Dot1sCistPortReceiveSemState_Object = MibTableColumn
dot1sCistPortReceiveSemState = _Dot1sCistPortReceiveSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 28),
    _Dot1sCistPortReceiveSemState_Type()
)
dot1sCistPortReceiveSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortReceiveSemState.setStatus("current")


class _Dot1sCistPortProtMigrationSemState_Type(Integer32):
    """Custom type dot1sCistPortProtMigrationSemState based on Integer32"""
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
        *(("init", 0),
          ("sendingrstp", 2),
          ("sendingstp", 4),
          ("sendrstp", 1),
          ("sendstp", 3))
    )


_Dot1sCistPortProtMigrationSemState_Type.__name__ = "Integer32"
_Dot1sCistPortProtMigrationSemState_Object = MibTableColumn
dot1sCistPortProtMigrationSemState = _Dot1sCistPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 29),
    _Dot1sCistPortProtMigrationSemState_Type()
)
dot1sCistPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortProtMigrationSemState.setStatus("current")
_Dot1sCistProtocolMigrationCount_Type = Counter32
_Dot1sCistProtocolMigrationCount_Object = MibTableColumn
dot1sCistProtocolMigrationCount = _Dot1sCistProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 30),
    _Dot1sCistProtocolMigrationCount_Type()
)
dot1sCistProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistProtocolMigrationCount.setStatus("current")
_Dot1sCistPortDesignatedCost_Type = Integer32
_Dot1sCistPortDesignatedCost_Object = MibTableColumn
dot1sCistPortDesignatedCost = _Dot1sCistPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 31),
    _Dot1sCistPortDesignatedCost_Type()
)
dot1sCistPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortDesignatedCost.setStatus("current")
_Dot1sCistPortRegionalRoot_Type = BridgeId
_Dot1sCistPortRegionalRoot_Object = MibTableColumn
dot1sCistPortRegionalRoot = _Dot1sCistPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 32),
    _Dot1sCistPortRegionalRoot_Type()
)
dot1sCistPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRegionalRoot.setStatus("current")
_Dot1sCistPortRegionalPathCost_Type = Integer32
_Dot1sCistPortRegionalPathCost_Object = MibTableColumn
dot1sCistPortRegionalPathCost = _Dot1sCistPortRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 33),
    _Dot1sCistPortRegionalPathCost_Type()
)
dot1sCistPortRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRegionalPathCost.setStatus("current")


class _Dot1sCistSelectedPortRole_Type(Integer32):
    """Custom type dot1sCistSelectedPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("root", 3))
    )


_Dot1sCistSelectedPortRole_Type.__name__ = "Integer32"
_Dot1sCistSelectedPortRole_Object = MibTableColumn
dot1sCistSelectedPortRole = _Dot1sCistSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 34),
    _Dot1sCistSelectedPortRole_Type()
)
dot1sCistSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistSelectedPortRole.setStatus("current")


class _Dot1sCistCurrentPortRole_Type(Integer32):
    """Custom type dot1sCistCurrentPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("root", 3))
    )


_Dot1sCistCurrentPortRole_Type.__name__ = "Integer32"
_Dot1sCistCurrentPortRole_Object = MibTableColumn
dot1sCistCurrentPortRole = _Dot1sCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 35),
    _Dot1sCistCurrentPortRole_Type()
)
dot1sCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistCurrentPortRole.setStatus("current")


class _Dot1sCistPortInfoSemState_Type(Integer32):
    """Custom type dot1sCistPortInfoSemState based on Integer32"""
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
        *(("aged", 1),
          ("current", 7),
          ("disabled", 0),
          ("inferiordesg", 5),
          ("notdesg", 6),
          ("other", 9),
          ("receive", 8),
          ("repeatdesg", 4),
          ("superiordesg", 3),
          ("update", 2))
    )


_Dot1sCistPortInfoSemState_Type.__name__ = "Integer32"
_Dot1sCistPortInfoSemState_Object = MibTableColumn
dot1sCistPortInfoSemState = _Dot1sCistPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 36),
    _Dot1sCistPortInfoSemState_Type()
)
dot1sCistPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortInfoSemState.setStatus("current")


class _Dot1sCistPortRoleTransitionSemState_Type(Integer32):
    """Custom type dot1sCistPortRoleTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternateport", 5),
          ("designatedport", 4),
          ("disabledport", 2),
          ("disableport", 1),
          ("init", 0),
          ("masterport", 6),
          ("rootport", 3))
    )


_Dot1sCistPortRoleTransitionSemState_Type.__name__ = "Integer32"
_Dot1sCistPortRoleTransitionSemState_Object = MibTableColumn
dot1sCistPortRoleTransitionSemState = _Dot1sCistPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 37),
    _Dot1sCistPortRoleTransitionSemState_Type()
)
dot1sCistPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortRoleTransitionSemState.setStatus("current")


class _Dot1sCistPortStateTransitionSemState_Type(Integer32):
    """Custom type dot1sCistPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_Dot1sCistPortStateTransitionSemState_Type.__name__ = "Integer32"
_Dot1sCistPortStateTransitionSemState_Object = MibTableColumn
dot1sCistPortStateTransitionSemState = _Dot1sCistPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 38),
    _Dot1sCistPortStateTransitionSemState_Type()
)
dot1sCistPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortStateTransitionSemState.setStatus("current")


class _Dot1sCistPortTopologyChangeSemState_Type(Integer32):
    """Custom type dot1sCistPortTopologyChangeSemState based on Integer32"""
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
        *(("acknowledged", 7),
          ("active", 3),
          ("detected", 2),
          ("inactive", 0),
          ("learning", 1),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_Dot1sCistPortTopologyChangeSemState_Type.__name__ = "Integer32"
_Dot1sCistPortTopologyChangeSemState_Object = MibTableColumn
dot1sCistPortTopologyChangeSemState = _Dot1sCistPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 39),
    _Dot1sCistPortTopologyChangeSemState_Type()
)
dot1sCistPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortTopologyChangeSemState.setStatus("current")


class _Dot1sCistPortHelloTime_Type(Timeout):
    """Custom type dot1sCistPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_Dot1sCistPortHelloTime_Type.__name__ = "Timeout"
_Dot1sCistPortHelloTime_Object = MibTableColumn
dot1sCistPortHelloTime = _Dot1sCistPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 40),
    _Dot1sCistPortHelloTime_Type()
)
dot1sCistPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortHelloTime.setStatus("current")


class _Dot1sCistPortOperVersion_Type(Integer32):
    """Custom type dot1sCistPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_Dot1sCistPortOperVersion_Type.__name__ = "Integer32"
_Dot1sCistPortOperVersion_Object = MibTableColumn
dot1sCistPortOperVersion = _Dot1sCistPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 41),
    _Dot1sCistPortOperVersion_Type()
)
dot1sCistPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortOperVersion.setStatus("current")
_Dot1sCistPortEffectivePortState_Type = TruthValue
_Dot1sCistPortEffectivePortState_Object = MibTableColumn
dot1sCistPortEffectivePortState = _Dot1sCistPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 42),
    _Dot1sCistPortEffectivePortState_Type()
)
dot1sCistPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sCistPortEffectivePortState.setStatus("current")
_Dot1sCistPortAutoEdgeStatus_Type = TruthValue
_Dot1sCistPortAutoEdgeStatus_Object = MibTableColumn
dot1sCistPortAutoEdgeStatus = _Dot1sCistPortAutoEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 43),
    _Dot1sCistPortAutoEdgeStatus_Type()
)
dot1sCistPortAutoEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortAutoEdgeStatus.setStatus("current")
_Dot1sCistPortRestrictedRole_Type = TruthValue
_Dot1sCistPortRestrictedRole_Object = MibTableColumn
dot1sCistPortRestrictedRole = _Dot1sCistPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 44),
    _Dot1sCistPortRestrictedRole_Type()
)
dot1sCistPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortRestrictedRole.setStatus("current")
_Dot1sCistPortRestrictedTCN_Type = TruthValue
_Dot1sCistPortRestrictedTCN_Object = MibTableColumn
dot1sCistPortRestrictedTCN = _Dot1sCistPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 6, 1, 45),
    _Dot1sCistPortRestrictedTCN_Type()
)
dot1sCistPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sCistPortRestrictedTCN.setStatus("current")
_Dot1sMstiPortTable_Object = MibTable
dot1sMstiPortTable = _Dot1sMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7)
)
if mibBuilder.loadTexts:
    dot1sMstiPortTable.setStatus("current")
_Dot1sMstiPortEntry_Object = MibTableRow
dot1sMstiPortEntry = _Dot1sMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1)
)
dot1sMstiPortEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sMstiPort"),
    (0, "AT-GS950-16-MIB", "dot1sInstanceIndex"),
)
if mibBuilder.loadTexts:
    dot1sMstiPortEntry.setStatus("current")


class _Dot1sMstiPort_Type(Integer32):
    """Custom type dot1sMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1sMstiPort_Type.__name__ = "Integer32"
_Dot1sMstiPort_Object = MibTableColumn
dot1sMstiPort = _Dot1sMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 1),
    _Dot1sMstiPort_Type()
)
dot1sMstiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1sMstiPort.setStatus("current")


class _Dot1sMstiPortPathCost_Type(Integer32):
    """Custom type dot1sMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Dot1sMstiPortPathCost_Type.__name__ = "Integer32"
_Dot1sMstiPortPathCost_Object = MibTableColumn
dot1sMstiPortPathCost = _Dot1sMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 2),
    _Dot1sMstiPortPathCost_Type()
)
dot1sMstiPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiPortPathCost.setStatus("current")


class _Dot1sMstiPortPriority_Type(Integer32):
    """Custom type dot1sMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Dot1sMstiPortPriority_Type.__name__ = "Integer32"
_Dot1sMstiPortPriority_Object = MibTableColumn
dot1sMstiPortPriority = _Dot1sMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 3),
    _Dot1sMstiPortPriority_Type()
)
dot1sMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiPortPriority.setStatus("current")
_Dot1sMstiPortDesignatedRoot_Type = BridgeId
_Dot1sMstiPortDesignatedRoot_Object = MibTableColumn
dot1sMstiPortDesignatedRoot = _Dot1sMstiPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 4),
    _Dot1sMstiPortDesignatedRoot_Type()
)
dot1sMstiPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortDesignatedRoot.setStatus("current")
_Dot1sMstiPortDesignatedBridge_Type = BridgeId
_Dot1sMstiPortDesignatedBridge_Object = MibTableColumn
dot1sMstiPortDesignatedBridge = _Dot1sMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 5),
    _Dot1sMstiPortDesignatedBridge_Type()
)
dot1sMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortDesignatedBridge.setStatus("current")


class _Dot1sMstiPortDesignatedPort_Type(OctetString):
    """Custom type dot1sMstiPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Dot1sMstiPortDesignatedPort_Type.__name__ = "OctetString"
_Dot1sMstiPortDesignatedPort_Object = MibTableColumn
dot1sMstiPortDesignatedPort = _Dot1sMstiPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 6),
    _Dot1sMstiPortDesignatedPort_Type()
)
dot1sMstiPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortDesignatedPort.setStatus("current")


class _Dot1sMstiPortState_Type(Integer32):
    """Custom type dot1sMstiPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_Dot1sMstiPortState_Type.__name__ = "Integer32"
_Dot1sMstiPortState_Object = MibTableColumn
dot1sMstiPortState = _Dot1sMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 7),
    _Dot1sMstiPortState_Type()
)
dot1sMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortState.setStatus("current")


class _Dot1sMstiForcePortState_Type(Integer32):
    """Custom type dot1sMstiForcePortState based on Integer32"""
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


_Dot1sMstiForcePortState_Type.__name__ = "Integer32"
_Dot1sMstiForcePortState_Object = MibTableColumn
dot1sMstiForcePortState = _Dot1sMstiForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 8),
    _Dot1sMstiForcePortState_Type()
)
dot1sMstiForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstiForcePortState.setStatus("current")
_Dot1sMstiPortForwardTransitions_Type = Counter32
_Dot1sMstiPortForwardTransitions_Object = MibTableColumn
dot1sMstiPortForwardTransitions = _Dot1sMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 9),
    _Dot1sMstiPortForwardTransitions_Type()
)
dot1sMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortForwardTransitions.setStatus("current")
_Dot1sMstiPortReceivedBPDUs_Type = Counter32
_Dot1sMstiPortReceivedBPDUs_Object = MibTableColumn
dot1sMstiPortReceivedBPDUs = _Dot1sMstiPortReceivedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 10),
    _Dot1sMstiPortReceivedBPDUs_Type()
)
dot1sMstiPortReceivedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortReceivedBPDUs.setStatus("current")
_Dot1sMstiPortTransmittedBPDUs_Type = Counter32
_Dot1sMstiPortTransmittedBPDUs_Object = MibTableColumn
dot1sMstiPortTransmittedBPDUs = _Dot1sMstiPortTransmittedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 11),
    _Dot1sMstiPortTransmittedBPDUs_Type()
)
dot1sMstiPortTransmittedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortTransmittedBPDUs.setStatus("current")
_Dot1sMstiPortInvalidBPDUsRcvd_Type = Counter32
_Dot1sMstiPortInvalidBPDUsRcvd_Object = MibTableColumn
dot1sMstiPortInvalidBPDUsRcvd = _Dot1sMstiPortInvalidBPDUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 12),
    _Dot1sMstiPortInvalidBPDUsRcvd_Type()
)
dot1sMstiPortInvalidBPDUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortInvalidBPDUsRcvd.setStatus("current")
_Dot1sMstiPortDesignatedCost_Type = Integer32
_Dot1sMstiPortDesignatedCost_Object = MibTableColumn
dot1sMstiPortDesignatedCost = _Dot1sMstiPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 13),
    _Dot1sMstiPortDesignatedCost_Type()
)
dot1sMstiPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortDesignatedCost.setStatus("current")


class _Dot1sMstiSelectedPortRole_Type(Integer32):
    """Custom type dot1sMstiSelectedPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_Dot1sMstiSelectedPortRole_Type.__name__ = "Integer32"
_Dot1sMstiSelectedPortRole_Object = MibTableColumn
dot1sMstiSelectedPortRole = _Dot1sMstiSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 14),
    _Dot1sMstiSelectedPortRole_Type()
)
dot1sMstiSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiSelectedPortRole.setStatus("current")


class _Dot1sMstiCurrentPortRole_Type(Integer32):
    """Custom type dot1sMstiCurrentPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_Dot1sMstiCurrentPortRole_Type.__name__ = "Integer32"
_Dot1sMstiCurrentPortRole_Object = MibTableColumn
dot1sMstiCurrentPortRole = _Dot1sMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 15),
    _Dot1sMstiCurrentPortRole_Type()
)
dot1sMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiCurrentPortRole.setStatus("current")


class _Dot1sMstiPortInfoSemState_Type(Integer32):
    """Custom type dot1sMstiPortInfoSemState based on Integer32"""
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
        *(("aged", 1),
          ("current", 7),
          ("disabled", 0),
          ("inferiordesg", 5),
          ("notdesg", 6),
          ("other", 9),
          ("receive", 8),
          ("repeatdesg", 4),
          ("superiordesg", 3),
          ("update", 2))
    )


_Dot1sMstiPortInfoSemState_Type.__name__ = "Integer32"
_Dot1sMstiPortInfoSemState_Object = MibTableColumn
dot1sMstiPortInfoSemState = _Dot1sMstiPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 16),
    _Dot1sMstiPortInfoSemState_Type()
)
dot1sMstiPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortInfoSemState.setStatus("current")


class _Dot1sMstiPortRoleTransitionSemState_Type(Integer32):
    """Custom type dot1sMstiPortRoleTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternateport", 5),
          ("designatedport", 4),
          ("disabledport", 2),
          ("disableport", 1),
          ("init", 0),
          ("masterport", 6),
          ("rootport", 3))
    )


_Dot1sMstiPortRoleTransitionSemState_Type.__name__ = "Integer32"
_Dot1sMstiPortRoleTransitionSemState_Object = MibTableColumn
dot1sMstiPortRoleTransitionSemState = _Dot1sMstiPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 17),
    _Dot1sMstiPortRoleTransitionSemState_Type()
)
dot1sMstiPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortRoleTransitionSemState.setStatus("current")


class _Dot1sMstiPortStateTransitionSemState_Type(Integer32):
    """Custom type dot1sMstiPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_Dot1sMstiPortStateTransitionSemState_Type.__name__ = "Integer32"
_Dot1sMstiPortStateTransitionSemState_Object = MibTableColumn
dot1sMstiPortStateTransitionSemState = _Dot1sMstiPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 18),
    _Dot1sMstiPortStateTransitionSemState_Type()
)
dot1sMstiPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortStateTransitionSemState.setStatus("current")


class _Dot1sMstiPortTopologyChangeSemState_Type(Integer32):
    """Custom type dot1sMstiPortTopologyChangeSemState based on Integer32"""
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
        *(("acknowledged", 7),
          ("active", 3),
          ("detected", 2),
          ("inactive", 0),
          ("learning", 1),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_Dot1sMstiPortTopologyChangeSemState_Type.__name__ = "Integer32"
_Dot1sMstiPortTopologyChangeSemState_Object = MibTableColumn
dot1sMstiPortTopologyChangeSemState = _Dot1sMstiPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 19),
    _Dot1sMstiPortTopologyChangeSemState_Type()
)
dot1sMstiPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortTopologyChangeSemState.setStatus("current")
_Dot1sMstiPortEffectivePortState_Type = TruthValue
_Dot1sMstiPortEffectivePortState_Object = MibTableColumn
dot1sMstiPortEffectivePortState = _Dot1sMstiPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 1, 7, 1, 20),
    _Dot1sMstiPortEffectivePortState_Type()
)
dot1sMstiPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sMstiPortEffectivePortState.setStatus("current")
_Dot1sMstTrapsControl_ObjectIdentity = ObjectIdentity
dot1sMstTrapsControl = _Dot1sMstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2)
)


class _Dot1sMstSetGlobalTrapOption_Type(Integer32):
    """Custom type dot1sMstSetGlobalTrapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dot1sMstSetGlobalTrapOption_Type.__name__ = "Integer32"
_Dot1sMstSetGlobalTrapOption_Object = MibScalar
dot1sMstSetGlobalTrapOption = _Dot1sMstSetGlobalTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 1),
    _Dot1sMstSetGlobalTrapOption_Type()
)
dot1sMstSetGlobalTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sMstSetGlobalTrapOption.setStatus("current")


class _Dot1sGlobalErrTrapType_Type(Integer32):
    """Custom type dot1sGlobalErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufffail", 2),
          ("memfail", 1),
          ("none", 0))
    )


_Dot1sGlobalErrTrapType_Type.__name__ = "Integer32"
_Dot1sGlobalErrTrapType_Object = MibScalar
dot1sGlobalErrTrapType = _Dot1sGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 2),
    _Dot1sGlobalErrTrapType_Type()
)
dot1sGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sGlobalErrTrapType.setStatus("current")
_Dot1sMstTrapsControlTable_Object = MibTable
dot1sMstTrapsControlTable = _Dot1sMstTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 3)
)
if mibBuilder.loadTexts:
    dot1sMstTrapsControlTable.setStatus("current")
_Dot1sMstTrapsControlEntry_Object = MibTableRow
dot1sMstTrapsControlEntry = _Dot1sMstTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 3, 1)
)
dot1sMstTrapsControlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sMstContextId"),
)
if mibBuilder.loadTexts:
    dot1sMstTrapsControlEntry.setStatus("current")


class _Dot1sSetTraps_Type(Integer32):
    """Custom type dot1sSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot1sSetTraps_Type.__name__ = "Integer32"
_Dot1sSetTraps_Object = MibTableColumn
dot1sSetTraps = _Dot1sSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 3, 1, 1),
    _Dot1sSetTraps_Type()
)
dot1sSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1sSetTraps.setStatus("current")


class _Dot1sGenTrapType_Type(Integer32):
    """Custom type dot1sGenTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("none", 0),
          ("up", 1))
    )


_Dot1sGenTrapType_Type.__name__ = "Integer32"
_Dot1sGenTrapType_Object = MibTableColumn
dot1sGenTrapType = _Dot1sGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 3, 1, 2),
    _Dot1sGenTrapType_Type()
)
dot1sGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sGenTrapType.setStatus("current")
_Dot1sPortTrapNotificationTable_Object = MibTable
dot1sPortTrapNotificationTable = _Dot1sPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 4)
)
if mibBuilder.loadTexts:
    dot1sPortTrapNotificationTable.setStatus("current")
_Dot1sPortTrapNotificationEntry_Object = MibTableRow
dot1sPortTrapNotificationEntry = _Dot1sPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 4, 1)
)
dot1sPortTrapNotificationEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sPortTrapIndex"),
)
if mibBuilder.loadTexts:
    dot1sPortTrapNotificationEntry.setStatus("current")


class _Dot1sPortTrapIndex_Type(Integer32):
    """Custom type dot1sPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Dot1sPortTrapIndex_Type.__name__ = "Integer32"
_Dot1sPortTrapIndex_Object = MibTableColumn
dot1sPortTrapIndex = _Dot1sPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 4, 1, 1),
    _Dot1sPortTrapIndex_Type()
)
dot1sPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1sPortTrapIndex.setStatus("current")


class _Dot1sPortMigrationType_Type(Integer32):
    """Custom type dot1sPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendrstp", 1),
          ("sendstp", 0))
    )


_Dot1sPortMigrationType_Type.__name__ = "Integer32"
_Dot1sPortMigrationType_Object = MibTableColumn
dot1sPortMigrationType = _Dot1sPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 4, 1, 2),
    _Dot1sPortMigrationType_Type()
)
dot1sPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sPortMigrationType.setStatus("current")


class _Dot1sPktErrType_Type(Integer32):
    """Custom type dot1sPktErrType based on Integer32"""
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
        *(("configLengthErr", 2),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("invalidBpdu", 1),
          ("maxAgeErr", 5),
          ("mstpLengthErr", 8),
          ("protocolIdErr", 0),
          ("rstpLengthErr", 4),
          ("tcnLengthErr", 3))
    )


_Dot1sPktErrType_Type.__name__ = "Integer32"
_Dot1sPktErrType_Object = MibTableColumn
dot1sPktErrType = _Dot1sPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 4, 1, 3),
    _Dot1sPktErrType_Type()
)
dot1sPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sPktErrType.setStatus("current")
_Dot1sPktErrVal_Type = Integer32
_Dot1sPktErrVal_Object = MibTableColumn
dot1sPktErrVal = _Dot1sPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 4, 1, 4),
    _Dot1sPktErrVal_Type()
)
dot1sPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sPktErrVal.setStatus("current")
_Dot1sPortRoleTrapNotificationTable_Object = MibTable
dot1sPortRoleTrapNotificationTable = _Dot1sPortRoleTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 5)
)
if mibBuilder.loadTexts:
    dot1sPortRoleTrapNotificationTable.setStatus("current")
_Dot1sPortRoleTrapNotificationEntry_Object = MibTableRow
dot1sPortRoleTrapNotificationEntry = _Dot1sPortRoleTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 5, 1)
)
dot1sPortRoleTrapNotificationEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1sPortTrapIndex"),
    (0, "AT-GS950-16-MIB", "dot1sMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    dot1sPortRoleTrapNotificationEntry.setStatus("current")


class _Dot1sPortRoleType_Type(Integer32):
    """Custom type dot1sPortRoleType based on Integer32"""
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
        *(("alternatePort", 1),
          ("backupPort", 2),
          ("designatedPort", 4),
          ("disabledPort", 0),
          ("masterport", 5),
          ("rootPort", 3))
    )


_Dot1sPortRoleType_Type.__name__ = "Integer32"
_Dot1sPortRoleType_Object = MibTableColumn
dot1sPortRoleType = _Dot1sPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 5, 1, 1),
    _Dot1sPortRoleType_Type()
)
dot1sPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sPortRoleType.setStatus("current")


class _Dot1sOldRoleType_Type(Integer32):
    """Custom type dot1sOldRoleType based on Integer32"""
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
        *(("alternatePort", 1),
          ("backupPort", 2),
          ("designatedPort", 4),
          ("disabledPort", 0),
          ("masterport", 5),
          ("rootPort", 3))
    )


_Dot1sOldRoleType_Type.__name__ = "Integer32"
_Dot1sOldRoleType_Object = MibTableColumn
dot1sOldRoleType = _Dot1sOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 2, 5, 1, 2),
    _Dot1sOldRoleType_Type()
)
dot1sOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1sOldRoleType.setStatus("current")
_Dot1sMstTraps_ObjectIdentity = ObjectIdentity
dot1sMstTraps = _Dot1sMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3)
)
_Dot1sTraps_ObjectIdentity = ObjectIdentity
dot1sTraps = _Dot1sTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0)
)
_L2Rst_ObjectIdentity = ObjectIdentity
l2Rst = _L2Rst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119)
)
_Dot1wRst_ObjectIdentity = ObjectIdentity
dot1wRst = _Dot1wRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1)
)
_Dot1wRstTable_Object = MibTable
dot1wRstTable = _Dot1wRstTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3)
)
if mibBuilder.loadTexts:
    dot1wRstTable.setStatus("current")
_Dot1wRstEntry_Object = MibTableRow
dot1wRstEntry = _Dot1wRstEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1)
)
dot1wRstEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1wRstContextId"),
)
if mibBuilder.loadTexts:
    dot1wRstEntry.setStatus("current")


class _Dot1wRstContextId_Type(Integer32):
    """Custom type dot1wRstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1wRstContextId_Type.__name__ = "Integer32"
_Dot1wRstContextId_Object = MibTableColumn
dot1wRstContextId = _Dot1wRstContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 1),
    _Dot1wRstContextId_Type()
)
dot1wRstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1wRstContextId.setStatus("current")


class _Dot1wSystemControl_Type(Integer32):
    """Custom type dot1wSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("start", 1))
    )


_Dot1wSystemControl_Type.__name__ = "Integer32"
_Dot1wSystemControl_Object = MibTableColumn
dot1wSystemControl = _Dot1wSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 2),
    _Dot1wSystemControl_Type()
)
dot1wSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wSystemControl.setStatus("current")
_Dot1wModuleStatus_Type = EnabledStatus
_Dot1wModuleStatus_Object = MibTableColumn
dot1wModuleStatus = _Dot1wModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 3),
    _Dot1wModuleStatus_Type()
)
dot1wModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wModuleStatus.setStatus("current")


class _Dot1wTraceOption_Type(Integer32):
    """Custom type dot1wTraceOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1wTraceOption_Type.__name__ = "Integer32"
_Dot1wTraceOption_Object = MibTableColumn
dot1wTraceOption = _Dot1wTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 4),
    _Dot1wTraceOption_Type()
)
dot1wTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wTraceOption.setStatus("current")


class _Dot1wDebugOption_Type(Integer32):
    """Custom type dot1wDebugOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_Dot1wDebugOption_Type.__name__ = "Integer32"
_Dot1wDebugOption_Object = MibTableColumn
dot1wDebugOption = _Dot1wDebugOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 5),
    _Dot1wDebugOption_Type()
)
dot1wDebugOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wDebugOption.setStatus("current")
_Dot1wRstpUpCount_Type = Counter32
_Dot1wRstpUpCount_Object = MibTableColumn
dot1wRstpUpCount = _Dot1wRstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 6),
    _Dot1wRstpUpCount_Type()
)
dot1wRstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wRstpUpCount.setStatus("current")
_Dot1wRstpDownCount_Type = Counter32
_Dot1wRstpDownCount_Object = MibTableColumn
dot1wRstpDownCount = _Dot1wRstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 7),
    _Dot1wRstpDownCount_Type()
)
dot1wRstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wRstpDownCount.setStatus("current")
_Dot1wBufferFailureCount_Type = Counter32
_Dot1wBufferFailureCount_Object = MibTableColumn
dot1wBufferFailureCount = _Dot1wBufferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 8),
    _Dot1wBufferFailureCount_Type()
)
dot1wBufferFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wBufferFailureCount.setStatus("current")
_Dot1wMemAllocFailureCount_Type = Counter32
_Dot1wMemAllocFailureCount_Object = MibTableColumn
dot1wMemAllocFailureCount = _Dot1wMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 9),
    _Dot1wMemAllocFailureCount_Type()
)
dot1wMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wMemAllocFailureCount.setStatus("current")
_Dot1wNewRootIdCount_Type = Counter32
_Dot1wNewRootIdCount_Object = MibTableColumn
dot1wNewRootIdCount = _Dot1wNewRootIdCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 10),
    _Dot1wNewRootIdCount_Type()
)
dot1wNewRootIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wNewRootIdCount.setStatus("current")


class _Dot1wPortRoleSelSmState_Type(Integer32):
    """Custom type dot1wPortRoleSelSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_Dot1wPortRoleSelSmState_Type.__name__ = "Integer32"
_Dot1wPortRoleSelSmState_Object = MibTableColumn
dot1wPortRoleSelSmState = _Dot1wPortRoleSelSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 11),
    _Dot1wPortRoleSelSmState_Type()
)
dot1wPortRoleSelSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRoleSelSmState.setStatus("current")
_Dot1wOldDesignatedRoot_Type = BridgeId
_Dot1wOldDesignatedRoot_Object = MibTableColumn
dot1wOldDesignatedRoot = _Dot1wOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 12),
    _Dot1wOldDesignatedRoot_Type()
)
dot1wOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wOldDesignatedRoot.setStatus("current")


class _Dot1wDynamicPathcostCalculation_Type(TruthValue):
    """Custom type dot1wDynamicPathcostCalculation based on TruthValue"""


_Dot1wDynamicPathcostCalculation_Object = MibTableColumn
dot1wDynamicPathcostCalculation = _Dot1wDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 13),
    _Dot1wDynamicPathcostCalculation_Type()
)
dot1wDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wDynamicPathcostCalculation.setStatus("current")


class _Dot1wContextName_Type(DisplayString):
    """Custom type dot1wContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot1wContextName_Type.__name__ = "DisplayString"
_Dot1wContextName_Object = MibTableColumn
dot1wContextName = _Dot1wContextName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 3, 1, 14),
    _Dot1wContextName_Type()
)
dot1wContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wContextName.setStatus("current")
_Dot1wPortExtTable_Object = MibTable
dot1wPortExtTable = _Dot1wPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4)
)
if mibBuilder.loadTexts:
    dot1wPortExtTable.setStatus("current")
_Dot1wPortExtEntry_Object = MibTableRow
dot1wPortExtEntry = _Dot1wPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1)
)
dot1wPortExtEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1wPort"),
)
if mibBuilder.loadTexts:
    dot1wPortExtEntry.setStatus("current")


class _Dot1wPort_Type(Integer32):
    """Custom type dot1wPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Dot1wPort_Type.__name__ = "Integer32"
_Dot1wPort_Object = MibTableColumn
dot1wPort = _Dot1wPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 1),
    _Dot1wPort_Type()
)
dot1wPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1wPort.setStatus("current")


class _Dot1wPortRole_Type(Integer32):
    """Custom type dot1wPortRole based on Integer32"""
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
        *(("alternatePort", 1),
          ("backupPort", 2),
          ("designatedPort", 4),
          ("disabledPort", 0),
          ("rootPort", 3))
    )


_Dot1wPortRole_Type.__name__ = "Integer32"
_Dot1wPortRole_Object = MibTableColumn
dot1wPortRole = _Dot1wPortRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 2),
    _Dot1wPortRole_Type()
)
dot1wPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRole.setStatus("current")


class _Dot1wPortOperVersion_Type(Integer32):
    """Custom type dot1wPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_Dot1wPortOperVersion_Type.__name__ = "Integer32"
_Dot1wPortOperVersion_Object = MibTableColumn
dot1wPortOperVersion = _Dot1wPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 3),
    _Dot1wPortOperVersion_Type()
)
dot1wPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortOperVersion.setStatus("current")


class _Dot1wPortInfoSmState_Type(Integer32):
    """Custom type dot1wPortInfoSmState based on Integer32"""
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
        *(("aged", 1),
          ("disabled", 0),
          ("inferiordesignated", 8),
          ("notdesignated", 5),
          ("present", 6),
          ("receive", 7),
          ("repeat", 4),
          ("superior", 3),
          ("update", 2))
    )


_Dot1wPortInfoSmState_Type.__name__ = "Integer32"
_Dot1wPortInfoSmState_Object = MibTableColumn
dot1wPortInfoSmState = _Dot1wPortInfoSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 4),
    _Dot1wPortInfoSmState_Type()
)
dot1wPortInfoSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortInfoSmState.setStatus("current")


class _Dot1wPortMigSmState_Type(Integer32):
    """Custom type dot1wPortMigSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkingrstp", 0),
          ("selectingstp", 1),
          ("sensing", 2))
    )


_Dot1wPortMigSmState_Type.__name__ = "Integer32"
_Dot1wPortMigSmState_Object = MibTableColumn
dot1wPortMigSmState = _Dot1wPortMigSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 5),
    _Dot1wPortMigSmState_Type()
)
dot1wPortMigSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortMigSmState.setStatus("current")


class _Dot1wPortRoleTransSmState_Type(Integer32):
    """Custom type dot1wPortRoleTransSmState based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("backupport", 5),
          ("designatedforward", 15),
          ("designatedlearn", 16),
          ("designatedlisten", 17),
          ("designatedport", 4),
          ("designatedpropose", 12),
          ("designatedretired", 14),
          ("designatedsynced", 13),
          ("disabledport", 2),
          ("disableport", 1),
          ("init", 0),
          ("reroot", 8),
          ("rerooted", 11),
          ("rootagreed", 7),
          ("rootforward", 9),
          ("rootlearn", 10),
          ("rootport", 3),
          ("rootproposed", 6))
    )


_Dot1wPortRoleTransSmState_Type.__name__ = "Integer32"
_Dot1wPortRoleTransSmState_Object = MibTableColumn
dot1wPortRoleTransSmState = _Dot1wPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 6),
    _Dot1wPortRoleTransSmState_Type()
)
dot1wPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRoleTransSmState.setStatus("current")


class _Dot1wPortStateTransSmState_Type(Integer32):
    """Custom type dot1wPortStateTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_Dot1wPortStateTransSmState_Type.__name__ = "Integer32"
_Dot1wPortStateTransSmState_Object = MibTableColumn
dot1wPortStateTransSmState = _Dot1wPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 7),
    _Dot1wPortStateTransSmState_Type()
)
dot1wPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortStateTransSmState.setStatus("current")


class _Dot1wPortTopoChSmState_Type(Integer32):
    """Custom type dot1wPortTopoChSmState based on Integer32"""
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
        *(("acknowledged", 7),
          ("active", 3),
          ("detected", 2),
          ("inactive", 0),
          ("learning", 1),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_Dot1wPortTopoChSmState_Type.__name__ = "Integer32"
_Dot1wPortTopoChSmState_Object = MibTableColumn
dot1wPortTopoChSmState = _Dot1wPortTopoChSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 8),
    _Dot1wPortTopoChSmState_Type()
)
dot1wPortTopoChSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortTopoChSmState.setStatus("current")


class _Dot1wPortTxSmState_Type(Integer32):
    """Custom type dot1wPortTxSmState based on Integer32"""
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
        *(("idle", 5),
          ("transmitconfig", 2),
          ("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitrstp", 4),
          ("transmittcn", 3))
    )


_Dot1wPortTxSmState_Type.__name__ = "Integer32"
_Dot1wPortTxSmState_Object = MibTableColumn
dot1wPortTxSmState = _Dot1wPortTxSmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 9),
    _Dot1wPortTxSmState_Type()
)
dot1wPortTxSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortTxSmState.setStatus("current")
_Dot1wPortRxRstBpduCount_Type = Counter32
_Dot1wPortRxRstBpduCount_Object = MibTableColumn
dot1wPortRxRstBpduCount = _Dot1wPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 10),
    _Dot1wPortRxRstBpduCount_Type()
)
dot1wPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRxRstBpduCount.setStatus("current")
_Dot1wPortRxConfigBpduCount_Type = Counter32
_Dot1wPortRxConfigBpduCount_Object = MibTableColumn
dot1wPortRxConfigBpduCount = _Dot1wPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 11),
    _Dot1wPortRxConfigBpduCount_Type()
)
dot1wPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRxConfigBpduCount.setStatus("current")
_Dot1wPortRxTcnBpduCount_Type = Counter32
_Dot1wPortRxTcnBpduCount_Object = MibTableColumn
dot1wPortRxTcnBpduCount = _Dot1wPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 12),
    _Dot1wPortRxTcnBpduCount_Type()
)
dot1wPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRxTcnBpduCount.setStatus("current")
_Dot1wPortTxRstBpduCount_Type = Counter32
_Dot1wPortTxRstBpduCount_Object = MibTableColumn
dot1wPortTxRstBpduCount = _Dot1wPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 13),
    _Dot1wPortTxRstBpduCount_Type()
)
dot1wPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortTxRstBpduCount.setStatus("current")
_Dot1wPortTxConfigBpduCount_Type = Counter32
_Dot1wPortTxConfigBpduCount_Object = MibTableColumn
dot1wPortTxConfigBpduCount = _Dot1wPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 14),
    _Dot1wPortTxConfigBpduCount_Type()
)
dot1wPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortTxConfigBpduCount.setStatus("current")
_Dot1wPortTxTcnBpduCount_Type = Counter32
_Dot1wPortTxTcnBpduCount_Object = MibTableColumn
dot1wPortTxTcnBpduCount = _Dot1wPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 15),
    _Dot1wPortTxTcnBpduCount_Type()
)
dot1wPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortTxTcnBpduCount.setStatus("current")
_Dot1wPortInvalidRstBpduRxCount_Type = Counter32
_Dot1wPortInvalidRstBpduRxCount_Object = MibTableColumn
dot1wPortInvalidRstBpduRxCount = _Dot1wPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 16),
    _Dot1wPortInvalidRstBpduRxCount_Type()
)
dot1wPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortInvalidRstBpduRxCount.setStatus("current")
_Dot1wPortInvalidConfigBpduRxCount_Type = Counter32
_Dot1wPortInvalidConfigBpduRxCount_Object = MibTableColumn
dot1wPortInvalidConfigBpduRxCount = _Dot1wPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 17),
    _Dot1wPortInvalidConfigBpduRxCount_Type()
)
dot1wPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortInvalidConfigBpduRxCount.setStatus("current")
_Dot1wPortInvalidTcnBpduRxCount_Type = Counter32
_Dot1wPortInvalidTcnBpduRxCount_Object = MibTableColumn
dot1wPortInvalidTcnBpduRxCount = _Dot1wPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 18),
    _Dot1wPortInvalidTcnBpduRxCount_Type()
)
dot1wPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortInvalidTcnBpduRxCount.setStatus("current")
_Dot1wPortProtocolMigrationCount_Type = Counter32
_Dot1wPortProtocolMigrationCount_Object = MibTableColumn
dot1wPortProtocolMigrationCount = _Dot1wPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 19),
    _Dot1wPortProtocolMigrationCount_Type()
)
dot1wPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortProtocolMigrationCount.setStatus("current")
_Dot1wPortEffectivePortState_Type = TruthValue
_Dot1wPortEffectivePortState_Object = MibTableColumn
dot1wPortEffectivePortState = _Dot1wPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 20),
    _Dot1wPortEffectivePortState_Type()
)
dot1wPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortEffectivePortState.setStatus("current")
_Dot1wPortAutoEdge_Type = TruthValue
_Dot1wPortAutoEdge_Object = MibTableColumn
dot1wPortAutoEdge = _Dot1wPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 21),
    _Dot1wPortAutoEdge_Type()
)
dot1wPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wPortAutoEdge.setStatus("current")
_Dot1wPortRestrictedRole_Type = TruthValue
_Dot1wPortRestrictedRole_Object = MibTableColumn
dot1wPortRestrictedRole = _Dot1wPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 22),
    _Dot1wPortRestrictedRole_Type()
)
dot1wPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wPortRestrictedRole.setStatus("current")
_Dot1wPortRestrictedTCN_Type = TruthValue
_Dot1wPortRestrictedTCN_Object = MibTableColumn
dot1wPortRestrictedTCN = _Dot1wPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 1, 4, 1, 23),
    _Dot1wPortRestrictedTCN_Type()
)
dot1wPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wPortRestrictedTCN.setStatus("current")
_Dot1wRstTrapsControl_ObjectIdentity = ObjectIdentity
dot1wRstTrapsControl = _Dot1wRstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2)
)


class _Dot1wSetGlobalTraps_Type(Integer32):
    """Custom type dot1wSetGlobalTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dot1wSetGlobalTraps_Type.__name__ = "Integer32"
_Dot1wSetGlobalTraps_Object = MibScalar
dot1wSetGlobalTraps = _Dot1wSetGlobalTraps_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 1),
    _Dot1wSetGlobalTraps_Type()
)
dot1wSetGlobalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wSetGlobalTraps.setStatus("current")


class _Dot1wGlobalErrTrapType_Type(Integer32):
    """Custom type dot1wGlobalErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufffail", 2),
          ("memfail", 1),
          ("none", 0))
    )


_Dot1wGlobalErrTrapType_Type.__name__ = "Integer32"
_Dot1wGlobalErrTrapType_Object = MibScalar
dot1wGlobalErrTrapType = _Dot1wGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 2),
    _Dot1wGlobalErrTrapType_Type()
)
dot1wGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wGlobalErrTrapType.setStatus("current")
_Dot1wRstTrapsControlTable_Object = MibTable
dot1wRstTrapsControlTable = _Dot1wRstTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 3)
)
if mibBuilder.loadTexts:
    dot1wRstTrapsControlTable.setStatus("current")
_Dot1wRstTrapsControlEntry_Object = MibTableRow
dot1wRstTrapsControlEntry = _Dot1wRstTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 3, 1)
)
dot1wRstTrapsControlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1wRstContextId"),
)
if mibBuilder.loadTexts:
    dot1wRstTrapsControlEntry.setStatus("current")


class _Dot1wSetTraps_Type(Integer32):
    """Custom type dot1wSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot1wSetTraps_Type.__name__ = "Integer32"
_Dot1wSetTraps_Object = MibTableColumn
dot1wSetTraps = _Dot1wSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 3, 1, 1),
    _Dot1wSetTraps_Type()
)
dot1wSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1wSetTraps.setStatus("current")


class _Dot1wGenTrapType_Type(Integer32):
    """Custom type dot1wGenTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("none", 0),
          ("up", 1))
    )


_Dot1wGenTrapType_Type.__name__ = "Integer32"
_Dot1wGenTrapType_Object = MibTableColumn
dot1wGenTrapType = _Dot1wGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 3, 1, 2),
    _Dot1wGenTrapType_Type()
)
dot1wGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wGenTrapType.setStatus("current")
_Dot1wPortTrapNotificationTable_Object = MibTable
dot1wPortTrapNotificationTable = _Dot1wPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4)
)
if mibBuilder.loadTexts:
    dot1wPortTrapNotificationTable.setStatus("current")
_Dot1wPortTrapNotificationEntry_Object = MibTableRow
dot1wPortTrapNotificationEntry = _Dot1wPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1)
)
dot1wPortTrapNotificationEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1wPortTrapIndex"),
)
if mibBuilder.loadTexts:
    dot1wPortTrapNotificationEntry.setStatus("current")


class _Dot1wPortTrapIndex_Type(Integer32):
    """Custom type dot1wPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Dot1wPortTrapIndex_Type.__name__ = "Integer32"
_Dot1wPortTrapIndex_Object = MibTableColumn
dot1wPortTrapIndex = _Dot1wPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1, 1),
    _Dot1wPortTrapIndex_Type()
)
dot1wPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1wPortTrapIndex.setStatus("current")


class _Dot1wPortMigrationType_Type(Integer32):
    """Custom type dot1wPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendrstp", 1),
          ("sendstp", 0))
    )


_Dot1wPortMigrationType_Type.__name__ = "Integer32"
_Dot1wPortMigrationType_Object = MibTableColumn
dot1wPortMigrationType = _Dot1wPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1, 2),
    _Dot1wPortMigrationType_Type()
)
dot1wPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortMigrationType.setStatus("current")


class _Dot1wPktErrType_Type(Integer32):
    """Custom type dot1wPktErrType based on Integer32"""
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
        *(("configLengthErr", 2),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("invalidBpdu", 1),
          ("maxAgeErr", 5),
          ("protocolIdErr", 0),
          ("rstpLengthErr", 4),
          ("tcnLengthErr", 3))
    )


_Dot1wPktErrType_Type.__name__ = "Integer32"
_Dot1wPktErrType_Object = MibTableColumn
dot1wPktErrType = _Dot1wPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1, 3),
    _Dot1wPktErrType_Type()
)
dot1wPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPktErrType.setStatus("current")
_Dot1wPktErrVal_Type = Integer32
_Dot1wPktErrVal_Object = MibTableColumn
dot1wPktErrVal = _Dot1wPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1, 4),
    _Dot1wPktErrVal_Type()
)
dot1wPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPktErrVal.setStatus("current")


class _Dot1wPortRoleType_Type(Integer32):
    """Custom type dot1wPortRoleType based on Integer32"""
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
        *(("alternatePort", 1),
          ("backupPort", 2),
          ("designatedPort", 4),
          ("disabledPort", 0),
          ("rootPort", 3))
    )


_Dot1wPortRoleType_Type.__name__ = "Integer32"
_Dot1wPortRoleType_Object = MibTableColumn
dot1wPortRoleType = _Dot1wPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1, 5),
    _Dot1wPortRoleType_Type()
)
dot1wPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wPortRoleType.setStatus("current")


class _Dot1wOldRoleType_Type(Integer32):
    """Custom type dot1wOldRoleType based on Integer32"""
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
        *(("alternatePort", 1),
          ("backupPort", 2),
          ("designatedPort", 4),
          ("disabledPort", 0),
          ("rootPort", 3))
    )


_Dot1wOldRoleType_Type.__name__ = "Integer32"
_Dot1wOldRoleType_Object = MibTableColumn
dot1wOldRoleType = _Dot1wOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 2, 4, 1, 6),
    _Dot1wOldRoleType_Type()
)
dot1wOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1wOldRoleType.setStatus("current")
_Dot1wRstTraps_ObjectIdentity = ObjectIdentity
dot1wRstTraps = _Dot1wRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3)
)
_Dot1wTraps_ObjectIdentity = ObjectIdentity
dot1wTraps = _Dot1wTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0)
)
_L2Vlan_ObjectIdentity = ObjectIdentity
l2Vlan = _L2Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120)
)
_L2Dot1qVlan_ObjectIdentity = ObjectIdentity
l2Dot1qVlan = _L2Dot1qVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1)
)
_Dot1qVlanGlobalTrace_Type = TruthValue
_Dot1qVlanGlobalTrace_Object = MibScalar
dot1qVlanGlobalTrace = _Dot1qVlanGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 1),
    _Dot1qVlanGlobalTrace_Type()
)
dot1qVlanGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanGlobalTrace.setStatus("current")
_Dot1qVlanGlobalsTable_Object = MibTable
dot1qVlanGlobalsTable = _Dot1qVlanGlobalsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2)
)
if mibBuilder.loadTexts:
    dot1qVlanGlobalsTable.setStatus("current")
_Dot1qVlanGlobalsEntry_Object = MibTableRow
dot1qVlanGlobalsEntry = _Dot1qVlanGlobalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1)
)
dot1qVlanGlobalsEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dot1qVlanGlobalsContextId"),
)
if mibBuilder.loadTexts:
    dot1qVlanGlobalsEntry.setStatus("current")


class _Dot1qVlanGlobalsContextId_Type(Integer32):
    """Custom type dot1qVlanGlobalsContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qVlanGlobalsContextId_Type.__name__ = "Integer32"
_Dot1qVlanGlobalsContextId_Object = MibTableColumn
dot1qVlanGlobalsContextId = _Dot1qVlanGlobalsContextId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1, 1),
    _Dot1qVlanGlobalsContextId_Type()
)
dot1qVlanGlobalsContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanGlobalsContextId.setStatus("current")


class _Dot1qGarpShutdownStatus_Type(TruthValue):
    """Custom type dot1qGarpShutdownStatus based on TruthValue"""


_Dot1qGarpShutdownStatus_Object = MibTableColumn
dot1qGarpShutdownStatus = _Dot1qGarpShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1, 6),
    _Dot1qGarpShutdownStatus_Type()
)
dot1qGarpShutdownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qGarpShutdownStatus.setStatus("current")


class _Dot1qVlanDebug_Type(Integer32):
    """Custom type dot1qVlanDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_Dot1qVlanDebug_Type.__name__ = "Integer32"
_Dot1qVlanDebug_Object = MibTableColumn
dot1qVlanDebug = _Dot1qVlanDebug_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1, 7),
    _Dot1qVlanDebug_Type()
)
dot1qVlanDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanDebug.setStatus("current")


class _Dot1qVlanLearningMode_Type(Integer32):
    """Custom type dot1qVlanLearningMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2))
    )


_Dot1qVlanLearningMode_Type.__name__ = "Integer32"
_Dot1qVlanLearningMode_Object = MibTableColumn
dot1qVlanLearningMode = _Dot1qVlanLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1, 8),
    _Dot1qVlanLearningMode_Type()
)
dot1qVlanLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanLearningMode.setStatus("current")
_Dot1qVlanOperStatus_Type = EnabledStatus
_Dot1qVlanOperStatus_Object = MibTableColumn
dot1qVlanOperStatus = _Dot1qVlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1, 10),
    _Dot1qVlanOperStatus_Type()
)
dot1qVlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanOperStatus.setStatus("current")
_Dot1qGvrpOperStatus_Type = EnabledStatus
_Dot1qGvrpOperStatus_Object = MibTableColumn
dot1qGvrpOperStatus = _Dot1qGvrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 1, 2, 1, 11),
    _Dot1qGvrpOperStatus_Type()
)
dot1qGvrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qGvrpOperStatus.setStatus("current")
_PortBaseVlan_ObjectIdentity = ObjectIdentity
portBaseVlan = _PortBaseVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3)
)
_PortBaseVlanEnablePerPort_Type = PortList
_PortBaseVlanEnablePerPort_Object = MibScalar
portBaseVlanEnablePerPort = _PortBaseVlanEnablePerPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 1),
    _PortBaseVlanEnablePerPort_Type()
)
portBaseVlanEnablePerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseVlanEnablePerPort.setStatus("current")
_PortBaseVlanCurrentTable_Object = MibTable
portBaseVlanCurrentTable = _PortBaseVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2)
)
if mibBuilder.loadTexts:
    portBaseVlanCurrentTable.setStatus("current")
_TabPortBaseVlanCurrentEntry_Object = MibTableRow
tabPortBaseVlanCurrentEntry = _TabPortBaseVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1)
)
tabPortBaseVlanCurrentEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "portBaseVlanIndex"),
)
if mibBuilder.loadTexts:
    tabPortBaseVlanCurrentEntry.setStatus("current")


class _PortBaseVlanIndex_Type(Integer32):
    """Custom type portBaseVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortBaseVlanIndex_Type.__name__ = "Integer32"
_PortBaseVlanIndex_Object = MibTableColumn
portBaseVlanIndex = _PortBaseVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1, 1),
    _PortBaseVlanIndex_Type()
)
portBaseVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseVlanIndex.setStatus("current")
_PortBaseVlanName_Type = OctetString
_PortBaseVlanName_Object = MibTableColumn
portBaseVlanName = _PortBaseVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1, 2),
    _PortBaseVlanName_Type()
)
portBaseVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseVlanName.setStatus("current")
_PortBaseVlanCurrentEgressPorts_Type = PortList
_PortBaseVlanCurrentEgressPorts_Object = MibTableColumn
portBaseVlanCurrentEgressPorts = _PortBaseVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1, 3),
    _PortBaseVlanCurrentEgressPorts_Type()
)
portBaseVlanCurrentEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseVlanCurrentEgressPorts.setStatus("current")


class _PortBaseVlanStatus_Type(Integer32):
    """Custom type portBaseVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_PortBaseVlanStatus_Type.__name__ = "Integer32"
_PortBaseVlanStatus_Object = MibTableColumn
portBaseVlanStatus = _PortBaseVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1, 4),
    _PortBaseVlanStatus_Type()
)
portBaseVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseVlanStatus.setStatus("current")
_PortBaseVlanCreationTime_Type = TimeTicks
_PortBaseVlanCreationTime_Object = MibTableColumn
portBaseVlanCreationTime = _PortBaseVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1, 5),
    _PortBaseVlanCreationTime_Type()
)
portBaseVlanCreationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseVlanCreationTime.setStatus("current")
_PortBaseVlanRowStatus_Type = RowStatus
_PortBaseVlanRowStatus_Object = MibTableColumn
portBaseVlanRowStatus = _PortBaseVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 3, 2, 1, 6),
    _PortBaseVlanRowStatus_Type()
)
portBaseVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portBaseVlanRowStatus.setStatus("current")
_PortBaseStatic_ObjectIdentity = ObjectIdentity
portBaseStatic = _PortBaseStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4)
)
_PortBaseStaticUnicastTable_Object = MibTable
portBaseStaticUnicastTable = _PortBaseStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1)
)
if mibBuilder.loadTexts:
    portBaseStaticUnicastTable.setStatus("current")
_TabPortBaseStaticUnicastEntry_Object = MibTableRow
tabPortBaseStaticUnicastEntry = _TabPortBaseStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1)
)
tabPortBaseStaticUnicastEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "portBaseStaticUnicastIndex"),
)
if mibBuilder.loadTexts:
    tabPortBaseStaticUnicastEntry.setStatus("current")


class _PortBaseStaticUnicastIndex_Type(Integer32):
    """Custom type portBaseStaticUnicastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortBaseStaticUnicastIndex_Type.__name__ = "Integer32"
_PortBaseStaticUnicastIndex_Object = MibTableColumn
portBaseStaticUnicastIndex = _PortBaseStaticUnicastIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1, 1),
    _PortBaseStaticUnicastIndex_Type()
)
portBaseStaticUnicastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseStaticUnicastIndex.setStatus("current")
_PortBaseStaticUnicastVlanIndex_Type = Integer32
_PortBaseStaticUnicastVlanIndex_Object = MibTableColumn
portBaseStaticUnicastVlanIndex = _PortBaseStaticUnicastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1, 2),
    _PortBaseStaticUnicastVlanIndex_Type()
)
portBaseStaticUnicastVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticUnicastVlanIndex.setStatus("current")
_PortBaseStaticUnicastAddress_Type = MacAddress
_PortBaseStaticUnicastAddress_Object = MibTableColumn
portBaseStaticUnicastAddress = _PortBaseStaticUnicastAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1, 3),
    _PortBaseStaticUnicastAddress_Type()
)
portBaseStaticUnicastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticUnicastAddress.setStatus("current")
_PortBaseStaticUnicastAllowedToGoTo_Type = PortList
_PortBaseStaticUnicastAllowedToGoTo_Object = MibTableColumn
portBaseStaticUnicastAllowedToGoTo = _PortBaseStaticUnicastAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1, 4),
    _PortBaseStaticUnicastAllowedToGoTo_Type()
)
portBaseStaticUnicastAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticUnicastAllowedToGoTo.setStatus("current")


class _PortBaseStaticUnicastStatus_Type(Integer32):
    """Custom type portBaseStaticUnicastStatus based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_PortBaseStaticUnicastStatus_Type.__name__ = "Integer32"
_PortBaseStaticUnicastStatus_Object = MibTableColumn
portBaseStaticUnicastStatus = _PortBaseStaticUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1, 5),
    _PortBaseStaticUnicastStatus_Type()
)
portBaseStaticUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticUnicastStatus.setStatus("current")
_PortBaseStaticUnicastRowStatus_Type = RowStatus
_PortBaseStaticUnicastRowStatus_Object = MibTableColumn
portBaseStaticUnicastRowStatus = _PortBaseStaticUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 1, 1, 6),
    _PortBaseStaticUnicastRowStatus_Type()
)
portBaseStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portBaseStaticUnicastRowStatus.setStatus("current")
_PortBaseStaticMulticastTable_Object = MibTable
portBaseStaticMulticastTable = _PortBaseStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2)
)
if mibBuilder.loadTexts:
    portBaseStaticMulticastTable.setStatus("current")
_TabPortBaseStaticMulticastEntry_Object = MibTableRow
tabPortBaseStaticMulticastEntry = _TabPortBaseStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1)
)
tabPortBaseStaticMulticastEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "portBaseStaticMulticastIndex"),
)
if mibBuilder.loadTexts:
    tabPortBaseStaticMulticastEntry.setStatus("current")


class _PortBaseStaticMulticastIndex_Type(Integer32):
    """Custom type portBaseStaticMulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortBaseStaticMulticastIndex_Type.__name__ = "Integer32"
_PortBaseStaticMulticastIndex_Object = MibTableColumn
portBaseStaticMulticastIndex = _PortBaseStaticMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1, 1),
    _PortBaseStaticMulticastIndex_Type()
)
portBaseStaticMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseStaticMulticastIndex.setStatus("current")
_PortBaseStaticMulticastVlanIndex_Type = Integer32
_PortBaseStaticMulticastVlanIndex_Object = MibTableColumn
portBaseStaticMulticastVlanIndex = _PortBaseStaticMulticastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1, 2),
    _PortBaseStaticMulticastVlanIndex_Type()
)
portBaseStaticMulticastVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticMulticastVlanIndex.setStatus("current")
_PortBaseStaticMulticastAddress_Type = MacAddress
_PortBaseStaticMulticastAddress_Object = MibTableColumn
portBaseStaticMulticastAddress = _PortBaseStaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1, 3),
    _PortBaseStaticMulticastAddress_Type()
)
portBaseStaticMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticMulticastAddress.setStatus("current")
_PortBaseStaticMulticastStaticEgressPorts_Type = PortList
_PortBaseStaticMulticastStaticEgressPorts_Object = MibTableColumn
portBaseStaticMulticastStaticEgressPorts = _PortBaseStaticMulticastStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1, 4),
    _PortBaseStaticMulticastStaticEgressPorts_Type()
)
portBaseStaticMulticastStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticMulticastStaticEgressPorts.setStatus("current")


class _PortBaseStaticMulticastStatus_Type(Integer32):
    """Custom type portBaseStaticMulticastStatus based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_PortBaseStaticMulticastStatus_Type.__name__ = "Integer32"
_PortBaseStaticMulticastStatus_Object = MibTableColumn
portBaseStaticMulticastStatus = _PortBaseStaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1, 5),
    _PortBaseStaticMulticastStatus_Type()
)
portBaseStaticMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseStaticMulticastStatus.setStatus("current")
_PortBaseStaticMulticastRowStatus_Type = RowStatus
_PortBaseStaticMulticastRowStatus_Object = MibTableColumn
portBaseStaticMulticastRowStatus = _PortBaseStaticMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 120, 4, 2, 1, 6),
    _PortBaseStaticMulticastRowStatus_Type()
)
portBaseStaticMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portBaseStaticMulticastRowStatus.setStatus("current")
_Fslldp_ObjectIdentity = ObjectIdentity
fslldp = _Fslldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158)
)
_FsLldpSystem_ObjectIdentity = ObjectIdentity
fsLldpSystem = _FsLldpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 1)
)


class _FsLldpSystemControl_Type(Integer32):
    """Custom type fsLldpSystemControl based on Integer32"""
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
        *(("shutdown", 3),
          ("shutdownInProgress", 2),
          ("start", 1))
    )


_FsLldpSystemControl_Type.__name__ = "Integer32"
_FsLldpSystemControl_Object = MibScalar
fsLldpSystemControl = _FsLldpSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 1, 1),
    _FsLldpSystemControl_Type()
)
fsLldpSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpSystemControl.setStatus("current")


class _FsLldpModuleStatus_Type(Integer32):
    """Custom type fsLldpModuleStatus based on Integer32"""
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


_FsLldpModuleStatus_Type.__name__ = "Integer32"
_FsLldpModuleStatus_Object = MibScalar
fsLldpModuleStatus = _FsLldpModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 1, 2),
    _FsLldpModuleStatus_Type()
)
fsLldpModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpModuleStatus.setStatus("current")


class _FsLldpTraceInput_Type(OctetString):
    """Custom type fsLldpTraceInput based on OctetString"""
    defaultValue = OctetString("critical")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 280),
    )


_FsLldpTraceInput_Type.__name__ = "OctetString"
_FsLldpTraceInput_Object = MibScalar
fsLldpTraceInput = _FsLldpTraceInput_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 1, 3),
    _FsLldpTraceInput_Type()
)
fsLldpTraceInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpTraceInput.setStatus("current")


class _FsLldpTraceOption_Type(Integer32):
    """Custom type fsLldpTraceOption based on Integer32"""
    defaultHexValue = 8192


_FsLldpTraceOption_Object = MibScalar
fsLldpTraceOption = _FsLldpTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 1, 4),
    _FsLldpTraceOption_Type()
)
fsLldpTraceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpTraceOption.setStatus("current")
_FsLldpTLV_ObjectIdentity = ObjectIdentity
fsLldpTLV = _FsLldpTLV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2)
)


class _FsLldpLocChassisIdSubtype_Type(Integer32):
    """Custom type fsLldpLocChassisIdSubtype based on Integer32"""
    defaultValue = 4

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
        *(("chassiscomp", 1),
          ("ifalias", 2),
          ("ifname", 6),
          ("local", 7),
          ("macaddr", 4),
          ("nwaddr", 5),
          ("portcomp", 3))
    )


_FsLldpLocChassisIdSubtype_Type.__name__ = "Integer32"
_FsLldpLocChassisIdSubtype_Object = MibScalar
fsLldpLocChassisIdSubtype = _FsLldpLocChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 1),
    _FsLldpLocChassisIdSubtype_Type()
)
fsLldpLocChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpLocChassisIdSubtype.setStatus("current")


class _FsLldpLocChassisId_Type(OctetString):
    """Custom type fsLldpLocChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsLldpLocChassisId_Type.__name__ = "OctetString"
_FsLldpLocChassisId_Object = MibScalar
fsLldpLocChassisId = _FsLldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 2),
    _FsLldpLocChassisId_Type()
)
fsLldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpLocChassisId.setStatus("current")
_FsLldpLocPortTable_Object = MibTable
fsLldpLocPortTable = _FsLldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 3)
)
if mibBuilder.loadTexts:
    fsLldpLocPortTable.setStatus("current")
_FsLldpLocPortEntry_Object = MibTableRow
fsLldpLocPortEntry = _FsLldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 3, 1)
)
fsLldpLocPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    fsLldpLocPortEntry.setStatus("current")


class _FsLldpLocPortIdSubtype_Type(Integer32):
    """Custom type fsLldpLocPortIdSubtype based on Integer32"""
    defaultValue = 1

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
        *(("agentcircuitid", 6),
          ("ifalias", 1),
          ("ifname", 5),
          ("local", 7),
          ("macaddr", 3),
          ("nwaddr", 4),
          ("portcomp", 2))
    )


_FsLldpLocPortIdSubtype_Type.__name__ = "Integer32"
_FsLldpLocPortIdSubtype_Object = MibTableColumn
fsLldpLocPortIdSubtype = _FsLldpLocPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 3, 1, 1),
    _FsLldpLocPortIdSubtype_Type()
)
fsLldpLocPortIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocPortIdSubtype.setStatus("current")


class _FsLldpLocPortId_Type(OctetString):
    """Custom type fsLldpLocPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsLldpLocPortId_Type.__name__ = "OctetString"
_FsLldpLocPortId_Object = MibTableColumn
fsLldpLocPortId = _FsLldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 3, 1, 2),
    _FsLldpLocPortId_Type()
)
fsLldpLocPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocPortId.setStatus("current")


class _FsLldpPortConfigNotificationType_Type(Integer32):
    """Custom type fsLldpPortConfigNotificationType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("misCfg", 2),
          ("remTabChg", 1),
          ("remTabChgAndMisCfg", 3))
    )


_FsLldpPortConfigNotificationType_Type.__name__ = "Integer32"
_FsLldpPortConfigNotificationType_Object = MibTableColumn
fsLldpPortConfigNotificationType = _FsLldpPortConfigNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 2, 3, 1, 3),
    _FsLldpPortConfigNotificationType_Type()
)
fsLldpPortConfigNotificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpPortConfigNotificationType.setStatus("current")
_FsLldpStatistics_ObjectIdentity = ObjectIdentity
fsLldpStatistics = _FsLldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 3)
)
_FsLldpMemAllocFailure_Type = Integer32
_FsLldpMemAllocFailure_Object = MibScalar
fsLldpMemAllocFailure = _FsLldpMemAllocFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 3, 1),
    _FsLldpMemAllocFailure_Type()
)
fsLldpMemAllocFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMemAllocFailure.setStatus("current")
_FsLldpInputQOverFlows_Type = Integer32
_FsLldpInputQOverFlows_Object = MibScalar
fsLldpInputQOverFlows = _FsLldpInputQOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 3, 2),
    _FsLldpInputQOverFlows_Type()
)
fsLldpInputQOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpInputQOverFlows.setStatus("current")
_FsLldpStatsRemTablesUpdates_Type = ZeroBasedCounter32
_FsLldpStatsRemTablesUpdates_Object = MibScalar
fsLldpStatsRemTablesUpdates = _FsLldpStatsRemTablesUpdates_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 3, 3),
    _FsLldpStatsRemTablesUpdates_Type()
)
fsLldpStatsRemTablesUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpStatsRemTablesUpdates.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpStatsRemTablesUpdates.setUnits("table entries")
_FsLldpNotification_ObjectIdentity = ObjectIdentity
fsLldpNotification = _FsLldpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4)
)
_FsLldpTraps_ObjectIdentity = ObjectIdentity
fsLldpTraps = _FsLldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0)
)
_L2VoiceVlan_ObjectIdentity = ObjectIdentity
l2VoiceVlan = _L2VoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163)
)
_VoicevlanSystem_ObjectIdentity = ObjectIdentity
voicevlanSystem = _VoicevlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1)
)


class _VoiceVlanMode_Type(Integer32):
    """Custom type voiceVlanMode based on Integer32"""
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


_VoiceVlanMode_Type.__name__ = "Integer32"
_VoiceVlanMode_Object = MibScalar
voiceVlanMode = _VoiceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 2),
    _VoiceVlanMode_Type()
)
voiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanMode.setStatus("current")
_VoiceVlanId_Type = Integer32
_VoiceVlanId_Object = MibScalar
voiceVlanId = _VoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 3),
    _VoiceVlanId_Type()
)
voiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanId.setStatus("current")
_VoiceVlanTimeout_Type = Integer32
_VoiceVlanTimeout_Object = MibScalar
voiceVlanTimeout = _VoiceVlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 4),
    _VoiceVlanTimeout_Type()
)
voiceVlanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanTimeout.setStatus("current")


class _VoiceVlanPriority_Type(Integer32):
    """Custom type voiceVlanPriority based on Integer32"""
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
        *(("high", 1),
          ("highest", 0),
          ("low", 3),
          ("medium", 2))
    )


_VoiceVlanPriority_Type.__name__ = "Integer32"
_VoiceVlanPriority_Object = MibScalar
voiceVlanPriority = _VoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 5),
    _VoiceVlanPriority_Type()
)
voiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPriority.setStatus("current")
_VoicevlanPortControlTable_Object = MibTable
voicevlanPortControlTable = _VoicevlanPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 6)
)
if mibBuilder.loadTexts:
    voicevlanPortControlTable.setStatus("current")
_VoicevlanPortControlEntry_Object = MibTableRow
voicevlanPortControlEntry = _VoicevlanPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 6, 1)
)
voicevlanPortControlEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "voicevlanPortControlIndex"),
)
if mibBuilder.loadTexts:
    voicevlanPortControlEntry.setStatus("current")
_VoicevlanPortControlIndex_Type = InterfaceIndex
_VoicevlanPortControlIndex_Object = MibTableColumn
voicevlanPortControlIndex = _VoicevlanPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 6, 1, 1),
    _VoicevlanPortControlIndex_Type()
)
voicevlanPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortControlIndex.setStatus("current")


class _VoicevlanPortAutoDetection_Type(Integer32):
    """Custom type voicevlanPortAutoDetection based on Integer32"""
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


_VoicevlanPortAutoDetection_Type.__name__ = "Integer32"
_VoicevlanPortAutoDetection_Object = MibTableColumn
voicevlanPortAutoDetection = _VoicevlanPortAutoDetection_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 6, 1, 2),
    _VoicevlanPortAutoDetection_Type()
)
voicevlanPortAutoDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanPortAutoDetection.setStatus("current")


class _VoicevlanPortState_Type(Integer32):
    """Custom type voicevlanPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 1),
          ("none", 3))
    )


_VoicevlanPortState_Type.__name__ = "Integer32"
_VoicevlanPortState_Object = MibTableColumn
voicevlanPortState = _VoicevlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 1, 6, 1, 3),
    _VoicevlanPortState_Type()
)
voicevlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortState.setStatus("current")
_VoicevlanOUI_ObjectIdentity = ObjectIdentity
voicevlanOUI = _VoicevlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2)
)
_VoicevlanOUITable_Object = MibTable
voicevlanOUITable = _VoicevlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2, 1)
)
if mibBuilder.loadTexts:
    voicevlanOUITable.setStatus("current")
_VoicevlanOUIEntry_Object = MibTableRow
voicevlanOUIEntry = _VoicevlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2, 1, 1)
)
voicevlanOUIEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "voicevlanOUITelephonyOUI"),
)
if mibBuilder.loadTexts:
    voicevlanOUIEntry.setStatus("current")
_VoicevlanOUITelephonyOUI_Type = MacAddress
_VoicevlanOUITelephonyOUI_Object = MibTableColumn
voicevlanOUITelephonyOUI = _VoicevlanOUITelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2, 1, 1, 1),
    _VoicevlanOUITelephonyOUI_Type()
)
voicevlanOUITelephonyOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUITelephonyOUI.setStatus("current")
_VoicevlanOUIDescription_Type = OctetString
_VoicevlanOUIDescription_Object = MibTableColumn
voicevlanOUIDescription = _VoicevlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2, 1, 1, 2),
    _VoicevlanOUIDescription_Type()
)
voicevlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIDescription.setStatus("current")
_VoicevlanOUIMask_Type = MacAddress
_VoicevlanOUIMask_Object = MibTableColumn
voicevlanOUIMask = _VoicevlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2, 1, 1, 3),
    _VoicevlanOUIMask_Type()
)
voicevlanOUIMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUIMask.setStatus("current")
_VoicevlanOUIStatus_Type = RowStatus
_VoicevlanOUIStatus_Object = MibTableColumn
voicevlanOUIStatus = _VoicevlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 163, 2, 1, 1, 4),
    _VoicevlanOUIStatus_Type()
)
voicevlanOUIStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voicevlanOUIStatus.setStatus("current")
_TrafficSeg_ObjectIdentity = ObjectIdentity
trafficSeg = _TrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 165)
)
_TrafficSegTable_Object = MibTable
trafficSegTable = _TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 165, 1)
)
if mibBuilder.loadTexts:
    trafficSegTable.setStatus("current")
_TrafficSegEntry_Object = MibTableRow
trafficSegEntry = _TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 165, 1, 1)
)
trafficSegEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "trafficSegIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegEntry.setStatus("current")
_TrafficSegIfIndex_Type = InterfaceIndex
_TrafficSegIfIndex_Object = MibTableColumn
trafficSegIfIndex = _TrafficSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 165, 1, 1, 1),
    _TrafficSegIfIndex_Type()
)
trafficSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegIfIndex.setStatus("current")
_TrafficSegMemberList_Type = PortList
_TrafficSegMemberList_Object = MibTableColumn
trafficSegMemberList = _TrafficSegMemberList_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 165, 1, 1, 2),
    _TrafficSegMemberList_Type()
)
trafficSegMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegMemberList.setStatus("current")
_AtiAclMib_ObjectIdentity = ObjectIdentity
atiAclMib = _AtiAclMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166)
)
_AtiAcl_ObjectIdentity = ObjectIdentity
atiAcl = _AtiAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1)
)
_AtiAclClassifierTable_Object = MibTable
atiAclClassifierTable = _AtiAclClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1)
)
if mibBuilder.loadTexts:
    atiAclClassifierTable.setStatus("current")
_AtiAclClassifierEntry_Object = MibTableRow
atiAclClassifierEntry = _AtiAclClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1)
)
atiAclClassifierEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiAclClassifierIndex"),
)
if mibBuilder.loadTexts:
    atiAclClassifierEntry.setStatus("current")


class _AtiAclClassifierIndex_Type(Integer32):
    """Custom type atiAclClassifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclClassifierIndex_Type.__name__ = "Integer32"
_AtiAclClassifierIndex_Object = MibTableColumn
atiAclClassifierIndex = _AtiAclClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 1),
    _AtiAclClassifierIndex_Type()
)
atiAclClassifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiAclClassifierIndex.setStatus("current")
_AtiAclClassifierSrcMac_Type = MacAddress
_AtiAclClassifierSrcMac_Object = MibTableColumn
atiAclClassifierSrcMac = _AtiAclClassifierSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 2),
    _AtiAclClassifierSrcMac_Type()
)
atiAclClassifierSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierSrcMac.setStatus("current")


class _AtiAclClassifierSrcMacMaskLen_Type(Integer32):
    """Custom type atiAclClassifierSrcMacMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AtiAclClassifierSrcMacMaskLen_Type.__name__ = "Integer32"
_AtiAclClassifierSrcMacMaskLen_Object = MibTableColumn
atiAclClassifierSrcMacMaskLen = _AtiAclClassifierSrcMacMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 3),
    _AtiAclClassifierSrcMacMaskLen_Type()
)
atiAclClassifierSrcMacMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierSrcMacMaskLen.setStatus("current")
_AtiAclClassifierDstMac_Type = MacAddress
_AtiAclClassifierDstMac_Object = MibTableColumn
atiAclClassifierDstMac = _AtiAclClassifierDstMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 4),
    _AtiAclClassifierDstMac_Type()
)
atiAclClassifierDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierDstMac.setStatus("current")


class _AtiAclClassifierDstMacMaskLen_Type(Integer32):
    """Custom type atiAclClassifierDstMacMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AtiAclClassifierDstMacMaskLen_Type.__name__ = "Integer32"
_AtiAclClassifierDstMacMaskLen_Object = MibTableColumn
atiAclClassifierDstMacMaskLen = _AtiAclClassifierDstMacMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 5),
    _AtiAclClassifierDstMacMaskLen_Type()
)
atiAclClassifierDstMacMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierDstMacMaskLen.setStatus("current")


class _AtiAclClassifierVlanId_Type(Integer32):
    """Custom type atiAclClassifierVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4000),
    )


_AtiAclClassifierVlanId_Type.__name__ = "Integer32"
_AtiAclClassifierVlanId_Object = MibTableColumn
atiAclClassifierVlanId = _AtiAclClassifierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 6),
    _AtiAclClassifierVlanId_Type()
)
atiAclClassifierVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierVlanId.setStatus("current")


class _AtiAclClassifierCos_Type(Integer32):
    """Custom type atiAclClassifierCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AtiAclClassifierCos_Type.__name__ = "Integer32"
_AtiAclClassifierCos_Object = MibTableColumn
atiAclClassifierCos = _AtiAclClassifierCos_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 7),
    _AtiAclClassifierCos_Type()
)
atiAclClassifierCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierCos.setStatus("current")


class _AtiAclClassifierEtherType_Type(Integer32):
    """Custom type atiAclClassifierEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AtiAclClassifierEtherType_Type.__name__ = "Integer32"
_AtiAclClassifierEtherType_Object = MibTableColumn
atiAclClassifierEtherType = _AtiAclClassifierEtherType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 8),
    _AtiAclClassifierEtherType_Type()
)
atiAclClassifierEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierEtherType.setStatus("current")
_AtiAclClassifierSrcIp_Type = IpAddress
_AtiAclClassifierSrcIp_Object = MibTableColumn
atiAclClassifierSrcIp = _AtiAclClassifierSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 10),
    _AtiAclClassifierSrcIp_Type()
)
atiAclClassifierSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierSrcIp.setStatus("current")


class _AtiAclClassifierSrcIpMaskLen_Type(Integer32):
    """Custom type atiAclClassifierSrcIpMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtiAclClassifierSrcIpMaskLen_Type.__name__ = "Integer32"
_AtiAclClassifierSrcIpMaskLen_Object = MibTableColumn
atiAclClassifierSrcIpMaskLen = _AtiAclClassifierSrcIpMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 11),
    _AtiAclClassifierSrcIpMaskLen_Type()
)
atiAclClassifierSrcIpMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierSrcIpMaskLen.setStatus("current")
_AtiAclClassifierDstIp_Type = IpAddress
_AtiAclClassifierDstIp_Object = MibTableColumn
atiAclClassifierDstIp = _AtiAclClassifierDstIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 12),
    _AtiAclClassifierDstIp_Type()
)
atiAclClassifierDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierDstIp.setStatus("current")


class _AtiAclClassifierDstIpMaskLen_Type(Integer32):
    """Custom type atiAclClassifierDstIpMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtiAclClassifierDstIpMaskLen_Type.__name__ = "Integer32"
_AtiAclClassifierDstIpMaskLen_Object = MibTableColumn
atiAclClassifierDstIpMaskLen = _AtiAclClassifierDstIpMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 13),
    _AtiAclClassifierDstIpMaskLen_Type()
)
atiAclClassifierDstIpMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierDstIpMaskLen.setStatus("current")


class _AtiAclClassifierDscp_Type(Integer32):
    """Custom type atiAclClassifierDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AtiAclClassifierDscp_Type.__name__ = "Integer32"
_AtiAclClassifierDscp_Object = MibTableColumn
atiAclClassifierDscp = _AtiAclClassifierDscp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 14),
    _AtiAclClassifierDscp_Type()
)
atiAclClassifierDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierDscp.setStatus("current")


class _AtiAclClassifierProtocol_Type(Integer32):
    """Custom type atiAclClassifierProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AtiAclClassifierProtocol_Type.__name__ = "Integer32"
_AtiAclClassifierProtocol_Object = MibTableColumn
atiAclClassifierProtocol = _AtiAclClassifierProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 15),
    _AtiAclClassifierProtocol_Type()
)
atiAclClassifierProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierProtocol.setStatus("current")


class _AtiAclClassifierSrcPort_Type(Integer32):
    """Custom type atiAclClassifierSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AtiAclClassifierSrcPort_Type.__name__ = "Integer32"
_AtiAclClassifierSrcPort_Object = MibTableColumn
atiAclClassifierSrcPort = _AtiAclClassifierSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 20),
    _AtiAclClassifierSrcPort_Type()
)
atiAclClassifierSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierSrcPort.setStatus("current")


class _AtiAclClassifierDstPort_Type(Integer32):
    """Custom type atiAclClassifierDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AtiAclClassifierDstPort_Type.__name__ = "Integer32"
_AtiAclClassifierDstPort_Object = MibTableColumn
atiAclClassifierDstPort = _AtiAclClassifierDstPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 21),
    _AtiAclClassifierDstPort_Type()
)
atiAclClassifierDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclClassifierDstPort.setStatus("current")
_AtiAclClassifierRowStatus_Type = RowStatus
_AtiAclClassifierRowStatus_Object = MibTableColumn
atiAclClassifierRowStatus = _AtiAclClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 1, 1, 30),
    _AtiAclClassifierRowStatus_Type()
)
atiAclClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiAclClassifierRowStatus.setStatus("current")
_AtiAclProfileActionTable_Object = MibTable
atiAclProfileActionTable = _AtiAclProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 2)
)
if mibBuilder.loadTexts:
    atiAclProfileActionTable.setStatus("current")
_AtiAclProfileActionEntry_Object = MibTableRow
atiAclProfileActionEntry = _AtiAclProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 2, 1)
)
atiAclProfileActionEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiAclProfileActionIndex"),
)
if mibBuilder.loadTexts:
    atiAclProfileActionEntry.setStatus("current")


class _AtiAclProfileActionIndex_Type(Integer32):
    """Custom type atiAclProfileActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_AtiAclProfileActionIndex_Type.__name__ = "Integer32"
_AtiAclProfileActionIndex_Object = MibTableColumn
atiAclProfileActionIndex = _AtiAclProfileActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 2, 1, 1),
    _AtiAclProfileActionIndex_Type()
)
atiAclProfileActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiAclProfileActionIndex.setStatus("current")


class _AtiAclProfileActionCos_Type(Integer32):
    """Custom type atiAclProfileActionCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AtiAclProfileActionCos_Type.__name__ = "Integer32"
_AtiAclProfileActionCos_Object = MibTableColumn
atiAclProfileActionCos = _AtiAclProfileActionCos_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 2, 1, 2),
    _AtiAclProfileActionCos_Type()
)
atiAclProfileActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclProfileActionCos.setStatus("current")


class _AtiAclProfileActionDscp_Type(Integer32):
    """Custom type atiAclProfileActionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AtiAclProfileActionDscp_Type.__name__ = "Integer32"
_AtiAclProfileActionDscp_Object = MibTableColumn
atiAclProfileActionDscp = _AtiAclProfileActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 2, 1, 3),
    _AtiAclProfileActionDscp_Type()
)
atiAclProfileActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclProfileActionDscp.setStatus("current")
_AtiAclProfileActionRowStatus_Type = RowStatus
_AtiAclProfileActionRowStatus_Object = MibTableColumn
atiAclProfileActionRowStatus = _AtiAclProfileActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 2, 1, 4),
    _AtiAclProfileActionRowStatus_Type()
)
atiAclProfileActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiAclProfileActionRowStatus.setStatus("current")
_AtiAclInProfileActionTable_Object = MibTable
atiAclInProfileActionTable = _AtiAclInProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 3)
)
if mibBuilder.loadTexts:
    atiAclInProfileActionTable.setStatus("current")
_AtiAclInProfileActionEntry_Object = MibTableRow
atiAclInProfileActionEntry = _AtiAclInProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 3, 1)
)
atiAclInProfileActionEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiAclInProfileActionIndex"),
)
if mibBuilder.loadTexts:
    atiAclInProfileActionEntry.setStatus("current")


class _AtiAclInProfileActionIndex_Type(Integer32):
    """Custom type atiAclInProfileActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclInProfileActionIndex_Type.__name__ = "Integer32"
_AtiAclInProfileActionIndex_Object = MibTableColumn
atiAclInProfileActionIndex = _AtiAclInProfileActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 3, 1, 1),
    _AtiAclInProfileActionIndex_Type()
)
atiAclInProfileActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiAclInProfileActionIndex.setStatus("current")


class _AtiAclInProfileActionPermitDeny_Type(Integer32):
    """Custom type atiAclInProfileActionPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtiAclInProfileActionPermitDeny_Type.__name__ = "Integer32"
_AtiAclInProfileActionPermitDeny_Object = MibTableColumn
atiAclInProfileActionPermitDeny = _AtiAclInProfileActionPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 3, 1, 2),
    _AtiAclInProfileActionPermitDeny_Type()
)
atiAclInProfileActionPermitDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclInProfileActionPermitDeny.setStatus("current")


class _AtiAclInProfileActionActionId_Type(Integer32):
    """Custom type atiAclInProfileActionActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 72),
    )


_AtiAclInProfileActionActionId_Type.__name__ = "Integer32"
_AtiAclInProfileActionActionId_Object = MibTableColumn
atiAclInProfileActionActionId = _AtiAclInProfileActionActionId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 3, 1, 3),
    _AtiAclInProfileActionActionId_Type()
)
atiAclInProfileActionActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclInProfileActionActionId.setStatus("current")
_AtiAclInProfileActionRowStatus_Type = RowStatus
_AtiAclInProfileActionRowStatus_Object = MibTableColumn
atiAclInProfileActionRowStatus = _AtiAclInProfileActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 3, 1, 4),
    _AtiAclInProfileActionRowStatus_Type()
)
atiAclInProfileActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiAclInProfileActionRowStatus.setStatus("current")
_AtiAclOutProfileActionTable_Object = MibTable
atiAclOutProfileActionTable = _AtiAclOutProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4)
)
if mibBuilder.loadTexts:
    atiAclOutProfileActionTable.setStatus("current")
_AtiAclOutProfileActionEntry_Object = MibTableRow
atiAclOutProfileActionEntry = _AtiAclOutProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1)
)
atiAclOutProfileActionEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiAclOutProfileActionIndex"),
)
if mibBuilder.loadTexts:
    atiAclOutProfileActionEntry.setStatus("current")


class _AtiAclOutProfileActionIndex_Type(Integer32):
    """Custom type atiAclOutProfileActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclOutProfileActionIndex_Type.__name__ = "Integer32"
_AtiAclOutProfileActionIndex_Object = MibTableColumn
atiAclOutProfileActionIndex = _AtiAclOutProfileActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1, 1),
    _AtiAclOutProfileActionIndex_Type()
)
atiAclOutProfileActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiAclOutProfileActionIndex.setStatus("current")


class _AtiAclOutProfileActionPermitDeny_Type(Integer32):
    """Custom type atiAclOutProfileActionPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtiAclOutProfileActionPermitDeny_Type.__name__ = "Integer32"
_AtiAclOutProfileActionPermitDeny_Object = MibTableColumn
atiAclOutProfileActionPermitDeny = _AtiAclOutProfileActionPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1, 2),
    _AtiAclOutProfileActionPermitDeny_Type()
)
atiAclOutProfileActionPermitDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclOutProfileActionPermitDeny.setStatus("current")


class _AtiAclOutProfileActionCommittedRate_Type(Integer32):
    """Custom type atiAclOutProfileActionCommittedRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_AtiAclOutProfileActionCommittedRate_Type.__name__ = "Integer32"
_AtiAclOutProfileActionCommittedRate_Object = MibTableColumn
atiAclOutProfileActionCommittedRate = _AtiAclOutProfileActionCommittedRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1, 3),
    _AtiAclOutProfileActionCommittedRate_Type()
)
atiAclOutProfileActionCommittedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclOutProfileActionCommittedRate.setStatus("current")


class _AtiAclOutProfileActionBurstSize_Type(Integer32):
    """Custom type atiAclOutProfileActionBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 64),
    )


_AtiAclOutProfileActionBurstSize_Type.__name__ = "Integer32"
_AtiAclOutProfileActionBurstSize_Object = MibTableColumn
atiAclOutProfileActionBurstSize = _AtiAclOutProfileActionBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1, 4),
    _AtiAclOutProfileActionBurstSize_Type()
)
atiAclOutProfileActionBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclOutProfileActionBurstSize.setStatus("current")


class _AtiAclOutProfileActionActionId_Type(Integer32):
    """Custom type atiAclOutProfileActionActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 72),
    )


_AtiAclOutProfileActionActionId_Type.__name__ = "Integer32"
_AtiAclOutProfileActionActionId_Object = MibTableColumn
atiAclOutProfileActionActionId = _AtiAclOutProfileActionActionId_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1, 5),
    _AtiAclOutProfileActionActionId_Type()
)
atiAclOutProfileActionActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclOutProfileActionActionId.setStatus("current")
_AtiAclOutProfileActionRowStatus_Type = RowStatus
_AtiAclOutProfileActionRowStatus_Object = MibTableColumn
atiAclOutProfileActionRowStatus = _AtiAclOutProfileActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 4, 1, 6),
    _AtiAclOutProfileActionRowStatus_Type()
)
atiAclOutProfileActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiAclOutProfileActionRowStatus.setStatus("current")
_AtiAclPortListTable_Object = MibTable
atiAclPortListTable = _AtiAclPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 5)
)
if mibBuilder.loadTexts:
    atiAclPortListTable.setStatus("current")
_AtiAclPortListEntry_Object = MibTableRow
atiAclPortListEntry = _AtiAclPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 5, 1)
)
atiAclPortListEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiAclPortListIndex"),
)
if mibBuilder.loadTexts:
    atiAclPortListEntry.setStatus("current")


class _AtiAclPortListIndex_Type(Integer32):
    """Custom type atiAclPortListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclPortListIndex_Type.__name__ = "Integer32"
_AtiAclPortListIndex_Object = MibTableColumn
atiAclPortListIndex = _AtiAclPortListIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 5, 1, 1),
    _AtiAclPortListIndex_Type()
)
atiAclPortListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiAclPortListIndex.setStatus("current")


class _AtiAclPortListString_Type(DisplayString):
    """Custom type atiAclPortListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AtiAclPortListString_Type.__name__ = "DisplayString"
_AtiAclPortListString_Object = MibTableColumn
atiAclPortListString = _AtiAclPortListString_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 5, 1, 2),
    _AtiAclPortListString_Type()
)
atiAclPortListString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclPortListString.setStatus("current")
_AtiAclPortListRowStatus_Type = RowStatus
_AtiAclPortListRowStatus_Object = MibTableColumn
atiAclPortListRowStatus = _AtiAclPortListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 5, 1, 3),
    _AtiAclPortListRowStatus_Type()
)
atiAclPortListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiAclPortListRowStatus.setStatus("current")
_AtiAclPolicyTable_Object = MibTable
atiAclPolicyTable = _AtiAclPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6)
)
if mibBuilder.loadTexts:
    atiAclPolicyTable.setStatus("current")
_AtiAclPolicyEntry_Object = MibTableRow
atiAclPolicyEntry = _AtiAclPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1)
)
atiAclPolicyEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiAclPolicyIndex"),
)
if mibBuilder.loadTexts:
    atiAclPolicyEntry.setStatus("current")


class _AtiAclPolicyIndex_Type(Integer32):
    """Custom type atiAclPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclPolicyIndex_Type.__name__ = "Integer32"
_AtiAclPolicyIndex_Object = MibTableColumn
atiAclPolicyIndex = _AtiAclPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 1),
    _AtiAclPolicyIndex_Type()
)
atiAclPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiAclPolicyIndex.setStatus("current")


class _AtiAclPolicyClassifierIndex_Type(Integer32):
    """Custom type atiAclPolicyClassifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclPolicyClassifierIndex_Type.__name__ = "Integer32"
_AtiAclPolicyClassifierIndex_Object = MibTableColumn
atiAclPolicyClassifierIndex = _AtiAclPolicyClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 2),
    _AtiAclPolicyClassifierIndex_Type()
)
atiAclPolicyClassifierIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclPolicyClassifierIndex.setStatus("current")


class _AtiAclPolicySequence_Type(Integer32):
    """Custom type atiAclPolicySequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtiAclPolicySequence_Type.__name__ = "Integer32"
_AtiAclPolicySequence_Object = MibTableColumn
atiAclPolicySequence = _AtiAclPolicySequence_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 3),
    _AtiAclPolicySequence_Type()
)
atiAclPolicySequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclPolicySequence.setStatus("current")


class _AtiAclPolicyInProfileIndex_Type(Integer32):
    """Custom type atiAclPolicyInProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclPolicyInProfileIndex_Type.__name__ = "Integer32"
_AtiAclPolicyInProfileIndex_Object = MibTableColumn
atiAclPolicyInProfileIndex = _AtiAclPolicyInProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 4),
    _AtiAclPolicyInProfileIndex_Type()
)
atiAclPolicyInProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclPolicyInProfileIndex.setStatus("current")


class _AtiAclPolicyOutProfileIndex_Type(Integer32):
    """Custom type atiAclPolicyOutProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtiAclPolicyOutProfileIndex_Type.__name__ = "Integer32"
_AtiAclPolicyOutProfileIndex_Object = MibTableColumn
atiAclPolicyOutProfileIndex = _AtiAclPolicyOutProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 5),
    _AtiAclPolicyOutProfileIndex_Type()
)
atiAclPolicyOutProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclPolicyOutProfileIndex.setStatus("current")


class _AtiAclPolicyPortListIndex_Type(Integer32):
    """Custom type atiAclPolicyPortListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiAclPolicyPortListIndex_Type.__name__ = "Integer32"
_AtiAclPolicyPortListIndex_Object = MibTableColumn
atiAclPolicyPortListIndex = _AtiAclPolicyPortListIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 6),
    _AtiAclPolicyPortListIndex_Type()
)
atiAclPolicyPortListIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiAclPolicyPortListIndex.setStatus("current")
_AtiAclPolicyRowStatus_Type = RowStatus
_AtiAclPolicyRowStatus_Object = MibTableColumn
atiAclPolicyRowStatus = _AtiAclPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 1, 6, 1, 7),
    _AtiAclPolicyRowStatus_Type()
)
atiAclPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiAclPolicyRowStatus.setStatus("current")
_AtiMacFilter_ObjectIdentity = ObjectIdentity
atiMacFilter = _AtiMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 2)
)
_AtiDstMacFilterTable_Object = MibTable
atiDstMacFilterTable = _AtiDstMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 2, 1)
)
if mibBuilder.loadTexts:
    atiDstMacFilterTable.setStatus("current")
_AtiDstMacFilterEntry_Object = MibTableRow
atiDstMacFilterEntry = _AtiDstMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 2, 1, 1)
)
atiDstMacFilterEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "atiDstMacFilterIndex"),
)
if mibBuilder.loadTexts:
    atiDstMacFilterEntry.setStatus("current")


class _AtiDstMacFilterIndex_Type(Integer32):
    """Custom type atiDstMacFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_AtiDstMacFilterIndex_Type.__name__ = "Integer32"
_AtiDstMacFilterIndex_Object = MibTableColumn
atiDstMacFilterIndex = _AtiDstMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 2, 1, 1, 1),
    _AtiDstMacFilterIndex_Type()
)
atiDstMacFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiDstMacFilterIndex.setStatus("current")
_AtiDstMacFilterAddress_Type = MacAddress
_AtiDstMacFilterAddress_Object = MibTableColumn
atiDstMacFilterAddress = _AtiDstMacFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 2, 1, 1, 2),
    _AtiDstMacFilterAddress_Type()
)
atiDstMacFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiDstMacFilterAddress.setStatus("current")
_AtiDstMacFilterRowStatus_Type = RowStatus
_AtiDstMacFilterRowStatus_Object = MibTableColumn
atiDstMacFilterRowStatus = _AtiDstMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 166, 2, 1, 1, 3),
    _AtiDstMacFilterRowStatus_Type()
)
atiDstMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiDstMacFilterRowStatus.setStatus("current")
_L2DhcpSnoop_ObjectIdentity = ObjectIdentity
l2DhcpSnoop = _L2DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181)
)


class _DhcpSnoopSystemStatus_Type(Integer32):
    """Custom type dhcpSnoopSystemStatus based on Integer32"""
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


_DhcpSnoopSystemStatus_Type.__name__ = "Integer32"
_DhcpSnoopSystemStatus_Object = MibScalar
dhcpSnoopSystemStatus = _DhcpSnoopSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 1),
    _DhcpSnoopSystemStatus_Type()
)
dhcpSnoopSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopSystemStatus.setStatus("current")


class _DhcpSnoopOption82Insertion_Type(Integer32):
    """Custom type dhcpSnoopOption82Insertion based on Integer32"""
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


_DhcpSnoopOption82Insertion_Type.__name__ = "Integer32"
_DhcpSnoopOption82Insertion_Object = MibScalar
dhcpSnoopOption82Insertion = _DhcpSnoopOption82Insertion_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 2),
    _DhcpSnoopOption82Insertion_Type()
)
dhcpSnoopOption82Insertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOption82Insertion.setStatus("current")


class _DhcpSnoopPassThroughOption82_Type(Integer32):
    """Custom type dhcpSnoopPassThroughOption82 based on Integer32"""
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


_DhcpSnoopPassThroughOption82_Type.__name__ = "Integer32"
_DhcpSnoopPassThroughOption82_Object = MibScalar
dhcpSnoopPassThroughOption82 = _DhcpSnoopPassThroughOption82_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 3),
    _DhcpSnoopPassThroughOption82_Type()
)
dhcpSnoopPassThroughOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPassThroughOption82.setStatus("current")


class _DhcpSnoopVerifyMACAddress_Type(Integer32):
    """Custom type dhcpSnoopVerifyMACAddress based on Integer32"""
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


_DhcpSnoopVerifyMACAddress_Type.__name__ = "Integer32"
_DhcpSnoopVerifyMACAddress_Object = MibScalar
dhcpSnoopVerifyMACAddress = _DhcpSnoopVerifyMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 4),
    _DhcpSnoopVerifyMACAddress_Type()
)
dhcpSnoopVerifyMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVerifyMACAddress.setStatus("current")


class _DhcpSnoopBackupDatabase_Type(Integer32):
    """Custom type dhcpSnoopBackupDatabase based on Integer32"""
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


_DhcpSnoopBackupDatabase_Type.__name__ = "Integer32"
_DhcpSnoopBackupDatabase_Object = MibScalar
dhcpSnoopBackupDatabase = _DhcpSnoopBackupDatabase_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 5),
    _DhcpSnoopBackupDatabase_Type()
)
dhcpSnoopBackupDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBackupDatabase.setStatus("current")


class _DhcpSnoopBackupDatabaseInterval_Type(Integer32):
    """Custom type dhcpSnoopBackupDatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86400),
    )


_DhcpSnoopBackupDatabaseInterval_Type.__name__ = "Integer32"
_DhcpSnoopBackupDatabaseInterval_Object = MibScalar
dhcpSnoopBackupDatabaseInterval = _DhcpSnoopBackupDatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 6),
    _DhcpSnoopBackupDatabaseInterval_Type()
)
dhcpSnoopBackupDatabaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBackupDatabaseInterval.setStatus("current")
_DhcpSnoopVLANSettingTable_Object = MibTable
dhcpSnoopVLANSettingTable = _DhcpSnoopVLANSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 7)
)
if mibBuilder.loadTexts:
    dhcpSnoopVLANSettingTable.setStatus("current")
_DhcpSnoopVLANSettingEntry_Object = MibTableRow
dhcpSnoopVLANSettingEntry = _DhcpSnoopVLANSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 7, 1)
)
dhcpSnoopVLANSettingEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dhcpSnoopVLANSettingVID"),
)
if mibBuilder.loadTexts:
    dhcpSnoopVLANSettingEntry.setStatus("current")


class _DhcpSnoopVLANSettingVID_Type(Unsigned32):
    """Custom type dhcpSnoopVLANSettingVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopVLANSettingVID_Type.__name__ = "Unsigned32"
_DhcpSnoopVLANSettingVID_Object = MibTableColumn
dhcpSnoopVLANSettingVID = _DhcpSnoopVLANSettingVID_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 7, 1, 1),
    _DhcpSnoopVLANSettingVID_Type()
)
dhcpSnoopVLANSettingVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopVLANSettingVID.setStatus("current")


class _DhcpSnoopVLANSettingStatus_Type(Integer32):
    """Custom type dhcpSnoopVLANSettingStatus based on Integer32"""
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


_DhcpSnoopVLANSettingStatus_Type.__name__ = "Integer32"
_DhcpSnoopVLANSettingStatus_Object = MibTableColumn
dhcpSnoopVLANSettingStatus = _DhcpSnoopVLANSettingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 7, 1, 2),
    _DhcpSnoopVLANSettingStatus_Type()
)
dhcpSnoopVLANSettingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVLANSettingStatus.setStatus("current")
_DhcpSnoopPortSettingTable_Object = MibTable
dhcpSnoopPortSettingTable = _DhcpSnoopPortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 8)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortSettingTable.setStatus("current")
_DhcpSnoopPortSettingEntry_Object = MibTableRow
dhcpSnoopPortSettingEntry = _DhcpSnoopPortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 8, 1)
)
dhcpSnoopPortSettingEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dhcpSnoopPortSettingIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortSettingEntry.setStatus("current")


class _DhcpSnoopPortSettingIndex_Type(Integer32):
    """Custom type dhcpSnoopPortSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcpSnoopPortSettingIndex_Type.__name__ = "Integer32"
_DhcpSnoopPortSettingIndex_Object = MibTableColumn
dhcpSnoopPortSettingIndex = _DhcpSnoopPortSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 8, 1, 1),
    _DhcpSnoopPortSettingIndex_Type()
)
dhcpSnoopPortSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopPortSettingIndex.setStatus("current")


class _DhcpSnoopPortSettingStatus_Type(Integer32):
    """Custom type dhcpSnoopPortSettingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 0))
    )


_DhcpSnoopPortSettingStatus_Type.__name__ = "Integer32"
_DhcpSnoopPortSettingStatus_Object = MibTableColumn
dhcpSnoopPortSettingStatus = _DhcpSnoopPortSettingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 8, 1, 2),
    _DhcpSnoopPortSettingStatus_Type()
)
dhcpSnoopPortSettingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortSettingStatus.setStatus("current")
_DhcpSnoopBindindDatabaseTable_Object = MibTable
dhcpSnoopBindindDatabaseTable = _DhcpSnoopBindindDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9)
)
if mibBuilder.loadTexts:
    dhcpSnoopBindindDatabaseTable.setStatus("current")
_DhcpSnoopBindindDatabaseEntry_Object = MibTableRow
dhcpSnoopBindindDatabaseEntry = _DhcpSnoopBindindDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1)
)
dhcpSnoopBindindDatabaseEntry.setIndexNames(
    (0, "AT-GS950-16-MIB", "dhcpSnoopBindindDBMacAddress"),
)
if mibBuilder.loadTexts:
    dhcpSnoopBindindDatabaseEntry.setStatus("current")
_DhcpSnoopBindindDBMacAddress_Type = MacAddress
_DhcpSnoopBindindDBMacAddress_Object = MibTableColumn
dhcpSnoopBindindDBMacAddress = _DhcpSnoopBindindDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 1),
    _DhcpSnoopBindindDBMacAddress_Type()
)
dhcpSnoopBindindDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBMacAddress.setStatus("current")


class _DhcpSnoopBindindDBVLANID_Type(Unsigned32):
    """Custom type dhcpSnoopBindindDBVLANID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopBindindDBVLANID_Type.__name__ = "Unsigned32"
_DhcpSnoopBindindDBVLANID_Object = MibTableColumn
dhcpSnoopBindindDBVLANID = _DhcpSnoopBindindDBVLANID_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 2),
    _DhcpSnoopBindindDBVLANID_Type()
)
dhcpSnoopBindindDBVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBVLANID.setStatus("current")
_DhcpSnoopBindindDBIPAddress_Type = IpAddress
_DhcpSnoopBindindDBIPAddress_Object = MibTableColumn
dhcpSnoopBindindDBIPAddress = _DhcpSnoopBindindDBIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 3),
    _DhcpSnoopBindindDBIPAddress_Type()
)
dhcpSnoopBindindDBIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBIPAddress.setStatus("current")
_DhcpSnoopBindindDBPortNumber_Type = Integer32
_DhcpSnoopBindindDBPortNumber_Object = MibTableColumn
dhcpSnoopBindindDBPortNumber = _DhcpSnoopBindindDBPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 4),
    _DhcpSnoopBindindDBPortNumber_Type()
)
dhcpSnoopBindindDBPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBPortNumber.setStatus("current")


class _DhcpSnoopBindindDBType_Type(Integer32):
    """Custom type dhcpSnoopBindindDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_DhcpSnoopBindindDBType_Type.__name__ = "Integer32"
_DhcpSnoopBindindDBType_Object = MibTableColumn
dhcpSnoopBindindDBType = _DhcpSnoopBindindDBType_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 5),
    _DhcpSnoopBindindDBType_Type()
)
dhcpSnoopBindindDBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBType.setStatus("current")
_DhcpSnoopBindindDBLeaseTime_Type = Unsigned32
_DhcpSnoopBindindDBLeaseTime_Object = MibTableColumn
dhcpSnoopBindindDBLeaseTime = _DhcpSnoopBindindDBLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 6),
    _DhcpSnoopBindindDBLeaseTime_Type()
)
dhcpSnoopBindindDBLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBLeaseTime.setStatus("current")
_DhcpSnoopBindindDBRowStatus_Type = RowStatus
_DhcpSnoopBindindDBRowStatus_Object = MibTableColumn
dhcpSnoopBindindDBRowStatus = _DhcpSnoopBindindDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 181, 9, 1, 7),
    _DhcpSnoopBindindDBRowStatus_Type()
)
dhcpSnoopBindindDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopBindindDBRowStatus.setStatus("current")
dot1dStpEntry.registerAugmentions(
    ("AT-GS950-16-MIB",
     "dot1dStpExtEntry")
)
dot1dStpExtEntry.setIndexNames(*dot1dStpEntry.getIndexNames())
dot1dStpPortEntry.registerAugmentions(
    ("AT-GS950-16-MIB",
     "dot1dStpExtPortEntry")
)
dot1dStpExtPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("AT-GS950-16-MIB",
     "dot1dPortCapabilitiesEntry")
)
dot1dPortCapabilitiesEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("AT-GS950-16-MIB",
     "dot1dPortPriorityEntry")
)
dot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("AT-GS950-16-MIB",
     "dot1dPortGarpEntry")
)
dot1dPortGarpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

dot1dExtCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 1)
)
dot1dExtCapGroup.setObjects(
      *(("AT-GS950-16-MIB", "dot1dDeviceCapabilities"),
        ("AT-GS950-16-MIB", "dot1dPortCapabilities"))
)
if mibBuilder.loadTexts:
    dot1dExtCapGroup.setStatus("current")

dot1dDeviceGmrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 2)
)
dot1dDeviceGmrpGroup.setObjects(
    ("AT-GS950-16-MIB", "dot1dGmrpStatus")
)
if mibBuilder.loadTexts:
    dot1dDeviceGmrpGroup.setStatus("current")

dot1dDevicePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 3)
)
dot1dDevicePriorityGroup.setObjects(
    ("AT-GS950-16-MIB", "dot1dTrafficClassesEnabled")
)
if mibBuilder.loadTexts:
    dot1dDevicePriorityGroup.setStatus("current")

dot1dDefaultPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 4)
)
dot1dDefaultPriorityGroup.setObjects(
    ("AT-GS950-16-MIB", "dot1dPortDefaultUserPriority")
)
if mibBuilder.loadTexts:
    dot1dDefaultPriorityGroup.setStatus("current")

dot1dRegenPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 5)
)
dot1dRegenPriorityGroup.setObjects(
    ("AT-GS950-16-MIB", "dot1dRegenUserPriority")
)
if mibBuilder.loadTexts:
    dot1dRegenPriorityGroup.setStatus("current")

dot1dPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 6)
)
dot1dPriorityGroup.setObjects(
      *(("AT-GS950-16-MIB", "dot1dPortNumTrafficClasses"),
        ("AT-GS950-16-MIB", "dot1dTrafficClass"))
)
if mibBuilder.loadTexts:
    dot1dPriorityGroup.setStatus("current")

dot1dAccessPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 7)
)
dot1dAccessPriorityGroup.setObjects(
    ("AT-GS950-16-MIB", "dot1dPortOutboundAccessPriority")
)
if mibBuilder.loadTexts:
    dot1dAccessPriorityGroup.setStatus("current")

dot1dPortGarpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 8)
)
dot1dPortGarpGroup.setObjects(
      *(("AT-GS950-16-MIB", "dot1dPortGarpJoinTime"),
        ("AT-GS950-16-MIB", "dot1dPortGarpLeaveTime"),
        ("AT-GS950-16-MIB", "dot1dPortGarpLeaveAllTime"))
)
if mibBuilder.loadTexts:
    dot1dPortGarpGroup.setStatus("current")

dot1dHCPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 10)
)
dot1dHCPortGroup.setObjects(
      *(("AT-GS950-16-MIB", "dot1dTpHCPortInFrames"),
        ("AT-GS950-16-MIB", "dot1dTpHCPortOutFrames"),
        ("AT-GS950-16-MIB", "dot1dTpHCPortInDiscards"))
)
if mibBuilder.loadTexts:
    dot1dHCPortGroup.setStatus("current")

dot1dPortOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 1, 11)
)
dot1dPortOverflowGroup.setObjects(
      *(("AT-GS950-16-MIB", "dot1dTpPortInOverflowFrames"),
        ("AT-GS950-16-MIB", "dot1dTpPortOutOverflowFrames"),
        ("AT-GS950-16-MIB", "dot1dTpPortInOverflowDiscards"))
)
if mibBuilder.loadTexts:
    dot1dPortOverflowGroup.setStatus("current")


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 0, 1)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        "current"
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 0, 2)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

dot1sGlobalErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 1)
)
dot1sGlobalErrTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    dot1sGlobalErrTrap.setStatus(
        "current"
    )

dot1sGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 2)
)
dot1sGenTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sContextName"),
        ("AT-GS950-16-MIB", "dot1sGenTrapType"))
)
if mibBuilder.loadTexts:
    dot1sGenTrap.setStatus(
        "current"
    )

dot1sNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 3)
)
dot1sNewRootTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sContextName"),
        ("AT-GS950-16-MIB", "dot1sOldDesignatedRoot"),
        ("AT-GS950-16-MIB", "dot1sMstiBridgeRegionalRoot"))
)
if mibBuilder.loadTexts:
    dot1sNewRootTrap.setStatus(
        "current"
    )

dot1sTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 4)
)
dot1sTopologyChgTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sContextName"),
        ("AT-GS950-16-MIB", "dot1sMstiTopChanges"))
)
if mibBuilder.loadTexts:
    dot1sTopologyChgTrap.setStatus(
        "current"
    )

dot1sProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 5)
)
dot1sProtocolMigrationTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sContextName"),
        ("AT-GS950-16-MIB", "dot1sForceProtocolVersion"),
        ("AT-GS950-16-MIB", "dot1sPortMigrationType"))
)
if mibBuilder.loadTexts:
    dot1sProtocolMigrationTrap.setStatus(
        "current"
    )

dot1sInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 6)
)
dot1sInvalidBpduRxdTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sContextName"),
        ("AT-GS950-16-MIB", "dot1sPktErrType"),
        ("AT-GS950-16-MIB", "dot1sPktErrVal"))
)
if mibBuilder.loadTexts:
    dot1sInvalidBpduRxdTrap.setStatus(
        "current"
    )

dot1sRegionConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 7)
)
dot1sRegionConfigChangeTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sContextName"),
        ("AT-GS950-16-MIB", "dot1sMstiConfigIdSel"),
        ("AT-GS950-16-MIB", "dot1sMstiRegionName"),
        ("AT-GS950-16-MIB", "dot1sMstiRegionVersion"),
        ("AT-GS950-16-MIB", "dot1sMstiConfigDigest"))
)
if mibBuilder.loadTexts:
    dot1sRegionConfigChangeTrap.setStatus(
        "current"
    )

dot1sNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 118, 3, 0, 8)
)
dot1sNewPortRoleTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1sBrgAddress"),
        ("AT-GS950-16-MIB", "dot1sPortRoleType"),
        ("AT-GS950-16-MIB", "dot1sOldRoleType"))
)
if mibBuilder.loadTexts:
    dot1sNewPortRoleTrap.setStatus(
        "current"
    )

dot1wGlobalErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 1)
)
dot1wGlobalErrTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    dot1wGlobalErrTrap.setStatus(
        "current"
    )

dot1wGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 2)
)
dot1wGenTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wContextName"),
        ("AT-GS950-16-MIB", "dot1wGenTrapType"))
)
if mibBuilder.loadTexts:
    dot1wGenTrap.setStatus(
        "current"
    )

dot1wNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 3)
)
dot1wNewRootTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wContextName"),
        ("AT-GS950-16-MIB", "dot1wOldDesignatedRoot"),
        ("AT-GS950-16-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    dot1wNewRootTrap.setStatus(
        "current"
    )

dot1wTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 4)
)
dot1wTopologyChgTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wContextName"))
)
if mibBuilder.loadTexts:
    dot1wTopologyChgTrap.setStatus(
        "current"
    )

dot1wProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 5)
)
dot1wProtocolMigrationTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wContextName"),
        ("AT-GS950-16-MIB", "dot1dStpVersion"),
        ("AT-GS950-16-MIB", "dot1wPortMigrationType"))
)
if mibBuilder.loadTexts:
    dot1wProtocolMigrationTrap.setStatus(
        "current"
    )

dot1wInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 6)
)
dot1wInvalidBpduRxdTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wContextName"),
        ("AT-GS950-16-MIB", "dot1wPktErrType"),
        ("AT-GS950-16-MIB", "dot1wPktErrVal"))
)
if mibBuilder.loadTexts:
    dot1wInvalidBpduRxdTrap.setStatus(
        "current"
    )

dot1wNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 119, 3, 0, 7)
)
dot1wNewPortRoleTrap.setObjects(
      *(("AT-GS950-16-MIB", "dot1dBaseBridgeAddress"),
        ("AT-GS950-16-MIB", "dot1wPortRoleType"),
        ("AT-GS950-16-MIB", "dot1wOldRoleType"))
)
if mibBuilder.loadTexts:
    dot1wNewPortRoleTrap.setStatus(
        "current"
    )

fsLldpRemTablesChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 1)
)
fsLldpRemTablesChange.setObjects(
      *(("LLDP-MIB", "lldpStatsRemTablesInserts"),
        ("LLDP-MIB", "lldpStatsRemTablesDeletes"),
        ("LLDP-MIB", "lldpStatsRemTablesDrops"),
        ("LLDP-MIB", "lldpStatsRemTablesAgeouts"),
        ("AT-GS950-16-MIB", "fsLldpStatsRemTablesUpdates"))
)
if mibBuilder.loadTexts:
    fsLldpRemTablesChange.setStatus(
        "current"
    )

fsLldpExceedsMaxFrameSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 2)
)
fsLldpExceedsMaxFrameSize.setObjects(
    ("LLDP-MIB", "lldpLocPortId")
)
if mibBuilder.loadTexts:
    fsLldpExceedsMaxFrameSize.setStatus(
        "current"
    )

fsLldpDupChasisId = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 3)
)
fsLldpDupChasisId.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"))
)
if mibBuilder.loadTexts:
    fsLldpDupChasisId.setStatus(
        "current"
    )

fsLldpDupSystemName = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 4)
)
fsLldpDupSystemName.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-MIB", "lldpRemSysName"))
)
if mibBuilder.loadTexts:
    fsLldpDupSystemName.setStatus(
        "current"
    )

fsLldpDupManagmentAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 5)
)
fsLldpDupManagmentAddress.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-MIB", "lldpRemManAddr"))
)
if mibBuilder.loadTexts:
    fsLldpDupManagmentAddress.setStatus(
        "current"
    )

fsLldpMisConfigPortVlanID = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 6)
)
fsLldpMisConfigPortVlanID.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemPortVlanId"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigPortVlanID.setStatus(
        "current"
    )

fsLldpMisConfigPortProtoVlanID = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 7)
)
fsLldpMisConfigPortProtoVlanID.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanSupported"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigPortProtoVlanID.setStatus(
        "current"
    )

fsLldpMisConfigVlanName = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 8)
)
fsLldpMisConfigVlanName.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemVlanName"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigVlanName.setStatus(
        "current"
    )

fsLldpMisConfigProtocolIdentity = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 9)
)
fsLldpMisConfigProtocolIdentity.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtocolId"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigProtocolIdentity.setStatus(
        "current"
    )

fsLldpMisConfigLinkAggStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 10)
)
fsLldpMisConfigLinkAggStatus.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemLinkAggStatus"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigLinkAggStatus.setStatus(
        "current"
    )

fsLldpMisConfigPowerMDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 11)
)
fsLldpMisConfigPowerMDI.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerClass"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigPowerMDI.setStatus(
        "current"
    )

fsLldpMisConfigMaxFrameSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 12)
)
fsLldpMisConfigMaxFrameSize.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemMaxFrameSize"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigMaxFrameSize.setStatus(
        "current"
    )

fsLldpMisConfigOperMauType = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 158, 4, 0, 13)
)
fsLldpMisConfigOperMauType.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortOperMauType"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigOperMauType.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

dot1dCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 166, 116, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-GS950-16-MIB",
    **{"L2snmpLevel": L2snmpLevel,
       "PortLaMode": PortLaMode,
       "LacpKey": LacpKey,
       "LacpState": LacpState,
       "PaeControlledPortStatus": PaeControlledPortStatus,
       "AuthenticMethod": AuthenticMethod,
       "PermissionType": PermissionType,
       "IfDirection": IfDirection,
       "DscpOrAny": DscpOrAny,
       "InetAddressIPv4": InetAddressIPv4,
       "InetAddressIPv6": InetAddressIPv6,
       "InetAddressDNS": InetAddressDNS,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "VlanIndex": VlanIndex,
       "VlanId": VlanId,
       "at-GS95016v3": at_GS95016v3,
       "l2Snmp": l2Snmp,
       "sysSnmpUser": sysSnmpUser,
       "sysSnmpUserTable": sysSnmpUserTable,
       "sysSnmpUserEntry": sysSnmpUserEntry,
       "sysSnmpUserName": sysSnmpUserName,
       "sysSnmpUserAuthProtocol": sysSnmpUserAuthProtocol,
       "sysSnmpUserPrivProtocol": sysSnmpUserPrivProtocol,
       "sysSnmpUserStatus": sysSnmpUserStatus,
       "sysSnmpGroup": sysSnmpGroup,
       "sysSnmpGroupTable": sysSnmpGroupTable,
       "sysSnmpGroupEntry": sysSnmpGroupEntry,
       "sysSnmpSecurityModel": sysSnmpSecurityModel,
       "sysSnmpSecurityName": sysSnmpSecurityName,
       "sysSnmpGroupName": sysSnmpGroupName,
       "sysSnmpGroupStatus": sysSnmpGroupStatus,
       "sysSnmpGroupAccess": sysSnmpGroupAccess,
       "sysSnmpGroupAccessTable": sysSnmpGroupAccessTable,
       "sysSnmpGroupAccessEntry": sysSnmpGroupAccessEntry,
       "sysSnmpaccessGroupIndex": sysSnmpaccessGroupIndex,
       "sysSnmpaccessSecurityModel": sysSnmpaccessSecurityModel,
       "sysSnmpaccessSecurityLevel": sysSnmpaccessSecurityLevel,
       "sysSnmpaccessReadViewName": sysSnmpaccessReadViewName,
       "sysSnmpaccessWriteViewName": sysSnmpaccessWriteViewName,
       "sysSnmpaccessNotifyViewName": sysSnmpaccessNotifyViewName,
       "sysSnmpaccessStatus": sysSnmpaccessStatus,
       "sysSnmpViewTree": sysSnmpViewTree,
       "sysSnmpViewTreeTable": sysSnmpViewTreeTable,
       "sysSnmpViewTreeEntry": sysSnmpViewTreeEntry,
       "sysSnmpviewTreeName": sysSnmpviewTreeName,
       "sysSnmpviewTreeSubtree": sysSnmpviewTreeSubtree,
       "sysSnmpviewTreeMask": sysSnmpviewTreeMask,
       "sysSnmpviewTreeType": sysSnmpviewTreeType,
       "sysSnmpviewTreeStatus": sysSnmpviewTreeStatus,
       "sysSnmpCommunity": sysSnmpCommunity,
       "sysSnmpCommunityTable": sysSnmpCommunityTable,
       "sysSnmpCommunityEntry": sysSnmpCommunityEntry,
       "sysSnmpsnmpCommunityIndex": sysSnmpsnmpCommunityIndex,
       "sysSnmpsnmpCommunityName": sysSnmpsnmpCommunityName,
       "sysSnmpsnmpCommunityPolicy": sysSnmpsnmpCommunityPolicy,
       "sysSnmpsnmpCommunityStatus": sysSnmpsnmpCommunityStatus,
       "sysSnmpTrapManager": sysSnmpTrapManager,
       "sysSnmpTrapManagerTable": sysSnmpTrapManagerTable,
       "sysSnmpTrapManagerEntry": sysSnmpTrapManagerEntry,
       "sysSnmpsnmpTrapManagerName": sysSnmpsnmpTrapManagerName,
       "sysSnmpsnmpTrapManagerAddress": sysSnmpsnmpTrapManagerAddress,
       "sysSnmpsnmpTrapManagerSecurityLevel": sysSnmpsnmpTrapManagerSecurityLevel,
       "sysSnmpsnmpTrapManagerStatus": sysSnmpsnmpTrapManagerStatus,
       "sysSnmpEngineID": sysSnmpEngineID,
       "snmpGlobalState": snmpGlobalState,
       "l2Radius": l2Radius,
       "sysRadiusExtClient": sysRadiusExtClient,
       "sysRadiusExtServerTable": sysRadiusExtServerTable,
       "sysRadiusExtServerEntry": sysRadiusExtServerEntry,
       "sysRadiusExtServerIndex": sysRadiusExtServerIndex,
       "sysRadiusExtServerAddress": sysRadiusExtServerAddress,
       "sysRadiusExtServerSharedSecret": sysRadiusExtServerSharedSecret,
       "sysRadiusExtServerResponseTime": sysRadiusExtServerResponseTime,
       "sysRadiusExtServerMaximumRetransmission": sysRadiusExtServerMaximumRetransmission,
       "sysRadiusExtServerAuthPortNum": sysRadiusExtServerAuthPortNum,
       "sysRadiusExtServerEntryStatus": sysRadiusExtServerEntryStatus,
       "sysRadiusExtServerAccPort": sysRadiusExtServerAccPort,
       "l2Cfa": l2Cfa,
       "if": _pysmi_if,
       "ifMaxInterfaces": ifMaxInterfaces,
       "ifMaxPhysInterfaces": ifMaxPhysInterfaces,
       "ifAvailableIndex": ifAvailableIndex,
       "ifMainTable": ifMainTable,
       "ifMainEntry": ifMainEntry,
       "ifMainIndex": ifMainIndex,
       "ifMainType": ifMainType,
       "ifMainMtu": ifMainMtu,
       "ifMainAdminStatus": ifMainAdminStatus,
       "ifMainOperStatus": ifMainOperStatus,
       "ifMainEncapType": ifMainEncapType,
       "ifMainBrgPortType": ifMainBrgPortType,
       "ifMainRowStatus": ifMainRowStatus,
       "ifIpTable": ifIpTable,
       "ifIpEntry": ifIpEntry,
       "ifIpAddrAllocMethod": ifIpAddrAllocMethod,
       "ifIpAddr": ifIpAddr,
       "ifIpSubnetMask": ifIpSubnetMask,
       "ifIpBroadcastAddr": ifIpBroadcastAddr,
       "ifIpForwardingEnable": ifIpForwardingEnable,
       "ifIpAddrAllocProtocol": ifIpAddrAllocProtocol,
       "ifIvrTable": ifIvrTable,
       "ifIvrEntry": ifIvrEntry,
       "ifIvrBridgedIface": ifIvrBridgedIface,
       "ifSetMgmtVlanList": ifSetMgmtVlanList,
       "ifResetMgmtVlanList": ifResetMgmtVlanList,
       "ifSecondaryIpAddressTable": ifSecondaryIpAddressTable,
       "ifSecondaryIpAddressEntry": ifSecondaryIpAddressEntry,
       "ifSecondaryIpAddress": ifSecondaryIpAddress,
       "ifSecondaryIpSubnetMask": ifSecondaryIpSubnetMask,
       "ifSecondaryIpBroadcastAddr": ifSecondaryIpBroadcastAddr,
       "ifSecondaryIpRowStatus": ifSecondaryIpRowStatus,
       "traps": traps,
       "l2Rmon": l2Rmon,
       "sysRmonEnableStatus": sysRmonEnableStatus,
       "sysRmonHwStatsSupp": sysRmonHwStatsSupp,
       "sysRmonHwHistorySupp": sysRmonHwHistorySupp,
       "sysRmonHwAlarmSupp": sysRmonHwAlarmSupp,
       "sysRmonHwEventSupp": sysRmonHwEventSupp,
       "l2La": l2La,
       "sysLaSystem": sysLaSystem,
       "sysLaSystemControl": sysLaSystemControl,
       "sysLaStatus": sysLaStatus,
       "sysLaTraceOption": sysLaTraceOption,
       "sysLaMaxPortsPerPortChannel": sysLaMaxPortsPerPortChannel,
       "sysLaMaxPortChannels": sysLaMaxPortChannels,
       "sysLaOperStatus": sysLaOperStatus,
       "sysLaActorSystemID": sysLaActorSystemID,
       "sysLaPortChannel": sysLaPortChannel,
       "sysLaPortChannelTable": sysLaPortChannelTable,
       "sysLaPortChannelEntry": sysLaPortChannelEntry,
       "sysLaPortChannelIfIndex": sysLaPortChannelIfIndex,
       "sysLaPortChannelGroup": sysLaPortChannelGroup,
       "sysLaPortChannelAdminMacAddress": sysLaPortChannelAdminMacAddress,
       "sysLaPortChannelMacSelection": sysLaPortChannelMacSelection,
       "sysLaPortChannelMode": sysLaPortChannelMode,
       "sysLaPortChannelPortCount": sysLaPortChannelPortCount,
       "sysLaPortChannelActivePortCount": sysLaPortChannelActivePortCount,
       "sysLaPortChannelSelectionPolicy": sysLaPortChannelSelectionPolicy,
       "sysLaPortChannelDefaultPortIndex": sysLaPortChannelDefaultPortIndex,
       "sysLaPort": sysLaPort,
       "sysLaPortTable": sysLaPortTable,
       "sysLaPortEntry": sysLaPortEntry,
       "sysLaPortIndex": sysLaPortIndex,
       "sysLaPortMode": sysLaPortMode,
       "sysLaPortBundleState": sysLaPortBundleState,
       "sysLaPortActorResetAdminState": sysLaPortActorResetAdminState,
       "sysLaPortAggregateWaitTime": sysLaPortAggregateWaitTime,
       "sysLaPortPartnerResetAdminState": sysLaPortPartnerResetAdminState,
       "sysLaPortActorAdminPort": sysLaPortActorAdminPort,
       "sysLaPortRestoreMtu": sysLaPortRestoreMtu,
       "sysLaPortSelectAggregator": sysLaPortSelectAggregator,
       "l2Pnac": l2Pnac,
       "sysPnacPaeSystem": sysPnacPaeSystem,
       "sysPnacSystemControl": sysPnacSystemControl,
       "sysPnacAuthenticServer": sysPnacAuthenticServer,
       "sysPnacNasId": sysPnacNasId,
       "sysPnacPaePortTable": sysPnacPaePortTable,
       "sysPnacPaePortEntry": sysPnacPaePortEntry,
       "sysPnacPaePortNumber": sysPnacPaePortNumber,
       "sysPnacPaePortStatus": sysPnacPaePortStatus,
       "sysPnacPaeMultiAuthEnable": sysPnacPaeMultiAuthEnable,
       "sysPnacPaeProtocolMode": sysPnacPaeProtocolMode,
       "sysPnacPaePiggybackMode": sysPnacPaePiggybackMode,
       "sysPnacPaeVlanAssignment": sysPnacPaeVlanAssignment,
       "sysPnacPaeSecureVlan": sysPnacPaeSecureVlan,
       "sysPnacModuleOperStatus": sysPnacModuleOperStatus,
       "sysPnacAuthServer": sysPnacAuthServer,
       "sysPnacASUserConfigTable": sysPnacASUserConfigTable,
       "sysPnacASUserConfigEntry": sysPnacASUserConfigEntry,
       "sysPnacASUserConfigUserName": sysPnacASUserConfigUserName,
       "sysPnacASUserConfigPassword": sysPnacASUserConfigPassword,
       "sysPnacASUserConfigAuthProtocol": sysPnacASUserConfigAuthProtocol,
       "sysPnacASUserConfigAuthTimeout": sysPnacASUserConfigAuthTimeout,
       "sysPnacASUserConfigPortList": sysPnacASUserConfigPortList,
       "sysPnacASUserConfigPermission": sysPnacASUserConfigPermission,
       "sysPnacASUserConfigDynamicVlanID": sysPnacASUserConfigDynamicVlanID,
       "sysPnacASUserConfigRowStatus": sysPnacASUserConfigRowStatus,
       "sysGuestVlan": sysGuestVlan,
       "sysPnacGuestVlanTable": sysPnacGuestVlanTable,
       "sysPnacGuestVlanEntry": sysPnacGuestVlanEntry,
       "sysPnacPaePortNo": sysPnacPaePortNo,
       "sysPnacGuestVlanId": sysPnacGuestVlanId,
       "l2System": l2System,
       "sysSystemInfo": sysSystemInfo,
       "sysSwitchName": sysSwitchName,
       "sysHardwareVersion": sysHardwareVersion,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysDefaultIpAddrCfgMode": sysDefaultIpAddrCfgMode,
       "sysDefaultIpAddr": sysDefaultIpAddr,
       "sysDefaultIpSubnetMask": sysDefaultIpSubnetMask,
       "sysRestart": sysRestart,
       "sysConfigSaveOption": sysConfigSaveOption,
       "sysConfigSaveIpAddr": sysConfigSaveIpAddr,
       "sysConfigSaveFileName": sysConfigSaveFileName,
       "sysInitiateConfigSave": sysInitiateConfigSave,
       "sysConfigSaveStatus": sysConfigSaveStatus,
       "sysConfigRestoreOption": sysConfigRestoreOption,
       "sysRemoteConfigRestoreIpAddr": sysRemoteConfigRestoreIpAddr,
       "sysConfigRestoreFileName": sysConfigRestoreFileName,
       "sysInitiateRemoteConfigRestore": sysInitiateRemoteConfigRestore,
       "sysConfigRestoreStatus": sysConfigRestoreStatus,
       "sysDlFirmwareFromIp": sysDlFirmwareFromIp,
       "sysDlFirmwareName": sysDlFirmwareName,
       "sysInitiateDlFirmware": sysInitiateDlFirmware,
       "sysLoggingOption": sysLoggingOption,
       "sysUploadLogFileToIp": sysUploadLogFileToIp,
       "sysLogFileName": sysLogFileName,
       "sysInitiateUlLogFile": sysInitiateUlLogFile,
       "sysSysContact": sysSysContact,
       "sysSysLocation": sysSysLocation,
       "sysLoginAuthentication": sysLoginAuthentication,
       "sysSwitchBaseMacAddress": sysSwitchBaseMacAddress,
       "sysSwitchDate": sysSwitchDate,
       "sysHttpPort": sysHttpPort,
       "sysHttpStatus": sysHttpStatus,
       "sysDefaultVlanId": sysDefaultVlanId,
       "sysWebAutoTimeoutInterval": sysWebAutoTimeoutInterval,
       "sysCliAutoTimeoutInterval": sysCliAutoTimeoutInterval,
       "sysCpuPolicerStatus": sysCpuPolicerStatus,
       "sysLedEcoModeStatus": sysLedEcoModeStatus,
       "sysPowerSavingEnable": sysPowerSavingEnable,
       "sysDhcpAutoConfiguration": sysDhcpAutoConfiguration,
       "sysAsyVLANEnable": sysAsyVLANEnable,
       "issCosEnable": issCosEnable,
       "sysTrapEnable": sysTrapEnable,
       "sysFDResetStateEnable": sysFDResetStateEnable,
       "sysFDRInputPw": sysFDRInputPw,
       "sysConfigControl": sysConfigControl,
       "sysConfigCtrlTable": sysConfigCtrlTable,
       "sysConfigCtrlEntry": sysConfigCtrlEntry,
       "sysConfigCtrlIndex": sysConfigCtrlIndex,
       "sysConfigCtrlEgressStatus": sysConfigCtrlEgressStatus,
       "sysConfigCtrlStatsCollection": sysConfigCtrlStatsCollection,
       "sysConfigCtrlStatus": sysConfigCtrlStatus,
       "sysPortCtrlTable": sysPortCtrlTable,
       "sysPortCtrlEntry": sysPortCtrlEntry,
       "sysPortCtrlIndex": sysPortCtrlIndex,
       "sysPortCtrlMode": sysPortCtrlMode,
       "sysPortCtrlDuplex": sysPortCtrlDuplex,
       "sysPortCtrlSpeed": sysPortCtrlSpeed,
       "sysPortCtrlFlowControl": sysPortCtrlFlowControl,
       "sysPortCtrlMDI": sysPortCtrlMDI,
       "issJumboFramePerPortEnable": issJumboFramePerPortEnable,
       "issJumboFramePerPortMtu": issJumboFramePerPortMtu,
       "sysPortCtrlEAPPassThrough": sysPortCtrlEAPPassThrough,
       "sysPortCtrlBPDUPassThrough": sysPortCtrlBPDUPassThrough,
       "sysMirror": sysMirror,
       "sysMirrorStatus": sysMirrorStatus,
       "sysMirrorToPort": sysMirrorToPort,
       "sysMirrorCtrlTable": sysMirrorCtrlTable,
       "sysMirrorCtrlEntry": sysMirrorCtrlEntry,
       "sysMirrorCtrlIndex": sysMirrorCtrlIndex,
       "sysMirrorCtrlIngressMirroring": sysMirrorCtrlIngressMirroring,
       "sysMirrorCtrlEgressMirroring": sysMirrorCtrlEgressMirroring,
       "sysMirrorCtrlStatus": sysMirrorCtrlStatus,
       "sysRateControl": sysRateControl,
       "sysRateCtrlTable": sysRateCtrlTable,
       "sysRateCtrlEntry": sysRateCtrlEntry,
       "sysRateCtrlIndex": sysRateCtrlIndex,
       "sysRateCtrlEgressLimitValue": sysRateCtrlEgressLimitValue,
       "sysRateCtrlIngressLimitValue": sysRateCtrlIngressLimitValue,
       "sysIpAuthMgr": sysIpAuthMgr,
       "sysIpAuthMgrStatus": sysIpAuthMgrStatus,
       "sysIpAuthMgrTable": sysIpAuthMgrTable,
       "sysIpAuthMgrEntry": sysIpAuthMgrEntry,
       "sysIpAuthMgrIpAddr": sysIpAuthMgrIpAddr,
       "sysIpAuthMgrIpMask": sysIpAuthMgrIpMask,
       "sysIpAuthMgrPortList": sysIpAuthMgrPortList,
       "sysIpAuthMgrVlanList": sysIpAuthMgrVlanList,
       "sysIpAuthMgrAllowedServices": sysIpAuthMgrAllowedServices,
       "sysIpAuthMgrRowStatus": sysIpAuthMgrRowStatus,
       "sysStormControl": sysStormControl,
       "sysStormCtrlTable": sysStormCtrlTable,
       "sysStormCtrlEntry": sysStormCtrlEntry,
       "sysStormCtrlIndex": sysStormCtrlIndex,
       "sysDlfOnOff": sysDlfOnOff,
       "sysBroadcastOnOff": sysBroadcastOnOff,
       "sysMulticastOnOff": sysMulticastOnOff,
       "sysStormCtrlThreshold": sysStormCtrlThreshold,
       "sysStormCtrlRowStatus": sysStormCtrlRowStatus,
       "sysLBDdetect": sysLBDdetect,
       "sysLBDStateEnable": sysLBDStateEnable,
       "sysLBDInterval": sysLBDInterval,
       "sysLBDRecoverTime": sysLBDRecoverTime,
       "sysLBDCtrlTable": sysLBDCtrlTable,
       "sysLBDCtrlEntry": sysLBDCtrlEntry,
       "sysLBDCtrlIndex": sysLBDCtrlIndex,
       "sysLBDPortStatus": sysLBDPortStatus,
       "sysLBDPortLoopStatus": sysLBDPortLoopStatus,
       "sysUserAuthMgr": sysUserAuthMgr,
       "sysUserAuthMgrTable": sysUserAuthMgrTable,
       "sysUserAuthMgrEntry": sysUserAuthMgrEntry,
       "sysUserAuthMgrId": sysUserAuthMgrId,
       "sysUserAuthMgrName": sysUserAuthMgrName,
       "sysUserAuthMgrRowStatus": sysUserAuthMgrRowStatus,
       "l2Dfs": l2Dfs,
       "sysDfsMIBObjects": sysDfsMIBObjects,
       "sysDfsMFClassifier": sysDfsMFClassifier,
       "sysDfsMultiFieldClfrTable": sysDfsMultiFieldClfrTable,
       "sysDfsMultiFieldClfrEntry": sysDfsMultiFieldClfrEntry,
       "sysDfsMultiFieldClfrId": sysDfsMultiFieldClfrId,
       "sysDfsMultiFieldClfrFilterId": sysDfsMultiFieldClfrFilterId,
       "sysDfsMultiFieldClfrFilterType": sysDfsMultiFieldClfrFilterType,
       "sysDfsMultiFieldClfrStatus": sysDfsMultiFieldClfrStatus,
       "sysDfsClassifier": sysDfsClassifier,
       "sysDfsClfrTable": sysDfsClfrTable,
       "sysDfsClfrEntry": sysDfsClfrEntry,
       "sysDfsClfrId": sysDfsClfrId,
       "sysDfsClfrMFClfrId": sysDfsClfrMFClfrId,
       "sysDfsClfrInProActionId": sysDfsClfrInProActionId,
       "sysDfsClfrOutProActionId": sysDfsClfrOutProActionId,
       "sysDfsClfrStatus": sysDfsClfrStatus,
       "sysDfsInProfileAction": sysDfsInProfileAction,
       "sysDfsInProfileActionTable": sysDfsInProfileActionTable,
       "sysDfsInProfileActionEntry": sysDfsInProfileActionEntry,
       "sysDfsInProfileActionId": sysDfsInProfileActionId,
       "sysDfsInProfileActionFlag": sysDfsInProfileActionFlag,
       "sysDfsInProfileActionNewPrio": sysDfsInProfileActionNewPrio,
       "sysDfsInProfileActionDscp": sysDfsInProfileActionDscp,
       "sysDfsInProfileActionStatus": sysDfsInProfileActionStatus,
       "sysDfsOutProfileAction": sysDfsOutProfileAction,
       "sysDfsOutProfileActionTable": sysDfsOutProfileActionTable,
       "sysDfsOutProfileActionEntry": sysDfsOutProfileActionEntry,
       "sysDfsOutProfileActionId": sysDfsOutProfileActionId,
       "sysDfsOutProfileActionFlag": sysDfsOutProfileActionFlag,
       "sysDfsOutProfileActionMID": sysDfsOutProfileActionMID,
       "sysDfsOutProfileActionStatus": sysDfsOutProfileActionStatus,
       "sysDfsMeter": sysDfsMeter,
       "sysDfsMeterTable": sysDfsMeterTable,
       "sysDfsMeterEntry": sysDfsMeterEntry,
       "sysDfsMeterId": sysDfsMeterId,
       "sysDfsMeterRefreshCount": sysDfsMeterRefreshCount,
       "sysDfsMeterStatus": sysDfsMeterStatus,
       "sysDfsEnterpriseCoSqAlgorithm": sysDfsEnterpriseCoSqAlgorithm,
       "sysDfsCoSqAlgorithmTable": sysDfsCoSqAlgorithmTable,
       "sysDfsCoSqAlgorithmEntry": sysDfsCoSqAlgorithmEntry,
       "sysDfsPortId": sysDfsPortId,
       "sysDfsCoSqAlgorithm": sysDfsCoSqAlgorithm,
       "l2Syslog": l2Syslog,
       "sysSyslogGeneralGroup": sysSyslogGeneralGroup,
       "sysSyslogLogging": sysSyslogLogging,
       "sysSyslogTimeStamp": sysSyslogTimeStamp,
       "sysSyslogSysBuffers": sysSyslogSysBuffers,
       "sysSyslogClearLog": sysSyslogClearLog,
       "sysSyslogConfigTable": sysSyslogConfigTable,
       "sysSyslogConfigEntry": sysSyslogConfigEntry,
       "sysSyslogConfigModule": sysSyslogConfigModule,
       "sysSyslogConfigLogLevel": sysSyslogConfigLogLevel,
       "sysSyslogFacility": sysSyslogFacility,
       "sysSyslogLogs": sysSyslogLogs,
       "sysSyslogLogSrvAddr": sysSyslogLogSrvAddr,
       "l2Security": l2Security,
       "sysPortSecurity": sysPortSecurity,
       "sysPortSecurityTable": sysPortSecurityTable,
       "sysPortSecurityEntry": sysPortSecurityEntry,
       "sysPortSecurityIndex": sysPortSecurityIndex,
       "sysPortSecurityState": sysPortSecurityState,
       "sysPortSecurityMLA": sysPortSecurityMLA,
       "l2Ssl": l2Ssl,
       "sysSslGeneralGroup": sysSslGeneralGroup,
       "sysSslSecureHttpStatus": sysSslSecureHttpStatus,
       "sysSslPort": sysSslPort,
       "sysSslTrace": sysSslTrace,
       "sysSslCiphers": sysSslCiphers,
       "sysSslCipherList": sysSslCipherList,
       "sysSslDefaultCipherList": sysSslDefaultCipherList,
       "l2Ssh": l2Ssh,
       "sysSshGeneralGroup": sysSshGeneralGroup,
       "sysSshVersionCompatibility": sysSshVersionCompatibility,
       "sysSshCipherList": sysSshCipherList,
       "sysSshMacList": sysSshMacList,
       "sysSshTrace": sysSshTrace,
       "sysSshStatus": sysSshStatus,
       "l2Sntp": l2Sntp,
       "sysSntpGeneralGroup": sysSntpGeneralGroup,
       "sysSntpStatus": sysSntpStatus,
       "sysSntpPollInterval": sysSntpPollInterval,
       "sysSntpTimeSeconds": sysSntpTimeSeconds,
       "sysSntpPrimarySrvAddr": sysSntpPrimarySrvAddr,
       "sysSntpSecondSrvAddr": sysSntpSecondSrvAddr,
       "sysSntpTimeZoneMappingIndex": sysSntpTimeZoneMappingIndex,
       "sysSntpTzGroup": sysSntpTzGroup,
       "sysSntpTzDSTStatus": sysSntpTzDSTStatus,
       "sysSntpTzMinutesWest": sysSntpTzMinutesWest,
       "sysSntpTzDSTStartMon": sysSntpTzDSTStartMon,
       "sysSntpTzDSTStartDay": sysSntpTzDSTStartDay,
       "sysSntpTzDSTStartHour": sysSntpTzDSTStartHour,
       "sysSntpTzDSTStartMinute": sysSntpTzDSTStartMinute,
       "sysSntpTzDSTEndMon": sysSntpTzDSTEndMon,
       "sysSntpTzDSTEndDay": sysSntpTzDSTEndDay,
       "sysSntpTzDSTEndHour": sysSntpTzDSTEndHour,
       "sysSntpTzDSTEndMinute": sysSntpTzDSTEndMinute,
       "sysSntpTzDSTForwardOffset": sysSntpTzDSTForwardOffset,
       "l2Dscp": l2Dscp,
       "sysDscpMIBObjects": sysDscpMIBObjects,
       "sysDscpEnable": sysDscpEnable,
       "sysDscpTypeGroup": sysDscpTypeGroup,
       "sysDscpType01": sysDscpType01,
       "sysDscpType02": sysDscpType02,
       "sysDscpType03": sysDscpType03,
       "sysDscpType04": sysDscpType04,
       "sysDscpType05": sysDscpType05,
       "sysDscpType06": sysDscpType06,
       "sysDscpType07": sysDscpType07,
       "sysDscpType08": sysDscpType08,
       "sysDscpType09": sysDscpType09,
       "sysDscpType10": sysDscpType10,
       "sysDscpType11": sysDscpType11,
       "sysDscpType12": sysDscpType12,
       "sysDscpType13": sysDscpType13,
       "sysDscpType14": sysDscpType14,
       "sysDscpType15": sysDscpType15,
       "sysDscpType16": sysDscpType16,
       "sysDscpType17": sysDscpType17,
       "sysDscpType18": sysDscpType18,
       "sysDscpType19": sysDscpType19,
       "sysDscpType20": sysDscpType20,
       "sysDscpType21": sysDscpType21,
       "sysDscpType22": sysDscpType22,
       "sysDscpType23": sysDscpType23,
       "sysDscpType24": sysDscpType24,
       "sysDscpType25": sysDscpType25,
       "sysDscpType26": sysDscpType26,
       "sysDscpType27": sysDscpType27,
       "sysDscpType28": sysDscpType28,
       "sysDscpType29": sysDscpType29,
       "sysDscpType30": sysDscpType30,
       "sysDscpType31": sysDscpType31,
       "sysDscpType32": sysDscpType32,
       "sysDscpType33": sysDscpType33,
       "sysDscpType34": sysDscpType34,
       "sysDscpType35": sysDscpType35,
       "sysDscpType36": sysDscpType36,
       "sysDscpType37": sysDscpType37,
       "sysDscpType38": sysDscpType38,
       "sysDscpType39": sysDscpType39,
       "sysDscpType40": sysDscpType40,
       "sysDscpType41": sysDscpType41,
       "sysDscpType42": sysDscpType42,
       "sysDscpType43": sysDscpType43,
       "sysDscpType44": sysDscpType44,
       "sysDscpType45": sysDscpType45,
       "sysDscpType46": sysDscpType46,
       "sysDscpType47": sysDscpType47,
       "sysDscpType48": sysDscpType48,
       "sysDscpType49": sysDscpType49,
       "sysDscpType50": sysDscpType50,
       "sysDscpType51": sysDscpType51,
       "sysDscpType52": sysDscpType52,
       "sysDscpType53": sysDscpType53,
       "sysDscpType54": sysDscpType54,
       "sysDscpType55": sysDscpType55,
       "sysDscpType56": sysDscpType56,
       "sysDscpType57": sysDscpType57,
       "sysDscpType58": sysDscpType58,
       "sysDscpType59": sysDscpType59,
       "sysDscpType60": sysDscpType60,
       "sysDscpType61": sysDscpType61,
       "sysDscpType62": sysDscpType62,
       "sysDscpType63": sysDscpType63,
       "sysDscpType64": sysDscpType64,
       "l2Snoop": l2Snoop,
       "sysSnoopInst": sysSnoopInst,
       "sysSnoopInstanceGlobalTable": sysSnoopInstanceGlobalTable,
       "sysSnoopInstanceGlobalEntry": sysSnoopInstanceGlobalEntry,
       "sysSnoopInstanceGlobalInstId": sysSnoopInstanceGlobalInstId,
       "sysSnoopInstanceGlobalSystemControl": sysSnoopInstanceGlobalSystemControl,
       "sysSnoopInstanceConfigTable": sysSnoopInstanceConfigTable,
       "sysSnoopInstanceConfigEntry": sysSnoopInstanceConfigEntry,
       "sysSnoopInstanceConfigInstId": sysSnoopInstanceConfigInstId,
       "sysSnoopInetAddressType": sysSnoopInetAddressType,
       "sysSnoopStatus": sysSnoopStatus,
       "sysSnoopRouterPortPurgeInterval": sysSnoopRouterPortPurgeInterval,
       "sysSnoopPortPurgeInterval": sysSnoopPortPurgeInterval,
       "sysSnoopReportForwardInterval": sysSnoopReportForwardInterval,
       "sysSnoopRetryCount": sysSnoopRetryCount,
       "sysSnoopGrpQueryInterval": sysSnoopGrpQueryInterval,
       "sysSnoopReportFwdOnAllPorts": sysSnoopReportFwdOnAllPorts,
       "sysSnoopOperStatus": sysSnoopOperStatus,
       "sysSnoopSendQueryOnTopoChange": sysSnoopSendQueryOnTopoChange,
       "sysSnoopQuerierQueryInterval": sysSnoopQuerierQueryInterval,
       "sysSnoopVlan": sysSnoopVlan,
       "sysSnoopVlanMcastMacFwdTable": sysSnoopVlanMcastMacFwdTable,
       "sysSnoopVlanMcastMacFwdEntry": sysSnoopVlanMcastMacFwdEntry,
       "sysSnoopVlanMcastMacFwdInstId": sysSnoopVlanMcastMacFwdInstId,
       "sysSnoopVlanMcastMacFwdVlanId": sysSnoopVlanMcastMacFwdVlanId,
       "sysSnoopVlanMcastMacFwdInetAddressType": sysSnoopVlanMcastMacFwdInetAddressType,
       "sysSnoopVlanMcastMacFwdGroupAddress": sysSnoopVlanMcastMacFwdGroupAddress,
       "sysSnoopVlanMcastMacFwdPortList": sysSnoopVlanMcastMacFwdPortList,
       "sysSnoopVlanRouterTable": sysSnoopVlanRouterTable,
       "sysSnoopVlanRouterEntry": sysSnoopVlanRouterEntry,
       "sysSnoopVlanRouterInstId": sysSnoopVlanRouterInstId,
       "sysSnoopVlanRouterVlanId": sysSnoopVlanRouterVlanId,
       "sysSnoopVlanRouterInetAddressType": sysSnoopVlanRouterInetAddressType,
       "sysSnoopVlanRouterPortList": sysSnoopVlanRouterPortList,
       "sysSnoopVlanFilterTable": sysSnoopVlanFilterTable,
       "sysSnoopVlanFilterEntry": sysSnoopVlanFilterEntry,
       "sysSnoopVlanFilterInstId": sysSnoopVlanFilterInstId,
       "sysSnoopVlanFilterVlanId": sysSnoopVlanFilterVlanId,
       "sysSnoopVlanFilterInetAddressType": sysSnoopVlanFilterInetAddressType,
       "sysSnoopVlanSnoopStatus": sysSnoopVlanSnoopStatus,
       "sysSnoopVlanOperatingVersion": sysSnoopVlanOperatingVersion,
       "sysSnoopVlanFastLeave": sysSnoopVlanFastLeave,
       "sysSnoopVlanQuerier": sysSnoopVlanQuerier,
       "sysSnoopVlanCfgQuerier": sysSnoopVlanCfgQuerier,
       "sysSnoopVlanQueryInterval": sysSnoopVlanQueryInterval,
       "sysSnoopVlanRtrPortList": sysSnoopVlanRtrPortList,
       "sysSnoopVlanRowStatus": sysSnoopVlanRowStatus,
       "sysSnoopStats": sysSnoopStats,
       "sysSnoopStatsTable": sysSnoopStatsTable,
       "sysSnoopStatsEntry": sysSnoopStatsEntry,
       "sysSnoopStatsInstId": sysSnoopStatsInstId,
       "sysSnoopStatsVlanId": sysSnoopStatsVlanId,
       "sysSnoopStatsInetAddressType": sysSnoopStatsInetAddressType,
       "sysSnoopStatsRxGenQueries": sysSnoopStatsRxGenQueries,
       "sysSnoopStatsRxGrpQueries": sysSnoopStatsRxGrpQueries,
       "sysSnoopStatsRxAsmReports": sysSnoopStatsRxAsmReports,
       "sysSnoopStatsRxAsmLeaves": sysSnoopStatsRxAsmLeaves,
       "sysSnoopStatsTxGenQueries": sysSnoopStatsTxGenQueries,
       "sysSnoopStatsTxGrpQueries": sysSnoopStatsTxGrpQueries,
       "sysSnoopStatsTxAsmReports": sysSnoopStatsTxAsmReports,
       "sysSnoopStatsTxAsmLeaves": sysSnoopStatsTxAsmLeaves,
       "sysSnoopStatsDroppedPkts": sysSnoopStatsDroppedPkts,
       "l2Bridge": l2Bridge,
       "dot1dNotifications": dot1dNotifications,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "dot1dBase": dot1dBase,
       "dot1dBaseTable": dot1dBaseTable,
       "dot1dBaseEntry": dot1dBaseEntry,
       "dot1dBaseContextId": dot1dBaseContextId,
       "dot1dBaseBridgeAddress": dot1dBaseBridgeAddress,
       "dot1dBaseNumPorts": dot1dBaseNumPorts,
       "dot1dBaseType": dot1dBaseType,
       "dot1dBasePortTable": dot1dBasePortTable,
       "dot1dBasePortEntry": dot1dBasePortEntry,
       "dot1dBasePort": dot1dBasePort,
       "dot1dBasePortIfIndex": dot1dBasePortIfIndex,
       "dot1dBasePortCircuit": dot1dBasePortCircuit,
       "dot1dBasePortDelayExceededDiscards": dot1dBasePortDelayExceededDiscards,
       "dot1dBasePortMtuExceededDiscards": dot1dBasePortMtuExceededDiscards,
       "l2Dot1dStp": l2Dot1dStp,
       "dot1dStpTable": dot1dStpTable,
       "dot1dStpEntry": dot1dStpEntry,
       "dot1dStpContextId": dot1dStpContextId,
       "dot1dStpProtocolSpecification": dot1dStpProtocolSpecification,
       "dot1dStpPriority": dot1dStpPriority,
       "dot1dStpTimeSinceTopologyChange": dot1dStpTimeSinceTopologyChange,
       "dot1dStpTopChanges": dot1dStpTopChanges,
       "dot1dStpDesignatedRoot": dot1dStpDesignatedRoot,
       "dot1dStpRootCost": dot1dStpRootCost,
       "dot1dStpRootPort": dot1dStpRootPort,
       "dot1dStpMaxAge": dot1dStpMaxAge,
       "dot1dStpHelloTime": dot1dStpHelloTime,
       "dot1dStpHoldTime": dot1dStpHoldTime,
       "dot1dStpForwardDelay": dot1dStpForwardDelay,
       "dot1dStpBridgeMaxAge": dot1dStpBridgeMaxAge,
       "dot1dStpBridgeHelloTime": dot1dStpBridgeHelloTime,
       "dot1dStpBridgeForwardDelay": dot1dStpBridgeForwardDelay,
       "dot1dStpPortTable": dot1dStpPortTable,
       "dot1dStpPortEntry": dot1dStpPortEntry,
       "dot1dStpPort": dot1dStpPort,
       "dot1dStpPortPriority": dot1dStpPortPriority,
       "dot1dStpPortState": dot1dStpPortState,
       "dot1dStpPortEnable": dot1dStpPortEnable,
       "dot1dStpPortPathCost": dot1dStpPortPathCost,
       "dot1dStpPortDesignatedRoot": dot1dStpPortDesignatedRoot,
       "dot1dStpPortDesignatedCost": dot1dStpPortDesignatedCost,
       "dot1dStpPortDesignatedBridge": dot1dStpPortDesignatedBridge,
       "dot1dStpPortDesignatedPort": dot1dStpPortDesignatedPort,
       "dot1dStpPortForwardTransitions": dot1dStpPortForwardTransitions,
       "dot1dStpExtTable": dot1dStpExtTable,
       "dot1dStpExtEntry": dot1dStpExtEntry,
       "dot1dStpVersion": dot1dStpVersion,
       "dot1dStpTxHoldCount": dot1dStpTxHoldCount,
       "dot1dStpPathCostDefault": dot1dStpPathCostDefault,
       "dot1dStpExtPortTable": dot1dStpExtPortTable,
       "dot1dStpExtPortEntry": dot1dStpExtPortEntry,
       "dot1dStpPortProtocolMigration": dot1dStpPortProtocolMigration,
       "dot1dStpPortAdminEdgePort": dot1dStpPortAdminEdgePort,
       "dot1dStpPortOperEdgePort": dot1dStpPortOperEdgePort,
       "dot1dStpPortAdminPointToPoint": dot1dStpPortAdminPointToPoint,
       "dot1dStpPortOperPointToPoint": dot1dStpPortOperPointToPoint,
       "dot1dSr": dot1dSr,
       "dot1dTp": dot1dTp,
       "dot1dTpTable": dot1dTpTable,
       "dot1dTpEntry": dot1dTpEntry,
       "dot1dTpLearnedEntryDiscards": dot1dTpLearnedEntryDiscards,
       "dot1dTpAgingTime": dot1dTpAgingTime,
       "dot1dTpFdbTable": dot1dTpFdbTable,
       "dot1dTpFdbEntry": dot1dTpFdbEntry,
       "dot1dTpFdbAddress": dot1dTpFdbAddress,
       "dot1dTpFdbPort": dot1dTpFdbPort,
       "dot1dTpFdbStatus": dot1dTpFdbStatus,
       "dot1dTpPortTable": dot1dTpPortTable,
       "dot1dTpPortEntry": dot1dTpPortEntry,
       "dot1dTpPort": dot1dTpPort,
       "dot1dTpPortMaxInfo": dot1dTpPortMaxInfo,
       "dot1dTpPortInFrames": dot1dTpPortInFrames,
       "dot1dTpPortOutFrames": dot1dTpPortOutFrames,
       "dot1dTpPortInDiscards": dot1dTpPortInDiscards,
       "dot1dTpHCPortTable": dot1dTpHCPortTable,
       "dot1dTpHCPortEntry": dot1dTpHCPortEntry,
       "dot1dTpHCPortInFrames": dot1dTpHCPortInFrames,
       "dot1dTpHCPortOutFrames": dot1dTpHCPortOutFrames,
       "dot1dTpHCPortInDiscards": dot1dTpHCPortInDiscards,
       "dot1dTpPortOverflowTable": dot1dTpPortOverflowTable,
       "dot1dTpPortOverflowEntry": dot1dTpPortOverflowEntry,
       "dot1dTpPortInOverflowFrames": dot1dTpPortInOverflowFrames,
       "dot1dTpPortOutOverflowFrames": dot1dTpPortOutOverflowFrames,
       "dot1dTpPortInOverflowDiscards": dot1dTpPortInOverflowDiscards,
       "dot1dStatic": dot1dStatic,
       "dot1dStaticTable": dot1dStaticTable,
       "dot1dStaticEntry": dot1dStaticEntry,
       "dot1dStaticAddress": dot1dStaticAddress,
       "dot1dStaticReceivePort": dot1dStaticReceivePort,
       "dot1dStaticRowStatus": dot1dStaticRowStatus,
       "dot1dStaticStatus": dot1dStaticStatus,
       "dot1dStaticAllowedToGoTable": dot1dStaticAllowedToGoTable,
       "dot1dStaticAllowedToGoEntry": dot1dStaticAllowedToGoEntry,
       "dot1dStaticAllowedIsMember": dot1dStaticAllowedIsMember,
       "dot1dPBridge": dot1dPBridge,
       "dot1dMIBObjects": dot1dMIBObjects,
       "dot1dExtBase": dot1dExtBase,
       "dot1dExtBaseTable": dot1dExtBaseTable,
       "dot1dExtBaseEntry": dot1dExtBaseEntry,
       "dot1dBridgeContextId": dot1dBridgeContextId,
       "dot1dDeviceCapabilities": dot1dDeviceCapabilities,
       "dot1dTrafficClassesEnabled": dot1dTrafficClassesEnabled,
       "dot1dGmrpStatus": dot1dGmrpStatus,
       "dot1dPortCapabilitiesTable": dot1dPortCapabilitiesTable,
       "dot1dPortCapabilitiesEntry": dot1dPortCapabilitiesEntry,
       "dot1dPortCapabilities": dot1dPortCapabilities,
       "dot1dPriority": dot1dPriority,
       "dot1dPortPriorityTable": dot1dPortPriorityTable,
       "dot1dPortPriorityEntry": dot1dPortPriorityEntry,
       "dot1dPortDefaultUserPriority": dot1dPortDefaultUserPriority,
       "dot1dPortNumTrafficClasses": dot1dPortNumTrafficClasses,
       "dot1dUserPriorityRegenTable": dot1dUserPriorityRegenTable,
       "dot1dUserPriorityRegenEntry": dot1dUserPriorityRegenEntry,
       "dot1dUserPriority": dot1dUserPriority,
       "dot1dRegenUserPriority": dot1dRegenUserPriority,
       "dot1dTrafficClassTable": dot1dTrafficClassTable,
       "dot1dTrafficClassEntry": dot1dTrafficClassEntry,
       "dot1dTrafficClassPriority": dot1dTrafficClassPriority,
       "dot1dTrafficClass": dot1dTrafficClass,
       "dot1dPortOutboundAccessPriorityTable": dot1dPortOutboundAccessPriorityTable,
       "dot1dPortOutboundAccessPriorityEntry": dot1dPortOutboundAccessPriorityEntry,
       "dot1dPortOutboundAccessPriority": dot1dPortOutboundAccessPriority,
       "dot1dGarp": dot1dGarp,
       "dot1dPortGarpTable": dot1dPortGarpTable,
       "dot1dPortGarpEntry": dot1dPortGarpEntry,
       "dot1dPortGarpJoinTime": dot1dPortGarpJoinTime,
       "dot1dPortGarpLeaveTime": dot1dPortGarpLeaveTime,
       "dot1dPortGarpLeaveAllTime": dot1dPortGarpLeaveAllTime,
       "dot1dConformance": dot1dConformance,
       "dot1dGroups": dot1dGroups,
       "dot1dExtCapGroup": dot1dExtCapGroup,
       "dot1dDeviceGmrpGroup": dot1dDeviceGmrpGroup,
       "dot1dDevicePriorityGroup": dot1dDevicePriorityGroup,
       "dot1dDefaultPriorityGroup": dot1dDefaultPriorityGroup,
       "dot1dRegenPriorityGroup": dot1dRegenPriorityGroup,
       "dot1dPriorityGroup": dot1dPriorityGroup,
       "dot1dAccessPriorityGroup": dot1dAccessPriorityGroup,
       "dot1dPortGarpGroup": dot1dPortGarpGroup,
       "dot1dHCPortGroup": dot1dHCPortGroup,
       "dot1dPortOverflowGroup": dot1dPortOverflowGroup,
       "dot1dCompliances": dot1dCompliances,
       "dot1dCompliance": dot1dCompliance,
       "dot1qQBridge": dot1qQBridge,
       "dot1qMIBObjects": dot1qMIBObjects,
       "dot1qBase": dot1qBase,
       "dot1qBaseTable": dot1qBaseTable,
       "dot1qBaseEntry": dot1qBaseEntry,
       "dot1qVlanContextId": dot1qVlanContextId,
       "dot1qVlanVersionNumber": dot1qVlanVersionNumber,
       "dot1qMaxVlanId": dot1qMaxVlanId,
       "dot1qMaxSupportedVlans": dot1qMaxSupportedVlans,
       "dot1qNumVlans": dot1qNumVlans,
       "dot1qGvrpStatus": dot1qGvrpStatus,
       "dot1qTp": dot1qTp,
       "dot1qFdbTable": dot1qFdbTable,
       "dot1qFdbEntry": dot1qFdbEntry,
       "dot1qFdbId": dot1qFdbId,
       "dot1qFdbDynamicCount": dot1qFdbDynamicCount,
       "dot1qTpFdbTable": dot1qTpFdbTable,
       "dot1qTpFdbEntry": dot1qTpFdbEntry,
       "dot1qTpFdbAddress": dot1qTpFdbAddress,
       "dot1qTpFdbPort": dot1qTpFdbPort,
       "dot1qTpFdbStatus": dot1qTpFdbStatus,
       "dot1qTpFdbPw": dot1qTpFdbPw,
       "dot1qStatic": dot1qStatic,
       "dot1qStaticUnicastTable": dot1qStaticUnicastTable,
       "dot1qStaticUnicastEntry": dot1qStaticUnicastEntry,
       "dot1qStaticUnicastAddress": dot1qStaticUnicastAddress,
       "dot1qStaticUnicastReceivePort": dot1qStaticUnicastReceivePort,
       "dot1qStaticUnicastRowStatus": dot1qStaticUnicastRowStatus,
       "dot1qStaticUnicastStatus": dot1qStaticUnicastStatus,
       "dot1qStaticAllowedToGoTable": dot1qStaticAllowedToGoTable,
       "dot1qStaticAllowedToGoEntry": dot1qStaticAllowedToGoEntry,
       "dot1qStaticAllowedIsMember": dot1qStaticAllowedIsMember,
       "dot1qTpPort": dot1qTpPort,
       "dot1qStaticMulticastTable": dot1qStaticMulticastTable,
       "dot1qStaticMulticastEntry": dot1qStaticMulticastEntry,
       "dot1qStaticMulticastAddress": dot1qStaticMulticastAddress,
       "dot1qStaticMulticastReceivePort": dot1qStaticMulticastReceivePort,
       "dot1qStaticMulticastRowStatus": dot1qStaticMulticastRowStatus,
       "dot1qStaticMulticastStatus": dot1qStaticMulticastStatus,
       "dot1qStaticMcastPortTable": dot1qStaticMcastPortTable,
       "dot1qStaticMcastPortEntry": dot1qStaticMcastPortEntry,
       "dot1qStaticMcastPort": dot1qStaticMcastPort,
       "dot1qVlanIndex": dot1qVlanIndex,
       "dot1qVlan": dot1qVlan,
       "dot1qVlanNumDeletesTable": dot1qVlanNumDeletesTable,
       "dot1qVlanNumDeletesEntry": dot1qVlanNumDeletesEntry,
       "dot1qVlanNumDeletes": dot1qVlanNumDeletes,
       "dot1qVlanCurrentTable": dot1qVlanCurrentTable,
       "dot1qVlanCurrentEntry": dot1qVlanCurrentEntry,
       "dot1qVlanTimeMark": dot1qVlanTimeMark,
       "dot1qVlanFdbId": dot1qVlanFdbId,
       "dot1qVlanStatus": dot1qVlanStatus,
       "dot1qVlanCreationTime": dot1qVlanCreationTime,
       "dot1qVlanEgressPortTable": dot1qVlanEgressPortTable,
       "dot1qVlanEgressPortEntry": dot1qVlanEgressPortEntry,
       "dot1qVlanCurrentEgressPort": dot1qVlanCurrentEgressPort,
       "dot1qVlanStaticTable": dot1qVlanStaticTable,
       "dot1qVlanStaticEntry": dot1qVlanStaticEntry,
       "dot1qVlanStaticName": dot1qVlanStaticName,
       "dot1qVlanStaticRowStatus": dot1qVlanStaticRowStatus,
       "dot1qVlanStaticPortConfigTable": dot1qVlanStaticPortConfigTable,
       "dot1qVlanStaticPortConfigEntry": dot1qVlanStaticPortConfigEntry,
       "dot1qVlanStaticPort": dot1qVlanStaticPort,
       "dot1qPortVlanTable": dot1qPortVlanTable,
       "dot1qPortVlanEntry": dot1qPortVlanEntry,
       "dot1qPvid": dot1qPvid,
       "dot1qPortAcceptableFrameTypes": dot1qPortAcceptableFrameTypes,
       "dot1qPortIngressFiltering": dot1qPortIngressFiltering,
       "dot1qPortGvrpStatus": dot1qPortGvrpStatus,
       "dot1qPortGvrpFailedRegistrations": dot1qPortGvrpFailedRegistrations,
       "dot1qPortGvrpLastPduOrigin": dot1qPortGvrpLastPduOrigin,
       "dot1qPortRestrictedVlanRegistration": dot1qPortRestrictedVlanRegistration,
       "l2Mst": l2Mst,
       "dot1sMst": dot1sMst,
       "dot1sMstTable": dot1sMstTable,
       "dot1sMstEntry": dot1sMstEntry,
       "dot1sMstContextId": dot1sMstContextId,
       "dot1sSystemControl": dot1sSystemControl,
       "dot1sModuleStatus": dot1sModuleStatus,
       "dot1sMaxMstInstanceNumber": dot1sMaxMstInstanceNumber,
       "dot1sNoOfMstiSupported": dot1sNoOfMstiSupported,
       "dot1sMaxHopCount": dot1sMaxHopCount,
       "dot1sBrgAddress": dot1sBrgAddress,
       "dot1sCistRoot": dot1sCistRoot,
       "dot1sCistRegionalRoot": dot1sCistRegionalRoot,
       "dot1sCistRootCost": dot1sCistRootCost,
       "dot1sCistRegionalRootCost": dot1sCistRegionalRootCost,
       "dot1sCistRootPort": dot1sCistRootPort,
       "dot1sCistBridgePriority": dot1sCistBridgePriority,
       "dot1sCistBridgeMaxAge": dot1sCistBridgeMaxAge,
       "dot1sCistBridgeForwardDelay": dot1sCistBridgeForwardDelay,
       "dot1sCistHoldTime": dot1sCistHoldTime,
       "dot1sCistMaxAge": dot1sCistMaxAge,
       "dot1sCistForwardDelay": dot1sCistForwardDelay,
       "dot1sMstpUpCount": dot1sMstpUpCount,
       "dot1sMstpDownCount": dot1sMstpDownCount,
       "dot1sPathCostDefaultType": dot1sPathCostDefaultType,
       "dot1sTrace": dot1sTrace,
       "dot1sDebug": dot1sDebug,
       "dot1sForceProtocolVersion": dot1sForceProtocolVersion,
       "dot1sTxHoldCount": dot1sTxHoldCount,
       "dot1sMstiConfigIdSel": dot1sMstiConfigIdSel,
       "dot1sMstiRegionName": dot1sMstiRegionName,
       "dot1sMstiRegionVersion": dot1sMstiRegionVersion,
       "dot1sMstiConfigDigest": dot1sMstiConfigDigest,
       "dot1sBufferOverFlowCount": dot1sBufferOverFlowCount,
       "dot1sMemAllocFailureCount": dot1sMemAllocFailureCount,
       "dot1sRegionConfigChangeCount": dot1sRegionConfigChangeCount,
       "dot1sCistBridgeRoleSelectionSemState": dot1sCistBridgeRoleSelectionSemState,
       "dot1sCistTimeSinceTopologyChange": dot1sCistTimeSinceTopologyChange,
       "dot1sCistTopChanges": dot1sCistTopChanges,
       "dot1sCistNewRootBridgeCount": dot1sCistNewRootBridgeCount,
       "dot1sCistHelloTime": dot1sCistHelloTime,
       "dot1sCistBridgeHelloTime": dot1sCistBridgeHelloTime,
       "dot1sCistDynamicPathcostCalculation": dot1sCistDynamicPathcostCalculation,
       "dot1sContextName": dot1sContextName,
       "dot1sMstiBridgeTable": dot1sMstiBridgeTable,
       "dot1sMstiBridgeEntry": dot1sMstiBridgeEntry,
       "dot1sMstiInstanceIndex": dot1sMstiInstanceIndex,
       "dot1sMstiBridgeRegionalRoot": dot1sMstiBridgeRegionalRoot,
       "dot1sMstiBridgePriority": dot1sMstiBridgePriority,
       "dot1sMstiRootCost": dot1sMstiRootCost,
       "dot1sMstiRootPort": dot1sMstiRootPort,
       "dot1sMstiTimeSinceTopologyChange": dot1sMstiTimeSinceTopologyChange,
       "dot1sMstiTopChanges": dot1sMstiTopChanges,
       "dot1sMstiNewRootBridgeCount": dot1sMstiNewRootBridgeCount,
       "dot1sMstiBridgeRoleSelectionSemState": dot1sMstiBridgeRoleSelectionSemState,
       "dot1sInstanceUpCount": dot1sInstanceUpCount,
       "dot1sInstanceDownCount": dot1sInstanceDownCount,
       "dot1sOldDesignatedRoot": dot1sOldDesignatedRoot,
       "dot1sVlanInstanceMappingTable": dot1sVlanInstanceMappingTable,
       "dot1sVlanInstanceMappingEntry": dot1sVlanInstanceMappingEntry,
       "dot1sInstanceIndex": dot1sInstanceIndex,
       "dot1sMapVlanIndex": dot1sMapVlanIndex,
       "dot1sUnMapVlanIndex": dot1sUnMapVlanIndex,
       "dot1sSetVlanList": dot1sSetVlanList,
       "dot1sResetVlanList": dot1sResetVlanList,
       "dot1sInstanceVlanMapped": dot1sInstanceVlanMapped,
       "dot1sInstanceVlanMapped2k": dot1sInstanceVlanMapped2k,
       "dot1sInstanceVlanMapped3k": dot1sInstanceVlanMapped3k,
       "dot1sInstanceVlanMapped4k": dot1sInstanceVlanMapped4k,
       "dot1sCistPortTable": dot1sCistPortTable,
       "dot1sCistPortEntry": dot1sCistPortEntry,
       "dot1sCistPort": dot1sCistPort,
       "dot1sCistPortPathCost": dot1sCistPortPathCost,
       "dot1sCistPortPriority": dot1sCistPortPriority,
       "dot1sCistPortDesignatedRoot": dot1sCistPortDesignatedRoot,
       "dot1sCistPortDesignatedBridge": dot1sCistPortDesignatedBridge,
       "dot1sCistPortDesignatedPort": dot1sCistPortDesignatedPort,
       "dot1sCistPortAdminP2P": dot1sCistPortAdminP2P,
       "dot1sCistPortOperP2P": dot1sCistPortOperP2P,
       "dot1sCistPortAdminEdgeStatus": dot1sCistPortAdminEdgeStatus,
       "dot1sCistPortOperEdgeStatus": dot1sCistPortOperEdgeStatus,
       "dot1sCistPortProtocolMigration": dot1sCistPortProtocolMigration,
       "dot1sCistPortState": dot1sCistPortState,
       "dot1sCistForcePortState": dot1sCistForcePortState,
       "dot1sCistPortForwardTransitions": dot1sCistPortForwardTransitions,
       "dot1sCistPortRxMstBpduCount": dot1sCistPortRxMstBpduCount,
       "dot1sCistPortRxRstBpduCount": dot1sCistPortRxRstBpduCount,
       "dot1sCistPortRxConfigBpduCount": dot1sCistPortRxConfigBpduCount,
       "dot1sCistPortRxTcnBpduCount": dot1sCistPortRxTcnBpduCount,
       "dot1sCistPortTxMstBpduCount": dot1sCistPortTxMstBpduCount,
       "dot1sCistPortTxRstBpduCount": dot1sCistPortTxRstBpduCount,
       "dot1sCistPortTxConfigBpduCount": dot1sCistPortTxConfigBpduCount,
       "dot1sCistPortTxTcnBpduCount": dot1sCistPortTxTcnBpduCount,
       "dot1sCistPortInvalidMstBpduRxCount": dot1sCistPortInvalidMstBpduRxCount,
       "dot1sCistPortInvalidRstBpduRxCount": dot1sCistPortInvalidRstBpduRxCount,
       "dot1sCistPortInvalidConfigBpduRxCount": dot1sCistPortInvalidConfigBpduRxCount,
       "dot1sCistPortInvalidTcnBpduRxCount": dot1sCistPortInvalidTcnBpduRxCount,
       "dot1sCistPortTransmitSemState": dot1sCistPortTransmitSemState,
       "dot1sCistPortReceiveSemState": dot1sCistPortReceiveSemState,
       "dot1sCistPortProtMigrationSemState": dot1sCistPortProtMigrationSemState,
       "dot1sCistProtocolMigrationCount": dot1sCistProtocolMigrationCount,
       "dot1sCistPortDesignatedCost": dot1sCistPortDesignatedCost,
       "dot1sCistPortRegionalRoot": dot1sCistPortRegionalRoot,
       "dot1sCistPortRegionalPathCost": dot1sCistPortRegionalPathCost,
       "dot1sCistSelectedPortRole": dot1sCistSelectedPortRole,
       "dot1sCistCurrentPortRole": dot1sCistCurrentPortRole,
       "dot1sCistPortInfoSemState": dot1sCistPortInfoSemState,
       "dot1sCistPortRoleTransitionSemState": dot1sCistPortRoleTransitionSemState,
       "dot1sCistPortStateTransitionSemState": dot1sCistPortStateTransitionSemState,
       "dot1sCistPortTopologyChangeSemState": dot1sCistPortTopologyChangeSemState,
       "dot1sCistPortHelloTime": dot1sCistPortHelloTime,
       "dot1sCistPortOperVersion": dot1sCistPortOperVersion,
       "dot1sCistPortEffectivePortState": dot1sCistPortEffectivePortState,
       "dot1sCistPortAutoEdgeStatus": dot1sCistPortAutoEdgeStatus,
       "dot1sCistPortRestrictedRole": dot1sCistPortRestrictedRole,
       "dot1sCistPortRestrictedTCN": dot1sCistPortRestrictedTCN,
       "dot1sMstiPortTable": dot1sMstiPortTable,
       "dot1sMstiPortEntry": dot1sMstiPortEntry,
       "dot1sMstiPort": dot1sMstiPort,
       "dot1sMstiPortPathCost": dot1sMstiPortPathCost,
       "dot1sMstiPortPriority": dot1sMstiPortPriority,
       "dot1sMstiPortDesignatedRoot": dot1sMstiPortDesignatedRoot,
       "dot1sMstiPortDesignatedBridge": dot1sMstiPortDesignatedBridge,
       "dot1sMstiPortDesignatedPort": dot1sMstiPortDesignatedPort,
       "dot1sMstiPortState": dot1sMstiPortState,
       "dot1sMstiForcePortState": dot1sMstiForcePortState,
       "dot1sMstiPortForwardTransitions": dot1sMstiPortForwardTransitions,
       "dot1sMstiPortReceivedBPDUs": dot1sMstiPortReceivedBPDUs,
       "dot1sMstiPortTransmittedBPDUs": dot1sMstiPortTransmittedBPDUs,
       "dot1sMstiPortInvalidBPDUsRcvd": dot1sMstiPortInvalidBPDUsRcvd,
       "dot1sMstiPortDesignatedCost": dot1sMstiPortDesignatedCost,
       "dot1sMstiSelectedPortRole": dot1sMstiSelectedPortRole,
       "dot1sMstiCurrentPortRole": dot1sMstiCurrentPortRole,
       "dot1sMstiPortInfoSemState": dot1sMstiPortInfoSemState,
       "dot1sMstiPortRoleTransitionSemState": dot1sMstiPortRoleTransitionSemState,
       "dot1sMstiPortStateTransitionSemState": dot1sMstiPortStateTransitionSemState,
       "dot1sMstiPortTopologyChangeSemState": dot1sMstiPortTopologyChangeSemState,
       "dot1sMstiPortEffectivePortState": dot1sMstiPortEffectivePortState,
       "dot1sMstTrapsControl": dot1sMstTrapsControl,
       "dot1sMstSetGlobalTrapOption": dot1sMstSetGlobalTrapOption,
       "dot1sGlobalErrTrapType": dot1sGlobalErrTrapType,
       "dot1sMstTrapsControlTable": dot1sMstTrapsControlTable,
       "dot1sMstTrapsControlEntry": dot1sMstTrapsControlEntry,
       "dot1sSetTraps": dot1sSetTraps,
       "dot1sGenTrapType": dot1sGenTrapType,
       "dot1sPortTrapNotificationTable": dot1sPortTrapNotificationTable,
       "dot1sPortTrapNotificationEntry": dot1sPortTrapNotificationEntry,
       "dot1sPortTrapIndex": dot1sPortTrapIndex,
       "dot1sPortMigrationType": dot1sPortMigrationType,
       "dot1sPktErrType": dot1sPktErrType,
       "dot1sPktErrVal": dot1sPktErrVal,
       "dot1sPortRoleTrapNotificationTable": dot1sPortRoleTrapNotificationTable,
       "dot1sPortRoleTrapNotificationEntry": dot1sPortRoleTrapNotificationEntry,
       "dot1sPortRoleType": dot1sPortRoleType,
       "dot1sOldRoleType": dot1sOldRoleType,
       "dot1sMstTraps": dot1sMstTraps,
       "dot1sTraps": dot1sTraps,
       "dot1sGlobalErrTrap": dot1sGlobalErrTrap,
       "dot1sGenTrap": dot1sGenTrap,
       "dot1sNewRootTrap": dot1sNewRootTrap,
       "dot1sTopologyChgTrap": dot1sTopologyChgTrap,
       "dot1sProtocolMigrationTrap": dot1sProtocolMigrationTrap,
       "dot1sInvalidBpduRxdTrap": dot1sInvalidBpduRxdTrap,
       "dot1sRegionConfigChangeTrap": dot1sRegionConfigChangeTrap,
       "dot1sNewPortRoleTrap": dot1sNewPortRoleTrap,
       "l2Rst": l2Rst,
       "dot1wRst": dot1wRst,
       "dot1wRstTable": dot1wRstTable,
       "dot1wRstEntry": dot1wRstEntry,
       "dot1wRstContextId": dot1wRstContextId,
       "dot1wSystemControl": dot1wSystemControl,
       "dot1wModuleStatus": dot1wModuleStatus,
       "dot1wTraceOption": dot1wTraceOption,
       "dot1wDebugOption": dot1wDebugOption,
       "dot1wRstpUpCount": dot1wRstpUpCount,
       "dot1wRstpDownCount": dot1wRstpDownCount,
       "dot1wBufferFailureCount": dot1wBufferFailureCount,
       "dot1wMemAllocFailureCount": dot1wMemAllocFailureCount,
       "dot1wNewRootIdCount": dot1wNewRootIdCount,
       "dot1wPortRoleSelSmState": dot1wPortRoleSelSmState,
       "dot1wOldDesignatedRoot": dot1wOldDesignatedRoot,
       "dot1wDynamicPathcostCalculation": dot1wDynamicPathcostCalculation,
       "dot1wContextName": dot1wContextName,
       "dot1wPortExtTable": dot1wPortExtTable,
       "dot1wPortExtEntry": dot1wPortExtEntry,
       "dot1wPort": dot1wPort,
       "dot1wPortRole": dot1wPortRole,
       "dot1wPortOperVersion": dot1wPortOperVersion,
       "dot1wPortInfoSmState": dot1wPortInfoSmState,
       "dot1wPortMigSmState": dot1wPortMigSmState,
       "dot1wPortRoleTransSmState": dot1wPortRoleTransSmState,
       "dot1wPortStateTransSmState": dot1wPortStateTransSmState,
       "dot1wPortTopoChSmState": dot1wPortTopoChSmState,
       "dot1wPortTxSmState": dot1wPortTxSmState,
       "dot1wPortRxRstBpduCount": dot1wPortRxRstBpduCount,
       "dot1wPortRxConfigBpduCount": dot1wPortRxConfigBpduCount,
       "dot1wPortRxTcnBpduCount": dot1wPortRxTcnBpduCount,
       "dot1wPortTxRstBpduCount": dot1wPortTxRstBpduCount,
       "dot1wPortTxConfigBpduCount": dot1wPortTxConfigBpduCount,
       "dot1wPortTxTcnBpduCount": dot1wPortTxTcnBpduCount,
       "dot1wPortInvalidRstBpduRxCount": dot1wPortInvalidRstBpduRxCount,
       "dot1wPortInvalidConfigBpduRxCount": dot1wPortInvalidConfigBpduRxCount,
       "dot1wPortInvalidTcnBpduRxCount": dot1wPortInvalidTcnBpduRxCount,
       "dot1wPortProtocolMigrationCount": dot1wPortProtocolMigrationCount,
       "dot1wPortEffectivePortState": dot1wPortEffectivePortState,
       "dot1wPortAutoEdge": dot1wPortAutoEdge,
       "dot1wPortRestrictedRole": dot1wPortRestrictedRole,
       "dot1wPortRestrictedTCN": dot1wPortRestrictedTCN,
       "dot1wRstTrapsControl": dot1wRstTrapsControl,
       "dot1wSetGlobalTraps": dot1wSetGlobalTraps,
       "dot1wGlobalErrTrapType": dot1wGlobalErrTrapType,
       "dot1wRstTrapsControlTable": dot1wRstTrapsControlTable,
       "dot1wRstTrapsControlEntry": dot1wRstTrapsControlEntry,
       "dot1wSetTraps": dot1wSetTraps,
       "dot1wGenTrapType": dot1wGenTrapType,
       "dot1wPortTrapNotificationTable": dot1wPortTrapNotificationTable,
       "dot1wPortTrapNotificationEntry": dot1wPortTrapNotificationEntry,
       "dot1wPortTrapIndex": dot1wPortTrapIndex,
       "dot1wPortMigrationType": dot1wPortMigrationType,
       "dot1wPktErrType": dot1wPktErrType,
       "dot1wPktErrVal": dot1wPktErrVal,
       "dot1wPortRoleType": dot1wPortRoleType,
       "dot1wOldRoleType": dot1wOldRoleType,
       "dot1wRstTraps": dot1wRstTraps,
       "dot1wTraps": dot1wTraps,
       "dot1wGlobalErrTrap": dot1wGlobalErrTrap,
       "dot1wGenTrap": dot1wGenTrap,
       "dot1wNewRootTrap": dot1wNewRootTrap,
       "dot1wTopologyChgTrap": dot1wTopologyChgTrap,
       "dot1wProtocolMigrationTrap": dot1wProtocolMigrationTrap,
       "dot1wInvalidBpduRxdTrap": dot1wInvalidBpduRxdTrap,
       "dot1wNewPortRoleTrap": dot1wNewPortRoleTrap,
       "l2Vlan": l2Vlan,
       "l2Dot1qVlan": l2Dot1qVlan,
       "dot1qVlanGlobalTrace": dot1qVlanGlobalTrace,
       "dot1qVlanGlobalsTable": dot1qVlanGlobalsTable,
       "dot1qVlanGlobalsEntry": dot1qVlanGlobalsEntry,
       "dot1qVlanGlobalsContextId": dot1qVlanGlobalsContextId,
       "dot1qGarpShutdownStatus": dot1qGarpShutdownStatus,
       "dot1qVlanDebug": dot1qVlanDebug,
       "dot1qVlanLearningMode": dot1qVlanLearningMode,
       "dot1qVlanOperStatus": dot1qVlanOperStatus,
       "dot1qGvrpOperStatus": dot1qGvrpOperStatus,
       "portBaseVlan": portBaseVlan,
       "portBaseVlanEnablePerPort": portBaseVlanEnablePerPort,
       "portBaseVlanCurrentTable": portBaseVlanCurrentTable,
       "tabPortBaseVlanCurrentEntry": tabPortBaseVlanCurrentEntry,
       "portBaseVlanIndex": portBaseVlanIndex,
       "portBaseVlanName": portBaseVlanName,
       "portBaseVlanCurrentEgressPorts": portBaseVlanCurrentEgressPorts,
       "portBaseVlanStatus": portBaseVlanStatus,
       "portBaseVlanCreationTime": portBaseVlanCreationTime,
       "portBaseVlanRowStatus": portBaseVlanRowStatus,
       "portBaseStatic": portBaseStatic,
       "portBaseStaticUnicastTable": portBaseStaticUnicastTable,
       "tabPortBaseStaticUnicastEntry": tabPortBaseStaticUnicastEntry,
       "portBaseStaticUnicastIndex": portBaseStaticUnicastIndex,
       "portBaseStaticUnicastVlanIndex": portBaseStaticUnicastVlanIndex,
       "portBaseStaticUnicastAddress": portBaseStaticUnicastAddress,
       "portBaseStaticUnicastAllowedToGoTo": portBaseStaticUnicastAllowedToGoTo,
       "portBaseStaticUnicastStatus": portBaseStaticUnicastStatus,
       "portBaseStaticUnicastRowStatus": portBaseStaticUnicastRowStatus,
       "portBaseStaticMulticastTable": portBaseStaticMulticastTable,
       "tabPortBaseStaticMulticastEntry": tabPortBaseStaticMulticastEntry,
       "portBaseStaticMulticastIndex": portBaseStaticMulticastIndex,
       "portBaseStaticMulticastVlanIndex": portBaseStaticMulticastVlanIndex,
       "portBaseStaticMulticastAddress": portBaseStaticMulticastAddress,
       "portBaseStaticMulticastStaticEgressPorts": portBaseStaticMulticastStaticEgressPorts,
       "portBaseStaticMulticastStatus": portBaseStaticMulticastStatus,
       "portBaseStaticMulticastRowStatus": portBaseStaticMulticastRowStatus,
       "fslldp": fslldp,
       "fsLldpSystem": fsLldpSystem,
       "fsLldpSystemControl": fsLldpSystemControl,
       "fsLldpModuleStatus": fsLldpModuleStatus,
       "fsLldpTraceInput": fsLldpTraceInput,
       "fsLldpTraceOption": fsLldpTraceOption,
       "fsLldpTLV": fsLldpTLV,
       "fsLldpLocChassisIdSubtype": fsLldpLocChassisIdSubtype,
       "fsLldpLocChassisId": fsLldpLocChassisId,
       "fsLldpLocPortTable": fsLldpLocPortTable,
       "fsLldpLocPortEntry": fsLldpLocPortEntry,
       "fsLldpLocPortIdSubtype": fsLldpLocPortIdSubtype,
       "fsLldpLocPortId": fsLldpLocPortId,
       "fsLldpPortConfigNotificationType": fsLldpPortConfigNotificationType,
       "fsLldpStatistics": fsLldpStatistics,
       "fsLldpMemAllocFailure": fsLldpMemAllocFailure,
       "fsLldpInputQOverFlows": fsLldpInputQOverFlows,
       "fsLldpStatsRemTablesUpdates": fsLldpStatsRemTablesUpdates,
       "fsLldpNotification": fsLldpNotification,
       "fsLldpTraps": fsLldpTraps,
       "fsLldpRemTablesChange": fsLldpRemTablesChange,
       "fsLldpExceedsMaxFrameSize": fsLldpExceedsMaxFrameSize,
       "fsLldpDupChasisId": fsLldpDupChasisId,
       "fsLldpDupSystemName": fsLldpDupSystemName,
       "fsLldpDupManagmentAddress": fsLldpDupManagmentAddress,
       "fsLldpMisConfigPortVlanID": fsLldpMisConfigPortVlanID,
       "fsLldpMisConfigPortProtoVlanID": fsLldpMisConfigPortProtoVlanID,
       "fsLldpMisConfigVlanName": fsLldpMisConfigVlanName,
       "fsLldpMisConfigProtocolIdentity": fsLldpMisConfigProtocolIdentity,
       "fsLldpMisConfigLinkAggStatus": fsLldpMisConfigLinkAggStatus,
       "fsLldpMisConfigPowerMDI": fsLldpMisConfigPowerMDI,
       "fsLldpMisConfigMaxFrameSize": fsLldpMisConfigMaxFrameSize,
       "fsLldpMisConfigOperMauType": fsLldpMisConfigOperMauType,
       "l2VoiceVlan": l2VoiceVlan,
       "voicevlanSystem": voicevlanSystem,
       "voiceVlanMode": voiceVlanMode,
       "voiceVlanId": voiceVlanId,
       "voiceVlanTimeout": voiceVlanTimeout,
       "voiceVlanPriority": voiceVlanPriority,
       "voicevlanPortControlTable": voicevlanPortControlTable,
       "voicevlanPortControlEntry": voicevlanPortControlEntry,
       "voicevlanPortControlIndex": voicevlanPortControlIndex,
       "voicevlanPortAutoDetection": voicevlanPortAutoDetection,
       "voicevlanPortState": voicevlanPortState,
       "voicevlanOUI": voicevlanOUI,
       "voicevlanOUITable": voicevlanOUITable,
       "voicevlanOUIEntry": voicevlanOUIEntry,
       "voicevlanOUITelephonyOUI": voicevlanOUITelephonyOUI,
       "voicevlanOUIDescription": voicevlanOUIDescription,
       "voicevlanOUIMask": voicevlanOUIMask,
       "voicevlanOUIStatus": voicevlanOUIStatus,
       "trafficSeg": trafficSeg,
       "trafficSegTable": trafficSegTable,
       "trafficSegEntry": trafficSegEntry,
       "trafficSegIfIndex": trafficSegIfIndex,
       "trafficSegMemberList": trafficSegMemberList,
       "atiAclMib": atiAclMib,
       "atiAcl": atiAcl,
       "atiAclClassifierTable": atiAclClassifierTable,
       "atiAclClassifierEntry": atiAclClassifierEntry,
       "atiAclClassifierIndex": atiAclClassifierIndex,
       "atiAclClassifierSrcMac": atiAclClassifierSrcMac,
       "atiAclClassifierSrcMacMaskLen": atiAclClassifierSrcMacMaskLen,
       "atiAclClassifierDstMac": atiAclClassifierDstMac,
       "atiAclClassifierDstMacMaskLen": atiAclClassifierDstMacMaskLen,
       "atiAclClassifierVlanId": atiAclClassifierVlanId,
       "atiAclClassifierCos": atiAclClassifierCos,
       "atiAclClassifierEtherType": atiAclClassifierEtherType,
       "atiAclClassifierSrcIp": atiAclClassifierSrcIp,
       "atiAclClassifierSrcIpMaskLen": atiAclClassifierSrcIpMaskLen,
       "atiAclClassifierDstIp": atiAclClassifierDstIp,
       "atiAclClassifierDstIpMaskLen": atiAclClassifierDstIpMaskLen,
       "atiAclClassifierDscp": atiAclClassifierDscp,
       "atiAclClassifierProtocol": atiAclClassifierProtocol,
       "atiAclClassifierSrcPort": atiAclClassifierSrcPort,
       "atiAclClassifierDstPort": atiAclClassifierDstPort,
       "atiAclClassifierRowStatus": atiAclClassifierRowStatus,
       "atiAclProfileActionTable": atiAclProfileActionTable,
       "atiAclProfileActionEntry": atiAclProfileActionEntry,
       "atiAclProfileActionIndex": atiAclProfileActionIndex,
       "atiAclProfileActionCos": atiAclProfileActionCos,
       "atiAclProfileActionDscp": atiAclProfileActionDscp,
       "atiAclProfileActionRowStatus": atiAclProfileActionRowStatus,
       "atiAclInProfileActionTable": atiAclInProfileActionTable,
       "atiAclInProfileActionEntry": atiAclInProfileActionEntry,
       "atiAclInProfileActionIndex": atiAclInProfileActionIndex,
       "atiAclInProfileActionPermitDeny": atiAclInProfileActionPermitDeny,
       "atiAclInProfileActionActionId": atiAclInProfileActionActionId,
       "atiAclInProfileActionRowStatus": atiAclInProfileActionRowStatus,
       "atiAclOutProfileActionTable": atiAclOutProfileActionTable,
       "atiAclOutProfileActionEntry": atiAclOutProfileActionEntry,
       "atiAclOutProfileActionIndex": atiAclOutProfileActionIndex,
       "atiAclOutProfileActionPermitDeny": atiAclOutProfileActionPermitDeny,
       "atiAclOutProfileActionCommittedRate": atiAclOutProfileActionCommittedRate,
       "atiAclOutProfileActionBurstSize": atiAclOutProfileActionBurstSize,
       "atiAclOutProfileActionActionId": atiAclOutProfileActionActionId,
       "atiAclOutProfileActionRowStatus": atiAclOutProfileActionRowStatus,
       "atiAclPortListTable": atiAclPortListTable,
       "atiAclPortListEntry": atiAclPortListEntry,
       "atiAclPortListIndex": atiAclPortListIndex,
       "atiAclPortListString": atiAclPortListString,
       "atiAclPortListRowStatus": atiAclPortListRowStatus,
       "atiAclPolicyTable": atiAclPolicyTable,
       "atiAclPolicyEntry": atiAclPolicyEntry,
       "atiAclPolicyIndex": atiAclPolicyIndex,
       "atiAclPolicyClassifierIndex": atiAclPolicyClassifierIndex,
       "atiAclPolicySequence": atiAclPolicySequence,
       "atiAclPolicyInProfileIndex": atiAclPolicyInProfileIndex,
       "atiAclPolicyOutProfileIndex": atiAclPolicyOutProfileIndex,
       "atiAclPolicyPortListIndex": atiAclPolicyPortListIndex,
       "atiAclPolicyRowStatus": atiAclPolicyRowStatus,
       "atiMacFilter": atiMacFilter,
       "atiDstMacFilterTable": atiDstMacFilterTable,
       "atiDstMacFilterEntry": atiDstMacFilterEntry,
       "atiDstMacFilterIndex": atiDstMacFilterIndex,
       "atiDstMacFilterAddress": atiDstMacFilterAddress,
       "atiDstMacFilterRowStatus": atiDstMacFilterRowStatus,
       "l2DhcpSnoop": l2DhcpSnoop,
       "dhcpSnoopSystemStatus": dhcpSnoopSystemStatus,
       "dhcpSnoopOption82Insertion": dhcpSnoopOption82Insertion,
       "dhcpSnoopPassThroughOption82": dhcpSnoopPassThroughOption82,
       "dhcpSnoopVerifyMACAddress": dhcpSnoopVerifyMACAddress,
       "dhcpSnoopBackupDatabase": dhcpSnoopBackupDatabase,
       "dhcpSnoopBackupDatabaseInterval": dhcpSnoopBackupDatabaseInterval,
       "dhcpSnoopVLANSettingTable": dhcpSnoopVLANSettingTable,
       "dhcpSnoopVLANSettingEntry": dhcpSnoopVLANSettingEntry,
       "dhcpSnoopVLANSettingVID": dhcpSnoopVLANSettingVID,
       "dhcpSnoopVLANSettingStatus": dhcpSnoopVLANSettingStatus,
       "dhcpSnoopPortSettingTable": dhcpSnoopPortSettingTable,
       "dhcpSnoopPortSettingEntry": dhcpSnoopPortSettingEntry,
       "dhcpSnoopPortSettingIndex": dhcpSnoopPortSettingIndex,
       "dhcpSnoopPortSettingStatus": dhcpSnoopPortSettingStatus,
       "dhcpSnoopBindindDatabaseTable": dhcpSnoopBindindDatabaseTable,
       "dhcpSnoopBindindDatabaseEntry": dhcpSnoopBindindDatabaseEntry,
       "dhcpSnoopBindindDBMacAddress": dhcpSnoopBindindDBMacAddress,
       "dhcpSnoopBindindDBVLANID": dhcpSnoopBindindDBVLANID,
       "dhcpSnoopBindindDBIPAddress": dhcpSnoopBindindDBIPAddress,
       "dhcpSnoopBindindDBPortNumber": dhcpSnoopBindindDBPortNumber,
       "dhcpSnoopBindindDBType": dhcpSnoopBindindDBType,
       "dhcpSnoopBindindDBLeaseTime": dhcpSnoopBindindDBLeaseTime,
       "dhcpSnoopBindindDBRowStatus": dhcpSnoopBindindDBRowStatus}
)
