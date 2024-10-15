# SNMP MIB module (HH3C-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:58 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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


# MODULE-IDENTITY

hh3cStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91)
)
hh3cStack.setRevisions(
        ("2008-04-30 16:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cStackGlobalConfig_ObjectIdentity = ObjectIdentity
hh3cStackGlobalConfig = _Hh3cStackGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1)
)
_Hh3cStackMaxMember_Type = Integer32
_Hh3cStackMaxMember_Object = MibScalar
hh3cStackMaxMember = _Hh3cStackMaxMember_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 1),
    _Hh3cStackMaxMember_Type()
)
hh3cStackMaxMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMaxMember.setStatus("current")
_Hh3cStackMemberNum_Type = Integer32
_Hh3cStackMemberNum_Object = MibScalar
hh3cStackMemberNum = _Hh3cStackMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 2),
    _Hh3cStackMemberNum_Type()
)
hh3cStackMemberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMemberNum.setStatus("current")
_Hh3cStackMaxConfigPriority_Type = Integer32
_Hh3cStackMaxConfigPriority_Object = MibScalar
hh3cStackMaxConfigPriority = _Hh3cStackMaxConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 3),
    _Hh3cStackMaxConfigPriority_Type()
)
hh3cStackMaxConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMaxConfigPriority.setStatus("current")


class _Hh3cStackAutoUpdate_Type(Integer32):
    """Custom type hh3cStackAutoUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Hh3cStackAutoUpdate_Type.__name__ = "Integer32"
_Hh3cStackAutoUpdate_Object = MibScalar
hh3cStackAutoUpdate = _Hh3cStackAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 4),
    _Hh3cStackAutoUpdate_Type()
)
hh3cStackAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackAutoUpdate.setStatus("current")


class _Hh3cStackMacPersistence_Type(Integer32):
    """Custom type hh3cStackMacPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPersist", 1),
          ("persistForSixMin", 2),
          ("persistForever", 3))
    )


_Hh3cStackMacPersistence_Type.__name__ = "Integer32"
_Hh3cStackMacPersistence_Object = MibScalar
hh3cStackMacPersistence = _Hh3cStackMacPersistence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 5),
    _Hh3cStackMacPersistence_Type()
)
hh3cStackMacPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackMacPersistence.setStatus("current")


class _Hh3cStackLinkDelayInterval_Type(Integer32):
    """Custom type hh3cStackLinkDelayInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(200, 2000),
    )


_Hh3cStackLinkDelayInterval_Type.__name__ = "Integer32"
_Hh3cStackLinkDelayInterval_Object = MibScalar
hh3cStackLinkDelayInterval = _Hh3cStackLinkDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 6),
    _Hh3cStackLinkDelayInterval_Type()
)
hh3cStackLinkDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackLinkDelayInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cStackLinkDelayInterval.setUnits("millisecond")


class _Hh3cStackTopology_Type(Integer32):
    """Custom type hh3cStackTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chainConn", 1),
          ("ringConn", 2))
    )


_Hh3cStackTopology_Type.__name__ = "Integer32"
_Hh3cStackTopology_Object = MibScalar
hh3cStackTopology = _Hh3cStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 7),
    _Hh3cStackTopology_Type()
)
hh3cStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackTopology.setStatus("current")
_Hh3cStackDeviceConfigTable_Object = MibTable
hh3cStackDeviceConfigTable = _Hh3cStackDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2)
)
if mibBuilder.loadTexts:
    hh3cStackDeviceConfigTable.setStatus("current")
