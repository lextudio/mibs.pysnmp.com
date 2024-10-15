# SNMP MIB module (LUMINOUS-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LUMINOUS-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:33 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumTopologyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Luminous_ObjectIdentity = ObjectIdentity
luminous = _Luminous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614)
)
_LumADM_ObjectIdentity = ObjectIdentity
lumADM = _LumADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1)
)
_LumRingCommands_ObjectIdentity = ObjectIdentity
lumRingCommands = _LumRingCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1)
)
_LumTopoDiscoveryGroup_ObjectIdentity = ObjectIdentity
lumTopoDiscoveryGroup = _LumTopoDiscoveryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1)
)


class _LumTopoDiscoveryRetries_Type(Integer32):
    """Custom type lumTopoDiscoveryRetries based on Integer32"""
    defaultValue = 3


_LumTopoDiscoveryRetries_Object = MibScalar
lumTopoDiscoveryRetries = _LumTopoDiscoveryRetries_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1, 1),
    _LumTopoDiscoveryRetries_Type()
)
lumTopoDiscoveryRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumTopoDiscoveryRetries.setStatus("current")
_LumTopoNeighborInfoTimer_Type = Integer32
_LumTopoNeighborInfoTimer_Object = MibScalar
lumTopoNeighborInfoTimer = _LumTopoNeighborInfoTimer_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1, 2),
    _LumTopoNeighborInfoTimer_Type()
)
lumTopoNeighborInfoTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumTopoNeighborInfoTimer.setStatus("current")
_LumTopoDiscoveryConvergenceTimer_Type = Integer32
_LumTopoDiscoveryConvergenceTimer_Object = MibScalar
lumTopoDiscoveryConvergenceTimer = _LumTopoDiscoveryConvergenceTimer_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1, 3),
    _LumTopoDiscoveryConvergenceTimer_Type()
)
lumTopoDiscoveryConvergenceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumTopoDiscoveryConvergenceTimer.setStatus("current")
_LumTopoDiscoveryTimer_Type = Integer32
_LumTopoDiscoveryTimer_Object = MibScalar
lumTopoDiscoveryTimer = _LumTopoDiscoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1, 4),
    _LumTopoDiscoveryTimer_Type()
)
lumTopoDiscoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumTopoDiscoveryTimer.setStatus("current")


class _LumTopoDiscovery_Type(Integer32):
    """Custom type lumTopoDiscovery based on Integer32"""
    defaultValue = 1

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
        *(("discoveryFailed", 4),
          ("doDiscover", 2),
          ("none", 1),
          ("stopDiscover", 3))
    )


_LumTopoDiscovery_Type.__name__ = "Integer32"
_LumTopoDiscovery_Object = MibScalar
lumTopoDiscovery = _LumTopoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1, 5),
    _LumTopoDiscovery_Type()
)
lumTopoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumTopoDiscovery.setStatus("current")
_LumTopoDiscoveryFailedNode_Type = IpAddress
_LumTopoDiscoveryFailedNode_Object = MibScalar
lumTopoDiscoveryFailedNode = _LumTopoDiscoveryFailedNode_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 1, 6),
    _LumTopoDiscoveryFailedNode_Type()
)
lumTopoDiscoveryFailedNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumTopoDiscoveryFailedNode.setStatus("current")


class _LumRingCommand_Type(Integer32):
    """Custom type lumRingCommand based on Integer32"""
    defaultValue = 1

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
        *(("clearAll", 2),
          ("commandFailed", 4),
          ("lockoutOfProtection", 3),
          ("none", 1))
    )


_LumRingCommand_Type.__name__ = "Integer32"
_LumRingCommand_Object = MibScalar
lumRingCommand = _LumRingCommand_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 2),
    _LumRingCommand_Type()
)
lumRingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumRingCommand.setStatus("current")


