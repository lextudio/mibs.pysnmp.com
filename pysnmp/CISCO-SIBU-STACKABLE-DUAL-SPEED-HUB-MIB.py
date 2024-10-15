# SNMP MIB module (CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:16 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(rptrGroupIndex,
 rptrPortGroupIndex,
 rptrPortIndex) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrGroupIndex",
    "rptrPortGroupIndex",
    "rptrPortIndex")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSibuStackableDualSpeedHubMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44)
)
ciscoSibuStackableDualSpeedHubMIB.setRevisions(
        ("1998-10-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HubNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSibuStackableDualSpeedHubMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBObjects = _CiscoSibuStackableDualSpeedHubMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1)
)
_CssSystem_ObjectIdentity = ObjectIdentity
cssSystem = _CssSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 1)
)


class _CssSystemLinkTraps_Type(Integer32):
    """Custom type cssSystemLinkTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CssSystemLinkTraps_Type.__name__ = "Integer32"
_CssSystemLinkTraps_Object = MibScalar
cssSystemLinkTraps = _CssSystemLinkTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 1, 1),
    _CssSystemLinkTraps_Type()
)
cssSystemLinkTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssSystemLinkTraps.setStatus("current")
_CssGroup_ObjectIdentity = ObjectIdentity
cssGroup = _CssGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2)
)
_CssGroupTable_Object = MibTable
cssGroupTable = _CssGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cssGroupTable.setStatus("current")
_CssGroupEntry_Object = MibTableRow
cssGroupEntry = _CssGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1)
)
cssGroupEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrGroupIndex"),
)
if mibBuilder.loadTexts:
    cssGroupEntry.setStatus("current")
_CssGroupID_Type = HubNumber
_CssGroupID_Object = MibTableColumn
cssGroupID = _CssGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 1),
    _CssGroupID_Type()
)
cssGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupID.setStatus("current")


class _CssGroupType_Type(Integer32):
    """Custom type cssGroupType based on Integer32"""
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
        *(("cisco1538MDS", 1),
          ("cisco1538UDS", 2),
          ("wsC412", 4),
          ("wsC412M", 3),
          ("wsC424", 6),
          ("wsC424M", 5))
    )


_CssGroupType_Type.__name__ = "Integer32"
_CssGroupType_Object = MibTableColumn
cssGroupType = _CssGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 2),
    _CssGroupType_Type()
)
cssGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupType.setStatus("current")


class _CssGroupSerialNo_Type(DisplayString):
    """Custom type cssGroupSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CssGroupSerialNo_Type.__name__ = "DisplayString"
_CssGroupSerialNo_Object = MibTableColumn
cssGroupSerialNo = _CssGroupSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 4),
    _CssGroupSerialNo_Type()
)
cssGroupSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupSerialNo.setStatus("current")


class _CssGroupBoardRevision_Type(Integer32):
    """Custom type cssGroupBoardRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CssGroupBoardRevision_Type.__name__ = "Integer32"
_CssGroupBoardRevision_Object = MibTableColumn
cssGroupBoardRevision = _CssGroupBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 5),
    _CssGroupBoardRevision_Type()
)
cssGroupBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupBoardRevision.setStatus("current")


class _CssGroupAgentBootVersion_Type(DisplayString):
    """Custom type cssGroupAgentBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CssGroupAgentBootVersion_Type.__name__ = "DisplayString"
_CssGroupAgentBootVersion_Object = MibTableColumn
cssGroupAgentBootVersion = _CssGroupAgentBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 6),
    _CssGroupAgentBootVersion_Type()
)
cssGroupAgentBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupAgentBootVersion.setStatus("current")


class _CssGroupAgentFirmwareVersion_Type(DisplayString):
    """Custom type cssGroupAgentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CssGroupAgentFirmwareVersion_Type.__name__ = "DisplayString"
_CssGroupAgentFirmwareVersion_Object = MibTableColumn
cssGroupAgentFirmwareVersion = _CssGroupAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 7),
    _CssGroupAgentFirmwareVersion_Type()
)
cssGroupAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupAgentFirmwareVersion.setStatus("current")


class _CssGroupAgentStatus_Type(Integer32):
    """Custom type cssGroupAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("notPresent", 1),
          ("primary", 2))
    )


