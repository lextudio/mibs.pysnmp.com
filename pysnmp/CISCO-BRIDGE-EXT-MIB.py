# SNMP MIB module (CISCO-BRIDGE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BRIDGE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:23 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPortList,
 CiscoPortListRange) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPortList",
    "CiscoPortListRange")

(VlanId,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex")

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

ciscoBridgeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401)
)
ciscoBridgeExtMIB.setRevisions(
        ("2008-05-22 00:00",
         "2005-04-07 00:00",
         "2004-12-03 00:00",
         "2004-08-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CbExtMIBNotifications_ObjectIdentity = ObjectIdentity
cbExtMIBNotifications = _CbExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 0)
)
_CbExtMIBObjects_ObjectIdentity = ObjectIdentity
cbExtMIBObjects = _CbExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1)
)
_CbeDot1dTp_ObjectIdentity = ObjectIdentity
cbeDot1dTp = _CbeDot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1)
)


class _CbeDot1dTpGlobalAgingTime_Type(Unsigned32):
    """Custom type cbeDot1dTpGlobalAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_CbeDot1dTpGlobalAgingTime_Type.__name__ = "Unsigned32"
_CbeDot1dTpGlobalAgingTime_Object = MibScalar
cbeDot1dTpGlobalAgingTime = _CbeDot1dTpGlobalAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 1),
    _CbeDot1dTpGlobalAgingTime_Type()
)
cbeDot1dTpGlobalAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbeDot1dTpGlobalAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cbeDot1dTpGlobalAgingTime.setUnits("seconds")
_CbeDot1dTpVlanTable_Object = MibTable
cbeDot1dTpVlanTable = _CbeDot1dTpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cbeDot1dTpVlanTable.setStatus("current")
_CbeDot1dTpVlanEntry_Object = MibTableRow
cbeDot1dTpVlanEntry = _CbeDot1dTpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 2, 1)
)
cbeDot1dTpVlanEntry.setIndexNames(
    (0, "CISCO-BRIDGE-EXT-MIB", "cbeDot1dTpVlanIndex"),
)
if mibBuilder.loadTexts:
    cbeDot1dTpVlanEntry.setStatus("current")
_CbeDot1dTpVlanIndex_Type = VlanIndex
_CbeDot1dTpVlanIndex_Object = MibTableColumn
cbeDot1dTpVlanIndex = _CbeDot1dTpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 2, 1, 1),
    _CbeDot1dTpVlanIndex_Type()
)
cbeDot1dTpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbeDot1dTpVlanIndex.setStatus("current")


class _CbeDot1dTpVlanAgingTime_Type(Unsigned32):
    """Custom type cbeDot1dTpVlanAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_CbeDot1dTpVlanAgingTime_Type.__name__ = "Unsigned32"
_CbeDot1dTpVlanAgingTime_Object = MibTableColumn
cbeDot1dTpVlanAgingTime = _CbeDot1dTpVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 2, 1, 2),
    _CbeDot1dTpVlanAgingTime_Type()
)
cbeDot1dTpVlanAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbeDot1dTpVlanAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cbeDot1dTpVlanAgingTime.setUnits("seconds")


class _CbeDot1dTpVlanAgingFromGlobal_Type(TruthValue):
    """Custom type cbeDot1dTpVlanAgingFromGlobal based on TruthValue"""


_CbeDot1dTpVlanAgingFromGlobal_Object = MibTableColumn
cbeDot1dTpVlanAgingFromGlobal = _CbeDot1dTpVlanAgingFromGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 2, 1, 3),
    _CbeDot1dTpVlanAgingFromGlobal_Type()
)
cbeDot1dTpVlanAgingFromGlobal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbeDot1dTpVlanAgingFromGlobal.setStatus("current")
_CbeDot1dTpVlanRowStatus_Type = RowStatus
_CbeDot1dTpVlanRowStatus_Object = MibTableColumn
cbeDot1dTpVlanRowStatus = _CbeDot1dTpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 1, 2, 1, 4),
    _CbeDot1dTpVlanRowStatus_Type()
)
cbeDot1dTpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbeDot1dTpVlanRowStatus.setStatus("current")
_CbeDot1dStatic_ObjectIdentity = ObjectIdentity
cbeDot1dStatic = _CbeDot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2)
)
_CbeDot1dStaticTable_Object = MibTable
cbeDot1dStaticTable = _CbeDot1dStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cbeDot1dStaticTable.setStatus("current")
_CbeDot1dStaticEntry_Object = MibTableRow
cbeDot1dStaticEntry = _CbeDot1dStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1)
)
cbeDot1dStaticEntry.setIndexNames(
    (0, "CISCO-BRIDGE-EXT-MIB", "cbeDot1dVlanIndex"),
    (0, "CISCO-BRIDGE-EXT-MIB", "cbeDot1dStaticAddress"),
    (0, "CISCO-BRIDGE-EXT-MIB", "cbeDot1dStaticReceivePort"),
    (0, "CISCO-BRIDGE-EXT-MIB", "cbeDot1dStaticPortRangeIndex"),
)
if mibBuilder.loadTexts:
    cbeDot1dStaticEntry.setStatus("current")