class _LumRingRevertiveMode_Type(Integer32):
    """Custom type lumRingRevertiveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertiveMode", 2),
          ("revertiveMode", 1))
    )


_LumRingRevertiveMode_Type.__name__ = "Integer32"
_LumRingRevertiveMode_Object = MibScalar
lumRingRevertiveMode = _LumRingRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 3),
    _LumRingRevertiveMode_Type()
)
lumRingRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumRingRevertiveMode.setStatus("current")


class _LumProtectionSwitchHysteresis_Type(Integer32):
    """Custom type lumProtectionSwitchHysteresis based on Integer32"""
    defaultValue = 10


_LumProtectionSwitchHysteresis_Object = MibScalar
lumProtectionSwitchHysteresis = _LumProtectionSwitchHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 1, 4),
    _LumProtectionSwitchHysteresis_Type()
)
lumProtectionSwitchHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumProtectionSwitchHysteresis.setStatus("current")
_LumProtectionSwitchingTable_Object = MibTable
lumProtectionSwitchingTable = _LumProtectionSwitchingTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lumProtectionSwitchingTable.setStatus("current")
_LumProtectionSwitchingEntry_Object = MibTableRow
lumProtectionSwitchingEntry = _LumProtectionSwitchingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2, 1)
)
lumProtectionSwitchingEntry.setIndexNames(
    (0, "LUMINOUS-TOPOLOGY-MIB", "lumProtDestinationIP"),
)
if mibBuilder.loadTexts:
    lumProtectionSwitchingEntry.setStatus("current")
_LumProtDestinationIP_Type = IpAddress
_LumProtDestinationIP_Object = MibTableColumn
lumProtDestinationIP = _LumProtDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2, 1, 1),
    _LumProtDestinationIP_Type()
)
lumProtDestinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumProtDestinationIP.setStatus("current")
_LumProtMeasDestCost_Type = Integer32
_LumProtMeasDestCost_Object = MibTableColumn
lumProtMeasDestCost = _LumProtMeasDestCost_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2, 1, 2),
    _LumProtMeasDestCost_Type()
)
lumProtMeasDestCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumProtMeasDestCost.setStatus("current")
_LumProtNonRevDestCost_Type = Integer32
_LumProtNonRevDestCost_Object = MibTableColumn
lumProtNonRevDestCost = _LumProtNonRevDestCost_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2, 1, 3),
    _LumProtNonRevDestCost_Type()
)
lumProtNonRevDestCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumProtNonRevDestCost.setStatus("current")
_LumProtMeasPrefDir_Type = Integer32
_LumProtMeasPrefDir_Object = MibTableColumn
lumProtMeasPrefDir = _LumProtMeasPrefDir_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2, 1, 4),
    _LumProtMeasPrefDir_Type()
)
lumProtMeasPrefDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumProtMeasPrefDir.setStatus("current")
_LumProtNonRevPrefDir_Type = Integer32
_LumProtNonRevPrefDir_Object = MibTableColumn
lumProtNonRevPrefDir = _LumProtNonRevPrefDir_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 2, 1, 5),
    _LumProtNonRevPrefDir_Type()
)
lumProtNonRevPrefDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumProtNonRevPrefDir.setStatus("current")
_LumRingLinkTable_Object = MibTable
lumRingLinkTable = _LumRingLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lumRingLinkTable.setStatus("current")
_LumRingLinkEntry_Object = MibTableRow
lumRingLinkEntry = _LumRingLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1)
)
lumRingLinkEntry.setIndexNames(
    (0, "LUMINOUS-TOPOLOGY-MIB", "lumLinkIngressNodeIP"),
    (0, "LUMINOUS-TOPOLOGY-MIB", "lumLinkEgressNodeIP"),
    (0, "LUMINOUS-TOPOLOGY-MIB", "lumLinkIngressInterface"),
    (0, "LUMINOUS-TOPOLOGY-MIB", "lumLinkEgressInterface"),
)
if mibBuilder.loadTexts:
    lumRingLinkEntry.setStatus("current")
_LumLinkIngressNodeIP_Type = IpAddress
_LumLinkIngressNodeIP_Object = MibTableColumn
lumLinkIngressNodeIP = _LumLinkIngressNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 1),
    _LumLinkIngressNodeIP_Type()
)
lumLinkIngressNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkIngressNodeIP.setStatus("current")
_LumLinkEgressNodeIP_Type = IpAddress
_LumLinkEgressNodeIP_Object = MibTableColumn
lumLinkEgressNodeIP = _LumLinkEgressNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 2),
    _LumLinkEgressNodeIP_Type()
)
lumLinkEgressNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkEgressNodeIP.setStatus("current")
_LumLinkIngressInterface_Type = Integer32
_LumLinkIngressInterface_Object = MibTableColumn
lumLinkIngressInterface = _LumLinkIngressInterface_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 3),
    _LumLinkIngressInterface_Type()
)
lumLinkIngressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkIngressInterface.setStatus("current")
_LumLinkEgressInterface_Type = Integer32
_LumLinkEgressInterface_Object = MibTableColumn
lumLinkEgressInterface = _LumLinkEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 4),
    _LumLinkEgressInterface_Type()
)
lumLinkEgressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkEgressInterface.setStatus("current")
_LumLinkOperStatus_Type = Integer32
_LumLinkOperStatus_Object = MibTableColumn
lumLinkOperStatus = _LumLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 5),
    _LumLinkOperStatus_Type()
)
lumLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkOperStatus.setStatus("current")
_LumLinkNonRevStatus_Type = Integer32
_LumLinkNonRevStatus_Object = MibTableColumn
lumLinkNonRevStatus = _LumLinkNonRevStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 6),
    _LumLinkNonRevStatus_Type()
)
lumLinkNonRevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkNonRevStatus.setStatus("current")
_LumLinkAdminStatus_Type = Integer32
_LumLinkAdminStatus_Object = MibTableColumn
lumLinkAdminStatus = _LumLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 7),
    _LumLinkAdminStatus_Type()
)
lumLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumLinkAdminStatus.setStatus("current")
_LumLinkSyncOperStatus_Type = Integer32
_LumLinkSyncOperStatus_Object = MibTableColumn
lumLinkSyncOperStatus = _LumLinkSyncOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 8),
    _LumLinkSyncOperStatus_Type()
)
lumLinkSyncOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkSyncOperStatus.setStatus("current")
_LumLinkSyncNonRevStatus_Type = Integer32
_LumLinkSyncNonRevStatus_Object = MibTableColumn
lumLinkSyncNonRevStatus = _LumLinkSyncNonRevStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 9),
    _LumLinkSyncNonRevStatus_Type()
)
lumLinkSyncNonRevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumLinkSyncNonRevStatus.setStatus("current")
_LumLinkSyncAdminStatus_Type = Integer32
_LumLinkSyncAdminStatus_Object = MibTableColumn
lumLinkSyncAdminStatus = _LumLinkSyncAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 3, 1, 10),
    _LumLinkSyncAdminStatus_Type()
)
lumLinkSyncAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumLinkSyncAdminStatus.setStatus("current")
_LumRingThresholdTable_Object = MibTable
lumRingThresholdTable = _LumRingThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lumRingThresholdTable.setStatus("current")
_LumRingThresholdEntry_Object = MibTableRow
lumRingThresholdEntry = _LumRingThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 4, 1)
)
lumRingThresholdEntry.setIndexNames(
    (0, "LUMINOUS-TOPOLOGY-MIB", "lumRingThresholdWindow"),
)
if mibBuilder.loadTexts:
    lumRingThresholdEntry.setStatus("current")
_LumRingThresholdWindow_Type = Integer32
_LumRingThresholdWindow_Object = MibTableColumn
lumRingThresholdWindow = _LumRingThresholdWindow_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 4, 1, 1),
    _LumRingThresholdWindow_Type()
)
lumRingThresholdWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumRingThresholdWindow.setStatus("current")
_LumRingThresholdValue_Type = Integer32
_LumRingThresholdValue_Object = MibTableColumn
lumRingThresholdValue = _LumRingThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 4, 1, 2),
    _LumRingThresholdValue_Type()
)
lumRingThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumRingThresholdValue.setStatus("current")
_LumRingThresholdStatus_Type = RowStatus
_LumRingThresholdStatus_Object = MibTableColumn
lumRingThresholdStatus = _LumRingThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 3, 4, 1, 3),
    _LumRingThresholdStatus_Type()
)
lumRingThresholdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumRingThresholdStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUMINOUS-TOPOLOGY-MIB",
    **{"luminous": luminous,
       "lumADM": lumADM,
       "lumTopologyMIB": lumTopologyMIB,
       "lumRingCommands": lumRingCommands,
       "lumTopoDiscoveryGroup": lumTopoDiscoveryGroup,
       "lumTopoDiscoveryRetries": lumTopoDiscoveryRetries,
       "lumTopoNeighborInfoTimer": lumTopoNeighborInfoTimer,
       "lumTopoDiscoveryConvergenceTimer": lumTopoDiscoveryConvergenceTimer,
       "lumTopoDiscoveryTimer": lumTopoDiscoveryTimer,
       "lumTopoDiscovery": lumTopoDiscovery,
       "lumTopoDiscoveryFailedNode": lumTopoDiscoveryFailedNode,
       "lumRingCommand": lumRingCommand,
       "lumRingRevertiveMode": lumRingRevertiveMode,
       "lumProtectionSwitchHysteresis": lumProtectionSwitchHysteresis,
       "lumProtectionSwitchingTable": lumProtectionSwitchingTable,
       "lumProtectionSwitchingEntry": lumProtectionSwitchingEntry,
       "lumProtDestinationIP": lumProtDestinationIP,
       "lumProtMeasDestCost": lumProtMeasDestCost,
       "lumProtNonRevDestCost": lumProtNonRevDestCost,
       "lumProtMeasPrefDir": lumProtMeasPrefDir,
       "lumProtNonRevPrefDir": lumProtNonRevPrefDir,
       "lumRingLinkTable": lumRingLinkTable,
       "lumRingLinkEntry": lumRingLinkEntry,
       "lumLinkIngressNodeIP": lumLinkIngressNodeIP,
       "lumLinkEgressNodeIP": lumLinkEgressNodeIP,
       "lumLinkIngressInterface": lumLinkIngressInterface,
       "lumLinkEgressInterface": lumLinkEgressInterface,
       "lumLinkOperStatus": lumLinkOperStatus,
       "lumLinkNonRevStatus": lumLinkNonRevStatus,
       "lumLinkAdminStatus": lumLinkAdminStatus,
       "lumLinkSyncOperStatus": lumLinkSyncOperStatus,
       "lumLinkSyncNonRevStatus": lumLinkSyncNonRevStatus,
       "lumLinkSyncAdminStatus": lumLinkSyncAdminStatus,
       "lumRingThresholdTable": lumRingThresholdTable,
       "lumRingThresholdEntry": lumRingThresholdEntry,
       "lumRingThresholdWindow": lumRingThresholdWindow,
       "lumRingThresholdValue": lumRingThresholdValue,
       "lumRingThresholdStatus": lumRingThresholdStatus}
)