_CssGroupAgentStatus_Type.__name__ = "Integer32"
_CssGroupAgentStatus_Object = MibTableColumn
cssGroupAgentStatus = _CssGroupAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 8),
    _CssGroupAgentStatus_Type()
)
cssGroupAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupAgentStatus.setStatus("current")
_CssGroupAgentPhysAddress_Type = PhysAddress
_CssGroupAgentPhysAddress_Object = MibTableColumn
cssGroupAgentPhysAddress = _CssGroupAgentPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 9),
    _CssGroupAgentPhysAddress_Type()
)
cssGroupAgentPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupAgentPhysAddress.setStatus("current")


class _CssGroupInternalPowerState_Type(Integer32):
    """Custom type cssGroupInternalPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CssGroupInternalPowerState_Type.__name__ = "Integer32"
_CssGroupInternalPowerState_Object = MibTableColumn
cssGroupInternalPowerState = _CssGroupInternalPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 12),
    _CssGroupInternalPowerState_Type()
)
cssGroupInternalPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupInternalPowerState.setStatus("current")


class _CssGroupRedundantPowerState_Type(Integer32):
    """Custom type cssGroupRedundantPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("healthy", 2),
          ("off", 1))
    )


_CssGroupRedundantPowerState_Type.__name__ = "Integer32"
_CssGroupRedundantPowerState_Object = MibTableColumn
cssGroupRedundantPowerState = _CssGroupRedundantPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 13),
    _CssGroupRedundantPowerState_Type()
)
cssGroupRedundantPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssGroupRedundantPowerState.setStatus("current")


class _CssGroupReset_Type(Integer32):
    """Custom type cssGroupReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_CssGroupReset_Type.__name__ = "Integer32"
_CssGroupReset_Object = MibTableColumn
cssGroupReset = _CssGroupReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 14),
    _CssGroupReset_Type()
)
cssGroupReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssGroupReset.setStatus("current")


class _CssGroupConfigDefaultReset_Type(Integer32):
    """Custom type cssGroupConfigDefaultReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_CssGroupConfigDefaultReset_Type.__name__ = "Integer32"
_CssGroupConfigDefaultReset_Object = MibTableColumn
cssGroupConfigDefaultReset = _CssGroupConfigDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 15),
    _CssGroupConfigDefaultReset_Type()
)
cssGroupConfigDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssGroupConfigDefaultReset.setStatus("current")


class _CssGroupIsolatedState_Type(Integer32):
    """Custom type cssGroupIsolatedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("isolated", 1))
    )


_CssGroupIsolatedState_Type.__name__ = "Integer32"
_CssGroupIsolatedState_Object = MibTableColumn
cssGroupIsolatedState = _CssGroupIsolatedState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 16),
    _CssGroupIsolatedState_Type()
)
cssGroupIsolatedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssGroupIsolatedState.setStatus("current")
_CssRepeaterPort_ObjectIdentity = ObjectIdentity
cssRepeaterPort = _CssRepeaterPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3)
)
_CssRepeaterPortTable_Object = MibTable
cssRepeaterPortTable = _CssRepeaterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cssRepeaterPortTable.setStatus("current")
_CssRepeaterPortEntry_Object = MibTableRow
cssRepeaterPortEntry = _CssRepeaterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1)
)
cssRepeaterPortEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrPortGroupIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrPortIndex"),
)
if mibBuilder.loadTexts:
    cssRepeaterPortEntry.setStatus("current")


class _CssRepeaterPortName_Type(DisplayString):
    """Custom type cssRepeaterPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CssRepeaterPortName_Type.__name__ = "DisplayString"
