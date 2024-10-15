# SNMP MIB module (ENTERASYS-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:52 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

etsysFirewallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37)
)
etsysFirewallMIB.setRevisions(
        ("2004-11-17 22:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysFWConfigurationObjects_ObjectIdentity = ObjectIdentity
etsysFWConfigurationObjects = _EtsysFWConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1)
)
_EtsysFWFirewallEnabled_Type = TruthValue
_EtsysFWFirewallEnabled_Object = MibScalar
etsysFWFirewallEnabled = _EtsysFWFirewallEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 1),
    _EtsysFWFirewallEnabled_Type()
)
etsysFWFirewallEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWFirewallEnabled.setStatus("current")


class _EtsysFWTcpTimeout_Type(Unsigned32):
    """Custom type etsysFWTcpTimeout based on Unsigned32"""
    defaultValue = 1200


_EtsysFWTcpTimeout_Object = MibScalar
etsysFWTcpTimeout = _EtsysFWTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 2),
    _EtsysFWTcpTimeout_Type()
)
etsysFWTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWTcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysFWTcpTimeout.setUnits("seconds")


class _EtsysFWUdpTimeout_Type(Unsigned32):
    """Custom type etsysFWUdpTimeout based on Unsigned32"""
    defaultValue = 600


_EtsysFWUdpTimeout_Object = MibScalar
etsysFWUdpTimeout = _EtsysFWUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 3),
    _EtsysFWUdpTimeout_Type()
)
etsysFWUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWUdpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysFWUdpTimeout.setUnits("seconds")


class _EtsysFWIcmpTimeout_Type(Unsigned32):
    """Custom type etsysFWIcmpTimeout based on Unsigned32"""
    defaultValue = 60


_EtsysFWIcmpTimeout_Object = MibScalar
etsysFWIcmpTimeout = _EtsysFWIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 4),
    _EtsysFWIcmpTimeout_Type()
)
etsysFWIcmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWIcmpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysFWIcmpTimeout.setUnits("seconds")


class _EtsysFWAuthTimeout_Type(Unsigned32):
    """Custom type etsysFWAuthTimeout based on Unsigned32"""
    defaultValue = 60


_EtsysFWAuthTimeout_Object = MibScalar
etsysFWAuthTimeout = _EtsysFWAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 5),
    _EtsysFWAuthTimeout_Type()
)
etsysFWAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWAuthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysFWAuthTimeout.setUnits("seconds")


class _EtsysFWAuthPort_Type(Integer32):
    """Custom type etsysFWAuthPort based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_EtsysFWAuthPort_Type.__name__ = "Integer32"
_EtsysFWAuthPort_Object = MibScalar
etsysFWAuthPort = _EtsysFWAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 6),
    _EtsysFWAuthPort_Type()
)
etsysFWAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWAuthPort.setStatus("current")


class _EtsysFWLoggingThreshold_Type(Integer32):
    """Custom type etsysFWLoggingThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EtsysFWLoggingThreshold_Type.__name__ = "Integer32"
_EtsysFWLoggingThreshold_Object = MibScalar
etsysFWLoggingThreshold = _EtsysFWLoggingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 7),
    _EtsysFWLoggingThreshold_Type()
)
etsysFWLoggingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWLoggingThreshold.setStatus("current")


class _EtsysFWRPCMicrosoftTimeout_Type(Unsigned32):
    """Custom type etsysFWRPCMicrosoftTimeout based on Unsigned32"""
    defaultValue = 3


_EtsysFWRPCMicrosoftTimeout_Object = MibScalar
etsysFWRPCMicrosoftTimeout = _EtsysFWRPCMicrosoftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 8),
    _EtsysFWRPCMicrosoftTimeout_Type()
)
etsysFWRPCMicrosoftTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWRPCMicrosoftTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysFWRPCMicrosoftTimeout.setUnits("seconds")


class _EtsysFWRPCSunTimeout_Type(Unsigned32):
    """Custom type etsysFWRPCSunTimeout based on Unsigned32"""
    defaultValue = 3


_EtsysFWRPCSunTimeout_Object = MibScalar
etsysFWRPCSunTimeout = _EtsysFWRPCSunTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 9),
    _EtsysFWRPCSunTimeout_Type()
)
etsysFWRPCSunTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWRPCSunTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysFWRPCSunTimeout.setUnits("seconds")
_EtsysFWFirewallOnIntfLastChange_Type = TimeStamp
_EtsysFWFirewallOnIntfLastChange_Object = MibScalar
etsysFWFirewallOnIntfLastChange = _EtsysFWFirewallOnIntfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 10),
    _EtsysFWFirewallOnIntfLastChange_Type()
)
etsysFWFirewallOnIntfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWFirewallOnIntfLastChange.setStatus("current")
_EtsysFWFirewallOnIntfTable_Object = MibTable
etsysFWFirewallOnIntfTable = _EtsysFWFirewallOnIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 11)
)
if mibBuilder.loadTexts:
    etsysFWFirewallOnIntfTable.setStatus("current")
_EtsysFWFirewallOnIntfEntry_Object = MibTableRow
etsysFWFirewallOnIntfEntry = _EtsysFWFirewallOnIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 11, 1)
)
etsysFWFirewallOnIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysFWFirewallOnIntfEntry.setStatus("current")


class _EtsysFWFirewallOnIntfEnabled_Type(TruthValue):
    """Custom type etsysFWFirewallOnIntfEnabled based on TruthValue"""


_EtsysFWFirewallOnIntfEnabled_Object = MibTableColumn
etsysFWFirewallOnIntfEnabled = _EtsysFWFirewallOnIntfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 11, 1, 1),
    _EtsysFWFirewallOnIntfEnabled_Type()
)
etsysFWFirewallOnIntfEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFirewallOnIntfEnabled.setStatus("current")


class _EtsysFWFirewallOnIntfStorageType_Type(StorageType):
    """Custom type etsysFWFirewallOnIntfStorageType based on StorageType"""


_EtsysFWFirewallOnIntfStorageType_Object = MibTableColumn
etsysFWFirewallOnIntfStorageType = _EtsysFWFirewallOnIntfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 11, 1, 2),
    _EtsysFWFirewallOnIntfStorageType_Type()
)
etsysFWFirewallOnIntfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFirewallOnIntfStorageType.setStatus("current")
_EtsysFWFirewallOnIntfRowStatus_Type = RowStatus
_EtsysFWFirewallOnIntfRowStatus_Object = MibTableColumn
etsysFWFirewallOnIntfRowStatus = _EtsysFWFirewallOnIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 11, 1, 3),
    _EtsysFWFirewallOnIntfRowStatus_Type()
)
etsysFWFirewallOnIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFirewallOnIntfRowStatus.setStatus("current")
_EtsysFWFirewallIntfFilterLastChange_Type = TimeStamp
_EtsysFWFirewallIntfFilterLastChange_Object = MibScalar
etsysFWFirewallIntfFilterLastChange = _EtsysFWFirewallIntfFilterLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 12),
    _EtsysFWFirewallIntfFilterLastChange_Type()
)
etsysFWFirewallIntfFilterLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterLastChange.setStatus("current")
_EtsysFWFirewallIntfFilterTable_Object = MibTable
etsysFWFirewallIntfFilterTable = _EtsysFWFirewallIntfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 13)
)
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterTable.setStatus("current")
_EtsysFWFirewallIntfFilterEntry_Object = MibTableRow
etsysFWFirewallIntfFilterEntry = _EtsysFWFirewallIntfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 13, 1)
)
etsysFWFirewallIntfFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWFirewallIntfFilterType"),
)
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterEntry.setStatus("current")


class _EtsysFWFirewallIntfFilterType_Type(Integer32):
    """Custom type etsysFWFirewallIntfFilterType based on Integer32"""
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
        *(("ipBroadcast", 1),
          ("ipMulticast", 2),
          ("ipOptionAll", 3),
          ("ipOptionLooseSourceRoute", 5),
          ("ipOptionOther", 4),
          ("ipOptionRecordRoute", 6),
          ("ipOptionStrictSourceRoute", 7),
          ("ipOptionTimeStamp", 8))
    )


_EtsysFWFirewallIntfFilterType_Type.__name__ = "Integer32"
_EtsysFWFirewallIntfFilterType_Object = MibTableColumn
etsysFWFirewallIntfFilterType = _EtsysFWFirewallIntfFilterType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 13, 1, 1),
    _EtsysFWFirewallIntfFilterType_Type()
)
etsysFWFirewallIntfFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterType.setStatus("current")


class _EtsysFWFirewallIntfFilterDirection_Type(Integer32):
    """Custom type etsysFWFirewallIntfFilterDirection based on Integer32"""
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
        *(("both", 4),
          ("in", 2),
          ("none", 1),
          ("out", 3))
    )


_EtsysFWFirewallIntfFilterDirection_Type.__name__ = "Integer32"
_EtsysFWFirewallIntfFilterDirection_Object = MibTableColumn
etsysFWFirewallIntfFilterDirection = _EtsysFWFirewallIntfFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 13, 1, 2),
    _EtsysFWFirewallIntfFilterDirection_Type()
)
etsysFWFirewallIntfFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterDirection.setStatus("current")


class _EtsysFWFirewallIntfFilterStorageType_Type(StorageType):
    """Custom type etsysFWFirewallIntfFilterStorageType based on StorageType"""


_EtsysFWFirewallIntfFilterStorageType_Object = MibTableColumn
etsysFWFirewallIntfFilterStorageType = _EtsysFWFirewallIntfFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 13, 1, 3),
    _EtsysFWFirewallIntfFilterStorageType_Type()
)
etsysFWFirewallIntfFilterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterStorageType.setStatus("current")
_EtsysFWFirewallIntfFilterRowStatus_Type = RowStatus
_EtsysFWFirewallIntfFilterRowStatus_Object = MibTableColumn
etsysFWFirewallIntfFilterRowStatus = _EtsysFWFirewallIntfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 1, 13, 1, 4),
    _EtsysFWFirewallIntfFilterRowStatus_Type()
)
etsysFWFirewallIntfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFirewallIntfFilterRowStatus.setStatus("current")
_EtsysFWPolicyObjects_ObjectIdentity = ObjectIdentity
etsysFWPolicyObjects = _EtsysFWPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2)
)
_EtsysFWPolicyGroups_ObjectIdentity = ObjectIdentity
etsysFWPolicyGroups = _EtsysFWPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1)
)


class _EtsysFWSystemPolicyGroupName_Type(SnmpAdminString):
    """Custom type etsysFWSystemPolicyGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysFWSystemPolicyGroupName_Type.__name__ = "SnmpAdminString"
_EtsysFWSystemPolicyGroupName_Object = MibScalar
etsysFWSystemPolicyGroupName = _EtsysFWSystemPolicyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 1),
    _EtsysFWSystemPolicyGroupName_Type()
)
etsysFWSystemPolicyGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFWSystemPolicyGroupName.setStatus("current")
_EtsysFWIntfToGroupLastChange_Type = TimeStamp
_EtsysFWIntfToGroupLastChange_Object = MibScalar
etsysFWIntfToGroupLastChange = _EtsysFWIntfToGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 2),
    _EtsysFWIntfToGroupLastChange_Type()
)
etsysFWIntfToGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIntfToGroupLastChange.setStatus("current")
_EtsysFWIntfToGroupTable_Object = MibTable
etsysFWIntfToGroupTable = _EtsysFWIntfToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysFWIntfToGroupTable.setStatus("current")
_EtsysFWIntfToGroupEntry_Object = MibTableRow
etsysFWIntfToGroupEntry = _EtsysFWIntfToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 3, 1)
)
etsysFWIntfToGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWIntfToGroupIntfDirection"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWIntfToGroupName"),
)
if mibBuilder.loadTexts:
    etsysFWIntfToGroupEntry.setStatus("current")


class _EtsysFWIntfToGroupIntfDirection_Type(Integer32):
    """Custom type etsysFWIntfToGroupIntfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_EtsysFWIntfToGroupIntfDirection_Type.__name__ = "Integer32"
_EtsysFWIntfToGroupIntfDirection_Object = MibTableColumn
etsysFWIntfToGroupIntfDirection = _EtsysFWIntfToGroupIntfDirection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 3, 1, 1),
    _EtsysFWIntfToGroupIntfDirection_Type()
)
etsysFWIntfToGroupIntfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWIntfToGroupIntfDirection.setStatus("current")


