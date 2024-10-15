# SNMP MIB module (CENTILLION-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:10 2024
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

(Boolean,
 CardId,
 EnableIndicator,
 PortId,
 StatusIndicator,
 sysConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "Boolean",
    "CardId",
    "EnableIndicator",
    "PortId",
    "StatusIndicator",
    "sysConfig")

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


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31)
)
_VlanMcastProtocolGroup_ObjectIdentity = ObjectIdentity
vlanMcastProtocolGroup = _VlanMcastProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1)
)
_VlanIGMPProtocolGroup_ObjectIdentity = ObjectIdentity
vlanIGMPProtocolGroup = _VlanIGMPProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1)
)
_VlanIGMPConfig_ObjectIdentity = ObjectIdentity
vlanIGMPConfig = _VlanIGMPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1)
)
_IgmpGeneralConfigTable_Object = MibTable
igmpGeneralConfigTable = _IgmpGeneralConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    igmpGeneralConfigTable.setStatus("mandatory")
_IgmpGeneralConfigEntry_Object = MibTableRow
igmpGeneralConfigEntry = _IgmpGeneralConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1)
)
igmpGeneralConfigEntry.setIndexNames(
    (0, "CENTILLION-MCAST-MIB", "igmpGeneralConfigVlanId"),
)
if mibBuilder.loadTexts:
    igmpGeneralConfigEntry.setStatus("mandatory")
_IgmpGeneralConfigVlanId_Type = VlanId
_IgmpGeneralConfigVlanId_Object = MibTableColumn
igmpGeneralConfigVlanId = _IgmpGeneralConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 1),
    _IgmpGeneralConfigVlanId_Type()
)
igmpGeneralConfigVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGeneralConfigVlanId.setStatus("mandatory")
_IgmpGeneralConfigPseudoQuery_Type = EnableIndicator
_IgmpGeneralConfigPseudoQuery_Object = MibTableColumn
igmpGeneralConfigPseudoQuery = _IgmpGeneralConfigPseudoQuery_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 2),
    _IgmpGeneralConfigPseudoQuery_Type()
)
igmpGeneralConfigPseudoQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGeneralConfigPseudoQuery.setStatus("mandatory")
_IgmpGeneralConfigIrapQuery_Type = EnableIndicator
_IgmpGeneralConfigIrapQuery_Object = MibTableColumn
igmpGeneralConfigIrapQuery = _IgmpGeneralConfigIrapQuery_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 3),
    _IgmpGeneralConfigIrapQuery_Type()
)
igmpGeneralConfigIrapQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGeneralConfigIrapQuery.setStatus("mandatory")
_IgmpGeneralConfigIgmpSupport_Type = EnableIndicator
_IgmpGeneralConfigIgmpSupport_Object = MibTableColumn
igmpGeneralConfigIgmpSupport = _IgmpGeneralConfigIgmpSupport_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 4),
    _IgmpGeneralConfigIgmpSupport_Type()
)
igmpGeneralConfigIgmpSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGeneralConfigIgmpSupport.setStatus("mandatory")
_IgmpGeneralConfigMaxGroup_Type = Integer32
_IgmpGeneralConfigMaxGroup_Object = MibTableColumn
igmpGeneralConfigMaxGroup = _IgmpGeneralConfigMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 5),
    _IgmpGeneralConfigMaxGroup_Type()
)
igmpGeneralConfigMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGeneralConfigMaxGroup.setStatus("mandatory")
_IgmpTimerConfigTable_Object = MibTable
igmpTimerConfigTable = _IgmpTimerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    igmpTimerConfigTable.setStatus("mandatory")
_IgmpTimerConfigEntry_Object = MibTableRow
igmpTimerConfigEntry = _IgmpTimerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1)
)
igmpTimerConfigEntry.setIndexNames(
    (0, "CENTILLION-MCAST-MIB", "igmpTimerConfigVlanId"),
)
if mibBuilder.loadTexts:
    igmpTimerConfigEntry.setStatus("mandatory")