_CssRepeaterPortName_Object = MibTableColumn
cssRepeaterPortName = _CssRepeaterPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 1),
    _CssRepeaterPortName_Type()
)
cssRepeaterPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssRepeaterPortName.setStatus("current")


class _CssRepeaterPortControllerRevision_Type(Integer32):
    """Custom type cssRepeaterPortControllerRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CssRepeaterPortControllerRevision_Type.__name__ = "Integer32"
_CssRepeaterPortControllerRevision_Object = MibTableColumn
cssRepeaterPortControllerRevision = _CssRepeaterPortControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 2),
    _CssRepeaterPortControllerRevision_Type()
)
cssRepeaterPortControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssRepeaterPortControllerRevision.setStatus("current")


class _CssRepeaterPortSpeedAdmin_Type(Integer32):
    """Custom type cssRepeaterPortSpeedAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 3),
          ("oneHundredMbps", 2),
          ("tenMbps", 1))
    )


_CssRepeaterPortSpeedAdmin_Type.__name__ = "Integer32"
_CssRepeaterPortSpeedAdmin_Object = MibTableColumn
cssRepeaterPortSpeedAdmin = _CssRepeaterPortSpeedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 3),
    _CssRepeaterPortSpeedAdmin_Type()
)
cssRepeaterPortSpeedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssRepeaterPortSpeedAdmin.setStatus("current")


class _CssRepeaterPortSpeedStatus_Type(Integer32):
    """Custom type cssRepeaterPortSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredMbps", 2),
          ("tenMbps", 1))
    )


_CssRepeaterPortSpeedStatus_Type.__name__ = "Integer32"
_CssRepeaterPortSpeedStatus_Object = MibTableColumn
cssRepeaterPortSpeedStatus = _CssRepeaterPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 4),
    _CssRepeaterPortSpeedStatus_Type()
)
cssRepeaterPortSpeedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssRepeaterPortSpeedStatus.setStatus("current")


class _CssRepeaterPortLinkStatus_Type(Integer32):
    """Custom type cssRepeaterPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("noLink", 2))
    )


_CssRepeaterPortLinkStatus_Type.__name__ = "Integer32"
_CssRepeaterPortLinkStatus_Object = MibTableColumn
cssRepeaterPortLinkStatus = _CssRepeaterPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 5),
    _CssRepeaterPortLinkStatus_Type()
)
cssRepeaterPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssRepeaterPortLinkStatus.setStatus("current")
_CssSwitchPort_ObjectIdentity = ObjectIdentity
cssSwitchPort = _CssSwitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4)
)
_CssSwitchPortTable_Object = MibTable
cssSwitchPortTable = _CssSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cssSwitchPortTable.setStatus("current")
_CssSwitchPortEntry_Object = MibTableRow
cssSwitchPortEntry = _CssSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1)
)
cssSwitchPortEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrGroupIndex"),
    (0, "CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortModuleID"),
    (0, "CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortPortID"),
)
if mibBuilder.loadTexts:
    cssSwitchPortEntry.setStatus("current")


class _CssSwitchPortModuleID_Type(Integer32):
    """Custom type cssSwitchPortModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CssSwitchPortModuleID_Type.__name__ = "Integer32"
_CssSwitchPortModuleID_Object = MibTableColumn
cssSwitchPortModuleID = _CssSwitchPortModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 1),
    _CssSwitchPortModuleID_Type()
)
cssSwitchPortModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortModuleID.setStatus("current")


class _CssSwitchPortPortID_Type(Integer32):
    """Custom type cssSwitchPortPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CssSwitchPortPortID_Type.__name__ = "Integer32"
_CssSwitchPortPortID_Object = MibTableColumn
cssSwitchPortPortID = _CssSwitchPortPortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 2),
    _CssSwitchPortPortID_Type()
)
cssSwitchPortPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortPortID.setStatus("current")


