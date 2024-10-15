# SNMP MIB module (MY-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-AP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:18 2024
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
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7)
)
myApMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyApMIBObjects_ObjectIdentity = ObjectIdentity
myApMIBObjects = _MyApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1)
)
_MyApMaxNumber_Type = Integer32
_MyApMaxNumber_Object = MibScalar
myApMaxNumber = _MyApMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 1),
    _MyApMaxNumber_Type()
)
myApMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApMaxNumber.setStatus("current")
_MyApCurrentNumber_Type = Integer32
_MyApCurrentNumber_Object = MibScalar
myApCurrentNumber = _MyApCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 2),
    _MyApCurrentNumber_Type()
)
myApCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApCurrentNumber.setStatus("current")
_MyApPortConfigTable_Object = MibTable
myApPortConfigTable = _MyApPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    myApPortConfigTable.setStatus("obsolete")
_MyApPortConfigEntry_Object = MibTableRow
myApPortConfigEntry = _MyApPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 3, 1)
)
myApPortConfigEntry.setIndexNames(
    (0, "MY-AP-MIB", "myApPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    myApPortConfigEntry.setStatus("obsolete")
_MyApPortConfigPortIndex_Type = IfIndex
_MyApPortConfigPortIndex_Object = MibTableColumn
myApPortConfigPortIndex = _MyApPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 3, 1, 1),
    _MyApPortConfigPortIndex_Type()
)
myApPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myApPortConfigPortIndex.setStatus("obsolete")
_MyApPortConfigApIndex_Type = IfIndex
_MyApPortConfigApIndex_Object = MibTableColumn
myApPortConfigApIndex = _MyApPortConfigApIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 3, 1, 2),
    _MyApPortConfigApIndex_Type()
)
myApPortConfigApIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myApPortConfigApIndex.setStatus("obsolete")
_MyApTable_Object = MibTable
myApTable = _MyApTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    myApTable.setStatus("obsolete")
_MyApEntry_Object = MibTableRow
myApEntry = _MyApEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 4, 1)
)
myApEntry.setIndexNames(
    (0, "MY-AP-MIB", "myApIndex"),
)
if mibBuilder.loadTexts:
    myApEntry.setStatus("obsolete")
_MyApIndex_Type = IfIndex
_MyApIndex_Object = MibTableColumn
myApIndex = _MyApIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 4, 1, 1),
    _MyApIndex_Type()
)
myApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApIndex.setStatus("obsolete")
_MyApMemberAction_Type = MemberMap
_MyApMemberAction_Object = MibTableColumn
myApMemberAction = _MyApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 4, 1, 2),
    _MyApMemberAction_Type()
)
myApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApMemberAction.setStatus("obsolete")
_MyApPossibleMember_Type = MemberMap
_MyApPossibleMember_Object = MibTableColumn
myApPossibleMember = _MyApPossibleMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 4, 1, 3),
    _MyApPossibleMember_Type()
)
myApPossibleMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApPossibleMember.setStatus("obsolete")
_MyApMaxPtNumber_Type = Integer32
_MyApMaxPtNumber_Object = MibTableColumn
myApMaxPtNumber = _MyApMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 4, 1, 4),
    _MyApMaxPtNumber_Type()
)
myApMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApMaxPtNumber.setStatus("obsolete")


class _MyApFlowBalance_Type(Integer32):
    """Custom type myApFlowBalance based on Integer32"""
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
        *(("destination-ip", 5),
          ("destination-mac", 2),
          ("source-ip", 4),
          ("source-mac", 1),
          ("src-dest-ip", 6),
          ("src-dest-mac", 3),
          ("src-dest-port", 7),
          ("unknown", 0))
    )


_MyApFlowBalance_Type.__name__ = "Integer32"
_MyApFlowBalance_Object = MibScalar
myApFlowBalance = _MyApFlowBalance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 5),
    _MyApFlowBalance_Type()
)
myApFlowBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myApFlowBalance.setStatus("current")
_MyApConfigTable_Object = MibTable
myApConfigTable = _MyApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    myApConfigTable.setStatus("current")
_MyApConfigEntry_Object = MibTableRow
myApConfigEntry = _MyApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1)
)
myApConfigEntry.setIndexNames(
    (0, "MY-AP-MIB", "myApConfigNumber"),
)
if mibBuilder.loadTexts:
    myApConfigEntry.setStatus("current")
_MyApConfigNumber_Type = Integer32
_MyApConfigNumber_Object = MibTableColumn
myApConfigNumber = _MyApConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1, 1),
    _MyApConfigNumber_Type()
)
myApConfigNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myApConfigNumber.setStatus("current")
_MyApConfigIndex_Type = IfIndex
_MyApConfigIndex_Object = MibTableColumn
myApConfigIndex = _MyApConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1, 2),
    _MyApConfigIndex_Type()
)
myApConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApConfigIndex.setStatus("current")
_MyApConfigMaxPtNumber_Type = Integer32
_MyApConfigMaxPtNumber_Object = MibTableColumn
myApConfigMaxPtNumber = _MyApConfigMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1, 3),
    _MyApConfigMaxPtNumber_Type()
)
myApConfigMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApConfigMaxPtNumber.setStatus("current")
_MyApConfigCurrentPtNumber_Type = Integer32
_MyApConfigCurrentPtNumber_Object = MibTableColumn
myApConfigCurrentPtNumber = _MyApConfigCurrentPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1, 4),
    _MyApConfigCurrentPtNumber_Type()
)
myApConfigCurrentPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApConfigCurrentPtNumber.setStatus("current")
_MyApConfigPortMember_Type = PortList
_MyApConfigPortMember_Object = MibTableColumn
myApConfigPortMember = _MyApConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1, 5),
    _MyApConfigPortMember_Type()
)
myApConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApConfigPortMember.setStatus("current")
_MyApConfigAction_Type = Integer32
_MyApConfigAction_Object = MibTableColumn
myApConfigAction = _MyApConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 6, 1, 6),
    _MyApConfigAction_Type()
)
myApConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myApConfigAction.setStatus("current")
_MyApPortMemberTable_Object = MibTable
myApPortMemberTable = _MyApPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 7)
)
if mibBuilder.loadTexts:
    myApPortMemberTable.setStatus("current")
