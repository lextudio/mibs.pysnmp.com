# SNMP MIB module (CISCO-VSIMASTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VSIMASTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:41 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVsiMasterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 162)
)
ciscoVsiMasterMIB.setRevisions(
        ("2000-10-17 00:00",
         "2000-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VsiControllerIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VsiSessionIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VsiLogicalIfIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VsiXCIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVsiMasterObjects_ObjectIdentity = ObjectIdentity
ciscoVsiMasterObjects = _CiscoVsiMasterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1)
)
_VsiMasterControllerTable_Object = MibTable
vsiMasterControllerTable = _VsiMasterControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1)
)
if mibBuilder.loadTexts:
    vsiMasterControllerTable.setStatus("current")
_VsiMasterControllerEntry_Object = MibTableRow
vsiMasterControllerEntry = _VsiMasterControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1)
)
vsiMasterControllerEntry.setIndexNames(
    (0, "CISCO-VSIMASTER-MIB", "vsiControllerIndex"),
)
if mibBuilder.loadTexts:
    vsiMasterControllerEntry.setStatus("current")
_VsiControllerIndex_Type = VsiControllerIndex
_VsiControllerIndex_Object = MibTableColumn
vsiControllerIndex = _VsiControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 1),
    _VsiControllerIndex_Type()
)
vsiControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiControllerIndex.setStatus("current")


class _VsiControllerId_Type(Integer32):
    """Custom type vsiControllerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VsiControllerId_Type.__name__ = "Integer32"
_VsiControllerId_Object = MibTableColumn
vsiControllerId = _VsiControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 2),
    _VsiControllerId_Type()
)
vsiControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiControllerId.setStatus("current")


class _VsiCrossConnects_Type(Integer32):
    """Custom type vsiCrossConnects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsiCrossConnects_Type.__name__ = "Integer32"
_VsiCrossConnects_Object = MibTableColumn
vsiCrossConnects = _VsiCrossConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 3),
    _VsiCrossConnects_Type()
)
vsiCrossConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiCrossConnects.setStatus("current")


class _VsiControllerType_Type(Integer32):
    """Custom type vsiControllerType based on Integer32"""
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
        *(("mpls", 2),
          ("other", 1),
          ("par", 4),
          ("pnni", 3))
    )


_VsiControllerType_Type.__name__ = "Integer32"
_VsiControllerType_Object = MibTableColumn
vsiControllerType = _VsiControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 4),
    _VsiControllerType_Type()
)
vsiControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiControllerType.setStatus("current")


class _VsiBaseVersionSupported_Type(Integer32):
    """Custom type vsiBaseVersionSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VsiBaseVersionSupported_Type.__name__ = "Integer32"
_VsiBaseVersionSupported_Object = MibTableColumn
vsiBaseVersionSupported = _VsiBaseVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 5),
    _VsiBaseVersionSupported_Type()
)
vsiBaseVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiBaseVersionSupported.setStatus("current")


class _VsiTopVersionSupported_Type(Integer32):
    """Custom type vsiTopVersionSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VsiTopVersionSupported_Type.__name__ = "Integer32"
_VsiTopVersionSupported_Object = MibTableColumn
vsiTopVersionSupported = _VsiTopVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 6),
    _VsiTopVersionSupported_Type()
)
vsiTopVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiTopVersionSupported.setStatus("current")


class _VsiVersionInUse_Type(Integer32):
    """Custom type vsiVersionInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VsiVersionInUse_Type.__name__ = "Integer32"
_VsiVersionInUse_Object = MibTableColumn
vsiVersionInUse = _VsiVersionInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 7),
    _VsiVersionInUse_Type()
)
vsiVersionInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiVersionInUse.setStatus("current")


class _VsiSpecifiedVersion_Type(Integer32):
    """Custom type vsiSpecifiedVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VsiSpecifiedVersion_Type.__name__ = "Integer32"
_VsiSpecifiedVersion_Object = MibTableColumn
vsiSpecifiedVersion = _VsiSpecifiedVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 8),
    _VsiSpecifiedVersion_Type()
)
vsiSpecifiedVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiSpecifiedVersion.setStatus("current")
_VsiControlInterface_Type = InterfaceIndex
_VsiControlInterface_Object = MibTableColumn
vsiControlInterface = _VsiControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 9),
    _VsiControlInterface_Type()
)
vsiControlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiControlInterface.setStatus("current")
_VsiLogicalControlInterface_Type = VsiLogicalIfIndex
_VsiLogicalControlInterface_Object = MibTableColumn
vsiLogicalControlInterface = _VsiLogicalControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 10),
    _VsiLogicalControlInterface_Type()
)
vsiLogicalControlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalControlInterface.setStatus("current")
_VsiControlIfIpAddress_Type = IpAddress
_VsiControlIfIpAddress_Object = MibTableColumn
vsiControlIfIpAddress = _VsiControlIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 11),
    _VsiControlIfIpAddress_Type()
)
vsiControlIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiControlIfIpAddress.setStatus("current")


class _VsiAvailableChnlWarnThreshold_Type(Integer32):
    """Custom type vsiAvailableChnlWarnThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsiAvailableChnlWarnThreshold_Type.__name__ = "Integer32"
_VsiAvailableChnlWarnThreshold_Object = MibTableColumn
vsiAvailableChnlWarnThreshold = _VsiAvailableChnlWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 12),
    _VsiAvailableChnlWarnThreshold_Type()
)
vsiAvailableChnlWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiAvailableChnlWarnThreshold.setStatus("current")


class _VsiAvailableChnlAlarmThreshold_Type(Integer32):
    """Custom type vsiAvailableChnlAlarmThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsiAvailableChnlAlarmThreshold_Type.__name__ = "Integer32"
