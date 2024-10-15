# SNMP MIB module (HPN-ICF-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:54 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

hpnicfStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91)
)
hpnicfStack.setRevisions(
        ("2008-04-30 16:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfStackGlobalConfig_ObjectIdentity = ObjectIdentity
hpnicfStackGlobalConfig = _HpnicfStackGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1)
)
_HpnicfStackMaxMember_Type = Integer32
_HpnicfStackMaxMember_Object = MibScalar
hpnicfStackMaxMember = _HpnicfStackMaxMember_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 1),
    _HpnicfStackMaxMember_Type()
)
hpnicfStackMaxMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackMaxMember.setStatus("current")
_HpnicfStackMemberNum_Type = Integer32
_HpnicfStackMemberNum_Object = MibScalar
hpnicfStackMemberNum = _HpnicfStackMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 2),
    _HpnicfStackMemberNum_Type()
)
hpnicfStackMemberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackMemberNum.setStatus("current")
_HpnicfStackMaxConfigPriority_Type = Integer32
_HpnicfStackMaxConfigPriority_Object = MibScalar
hpnicfStackMaxConfigPriority = _HpnicfStackMaxConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 3),
    _HpnicfStackMaxConfigPriority_Type()
)
hpnicfStackMaxConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackMaxConfigPriority.setStatus("current")


class _HpnicfStackAutoUpdate_Type(Integer32):
    """Custom type hpnicfStackAutoUpdate based on Integer32"""
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


_HpnicfStackAutoUpdate_Type.__name__ = "Integer32"
_HpnicfStackAutoUpdate_Object = MibScalar
hpnicfStackAutoUpdate = _HpnicfStackAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 4),
    _HpnicfStackAutoUpdate_Type()
)
hpnicfStackAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStackAutoUpdate.setStatus("current")


class _HpnicfStackMacPersistence_Type(Integer32):
    """Custom type hpnicfStackMacPersistence based on Integer32"""
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


_HpnicfStackMacPersistence_Type.__name__ = "Integer32"
_HpnicfStackMacPersistence_Object = MibScalar
hpnicfStackMacPersistence = _HpnicfStackMacPersistence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 5),
    _HpnicfStackMacPersistence_Type()
)
hpnicfStackMacPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStackMacPersistence.setStatus("current")


