# SNMP MIB module (CTRON-SFPS-VSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-VSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:36 2024
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

(vlanSpanningTreePort,
 vlanSpanningTreeSwitch) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "vlanSpanningTreePort",
    "vlanSpanningTreeSwitch")

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



class SfpsSwitchPort(Integer32):
    """Custom type SfpsSwitchPort based on Integer32"""




class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VlanSpanningTreePortTable_Object = MibTable
vlanSpanningTreePortTable = _VlanSpanningTreePortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    vlanSpanningTreePortTable.setStatus("mandatory")
_VlanSpanningTreePortEntry_Object = MibTableRow
vlanSpanningTreePortEntry = _VlanSpanningTreePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1)
)
vlanSpanningTreePortEntry.setIndexNames(
    (0, "CTRON-SFPS-VSTP-MIB", "vlanSpanningTreePortPortNumber"),
)
if mibBuilder.loadTexts:
    vlanSpanningTreePortEntry.setStatus("mandatory")
_VlanSpanningTreePortPortNumber_Type = SfpsSwitchPort
_VlanSpanningTreePortPortNumber_Object = MibTableColumn
vlanSpanningTreePortPortNumber = _VlanSpanningTreePortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 1),
    _VlanSpanningTreePortPortNumber_Type()
)
vlanSpanningTreePortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortPortNumber.setStatus("mandatory")