_VsiAvailableChnlAlarmThreshold_Object = MibTableColumn
vsiAvailableChnlAlarmThreshold = _VsiAvailableChnlAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 13),
    _VsiAvailableChnlAlarmThreshold_Type()
)
vsiAvailableChnlAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiAvailableChnlAlarmThreshold.setStatus("current")


class _VsiAvailableChnlThresholdStatus_Type(Integer32):
    """Custom type vsiAvailableChnlThresholdStatus based on Integer32"""
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
        *(("alarm", 2),
          ("normal", 4),
          ("recovery", 3),
          ("warning", 1))
    )


_VsiAvailableChnlThresholdStatus_Type.__name__ = "Integer32"
_VsiAvailableChnlThresholdStatus_Object = MibTableColumn
vsiAvailableChnlThresholdStatus = _VsiAvailableChnlThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 14),
    _VsiAvailableChnlThresholdStatus_Type()
)
vsiAvailableChnlThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiAvailableChnlThresholdStatus.setStatus("current")
_VsiSessionTable_Object = MibTable
vsiSessionTable = _VsiSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2)
)
if mibBuilder.loadTexts:
    vsiSessionTable.setStatus("current")
_VsiSessionEntry_Object = MibTableRow
vsiSessionEntry = _VsiSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1)
)
vsiSessionEntry.setIndexNames(
    (0, "CISCO-VSIMASTER-MIB", "vsiSessionControllerIndex"),
    (0, "CISCO-VSIMASTER-MIB", "vsiSessionIndex"),
)
if mibBuilder.loadTexts:
    vsiSessionEntry.setStatus("current")
_VsiSessionControllerIndex_Type = VsiControllerIndex
_VsiSessionControllerIndex_Object = MibTableColumn
vsiSessionControllerIndex = _VsiSessionControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 1),
    _VsiSessionControllerIndex_Type()
)
vsiSessionControllerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsiSessionControllerIndex.setStatus("current")
_VsiSessionIndex_Type = VsiSessionIndex
_VsiSessionIndex_Object = MibTableColumn
vsiSessionIndex = _VsiSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 2),
    _VsiSessionIndex_Type()
)
vsiSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsiSessionIndex.setStatus("current")


class _VsiSessionVpi_Type(Integer32):
    """Custom type vsiSessionVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VsiSessionVpi_Type.__name__ = "Integer32"
_VsiSessionVpi_Object = MibTableColumn
vsiSessionVpi = _VsiSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 3),
    _VsiSessionVpi_Type()
)
vsiSessionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionVpi.setStatus("current")


class _VsiSessionVci_Type(Integer32):
    """Custom type vsiSessionVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiSessionVci_Type.__name__ = "Integer32"
_VsiSessionVci_Object = MibTableColumn
vsiSessionVci = _VsiSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 4),
    _VsiSessionVci_Type()
)
vsiSessionVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionVci.setStatus("current")


class _VsiSessionSwitchId_Type(Integer32):
    """Custom type vsiSessionSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VsiSessionSwitchId_Type.__name__ = "Integer32"
_VsiSessionSwitchId_Object = MibTableColumn
vsiSessionSwitchId = _VsiSessionSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 5),
    _VsiSessionSwitchId_Type()
)
vsiSessionSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionSwitchId.setStatus("current")
_VsiSessionSwitchName_Type = SnmpAdminString
_VsiSessionSwitchName_Object = MibTableColumn
vsiSessionSwitchName = _VsiSessionSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 6),
    _VsiSessionSwitchName_Type()
)
vsiSessionSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionSwitchName.setStatus("current")


class _VsiSessionSlaveId_Type(Integer32):
    """Custom type vsiSessionSlaveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VsiSessionSlaveId_Type.__name__ = "Integer32"
_VsiSessionSlaveId_Object = MibTableColumn
vsiSessionSlaveId = _VsiSessionSlaveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 7),
    _VsiSessionSlaveId_Type()
)
vsiSessionSlaveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionSlaveId.setStatus("current")


class _VsiSessionState_Type(Integer32):
    """Custom type vsiSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("configuring", 3),
          ("discovery", 7),
          ("established", 8),
          ("inactive", 1),
          ("resyncEnding", 6),
          ("resyncStarting", 4),
          ("resyncUnderway", 5),
          ("shutdownStarting", 9),
          ("unknown", 2))
    )


_VsiSessionState_Type.__name__ = "Integer32"
_VsiSessionState_Object = MibTableColumn
vsiSessionState = _VsiSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 8),
    _VsiSessionState_Type()
)
vsiSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionState.setStatus("current")


class _VsiSessionWindowSize_Type(Integer32):
    """Custom type vsiSessionWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiSessionWindowSize_Type.__name__ = "Integer32"
_VsiSessionWindowSize_Object = MibTableColumn
vsiSessionWindowSize = _VsiSessionWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 9),
    _VsiSessionWindowSize_Type()
)
vsiSessionWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionWindowSize.setStatus("current")


class _VsiSessionCmdsPending_Type(Gauge32):
    """Custom type vsiSessionCmdsPending based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiSessionCmdsPending_Type.__name__ = "Gauge32"
_VsiSessionCmdsPending_Object = MibTableColumn
vsiSessionCmdsPending = _VsiSessionCmdsPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 10),
    _VsiSessionCmdsPending_Type()
)
vsiSessionCmdsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionCmdsPending.setStatus("current")


class _VsiSessionActiveId_Type(Integer32):
    """Custom type vsiSessionActiveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsiSessionActiveId_Type.__name__ = "Integer32"