class _EtsysFWIntfToGroupName_Type(SnmpAdminString):
    """Custom type etsysFWIntfToGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWIntfToGroupName_Type.__name__ = "SnmpAdminString"
_EtsysFWIntfToGroupName_Object = MibTableColumn
etsysFWIntfToGroupName = _EtsysFWIntfToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 3, 1, 2),
    _EtsysFWIntfToGroupName_Type()
)
etsysFWIntfToGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWIntfToGroupName.setStatus("current")


class _EtsysFWIntfToGroupStorageType_Type(StorageType):
    """Custom type etsysFWIntfToGroupStorageType based on StorageType"""


_EtsysFWIntfToGroupStorageType_Object = MibTableColumn
etsysFWIntfToGroupStorageType = _EtsysFWIntfToGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 3, 1, 3),
    _EtsysFWIntfToGroupStorageType_Type()
)
etsysFWIntfToGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWIntfToGroupStorageType.setStatus("current")
_EtsysFWIntfToGroupRowStatus_Type = RowStatus
_EtsysFWIntfToGroupRowStatus_Object = MibTableColumn
etsysFWIntfToGroupRowStatus = _EtsysFWIntfToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 3, 1, 4),
    _EtsysFWIntfToGroupRowStatus_Type()
)
etsysFWIntfToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWIntfToGroupRowStatus.setStatus("current")
_EtsysFWGroupPolicyLastChange_Type = TimeStamp
_EtsysFWGroupPolicyLastChange_Object = MibScalar
etsysFWGroupPolicyLastChange = _EtsysFWGroupPolicyLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 4),
    _EtsysFWGroupPolicyLastChange_Type()
)
etsysFWGroupPolicyLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWGroupPolicyLastChange.setStatus("current")
_EtsysFWGroupPolicyTable_Object = MibTable
etsysFWGroupPolicyTable = _EtsysFWGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5)
)
if mibBuilder.loadTexts:
    etsysFWGroupPolicyTable.setStatus("current")
_EtsysFWGroupPolicyEntry_Object = MibTableRow
etsysFWGroupPolicyEntry = _EtsysFWGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5, 1)
)
etsysFWGroupPolicyEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWGroupPolicyName"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWGroupPolicyRuleDef"),
)
if mibBuilder.loadTexts:
    etsysFWGroupPolicyEntry.setStatus("current")


class _EtsysFWGroupPolicyName_Type(SnmpAdminString):
    """Custom type etsysFWGroupPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWGroupPolicyName_Type.__name__ = "SnmpAdminString"
_EtsysFWGroupPolicyName_Object = MibTableColumn
etsysFWGroupPolicyName = _EtsysFWGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5, 1, 1),
    _EtsysFWGroupPolicyName_Type()
)
etsysFWGroupPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWGroupPolicyName.setStatus("current")
_EtsysFWGroupPolicyRuleDef_Type = SnmpAdminString
_EtsysFWGroupPolicyRuleDef_Object = MibTableColumn
etsysFWGroupPolicyRuleDef = _EtsysFWGroupPolicyRuleDef_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5, 1, 2),
    _EtsysFWGroupPolicyRuleDef_Type()
)
etsysFWGroupPolicyRuleDef.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWGroupPolicyRuleDef.setStatus("current")


class _EtsysFWGroupPolicyPriority_Type(Integer32):
    """Custom type etsysFWGroupPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysFWGroupPolicyPriority_Type.__name__ = "Integer32"
_EtsysFWGroupPolicyPriority_Object = MibTableColumn
etsysFWGroupPolicyPriority = _EtsysFWGroupPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5, 1, 3),
    _EtsysFWGroupPolicyPriority_Type()
)
etsysFWGroupPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWGroupPolicyPriority.setStatus("current")


class _EtsysFWGroupPolicyStorageType_Type(StorageType):
    """Custom type etsysFWGroupPolicyStorageType based on StorageType"""


_EtsysFWGroupPolicyStorageType_Object = MibTableColumn
etsysFWGroupPolicyStorageType = _EtsysFWGroupPolicyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5, 1, 4),
    _EtsysFWGroupPolicyStorageType_Type()
)
etsysFWGroupPolicyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWGroupPolicyStorageType.setStatus("current")
_EtsysFWGroupPolicyRowStatus_Type = RowStatus
_EtsysFWGroupPolicyRowStatus_Object = MibTableColumn
etsysFWGroupPolicyRowStatus = _EtsysFWGroupPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 1, 5, 1, 5),
    _EtsysFWGroupPolicyRowStatus_Type()
)
etsysFWGroupPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWGroupPolicyRowStatus.setStatus("current")
_EtsysFWPolicyRules_ObjectIdentity = ObjectIdentity
etsysFWPolicyRules = _EtsysFWPolicyRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2)
)


class _EtsysFWPolicyRuleDefMaxEntries_Type(Integer32):
    """Custom type etsysFWPolicyRuleDefMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWPolicyRuleDefMaxEntries_Type.__name__ = "Integer32"
_EtsysFWPolicyRuleDefMaxEntries_Object = MibScalar
etsysFWPolicyRuleDefMaxEntries = _EtsysFWPolicyRuleDefMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 1),
    _EtsysFWPolicyRuleDefMaxEntries_Type()
)
etsysFWPolicyRuleDefMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefMaxEntries.setStatus("current")
_EtsysFWPolicyRuleDefNumEntries_Type = Gauge32
_EtsysFWPolicyRuleDefNumEntries_Object = MibScalar
etsysFWPolicyRuleDefNumEntries = _EtsysFWPolicyRuleDefNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 2),
    _EtsysFWPolicyRuleDefNumEntries_Type()
)
etsysFWPolicyRuleDefNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefNumEntries.setStatus("current")
_EtsysFWPolicyRuleDefLastChange_Type = TimeStamp
_EtsysFWPolicyRuleDefLastChange_Object = MibScalar
etsysFWPolicyRuleDefLastChange = _EtsysFWPolicyRuleDefLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 3),
    _EtsysFWPolicyRuleDefLastChange_Type()
)
etsysFWPolicyRuleDefLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefLastChange.setStatus("current")
_EtsysFWPolicyRuleDefTable_Object = MibTable
etsysFWPolicyRuleDefTable = _EtsysFWPolicyRuleDefTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4)
)
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefTable.setStatus("current")
_EtsysFWPolicyRuleDefEntry_Object = MibTableRow
etsysFWPolicyRuleDefEntry = _EtsysFWPolicyRuleDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1)
)
etsysFWPolicyRuleDefEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefName"),
)
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefEntry.setStatus("current")


class _EtsysFWPolicyRuleDefName_Type(SnmpAdminString):
    """Custom type etsysFWPolicyRuleDefName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWPolicyRuleDefName_Type.__name__ = "SnmpAdminString"
_EtsysFWPolicyRuleDefName_Object = MibTableColumn
etsysFWPolicyRuleDefName = _EtsysFWPolicyRuleDefName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 1),
    _EtsysFWPolicyRuleDefName_Type()
)
etsysFWPolicyRuleDefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefName.setStatus("current")
_EtsysFWPolicyRuleDefSrcNetwork_Type = VariablePointer
_EtsysFWPolicyRuleDefSrcNetwork_Object = MibTableColumn
etsysFWPolicyRuleDefSrcNetwork = _EtsysFWPolicyRuleDefSrcNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 2),
    _EtsysFWPolicyRuleDefSrcNetwork_Type()
)
etsysFWPolicyRuleDefSrcNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefSrcNetwork.setStatus("current")
_EtsysFWPolicyRuleDefDstNetwork_Type = VariablePointer
_EtsysFWPolicyRuleDefDstNetwork_Object = MibTableColumn
etsysFWPolicyRuleDefDstNetwork = _EtsysFWPolicyRuleDefDstNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 3),
    _EtsysFWPolicyRuleDefDstNetwork_Type()
)
etsysFWPolicyRuleDefDstNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefDstNetwork.setStatus("current")


class _EtsysFWPolicyRuleDefBidirectional_Type(TruthValue):
    """Custom type etsysFWPolicyRuleDefBidirectional based on TruthValue"""


_EtsysFWPolicyRuleDefBidirectional_Object = MibTableColumn
etsysFWPolicyRuleDefBidirectional = _EtsysFWPolicyRuleDefBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 4),
    _EtsysFWPolicyRuleDefBidirectional_Type()
)
etsysFWPolicyRuleDefBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefBidirectional.setStatus("current")
_EtsysFWPolicyRuleDefService_Type = VariablePointer
_EtsysFWPolicyRuleDefService_Object = MibTableColumn
etsysFWPolicyRuleDefService = _EtsysFWPolicyRuleDefService_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 5),
    _EtsysFWPolicyRuleDefService_Type()
)
etsysFWPolicyRuleDefService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefService.setStatus("current")
_EtsysFWPolicyRuleAuthName_Type = SnmpAdminString
_EtsysFWPolicyRuleAuthName_Object = MibTableColumn
etsysFWPolicyRuleAuthName = _EtsysFWPolicyRuleAuthName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 6),
    _EtsysFWPolicyRuleAuthName_Type()
)
etsysFWPolicyRuleAuthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleAuthName.setStatus("current")


class _EtsysFWPolicyRuleDefAction_Type(Integer32):
    """Custom type etsysFWPolicyRuleDefAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("allowAuth", 2),
          ("drop", 3))
    )


_EtsysFWPolicyRuleDefAction_Type.__name__ = "Integer32"
_EtsysFWPolicyRuleDefAction_Object = MibTableColumn
etsysFWPolicyRuleDefAction = _EtsysFWPolicyRuleDefAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 7),
    _EtsysFWPolicyRuleDefAction_Type()
)
etsysFWPolicyRuleDefAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefAction.setStatus("current")


class _EtsysFWPolicyRuleDefLogging_Type(TruthValue):
    """Custom type etsysFWPolicyRuleDefLogging based on TruthValue"""


_EtsysFWPolicyRuleDefLogging_Object = MibTableColumn
etsysFWPolicyRuleDefLogging = _EtsysFWPolicyRuleDefLogging_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 8),
    _EtsysFWPolicyRuleDefLogging_Type()
)
etsysFWPolicyRuleDefLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefLogging.setStatus("current")


class _EtsysFWPolicyRuleDefStorageType_Type(StorageType):
    """Custom type etsysFWPolicyRuleDefStorageType based on StorageType"""


_EtsysFWPolicyRuleDefStorageType_Object = MibTableColumn
etsysFWPolicyRuleDefStorageType = _EtsysFWPolicyRuleDefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 9),
    _EtsysFWPolicyRuleDefStorageType_Type()
)
etsysFWPolicyRuleDefStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefStorageType.setStatus("current")
_EtsysFWPolicyRuleDefRowStatus_Type = RowStatus
_EtsysFWPolicyRuleDefRowStatus_Object = MibTableColumn
etsysFWPolicyRuleDefRowStatus = _EtsysFWPolicyRuleDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 2, 4, 1, 10),
    _EtsysFWPolicyRuleDefRowStatus_Type()
)
etsysFWPolicyRuleDefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefRowStatus.setStatus("current")
_EtsysFWPolicyNetworks_ObjectIdentity = ObjectIdentity
etsysFWPolicyNetworks = _EtsysFWPolicyNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3)
)


class _EtsysFWNetworkGroupMaxEntries_Type(Integer32):
    """Custom type etsysFWNetworkGroupMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWNetworkGroupMaxEntries_Type.__name__ = "Integer32"
_EtsysFWNetworkGroupMaxEntries_Object = MibScalar
etsysFWNetworkGroupMaxEntries = _EtsysFWNetworkGroupMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 1),
    _EtsysFWNetworkGroupMaxEntries_Type()
)
etsysFWNetworkGroupMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupMaxEntries.setStatus("current")
_EtsysFWNetworkGroupNumEntries_Type = Gauge32
_EtsysFWNetworkGroupNumEntries_Object = MibScalar
etsysFWNetworkGroupNumEntries = _EtsysFWNetworkGroupNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 2),
    _EtsysFWNetworkGroupNumEntries_Type()
)
etsysFWNetworkGroupNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupNumEntries.setStatus("current")
_EtsysFWNetworkGroupLastChange_Type = TimeStamp
_EtsysFWNetworkGroupLastChange_Object = MibScalar
etsysFWNetworkGroupLastChange = _EtsysFWNetworkGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 3),
    _EtsysFWNetworkGroupLastChange_Type()
)
etsysFWNetworkGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupLastChange.setStatus("current")
_EtsysFWNetworkGroupTable_Object = MibTable
etsysFWNetworkGroupTable = _EtsysFWNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 4)
)
if mibBuilder.loadTexts:
    etsysFWNetworkGroupTable.setStatus("current")
_EtsysFWNetworkGroupEntry_Object = MibTableRow
etsysFWNetworkGroupEntry = _EtsysFWNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 4, 1)
)
etsysFWNetworkGroupEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupName"),
)
if mibBuilder.loadTexts:
    etsysFWNetworkGroupEntry.setStatus("current")


class _EtsysFWNetworkGroupName_Type(SnmpAdminString):
    """Custom type etsysFWNetworkGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWNetworkGroupName_Type.__name__ = "SnmpAdminString"