class _VlanSpanningTreePortPortState_Type(Integer32):
    """Custom type vlanSpanningTreePortPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("broken", 7),
          ("disabled", 2),
          ("enabled", 1),
          ("forwarding", 6),
          ("learning", 5),
          ("listening", 4))
    )


_VlanSpanningTreePortPortState_Type.__name__ = "Integer32"
_VlanSpanningTreePortPortState_Object = MibTableColumn
vlanSpanningTreePortPortState = _VlanSpanningTreePortPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 2),
    _VlanSpanningTreePortPortState_Type()
)
vlanSpanningTreePortPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortPortState.setStatus("mandatory")
_VlanSpanningTreePortPortIdentifier_Type = HexInteger
_VlanSpanningTreePortPortIdentifier_Object = MibTableColumn
vlanSpanningTreePortPortIdentifier = _VlanSpanningTreePortPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 3),
    _VlanSpanningTreePortPortIdentifier_Type()
)
vlanSpanningTreePortPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortPortIdentifier.setStatus("mandatory")
_VlanSpanningTreePortPathCost_Type = Integer32
_VlanSpanningTreePortPathCost_Object = MibTableColumn
vlanSpanningTreePortPathCost = _VlanSpanningTreePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 4),
    _VlanSpanningTreePortPathCost_Type()
)
vlanSpanningTreePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpanningTreePortPathCost.setStatus("mandatory")
_VlanSpanningTreePortDesignatedRoot_Type = OctetString
_VlanSpanningTreePortDesignatedRoot_Object = MibTableColumn
vlanSpanningTreePortDesignatedRoot = _VlanSpanningTreePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 5),
    _VlanSpanningTreePortDesignatedRoot_Type()
)
vlanSpanningTreePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortDesignatedRoot.setStatus("mandatory")
_VlanSpanningTreePortDesignatedCost_Type = Integer32
_VlanSpanningTreePortDesignatedCost_Object = MibTableColumn
vlanSpanningTreePortDesignatedCost = _VlanSpanningTreePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 6),
    _VlanSpanningTreePortDesignatedCost_Type()
)
vlanSpanningTreePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortDesignatedCost.setStatus("mandatory")
_VlanSpanningTreePortDesignatedBridge_Type = OctetString
_VlanSpanningTreePortDesignatedBridge_Object = MibTableColumn
vlanSpanningTreePortDesignatedBridge = _VlanSpanningTreePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 7),
    _VlanSpanningTreePortDesignatedBridge_Type()
)
vlanSpanningTreePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortDesignatedBridge.setStatus("mandatory")
_VlanSpanningTreePortDesignatedPort_Type = HexInteger
_VlanSpanningTreePortDesignatedPort_Object = MibTableColumn
vlanSpanningTreePortDesignatedPort = _VlanSpanningTreePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 8),
    _VlanSpanningTreePortDesignatedPort_Type()
)
vlanSpanningTreePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreePortDesignatedPort.setStatus("mandatory")
_VlanSpanningTreeSwitchTable_Object = MibTable
vlanSpanningTreeSwitchTable = _VlanSpanningTreeSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchTable.setStatus("mandatory")
_VlanSpanningTreeSwitchEntry_Object = MibTableRow
vlanSpanningTreeSwitchEntry = _VlanSpanningTreeSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1)
)
vlanSpanningTreeSwitchEntry.setIndexNames(
    (0, "CTRON-SFPS-VSTP-MIB", "vlanSpanningTreeSwitchIndex"),
)
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchEntry.setStatus("mandatory")
_VlanSpanningTreeSwitchIndex_Type = Integer32
_VlanSpanningTreeSwitchIndex_Object = MibTableColumn
vlanSpanningTreeSwitchIndex = _VlanSpanningTreeSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 1),
    _VlanSpanningTreeSwitchIndex_Type()
)
vlanSpanningTreeSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchIndex.setStatus("mandatory")
_VlanSpanningTreeSwitchBridgePriority_Type = HexInteger
_VlanSpanningTreeSwitchBridgePriority_Object = MibTableColumn
vlanSpanningTreeSwitchBridgePriority = _VlanSpanningTreeSwitchBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 2),
    _VlanSpanningTreeSwitchBridgePriority_Type()
)
vlanSpanningTreeSwitchBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchBridgePriority.setStatus("mandatory")
_VlanSpanningTreeSwitchBridgeId_Type = OctetString
_VlanSpanningTreeSwitchBridgeId_Object = MibTableColumn
vlanSpanningTreeSwitchBridgeId = _VlanSpanningTreeSwitchBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 3),
    _VlanSpanningTreeSwitchBridgeId_Type()
)
vlanSpanningTreeSwitchBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchBridgeId.setStatus("mandatory")
_VlanSpanningTreeSwitchDesignatedRoot_Type = OctetString
_VlanSpanningTreeSwitchDesignatedRoot_Object = MibTableColumn
vlanSpanningTreeSwitchDesignatedRoot = _VlanSpanningTreeSwitchDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 4),
    _VlanSpanningTreeSwitchDesignatedRoot_Type()
)
vlanSpanningTreeSwitchDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchDesignatedRoot.setStatus("mandatory")
_VlanSpanningTreeSwitchRootPathCost_Type = Integer32
_VlanSpanningTreeSwitchRootPathCost_Object = MibTableColumn
vlanSpanningTreeSwitchRootPathCost = _VlanSpanningTreeSwitchRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 5),
    _VlanSpanningTreeSwitchRootPathCost_Type()
)
vlanSpanningTreeSwitchRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchRootPathCost.setStatus("mandatory")
_VlanSpanningTreeSwitchOperTime_Type = TimeTicks
_VlanSpanningTreeSwitchOperTime_Object = MibTableColumn
vlanSpanningTreeSwitchOperTime = _VlanSpanningTreeSwitchOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 6),
    _VlanSpanningTreeSwitchOperTime_Type()
)
vlanSpanningTreeSwitchOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchOperTime.setStatus("mandatory")
_VlanSpanningTreeSwitchRootPort_Type = SfpsSwitchPort
_VlanSpanningTreeSwitchRootPort_Object = MibTableColumn
vlanSpanningTreeSwitchRootPort = _VlanSpanningTreeSwitchRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 7),
    _VlanSpanningTreeSwitchRootPort_Type()
)
vlanSpanningTreeSwitchRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchRootPort.setStatus("mandatory")
_VlanSpanningTreeSwitchRootPortTime_Type = TimeTicks
_VlanSpanningTreeSwitchRootPortTime_Object = MibTableColumn
vlanSpanningTreeSwitchRootPortTime = _VlanSpanningTreeSwitchRootPortTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 8),
    _VlanSpanningTreeSwitchRootPortTime_Type()
)
vlanSpanningTreeSwitchRootPortTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchRootPortTime.setStatus("mandatory")
_VlanSpanningTreeSwitchPrevRootPort_Type = SfpsSwitchPort
_VlanSpanningTreeSwitchPrevRootPort_Object = MibTableColumn
vlanSpanningTreeSwitchPrevRootPort = _VlanSpanningTreeSwitchPrevRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 9),
    _VlanSpanningTreeSwitchPrevRootPort_Type()
)
vlanSpanningTreeSwitchPrevRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchPrevRootPort.setStatus("mandatory")
_VlanSpanningTreeSwitchPrevRootPortTime_Type = TimeTicks
_VlanSpanningTreeSwitchPrevRootPortTime_Object = MibTableColumn
vlanSpanningTreeSwitchPrevRootPortTime = _VlanSpanningTreeSwitchPrevRootPortTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 10),
    _VlanSpanningTreeSwitchPrevRootPortTime_Type()
)
vlanSpanningTreeSwitchPrevRootPortTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchPrevRootPortTime.setStatus("mandatory")
_VlanSpanningTreeSwitchMaxAge_Type = Integer32
_VlanSpanningTreeSwitchMaxAge_Object = MibTableColumn
vlanSpanningTreeSwitchMaxAge = _VlanSpanningTreeSwitchMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 11),
    _VlanSpanningTreeSwitchMaxAge_Type()
)
vlanSpanningTreeSwitchMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchMaxAge.setStatus("mandatory")
_VlanSpanningTreeSwitchHelloTime_Type = Integer32
_VlanSpanningTreeSwitchHelloTime_Object = MibTableColumn
vlanSpanningTreeSwitchHelloTime = _VlanSpanningTreeSwitchHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 12),
    _VlanSpanningTreeSwitchHelloTime_Type()
)
vlanSpanningTreeSwitchHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchHelloTime.setStatus("mandatory")
_VlanSpanningTreeSwitchForwardDelay_Type = Integer32
_VlanSpanningTreeSwitchForwardDelay_Object = MibTableColumn
vlanSpanningTreeSwitchForwardDelay = _VlanSpanningTreeSwitchForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 13),
    _VlanSpanningTreeSwitchForwardDelay_Type()
)
vlanSpanningTreeSwitchForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpanningTreeSwitchForwardDelay.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-VSTP-MIB",
    **{"SfpsSwitchPort": SfpsSwitchPort,
       "HexInteger": HexInteger,
       "vlanSpanningTreePortTable": vlanSpanningTreePortTable,
       "vlanSpanningTreePortEntry": vlanSpanningTreePortEntry,
       "vlanSpanningTreePortPortNumber": vlanSpanningTreePortPortNumber,
       "vlanSpanningTreePortPortState": vlanSpanningTreePortPortState,
       "vlanSpanningTreePortPortIdentifier": vlanSpanningTreePortPortIdentifier,
       "vlanSpanningTreePortPathCost": vlanSpanningTreePortPathCost,
       "vlanSpanningTreePortDesignatedRoot": vlanSpanningTreePortDesignatedRoot,
       "vlanSpanningTreePortDesignatedCost": vlanSpanningTreePortDesignatedCost,
       "vlanSpanningTreePortDesignatedBridge": vlanSpanningTreePortDesignatedBridge,
       "vlanSpanningTreePortDesignatedPort": vlanSpanningTreePortDesignatedPort,
       "vlanSpanningTreeSwitchTable": vlanSpanningTreeSwitchTable,
       "vlanSpanningTreeSwitchEntry": vlanSpanningTreeSwitchEntry,
       "vlanSpanningTreeSwitchIndex": vlanSpanningTreeSwitchIndex,
       "vlanSpanningTreeSwitchBridgePriority": vlanSpanningTreeSwitchBridgePriority,
       "vlanSpanningTreeSwitchBridgeId": vlanSpanningTreeSwitchBridgeId,
       "vlanSpanningTreeSwitchDesignatedRoot": vlanSpanningTreeSwitchDesignatedRoot,
       "vlanSpanningTreeSwitchRootPathCost": vlanSpanningTreeSwitchRootPathCost,
       "vlanSpanningTreeSwitchOperTime": vlanSpanningTreeSwitchOperTime,
       "vlanSpanningTreeSwitchRootPort": vlanSpanningTreeSwitchRootPort,
       "vlanSpanningTreeSwitchRootPortTime": vlanSpanningTreeSwitchRootPortTime,
       "vlanSpanningTreeSwitchPrevRootPort": vlanSpanningTreeSwitchPrevRootPort,
       "vlanSpanningTreeSwitchPrevRootPortTime": vlanSpanningTreeSwitchPrevRootPortTime,
       "vlanSpanningTreeSwitchMaxAge": vlanSpanningTreeSwitchMaxAge,
       "vlanSpanningTreeSwitchHelloTime": vlanSpanningTreeSwitchHelloTime,
       "vlanSpanningTreeSwitchForwardDelay": vlanSpanningTreeSwitchForwardDelay}
)