_VsiSessionActiveId_Object = MibTableColumn
vsiSessionActiveId = _VsiSessionActiveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 11),
    _VsiSessionActiveId_Type()
)
vsiSessionActiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionActiveId.setStatus("current")


class _VsiSessionPowerupId_Type(Integer32):
    """Custom type vsiSessionPowerupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsiSessionPowerupId_Type.__name__ = "Integer32"
_VsiSessionPowerupId_Object = MibTableColumn
vsiSessionPowerupId = _VsiSessionPowerupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 12),
    _VsiSessionPowerupId_Type()
)
vsiSessionPowerupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiSessionPowerupId.setStatus("current")
_VsiLogicalIfTable_Object = MibTable
vsiLogicalIfTable = _VsiLogicalIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3)
)
if mibBuilder.loadTexts:
    vsiLogicalIfTable.setStatus("current")
_VsiLogicalIfEntry_Object = MibTableRow
vsiLogicalIfEntry = _VsiLogicalIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1)
)
vsiLogicalIfEntry.setIndexNames(
    (0, "CISCO-VSIMASTER-MIB", "vsiLogicalIfControllerIndex"),
    (0, "CISCO-VSIMASTER-MIB", "vsiLogicalIfIndex"),
)
if mibBuilder.loadTexts:
    vsiLogicalIfEntry.setStatus("current")
_VsiLogicalIfControllerIndex_Type = VsiControllerIndex
_VsiLogicalIfControllerIndex_Object = MibTableColumn
vsiLogicalIfControllerIndex = _VsiLogicalIfControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 1),
    _VsiLogicalIfControllerIndex_Type()
)
vsiLogicalIfControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfControllerIndex.setStatus("current")
_VsiLogicalIfIndex_Type = VsiLogicalIfIndex
_VsiLogicalIfIndex_Object = MibTableColumn
vsiLogicalIfIndex = _VsiLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 2),
    _VsiLogicalIfIndex_Type()
)
vsiLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfIndex.setStatus("current")
_VsiLogicalIfName_Type = SnmpAdminString
_VsiLogicalIfName_Object = MibTableColumn
vsiLogicalIfName = _VsiLogicalIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 3),
    _VsiLogicalIfName_Type()
)
vsiLogicalIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfName.setStatus("current")


class _VsiLogicalIfOperState_Type(Integer32):
    """Custom type vsiLogicalIfOperState based on Integer32"""
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
        *(("active", 2),
          ("failedExternal", 3),
          ("failedInternal", 4),
          ("removed", 1))
    )


_VsiLogicalIfOperState_Type.__name__ = "Integer32"
_VsiLogicalIfOperState_Object = MibTableColumn
vsiLogicalIfOperState = _VsiLogicalIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 4),
    _VsiLogicalIfOperState_Type()
)
vsiLogicalIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfOperState.setStatus("current")


class _VsiLogicalIfAdminState_Type(Integer32):
    """Custom type vsiLogicalIfAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pendingDown", 3),
          ("up", 2))
    )