class _HpnicfStackLinkDelayInterval_Type(Integer32):
    """Custom type hpnicfStackLinkDelayInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HpnicfStackLinkDelayInterval_Type.__name__ = "Integer32"
_HpnicfStackLinkDelayInterval_Object = MibScalar
hpnicfStackLinkDelayInterval = _HpnicfStackLinkDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 6),
    _HpnicfStackLinkDelayInterval_Type()
)
hpnicfStackLinkDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStackLinkDelayInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfStackLinkDelayInterval.setUnits("millisecond")


class _HpnicfStackTopology_Type(Integer32):
    """Custom type hpnicfStackTopology based on Integer32"""
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


_HpnicfStackTopology_Type.__name__ = "Integer32"
_HpnicfStackTopology_Object = MibScalar
hpnicfStackTopology = _HpnicfStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 7),
    _HpnicfStackTopology_Type()
)
hpnicfStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackTopology.setStatus("current")
_HpnicfStackDeviceConfigTable_Object = MibTable
hpnicfStackDeviceConfigTable = _HpnicfStackDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2)
)
if mibBuilder.loadTexts:
    hpnicfStackDeviceConfigTable.setStatus("current")
_HpnicfStackDeviceConfigEntry_Object = MibTableRow
hpnicfStackDeviceConfigEntry = _HpnicfStackDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1)
)
hpnicfStackDeviceConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfStackDeviceConfigEntry.setStatus("current")
_HpnicfStackMemberID_Type = Integer32
_HpnicfStackMemberID_Object = MibTableColumn
hpnicfStackMemberID = _HpnicfStackMemberID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 1),
    _HpnicfStackMemberID_Type()
)
hpnicfStackMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackMemberID.setStatus("current")
_HpnicfStackConfigMemberID_Type = Integer32
_HpnicfStackConfigMemberID_Object = MibTableColumn
hpnicfStackConfigMemberID = _HpnicfStackConfigMemberID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 2),
    _HpnicfStackConfigMemberID_Type()
)
hpnicfStackConfigMemberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStackConfigMemberID.setStatus("current")
_HpnicfStackPriority_Type = Integer32
_HpnicfStackPriority_Object = MibTableColumn
hpnicfStackPriority = _HpnicfStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 3),
    _HpnicfStackPriority_Type()
)
hpnicfStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStackPriority.setStatus("current")
_HpnicfStackPortNum_Type = Integer32
_HpnicfStackPortNum_Object = MibTableColumn
hpnicfStackPortNum = _HpnicfStackPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 4),
    _HpnicfStackPortNum_Type()
)
hpnicfStackPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackPortNum.setStatus("current")
_HpnicfStackPortMaxNum_Type = Integer32
_HpnicfStackPortMaxNum_Object = MibTableColumn
hpnicfStackPortMaxNum = _HpnicfStackPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 5),
    _HpnicfStackPortMaxNum_Type()
)
hpnicfStackPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackPortMaxNum.setStatus("current")
_HpnicfStackBoardConfigTable_Object = MibTable
hpnicfStackBoardConfigTable = _HpnicfStackBoardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3)
)
if mibBuilder.loadTexts:
    hpnicfStackBoardConfigTable.setStatus("current")
_HpnicfStackBoardConfigEntry_Object = MibTableRow
hpnicfStackBoardConfigEntry = _HpnicfStackBoardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3, 1)
)
hpnicfStackBoardConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfStackBoardConfigEntry.setStatus("current")


class _HpnicfStackBoardRole_Type(Integer32):
    """Custom type hpnicfStackBoardRole based on Integer32"""
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


_HpnicfStackBoardRole_Type.__name__ = "Integer32"
_HpnicfStackBoardRole_Object = MibTableColumn
hpnicfStackBoardRole = _HpnicfStackBoardRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3, 1, 1),
    _HpnicfStackBoardRole_Type()
)
hpnicfStackBoardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackBoardRole.setStatus("current")
_HpnicfStackBoardBelongtoMember_Type = Integer32
_HpnicfStackBoardBelongtoMember_Object = MibTableColumn
hpnicfStackBoardBelongtoMember = _HpnicfStackBoardBelongtoMember_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3, 1, 2),
    _HpnicfStackBoardBelongtoMember_Type()
)
hpnicfStackBoardBelongtoMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackBoardBelongtoMember.setStatus("current")
_HpnicfStackPortInfoTable_Object = MibTable
hpnicfStackPortInfoTable = _HpnicfStackPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4)
)
if mibBuilder.loadTexts:
    hpnicfStackPortInfoTable.setStatus("current")
_HpnicfStackPortInfoEntry_Object = MibTableRow
hpnicfStackPortInfoEntry = _HpnicfStackPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1)
)
hpnicfStackPortInfoEntry.setIndexNames(
    (0, "HPN-ICF-STACK-MIB", "hpnicfStackMemberID"),
    (0, "HPN-ICF-STACK-MIB", "hpnicfStackPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfStackPortInfoEntry.setStatus("current")
_HpnicfStackPortIndex_Type = Integer32
_HpnicfStackPortIndex_Object = MibTableColumn
hpnicfStackPortIndex = _HpnicfStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 1),
    _HpnicfStackPortIndex_Type()
)
hpnicfStackPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfStackPortIndex.setStatus("current")


class _HpnicfStackPortEnable_Type(Integer32):
    """Custom type hpnicfStackPortEnable based on Integer32"""
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


_HpnicfStackPortEnable_Type.__name__ = "Integer32"
_HpnicfStackPortEnable_Object = MibTableColumn
hpnicfStackPortEnable = _HpnicfStackPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 2),
    _HpnicfStackPortEnable_Type()
)
hpnicfStackPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackPortEnable.setStatus("current")


class _HpnicfStackPortStatus_Type(Integer32):
    """Custom type hpnicfStackPortStatus based on Integer32"""
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


_HpnicfStackPortStatus_Type.__name__ = "Integer32"
_HpnicfStackPortStatus_Object = MibTableColumn
hpnicfStackPortStatus = _HpnicfStackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 3),
    _HpnicfStackPortStatus_Type()
)
hpnicfStackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackPortStatus.setStatus("current")
_HpnicfStackNeighbor_Type = Integer32
_HpnicfStackNeighbor_Object = MibTableColumn
hpnicfStackNeighbor = _HpnicfStackNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 4),
    _HpnicfStackNeighbor_Type()
)
hpnicfStackNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackNeighbor.setStatus("current")


class _HpnicfStackPortForwardingPath_Type(OctetString):
    """Custom type hpnicfStackPortForwardingPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_HpnicfStackPortForwardingPath_Type.__name__ = "OctetString"
_HpnicfStackPortForwardingPath_Object = MibTableColumn
hpnicfStackPortForwardingPath = _HpnicfStackPortForwardingPath_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 5),
    _HpnicfStackPortForwardingPath_Type()
)
hpnicfStackPortForwardingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStackPortForwardingPath.setStatus("current")
_HpnicfStackPhyPortInfoTable_Object = MibTable
hpnicfStackPhyPortInfoTable = _HpnicfStackPhyPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 5)
)
if mibBuilder.loadTexts:
    hpnicfStackPhyPortInfoTable.setStatus("current")
_HpnicfStackPhyPortInfoEntry_Object = MibTableRow
hpnicfStackPhyPortInfoEntry = _HpnicfStackPhyPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 5, 1)
)
hpnicfStackPhyPortInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfStackPhyPortInfoEntry.setStatus("current")
_HpnicfStackBelongtoPort_Type = Integer32
_HpnicfStackBelongtoPort_Object = MibTableColumn
hpnicfStackBelongtoPort = _HpnicfStackBelongtoPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 5, 1, 1),
    _HpnicfStackBelongtoPort_Type()
)
hpnicfStackBelongtoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStackBelongtoPort.setStatus("current")
_HpnicfStackTrap_ObjectIdentity = ObjectIdentity
hpnicfStackTrap = _HpnicfStackTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6)
)
_HpnicfStackTrapOjbects_ObjectIdentity = ObjectIdentity
hpnicfStackTrapOjbects = _HpnicfStackTrapOjbects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0)
)