_CbeDot1dVlanIndex_Type = VlanIndex
_CbeDot1dVlanIndex_Object = MibTableColumn
cbeDot1dVlanIndex = _CbeDot1dVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1, 1),
    _CbeDot1dVlanIndex_Type()
)
cbeDot1dVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbeDot1dVlanIndex.setStatus("current")
_CbeDot1dStaticAddress_Type = MacAddress
_CbeDot1dStaticAddress_Object = MibTableColumn
cbeDot1dStaticAddress = _CbeDot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1, 2),
    _CbeDot1dStaticAddress_Type()
)
cbeDot1dStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbeDot1dStaticAddress.setStatus("current")


class _CbeDot1dStaticReceivePort_Type(Integer32):
    """Custom type cbeDot1dStaticReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbeDot1dStaticReceivePort_Type.__name__ = "Integer32"
_CbeDot1dStaticReceivePort_Object = MibTableColumn
cbeDot1dStaticReceivePort = _CbeDot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1, 3),
    _CbeDot1dStaticReceivePort_Type()
)
cbeDot1dStaticReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbeDot1dStaticReceivePort.setStatus("current")
_CbeDot1dStaticPortRangeIndex_Type = CiscoPortListRange
_CbeDot1dStaticPortRangeIndex_Object = MibTableColumn
cbeDot1dStaticPortRangeIndex = _CbeDot1dStaticPortRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1, 4),
    _CbeDot1dStaticPortRangeIndex_Type()
)
cbeDot1dStaticPortRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbeDot1dStaticPortRangeIndex.setStatus("current")
_CbeDot1dStaticAllowedToGoTo_Type = CiscoPortList
_CbeDot1dStaticAllowedToGoTo_Object = MibTableColumn
cbeDot1dStaticAllowedToGoTo = _CbeDot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1, 5),
    _CbeDot1dStaticAllowedToGoTo_Type()
)
cbeDot1dStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbeDot1dStaticAllowedToGoTo.setStatus("current")


class _CbeDot1dStaticStatus_Type(Integer32):
    """Custom type cbeDot1dStaticStatus based on Integer32"""
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


_CbeDot1dStaticStatus_Type.__name__ = "Integer32"
_CbeDot1dStaticStatus_Object = MibTableColumn
cbeDot1dStaticStatus = _CbeDot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 2, 1, 1, 6),
    _CbeDot1dStaticStatus_Type()
)
cbeDot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbeDot1dStaticStatus.setStatus("current")
_CbeDot1dVlan_ObjectIdentity = ObjectIdentity
cbeDot1dVlan = _CbeDot1dVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 3)
)
_CbeDot1dVlanTable_Object = MibTable
cbeDot1dVlanTable = _CbeDot1dVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cbeDot1dVlanTable.setStatus("current")
_CbeDot1dVlanEntry_Object = MibTableRow
cbeDot1dVlanEntry = _CbeDot1dVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 3, 1, 1)
)
cbeDot1dVlanEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    cbeDot1dVlanEntry.setStatus("current")
_CbeDot1dVlanOperVlan_Type = VlanId
_CbeDot1dVlanOperVlan_Object = MibTableColumn
cbeDot1dVlanOperVlan = _CbeDot1dVlanOperVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 1, 3, 1, 1, 1),
    _CbeDot1dVlanOperVlan_Type()
)
cbeDot1dVlanOperVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbeDot1dVlanOperVlan.setStatus("current")
_CbExtMIBConformance_ObjectIdentity = ObjectIdentity
cbExtMIBConformance = _CbExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2)
)
_CbExtMIBCompliances_ObjectIdentity = ObjectIdentity
cbExtMIBCompliances = _CbExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 1)
)
_CbExtMIBGroups_ObjectIdentity = ObjectIdentity
cbExtMIBGroups = _CbExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 2)
)

# Managed Objects groups

cbeDot1dTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 2, 1)
)
cbeDot1dTpGroup.setObjects(
      *(("CISCO-BRIDGE-EXT-MIB", "cbeDot1dTpGlobalAgingTime"),
        ("CISCO-BRIDGE-EXT-MIB", "cbeDot1dTpVlanAgingFromGlobal"))
)
if mibBuilder.loadTexts:
    cbeDot1dTpGroup.setStatus("current")

cbeDot1dTpVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 2, 2)
)
cbeDot1dTpVlanGroup.setObjects(
      *(("CISCO-BRIDGE-EXT-MIB", "cbeDot1dTpVlanAgingTime"),
        ("CISCO-BRIDGE-EXT-MIB", "cbeDot1dTpVlanRowStatus"))
)
if mibBuilder.loadTexts:
    cbeDot1dTpVlanGroup.setStatus("current")

cbeDot1dStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 2, 3)
)
cbeDot1dStaticGroup.setObjects(
      *(("CISCO-BRIDGE-EXT-MIB", "cbeDot1dStaticAllowedToGoTo"),
        ("CISCO-BRIDGE-EXT-MIB", "cbeDot1dStaticStatus"))
)
if mibBuilder.loadTexts:
    cbeDot1dStaticGroup.setStatus("current")

cbeDot1dOperVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 2, 4)
)
cbeDot1dOperVlanGroup.setObjects(
    ("CISCO-BRIDGE-EXT-MIB", "cbeDot1dVlanOperVlan")
)
if mibBuilder.loadTexts:
    cbeDot1dOperVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cbExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cbExtMIBCompliance.setStatus(
        "deprecated"
    )

cbExtMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cbExtMIBCompliance2.setStatus(
        "deprecated"
    )

cbExtMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 401, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cbExtMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BRIDGE-EXT-MIB",
    **{"ciscoBridgeExtMIB": ciscoBridgeExtMIB,
       "cbExtMIBNotifications": cbExtMIBNotifications,
       "cbExtMIBObjects": cbExtMIBObjects,
       "cbeDot1dTp": cbeDot1dTp,
       "cbeDot1dTpGlobalAgingTime": cbeDot1dTpGlobalAgingTime,
       "cbeDot1dTpVlanTable": cbeDot1dTpVlanTable,
       "cbeDot1dTpVlanEntry": cbeDot1dTpVlanEntry,
       "cbeDot1dTpVlanIndex": cbeDot1dTpVlanIndex,
       "cbeDot1dTpVlanAgingTime": cbeDot1dTpVlanAgingTime,
       "cbeDot1dTpVlanAgingFromGlobal": cbeDot1dTpVlanAgingFromGlobal,
       "cbeDot1dTpVlanRowStatus": cbeDot1dTpVlanRowStatus,
       "cbeDot1dStatic": cbeDot1dStatic,
       "cbeDot1dStaticTable": cbeDot1dStaticTable,
       "cbeDot1dStaticEntry": cbeDot1dStaticEntry,
       "cbeDot1dVlanIndex": cbeDot1dVlanIndex,
       "cbeDot1dStaticAddress": cbeDot1dStaticAddress,
       "cbeDot1dStaticReceivePort": cbeDot1dStaticReceivePort,
       "cbeDot1dStaticPortRangeIndex": cbeDot1dStaticPortRangeIndex,
       "cbeDot1dStaticAllowedToGoTo": cbeDot1dStaticAllowedToGoTo,
       "cbeDot1dStaticStatus": cbeDot1dStaticStatus,
       "cbeDot1dVlan": cbeDot1dVlan,
       "cbeDot1dVlanTable": cbeDot1dVlanTable,
       "cbeDot1dVlanEntry": cbeDot1dVlanEntry,
       "cbeDot1dVlanOperVlan": cbeDot1dVlanOperVlan,
       "cbExtMIBConformance": cbExtMIBConformance,
       "cbExtMIBCompliances": cbExtMIBCompliances,
       "cbExtMIBCompliance": cbExtMIBCompliance,
       "cbExtMIBCompliance2": cbExtMIBCompliance2,
       "cbExtMIBCompliance3": cbExtMIBCompliance3,
       "cbExtMIBGroups": cbExtMIBGroups,
       "cbeDot1dTpGroup": cbeDot1dTpGroup,
       "cbeDot1dTpVlanGroup": cbeDot1dTpVlanGroup,
       "cbeDot1dStaticGroup": cbeDot1dStaticGroup,
       "cbeDot1dOperVlanGroup": cbeDot1dOperVlanGroup}
)