_VsiLogicalIfAdminState_Type.__name__ = "Integer32"
_VsiLogicalIfAdminState_Object = MibTableColumn
vsiLogicalIfAdminState = _VsiLogicalIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 5),
    _VsiLogicalIfAdminState_Type()
)
vsiLogicalIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfAdminState.setStatus("current")
_VsiLogicalIfRxCells_Type = Counter32
_VsiLogicalIfRxCells_Object = MibTableColumn
vsiLogicalIfRxCells = _VsiLogicalIfRxCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 6),
    _VsiLogicalIfRxCells_Type()
)
vsiLogicalIfRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfRxCells.setStatus("current")
_VsiLogicalIfTxCells_Type = Counter32
_VsiLogicalIfTxCells_Object = MibTableColumn
vsiLogicalIfTxCells = _VsiLogicalIfTxCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 7),
    _VsiLogicalIfTxCells_Type()
)
vsiLogicalIfTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfTxCells.setStatus("current")
_VsiLogicalIfRxCellsDiscarded_Type = Counter32
_VsiLogicalIfRxCellsDiscarded_Object = MibTableColumn
vsiLogicalIfRxCellsDiscarded = _VsiLogicalIfRxCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 8),
    _VsiLogicalIfRxCellsDiscarded_Type()
)
vsiLogicalIfRxCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfRxCellsDiscarded.setStatus("current")
_VsiLogicalIfTxCellsDiscarded_Type = Counter32
_VsiLogicalIfTxCellsDiscarded_Object = MibTableColumn
vsiLogicalIfTxCellsDiscarded = _VsiLogicalIfTxCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 9),
    _VsiLogicalIfTxCellsDiscarded_Type()
)
vsiLogicalIfTxCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfTxCellsDiscarded.setStatus("current")
_VsiLogicalIfRxHeaderErrors_Type = Counter32
_VsiLogicalIfRxHeaderErrors_Object = MibTableColumn
vsiLogicalIfRxHeaderErrors = _VsiLogicalIfRxHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 10),
    _VsiLogicalIfRxHeaderErrors_Type()
)
vsiLogicalIfRxHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfRxHeaderErrors.setStatus("current")
_VsiLogicalIfRxInvalidAddrs_Type = Counter32
_VsiLogicalIfRxInvalidAddrs_Object = MibTableColumn
vsiLogicalIfRxInvalidAddrs = _VsiLogicalIfRxInvalidAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 11),
    _VsiLogicalIfRxInvalidAddrs_Type()
)
vsiLogicalIfRxInvalidAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfRxInvalidAddrs.setStatus("current")
_VsiLogicalIfEndPointsInUse_Type = Gauge32
_VsiLogicalIfEndPointsInUse_Object = MibTableColumn
vsiLogicalIfEndPointsInUse = _VsiLogicalIfEndPointsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 12),
    _VsiLogicalIfEndPointsInUse_Type()
)
vsiLogicalIfEndPointsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfEndPointsInUse.setStatus("current")
_VsiLogicalIfAvailIngressChnls_Type = Gauge32
_VsiLogicalIfAvailIngressChnls_Object = MibTableColumn
vsiLogicalIfAvailIngressChnls = _VsiLogicalIfAvailIngressChnls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 13),
    _VsiLogicalIfAvailIngressChnls_Type()
)
vsiLogicalIfAvailIngressChnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfAvailIngressChnls.setStatus("current")
_VsiLogicalIfAvailEgressChnls_Type = Gauge32
_VsiLogicalIfAvailEgressChnls_Object = MibTableColumn
vsiLogicalIfAvailEgressChnls = _VsiLogicalIfAvailEgressChnls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 14),
    _VsiLogicalIfAvailEgressChnls_Type()
)
vsiLogicalIfAvailEgressChnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfAvailEgressChnls.setStatus("current")
_VsiLogicalIfAvailIngressCellRate_Type = Gauge32
_VsiLogicalIfAvailIngressCellRate_Object = MibTableColumn
vsiLogicalIfAvailIngressCellRate = _VsiLogicalIfAvailIngressCellRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 15),
    _VsiLogicalIfAvailIngressCellRate_Type()
)
vsiLogicalIfAvailIngressCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfAvailIngressCellRate.setStatus("current")
_VsiLogicalIfAvailEgressCellRate_Type = Gauge32
_VsiLogicalIfAvailEgressCellRate_Object = MibTableColumn
vsiLogicalIfAvailEgressCellRate = _VsiLogicalIfAvailEgressCellRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 16),
    _VsiLogicalIfAvailEgressCellRate_Type()
)
vsiLogicalIfAvailEgressCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfAvailEgressCellRate.setStatus("current")
_VsiLogicalIfVcMergeSupported_Type = TruthValue
_VsiLogicalIfVcMergeSupported_Object = MibTableColumn
vsiLogicalIfVcMergeSupported = _VsiLogicalIfVcMergeSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 17),
    _VsiLogicalIfVcMergeSupported_Type()
)
vsiLogicalIfVcMergeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfVcMergeSupported.setStatus("current")
_VsiLogicalIfMulticastSupported_Type = TruthValue
_VsiLogicalIfMulticastSupported_Object = MibTableColumn
vsiLogicalIfMulticastSupported = _VsiLogicalIfMulticastSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 18),
    _VsiLogicalIfMulticastSupported_Type()
)
vsiLogicalIfMulticastSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMulticastSupported.setStatus("current")
_VsiLogicalIfVpiTranslated_Type = TruthValue
_VsiLogicalIfVpiTranslated_Object = MibTableColumn
vsiLogicalIfVpiTranslated = _VsiLogicalIfVpiTranslated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 19),
    _VsiLogicalIfVpiTranslated_Type()
)
vsiLogicalIfVpiTranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfVpiTranslated.setStatus("current")
_VsiLogicalIfStrictSigRange_Type = TruthValue
_VsiLogicalIfStrictSigRange_Object = MibTableColumn
vsiLogicalIfStrictSigRange = _VsiLogicalIfStrictSigRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 20),
    _VsiLogicalIfStrictSigRange_Type()
)
vsiLogicalIfStrictSigRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfStrictSigRange.setStatus("current")


class _VsiLogicalIfMaxIngressCellRate_Type(Integer32):
    """Custom type vsiLogicalIfMaxIngressCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsiLogicalIfMaxIngressCellRate_Type.__name__ = "Integer32"
_VsiLogicalIfMaxIngressCellRate_Object = MibTableColumn
vsiLogicalIfMaxIngressCellRate = _VsiLogicalIfMaxIngressCellRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 21),
    _VsiLogicalIfMaxIngressCellRate_Type()
)
vsiLogicalIfMaxIngressCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMaxIngressCellRate.setStatus("current")


class _VsiLogicalIfMaxEgressCellRate_Type(Integer32):
    """Custom type vsiLogicalIfMaxEgressCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsiLogicalIfMaxEgressCellRate_Type.__name__ = "Integer32"
_VsiLogicalIfMaxEgressCellRate_Object = MibTableColumn
vsiLogicalIfMaxEgressCellRate = _VsiLogicalIfMaxEgressCellRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 22),
    _VsiLogicalIfMaxEgressCellRate_Type()
)
vsiLogicalIfMaxEgressCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMaxEgressCellRate.setStatus("current")


class _VsiLogicalIfMinVpi_Type(Integer32):
    """Custom type vsiLogicalIfMinVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VsiLogicalIfMinVpi_Type.__name__ = "Integer32"
_VsiLogicalIfMinVpi_Object = MibTableColumn
vsiLogicalIfMinVpi = _VsiLogicalIfMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 23),
    _VsiLogicalIfMinVpi_Type()
)
vsiLogicalIfMinVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMinVpi.setStatus("current")


class _VsiLogicalIfMaxVpi_Type(Integer32):
    """Custom type vsiLogicalIfMaxVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VsiLogicalIfMaxVpi_Type.__name__ = "Integer32"
_VsiLogicalIfMaxVpi_Object = MibTableColumn
vsiLogicalIfMaxVpi = _VsiLogicalIfMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 24),
    _VsiLogicalIfMaxVpi_Type()
)
vsiLogicalIfMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMaxVpi.setStatus("current")


