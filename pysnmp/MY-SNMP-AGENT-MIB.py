# SNMP MIB module (MY-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-SNMP-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:28 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 MyTrapType) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "MyTrapType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mySnmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5)
)
mySnmpAgentMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Community(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_MySnmpAgentMIBObjects_ObjectIdentity = ObjectIdentity
mySnmpAgentMIBObjects = _MySnmpAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1)
)
_MySnmpCommunityObjects_ObjectIdentity = ObjectIdentity
mySnmpCommunityObjects = _MySnmpCommunityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1)
)
_MyCommunityMaxNum_Type = Integer32
_MyCommunityMaxNum_Object = MibScalar
myCommunityMaxNum = _MyCommunityMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 1),
    _MyCommunityMaxNum_Type()
)
myCommunityMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myCommunityMaxNum.setStatus("current")
_MyCommunityTable_Object = MibTable
myCommunityTable = _MyCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    myCommunityTable.setStatus("current")
_MyCommunityEntry_Object = MibTableRow
myCommunityEntry = _MyCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1)
)
myCommunityEntry.setIndexNames(
    (0, "MY-SNMP-AGENT-MIB", "myCommunityName"),
)
if mibBuilder.loadTexts:
    myCommunityEntry.setStatus("current")
_MyCommunityName_Type = Community
_MyCommunityName_Object = MibTableColumn
myCommunityName = _MyCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 1),
    _MyCommunityName_Type()
)
myCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myCommunityName.setStatus("current")


class _MyCommunityWritable_Type(Integer32):
    """Custom type myCommunityWritable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("writable", 2))
    )


_MyCommunityWritable_Type.__name__ = "Integer32"
_MyCommunityWritable_Object = MibTableColumn
myCommunityWritable = _MyCommunityWritable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 2),
    _MyCommunityWritable_Type()
)
myCommunityWritable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myCommunityWritable.setStatus("current")
_MyCommunityUserIpAddr_Type = IpAddress
_MyCommunityUserIpAddr_Object = MibTableColumn
myCommunityUserIpAddr = _MyCommunityUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 3),
    _MyCommunityUserIpAddr_Type()
)
myCommunityUserIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myCommunityUserIpAddr.setStatus("current")
_MyCommunityEnableIpAddrAuthen_Type = EnabledStatus
_MyCommunityEnableIpAddrAuthen_Object = MibTableColumn
myCommunityEnableIpAddrAuthen = _MyCommunityEnableIpAddrAuthen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 4),
    _MyCommunityEnableIpAddrAuthen_Type()
)
myCommunityEnableIpAddrAuthen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myCommunityEnableIpAddrAuthen.setStatus("current")
_MyCommunityStatus_Type = RowStatus
_MyCommunityStatus_Object = MibTableColumn
myCommunityStatus = _MyCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 5),
    _MyCommunityStatus_Type()
)
myCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myCommunityStatus.setStatus("current")
_MySnmpTrapObjects_ObjectIdentity = ObjectIdentity
mySnmpTrapObjects = _MySnmpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2)
)
_MyTrapDstMaxNumber_Type = Integer32
_MyTrapDstMaxNumber_Object = MibScalar
myTrapDstMaxNumber = _MyTrapDstMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 1),
    _MyTrapDstMaxNumber_Type()
)
myTrapDstMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myTrapDstMaxNumber.setStatus("current")
_MyTrapDstTable_Object = MibTable
myTrapDstTable = _MyTrapDstTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    myTrapDstTable.setStatus("current")
_MyTrapDstEntry_Object = MibTableRow
myTrapDstEntry = _MyTrapDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1)
)
myTrapDstEntry.setIndexNames(
    (0, "MY-SNMP-AGENT-MIB", "myTrapDstAddr"),
)
if mibBuilder.loadTexts:
    myTrapDstEntry.setStatus("current")
_MyTrapDstAddr_Type = IpAddress
_MyTrapDstAddr_Object = MibTableColumn
myTrapDstAddr = _MyTrapDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 1),
    _MyTrapDstAddr_Type()
)
myTrapDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myTrapDstAddr.setStatus("current")


class _MyTrapDstCommunity_Type(Community):
    """Custom type myTrapDstCommunity based on Community"""
    defaultValue = OctetString("public")


_MyTrapDstCommunity_Object = MibTableColumn
myTrapDstCommunity = _MyTrapDstCommunity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 2),
    _MyTrapDstCommunity_Type()
)
myTrapDstCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTrapDstCommunity.setStatus("current")


class _MyTrapDstSendTrapClass_Type(Integer32):
    """Custom type myTrapDstSendTrapClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1-Trap", 1),
          ("snmpv2c-Trap", 2))
    )