_EtsysFWNetworkGroupName_Object = MibTableColumn
etsysFWNetworkGroupName = _EtsysFWNetworkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 4, 1, 1),
    _EtsysFWNetworkGroupName_Type()
)
etsysFWNetworkGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupName.setStatus("current")


class _EtsysFWNetworkGroupStorageType_Type(StorageType):
    """Custom type etsysFWNetworkGroupStorageType based on StorageType"""


_EtsysFWNetworkGroupStorageType_Object = MibTableColumn
etsysFWNetworkGroupStorageType = _EtsysFWNetworkGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 4, 1, 2),
    _EtsysFWNetworkGroupStorageType_Type()
)
etsysFWNetworkGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupStorageType.setStatus("current")
_EtsysFWNetworkGroupRowStatus_Type = RowStatus
_EtsysFWNetworkGroupRowStatus_Object = MibTableColumn
etsysFWNetworkGroupRowStatus = _EtsysFWNetworkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 4, 1, 3),
    _EtsysFWNetworkGroupRowStatus_Type()
)
etsysFWNetworkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupRowStatus.setStatus("current")


class _EtsysFWNetworkGroupMaxNetworks_Type(Integer32):
    """Custom type etsysFWNetworkGroupMaxNetworks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWNetworkGroupMaxNetworks_Type.__name__ = "Integer32"
_EtsysFWNetworkGroupMaxNetworks_Object = MibScalar
etsysFWNetworkGroupMaxNetworks = _EtsysFWNetworkGroupMaxNetworks_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 5),
    _EtsysFWNetworkGroupMaxNetworks_Type()
)
etsysFWNetworkGroupMaxNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkGroupMaxNetworks.setStatus("current")
_EtsysFWNetwkInNetGrpLastChange_Type = TimeStamp
_EtsysFWNetwkInNetGrpLastChange_Object = MibScalar
etsysFWNetwkInNetGrpLastChange = _EtsysFWNetwkInNetGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 6),
    _EtsysFWNetwkInNetGrpLastChange_Type()
)
etsysFWNetwkInNetGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetwkInNetGrpLastChange.setStatus("current")
_EtsysFWNetwkInNetGrpTable_Object = MibTable
etsysFWNetwkInNetGrpTable = _EtsysFWNetwkInNetGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 7)
)
if mibBuilder.loadTexts:
    etsysFWNetwkInNetGrpTable.setStatus("current")
_EtsysFWNetwkInNetGrpEntry_Object = MibTableRow
etsysFWNetwkInNetGrpEntry = _EtsysFWNetwkInNetGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 7, 1)
)
etsysFWNetwkInNetGrpEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupName"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWNetwkInNetGrpSubNetwork"),
)
if mibBuilder.loadTexts:
    etsysFWNetwkInNetGrpEntry.setStatus("current")
_EtsysFWNetwkInNetGrpSubNetwork_Type = SnmpAdminString
_EtsysFWNetwkInNetGrpSubNetwork_Object = MibTableColumn
etsysFWNetwkInNetGrpSubNetwork = _EtsysFWNetwkInNetGrpSubNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 7, 1, 1),
    _EtsysFWNetwkInNetGrpSubNetwork_Type()
)
etsysFWNetwkInNetGrpSubNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWNetwkInNetGrpSubNetwork.setStatus("current")


class _EtsysFWNetwkInNetGrpStorageType_Type(StorageType):
    """Custom type etsysFWNetwkInNetGrpStorageType based on StorageType"""


_EtsysFWNetwkInNetGrpStorageType_Object = MibTableColumn
etsysFWNetwkInNetGrpStorageType = _EtsysFWNetwkInNetGrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 7, 1, 2),
    _EtsysFWNetwkInNetGrpStorageType_Type()
)
etsysFWNetwkInNetGrpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetwkInNetGrpStorageType.setStatus("current")
_EtsysFWNetwkInNetGrpRowStatus_Type = RowStatus
_EtsysFWNetwkInNetGrpRowStatus_Object = MibTableColumn
etsysFWNetwkInNetGrpRowStatus = _EtsysFWNetwkInNetGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 7, 1, 3),
    _EtsysFWNetwkInNetGrpRowStatus_Type()
)
etsysFWNetwkInNetGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetwkInNetGrpRowStatus.setStatus("current")


class _EtsysFWNetworkMaxEntries_Type(Integer32):
    """Custom type etsysFWNetworkMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWNetworkMaxEntries_Type.__name__ = "Integer32"
_EtsysFWNetworkMaxEntries_Object = MibScalar
etsysFWNetworkMaxEntries = _EtsysFWNetworkMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 8),
    _EtsysFWNetworkMaxEntries_Type()
)
etsysFWNetworkMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkMaxEntries.setStatus("current")
_EtsysFWNetworkNumEntries_Type = Gauge32
_EtsysFWNetworkNumEntries_Object = MibScalar
etsysFWNetworkNumEntries = _EtsysFWNetworkNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 9),
    _EtsysFWNetworkNumEntries_Type()
)
etsysFWNetworkNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkNumEntries.setStatus("current")
_EtsysFWNetworkLastChange_Type = TimeStamp
_EtsysFWNetworkLastChange_Object = MibScalar
etsysFWNetworkLastChange = _EtsysFWNetworkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 10),
    _EtsysFWNetworkLastChange_Type()
)
etsysFWNetworkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWNetworkLastChange.setStatus("current")
_EtsysFWNetworkTable_Object = MibTable
etsysFWNetworkTable = _EtsysFWNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11)
)
if mibBuilder.loadTexts:
    etsysFWNetworkTable.setStatus("current")
_EtsysFWNetworkEntry_Object = MibTableRow
etsysFWNetworkEntry = _EtsysFWNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1)
)
etsysFWNetworkEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWNetworkName"),
)
if mibBuilder.loadTexts:
    etsysFWNetworkEntry.setStatus("current")


class _EtsysFWNetworkName_Type(SnmpAdminString):
    """Custom type etsysFWNetworkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWNetworkName_Type.__name__ = "SnmpAdminString"
_EtsysFWNetworkName_Object = MibTableColumn
etsysFWNetworkName = _EtsysFWNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 1),
    _EtsysFWNetworkName_Type()
)
etsysFWNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWNetworkName.setStatus("current")


class _EtsysFWNetworkRealm_Type(Integer32):
    """Custom type etsysFWNetworkRealm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_EtsysFWNetworkRealm_Type.__name__ = "Integer32"
_EtsysFWNetworkRealm_Object = MibTableColumn
etsysFWNetworkRealm = _EtsysFWNetworkRealm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 2),
    _EtsysFWNetworkRealm_Type()
)
etsysFWNetworkRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkRealm.setStatus("current")


class _EtsysFWNetworkRangeOrMask_Type(Integer32):
    """Custom type etsysFWNetworkRangeOrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useIpAddrMask", 2),
          ("useIpAddrRange", 1))
    )


_EtsysFWNetworkRangeOrMask_Type.__name__ = "Integer32"
_EtsysFWNetworkRangeOrMask_Object = MibTableColumn
etsysFWNetworkRangeOrMask = _EtsysFWNetworkRangeOrMask_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 3),
    _EtsysFWNetworkRangeOrMask_Type()
)
etsysFWNetworkRangeOrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkRangeOrMask.setStatus("current")


class _EtsysFWNetworkIPVersion_Type(InetAddressType):
    """Custom type etsysFWNetworkIPVersion based on InetAddressType"""


_EtsysFWNetworkIPVersion_Object = MibTableColumn
etsysFWNetworkIPVersion = _EtsysFWNetworkIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 4),
    _EtsysFWNetworkIPVersion_Type()
)
etsysFWNetworkIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkIPVersion.setStatus("current")
_EtsysFWNetworkIPAddressBegin_Type = InetAddress
_EtsysFWNetworkIPAddressBegin_Object = MibTableColumn
etsysFWNetworkIPAddressBegin = _EtsysFWNetworkIPAddressBegin_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 5),
    _EtsysFWNetworkIPAddressBegin_Type()
)
etsysFWNetworkIPAddressBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkIPAddressBegin.setStatus("current")
_EtsysFWNetworkIPAddressEnd_Type = InetAddress
_EtsysFWNetworkIPAddressEnd_Object = MibTableColumn
etsysFWNetworkIPAddressEnd = _EtsysFWNetworkIPAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 6),
    _EtsysFWNetworkIPAddressEnd_Type()
)
etsysFWNetworkIPAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkIPAddressEnd.setStatus("current")
_EtsysFWNetworkIPAddressMask_Type = InetAddress
_EtsysFWNetworkIPAddressMask_Object = MibTableColumn
etsysFWNetworkIPAddressMask = _EtsysFWNetworkIPAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 7),
    _EtsysFWNetworkIPAddressMask_Type()
)
etsysFWNetworkIPAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkIPAddressMask.setStatus("current")


class _EtsysFWNetworkStorageType_Type(StorageType):
    """Custom type etsysFWNetworkStorageType based on StorageType"""


_EtsysFWNetworkStorageType_Object = MibTableColumn
etsysFWNetworkStorageType = _EtsysFWNetworkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 8),
    _EtsysFWNetworkStorageType_Type()
)
etsysFWNetworkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkStorageType.setStatus("current")
_EtsysFWNetworkRowStatus_Type = RowStatus
_EtsysFWNetworkRowStatus_Object = MibTableColumn
etsysFWNetworkRowStatus = _EtsysFWNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 3, 11, 1, 9),
    _EtsysFWNetworkRowStatus_Type()
)
etsysFWNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWNetworkRowStatus.setStatus("current")
_EtsysFWPolicyServices_ObjectIdentity = ObjectIdentity
etsysFWPolicyServices = _EtsysFWPolicyServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4)
)


class _EtsysFWServiceGroupMaxEntries_Type(Integer32):
    """Custom type etsysFWServiceGroupMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWServiceGroupMaxEntries_Type.__name__ = "Integer32"
_EtsysFWServiceGroupMaxEntries_Object = MibScalar
etsysFWServiceGroupMaxEntries = _EtsysFWServiceGroupMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 1),
    _EtsysFWServiceGroupMaxEntries_Type()
)
etsysFWServiceGroupMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceGroupMaxEntries.setStatus("current")
_EtsysFWServiceGroupNumEntries_Type = Gauge32
_EtsysFWServiceGroupNumEntries_Object = MibScalar
etsysFWServiceGroupNumEntries = _EtsysFWServiceGroupNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 2),
    _EtsysFWServiceGroupNumEntries_Type()
)
etsysFWServiceGroupNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceGroupNumEntries.setStatus("current")
_EtsysFWServiceGroupLastChange_Type = TimeStamp
_EtsysFWServiceGroupLastChange_Object = MibScalar
etsysFWServiceGroupLastChange = _EtsysFWServiceGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 3),
    _EtsysFWServiceGroupLastChange_Type()
)
etsysFWServiceGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceGroupLastChange.setStatus("current")
_EtsysFWServiceGroupTable_Object = MibTable
etsysFWServiceGroupTable = _EtsysFWServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 4)
)
if mibBuilder.loadTexts:
    etsysFWServiceGroupTable.setStatus("current")
_EtsysFWServiceGroupEntry_Object = MibTableRow
etsysFWServiceGroupEntry = _EtsysFWServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 4, 1)
)
etsysFWServiceGroupEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupName"),
)
if mibBuilder.loadTexts:
    etsysFWServiceGroupEntry.setStatus("current")