class _VsiLogicalIfMinVci_Type(Integer32):
    """Custom type vsiLogicalIfMinVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiLogicalIfMinVci_Type.__name__ = "Integer32"
_VsiLogicalIfMinVci_Object = MibTableColumn
vsiLogicalIfMinVci = _VsiLogicalIfMinVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 25),
    _VsiLogicalIfMinVci_Type()
)
vsiLogicalIfMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMinVci.setStatus("current")


class _VsiLogicalIfMaxVci_Type(Integer32):
    """Custom type vsiLogicalIfMaxVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiLogicalIfMaxVci_Type.__name__ = "Integer32"
_VsiLogicalIfMaxVci_Object = MibTableColumn
vsiLogicalIfMaxVci = _VsiLogicalIfMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 26),
    _VsiLogicalIfMaxVci_Type()
)
vsiLogicalIfMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfMaxVci.setStatus("current")
_VsiLogicalControlIfIndex_Type = InterfaceIndex
_VsiLogicalControlIfIndex_Object = MibTableColumn
vsiLogicalControlIfIndex = _VsiLogicalControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 27),
    _VsiLogicalControlIfIndex_Type()
)
vsiLogicalControlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalControlIfIndex.setStatus("current")
_VsiLogicalIfSessionIndex_Type = VsiSessionIndex
_VsiLogicalIfSessionIndex_Object = MibTableColumn
vsiLogicalIfSessionIndex = _VsiLogicalIfSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 28),
    _VsiLogicalIfSessionIndex_Type()
)
vsiLogicalIfSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiLogicalIfSessionIndex.setStatus("current")
_VsiXCTable_Object = MibTable
vsiXCTable = _VsiXCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4)
)
if mibBuilder.loadTexts:
    vsiXCTable.setStatus("current")
_VsiXCEntry_Object = MibTableRow
vsiXCEntry = _VsiXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1)
)
vsiXCEntry.setIndexNames(
    (0, "CISCO-VSIMASTER-MIB", "vsiXCControllerIndex"),
    (0, "CISCO-VSIMASTER-MIB", "vsiXCLogicalIfLow"),
    (0, "CISCO-VSIMASTER-MIB", "vsiXCLogicalIfHi"),
    (0, "CISCO-VSIMASTER-MIB", "vsiXCIndex"),
)
if mibBuilder.loadTexts:
    vsiXCEntry.setStatus("current")
_VsiXCControllerIndex_Type = VsiControllerIndex
_VsiXCControllerIndex_Object = MibTableColumn
vsiXCControllerIndex = _VsiXCControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 1),
    _VsiXCControllerIndex_Type()
)
vsiXCControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCControllerIndex.setStatus("current")
_VsiXCLogicalIfLow_Type = VsiLogicalIfIndex
_VsiXCLogicalIfLow_Object = MibTableColumn
vsiXCLogicalIfLow = _VsiXCLogicalIfLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 2),
    _VsiXCLogicalIfLow_Type()
)
vsiXCLogicalIfLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCLogicalIfLow.setStatus("current")
_VsiXCLogicalIfHi_Type = VsiLogicalIfIndex
_VsiXCLogicalIfHi_Object = MibTableColumn
vsiXCLogicalIfHi = _VsiXCLogicalIfHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 3),
    _VsiXCLogicalIfHi_Type()
)
vsiXCLogicalIfHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCLogicalIfHi.setStatus("current")
_VsiXCIndex_Type = VsiXCIndex
_VsiXCIndex_Object = MibTableColumn
vsiXCIndex = _VsiXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 4),
    _VsiXCIndex_Type()
)
vsiXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCIndex.setStatus("current")


class _VsiXCState_Type(Integer32):
    """Custom type vsiXCState based on Integer32"""
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
        *(("committed", 3),
          ("deleted", 1),
          ("reserved", 2),
          ("reservedFail", 4))
    )


_VsiXCState_Type.__name__ = "Integer32"
_VsiXCState_Object = MibTableColumn
vsiXCState = _VsiXCState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 5),
    _VsiXCState_Type()
)
vsiXCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCState.setStatus("current")


class _VsiXCVpiLow_Type(Integer32):
    """Custom type vsiXCVpiLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VsiXCVpiLow_Type.__name__ = "Integer32"
_VsiXCVpiLow_Object = MibTableColumn
vsiXCVpiLow = _VsiXCVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 6),
    _VsiXCVpiLow_Type()
)
vsiXCVpiLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCVpiLow.setStatus("current")


class _VsiXCVciLow_Type(Integer32):
    """Custom type vsiXCVciLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiXCVciLow_Type.__name__ = "Integer32"
_VsiXCVciLow_Object = MibTableColumn
vsiXCVciLow = _VsiXCVciLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 7),
    _VsiXCVciLow_Type()
)
vsiXCVciLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCVciLow.setStatus("current")


class _VsiXCVpiHi_Type(Integer32):
    """Custom type vsiXCVpiHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VsiXCVpiHi_Type.__name__ = "Integer32"
_VsiXCVpiHi_Object = MibTableColumn
vsiXCVpiHi = _VsiXCVpiHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 8),
    _VsiXCVpiHi_Type()
)
vsiXCVpiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCVpiHi.setStatus("current")


class _VsiXCVciHi_Type(Integer32):
    """Custom type vsiXCVciHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsiXCVciHi_Type.__name__ = "Integer32"
_VsiXCVciHi_Object = MibTableColumn
vsiXCVciHi = _VsiXCVciHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 9),
    _VsiXCVciHi_Type()
)
vsiXCVciHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiXCVciHi.setStatus("current")


