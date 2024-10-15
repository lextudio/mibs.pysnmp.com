# SNMP MIB module (ELTEX-MES-BRIDGE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-BRIDGE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:25 2024
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

(eltMesBridgeExtMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesBridgeExtMIB")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(rldot1sMstpInstanceEntry,) = mibBuilder.importSymbols(
    "RADLAN-BRIDGEMIBOBJECTS-MIB",
    "rldot1sMstpInstanceEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltBridgeStpGroupMacAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1ad", 2),
          ("dot1d", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesBridgeExtMIBObjects_ObjectIdentity = ObjectIdentity
eltMesBridgeExtMIBObjects = _EltMesBridgeExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0)
)
_EltMesBridgeExtMacLearning_ObjectIdentity = ObjectIdentity
eltMesBridgeExtMacLearning = _EltMesBridgeExtMacLearning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 0)
)
_EltBridgeExtMacLearningVlanTable_Object = MibTable
eltBridgeExtMacLearningVlanTable = _EltBridgeExtMacLearningVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 0, 1)
)
if mibBuilder.loadTexts:
    eltBridgeExtMacLearningVlanTable.setStatus("current")
_EltBridgeExtMacLearningVlanEntry_Object = MibTableRow
eltBridgeExtMacLearningVlanEntry = _EltBridgeExtMacLearningVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 0, 1, 1)
)
eltBridgeExtMacLearningVlanEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-EXT-MIB", "eltBridgeExtMacLearningVlanIndex"),
)
if mibBuilder.loadTexts:
    eltBridgeExtMacLearningVlanEntry.setStatus("current")
_EltBridgeExtMacLearningVlanIndex_Type = VlanIndex
_EltBridgeExtMacLearningVlanIndex_Object = MibTableColumn
eltBridgeExtMacLearningVlanIndex = _EltBridgeExtMacLearningVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 0, 1, 1, 1),
    _EltBridgeExtMacLearningVlanIndex_Type()
)
eltBridgeExtMacLearningVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltBridgeExtMacLearningVlanIndex.setStatus("current")


class _EltBridgeExtMacLearningVlanEnabled_Type(TruthValue):
    """Custom type eltBridgeExtMacLearningVlanEnabled based on TruthValue"""


_EltBridgeExtMacLearningVlanEnabled_Object = MibTableColumn
eltBridgeExtMacLearningVlanEnabled = _EltBridgeExtMacLearningVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 0, 1, 1, 2),
    _EltBridgeExtMacLearningVlanEnabled_Type()
)
eltBridgeExtMacLearningVlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltBridgeExtMacLearningVlanEnabled.setStatus("current")
_EltMesBridgeMstp_ObjectIdentity = ObjectIdentity
eltMesBridgeMstp = _EltMesBridgeMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3)
)
_Eltdot1sMstpPendingGroupTable_Object = MibTable
eltdot1sMstpPendingGroupTable = _Eltdot1sMstpPendingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3)
)
if mibBuilder.loadTexts:
    eltdot1sMstpPendingGroupTable.setStatus("current")
_Eltdot1sMstpPendingGroupEntry_Object = MibTableRow
eltdot1sMstpPendingGroupEntry = _Eltdot1sMstpPendingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3, 1)
)
eltdot1sMstpPendingGroupEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-EXT-MIB", "eltdot1sMstpPendingGroup"),
)
if mibBuilder.loadTexts:
    eltdot1sMstpPendingGroupEntry.setStatus("current")
_Eltdot1sMstpPendingGroup_Type = Integer32
_Eltdot1sMstpPendingGroup_Object = MibTableColumn
eltdot1sMstpPendingGroup = _Eltdot1sMstpPendingGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3, 1, 1),
    _Eltdot1sMstpPendingGroup_Type()
)
eltdot1sMstpPendingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpPendingGroup.setStatus("current")


class _Eltdot1sMstpVlanId1To1024_Type(OctetString):
    """Custom type eltdot1sMstpVlanId1To1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1sMstpVlanId1To1024_Type.__name__ = "OctetString"
_Eltdot1sMstpVlanId1To1024_Object = MibTableColumn
eltdot1sMstpVlanId1To1024 = _Eltdot1sMstpVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3, 1, 2),
    _Eltdot1sMstpVlanId1To1024_Type()
)
eltdot1sMstpVlanId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1sMstpVlanId1To1024.setStatus("current")


class _Eltdot1sMstpVlanId1025To2048_Type(OctetString):
    """Custom type eltdot1sMstpVlanId1025To2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1sMstpVlanId1025To2048_Type.__name__ = "OctetString"
_Eltdot1sMstpVlanId1025To2048_Object = MibTableColumn
eltdot1sMstpVlanId1025To2048 = _Eltdot1sMstpVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3, 1, 3),
    _Eltdot1sMstpVlanId1025To2048_Type()
)
eltdot1sMstpVlanId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1sMstpVlanId1025To2048.setStatus("current")