_IgmpTimerConfigVlanId_Type = VlanId
_IgmpTimerConfigVlanId_Object = MibTableColumn
igmpTimerConfigVlanId = _IgmpTimerConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 1),
    _IgmpTimerConfigVlanId_Type()
)
igmpTimerConfigVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpTimerConfigVlanId.setStatus("mandatory")


class _IgmpTimerConfigTimerRobustness_Type(Integer32):
    """Custom type igmpTimerConfigTimerRobustness based on Integer32"""
    defaultValue = 2


_IgmpTimerConfigTimerRobustness_Object = MibTableColumn
igmpTimerConfigTimerRobustness = _IgmpTimerConfigTimerRobustness_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 2),
    _IgmpTimerConfigTimerRobustness_Type()
)
igmpTimerConfigTimerRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpTimerConfigTimerRobustness.setStatus("mandatory")


class _IgmpTimerConfigQueryInterval_Type(Integer32):
    """Custom type igmpTimerConfigQueryInterval based on Integer32"""
    defaultValue = 125


_IgmpTimerConfigQueryInterval_Object = MibTableColumn
igmpTimerConfigQueryInterval = _IgmpTimerConfigQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 3),
    _IgmpTimerConfigQueryInterval_Type()
)
igmpTimerConfigQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpTimerConfigQueryInterval.setStatus("mandatory")


class _IgmpTimerConfigQueryResponse_Type(Integer32):
    """Custom type igmpTimerConfigQueryResponse based on Integer32"""
    defaultValue = 100


_IgmpTimerConfigQueryResponse_Object = MibTableColumn
igmpTimerConfigQueryResponse = _IgmpTimerConfigQueryResponse_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 4),
    _IgmpTimerConfigQueryResponse_Type()
)
igmpTimerConfigQueryResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpTimerConfigQueryResponse.setStatus("mandatory")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("mandatory")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "CENTILLION-MCAST-MIB", "igmpGroupVlanId"),
    (0, "CENTILLION-MCAST-MIB", "igmpGroupStatic"),
    (0, "CENTILLION-MCAST-MIB", "igmpGroupAddress"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("mandatory")
_IgmpGroupVlanId_Type = VlanId
_IgmpGroupVlanId_Object = MibTableColumn
igmpGroupVlanId = _IgmpGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 1),
    _IgmpGroupVlanId_Type()
)
igmpGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupVlanId.setStatus("mandatory")
_IgmpGroupStatic_Type = Boolean
_IgmpGroupStatic_Object = MibTableColumn
igmpGroupStatic = _IgmpGroupStatic_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 2),
    _IgmpGroupStatic_Type()
)
igmpGroupStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupStatic.setStatus("mandatory")
_IgmpGroupAddress_Type = IpAddress
_IgmpGroupAddress_Object = MibTableColumn
igmpGroupAddress = _IgmpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 3),
    _IgmpGroupAddress_Type()
)
igmpGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupAddress.setStatus("mandatory")