class _VsiControllerTrapEnable_Type(TruthValue):
    """Custom type vsiControllerTrapEnable based on TruthValue"""


_VsiControllerTrapEnable_Object = MibScalar
vsiControllerTrapEnable = _VsiControllerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 5),
    _VsiControllerTrapEnable_Type()
)
vsiControllerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiControllerTrapEnable.setStatus("current")


class _VsiSessionTrapEnable_Type(TruthValue):
    """Custom type vsiSessionTrapEnable based on TruthValue"""


_VsiSessionTrapEnable_Object = MibScalar
vsiSessionTrapEnable = _VsiSessionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 6),
    _VsiSessionTrapEnable_Type()
)
vsiSessionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiSessionTrapEnable.setStatus("current")


class _VsiLogicalIfTrapEnable_Type(TruthValue):
    """Custom type vsiLogicalIfTrapEnable based on TruthValue"""


_VsiLogicalIfTrapEnable_Object = MibScalar
vsiLogicalIfTrapEnable = _VsiLogicalIfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 7),
    _VsiLogicalIfTrapEnable_Type()
)
vsiLogicalIfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiLogicalIfTrapEnable.setStatus("current")


class _VsiXCTrapEnable_Type(TruthValue):
    """Custom type vsiXCTrapEnable based on TruthValue"""


_VsiXCTrapEnable_Object = MibScalar
vsiXCTrapEnable = _VsiXCTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 8),
    _VsiXCTrapEnable_Type()
)
vsiXCTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiXCTrapEnable.setStatus("current")


class _VsiVSITrapEnable_Type(TruthValue):
    """Custom type vsiVSITrapEnable based on TruthValue"""


_VsiVSITrapEnable_Object = MibScalar
vsiVSITrapEnable = _VsiVSITrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 9),
    _VsiVSITrapEnable_Type()
)
vsiVSITrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiVSITrapEnable.setStatus("current")
_CiscoVsiMasterNotifications_ObjectIdentity = ObjectIdentity
ciscoVsiMasterNotifications = _CiscoVsiMasterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2)
)
_CiscoVsiMasterConformance_ObjectIdentity = ObjectIdentity
ciscoVsiMasterConformance = _CiscoVsiMasterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3)
)
_CiscoVsiMasterGroups_ObjectIdentity = ObjectIdentity
ciscoVsiMasterGroups = _CiscoVsiMasterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1)
)
_CiscoVsiMasterCompliances_ObjectIdentity = ObjectIdentity
ciscoVsiMasterCompliances = _CiscoVsiMasterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 2)
)

# Managed Objects groups

ciscoVsiMasterGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1, 1)
)
ciscoVsiMasterGeneralGroup.setObjects(
      *(("CISCO-VSIMASTER-MIB", "vsiControllerIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiControllerId"),
        ("CISCO-VSIMASTER-MIB", "vsiCrossConnects"),
        ("CISCO-VSIMASTER-MIB", "vsiControllerType"),
        ("CISCO-VSIMASTER-MIB", "vsiBaseVersionSupported"),
        ("CISCO-VSIMASTER-MIB", "vsiTopVersionSupported"),
        ("CISCO-VSIMASTER-MIB", "vsiVersionInUse"),
        ("CISCO-VSIMASTER-MIB", "vsiSpecifiedVersion"),
        ("CISCO-VSIMASTER-MIB", "vsiControlInterface"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalControlInterface"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionVpi"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionVci"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionSwitchId"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionSwitchName"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionSlaveId"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionState"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionWindowSize"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionCmdsPending"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionActiveId"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionPowerupId"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfControllerIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfName"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfOperState"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfAdminState"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfRxCells"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfTxCells"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfRxCellsDiscarded"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfTxCellsDiscarded"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfRxHeaderErrors"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfRxInvalidAddrs"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfEndPointsInUse"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfAvailIngressChnls"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfAvailEgressChnls"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfAvailIngressCellRate"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfAvailEgressCellRate"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMaxIngressCellRate"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMaxEgressCellRate"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfVcMergeSupported"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMulticastSupported"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfVpiTranslated"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfStrictSigRange"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMinVpi"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMaxVpi"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMinVci"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfMaxVci"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalControlIfIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfSessionIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiXCControllerIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiXCLogicalIfLow"),
        ("CISCO-VSIMASTER-MIB", "vsiXCLogicalIfHi"),
        ("CISCO-VSIMASTER-MIB", "vsiXCIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiXCState"),
        ("CISCO-VSIMASTER-MIB", "vsiXCVpiLow"),
        ("CISCO-VSIMASTER-MIB", "vsiXCVciLow"),
        ("CISCO-VSIMASTER-MIB", "vsiXCVpiHi"),
        ("CISCO-VSIMASTER-MIB", "vsiXCVciHi"))
)
if mibBuilder.loadTexts:
    ciscoVsiMasterGeneralGroup.setStatus("current")

ciscoVsi2MasterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1, 2)
)
ciscoVsi2MasterGroup.setObjects(
      *(("CISCO-VSIMASTER-MIB", "vsiControlIfIpAddress"),
        ("CISCO-VSIMASTER-MIB", "vsiAvailableChnlWarnThreshold"),
        ("CISCO-VSIMASTER-MIB", "vsiAvailableChnlAlarmThreshold"),
        ("CISCO-VSIMASTER-MIB", "vsiAvailableChnlThresholdStatus"))
)
if mibBuilder.loadTexts:
    ciscoVsi2MasterGroup.setStatus("current")