class _Eltdot1sMstpVlanId2049To3072_Type(OctetString):
    """Custom type eltdot1sMstpVlanId2049To3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1sMstpVlanId2049To3072_Type.__name__ = "OctetString"
_Eltdot1sMstpVlanId2049To3072_Object = MibTableColumn
eltdot1sMstpVlanId2049To3072 = _Eltdot1sMstpVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3, 1, 4),
    _Eltdot1sMstpVlanId2049To3072_Type()
)
eltdot1sMstpVlanId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1sMstpVlanId2049To3072.setStatus("current")


class _Eltdot1sMstpVlanId3073To4094_Type(OctetString):
    """Custom type eltdot1sMstpVlanId3073To4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1sMstpVlanId3073To4094_Type.__name__ = "OctetString"
_Eltdot1sMstpVlanId3073To4094_Object = MibTableColumn
eltdot1sMstpVlanId3073To4094 = _Eltdot1sMstpVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 3, 1, 5),
    _Eltdot1sMstpVlanId3073To4094_Type()
)
eltdot1sMstpVlanId3073To4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1sMstpVlanId3073To4094.setStatus("current")
_Eltdot1sMstpInstanceTable_Object = MibTable
eltdot1sMstpInstanceTable = _Eltdot1sMstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 4)
)
if mibBuilder.loadTexts:
    eltdot1sMstpInstanceTable.setStatus("current")
_Eltdot1sMstpInstanceEntry_Object = MibTableRow
eltdot1sMstpInstanceEntry = _Eltdot1sMstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 4, 1)
)
if mibBuilder.loadTexts:
    eltdot1sMstpInstanceEntry.setStatus("current")
_Eltdot1sMstpInstanceLastTopologyChangePort_Type = Integer32
_Eltdot1sMstpInstanceLastTopologyChangePort_Object = MibTableColumn
eltdot1sMstpInstanceLastTopologyChangePort = _Eltdot1sMstpInstanceLastTopologyChangePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 3, 4, 1, 1),
    _Eltdot1sMstpInstanceLastTopologyChangePort_Type()
)
eltdot1sMstpInstanceLastTopologyChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpInstanceLastTopologyChangePort.setStatus("current")
_EltMesdot1dTp_ObjectIdentity = ObjectIdentity
eltMesdot1dTp = _EltMesdot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 4)
)
_Eltdot1dTpVlanTable_Object = MibTable
eltdot1dTpVlanTable = _Eltdot1dTpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 4, 1)
)
if mibBuilder.loadTexts:
    eltdot1dTpVlanTable.setStatus("current")
_Eltdot1dTpVlanEntry_Object = MibTableRow
eltdot1dTpVlanEntry = _Eltdot1dTpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 4, 1, 1)
)
eltdot1dTpVlanEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-EXT-MIB", "eltdot1dTpVlanIndex"),
)
if mibBuilder.loadTexts:
    eltdot1dTpVlanEntry.setStatus("current")
_Eltdot1dTpVlanIndex_Type = VlanIndex
_Eltdot1dTpVlanIndex_Object = MibTableColumn
eltdot1dTpVlanIndex = _Eltdot1dTpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 4, 1, 1, 1),
    _Eltdot1dTpVlanIndex_Type()
)
eltdot1dTpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltdot1dTpVlanIndex.setStatus("current")


class _Eltdot1dTpVlanAgingTime_Type(Integer32):
    """Custom type eltdot1dTpVlanAgingTime based on Integer32"""
    defaultValue = 300


_Eltdot1dTpVlanAgingTime_Object = MibTableColumn
eltdot1dTpVlanAgingTime = _Eltdot1dTpVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 4, 1, 1, 2),
    _Eltdot1dTpVlanAgingTime_Type()
)
eltdot1dTpVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dTpVlanAgingTime.setStatus("current")


class _Eltdot1dTpVlanAgingFromGlobal_Type(TruthValue):
    """Custom type eltdot1dTpVlanAgingFromGlobal based on TruthValue"""


_Eltdot1dTpVlanAgingFromGlobal_Object = MibTableColumn
eltdot1dTpVlanAgingFromGlobal = _Eltdot1dTpVlanAgingFromGlobal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 4, 1, 1, 3),
    _Eltdot1dTpVlanAgingFromGlobal_Type()
)
eltdot1dTpVlanAgingFromGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dTpVlanAgingFromGlobal.setStatus("current")
_EltMesBridgeStp_ObjectIdentity = ObjectIdentity
eltMesBridgeStp = _EltMesBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 5)
)
_EltBridgeStpConfigPortTable_Object = MibTable
eltBridgeStpConfigPortTable = _EltBridgeStpConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 5, 1)
)
if mibBuilder.loadTexts:
    eltBridgeStpConfigPortTable.setStatus("current")
_EltBridgeStpConfigPortEntry_Object = MibTableRow
eltBridgeStpConfigPortEntry = _EltBridgeStpConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 5, 1, 1)
)
eltBridgeStpConfigPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    eltBridgeStpConfigPortEntry.setStatus("current")