_Hh3cStackDeviceConfigEntry_Object = MibTableRow
hh3cStackDeviceConfigEntry = _Hh3cStackDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1)
)
hh3cStackDeviceConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackDeviceConfigEntry.setStatus("current")
_Hh3cStackMemberID_Type = Integer32
_Hh3cStackMemberID_Object = MibTableColumn
hh3cStackMemberID = _Hh3cStackMemberID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 1),
    _Hh3cStackMemberID_Type()
)
hh3cStackMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMemberID.setStatus("current")
_Hh3cStackConfigMemberID_Type = Integer32
_Hh3cStackConfigMemberID_Object = MibTableColumn
hh3cStackConfigMemberID = _Hh3cStackConfigMemberID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 2),
    _Hh3cStackConfigMemberID_Type()
)
hh3cStackConfigMemberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackConfigMemberID.setStatus("current")
_Hh3cStackPriority_Type = Integer32
_Hh3cStackPriority_Object = MibTableColumn
hh3cStackPriority = _Hh3cStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 3),
    _Hh3cStackPriority_Type()
)
hh3cStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackPriority.setStatus("current")
_Hh3cStackPortNum_Type = Integer32
_Hh3cStackPortNum_Object = MibTableColumn
hh3cStackPortNum = _Hh3cStackPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 4),
    _Hh3cStackPortNum_Type()
)
hh3cStackPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortNum.setStatus("current")
_Hh3cStackPortMaxNum_Type = Integer32
_Hh3cStackPortMaxNum_Object = MibTableColumn
hh3cStackPortMaxNum = _Hh3cStackPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 5),
    _Hh3cStackPortMaxNum_Type()
)
hh3cStackPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortMaxNum.setStatus("current")
_Hh3cStackBoardConfigTable_Object = MibTable
hh3cStackBoardConfigTable = _Hh3cStackBoardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3)
)
if mibBuilder.loadTexts:
    hh3cStackBoardConfigTable.setStatus("current")
_Hh3cStackBoardConfigEntry_Object = MibTableRow
hh3cStackBoardConfigEntry = _Hh3cStackBoardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3, 1)
)
hh3cStackBoardConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackBoardConfigEntry.setStatus("current")


class _Hh3cStackBoardRole_Type(Integer32):
    """Custom type hh3cStackBoardRole based on Integer32"""
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
        *(("loading", 3),
          ("master", 2),
          ("other", 4),
          ("slave", 1))
    )


_Hh3cStackBoardRole_Type.__name__ = "Integer32"
_Hh3cStackBoardRole_Object = MibTableColumn
hh3cStackBoardRole = _Hh3cStackBoardRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3, 1, 1),
    _Hh3cStackBoardRole_Type()
)
hh3cStackBoardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackBoardRole.setStatus("current")
_Hh3cStackBoardBelongtoMember_Type = Integer32
_Hh3cStackBoardBelongtoMember_Object = MibTableColumn
hh3cStackBoardBelongtoMember = _Hh3cStackBoardBelongtoMember_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3, 1, 2),
    _Hh3cStackBoardBelongtoMember_Type()
)
hh3cStackBoardBelongtoMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackBoardBelongtoMember.setStatus("current")
_Hh3cStackPortInfoTable_Object = MibTable
hh3cStackPortInfoTable = _Hh3cStackPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4)
)
if mibBuilder.loadTexts:
    hh3cStackPortInfoTable.setStatus("current")
_Hh3cStackPortInfoEntry_Object = MibTableRow
hh3cStackPortInfoEntry = _Hh3cStackPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1)
)
hh3cStackPortInfoEntry.setIndexNames(
    (0, "HH3C-STACK-MIB", "hh3cStackMemberID"),
    (0, "HH3C-STACK-MIB", "hh3cStackPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackPortInfoEntry.setStatus("current")
_Hh3cStackPortIndex_Type = Integer32
_Hh3cStackPortIndex_Object = MibTableColumn
hh3cStackPortIndex = _Hh3cStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 1),
    _Hh3cStackPortIndex_Type()
)
hh3cStackPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cStackPortIndex.setStatus("current")