ciscoVsi2AlarmControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1, 3)
)
ciscoVsi2AlarmControlGroup.setObjects(
      *(("CISCO-VSIMASTER-MIB", "vsiControllerTrapEnable"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionTrapEnable"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfTrapEnable"),
        ("CISCO-VSIMASTER-MIB", "vsiXCTrapEnable"),
        ("CISCO-VSIMASTER-MIB", "vsiVSITrapEnable"))
)
if mibBuilder.loadTexts:
    ciscoVsi2AlarmControlGroup.setStatus("current")


# Notification objects

vsiControllerAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 1)
)
vsiControllerAdded.setObjects(
    ("CISCO-VSIMASTER-MIB", "vsiControllerType")
)
if mibBuilder.loadTexts:
    vsiControllerAdded.setStatus(
        "current"
    )

vsiControllerDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 2)
)
vsiControllerDeleted.setObjects(
    ("CISCO-VSIMASTER-MIB", "vsiControllerType")
)
if mibBuilder.loadTexts:
    vsiControllerDeleted.setStatus(
        "current"
    )

vsiSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 3)
)
vsiSessionUp.setObjects(
    ("CISCO-VSIMASTER-MIB", "vsiSessionState")
)
if mibBuilder.loadTexts:
    vsiSessionUp.setStatus(
        "current"
    )

vsiSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 4)
)
vsiSessionDown.setObjects(
    ("CISCO-VSIMASTER-MIB", "vsiSessionState")
)
if mibBuilder.loadTexts:
    vsiSessionDown.setStatus(
        "current"
    )

vsiLogicalIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 5)
)
vsiLogicalIfUp.setObjects(
    ("CISCO-VSIMASTER-MIB", "vsiLogicalIfOperState")
)
if mibBuilder.loadTexts:
    vsiLogicalIfUp.setStatus(
        "current"
    )

vsiLogicalIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 6)
)
vsiLogicalIfDown.setObjects(
    ("CISCO-VSIMASTER-MIB", "vsiLogicalIfOperState")
)
if mibBuilder.loadTexts:
    vsiLogicalIfDown.setStatus(
        "current"
    )

vsiXCFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 7)
)
vsiXCFailed.setObjects(
      *(("CISCO-VSIMASTER-MIB", "vsiXCControllerIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiXCLogicalIfLow"),
        ("CISCO-VSIMASTER-MIB", "vsiXCLogicalIfHi"))
)
if mibBuilder.loadTexts:
    vsiXCFailed.setStatus(
        "current"
    )

vsiLcnExhaustionNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 2, 8)
)
vsiLcnExhaustionNotice.setObjects(
      *(("CISCO-VSIMASTER-MIB", "vsiControllerIndex"),
        ("CISCO-VSIMASTER-MIB", "vsiAvailableChnlThresholdStatus"))
)
if mibBuilder.loadTexts:
    vsiLcnExhaustionNotice.setStatus(
        "current"
    )


# Notifications groups

