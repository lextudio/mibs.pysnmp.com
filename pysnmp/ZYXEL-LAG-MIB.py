# SNMP MIB module (ZYXEL-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:11 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelLinkAggregation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelAggregationSetup_ObjectIdentity = ObjectIdentity
zyxelAggregationSetup = _ZyxelAggregationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1)
)
_ZyAggregationState_Type = EnabledStatus
_ZyAggregationState_Object = MibScalar
zyAggregationState = _ZyAggregationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 1),
    _ZyAggregationState_Type()
)
zyAggregationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationState.setStatus("current")
_ZyAggregationSysPriority_Type = Integer32
_ZyAggregationSysPriority_Object = MibScalar
zyAggregationSysPriority = _ZyAggregationSysPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 2),
    _ZyAggregationSysPriority_Type()
)
zyAggregationSysPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationSysPriority.setStatus("current")
_ZyxelAggregationGroupTable_Object = MibTable
zyxelAggregationGroupTable = _ZyxelAggregationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelAggregationGroupTable.setStatus("current")
_ZyxelAggregationGroupEntry_Object = MibTableRow
zyxelAggregationGroupEntry = _ZyxelAggregationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 3, 1)
)
zyxelAggregationGroupEntry.setIndexNames(
    (0, "ZYXEL-LAG-MIB", "zyAggregationGroupIndex"),
)
if mibBuilder.loadTexts:
    zyxelAggregationGroupEntry.setStatus("current")
_ZyAggregationGroupIndex_Type = Integer32
_ZyAggregationGroupIndex_Object = MibTableColumn
zyAggregationGroupIndex = _ZyAggregationGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 3, 1, 1),
    _ZyAggregationGroupIndex_Type()
)
zyAggregationGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAggregationGroupIndex.setStatus("current")
_ZyAggregationGroupState_Type = EnabledStatus
_ZyAggregationGroupState_Object = MibTableColumn
zyAggregationGroupState = _ZyAggregationGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 3, 1, 2),
    _ZyAggregationGroupState_Type()
)
zyAggregationGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationGroupState.setStatus("current")
_ZyAggregationGroupDynamicState_Type = EnabledStatus
_ZyAggregationGroupDynamicState_Object = MibTableColumn
zyAggregationGroupDynamicState = _ZyAggregationGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 3, 1, 3),
    _ZyAggregationGroupDynamicState_Type()
)
zyAggregationGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationGroupDynamicState.setStatus("current")


class _ZyAggregationGroupCriteria_Type(Integer32):
    """Custom type zyAggregationGroupCriteria based on Integer32"""
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
        *(("dstIp", 5),
          ("dstMac", 2),
          ("srcDstIp", 6),
          ("srcDstMac", 3),
          ("srcIp", 4),
          ("srcMac", 1))
    )


_ZyAggregationGroupCriteria_Type.__name__ = "Integer32"
_ZyAggregationGroupCriteria_Object = MibTableColumn
zyAggregationGroupCriteria = _ZyAggregationGroupCriteria_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 3, 1, 4),
    _ZyAggregationGroupCriteria_Type()
)
zyAggregationGroupCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationGroupCriteria.setStatus("current")
_ZyxelAggregationPortTable_Object = MibTable
zyxelAggregationPortTable = _ZyxelAggregationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelAggregationPortTable.setStatus("current")
_ZyxelAggregationPortEntry_Object = MibTableRow
zyxelAggregationPortEntry = _ZyxelAggregationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 4, 1)
)
zyxelAggregationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelAggregationPortEntry.setStatus("current")