class _EtsysFWServiceGroupName_Type(SnmpAdminString):
    """Custom type etsysFWServiceGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWServiceGroupName_Type.__name__ = "SnmpAdminString"
_EtsysFWServiceGroupName_Object = MibTableColumn
etsysFWServiceGroupName = _EtsysFWServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 4, 1, 1),
    _EtsysFWServiceGroupName_Type()
)
etsysFWServiceGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWServiceGroupName.setStatus("current")


class _EtsysFWServiceGroupStorageType_Type(StorageType):
    """Custom type etsysFWServiceGroupStorageType based on StorageType"""


_EtsysFWServiceGroupStorageType_Object = MibTableColumn
etsysFWServiceGroupStorageType = _EtsysFWServiceGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 4, 1, 2),
    _EtsysFWServiceGroupStorageType_Type()
)
etsysFWServiceGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceGroupStorageType.setStatus("current")
_EtsysFWServiceGroupRowStatus_Type = RowStatus
_EtsysFWServiceGroupRowStatus_Object = MibTableColumn
etsysFWServiceGroupRowStatus = _EtsysFWServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 4, 1, 3),
    _EtsysFWServiceGroupRowStatus_Type()
)
etsysFWServiceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceGroupRowStatus.setStatus("current")


class _EtsysFWServiceGroupMaxServices_Type(Integer32):
    """Custom type etsysFWServiceGroupMaxServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWServiceGroupMaxServices_Type.__name__ = "Integer32"
_EtsysFWServiceGroupMaxServices_Object = MibScalar
etsysFWServiceGroupMaxServices = _EtsysFWServiceGroupMaxServices_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 5),
    _EtsysFWServiceGroupMaxServices_Type()
)
etsysFWServiceGroupMaxServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceGroupMaxServices.setStatus("current")
_EtsysFWServiceInSvcGrpLastChange_Type = TimeStamp
_EtsysFWServiceInSvcGrpLastChange_Object = MibScalar
etsysFWServiceInSvcGrpLastChange = _EtsysFWServiceInSvcGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 6),
    _EtsysFWServiceInSvcGrpLastChange_Type()
)
etsysFWServiceInSvcGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceInSvcGrpLastChange.setStatus("current")
_EtsysFWServiceInSvcGrpTable_Object = MibTable
etsysFWServiceInSvcGrpTable = _EtsysFWServiceInSvcGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 7)
)
if mibBuilder.loadTexts:
    etsysFWServiceInSvcGrpTable.setStatus("current")
_EtsysFWServiceInSvcGrpEntry_Object = MibTableRow
etsysFWServiceInSvcGrpEntry = _EtsysFWServiceInSvcGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 7, 1)
)
etsysFWServiceInSvcGrpEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupName"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWServiceInSvcGrpSubService"),
)
if mibBuilder.loadTexts:
    etsysFWServiceInSvcGrpEntry.setStatus("current")
_EtsysFWServiceInSvcGrpSubService_Type = SnmpAdminString
_EtsysFWServiceInSvcGrpSubService_Object = MibTableColumn
etsysFWServiceInSvcGrpSubService = _EtsysFWServiceInSvcGrpSubService_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 7, 1, 1),
    _EtsysFWServiceInSvcGrpSubService_Type()
)
etsysFWServiceInSvcGrpSubService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWServiceInSvcGrpSubService.setStatus("current")


class _EtsysFWServiceInSvcGrpStorageType_Type(StorageType):
    """Custom type etsysFWServiceInSvcGrpStorageType based on StorageType"""


_EtsysFWServiceInSvcGrpStorageType_Object = MibTableColumn
etsysFWServiceInSvcGrpStorageType = _EtsysFWServiceInSvcGrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 7, 1, 2),
    _EtsysFWServiceInSvcGrpStorageType_Type()
)
etsysFWServiceInSvcGrpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceInSvcGrpStorageType.setStatus("current")
_EtsysFWServiceInSvcGrpRowStatus_Type = RowStatus
_EtsysFWServiceInSvcGrpRowStatus_Object = MibTableColumn
etsysFWServiceInSvcGrpRowStatus = _EtsysFWServiceInSvcGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 7, 1, 3),
    _EtsysFWServiceInSvcGrpRowStatus_Type()
)
etsysFWServiceInSvcGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceInSvcGrpRowStatus.setStatus("current")


class _EtsysFWServiceMaxEntries_Type(Integer32):
    """Custom type etsysFWServiceMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWServiceMaxEntries_Type.__name__ = "Integer32"
_EtsysFWServiceMaxEntries_Object = MibScalar
etsysFWServiceMaxEntries = _EtsysFWServiceMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 8),
    _EtsysFWServiceMaxEntries_Type()
)
etsysFWServiceMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceMaxEntries.setStatus("current")
_EtsysFWServiceNumEntries_Type = Gauge32
_EtsysFWServiceNumEntries_Object = MibScalar
etsysFWServiceNumEntries = _EtsysFWServiceNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 9),
    _EtsysFWServiceNumEntries_Type()
)
etsysFWServiceNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceNumEntries.setStatus("current")
_EtsysFWServiceLastChange_Type = TimeStamp
_EtsysFWServiceLastChange_Object = MibScalar
etsysFWServiceLastChange = _EtsysFWServiceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 10),
    _EtsysFWServiceLastChange_Type()
)
etsysFWServiceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWServiceLastChange.setStatus("current")
_EtsysFWServiceTable_Object = MibTable
etsysFWServiceTable = _EtsysFWServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11)
)
if mibBuilder.loadTexts:
    etsysFWServiceTable.setStatus("current")
_EtsysFWServiceEntry_Object = MibTableRow
etsysFWServiceEntry = _EtsysFWServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1)
)
etsysFWServiceEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWServiceName"),
)
if mibBuilder.loadTexts:
    etsysFWServiceEntry.setStatus("current")


class _EtsysFWServiceName_Type(SnmpAdminString):
    """Custom type etsysFWServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWServiceName_Type.__name__ = "SnmpAdminString"
_EtsysFWServiceName_Object = MibTableColumn
etsysFWServiceName = _EtsysFWServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 1),
    _EtsysFWServiceName_Type()
)
etsysFWServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWServiceName.setStatus("current")
_EtsysFWServiceSrcLowPort_Type = InetPortNumber
_EtsysFWServiceSrcLowPort_Object = MibTableColumn
etsysFWServiceSrcLowPort = _EtsysFWServiceSrcLowPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 2),
    _EtsysFWServiceSrcLowPort_Type()
)
etsysFWServiceSrcLowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceSrcLowPort.setStatus("current")
_EtsysFWServiceSrcHighPort_Type = InetPortNumber
_EtsysFWServiceSrcHighPort_Object = MibTableColumn
etsysFWServiceSrcHighPort = _EtsysFWServiceSrcHighPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 3),
    _EtsysFWServiceSrcHighPort_Type()
)
etsysFWServiceSrcHighPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceSrcHighPort.setStatus("current")
_EtsysFWServiceDstLowPort_Type = InetPortNumber
_EtsysFWServiceDstLowPort_Object = MibTableColumn
etsysFWServiceDstLowPort = _EtsysFWServiceDstLowPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 4),
    _EtsysFWServiceDstLowPort_Type()
)
etsysFWServiceDstLowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceDstLowPort.setStatus("current")
_EtsysFWServiceDstHighPort_Type = InetPortNumber
_EtsysFWServiceDstHighPort_Object = MibTableColumn
etsysFWServiceDstHighPort = _EtsysFWServiceDstHighPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 5),
    _EtsysFWServiceDstHighPort_Type()
)
etsysFWServiceDstHighPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceDstHighPort.setStatus("current")


class _EtsysFWServiceProtocol_Type(Integer32):
    """Custom type etsysFWServiceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_EtsysFWServiceProtocol_Type.__name__ = "Integer32"
_EtsysFWServiceProtocol_Object = MibTableColumn
etsysFWServiceProtocol = _EtsysFWServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 6),
    _EtsysFWServiceProtocol_Type()
)
etsysFWServiceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceProtocol.setStatus("current")


class _EtsysFWServiceStorageType_Type(StorageType):
    """Custom type etsysFWServiceStorageType based on StorageType"""


_EtsysFWServiceStorageType_Object = MibTableColumn
etsysFWServiceStorageType = _EtsysFWServiceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 7),
    _EtsysFWServiceStorageType_Type()
)
etsysFWServiceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceStorageType.setStatus("current")
_EtsysFWServiceRowStatus_Type = RowStatus
_EtsysFWServiceRowStatus_Object = MibTableColumn
etsysFWServiceRowStatus = _EtsysFWServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 4, 11, 1, 8),
    _EtsysFWServiceRowStatus_Type()
)
etsysFWServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWServiceRowStatus.setStatus("current")
_EtsysFWPolicyFilters_ObjectIdentity = ObjectIdentity
etsysFWPolicyFilters = _EtsysFWPolicyFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5)
)


class _EtsysFWFilterDefMaxEntries_Type(Integer32):
    """Custom type etsysFWFilterDefMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWFilterDefMaxEntries_Type.__name__ = "Integer32"
_EtsysFWFilterDefMaxEntries_Object = MibScalar
etsysFWFilterDefMaxEntries = _EtsysFWFilterDefMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 1),
    _EtsysFWFilterDefMaxEntries_Type()
)
etsysFWFilterDefMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWFilterDefMaxEntries.setStatus("current")
_EtsysFWFilterDefNumEntries_Type = Gauge32
_EtsysFWFilterDefNumEntries_Object = MibScalar
etsysFWFilterDefNumEntries = _EtsysFWFilterDefNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 2),
    _EtsysFWFilterDefNumEntries_Type()
)
etsysFWFilterDefNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWFilterDefNumEntries.setStatus("current")
_EtsysFWFilterDefLastChange_Type = TimeStamp
_EtsysFWFilterDefLastChange_Object = MibScalar
etsysFWFilterDefLastChange = _EtsysFWFilterDefLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 3),
    _EtsysFWFilterDefLastChange_Type()
)
etsysFWFilterDefLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWFilterDefLastChange.setStatus("current")
_EtsysFWFilterDefTable_Object = MibTable
etsysFWFilterDefTable = _EtsysFWFilterDefTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4)
)
if mibBuilder.loadTexts:
    etsysFWFilterDefTable.setStatus("current")
_EtsysFWFilterDefEntry_Object = MibTableRow
etsysFWFilterDefEntry = _EtsysFWFilterDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1)
)
etsysFWFilterDefEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefName"),
)
if mibBuilder.loadTexts:
    etsysFWFilterDefEntry.setStatus("current")


class _EtsysFWFilterDefName_Type(SnmpAdminString):
    """Custom type etsysFWFilterDefName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWFilterDefName_Type.__name__ = "SnmpAdminString"
_EtsysFWFilterDefName_Object = MibTableColumn
etsysFWFilterDefName = _EtsysFWFilterDefName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 1),
    _EtsysFWFilterDefName_Type()
)
etsysFWFilterDefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWFilterDefName.setStatus("current")
_EtsysFWFilterDefSrcNetwork_Type = VariablePointer
_EtsysFWFilterDefSrcNetwork_Object = MibTableColumn
etsysFWFilterDefSrcNetwork = _EtsysFWFilterDefSrcNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 2),
    _EtsysFWFilterDefSrcNetwork_Type()
)
etsysFWFilterDefSrcNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefSrcNetwork.setStatus("current")
_EtsysFWFilterDefDstNetwork_Type = VariablePointer
_EtsysFWFilterDefDstNetwork_Object = MibTableColumn
etsysFWFilterDefDstNetwork = _EtsysFWFilterDefDstNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 3),
    _EtsysFWFilterDefDstNetwork_Type()
)
etsysFWFilterDefDstNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefDstNetwork.setStatus("current")


class _EtsysFWFilterDefBidirectional_Type(TruthValue):
    """Custom type etsysFWFilterDefBidirectional based on TruthValue"""


_EtsysFWFilterDefBidirectional_Object = MibTableColumn
etsysFWFilterDefBidirectional = _EtsysFWFilterDefBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 4),
    _EtsysFWFilterDefBidirectional_Type()
)
etsysFWFilterDefBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefBidirectional.setStatus("current")
_EtsysFWFilterDefProtocol_Type = Integer32
_EtsysFWFilterDefProtocol_Object = MibTableColumn
etsysFWFilterDefProtocol = _EtsysFWFilterDefProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 5),
    _EtsysFWFilterDefProtocol_Type()
)
etsysFWFilterDefProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefProtocol.setStatus("current")
_EtsysFWFilterDefICMPType_Type = Integer32
_EtsysFWFilterDefICMPType_Object = MibTableColumn
etsysFWFilterDefICMPType = _EtsysFWFilterDefICMPType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 6),
    _EtsysFWFilterDefICMPType_Type()
)
etsysFWFilterDefICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefICMPType.setStatus("current")


class _EtsysFWFilterDefLogging_Type(TruthValue):
    """Custom type etsysFWFilterDefLogging based on TruthValue"""


_EtsysFWFilterDefLogging_Object = MibTableColumn
etsysFWFilterDefLogging = _EtsysFWFilterDefLogging_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 7),
    _EtsysFWFilterDefLogging_Type()
)
etsysFWFilterDefLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefLogging.setStatus("current")


class _EtsysFWFilterDefStorageType_Type(StorageType):
    """Custom type etsysFWFilterDefStorageType based on StorageType"""


_EtsysFWFilterDefStorageType_Object = MibTableColumn
etsysFWFilterDefStorageType = _EtsysFWFilterDefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 8),
    _EtsysFWFilterDefStorageType_Type()
)
etsysFWFilterDefStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefStorageType.setStatus("current")
_EtsysFWFilterDefRowStatus_Type = RowStatus
_EtsysFWFilterDefRowStatus_Object = MibTableColumn
etsysFWFilterDefRowStatus = _EtsysFWFilterDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 4, 1, 9),
    _EtsysFWFilterDefRowStatus_Type()
)
etsysFWFilterDefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWFilterDefRowStatus.setStatus("current")


class _EtsysFWCLSFilterMaxFilters_Type(Integer32):
    """Custom type etsysFWCLSFilterMaxFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysFWCLSFilterMaxFilters_Type.__name__ = "Integer32"