class _IgmpGroupIncluded_Type(Integer32):
    """Custom type igmpGroupIncluded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_IgmpGroupIncluded_Type.__name__ = "Integer32"
_IgmpGroupIncluded_Object = MibTableColumn
igmpGroupIncluded = _IgmpGroupIncluded_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 4),
    _IgmpGroupIncluded_Type()
)
igmpGroupIncluded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGroupIncluded.setStatus("mandatory")
_IgmpGroupStatus_Type = StatusIndicator
_IgmpGroupStatus_Object = MibTableColumn
igmpGroupStatus = _IgmpGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 5),
    _IgmpGroupStatus_Type()
)
igmpGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGroupStatus.setStatus("mandatory")
_IgmpRouterPortTable_Object = MibTable
igmpRouterPortTable = _IgmpRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    igmpRouterPortTable.setStatus("mandatory")
_IgmpRouterPortEntry_Object = MibTableRow
igmpRouterPortEntry = _IgmpRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1)
)
igmpRouterPortEntry.setIndexNames(
    (0, "CENTILLION-MCAST-MIB", "igmpRouterPortVlanId"),
    (0, "CENTILLION-MCAST-MIB", "igmpRouterPortStatic"),
    (0, "CENTILLION-MCAST-MIB", "igmpRouterPortCard"),
    (0, "CENTILLION-MCAST-MIB", "igmpRouterPortPort"),
)
if mibBuilder.loadTexts:
    igmpRouterPortEntry.setStatus("mandatory")
_IgmpRouterPortVlanId_Type = VlanId
_IgmpRouterPortVlanId_Object = MibTableColumn
igmpRouterPortVlanId = _IgmpRouterPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 1),
    _IgmpRouterPortVlanId_Type()
)
igmpRouterPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPortVlanId.setStatus("mandatory")
_IgmpRouterPortStatic_Type = Boolean
_IgmpRouterPortStatic_Object = MibTableColumn
igmpRouterPortStatic = _IgmpRouterPortStatic_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 2),
    _IgmpRouterPortStatic_Type()
)
igmpRouterPortStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPortStatic.setStatus("mandatory")
_IgmpRouterPortCard_Type = CardId
_IgmpRouterPortCard_Object = MibTableColumn
igmpRouterPortCard = _IgmpRouterPortCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 3),
    _IgmpRouterPortCard_Type()
)
igmpRouterPortCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPortCard.setStatus("mandatory")
_IgmpRouterPortPort_Type = PortId
_IgmpRouterPortPort_Object = MibTableColumn
igmpRouterPortPort = _IgmpRouterPortPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 4),
    _IgmpRouterPortPort_Type()
)
igmpRouterPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPortPort.setStatus("mandatory")
_IgmpRouterPortStatus_Type = StatusIndicator
_IgmpRouterPortStatus_Object = MibTableColumn
igmpRouterPortStatus = _IgmpRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 5),
    _IgmpRouterPortStatus_Type()
)
igmpRouterPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpRouterPortStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-MCAST-MIB",
    **{"VlanId": VlanId,
       "vlan": vlan,
       "vlanMcastProtocolGroup": vlanMcastProtocolGroup,
       "vlanIGMPProtocolGroup": vlanIGMPProtocolGroup,
       "vlanIGMPConfig": vlanIGMPConfig,
       "igmpGeneralConfigTable": igmpGeneralConfigTable,
       "igmpGeneralConfigEntry": igmpGeneralConfigEntry,
       "igmpGeneralConfigVlanId": igmpGeneralConfigVlanId,
       "igmpGeneralConfigPseudoQuery": igmpGeneralConfigPseudoQuery,
       "igmpGeneralConfigIrapQuery": igmpGeneralConfigIrapQuery,
       "igmpGeneralConfigIgmpSupport": igmpGeneralConfigIgmpSupport,
       "igmpGeneralConfigMaxGroup": igmpGeneralConfigMaxGroup,
       "igmpTimerConfigTable": igmpTimerConfigTable,
       "igmpTimerConfigEntry": igmpTimerConfigEntry,
       "igmpTimerConfigVlanId": igmpTimerConfigVlanId,
       "igmpTimerConfigTimerRobustness": igmpTimerConfigTimerRobustness,
       "igmpTimerConfigQueryInterval": igmpTimerConfigQueryInterval,
       "igmpTimerConfigQueryResponse": igmpTimerConfigQueryResponse,
       "igmpGroupTable": igmpGroupTable,
       "igmpGroupEntry": igmpGroupEntry,
       "igmpGroupVlanId": igmpGroupVlanId,
       "igmpGroupStatic": igmpGroupStatic,
       "igmpGroupAddress": igmpGroupAddress,
       "igmpGroupIncluded": igmpGroupIncluded,
       "igmpGroupStatus": igmpGroupStatus,
       "igmpRouterPortTable": igmpRouterPortTable,
       "igmpRouterPortEntry": igmpRouterPortEntry,
       "igmpRouterPortVlanId": igmpRouterPortVlanId,
       "igmpRouterPortStatic": igmpRouterPortStatic,
       "igmpRouterPortCard": igmpRouterPortCard,
       "igmpRouterPortPort": igmpRouterPortPort,
       "igmpRouterPortStatus": igmpRouterPortStatus}
)