class _CssSwitchPortName_Type(DisplayString):
    """Custom type cssSwitchPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CssSwitchPortName_Type.__name__ = "DisplayString"
_CssSwitchPortName_Object = MibTableColumn
cssSwitchPortName = _CssSwitchPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 3),
    _CssSwitchPortName_Type()
)
cssSwitchPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssSwitchPortName.setStatus("current")


class _CssSwitchPortType_Type(Integer32):
    """Custom type cssSwitchPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wsX4001", 1),
          ("wsX4002", 2))
    )


_CssSwitchPortType_Type.__name__ = "Integer32"
_CssSwitchPortType_Object = MibTableColumn
cssSwitchPortType = _CssSwitchPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 4),
    _CssSwitchPortType_Type()
)
cssSwitchPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortType.setStatus("current")


class _CssSwitchPortControllerRevision_Type(Integer32):
    """Custom type cssSwitchPortControllerRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CssSwitchPortControllerRevision_Type.__name__ = "Integer32"
_CssSwitchPortControllerRevision_Object = MibTableColumn
cssSwitchPortControllerRevision = _CssSwitchPortControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 5),
    _CssSwitchPortControllerRevision_Type()
)
cssSwitchPortControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortControllerRevision.setStatus("current")


class _CssSwitchPortState_Type(Integer32):
    """Custom type cssSwitchPortState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CssSwitchPortState_Type.__name__ = "Integer32"
_CssSwitchPortState_Object = MibTableColumn
cssSwitchPortState = _CssSwitchPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 6),
    _CssSwitchPortState_Type()
)
cssSwitchPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssSwitchPortState.setStatus("current")


class _CssSwitchPortDuplexAdmin_Type(Integer32):
    """Custom type cssSwitchPortDuplexAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_CssSwitchPortDuplexAdmin_Type.__name__ = "Integer32"
_CssSwitchPortDuplexAdmin_Object = MibTableColumn
cssSwitchPortDuplexAdmin = _CssSwitchPortDuplexAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 7),
    _CssSwitchPortDuplexAdmin_Type()
)
cssSwitchPortDuplexAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssSwitchPortDuplexAdmin.setStatus("current")


class _CssSwitchPortDuplexStatus_Type(Integer32):
    """Custom type cssSwitchPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_CssSwitchPortDuplexStatus_Type.__name__ = "Integer32"
_CssSwitchPortDuplexStatus_Object = MibTableColumn
cssSwitchPortDuplexStatus = _CssSwitchPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 8),
    _CssSwitchPortDuplexStatus_Type()
)
cssSwitchPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortDuplexStatus.setStatus("current")


class _CssSwitchPortSpeedAdmin_Type(Integer32):
    """Custom type cssSwitchPortSpeedAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 3),
          ("oneHundredMbps", 2),
          ("tenMbps", 1))
    )


_CssSwitchPortSpeedAdmin_Type.__name__ = "Integer32"
_CssSwitchPortSpeedAdmin_Object = MibTableColumn
cssSwitchPortSpeedAdmin = _CssSwitchPortSpeedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 9),
    _CssSwitchPortSpeedAdmin_Type()
)
cssSwitchPortSpeedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssSwitchPortSpeedAdmin.setStatus("current")


class _CssSwitchPortSpeedStatus_Type(Integer32):
    """Custom type cssSwitchPortSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredMbps", 2),
          ("tenMbps", 1))
    )


_CssSwitchPortSpeedStatus_Type.__name__ = "Integer32"
_CssSwitchPortSpeedStatus_Object = MibTableColumn
cssSwitchPortSpeedStatus = _CssSwitchPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 10),
    _CssSwitchPortSpeedStatus_Type()
)
cssSwitchPortSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortSpeedStatus.setStatus("current")