_EtsysFWCLSFilterMaxFilters_Object = MibScalar
etsysFWCLSFilterMaxFilters = _EtsysFWCLSFilterMaxFilters_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 5),
    _EtsysFWCLSFilterMaxFilters_Type()
)
etsysFWCLSFilterMaxFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWCLSFilterMaxFilters.setStatus("current")
_EtsysFWCLSFilterLastChange_Type = TimeStamp
_EtsysFWCLSFilterLastChange_Object = MibScalar
etsysFWCLSFilterLastChange = _EtsysFWCLSFilterLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 6),
    _EtsysFWCLSFilterLastChange_Type()
)
etsysFWCLSFilterLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWCLSFilterLastChange.setStatus("current")
_EtsysFWCLSFilterTable_Object = MibTable
etsysFWCLSFilterTable = _EtsysFWCLSFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 7)
)
if mibBuilder.loadTexts:
    etsysFWCLSFilterTable.setStatus("current")
_EtsysFWCLSFilterEntry_Object = MibTableRow
etsysFWCLSFilterEntry = _EtsysFWCLSFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 7, 1)
)
etsysFWCLSFilterEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefName"),
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWCLSFilterIndex"),
)
if mibBuilder.loadTexts:
    etsysFWCLSFilterEntry.setStatus("current")


class _EtsysFWCLSFilterIndex_Type(Integer32):
    """Custom type etsysFWCLSFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EtsysFWCLSFilterIndex_Type.__name__ = "Integer32"
_EtsysFWCLSFilterIndex_Object = MibTableColumn
etsysFWCLSFilterIndex = _EtsysFWCLSFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 7, 1, 1),
    _EtsysFWCLSFilterIndex_Type()
)
etsysFWCLSFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWCLSFilterIndex.setStatus("current")
_EtsysFWCLSFilterWord_Type = SnmpAdminString
_EtsysFWCLSFilterWord_Object = MibTableColumn
etsysFWCLSFilterWord = _EtsysFWCLSFilterWord_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 7, 1, 2),
    _EtsysFWCLSFilterWord_Type()
)
etsysFWCLSFilterWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWCLSFilterWord.setStatus("current")


class _EtsysFWCLSFilterStorageType_Type(StorageType):
    """Custom type etsysFWCLSFilterStorageType based on StorageType"""


_EtsysFWCLSFilterStorageType_Object = MibTableColumn
etsysFWCLSFilterStorageType = _EtsysFWCLSFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 7, 1, 3),
    _EtsysFWCLSFilterStorageType_Type()
)
etsysFWCLSFilterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWCLSFilterStorageType.setStatus("current")
_EtsysFWCLSFilterRowStatus_Type = RowStatus
_EtsysFWCLSFilterRowStatus_Object = MibTableColumn
etsysFWCLSFilterRowStatus = _EtsysFWCLSFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 7, 1, 4),
    _EtsysFWCLSFilterRowStatus_Type()
)
etsysFWCLSFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWCLSFilterRowStatus.setStatus("current")
_EtsysFWHTMLFilterTable_Object = MibTable
etsysFWHTMLFilterTable = _EtsysFWHTMLFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8)
)
if mibBuilder.loadTexts:
    etsysFWHTMLFilterTable.setStatus("current")
_EtsysFWHTMLFilterEntry_Object = MibTableRow
etsysFWHTMLFilterEntry = _EtsysFWHTMLFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1)
)
etsysFWHTMLFilterEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWHTMLFilterName"),
)
if mibBuilder.loadTexts:
    etsysFWHTMLFilterEntry.setStatus("current")


class _EtsysFWHTMLFilterName_Type(SnmpAdminString):
    """Custom type etsysFWHTMLFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWHTMLFilterName_Type.__name__ = "SnmpAdminString"
_EtsysFWHTMLFilterName_Object = MibTableColumn
etsysFWHTMLFilterName = _EtsysFWHTMLFilterName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1, 1),
    _EtsysFWHTMLFilterName_Type()
)
etsysFWHTMLFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFWHTMLFilterName.setStatus("current")


class _EtsysFWHTMLFilterType_Type(Integer32):
    """Custom type etsysFWHTMLFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("none", 1),
          ("selected", 2))
    )


_EtsysFWHTMLFilterType_Type.__name__ = "Integer32"
_EtsysFWHTMLFilterType_Object = MibTableColumn
etsysFWHTMLFilterType = _EtsysFWHTMLFilterType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1, 2),
    _EtsysFWHTMLFilterType_Type()
)
etsysFWHTMLFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWHTMLFilterType.setStatus("current")
_EtsysFWHTMLFilterNetwork_Type = SnmpAdminString
_EtsysFWHTMLFilterNetwork_Object = MibTableColumn
etsysFWHTMLFilterNetwork = _EtsysFWHTMLFilterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1, 3),
    _EtsysFWHTMLFilterNetwork_Type()
)
etsysFWHTMLFilterNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWHTMLFilterNetwork.setStatus("current")
_EtsysFWHTMLFilterLogging_Type = TruthValue
_EtsysFWHTMLFilterLogging_Object = MibTableColumn
etsysFWHTMLFilterLogging = _EtsysFWHTMLFilterLogging_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1, 4),
    _EtsysFWHTMLFilterLogging_Type()
)
etsysFWHTMLFilterLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWHTMLFilterLogging.setStatus("current")


class _EtsysFWHTMLFilterStorageType_Type(StorageType):
    """Custom type etsysFWHTMLFilterStorageType based on StorageType"""


_EtsysFWHTMLFilterStorageType_Object = MibTableColumn
etsysFWHTMLFilterStorageType = _EtsysFWHTMLFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1, 5),
    _EtsysFWHTMLFilterStorageType_Type()
)
etsysFWHTMLFilterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWHTMLFilterStorageType.setStatus("current")
_EtsysFWHTMLFilterRowStatus_Type = RowStatus
_EtsysFWHTMLFilterRowStatus_Object = MibTableColumn
etsysFWHTMLFilterRowStatus = _EtsysFWHTMLFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 2, 5, 8, 1, 6),
    _EtsysFWHTMLFilterRowStatus_Type()
)
etsysFWHTMLFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFWHTMLFilterRowStatus.setStatus("current")
_EtsysFWMonitoringObjects_ObjectIdentity = ObjectIdentity
etsysFWMonitoringObjects = _EtsysFWMonitoringObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3)
)
_EtsysFWPolicyRuleTrueNumEntries_Type = Gauge32
_EtsysFWPolicyRuleTrueNumEntries_Object = MibScalar
etsysFWPolicyRuleTrueNumEntries = _EtsysFWPolicyRuleTrueNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 1),
    _EtsysFWPolicyRuleTrueNumEntries_Type()
)
etsysFWPolicyRuleTrueNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueNumEntries.setStatus("current")
_EtsysFWPolicyRuleTrueLastChange_Type = TimeStamp
_EtsysFWPolicyRuleTrueLastChange_Object = MibScalar
etsysFWPolicyRuleTrueLastChange = _EtsysFWPolicyRuleTrueLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 2),
    _EtsysFWPolicyRuleTrueLastChange_Type()
)
etsysFWPolicyRuleTrueLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueLastChange.setStatus("current")
_EtsysFWPolicyRuleTrueTable_Object = MibTable
etsysFWPolicyRuleTrueTable = _EtsysFWPolicyRuleTrueTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 3)
)
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueTable.setStatus("current")
_EtsysFWPolicyRuleTrueEntry_Object = MibTableRow
etsysFWPolicyRuleTrueEntry = _EtsysFWPolicyRuleTrueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 3, 1)
)
etsysFWPolicyRuleTrueEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueIndex"),
)
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueEntry.setStatus("current")


class _EtsysFWPolicyRuleTrueIndex_Type(Integer32):
    """Custom type etsysFWPolicyRuleTrueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_EtsysFWPolicyRuleTrueIndex_Type.__name__ = "Integer32"
_EtsysFWPolicyRuleTrueIndex_Object = MibTableColumn
etsysFWPolicyRuleTrueIndex = _EtsysFWPolicyRuleTrueIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 3, 1, 1),
    _EtsysFWPolicyRuleTrueIndex_Type()
)
etsysFWPolicyRuleTrueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueIndex.setStatus("current")
_EtsysFWPolicyRuleTrueName_Type = SnmpAdminString
_EtsysFWPolicyRuleTrueName_Object = MibTableColumn
etsysFWPolicyRuleTrueName = _EtsysFWPolicyRuleTrueName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 3, 1, 2),
    _EtsysFWPolicyRuleTrueName_Type()
)
etsysFWPolicyRuleTrueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueName.setStatus("current")
_EtsysFWPolicyRuleTrueEvents_Type = Counter32
_EtsysFWPolicyRuleTrueEvents_Object = MibTableColumn
etsysFWPolicyRuleTrueEvents = _EtsysFWPolicyRuleTrueEvents_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 3, 1, 3),
    _EtsysFWPolicyRuleTrueEvents_Type()
)
etsysFWPolicyRuleTrueEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueEvents.setStatus("current")
_EtsysFWPolicyRuleTrueLastEvent_Type = DateAndTime
_EtsysFWPolicyRuleTrueLastEvent_Object = MibTableColumn
etsysFWPolicyRuleTrueLastEvent = _EtsysFWPolicyRuleTrueLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 3, 1, 4),
    _EtsysFWPolicyRuleTrueLastEvent_Type()
)
etsysFWPolicyRuleTrueLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueLastEvent.setStatus("current")
_EtsysFWSessionTotalsNumEntries_Type = Gauge32
_EtsysFWSessionTotalsNumEntries_Object = MibScalar
etsysFWSessionTotalsNumEntries = _EtsysFWSessionTotalsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 4),
    _EtsysFWSessionTotalsNumEntries_Type()
)
etsysFWSessionTotalsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessionTotalsNumEntries.setStatus("current")
_EtsysFWSessionTotalsLastChange_Type = TimeStamp
_EtsysFWSessionTotalsLastChange_Object = MibScalar
etsysFWSessionTotalsLastChange = _EtsysFWSessionTotalsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 5),
    _EtsysFWSessionTotalsLastChange_Type()
)
etsysFWSessionTotalsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessionTotalsLastChange.setStatus("current")
_EtsysFWSessionTotalsTable_Object = MibTable
etsysFWSessionTotalsTable = _EtsysFWSessionTotalsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6)
)
if mibBuilder.loadTexts:
    etsysFWSessionTotalsTable.setStatus("current")
_EtsysFWSessionTotalsEntry_Object = MibTableRow
etsysFWSessionTotalsEntry = _EtsysFWSessionTotalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1)
)
etsysFWSessionTotalsEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWSessTotIndex"),
)
if mibBuilder.loadTexts:
    etsysFWSessionTotalsEntry.setStatus("current")


class _EtsysFWSessTotIndex_Type(Integer32):
    """Custom type etsysFWSessTotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_EtsysFWSessTotIndex_Type.__name__ = "Integer32"
_EtsysFWSessTotIndex_Object = MibTableColumn
etsysFWSessTotIndex = _EtsysFWSessTotIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1, 1),
    _EtsysFWSessTotIndex_Type()
)
etsysFWSessTotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessTotIndex.setStatus("current")


class _EtsysFWSessTotProtocolID_Type(Unsigned32):
    """Custom type etsysFWSessTotProtocolID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EtsysFWSessTotProtocolID_Type.__name__ = "Unsigned32"
