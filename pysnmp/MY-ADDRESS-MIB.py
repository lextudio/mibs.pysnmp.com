# SNMP MIB module (MY-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:15 2024
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
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

myAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22)
)
myAddressMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyAddressMIBObjects_ObjectIdentity = ObjectIdentity
myAddressMIBObjects = _MyAddressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1)
)
_MyAddressManagementObjects_ObjectIdentity = ObjectIdentity
myAddressManagementObjects = _MyAddressManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1)
)
_MyDynamicAddressCurrentNum_Type = Integer32
_MyDynamicAddressCurrentNum_Object = MibScalar
myDynamicAddressCurrentNum = _MyDynamicAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 1),
    _MyDynamicAddressCurrentNum_Type()
)
myDynamicAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDynamicAddressCurrentNum.setStatus("current")
_MyStaticAddressCurrentNum_Type = Integer32
_MyStaticAddressCurrentNum_Object = MibScalar
myStaticAddressCurrentNum = _MyStaticAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 2),
    _MyStaticAddressCurrentNum_Type()
)
myStaticAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStaticAddressCurrentNum.setStatus("current")
_MyFilterAddressCurrentNum_Type = Integer32
_MyFilterAddressCurrentNum_Object = MibScalar
myFilterAddressCurrentNum = _MyFilterAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 3),
    _MyFilterAddressCurrentNum_Type()
)
myFilterAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFilterAddressCurrentNum.setStatus("current")
_MyAddressAvailableNum_Type = Integer32
_MyAddressAvailableNum_Object = MibScalar
myAddressAvailableNum = _MyAddressAvailableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 4),
    _MyAddressAvailableNum_Type()
)
myAddressAvailableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAddressAvailableNum.setStatus("current")
_MyMacAddressTable_Object = MibTable
myMacAddressTable = _MyMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5)
)
if mibBuilder.loadTexts:
    myMacAddressTable.setStatus("current")
_MyMacAddressEntry_Object = MibTableRow
myMacAddressEntry = _MyMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1)
)
myMacAddressEntry.setIndexNames(
    (0, "MY-ADDRESS-MIB", "myMacAddressFdbId"),
    (0, "MY-ADDRESS-MIB", "myMacAddress"),
)
if mibBuilder.loadTexts:
    myMacAddressEntry.setStatus("current")
_MyMacAddressFdbId_Type = Unsigned32
_MyMacAddressFdbId_Object = MibTableColumn
myMacAddressFdbId = _MyMacAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 1),
    _MyMacAddressFdbId_Type()
)
myMacAddressFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacAddressFdbId.setStatus("current")
_MyMacAddress_Type = MacAddress
_MyMacAddress_Object = MibTableColumn
myMacAddress = _MyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 2),
    _MyMacAddress_Type()
)
myMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacAddress.setStatus("current")
_MyMacAddressPort_Type = IfIndex
_MyMacAddressPort_Object = MibTableColumn
myMacAddressPort = _MyMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 3),
    _MyMacAddressPort_Type()
)
myMacAddressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMacAddressPort.setStatus("current")


class _MyMacAddressType_Type(Integer32):
    """Custom type myMacAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("filter", 3),
          ("static", 2))
    )


_MyMacAddressType_Type.__name__ = "Integer32"
_MyMacAddressType_Object = MibTableColumn
myMacAddressType = _MyMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 4),
    _MyMacAddressType_Type()
)
myMacAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMacAddressType.setStatus("current")
_MyMacAddressStatus_Type = RowStatus
_MyMacAddressStatus_Object = MibTableColumn
myMacAddressStatus = _MyMacAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 5),
    _MyMacAddressStatus_Type()
)
myMacAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myMacAddressStatus.setStatus("current")
_MyAddressNotificationObjects_ObjectIdentity = ObjectIdentity
myAddressNotificationObjects = _MyAddressNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2)
)
_MyMacNotiGlobalEnabled_Type = EnabledStatus
_MyMacNotiGlobalEnabled_Object = MibScalar
myMacNotiGlobalEnabled = _MyMacNotiGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 1),
    _MyMacNotiGlobalEnabled_Type()
)
myMacNotiGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMacNotiGlobalEnabled.setStatus("current")


class _MyMacNotificationInterval_Type(Unsigned32):
    """Custom type myMacNotificationInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MyMacNotificationInterval_Type.__name__ = "Unsigned32"
_MyMacNotificationInterval_Object = MibScalar
myMacNotificationInterval = _MyMacNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 2),
    _MyMacNotificationInterval_Type()
)
myMacNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMacNotificationInterval.setStatus("current")


