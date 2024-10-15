# SNMP MIB module (H3C-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:25 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91)
)
h3cStack.setRevisions(
        ("2008-04-30 16:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cStackGlobalConfig_ObjectIdentity = ObjectIdentity
h3cStackGlobalConfig = _H3cStackGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1)
)
_H3cStackMaxMember_Type = Integer32
_H3cStackMaxMember_Object = MibScalar
h3cStackMaxMember = _H3cStackMaxMember_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 1),
    _H3cStackMaxMember_Type()
)
h3cStackMaxMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackMaxMember.setStatus("current")
_H3cStackMemberNum_Type = Integer32
_H3cStackMemberNum_Object = MibScalar
h3cStackMemberNum = _H3cStackMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 2),
    _H3cStackMemberNum_Type()
)
h3cStackMemberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackMemberNum.setStatus("current")
_H3cStackMaxConfigPriority_Type = Integer32
_H3cStackMaxConfigPriority_Object = MibScalar
h3cStackMaxConfigPriority = _H3cStackMaxConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 3),
    _H3cStackMaxConfigPriority_Type()
)
h3cStackMaxConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackMaxConfigPriority.setStatus("current")


class _H3cStackAutoUpdate_Type(Integer32):
    """Custom type h3cStackAutoUpdate based on Integer32"""
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


_H3cStackAutoUpdate_Type.__name__ = "Integer32"
_H3cStackAutoUpdate_Object = MibScalar
h3cStackAutoUpdate = _H3cStackAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 4),
    _H3cStackAutoUpdate_Type()
)
h3cStackAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStackAutoUpdate.setStatus("current")


class _H3cStackMacPersistence_Type(Integer32):
    """Custom type h3cStackMacPersistence based on Integer32"""
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


_H3cStackMacPersistence_Type.__name__ = "Integer32"
_H3cStackMacPersistence_Object = MibScalar
h3cStackMacPersistence = _H3cStackMacPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 5),
    _H3cStackMacPersistence_Type()
)
h3cStackMacPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStackMacPersistence.setStatus("current")