class _EltBridgeStpConfigPortGroupMacAddress_Type(EltBridgeStpGroupMacAddressType):
    """Custom type eltBridgeStpConfigPortGroupMacAddress based on EltBridgeStpGroupMacAddressType"""


_EltBridgeStpConfigPortGroupMacAddress_Object = MibTableColumn
eltBridgeStpConfigPortGroupMacAddress = _EltBridgeStpConfigPortGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 5, 1, 1, 1),
    _EltBridgeStpConfigPortGroupMacAddress_Type()
)
eltBridgeStpConfigPortGroupMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltBridgeStpConfigPortGroupMacAddress.setStatus("current")


class _EltBridgeStpConfigPortRestrictedTcn_Type(TruthValue):
    """Custom type eltBridgeStpConfigPortRestrictedTcn based on TruthValue"""


_EltBridgeStpConfigPortRestrictedTcn_Object = MibTableColumn
eltBridgeStpConfigPortRestrictedTcn = _EltBridgeStpConfigPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 5, 1, 1, 2),
    _EltBridgeStpConfigPortRestrictedTcn_Type()
)
eltBridgeStpConfigPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltBridgeStpConfigPortRestrictedTcn.setStatus("current")
_Eltdot1dStpLastTopologyChangePort_Type = Integer32
_Eltdot1dStpLastTopologyChangePort_Object = MibScalar
eltdot1dStpLastTopologyChangePort = _Eltdot1dStpLastTopologyChangePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 5, 2),
    _Eltdot1dStpLastTopologyChangePort_Type()
)
eltdot1dStpLastTopologyChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpLastTopologyChangePort.setStatus("current")
rldot1sMstpInstanceEntry.registerAugmentions(
    ("ELTEX-MES-BRIDGE-EXT-MIB",
     "eltdot1sMstpInstanceEntry")
)
eltdot1sMstpInstanceEntry.setIndexNames(*rldot1sMstpInstanceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-BRIDGE-EXT-MIB",
    **{"EltBridgeStpGroupMacAddressType": EltBridgeStpGroupMacAddressType,
       "eltMesBridgeExtMIBObjects": eltMesBridgeExtMIBObjects,
       "eltMesBridgeExtMacLearning": eltMesBridgeExtMacLearning,
       "eltBridgeExtMacLearningVlanTable": eltBridgeExtMacLearningVlanTable,
       "eltBridgeExtMacLearningVlanEntry": eltBridgeExtMacLearningVlanEntry,
       "eltBridgeExtMacLearningVlanIndex": eltBridgeExtMacLearningVlanIndex,
       "eltBridgeExtMacLearningVlanEnabled": eltBridgeExtMacLearningVlanEnabled,
       "eltMesBridgeMstp": eltMesBridgeMstp,
       "eltdot1sMstpPendingGroupTable": eltdot1sMstpPendingGroupTable,
       "eltdot1sMstpPendingGroupEntry": eltdot1sMstpPendingGroupEntry,
       "eltdot1sMstpPendingGroup": eltdot1sMstpPendingGroup,
       "eltdot1sMstpVlanId1To1024": eltdot1sMstpVlanId1To1024,
       "eltdot1sMstpVlanId1025To2048": eltdot1sMstpVlanId1025To2048,
       "eltdot1sMstpVlanId2049To3072": eltdot1sMstpVlanId2049To3072,
       "eltdot1sMstpVlanId3073To4094": eltdot1sMstpVlanId3073To4094,
       "eltdot1sMstpInstanceTable": eltdot1sMstpInstanceTable,
       "eltdot1sMstpInstanceEntry": eltdot1sMstpInstanceEntry,
       "eltdot1sMstpInstanceLastTopologyChangePort": eltdot1sMstpInstanceLastTopologyChangePort,
       "eltMesdot1dTp": eltMesdot1dTp,
       "eltdot1dTpVlanTable": eltdot1dTpVlanTable,
       "eltdot1dTpVlanEntry": eltdot1dTpVlanEntry,
       "eltdot1dTpVlanIndex": eltdot1dTpVlanIndex,
       "eltdot1dTpVlanAgingTime": eltdot1dTpVlanAgingTime,
       "eltdot1dTpVlanAgingFromGlobal": eltdot1dTpVlanAgingFromGlobal,
       "eltMesBridgeStp": eltMesBridgeStp,
       "eltBridgeStpConfigPortTable": eltBridgeStpConfigPortTable,
       "eltBridgeStpConfigPortEntry": eltBridgeStpConfigPortEntry,
       "eltBridgeStpConfigPortGroupMacAddress": eltBridgeStpConfigPortGroupMacAddress,
       "eltBridgeStpConfigPortRestrictedTcn": eltBridgeStpConfigPortRestrictedTcn,
       "eltdot1dStpLastTopologyChangePort": eltdot1dStpLastTopologyChangePort}
)