class _MyMacNotiHisTableMaxLength_Type(Unsigned32):
    """Custom type myMacNotiHisTableMaxLength based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MyMacNotiHisTableMaxLength_Type.__name__ = "Unsigned32"
_MyMacNotiHisTableMaxLength_Object = MibScalar
myMacNotiHisTableMaxLength = _MyMacNotiHisTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 3),
    _MyMacNotiHisTableMaxLength_Type()
)
myMacNotiHisTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMacNotiHisTableMaxLength.setStatus("current")
_MyMacNotiHisTableCurrentLength_Type = Unsigned32
_MyMacNotiHisTableCurrentLength_Object = MibScalar
myMacNotiHisTableCurrentLength = _MyMacNotiHisTableCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 4),
    _MyMacNotiHisTableCurrentLength_Type()
)
myMacNotiHisTableCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacNotiHisTableCurrentLength.setStatus("current")
_MyMacNotiHisTable_Object = MibTable
myMacNotiHisTable = _MyMacNotiHisTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5)
)
if mibBuilder.loadTexts:
    myMacNotiHisTable.setStatus("current")
_MyMacNotiHisEntry_Object = MibTableRow
myMacNotiHisEntry = _MyMacNotiHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1)
)
myMacNotiHisEntry.setIndexNames(
    (0, "MY-ADDRESS-MIB", "myMacNotiHisIndex"),
)
if mibBuilder.loadTexts:
    myMacNotiHisEntry.setStatus("current")


class _MyMacNotiHisIndex_Type(Unsigned32):
    """Custom type myMacNotiHisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MyMacNotiHisIndex_Type.__name__ = "Unsigned32"
_MyMacNotiHisIndex_Object = MibTableColumn
myMacNotiHisIndex = _MyMacNotiHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1, 1),
    _MyMacNotiHisIndex_Type()
)
myMacNotiHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacNotiHisIndex.setStatus("current")