class _H3cStackLinkDelayInterval_Type(Integer32):
    """Custom type h3cStackLinkDelayInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(200, 2000),
    )


_H3cStackLinkDelayInterval_Type.__name__ = "Integer32"
_H3cStackLinkDelayInterval_Object = MibScalar
h3cStackLinkDelayInterval = _H3cStackLinkDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 6),
    _H3cStackLinkDelayInterval_Type()
)
h3cStackLinkDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStackLinkDelayInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cStackLinkDelayInterval.setUnits("millisecond")


class _H3cStackTopology_Type(Integer32):
    """Custom type h3cStackTopology based on Integer32"""
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


_H3cStackTopology_Type.__name__ = "Integer32"
_H3cStackTopology_Object = MibScalar
h3cStackTopology = _H3cStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 1, 7),
    _H3cStackTopology_Type()
)
h3cStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackTopology.setStatus("current")
_H3cStackDeviceConfigTable_Object = MibTable
h3cStackDeviceConfigTable = _H3cStackDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2)
)
if mibBuilder.loadTexts:
    h3cStackDeviceConfigTable.setStatus("current")
_H3cStackDeviceConfigEntry_Object = MibTableRow
h3cStackDeviceConfigEntry = _H3cStackDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2, 1)
)
h3cStackDeviceConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cStackDeviceConfigEntry.setStatus("current")
_H3cStackMemberID_Type = Integer32
_H3cStackMemberID_Object = MibTableColumn
h3cStackMemberID = _H3cStackMemberID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2, 1, 1),
    _H3cStackMemberID_Type()
)
h3cStackMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackMemberID.setStatus("current")
_H3cStackConfigMemberID_Type = Integer32
_H3cStackConfigMemberID_Object = MibTableColumn
h3cStackConfigMemberID = _H3cStackConfigMemberID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2, 1, 2),
    _H3cStackConfigMemberID_Type()
)
h3cStackConfigMemberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStackConfigMemberID.setStatus("current")
_H3cStackPriority_Type = Integer32
_H3cStackPriority_Object = MibTableColumn
h3cStackPriority = _H3cStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2, 1, 3),
    _H3cStackPriority_Type()
)
h3cStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStackPriority.setStatus("current")
_H3cStackPortNum_Type = Integer32
_H3cStackPortNum_Object = MibTableColumn
h3cStackPortNum = _H3cStackPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2, 1, 4),
    _H3cStackPortNum_Type()
)
h3cStackPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackPortNum.setStatus("current")
_H3cStackPortMaxNum_Type = Integer32
_H3cStackPortMaxNum_Object = MibTableColumn
h3cStackPortMaxNum = _H3cStackPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 2, 1, 5),
    _H3cStackPortMaxNum_Type()
)
h3cStackPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackPortMaxNum.setStatus("current")
_H3cStackBoardConfigTable_Object = MibTable
h3cStackBoardConfigTable = _H3cStackBoardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 3)
)
if mibBuilder.loadTexts:
    h3cStackBoardConfigTable.setStatus("current")
_H3cStackBoardConfigEntry_Object = MibTableRow
h3cStackBoardConfigEntry = _H3cStackBoardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 3, 1)
)
h3cStackBoardConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cStackBoardConfigEntry.setStatus("current")


class _H3cStackBoardRole_Type(Integer32):
    """Custom type h3cStackBoardRole based on Integer32"""
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


_H3cStackBoardRole_Type.__name__ = "Integer32"
_H3cStackBoardRole_Object = MibTableColumn
h3cStackBoardRole = _H3cStackBoardRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 3, 1, 1),
    _H3cStackBoardRole_Type()
)
h3cStackBoardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackBoardRole.setStatus("current")
_H3cStackBoardBelongtoMember_Type = Integer32
_H3cStackBoardBelongtoMember_Object = MibTableColumn
h3cStackBoardBelongtoMember = _H3cStackBoardBelongtoMember_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 3, 1, 2),
    _H3cStackBoardBelongtoMember_Type()
)
h3cStackBoardBelongtoMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackBoardBelongtoMember.setStatus("current")
_H3cStackPortInfoTable_Object = MibTable
h3cStackPortInfoTable = _H3cStackPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 4)
)
if mibBuilder.loadTexts:
    h3cStackPortInfoTable.setStatus("current")
_H3cStackPortInfoEntry_Object = MibTableRow
h3cStackPortInfoEntry = _H3cStackPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 4, 1)
)
h3cStackPortInfoEntry.setIndexNames(
    (0, "H3C-STACK-MIB", "h3cStackMemberID"),
    (0, "H3C-STACK-MIB", "h3cStackPortIndex"),
)
if mibBuilder.loadTexts:
    h3cStackPortInfoEntry.setStatus("current")
_H3cStackPortIndex_Type = Integer32
_H3cStackPortIndex_Object = MibTableColumn
h3cStackPortIndex = _H3cStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 4, 1, 1),
    _H3cStackPortIndex_Type()
)
h3cStackPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cStackPortIndex.setStatus("current")


class _H3cStackPortEnable_Type(Integer32):
    """Custom type h3cStackPortEnable based on Integer32"""
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


_H3cStackPortEnable_Type.__name__ = "Integer32"
_H3cStackPortEnable_Object = MibTableColumn
h3cStackPortEnable = _H3cStackPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 4, 1, 2),
    _H3cStackPortEnable_Type()
)
h3cStackPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackPortEnable.setStatus("current")


class _H3cStackPortStatus_Type(Integer32):
    """Custom type h3cStackPortStatus based on Integer32"""
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


_H3cStackPortStatus_Type.__name__ = "Integer32"
_H3cStackPortStatus_Object = MibTableColumn
h3cStackPortStatus = _H3cStackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 4, 1, 3),
    _H3cStackPortStatus_Type()
)
h3cStackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackPortStatus.setStatus("current")
_H3cStackNeighbor_Type = Integer32
_H3cStackNeighbor_Object = MibTableColumn
h3cStackNeighbor = _H3cStackNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 4, 1, 4),
    _H3cStackNeighbor_Type()
)
h3cStackNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStackNeighbor.setStatus("current")
_H3cStackPhyPortInfoTable_Object = MibTable
h3cStackPhyPortInfoTable = _H3cStackPhyPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 5)
)
if mibBuilder.loadTexts:
    h3cStackPhyPortInfoTable.setStatus("current")
_H3cStackPhyPortInfoEntry_Object = MibTableRow
h3cStackPhyPortInfoEntry = _H3cStackPhyPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 5, 1)
)
h3cStackPhyPortInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cStackPhyPortInfoEntry.setStatus("current")
_H3cStackBelongtoPort_Type = Integer32
_H3cStackBelongtoPort_Object = MibTableColumn
h3cStackBelongtoPort = _H3cStackBelongtoPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 5, 1, 1),
    _H3cStackBelongtoPort_Type()
)
h3cStackBelongtoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStackBelongtoPort.setStatus("current")
_H3cStackTrap_ObjectIdentity = ObjectIdentity
h3cStackTrap = _H3cStackTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 6)
)
_H3cStackTrapOjbects_ObjectIdentity = ObjectIdentity
h3cStackTrapOjbects = _H3cStackTrapOjbects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 6, 0)
)

# Managed Objects groups


# Notification objects

h3cStackPortLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 6, 0, 1)
)
h3cStackPortLinkStatusChange.setObjects(
      *(("H3C-STACK-MIB", "h3cStackMemberID"),
        ("H3C-STACK-MIB", "h3cStackPortIndex"),
        ("H3C-STACK-MIB", "h3cStackPortStatus"))
)
if mibBuilder.loadTexts:
    h3cStackPortLinkStatusChange.setStatus(
        "current"
    )

h3cStackTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91, 6, 0, 2)
)
h3cStackTopologyChange.setObjects(
    ("H3C-STACK-MIB", "h3cStackTopology")
)
if mibBuilder.loadTexts:
    h3cStackTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-STACK-MIB",
    **{"h3cStack": h3cStack,
       "h3cStackGlobalConfig": h3cStackGlobalConfig,
       "h3cStackMaxMember": h3cStackMaxMember,
       "h3cStackMemberNum": h3cStackMemberNum,
       "h3cStackMaxConfigPriority": h3cStackMaxConfigPriority,
       "h3cStackAutoUpdate": h3cStackAutoUpdate,
       "h3cStackMacPersistence": h3cStackMacPersistence,
       "h3cStackLinkDelayInterval": h3cStackLinkDelayInterval,
       "h3cStackTopology": h3cStackTopology,
       "h3cStackDeviceConfigTable": h3cStackDeviceConfigTable,
       "h3cStackDeviceConfigEntry": h3cStackDeviceConfigEntry,
       "h3cStackMemberID": h3cStackMemberID,
       "h3cStackConfigMemberID": h3cStackConfigMemberID,
       "h3cStackPriority": h3cStackPriority,
       "h3cStackPortNum": h3cStackPortNum,
       "h3cStackPortMaxNum": h3cStackPortMaxNum,
       "h3cStackBoardConfigTable": h3cStackBoardConfigTable,
       "h3cStackBoardConfigEntry": h3cStackBoardConfigEntry,
       "h3cStackBoardRole": h3cStackBoardRole,
       "h3cStackBoardBelongtoMember": h3cStackBoardBelongtoMember,
       "h3cStackPortInfoTable": h3cStackPortInfoTable,
       "h3cStackPortInfoEntry": h3cStackPortInfoEntry,
       "h3cStackPortIndex": h3cStackPortIndex,
       "h3cStackPortEnable": h3cStackPortEnable,
       "h3cStackPortStatus": h3cStackPortStatus,
       "h3cStackNeighbor": h3cStackNeighbor,
       "h3cStackPhyPortInfoTable": h3cStackPhyPortInfoTable,
       "h3cStackPhyPortInfoEntry": h3cStackPhyPortInfoEntry,
       "h3cStackBelongtoPort": h3cStackBelongtoPort,
       "h3cStackTrap": h3cStackTrap,
       "h3cStackTrapOjbects": h3cStackTrapOjbects,
       "h3cStackPortLinkStatusChange": h3cStackPortLinkStatusChange,
       "h3cStackTopologyChange": h3cStackTopologyChange}
)