class _CssSwitchPortLinkStatus_Type(Integer32):
    """Custom type cssSwitchPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("noLink", 2))
    )


_CssSwitchPortLinkStatus_Type.__name__ = "Integer32"
_CssSwitchPortLinkStatus_Object = MibTableColumn
cssSwitchPortLinkStatus = _CssSwitchPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 11),
    _CssSwitchPortLinkStatus_Type()
)
cssSwitchPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSwitchPortLinkStatus.setStatus("current")
_CiscoSibuStackableDualSpeedHubNotifications_ObjectIdentity = ObjectIdentity
ciscoSibuStackableDualSpeedHubNotifications = _CiscoSibuStackableDualSpeedHubNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 2)
)
_CiscoSibuStackableDualSpeedHubNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoSibuStackableDualSpeedHubNotificationsPrefix = _CiscoSibuStackableDualSpeedHubNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 2, 0)
)
_CiscoSibuStackableDualSpeedHubMIBComformance_ObjectIdentity = ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBComformance = _CiscoSibuStackableDualSpeedHubMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3)
)
_CiscoSibuStackableDualSpeedHubMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBCompliances = _CiscoSibuStackableDualSpeedHubMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 1)
)
_CiscoSibuStackableDualSpeedHubMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBGroups = _CiscoSibuStackableDualSpeedHubMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2)
)

# Managed Objects groups

ciscoSibuStackableDualSpeedHubGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2, 1)
)
ciscoSibuStackableDualSpeedHubGroup.setObjects(
      *(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSystemLinkTraps"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupID"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupType"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupSerialNo"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupBoardRevision"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentBootVersion"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentFirmwareVersion"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentStatus"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentPhysAddress"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupInternalPowerState"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupRedundantPowerState"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupReset"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupConfigDefaultReset"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupIsolatedState"))
)
if mibBuilder.loadTexts:
    ciscoSibuStackableDualSpeedHubGroup.setStatus("current")

ciscoSibuStackableDualSpeedHubRepeaterPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2, 2)
)
ciscoSibuStackableDualSpeedHubRepeaterPortGroup.setObjects(
      *(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortName"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortControllerRevision"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortSpeedAdmin"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortSpeedStatus"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortLinkStatus"))
)
if mibBuilder.loadTexts:
    ciscoSibuStackableDualSpeedHubRepeaterPortGroup.setStatus("current")

ciscoSibuStackableDualSpeedHubSwitchPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2, 3)
)
ciscoSibuStackableDualSpeedHubSwitchPortGroup.setObjects(
      *(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortModuleID"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortPortID"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortName"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortType"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortControllerRevision"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortState"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortDuplexAdmin"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortDuplexStatus"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortSpeedAdmin"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortSpeedStatus"),
        ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortLinkStatus"))
)
if mibBuilder.loadTexts:
    ciscoSibuStackableDualSpeedHubSwitchPortGroup.setStatus("current")


# Notification objects

ciscoSibuStackableDualSpeedHubRptrPortLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 2, 0, 1)
)
ciscoSibuStackableDualSpeedHubRptrPortLinkChange.setObjects(
    ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortLinkStatus")
)
if mibBuilder.loadTexts:
    ciscoSibuStackableDualSpeedHubRptrPortLinkChange.setStatus(
        "current"
    )

ciscoSibuStackableDualSpeedHubSwitchPortLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 2, 0, 2)
)
ciscoSibuStackableDualSpeedHubSwitchPortLinkChange.setObjects(
    ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortLinkStatus")
)
if mibBuilder.loadTexts:
    ciscoSibuStackableDualSpeedHubSwitchPortLinkChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSibuStackableDualSpeedHubCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSibuStackableDualSpeedHubCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB",
    **{"HubNumber": HubNumber,
       "ciscoSibuStackableDualSpeedHubMIB": ciscoSibuStackableDualSpeedHubMIB,
       "ciscoSibuStackableDualSpeedHubMIBObjects": ciscoSibuStackableDualSpeedHubMIBObjects,
       "cssSystem": cssSystem,
       "cssSystemLinkTraps": cssSystemLinkTraps,
       "cssGroup": cssGroup,
       "cssGroupTable": cssGroupTable,
       "cssGroupEntry": cssGroupEntry,
       "cssGroupID": cssGroupID,
       "cssGroupType": cssGroupType,
       "cssGroupSerialNo": cssGroupSerialNo,
       "cssGroupBoardRevision": cssGroupBoardRevision,
       "cssGroupAgentBootVersion": cssGroupAgentBootVersion,
       "cssGroupAgentFirmwareVersion": cssGroupAgentFirmwareVersion,
       "cssGroupAgentStatus": cssGroupAgentStatus,
       "cssGroupAgentPhysAddress": cssGroupAgentPhysAddress,
       "cssGroupInternalPowerState": cssGroupInternalPowerState,
       "cssGroupRedundantPowerState": cssGroupRedundantPowerState,
       "cssGroupReset": cssGroupReset,
       "cssGroupConfigDefaultReset": cssGroupConfigDefaultReset,
       "cssGroupIsolatedState": cssGroupIsolatedState,
       "cssRepeaterPort": cssRepeaterPort,
       "cssRepeaterPortTable": cssRepeaterPortTable,
       "cssRepeaterPortEntry": cssRepeaterPortEntry,
       "cssRepeaterPortName": cssRepeaterPortName,
       "cssRepeaterPortControllerRevision": cssRepeaterPortControllerRevision,
       "cssRepeaterPortSpeedAdmin": cssRepeaterPortSpeedAdmin,
       "cssRepeaterPortSpeedStatus": cssRepeaterPortSpeedStatus,
       "cssRepeaterPortLinkStatus": cssRepeaterPortLinkStatus,
       "cssSwitchPort": cssSwitchPort,
       "cssSwitchPortTable": cssSwitchPortTable,
       "cssSwitchPortEntry": cssSwitchPortEntry,
       "cssSwitchPortModuleID": cssSwitchPortModuleID,
       "cssSwitchPortPortID": cssSwitchPortPortID,
       "cssSwitchPortName": cssSwitchPortName,
       "cssSwitchPortType": cssSwitchPortType,
       "cssSwitchPortControllerRevision": cssSwitchPortControllerRevision,
       "cssSwitchPortState": cssSwitchPortState,
       "cssSwitchPortDuplexAdmin": cssSwitchPortDuplexAdmin,
       "cssSwitchPortDuplexStatus": cssSwitchPortDuplexStatus,
       "cssSwitchPortSpeedAdmin": cssSwitchPortSpeedAdmin,
       "cssSwitchPortSpeedStatus": cssSwitchPortSpeedStatus,
       "cssSwitchPortLinkStatus": cssSwitchPortLinkStatus,
       "ciscoSibuStackableDualSpeedHubNotifications": ciscoSibuStackableDualSpeedHubNotifications,
       "ciscoSibuStackableDualSpeedHubNotificationsPrefix": ciscoSibuStackableDualSpeedHubNotificationsPrefix,
       "ciscoSibuStackableDualSpeedHubRptrPortLinkChange": ciscoSibuStackableDualSpeedHubRptrPortLinkChange,
       "ciscoSibuStackableDualSpeedHubSwitchPortLinkChange": ciscoSibuStackableDualSpeedHubSwitchPortLinkChange,
       "ciscoSibuStackableDualSpeedHubMIBComformance": ciscoSibuStackableDualSpeedHubMIBComformance,
       "ciscoSibuStackableDualSpeedHubMIBCompliances": ciscoSibuStackableDualSpeedHubMIBCompliances,
       "ciscoSibuStackableDualSpeedHubCompliance": ciscoSibuStackableDualSpeedHubCompliance,
       "ciscoSibuStackableDualSpeedHubMIBGroups": ciscoSibuStackableDualSpeedHubMIBGroups,
       "ciscoSibuStackableDualSpeedHubGroup": ciscoSibuStackableDualSpeedHubGroup,
       "ciscoSibuStackableDualSpeedHubRepeaterPortGroup": ciscoSibuStackableDualSpeedHubRepeaterPortGroup,
       "ciscoSibuStackableDualSpeedHubSwitchPortGroup": ciscoSibuStackableDualSpeedHubSwitchPortGroup}
)