_MyTrapDstSendTrapClass_Type.__name__ = "Integer32"
_MyTrapDstSendTrapClass_Object = MibTableColumn
myTrapDstSendTrapClass = _MyTrapDstSendTrapClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 3),
    _MyTrapDstSendTrapClass_Type()
)
myTrapDstSendTrapClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTrapDstSendTrapClass.setStatus("current")
_MyTrapDstEntryStatus_Type = RowStatus
_MyTrapDstEntryStatus_Object = MibTableColumn
myTrapDstEntryStatus = _MyTrapDstEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 4),
    _MyTrapDstEntryStatus_Type()
)
myTrapDstEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myTrapDstEntryStatus.setStatus("current")
_MyTrapActionTable_Object = MibTable
myTrapActionTable = _MyTrapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    myTrapActionTable.setStatus("current")
_MyTrapActionEntry_Object = MibTableRow
myTrapActionEntry = _MyTrapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3, 1)
)
myTrapActionEntry.setIndexNames(
    (0, "MY-SNMP-AGENT-MIB", "myTrapType"),
)
if mibBuilder.loadTexts:
    myTrapActionEntry.setStatus("current")
_MyTrapType_Type = MyTrapType
_MyTrapType_Object = MibTableColumn
myTrapType = _MyTrapType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3, 1, 1),
    _MyTrapType_Type()
)
myTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myTrapType.setStatus("current")


class _MyTrapAction_Type(Integer32):
    """Custom type myTrapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sendtrap", 2))
    )


_MyTrapAction_Type.__name__ = "Integer32"
_MyTrapAction_Object = MibTableColumn
myTrapAction = _MyTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3, 1, 2),
    _MyTrapAction_Type()
)
myTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTrapAction.setStatus("current")
_MySnmpAgentMIBConformance_ObjectIdentity = ObjectIdentity
mySnmpAgentMIBConformance = _MySnmpAgentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2)
)
_MySnmpAgentMIBCompliances_ObjectIdentity = ObjectIdentity
mySnmpAgentMIBCompliances = _MySnmpAgentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 1)
)
_MySnmpAgentMIBGroups_ObjectIdentity = ObjectIdentity
mySnmpAgentMIBGroups = _MySnmpAgentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 2)
)

# Managed Objects groups

myCommunityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 2, 1)
)
myCommunityMIBGroup.setObjects(
      *(("MY-SNMP-AGENT-MIB", "myCommunityMaxNum"),
        ("MY-SNMP-AGENT-MIB", "myCommunityName"),
        ("MY-SNMP-AGENT-MIB", "myCommunityWritable"),
        ("MY-SNMP-AGENT-MIB", "myCommunityUserIpAddr"),
        ("MY-SNMP-AGENT-MIB", "myCommunityEnableIpAddrAuthen"),
        ("MY-SNMP-AGENT-MIB", "myCommunityStatus"))
)
if mibBuilder.loadTexts:
    myCommunityMIBGroup.setStatus("current")

mySnmpTrapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 2, 2)
)
mySnmpTrapMIBGroup.setObjects(
      *(("MY-SNMP-AGENT-MIB", "myTrapDstSendTrapClass"),
        ("MY-SNMP-AGENT-MIB", "myTrapDstMaxNumber"),
        ("MY-SNMP-AGENT-MIB", "myTrapDstAddr"),
        ("MY-SNMP-AGENT-MIB", "myTrapDstCommunity"),
        ("MY-SNMP-AGENT-MIB", "myTrapDstEntryStatus"),
        ("MY-SNMP-AGENT-MIB", "myTrapType"),
        ("MY-SNMP-AGENT-MIB", "myTrapAction"))
)
if mibBuilder.loadTexts:
    mySnmpTrapMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mySnmpAgentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mySnmpAgentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-SNMP-AGENT-MIB",
    **{"Community": Community,
       "mySnmpAgentMIB": mySnmpAgentMIB,
       "mySnmpAgentMIBObjects": mySnmpAgentMIBObjects,
       "mySnmpCommunityObjects": mySnmpCommunityObjects,
       "myCommunityMaxNum": myCommunityMaxNum,
       "myCommunityTable": myCommunityTable,
       "myCommunityEntry": myCommunityEntry,
       "myCommunityName": myCommunityName,
       "myCommunityWritable": myCommunityWritable,
       "myCommunityUserIpAddr": myCommunityUserIpAddr,
       "myCommunityEnableIpAddrAuthen": myCommunityEnableIpAddrAuthen,
       "myCommunityStatus": myCommunityStatus,
       "mySnmpTrapObjects": mySnmpTrapObjects,
       "myTrapDstMaxNumber": myTrapDstMaxNumber,
       "myTrapDstTable": myTrapDstTable,
       "myTrapDstEntry": myTrapDstEntry,
       "myTrapDstAddr": myTrapDstAddr,
       "myTrapDstCommunity": myTrapDstCommunity,
       "myTrapDstSendTrapClass": myTrapDstSendTrapClass,
       "myTrapDstEntryStatus": myTrapDstEntryStatus,
       "myTrapActionTable": myTrapActionTable,
       "myTrapActionEntry": myTrapActionEntry,
       "myTrapType": myTrapType,
       "myTrapAction": myTrapAction,
       "mySnmpAgentMIBConformance": mySnmpAgentMIBConformance,
       "mySnmpAgentMIBCompliances": mySnmpAgentMIBCompliances,
       "mySnmpAgentMIBCompliance": mySnmpAgentMIBCompliance,
       "mySnmpAgentMIBGroups": mySnmpAgentMIBGroups,
       "myCommunityMIBGroup": myCommunityMIBGroup,
       "mySnmpTrapMIBGroup": mySnmpTrapMIBGroup}
)