ciscoVsi2MasterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1, 4)
)
ciscoVsi2MasterNotificationGroup.setObjects(
      *(("CISCO-VSIMASTER-MIB", "vsiControllerAdded"),
        ("CISCO-VSIMASTER-MIB", "vsiControllerDeleted"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionUp"),
        ("CISCO-VSIMASTER-MIB", "vsiSessionDown"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfUp"),
        ("CISCO-VSIMASTER-MIB", "vsiLogicalIfDown"),
        ("CISCO-VSIMASTER-MIB", "vsiXCFailed"),
        ("CISCO-VSIMASTER-MIB", "vsiLcnExhaustionNotice"))
)
if mibBuilder.loadTexts:
    ciscoVsi2MasterNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoVsiMasterModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVsiMasterModuleCompliance.setStatus(
        "deprecated"
    )

ciscoVsi2MasterModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoVsi2MasterModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VSIMASTER-MIB",
    **{"VsiControllerIndex": VsiControllerIndex,
       "VsiSessionIndex": VsiSessionIndex,
       "VsiLogicalIfIndex": VsiLogicalIfIndex,
       "VsiXCIndex": VsiXCIndex,
       "ciscoVsiMasterMIB": ciscoVsiMasterMIB,
       "ciscoVsiMasterObjects": ciscoVsiMasterObjects,
       "vsiMasterControllerTable": vsiMasterControllerTable,
       "vsiMasterControllerEntry": vsiMasterControllerEntry,
       "vsiControllerIndex": vsiControllerIndex,
       "vsiControllerId": vsiControllerId,
       "vsiCrossConnects": vsiCrossConnects,
       "vsiControllerType": vsiControllerType,
       "vsiBaseVersionSupported": vsiBaseVersionSupported,
       "vsiTopVersionSupported": vsiTopVersionSupported,
       "vsiVersionInUse": vsiVersionInUse,
       "vsiSpecifiedVersion": vsiSpecifiedVersion,
       "vsiControlInterface": vsiControlInterface,
       "vsiLogicalControlInterface": vsiLogicalControlInterface,
       "vsiControlIfIpAddress": vsiControlIfIpAddress,
       "vsiAvailableChnlWarnThreshold": vsiAvailableChnlWarnThreshold,
       "vsiAvailableChnlAlarmThreshold": vsiAvailableChnlAlarmThreshold,
       "vsiAvailableChnlThresholdStatus": vsiAvailableChnlThresholdStatus,
       "vsiSessionTable": vsiSessionTable,
       "vsiSessionEntry": vsiSessionEntry,
       "vsiSessionControllerIndex": vsiSessionControllerIndex,
       "vsiSessionIndex": vsiSessionIndex,
       "vsiSessionVpi": vsiSessionVpi,
       "vsiSessionVci": vsiSessionVci,
       "vsiSessionSwitchId": vsiSessionSwitchId,
       "vsiSessionSwitchName": vsiSessionSwitchName,
       "vsiSessionSlaveId": vsiSessionSlaveId,
       "vsiSessionState": vsiSessionState,
       "vsiSessionWindowSize": vsiSessionWindowSize,
       "vsiSessionCmdsPending": vsiSessionCmdsPending,
       "vsiSessionActiveId": vsiSessionActiveId,
       "vsiSessionPowerupId": vsiSessionPowerupId,
       "vsiLogicalIfTable": vsiLogicalIfTable,
       "vsiLogicalIfEntry": vsiLogicalIfEntry,
       "vsiLogicalIfControllerIndex": vsiLogicalIfControllerIndex,
       "vsiLogicalIfIndex": vsiLogicalIfIndex,
       "vsiLogicalIfName": vsiLogicalIfName,
       "vsiLogicalIfOperState": vsiLogicalIfOperState,
       "vsiLogicalIfAdminState": vsiLogicalIfAdminState,
       "vsiLogicalIfRxCells": vsiLogicalIfRxCells,
       "vsiLogicalIfTxCells": vsiLogicalIfTxCells,
       "vsiLogicalIfRxCellsDiscarded": vsiLogicalIfRxCellsDiscarded,
       "vsiLogicalIfTxCellsDiscarded": vsiLogicalIfTxCellsDiscarded,
       "vsiLogicalIfRxHeaderErrors": vsiLogicalIfRxHeaderErrors,
       "vsiLogicalIfRxInvalidAddrs": vsiLogicalIfRxInvalidAddrs,
       "vsiLogicalIfEndPointsInUse": vsiLogicalIfEndPointsInUse,
       "vsiLogicalIfAvailIngressChnls": vsiLogicalIfAvailIngressChnls,
       "vsiLogicalIfAvailEgressChnls": vsiLogicalIfAvailEgressChnls,
       "vsiLogicalIfAvailIngressCellRate": vsiLogicalIfAvailIngressCellRate,
       "vsiLogicalIfAvailEgressCellRate": vsiLogicalIfAvailEgressCellRate,
       "vsiLogicalIfVcMergeSupported": vsiLogicalIfVcMergeSupported,
       "vsiLogicalIfMulticastSupported": vsiLogicalIfMulticastSupported,
       "vsiLogicalIfVpiTranslated": vsiLogicalIfVpiTranslated,
       "vsiLogicalIfStrictSigRange": vsiLogicalIfStrictSigRange,
       "vsiLogicalIfMaxIngressCellRate": vsiLogicalIfMaxIngressCellRate,
       "vsiLogicalIfMaxEgressCellRate": vsiLogicalIfMaxEgressCellRate,
       "vsiLogicalIfMinVpi": vsiLogicalIfMinVpi,
       "vsiLogicalIfMaxVpi": vsiLogicalIfMaxVpi,
       "vsiLogicalIfMinVci": vsiLogicalIfMinVci,
       "vsiLogicalIfMaxVci": vsiLogicalIfMaxVci,
       "vsiLogicalControlIfIndex": vsiLogicalControlIfIndex,
       "vsiLogicalIfSessionIndex": vsiLogicalIfSessionIndex,
       "vsiXCTable": vsiXCTable,
       "vsiXCEntry": vsiXCEntry,
       "vsiXCControllerIndex": vsiXCControllerIndex,
       "vsiXCLogicalIfLow": vsiXCLogicalIfLow,
       "vsiXCLogicalIfHi": vsiXCLogicalIfHi,
       "vsiXCIndex": vsiXCIndex,
       "vsiXCState": vsiXCState,
       "vsiXCVpiLow": vsiXCVpiLow,
       "vsiXCVciLow": vsiXCVciLow,
       "vsiXCVpiHi": vsiXCVpiHi,
       "vsiXCVciHi": vsiXCVciHi,
       "vsiControllerTrapEnable": vsiControllerTrapEnable,
       "vsiSessionTrapEnable": vsiSessionTrapEnable,
       "vsiLogicalIfTrapEnable": vsiLogicalIfTrapEnable,
       "vsiXCTrapEnable": vsiXCTrapEnable,
       "vsiVSITrapEnable": vsiVSITrapEnable,
       "ciscoVsiMasterNotifications": ciscoVsiMasterNotifications,
       "vsiControllerAdded": vsiControllerAdded,
       "vsiControllerDeleted": vsiControllerDeleted,
       "vsiSessionUp": vsiSessionUp,
       "vsiSessionDown": vsiSessionDown,
       "vsiLogicalIfUp": vsiLogicalIfUp,
       "vsiLogicalIfDown": vsiLogicalIfDown,
       "vsiXCFailed": vsiXCFailed,
       "vsiLcnExhaustionNotice": vsiLcnExhaustionNotice,
       "ciscoVsiMasterConformance": ciscoVsiMasterConformance,
       "ciscoVsiMasterGroups": ciscoVsiMasterGroups,
       "ciscoVsiMasterGeneralGroup": ciscoVsiMasterGeneralGroup,
       "ciscoVsi2MasterGroup": ciscoVsi2MasterGroup,
       "ciscoVsi2AlarmControlGroup": ciscoVsi2AlarmControlGroup,
       "ciscoVsi2MasterNotificationGroup": ciscoVsi2MasterNotificationGroup,
       "ciscoVsiMasterCompliances": ciscoVsiMasterCompliances,
       "ciscoVsiMasterModuleCompliance": ciscoVsiMasterModuleCompliance,
       "ciscoVsi2MasterModuleCompliance": ciscoVsi2MasterModuleCompliance}
)