_EtsysFWSessTotProtocolID_Object = MibTableColumn
etsysFWSessTotProtocolID = _EtsysFWSessTotProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1, 2),
    _EtsysFWSessTotProtocolID_Type()
)
etsysFWSessTotProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessTotProtocolID.setStatus("current")
_EtsysFWSessTotActiveSessions_Type = Counter32
_EtsysFWSessTotActiveSessions_Object = MibTableColumn
etsysFWSessTotActiveSessions = _EtsysFWSessTotActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1, 3),
    _EtsysFWSessTotActiveSessions_Type()
)
etsysFWSessTotActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessTotActiveSessions.setStatus("current")
_EtsysFWSessTotPeakSessions_Type = Counter32
_EtsysFWSessTotPeakSessions_Object = MibTableColumn
etsysFWSessTotPeakSessions = _EtsysFWSessTotPeakSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1, 4),
    _EtsysFWSessTotPeakSessions_Type()
)
etsysFWSessTotPeakSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessTotPeakSessions.setStatus("current")
_EtsysFWSessTotBlockedSessions_Type = Counter32
_EtsysFWSessTotBlockedSessions_Object = MibTableColumn
etsysFWSessTotBlockedSessions = _EtsysFWSessTotBlockedSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1, 5),
    _EtsysFWSessTotBlockedSessions_Type()
)
etsysFWSessTotBlockedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessTotBlockedSessions.setStatus("current")
_EtsysFWSessTotLastBlock_Type = DateAndTime
_EtsysFWSessTotLastBlock_Object = MibTableColumn
etsysFWSessTotLastBlock = _EtsysFWSessTotLastBlock_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 6, 1, 6),
    _EtsysFWSessTotLastBlock_Type()
)
etsysFWSessTotLastBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWSessTotLastBlock.setStatus("current")
_EtsysFWIpSessionNumEntries_Type = Gauge32
_EtsysFWIpSessionNumEntries_Object = MibScalar
etsysFWIpSessionNumEntries = _EtsysFWIpSessionNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 7),
    _EtsysFWIpSessionNumEntries_Type()
)
etsysFWIpSessionNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionNumEntries.setStatus("current")
_EtsysFWIpSessionLastChange_Type = TimeStamp
_EtsysFWIpSessionLastChange_Object = MibScalar
etsysFWIpSessionLastChange = _EtsysFWIpSessionLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 8),
    _EtsysFWIpSessionLastChange_Type()
)
etsysFWIpSessionLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionLastChange.setStatus("current")
_EtsysFWIpSessionTable_Object = MibTable
etsysFWIpSessionTable = _EtsysFWIpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9)
)
if mibBuilder.loadTexts:
    etsysFWIpSessionTable.setStatus("current")
_EtsysFWIpSessionEntry_Object = MibTableRow
etsysFWIpSessionEntry = _EtsysFWIpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1)
)
etsysFWIpSessionEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionIndex"),
)
if mibBuilder.loadTexts:
    etsysFWIpSessionEntry.setStatus("current")


class _EtsysFWIpSessionIndex_Type(Integer32):
    """Custom type etsysFWIpSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_EtsysFWIpSessionIndex_Type.__name__ = "Integer32"
_EtsysFWIpSessionIndex_Object = MibTableColumn
etsysFWIpSessionIndex = _EtsysFWIpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 1),
    _EtsysFWIpSessionIndex_Type()
)
etsysFWIpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionIndex.setStatus("current")
_EtsysFWIpSessionIPVersion_Type = InetAddressType
_EtsysFWIpSessionIPVersion_Object = MibTableColumn
etsysFWIpSessionIPVersion = _EtsysFWIpSessionIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 2),
    _EtsysFWIpSessionIPVersion_Type()
)
etsysFWIpSessionIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionIPVersion.setStatus("current")
_EtsysFWIpSessionSrcAddress_Type = InetAddress
_EtsysFWIpSessionSrcAddress_Object = MibTableColumn
etsysFWIpSessionSrcAddress = _EtsysFWIpSessionSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 3),
    _EtsysFWIpSessionSrcAddress_Type()
)
etsysFWIpSessionSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionSrcAddress.setStatus("current")
_EtsysFWIpSessionDstAddress_Type = InetAddress
_EtsysFWIpSessionDstAddress_Object = MibTableColumn
etsysFWIpSessionDstAddress = _EtsysFWIpSessionDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 4),
    _EtsysFWIpSessionDstAddress_Type()
)
etsysFWIpSessionDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionDstAddress.setStatus("current")
_EtsysFWIpSessionSrcPort_Type = InetPortNumber
_EtsysFWIpSessionSrcPort_Object = MibTableColumn
etsysFWIpSessionSrcPort = _EtsysFWIpSessionSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 5),
    _EtsysFWIpSessionSrcPort_Type()
)
etsysFWIpSessionSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionSrcPort.setStatus("current")
_EtsysFWIpSessionDstPort_Type = InetPortNumber
_EtsysFWIpSessionDstPort_Object = MibTableColumn
etsysFWIpSessionDstPort = _EtsysFWIpSessionDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 6),
    _EtsysFWIpSessionDstPort_Type()
)
etsysFWIpSessionDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionDstPort.setStatus("current")
_EtsysFWIpSessionProtocolID_Type = Unsigned32
_EtsysFWIpSessionProtocolID_Object = MibTableColumn
etsysFWIpSessionProtocolID = _EtsysFWIpSessionProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 7),
    _EtsysFWIpSessionProtocolID_Type()
)
etsysFWIpSessionProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionProtocolID.setStatus("current")
_EtsysFWIpSessionCreation_Type = DateAndTime
_EtsysFWIpSessionCreation_Object = MibTableColumn
etsysFWIpSessionCreation = _EtsysFWIpSessionCreation_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 9, 1, 8),
    _EtsysFWIpSessionCreation_Type()
)
etsysFWIpSessionCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWIpSessionCreation.setStatus("current")
_EtsysFWAuthAddressNumEntries_Type = Gauge32
_EtsysFWAuthAddressNumEntries_Object = MibScalar
etsysFWAuthAddressNumEntries = _EtsysFWAuthAddressNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 10),
    _EtsysFWAuthAddressNumEntries_Type()
)
etsysFWAuthAddressNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressNumEntries.setStatus("current")
_EtsysFWAuthAddressLastChange_Type = TimeStamp
_EtsysFWAuthAddressLastChange_Object = MibScalar
etsysFWAuthAddressLastChange = _EtsysFWAuthAddressLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 11),
    _EtsysFWAuthAddressLastChange_Type()
)
etsysFWAuthAddressLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressLastChange.setStatus("current")
_EtsysFWAuthAddressTable_Object = MibTable
etsysFWAuthAddressTable = _EtsysFWAuthAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12)
)
if mibBuilder.loadTexts:
    etsysFWAuthAddressTable.setStatus("current")
_EtsysFWAuthAddressEntry_Object = MibTableRow
etsysFWAuthAddressEntry = _EtsysFWAuthAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12, 1)
)
etsysFWAuthAddressEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressIndex"),
)
if mibBuilder.loadTexts:
    etsysFWAuthAddressEntry.setStatus("current")


class _EtsysFWAuthAddressIndex_Type(Integer32):
    """Custom type etsysFWAuthAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_EtsysFWAuthAddressIndex_Type.__name__ = "Integer32"
_EtsysFWAuthAddressIndex_Object = MibTableColumn
etsysFWAuthAddressIndex = _EtsysFWAuthAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12, 1, 1),
    _EtsysFWAuthAddressIndex_Type()
)
etsysFWAuthAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressIndex.setStatus("current")
_EtsysFWAuthAddressIPVersion_Type = InetAddressType
_EtsysFWAuthAddressIPVersion_Object = MibTableColumn
etsysFWAuthAddressIPVersion = _EtsysFWAuthAddressIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12, 1, 2),
    _EtsysFWAuthAddressIPVersion_Type()
)
etsysFWAuthAddressIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressIPVersion.setStatus("current")
_EtsysFWAuthAddressIPAddress_Type = InetAddress
_EtsysFWAuthAddressIPAddress_Object = MibTableColumn
etsysFWAuthAddressIPAddress = _EtsysFWAuthAddressIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12, 1, 3),
    _EtsysFWAuthAddressIPAddress_Type()
)
etsysFWAuthAddressIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressIPAddress.setStatus("current")
_EtsysFWAuthAddressGroupName_Type = SnmpAdminString
_EtsysFWAuthAddressGroupName_Object = MibTableColumn
etsysFWAuthAddressGroupName = _EtsysFWAuthAddressGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12, 1, 4),
    _EtsysFWAuthAddressGroupName_Type()
)
etsysFWAuthAddressGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressGroupName.setStatus("current")
_EtsysFWAuthAddressIdleTime_Type = Integer32
_EtsysFWAuthAddressIdleTime_Object = MibTableColumn
etsysFWAuthAddressIdleTime = _EtsysFWAuthAddressIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 12, 1, 5),
    _EtsysFWAuthAddressIdleTime_Type()
)
etsysFWAuthAddressIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWAuthAddressIdleTime.setStatus("current")
_EtsysFWDoSBlockedNumEntries_Type = Gauge32
_EtsysFWDoSBlockedNumEntries_Object = MibScalar
etsysFWDoSBlockedNumEntries = _EtsysFWDoSBlockedNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 13),
    _EtsysFWDoSBlockedNumEntries_Type()
)
etsysFWDoSBlockedNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSBlockedNumEntries.setStatus("current")
_EtsysFWDoSBlockedLastChange_Type = TimeStamp
_EtsysFWDoSBlockedLastChange_Object = MibScalar
etsysFWDoSBlockedLastChange = _EtsysFWDoSBlockedLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 14),
    _EtsysFWDoSBlockedLastChange_Type()
)
etsysFWDoSBlockedLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSBlockedLastChange.setStatus("current")
_EtsysFWDoSBlockedTable_Object = MibTable
etsysFWDoSBlockedTable = _EtsysFWDoSBlockedTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15)
)
if mibBuilder.loadTexts:
    etsysFWDoSBlockedTable.setStatus("current")
_EtsysFWDoSBlockedEntry_Object = MibTableRow
etsysFWDoSBlockedEntry = _EtsysFWDoSBlockedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15, 1)
)
etsysFWDoSBlockedEntry.setIndexNames(
    (0, "ENTERASYS-FIREWALL-MIB", "etsysFWDoSAttackName"),
)
if mibBuilder.loadTexts:
    etsysFWDoSBlockedEntry.setStatus("current")