class _MyMacNotiHisMacChangedMsg_Type(OctetString):
    """Custom type myMacNotiHisMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_MyMacNotiHisMacChangedMsg_Type.__name__ = "OctetString"
_MyMacNotiHisMacChangedMsg_Object = MibTableColumn
myMacNotiHisMacChangedMsg = _MyMacNotiHisMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1, 2),
    _MyMacNotiHisMacChangedMsg_Type()
)
myMacNotiHisMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacNotiHisMacChangedMsg.setStatus("current")
_MyMacNotiHisTimestamp_Type = TimeStamp
_MyMacNotiHisTimestamp_Object = MibTableColumn
myMacNotiHisTimestamp = _MyMacNotiHisTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1, 3),
    _MyMacNotiHisTimestamp_Type()
)
myMacNotiHisTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacNotiHisTimestamp.setStatus("current")
_MyMacNotiIfCfgTable_Object = MibTable
myMacNotiIfCfgTable = _MyMacNotiIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6)
)
if mibBuilder.loadTexts:
    myMacNotiIfCfgTable.setStatus("current")
_MyMacNotiIfCfgEntry_Object = MibTableRow
myMacNotiIfCfgEntry = _MyMacNotiIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1)
)
myMacNotiIfCfgEntry.setIndexNames(
    (0, "MY-ADDRESS-MIB", "myMacNotiIfIndex"),
)
if mibBuilder.loadTexts:
    myMacNotiIfCfgEntry.setStatus("current")
_MyMacNotiIfIndex_Type = IfIndex
_MyMacNotiIfIndex_Object = MibTableColumn
myMacNotiIfIndex = _MyMacNotiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1, 1),
    _MyMacNotiIfIndex_Type()
)
myMacNotiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMacNotiIfIndex.setStatus("current")


class _MyIfMacAddrLearntEnable_Type(EnabledStatus):
    """Custom type myIfMacAddrLearntEnable based on EnabledStatus"""


_MyIfMacAddrLearntEnable_Object = MibTableColumn
myIfMacAddrLearntEnable = _MyIfMacAddrLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1, 2),
    _MyIfMacAddrLearntEnable_Type()
)
myIfMacAddrLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfMacAddrLearntEnable.setStatus("current")


class _MyIfMacAddrRemovedEnable_Type(EnabledStatus):
    """Custom type myIfMacAddrRemovedEnable based on EnabledStatus"""


_MyIfMacAddrRemovedEnable_Object = MibTableColumn
myIfMacAddrRemovedEnable = _MyIfMacAddrRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1, 3),
    _MyIfMacAddrRemovedEnable_Type()
)
myIfMacAddrRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfMacAddrRemovedEnable.setStatus("current")
_MyAddressTraps_ObjectIdentity = ObjectIdentity
myAddressTraps = _MyAddressTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 2)
)
_MyAddressMIBConformance_ObjectIdentity = ObjectIdentity
myAddressMIBConformance = _MyAddressMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3)
)
_MyAddressMIBCompliances_ObjectIdentity = ObjectIdentity
myAddressMIBCompliances = _MyAddressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 1)
)
_MyAddressMIBGroups_ObjectIdentity = ObjectIdentity
myAddressMIBGroups = _MyAddressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 2)
)

# Managed Objects groups

myMacAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 2, 1)
)
myMacAddressMIBGroup.setObjects(
      *(("MY-ADDRESS-MIB", "myDynamicAddressCurrentNum"),
        ("MY-ADDRESS-MIB", "myStaticAddressCurrentNum"),
        ("MY-ADDRESS-MIB", "myFilterAddressCurrentNum"),
        ("MY-ADDRESS-MIB", "myAddressAvailableNum"),
        ("MY-ADDRESS-MIB", "myMacAddressFdbId"),
        ("MY-ADDRESS-MIB", "myMacAddress"),
        ("MY-ADDRESS-MIB", "myMacAddressPort"),
        ("MY-ADDRESS-MIB", "myMacAddressType"),
        ("MY-ADDRESS-MIB", "myMacAddressStatus"))
)
if mibBuilder.loadTexts:
    myMacAddressMIBGroup.setStatus("current")

myAddressNotificationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 2, 2)
)
myAddressNotificationMIBGroup.setObjects(
      *(("MY-ADDRESS-MIB", "myMacNotiGlobalEnabled"),
        ("MY-ADDRESS-MIB", "myMacNotificationInterval"),
        ("MY-ADDRESS-MIB", "myMacNotiHisTableMaxLength"),
        ("MY-ADDRESS-MIB", "myMacNotiHisTableCurrentLength"),
        ("MY-ADDRESS-MIB", "myMacNotiHisIndex"),
        ("MY-ADDRESS-MIB", "myMacNotiHisMacChangedMsg"),
        ("MY-ADDRESS-MIB", "myMacNotiHisTimestamp"),
        ("MY-ADDRESS-MIB", "myMacNotiIfIndex"),
        ("MY-ADDRESS-MIB", "myIfMacAddrLearntEnable"),
        ("MY-ADDRESS-MIB", "myIfMacAddrRemovedEnable"))
)
if mibBuilder.loadTexts:
    myAddressNotificationMIBGroup.setStatus("current")


# Notification objects

macChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 2, 1)
)
macChangedNotification.setObjects(
    ("MY-ADDRESS-MIB", "myMacNotiHisMacChangedMsg")
)
if mibBuilder.loadTexts:
    macChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myAddressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    myAddressMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-ADDRESS-MIB",
    **{"myAddressMIB": myAddressMIB,
       "myAddressMIBObjects": myAddressMIBObjects,
       "myAddressManagementObjects": myAddressManagementObjects,
       "myDynamicAddressCurrentNum": myDynamicAddressCurrentNum,
       "myStaticAddressCurrentNum": myStaticAddressCurrentNum,
       "myFilterAddressCurrentNum": myFilterAddressCurrentNum,
       "myAddressAvailableNum": myAddressAvailableNum,
       "myMacAddressTable": myMacAddressTable,
       "myMacAddressEntry": myMacAddressEntry,
       "myMacAddressFdbId": myMacAddressFdbId,
       "myMacAddress": myMacAddress,
       "myMacAddressPort": myMacAddressPort,
       "myMacAddressType": myMacAddressType,
       "myMacAddressStatus": myMacAddressStatus,
       "myAddressNotificationObjects": myAddressNotificationObjects,
       "myMacNotiGlobalEnabled": myMacNotiGlobalEnabled,
       "myMacNotificationInterval": myMacNotificationInterval,
       "myMacNotiHisTableMaxLength": myMacNotiHisTableMaxLength,
       "myMacNotiHisTableCurrentLength": myMacNotiHisTableCurrentLength,
       "myMacNotiHisTable": myMacNotiHisTable,
       "myMacNotiHisEntry": myMacNotiHisEntry,
       "myMacNotiHisIndex": myMacNotiHisIndex,
       "myMacNotiHisMacChangedMsg": myMacNotiHisMacChangedMsg,
       "myMacNotiHisTimestamp": myMacNotiHisTimestamp,
       "myMacNotiIfCfgTable": myMacNotiIfCfgTable,
       "myMacNotiIfCfgEntry": myMacNotiIfCfgEntry,
       "myMacNotiIfIndex": myMacNotiIfIndex,
       "myIfMacAddrLearntEnable": myIfMacAddrLearntEnable,
       "myIfMacAddrRemovedEnable": myIfMacAddrRemovedEnable,
       "myAddressTraps": myAddressTraps,
       "macChangedNotification": macChangedNotification,
       "myAddressMIBConformance": myAddressMIBConformance,
       "myAddressMIBCompliances": myAddressMIBCompliances,
       "myAddressMIBCompliance": myAddressMIBCompliance,
       "myAddressMIBGroups": myAddressMIBGroups,
       "myMacAddressMIBGroup": myMacAddressMIBGroup,
       "myAddressNotificationMIBGroup": myAddressNotificationMIBGroup}
)