_MyApPortMemberEntry_Object = MibTableRow
myApPortMemberEntry = _MyApPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 7, 1)
)
myApPortMemberEntry.setIndexNames(
    (0, "MY-AP-MIB", "myApPortMemberPortIndex"),
)
if mibBuilder.loadTexts:
    myApPortMemberEntry.setStatus("current")
_MyApPortMemberPortIndex_Type = IfIndex
_MyApPortMemberPortIndex_Object = MibTableColumn
myApPortMemberPortIndex = _MyApPortMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 7, 1, 1),
    _MyApPortMemberPortIndex_Type()
)
myApPortMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myApPortMemberPortIndex.setStatus("current")
_MyApPortMemberApNumber_Type = Integer32
_MyApPortMemberApNumber_Object = MibTableColumn
myApPortMemberApNumber = _MyApPortMemberApNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 7, 1, 2),
    _MyApPortMemberApNumber_Type()
)
myApPortMemberApNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myApPortMemberApNumber.setStatus("current")
_MyApPortMemberAction_Type = Integer32
_MyApPortMemberAction_Object = MibTableColumn
myApPortMemberAction = _MyApPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 1, 7, 1, 3),
    _MyApPortMemberAction_Type()
)
myApPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myApPortMemberAction.setStatus("current")
_MyApMIBConformance_ObjectIdentity = ObjectIdentity
myApMIBConformance = _MyApMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 2)
)
_MyApMIBCompliances_ObjectIdentity = ObjectIdentity
myApMIBCompliances = _MyApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 2, 1)
)
_MyApMIBGroups_ObjectIdentity = ObjectIdentity
myApMIBGroups = _MyApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 2, 2)
)

# Managed Objects groups

myApMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 2, 2, 1)
)
myApMIBGroup.setObjects(
      *(("MY-AP-MIB", "myApMaxNumber"),
        ("MY-AP-MIB", "myApCurrentNumber"),
        ("MY-AP-MIB", "myApPortConfigApIndex"),
        ("MY-AP-MIB", "myApIndex"),
        ("MY-AP-MIB", "myApMemberAction"),
        ("MY-AP-MIB", "myApMaxPtNumber"),
        ("MY-AP-MIB", "myApFlowBalance"),
        ("MY-AP-MIB", "myApConfigNumber"),
        ("MY-AP-MIB", "myApConfigIndex"),
        ("MY-AP-MIB", "myApConfigMaxPtNumber"),
        ("MY-AP-MIB", "myApConfigCurrentPtNumber"),
        ("MY-AP-MIB", "myApConfigPortMember"),
        ("MY-AP-MIB", "myApConfigAction"),
        ("MY-AP-MIB", "myApPortMemberPortIndex"),
        ("MY-AP-MIB", "myApPortMemberApNumber"),
        ("MY-AP-MIB", "myApPortMemberAction"))
)
if mibBuilder.loadTexts:
    myApMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myApMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-AP-MIB",
    **{"myApMIB": myApMIB,
       "myApMIBObjects": myApMIBObjects,
       "myApMaxNumber": myApMaxNumber,
       "myApCurrentNumber": myApCurrentNumber,
       "myApPortConfigTable": myApPortConfigTable,
       "myApPortConfigEntry": myApPortConfigEntry,
       "myApPortConfigPortIndex": myApPortConfigPortIndex,
       "myApPortConfigApIndex": myApPortConfigApIndex,
       "myApTable": myApTable,
       "myApEntry": myApEntry,
       "myApIndex": myApIndex,
       "myApMemberAction": myApMemberAction,
       "myApPossibleMember": myApPossibleMember,
       "myApMaxPtNumber": myApMaxPtNumber,
       "myApFlowBalance": myApFlowBalance,
       "myApConfigTable": myApConfigTable,
       "myApConfigEntry": myApConfigEntry,
       "myApConfigNumber": myApConfigNumber,
       "myApConfigIndex": myApConfigIndex,
       "myApConfigMaxPtNumber": myApConfigMaxPtNumber,
       "myApConfigCurrentPtNumber": myApConfigCurrentPtNumber,
       "myApConfigPortMember": myApConfigPortMember,
       "myApConfigAction": myApConfigAction,
       "myApPortMemberTable": myApPortMemberTable,
       "myApPortMemberEntry": myApPortMemberEntry,
       "myApPortMemberPortIndex": myApPortMemberPortIndex,
       "myApPortMemberApNumber": myApPortMemberApNumber,
       "myApPortMemberAction": myApPortMemberAction,
       "myApMIBConformance": myApMIBConformance,
       "myApMIBCompliances": myApMIBCompliances,
       "myApMIBCompliance": myApMIBCompliance,
       "myApMIBGroups": myApMIBGroups,
       "myApMIBGroup": myApMIBGroup}
)