class _EtsysFWDoSAttackName_Type(SnmpAdminString):
    """Custom type etsysFWDoSAttackName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysFWDoSAttackName_Type.__name__ = "SnmpAdminString"
_EtsysFWDoSAttackName_Object = MibTableColumn
etsysFWDoSAttackName = _EtsysFWDoSAttackName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15, 1, 1),
    _EtsysFWDoSAttackName_Type()
)
etsysFWDoSAttackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSAttackName.setStatus("current")
_EtsysFWDoSSrcIPVersion_Type = InetAddressType
_EtsysFWDoSSrcIPVersion_Object = MibTableColumn
etsysFWDoSSrcIPVersion = _EtsysFWDoSSrcIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15, 1, 2),
    _EtsysFWDoSSrcIPVersion_Type()
)
etsysFWDoSSrcIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSSrcIPVersion.setStatus("current")
_EtsysFWDoSSrcIPAddress_Type = InetAddress
_EtsysFWDoSSrcIPAddress_Object = MibTableColumn
etsysFWDoSSrcIPAddress = _EtsysFWDoSSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15, 1, 3),
    _EtsysFWDoSSrcIPAddress_Type()
)
etsysFWDoSSrcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSSrcIPAddress.setStatus("current")
_EtsysFWDoSAttackTime_Type = DateAndTime
_EtsysFWDoSAttackTime_Object = MibTableColumn
etsysFWDoSAttackTime = _EtsysFWDoSAttackTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15, 1, 4),
    _EtsysFWDoSAttackTime_Type()
)
etsysFWDoSAttackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSAttackTime.setStatus("current")
_EtsysFWDoSBlockedAttacks_Type = Counter32
_EtsysFWDoSBlockedAttacks_Object = MibTableColumn
etsysFWDoSBlockedAttacks = _EtsysFWDoSBlockedAttacks_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 3, 15, 1, 5),
    _EtsysFWDoSBlockedAttacks_Type()
)
etsysFWDoSBlockedAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFWDoSBlockedAttacks.setStatus("current")
_EtsysFirewallConformance_ObjectIdentity = ObjectIdentity
etsysFirewallConformance = _EtsysFirewallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4)
)
_EtsysFirewallGroups_ObjectIdentity = ObjectIdentity
etsysFirewallGroups = _EtsysFirewallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1)
)
_EtsysFirewallCompliances_ObjectIdentity = ObjectIdentity
etsysFirewallCompliances = _EtsysFirewallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 2)
)

# Managed Objects groups

etsysFWFirewallEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 1)
)
etsysFWFirewallEnabledGroup.setObjects(
    ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallEnabled")
)
if mibBuilder.loadTexts:
    etsysFWFirewallEnabledGroup.setStatus("current")

etsysFWFirewallConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 2)
)
etsysFWFirewallConfigGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWTcpTimeout"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWUdpTimeout"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIcmpTimeout"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthTimeout"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWLoggingThreshold"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWRPCMicrosoftTimeout"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWRPCSunTimeout"))
)
if mibBuilder.loadTexts:
    etsysFWFirewallConfigGroup.setStatus("current")

etsysFWFirewallIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 3)
)
etsysFWFirewallIntfGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallOnIntfLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallOnIntfEnabled"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallOnIntfStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallOnIntfRowStatus"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallIntfFilterLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallIntfFilterDirection"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallIntfFilterStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFirewallIntfFilterRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWFirewallIntfGroup.setStatus("current")

etsysFWSystemPolicyNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 4)
)
etsysFWSystemPolicyNameGroup.setObjects(
    ("ENTERASYS-FIREWALL-MIB", "etsysFWSystemPolicyGroupName")
)
if mibBuilder.loadTexts:
    etsysFWSystemPolicyNameGroup.setStatus("current")

etsysFWInterfacePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 5)
)
etsysFWInterfacePolicyGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWIntfToGroupLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIntfToGroupStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIntfToGroupRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWInterfacePolicyGroup.setStatus("current")

etsysFWGroupPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 6)
)
etsysFWGroupPolicyGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWGroupPolicyLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWGroupPolicyPriority"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWGroupPolicyStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWGroupPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWGroupPolicyGroup.setStatus("current")

etsysFWPolicyRuleDefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 7)
)
etsysFWPolicyRuleDefGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefMaxEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefSrcNetwork"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefDstNetwork"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefBidirectional"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefService"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleAuthName"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefAction"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefLogging"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleDefRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWPolicyRuleDefGroup.setStatus("current")

etsysFWNetworkGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 8)
)
etsysFWNetworkGroupGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupMaxEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupRowStatus"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkGroupMaxNetworks"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetwkInNetGrpLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetwkInNetGrpStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetwkInNetGrpRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWNetworkGroupGroup.setStatus("current")

etsysFWNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 9)
)
etsysFWNetworkGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkMaxEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkRealm"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkRangeOrMask"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkIPVersion"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkIPAddressBegin"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkIPAddressEnd"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkIPAddressMask"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWNetworkRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWNetworkGroup.setStatus("current")

etsysFWServiceGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 10)
)
etsysFWServiceGroupGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupMaxEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupRowStatus"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceGroupMaxServices"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceInSvcGrpLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceInSvcGrpStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceInSvcGrpRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWServiceGroupGroup.setStatus("current")

etsysFWServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 11)
)
etsysFWServiceGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWServiceMaxEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceSrcLowPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceSrcHighPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceDstLowPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceDstHighPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceProtocol"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWServiceRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWServiceGroup.setStatus("current")

etsysFWFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 12)
)
etsysFWFilterGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefMaxEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefSrcNetwork"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefDstNetwork"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefBidirectional"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefProtocol"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefICMPType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefLogging"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWFilterDefRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWFilterGroup.setStatus("current")

etsysFWCLSFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 13)
)
etsysFWCLSFilterGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWCLSFilterMaxFilters"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWCLSFilterLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWCLSFilterWord"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWCLSFilterStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWCLSFilterRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWCLSFilterGroup.setStatus("current")

etsysFWHTMLFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 14)
)
etsysFWHTMLFilterGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWHTMLFilterType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWHTMLFilterNetwork"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWHTMLFilterLogging"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWHTMLFilterStorageType"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWHTMLFilterRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFWHTMLFilterGroup.setStatus("current")

etsysFWPolicyRuleTrueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 15)
)
etsysFWPolicyRuleTrueGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueIndex"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueName"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueEvents"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWPolicyRuleTrueLastEvent"))
)
if mibBuilder.loadTexts:
    etsysFWPolicyRuleTrueGroup.setStatus("current")

etsysFWSessionTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 16)
)
etsysFWSessionTotalsGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWSessionTotalsNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessionTotalsLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessTotIndex"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessTotProtocolID"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessTotActiveSessions"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessTotPeakSessions"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessTotBlockedSessions"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWSessTotLastBlock"))
)
if mibBuilder.loadTexts:
    etsysFWSessionTotalsGroup.setStatus("current")

etsysFWIpSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 17)
)
etsysFWIpSessionGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionIndex"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionIPVersion"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionSrcAddress"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionDstAddress"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionSrcPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionDstPort"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionProtocolID"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWIpSessionCreation"))
)
if mibBuilder.loadTexts:
    etsysFWIpSessionGroup.setStatus("current")

etsysFWAuthAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 18)
)
etsysFWAuthAddressGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressIndex"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressIPVersion"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressIPAddress"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressGroupName"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWAuthAddressIdleTime"))
)
if mibBuilder.loadTexts:
    etsysFWAuthAddressGroup.setStatus("current")

etsysFWDoSBlockedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 1, 19)
)
etsysFWDoSBlockedGroup.setObjects(
      *(("ENTERASYS-FIREWALL-MIB", "etsysFWDoSBlockedNumEntries"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWDoSBlockedLastChange"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWDoSAttackName"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWDoSSrcIPVersion"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWDoSSrcIPAddress"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWDoSAttackTime"),
        ("ENTERASYS-FIREWALL-MIB", "etsysFWDoSBlockedAttacks"))
)
if mibBuilder.loadTexts:
    etsysFWDoSBlockedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysFirewallCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 37, 4, 2, 1)
)
if mibBuilder.loadTexts:
    etsysFirewallCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-FIREWALL-MIB",
    **{"etsysFirewallMIB": etsysFirewallMIB,
       "etsysFWConfigurationObjects": etsysFWConfigurationObjects,
       "etsysFWFirewallEnabled": etsysFWFirewallEnabled,
       "etsysFWTcpTimeout": etsysFWTcpTimeout,
       "etsysFWUdpTimeout": etsysFWUdpTimeout,
       "etsysFWIcmpTimeout": etsysFWIcmpTimeout,
       "etsysFWAuthTimeout": etsysFWAuthTimeout,
       "etsysFWAuthPort": etsysFWAuthPort,
       "etsysFWLoggingThreshold": etsysFWLoggingThreshold,
       "etsysFWRPCMicrosoftTimeout": etsysFWRPCMicrosoftTimeout,
       "etsysFWRPCSunTimeout": etsysFWRPCSunTimeout,
       "etsysFWFirewallOnIntfLastChange": etsysFWFirewallOnIntfLastChange,
       "etsysFWFirewallOnIntfTable": etsysFWFirewallOnIntfTable,
       "etsysFWFirewallOnIntfEntry": etsysFWFirewallOnIntfEntry,
       "etsysFWFirewallOnIntfEnabled": etsysFWFirewallOnIntfEnabled,
       "etsysFWFirewallOnIntfStorageType": etsysFWFirewallOnIntfStorageType,
       "etsysFWFirewallOnIntfRowStatus": etsysFWFirewallOnIntfRowStatus,
       "etsysFWFirewallIntfFilterLastChange": etsysFWFirewallIntfFilterLastChange,
       "etsysFWFirewallIntfFilterTable": etsysFWFirewallIntfFilterTable,
       "etsysFWFirewallIntfFilterEntry": etsysFWFirewallIntfFilterEntry,
       "etsysFWFirewallIntfFilterType": etsysFWFirewallIntfFilterType,
       "etsysFWFirewallIntfFilterDirection": etsysFWFirewallIntfFilterDirection,
       "etsysFWFirewallIntfFilterStorageType": etsysFWFirewallIntfFilterStorageType,
       "etsysFWFirewallIntfFilterRowStatus": etsysFWFirewallIntfFilterRowStatus,
       "etsysFWPolicyObjects": etsysFWPolicyObjects,
       "etsysFWPolicyGroups": etsysFWPolicyGroups,
       "etsysFWSystemPolicyGroupName": etsysFWSystemPolicyGroupName,
       "etsysFWIntfToGroupLastChange": etsysFWIntfToGroupLastChange,
       "etsysFWIntfToGroupTable": etsysFWIntfToGroupTable,
       "etsysFWIntfToGroupEntry": etsysFWIntfToGroupEntry,
       "etsysFWIntfToGroupIntfDirection": etsysFWIntfToGroupIntfDirection,
       "etsysFWIntfToGroupName": etsysFWIntfToGroupName,
       "etsysFWIntfToGroupStorageType": etsysFWIntfToGroupStorageType,
       "etsysFWIntfToGroupRowStatus": etsysFWIntfToGroupRowStatus,
       "etsysFWGroupPolicyLastChange": etsysFWGroupPolicyLastChange,
       "etsysFWGroupPolicyTable": etsysFWGroupPolicyTable,
       "etsysFWGroupPolicyEntry": etsysFWGroupPolicyEntry,
       "etsysFWGroupPolicyName": etsysFWGroupPolicyName,
       "etsysFWGroupPolicyRuleDef": etsysFWGroupPolicyRuleDef,
       "etsysFWGroupPolicyPriority": etsysFWGroupPolicyPriority,
       "etsysFWGroupPolicyStorageType": etsysFWGroupPolicyStorageType,
       "etsysFWGroupPolicyRowStatus": etsysFWGroupPolicyRowStatus,
       "etsysFWPolicyRules": etsysFWPolicyRules,
       "etsysFWPolicyRuleDefMaxEntries": etsysFWPolicyRuleDefMaxEntries,
       "etsysFWPolicyRuleDefNumEntries": etsysFWPolicyRuleDefNumEntries,
       "etsysFWPolicyRuleDefLastChange": etsysFWPolicyRuleDefLastChange,
       "etsysFWPolicyRuleDefTable": etsysFWPolicyRuleDefTable,
       "etsysFWPolicyRuleDefEntry": etsysFWPolicyRuleDefEntry,
       "etsysFWPolicyRuleDefName": etsysFWPolicyRuleDefName,
       "etsysFWPolicyRuleDefSrcNetwork": etsysFWPolicyRuleDefSrcNetwork,
       "etsysFWPolicyRuleDefDstNetwork": etsysFWPolicyRuleDefDstNetwork,
       "etsysFWPolicyRuleDefBidirectional": etsysFWPolicyRuleDefBidirectional,
       "etsysFWPolicyRuleDefService": etsysFWPolicyRuleDefService,
       "etsysFWPolicyRuleAuthName": etsysFWPolicyRuleAuthName,
       "etsysFWPolicyRuleDefAction": etsysFWPolicyRuleDefAction,
       "etsysFWPolicyRuleDefLogging": etsysFWPolicyRuleDefLogging,
       "etsysFWPolicyRuleDefStorageType": etsysFWPolicyRuleDefStorageType,
       "etsysFWPolicyRuleDefRowStatus": etsysFWPolicyRuleDefRowStatus,
       "etsysFWPolicyNetworks": etsysFWPolicyNetworks,
       "etsysFWNetworkGroupMaxEntries": etsysFWNetworkGroupMaxEntries,
       "etsysFWNetworkGroupNumEntries": etsysFWNetworkGroupNumEntries,
       "etsysFWNetworkGroupLastChange": etsysFWNetworkGroupLastChange,
       "etsysFWNetworkGroupTable": etsysFWNetworkGroupTable,
       "etsysFWNetworkGroupEntry": etsysFWNetworkGroupEntry,
       "etsysFWNetworkGroupName": etsysFWNetworkGroupName,
       "etsysFWNetworkGroupStorageType": etsysFWNetworkGroupStorageType,
       "etsysFWNetworkGroupRowStatus": etsysFWNetworkGroupRowStatus,
       "etsysFWNetworkGroupMaxNetworks": etsysFWNetworkGroupMaxNetworks,
       "etsysFWNetwkInNetGrpLastChange": etsysFWNetwkInNetGrpLastChange,
       "etsysFWNetwkInNetGrpTable": etsysFWNetwkInNetGrpTable,
       "etsysFWNetwkInNetGrpEntry": etsysFWNetwkInNetGrpEntry,
       "etsysFWNetwkInNetGrpSubNetwork": etsysFWNetwkInNetGrpSubNetwork,
       "etsysFWNetwkInNetGrpStorageType": etsysFWNetwkInNetGrpStorageType,
       "etsysFWNetwkInNetGrpRowStatus": etsysFWNetwkInNetGrpRowStatus,
       "etsysFWNetworkMaxEntries": etsysFWNetworkMaxEntries,
       "etsysFWNetworkNumEntries": etsysFWNetworkNumEntries,
       "etsysFWNetworkLastChange": etsysFWNetworkLastChange,
       "etsysFWNetworkTable": etsysFWNetworkTable,
       "etsysFWNetworkEntry": etsysFWNetworkEntry,
       "etsysFWNetworkName": etsysFWNetworkName,
       "etsysFWNetworkRealm": etsysFWNetworkRealm,
       "etsysFWNetworkRangeOrMask": etsysFWNetworkRangeOrMask,
       "etsysFWNetworkIPVersion": etsysFWNetworkIPVersion,
       "etsysFWNetworkIPAddressBegin": etsysFWNetworkIPAddressBegin,
       "etsysFWNetworkIPAddressEnd": etsysFWNetworkIPAddressEnd,
       "etsysFWNetworkIPAddressMask": etsysFWNetworkIPAddressMask,
       "etsysFWNetworkStorageType": etsysFWNetworkStorageType,
       "etsysFWNetworkRowStatus": etsysFWNetworkRowStatus,
       "etsysFWPolicyServices": etsysFWPolicyServices,
       "etsysFWServiceGroupMaxEntries": etsysFWServiceGroupMaxEntries,
       "etsysFWServiceGroupNumEntries": etsysFWServiceGroupNumEntries,
       "etsysFWServiceGroupLastChange": etsysFWServiceGroupLastChange,
       "etsysFWServiceGroupTable": etsysFWServiceGroupTable,
       "etsysFWServiceGroupEntry": etsysFWServiceGroupEntry,
       "etsysFWServiceGroupName": etsysFWServiceGroupName,
       "etsysFWServiceGroupStorageType": etsysFWServiceGroupStorageType,
       "etsysFWServiceGroupRowStatus": etsysFWServiceGroupRowStatus,
       "etsysFWServiceGroupMaxServices": etsysFWServiceGroupMaxServices,
       "etsysFWServiceInSvcGrpLastChange": etsysFWServiceInSvcGrpLastChange,
       "etsysFWServiceInSvcGrpTable": etsysFWServiceInSvcGrpTable,
       "etsysFWServiceInSvcGrpEntry": etsysFWServiceInSvcGrpEntry,
       "etsysFWServiceInSvcGrpSubService": etsysFWServiceInSvcGrpSubService,
       "etsysFWServiceInSvcGrpStorageType": etsysFWServiceInSvcGrpStorageType,
       "etsysFWServiceInSvcGrpRowStatus": etsysFWServiceInSvcGrpRowStatus,
       "etsysFWServiceMaxEntries": etsysFWServiceMaxEntries,
       "etsysFWServiceNumEntries": etsysFWServiceNumEntries,
       "etsysFWServiceLastChange": etsysFWServiceLastChange,
       "etsysFWServiceTable": etsysFWServiceTable,
       "etsysFWServiceEntry": etsysFWServiceEntry,
       "etsysFWServiceName": etsysFWServiceName,
       "etsysFWServiceSrcLowPort": etsysFWServiceSrcLowPort,
       "etsysFWServiceSrcHighPort": etsysFWServiceSrcHighPort,
       "etsysFWServiceDstLowPort": etsysFWServiceDstLowPort,
       "etsysFWServiceDstHighPort": etsysFWServiceDstHighPort,
       "etsysFWServiceProtocol": etsysFWServiceProtocol,
       "etsysFWServiceStorageType": etsysFWServiceStorageType,
       "etsysFWServiceRowStatus": etsysFWServiceRowStatus,
       "etsysFWPolicyFilters": etsysFWPolicyFilters,
       "etsysFWFilterDefMaxEntries": etsysFWFilterDefMaxEntries,
       "etsysFWFilterDefNumEntries": etsysFWFilterDefNumEntries,
       "etsysFWFilterDefLastChange": etsysFWFilterDefLastChange,
       "etsysFWFilterDefTable": etsysFWFilterDefTable,
       "etsysFWFilterDefEntry": etsysFWFilterDefEntry,
       "etsysFWFilterDefName": etsysFWFilterDefName,
       "etsysFWFilterDefSrcNetwork": etsysFWFilterDefSrcNetwork,
       "etsysFWFilterDefDstNetwork": etsysFWFilterDefDstNetwork,
       "etsysFWFilterDefBidirectional": etsysFWFilterDefBidirectional,
       "etsysFWFilterDefProtocol": etsysFWFilterDefProtocol,
       "etsysFWFilterDefICMPType": etsysFWFilterDefICMPType,
       "etsysFWFilterDefLogging": etsysFWFilterDefLogging,
       "etsysFWFilterDefStorageType": etsysFWFilterDefStorageType,
       "etsysFWFilterDefRowStatus": etsysFWFilterDefRowStatus,
       "etsysFWCLSFilterMaxFilters": etsysFWCLSFilterMaxFilters,
       "etsysFWCLSFilterLastChange": etsysFWCLSFilterLastChange,
       "etsysFWCLSFilterTable": etsysFWCLSFilterTable,
       "etsysFWCLSFilterEntry": etsysFWCLSFilterEntry,
       "etsysFWCLSFilterIndex": etsysFWCLSFilterIndex,
       "etsysFWCLSFilterWord": etsysFWCLSFilterWord,
       "etsysFWCLSFilterStorageType": etsysFWCLSFilterStorageType,
       "etsysFWCLSFilterRowStatus": etsysFWCLSFilterRowStatus,
       "etsysFWHTMLFilterTable": etsysFWHTMLFilterTable,
       "etsysFWHTMLFilterEntry": etsysFWHTMLFilterEntry,
       "etsysFWHTMLFilterName": etsysFWHTMLFilterName,
       "etsysFWHTMLFilterType": etsysFWHTMLFilterType,
       "etsysFWHTMLFilterNetwork": etsysFWHTMLFilterNetwork,
       "etsysFWHTMLFilterLogging": etsysFWHTMLFilterLogging,
       "etsysFWHTMLFilterStorageType": etsysFWHTMLFilterStorageType,
       "etsysFWHTMLFilterRowStatus": etsysFWHTMLFilterRowStatus,
       "etsysFWMonitoringObjects": etsysFWMonitoringObjects,
       "etsysFWPolicyRuleTrueNumEntries": etsysFWPolicyRuleTrueNumEntries,
       "etsysFWPolicyRuleTrueLastChange": etsysFWPolicyRuleTrueLastChange,
       "etsysFWPolicyRuleTrueTable": etsysFWPolicyRuleTrueTable,
       "etsysFWPolicyRuleTrueEntry": etsysFWPolicyRuleTrueEntry,
       "etsysFWPolicyRuleTrueIndex": etsysFWPolicyRuleTrueIndex,
       "etsysFWPolicyRuleTrueName": etsysFWPolicyRuleTrueName,
       "etsysFWPolicyRuleTrueEvents": etsysFWPolicyRuleTrueEvents,
       "etsysFWPolicyRuleTrueLastEvent": etsysFWPolicyRuleTrueLastEvent,
       "etsysFWSessionTotalsNumEntries": etsysFWSessionTotalsNumEntries,
       "etsysFWSessionTotalsLastChange": etsysFWSessionTotalsLastChange,
       "etsysFWSessionTotalsTable": etsysFWSessionTotalsTable,
       "etsysFWSessionTotalsEntry": etsysFWSessionTotalsEntry,
       "etsysFWSessTotIndex": etsysFWSessTotIndex,
       "etsysFWSessTotProtocolID": etsysFWSessTotProtocolID,
       "etsysFWSessTotActiveSessions": etsysFWSessTotActiveSessions,
       "etsysFWSessTotPeakSessions": etsysFWSessTotPeakSessions,
       "etsysFWSessTotBlockedSessions": etsysFWSessTotBlockedSessions,
       "etsysFWSessTotLastBlock": etsysFWSessTotLastBlock,
       "etsysFWIpSessionNumEntries": etsysFWIpSessionNumEntries,
       "etsysFWIpSessionLastChange": etsysFWIpSessionLastChange,
       "etsysFWIpSessionTable": etsysFWIpSessionTable,
       "etsysFWIpSessionEntry": etsysFWIpSessionEntry,
       "etsysFWIpSessionIndex": etsysFWIpSessionIndex,
       "etsysFWIpSessionIPVersion": etsysFWIpSessionIPVersion,
       "etsysFWIpSessionSrcAddress": etsysFWIpSessionSrcAddress,
       "etsysFWIpSessionDstAddress": etsysFWIpSessionDstAddress,
       "etsysFWIpSessionSrcPort": etsysFWIpSessionSrcPort,
       "etsysFWIpSessionDstPort": etsysFWIpSessionDstPort,
       "etsysFWIpSessionProtocolID": etsysFWIpSessionProtocolID,
       "etsysFWIpSessionCreation": etsysFWIpSessionCreation,
       "etsysFWAuthAddressNumEntries": etsysFWAuthAddressNumEntries,
       "etsysFWAuthAddressLastChange": etsysFWAuthAddressLastChange,
       "etsysFWAuthAddressTable": etsysFWAuthAddressTable,
       "etsysFWAuthAddressEntry": etsysFWAuthAddressEntry,
       "etsysFWAuthAddressIndex": etsysFWAuthAddressIndex,
       "etsysFWAuthAddressIPVersion": etsysFWAuthAddressIPVersion,
       "etsysFWAuthAddressIPAddress": etsysFWAuthAddressIPAddress,
       "etsysFWAuthAddressGroupName": etsysFWAuthAddressGroupName,
       "etsysFWAuthAddressIdleTime": etsysFWAuthAddressIdleTime,
       "etsysFWDoSBlockedNumEntries": etsysFWDoSBlockedNumEntries,
       "etsysFWDoSBlockedLastChange": etsysFWDoSBlockedLastChange,
       "etsysFWDoSBlockedTable": etsysFWDoSBlockedTable,
       "etsysFWDoSBlockedEntry": etsysFWDoSBlockedEntry,
       "etsysFWDoSAttackName": etsysFWDoSAttackName,
       "etsysFWDoSSrcIPVersion": etsysFWDoSSrcIPVersion,
       "etsysFWDoSSrcIPAddress": etsysFWDoSSrcIPAddress,
       "etsysFWDoSAttackTime": etsysFWDoSAttackTime,
       "etsysFWDoSBlockedAttacks": etsysFWDoSBlockedAttacks,
       "etsysFirewallConformance": etsysFirewallConformance,
       "etsysFirewallGroups": etsysFirewallGroups,
       "etsysFWFirewallEnabledGroup": etsysFWFirewallEnabledGroup,
       "etsysFWFirewallConfigGroup": etsysFWFirewallConfigGroup,
       "etsysFWFirewallIntfGroup": etsysFWFirewallIntfGroup,
       "etsysFWSystemPolicyNameGroup": etsysFWSystemPolicyNameGroup,
       "etsysFWInterfacePolicyGroup": etsysFWInterfacePolicyGroup,
       "etsysFWGroupPolicyGroup": etsysFWGroupPolicyGroup,
       "etsysFWPolicyRuleDefGroup": etsysFWPolicyRuleDefGroup,
       "etsysFWNetworkGroupGroup": etsysFWNetworkGroupGroup,
       "etsysFWNetworkGroup": etsysFWNetworkGroup,
       "etsysFWServiceGroupGroup": etsysFWServiceGroupGroup,
       "etsysFWServiceGroup": etsysFWServiceGroup,
       "etsysFWFilterGroup": etsysFWFilterGroup,
       "etsysFWCLSFilterGroup": etsysFWCLSFilterGroup,
       "etsysFWHTMLFilterGroup": etsysFWHTMLFilterGroup,
       "etsysFWPolicyRuleTrueGroup": etsysFWPolicyRuleTrueGroup,
       "etsysFWSessionTotalsGroup": etsysFWSessionTotalsGroup,
       "etsysFWIpSessionGroup": etsysFWIpSessionGroup,
       "etsysFWAuthAddressGroup": etsysFWAuthAddressGroup,
       "etsysFWDoSBlockedGroup": etsysFWDoSBlockedGroup,
       "etsysFirewallCompliances": etsysFirewallCompliances,
       "etsysFirewallCompliance": etsysFirewallCompliance}
)