class _ZyAggregationPortGroup_Type(Integer32):
    """Custom type zyAggregationPortGroup based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1", 1),
          ("t10", 10),
          ("t11", 11),
          ("t12", 12),
          ("t13", 13),
          ("t14", 14),
          ("t15", 15),
          ("t16", 16),
          ("t17", 17),
          ("t18", 18),
          ("t19", 19),
          ("t2", 2),
          ("t20", 20),
          ("t21", 21),
          ("t22", 22),
          ("t23", 23),
          ("t24", 24),
          ("t3", 3),
          ("t4", 4),
          ("t5", 5),
          ("t6", 6),
          ("t7", 7),
          ("t8", 8),
          ("t9", 9))
    )


_ZyAggregationPortGroup_Type.__name__ = "Integer32"
_ZyAggregationPortGroup_Object = MibTableColumn
zyAggregationPortGroup = _ZyAggregationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 4, 1, 1),
    _ZyAggregationPortGroup_Type()
)
zyAggregationPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationPortGroup.setStatus("current")
_ZyAggregationPortDynamicStateTimeout_Type = Integer32
_ZyAggregationPortDynamicStateTimeout_Object = MibTableColumn
zyAggregationPortDynamicStateTimeout = _ZyAggregationPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 4, 1, 2),
    _ZyAggregationPortDynamicStateTimeout_Type()
)
zyAggregationPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationPortDynamicStateTimeout.setStatus("current")
_ZyAggregationAutoLacpState_Type = EnabledStatus
_ZyAggregationAutoLacpState_Object = MibScalar
zyAggregationAutoLacpState = _ZyAggregationAutoLacpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 1, 5),
    _ZyAggregationAutoLacpState_Type()
)
zyAggregationAutoLacpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAggregationAutoLacpState.setStatus("current")
_ZyxelAggregationStatus_ObjectIdentity = ObjectIdentity
zyxelAggregationStatus = _ZyxelAggregationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 2)
)
_ZyAggregationAutoLacpTable_Object = MibTable
zyAggregationAutoLacpTable = _ZyAggregationAutoLacpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 2, 1)
)
if mibBuilder.loadTexts:
    zyAggregationAutoLacpTable.setStatus("current")
_ZyAggregationAutoLacpEntry_Object = MibTableRow
zyAggregationAutoLacpEntry = _ZyAggregationAutoLacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 2, 1, 1)
)
zyAggregationAutoLacpEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyAggregationAutoLacpEntry.setStatus("current")


class _ZyAggregationAutoLacpTrunkGroup_Type(Integer32):
    """Custom type zyAggregationAutoLacpTrunkGroup based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1", 1),
          ("t10", 10),
          ("t11", 11),
          ("t12", 12),
          ("t13", 13),
          ("t14", 14),
          ("t15", 15),
          ("t16", 16),
          ("t17", 17),
          ("t18", 18),
          ("t19", 19),
          ("t2", 2),
          ("t20", 20),
          ("t21", 21),
          ("t22", 22),
          ("t23", 23),
          ("t24", 24),
          ("t3", 3),
          ("t4", 4),
          ("t5", 5),
          ("t6", 6),
          ("t7", 7),
          ("t8", 8),
          ("t9", 9))
    )


_ZyAggregationAutoLacpTrunkGroup_Type.__name__ = "Integer32"
_ZyAggregationAutoLacpTrunkGroup_Object = MibTableColumn
zyAggregationAutoLacpTrunkGroup = _ZyAggregationAutoLacpTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 2, 1, 1, 1),
    _ZyAggregationAutoLacpTrunkGroup_Type()
)
zyAggregationAutoLacpTrunkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAggregationAutoLacpTrunkGroup.setStatus("current")
_ZyAggregationAutoLacpRemoteChassisId_Type = DisplayString
_ZyAggregationAutoLacpRemoteChassisId_Object = MibTableColumn
zyAggregationAutoLacpRemoteChassisId = _ZyAggregationAutoLacpRemoteChassisId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 2, 1, 1, 2),
    _ZyAggregationAutoLacpRemoteChassisId_Type()
)
zyAggregationAutoLacpRemoteChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAggregationAutoLacpRemoteChassisId.setStatus("current")
_ZyAggregationAutoLacpRemotePort_Type = Integer32
_ZyAggregationAutoLacpRemotePort_Object = MibTableColumn
zyAggregationAutoLacpRemotePort = _ZyAggregationAutoLacpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 42, 2, 1, 1, 3),
    _ZyAggregationAutoLacpRemotePort_Type()
)
zyAggregationAutoLacpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAggregationAutoLacpRemotePort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LAG-MIB",
    **{"zyxelLinkAggregation": zyxelLinkAggregation,
       "zyxelAggregationSetup": zyxelAggregationSetup,
       "zyAggregationState": zyAggregationState,
       "zyAggregationSysPriority": zyAggregationSysPriority,
       "zyxelAggregationGroupTable": zyxelAggregationGroupTable,
       "zyxelAggregationGroupEntry": zyxelAggregationGroupEntry,
       "zyAggregationGroupIndex": zyAggregationGroupIndex,
       "zyAggregationGroupState": zyAggregationGroupState,
       "zyAggregationGroupDynamicState": zyAggregationGroupDynamicState,
       "zyAggregationGroupCriteria": zyAggregationGroupCriteria,
       "zyxelAggregationPortTable": zyxelAggregationPortTable,
       "zyxelAggregationPortEntry": zyxelAggregationPortEntry,
       "zyAggregationPortGroup": zyAggregationPortGroup,
       "zyAggregationPortDynamicStateTimeout": zyAggregationPortDynamicStateTimeout,
       "zyAggregationAutoLacpState": zyAggregationAutoLacpState,
       "zyxelAggregationStatus": zyxelAggregationStatus,
       "zyAggregationAutoLacpTable": zyAggregationAutoLacpTable,
       "zyAggregationAutoLacpEntry": zyAggregationAutoLacpEntry,
       "zyAggregationAutoLacpTrunkGroup": zyAggregationAutoLacpTrunkGroup,
       "zyAggregationAutoLacpRemoteChassisId": zyAggregationAutoLacpRemoteChassisId,
       "zyAggregationAutoLacpRemotePort": zyAggregationAutoLacpRemotePort}
)