# Managed Objects groups


# Notification objects

hpnicfStackPortLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 1)
)
hpnicfStackPortLinkStatusChange.setObjects(
      *(("HPN-ICF-STACK-MIB", "hpnicfStackMemberID"),
        ("HPN-ICF-STACK-MIB", "hpnicfStackPortIndex"),
        ("HPN-ICF-STACK-MIB", "hpnicfStackPortStatus"))
)
if mibBuilder.loadTexts:
    hpnicfStackPortLinkStatusChange.setStatus(
        "current"
    )

hpnicfStackTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 2)
)
hpnicfStackTopologyChange.setObjects(
    ("HPN-ICF-STACK-MIB", "hpnicfStackTopology")
)
if mibBuilder.loadTexts:
    hpnicfStackTopologyChange.setStatus(
        "current"
    )

hpnicfStackMadBfdChangeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 3)
)
hpnicfStackMadBfdChangeNormal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfStackMadBfdChangeNormal.setStatus(
        "current"
    )

hpnicfStackMadBfdChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 4)
)
hpnicfStackMadBfdChangeFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfStackMadBfdChangeFailure.setStatus(
        "current"
    )

hpnicfStackMadLacpChangeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 5)
)
hpnicfStackMadLacpChangeNormal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfStackMadLacpChangeNormal.setStatus(
        "current"
    )

hpnicfStackMadLacpChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 6)
)
hpnicfStackMadLacpChangeFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfStackMadLacpChangeFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-STACK-MIB",
    **{"hpnicfStack": hpnicfStack,
       "hpnicfStackGlobalConfig": hpnicfStackGlobalConfig,
       "hpnicfStackMaxMember": hpnicfStackMaxMember,
       "hpnicfStackMemberNum": hpnicfStackMemberNum,
       "hpnicfStackMaxConfigPriority": hpnicfStackMaxConfigPriority,
       "hpnicfStackAutoUpdate": hpnicfStackAutoUpdate,
       "hpnicfStackMacPersistence": hpnicfStackMacPersistence,
       "hpnicfStackLinkDelayInterval": hpnicfStackLinkDelayInterval,
       "hpnicfStackTopology": hpnicfStackTopology,
       "hpnicfStackDeviceConfigTable": hpnicfStackDeviceConfigTable,
       "hpnicfStackDeviceConfigEntry": hpnicfStackDeviceConfigEntry,
       "hpnicfStackMemberID": hpnicfStackMemberID,
       "hpnicfStackConfigMemberID": hpnicfStackConfigMemberID,
       "hpnicfStackPriority": hpnicfStackPriority,
       "hpnicfStackPortNum": hpnicfStackPortNum,
       "hpnicfStackPortMaxNum": hpnicfStackPortMaxNum,
       "hpnicfStackBoardConfigTable": hpnicfStackBoardConfigTable,
       "hpnicfStackBoardConfigEntry": hpnicfStackBoardConfigEntry,
       "hpnicfStackBoardRole": hpnicfStackBoardRole,
       "hpnicfStackBoardBelongtoMember": hpnicfStackBoardBelongtoMember,
       "hpnicfStackPortInfoTable": hpnicfStackPortInfoTable,
       "hpnicfStackPortInfoEntry": hpnicfStackPortInfoEntry,
       "hpnicfStackPortIndex": hpnicfStackPortIndex,
       "hpnicfStackPortEnable": hpnicfStackPortEnable,
       "hpnicfStackPortStatus": hpnicfStackPortStatus,
       "hpnicfStackNeighbor": hpnicfStackNeighbor,
       "hpnicfStackPortForwardingPath": hpnicfStackPortForwardingPath,
       "hpnicfStackPhyPortInfoTable": hpnicfStackPhyPortInfoTable,
       "hpnicfStackPhyPortInfoEntry": hpnicfStackPhyPortInfoEntry,
       "hpnicfStackBelongtoPort": hpnicfStackBelongtoPort,
       "hpnicfStackTrap": hpnicfStackTrap,
       "hpnicfStackTrapOjbects": hpnicfStackTrapOjbects,
       "hpnicfStackPortLinkStatusChange": hpnicfStackPortLinkStatusChange,
       "hpnicfStackTopologyChange": hpnicfStackTopologyChange,
       "hpnicfStackMadBfdChangeNormal": hpnicfStackMadBfdChangeNormal,
       "hpnicfStackMadBfdChangeFailure": hpnicfStackMadBfdChangeFailure,
       "hpnicfStackMadLacpChangeNormal": hpnicfStackMadLacpChangeNormal,
       "hpnicfStackMadLacpChangeFailure": hpnicfStackMadLacpChangeFailure}
)