class _Hh3cStackPortEnable_Type(Integer32):
    """Custom type hh3cStackPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Hh3cStackPortEnable_Type.__name__ = "Integer32"
_Hh3cStackPortEnable_Object = MibTableColumn
hh3cStackPortEnable = _Hh3cStackPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 2),
    _Hh3cStackPortEnable_Type()
)
hh3cStackPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortEnable.setStatus("current")


class _Hh3cStackPortStatus_Type(Integer32):
    """Custom type hh3cStackPortStatus based on Integer32"""
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
        *(("disabled", 4),
          ("down", 2),
          ("silent", 3),
          ("up", 1))
    )


_Hh3cStackPortStatus_Type.__name__ = "Integer32"
_Hh3cStackPortStatus_Object = MibTableColumn
hh3cStackPortStatus = _Hh3cStackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 3),
    _Hh3cStackPortStatus_Type()
)
hh3cStackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortStatus.setStatus("current")
_Hh3cStackNeighbor_Type = Integer32
_Hh3cStackNeighbor_Object = MibTableColumn
hh3cStackNeighbor = _Hh3cStackNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 4),
    _Hh3cStackNeighbor_Type()
)
hh3cStackNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackNeighbor.setStatus("current")
_Hh3cStackPhyPortInfoTable_Object = MibTable
hh3cStackPhyPortInfoTable = _Hh3cStackPhyPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 5)
)
if mibBuilder.loadTexts:
    hh3cStackPhyPortInfoTable.setStatus("current")
_Hh3cStackPhyPortInfoEntry_Object = MibTableRow
hh3cStackPhyPortInfoEntry = _Hh3cStackPhyPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 5, 1)
)
hh3cStackPhyPortInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackPhyPortInfoEntry.setStatus("current")
_Hh3cStackBelongtoPort_Type = Integer32
_Hh3cStackBelongtoPort_Object = MibTableColumn
hh3cStackBelongtoPort = _Hh3cStackBelongtoPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 5, 1, 1),
    _Hh3cStackBelongtoPort_Type()
)
hh3cStackBelongtoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackBelongtoPort.setStatus("current")
_Hh3cStackTrap_ObjectIdentity = ObjectIdentity
hh3cStackTrap = _Hh3cStackTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6)
)
_Hh3cStackTrapOjbects_ObjectIdentity = ObjectIdentity
hh3cStackTrapOjbects = _Hh3cStackTrapOjbects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0)
)

# Managed Objects groups


# Notification objects

hh3cStackPortLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 1)
)
hh3cStackPortLinkStatusChange.setObjects(
      *(("HH3C-STACK-MIB", "hh3cStackMemberID"),
        ("HH3C-STACK-MIB", "hh3cStackPortIndex"),
        ("HH3C-STACK-MIB", "hh3cStackPortStatus"))
)
if mibBuilder.loadTexts:
    hh3cStackPortLinkStatusChange.setStatus(
        "current"
    )

hh3cStackTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 2)
)
hh3cStackTopologyChange.setObjects(
    ("HH3C-STACK-MIB", "hh3cStackTopology")
)
if mibBuilder.loadTexts:
    hh3cStackTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-STACK-MIB",
    **{"hh3cStack": hh3cStack,
       "hh3cStackGlobalConfig": hh3cStackGlobalConfig,
       "hh3cStackMaxMember": hh3cStackMaxMember,
       "hh3cStackMemberNum": hh3cStackMemberNum,
       "hh3cStackMaxConfigPriority": hh3cStackMaxConfigPriority,
       "hh3cStackAutoUpdate": hh3cStackAutoUpdate,
       "hh3cStackMacPersistence": hh3cStackMacPersistence,
       "hh3cStackLinkDelayInterval": hh3cStackLinkDelayInterval,
       "hh3cStackTopology": hh3cStackTopology,
       "hh3cStackDeviceConfigTable": hh3cStackDeviceConfigTable,
       "hh3cStackDeviceConfigEntry": hh3cStackDeviceConfigEntry,
       "hh3cStackMemberID": hh3cStackMemberID,
       "hh3cStackConfigMemberID": hh3cStackConfigMemberID,
       "hh3cStackPriority": hh3cStackPriority,
       "hh3cStackPortNum": hh3cStackPortNum,
       "hh3cStackPortMaxNum": hh3cStackPortMaxNum,
       "hh3cStackBoardConfigTable": hh3cStackBoardConfigTable,
       "hh3cStackBoardConfigEntry": hh3cStackBoardConfigEntry,
       "hh3cStackBoardRole": hh3cStackBoardRole,
       "hh3cStackBoardBelongtoMember": hh3cStackBoardBelongtoMember,
       "hh3cStackPortInfoTable": hh3cStackPortInfoTable,
       "hh3cStackPortInfoEntry": hh3cStackPortInfoEntry,
       "hh3cStackPortIndex": hh3cStackPortIndex,
       "hh3cStackPortEnable": hh3cStackPortEnable,
       "hh3cStackPortStatus": hh3cStackPortStatus,
       "hh3cStackNeighbor": hh3cStackNeighbor,
       "hh3cStackPhyPortInfoTable": hh3cStackPhyPortInfoTable,
       "hh3cStackPhyPortInfoEntry": hh3cStackPhyPortInfoEntry,
       "hh3cStackBelongtoPort": hh3cStackBelongtoPort,
       "hh3cStackTrap": hh3cStackTrap,
       "hh3cStackTrapOjbects": hh3cStackTrapOjbects,
       "hh3cStackPortLinkStatusChange": hh3cStackPortLinkStatusChange,
       "hh3cStackTopologyChange": hh3cStackTopologyChange}
)
