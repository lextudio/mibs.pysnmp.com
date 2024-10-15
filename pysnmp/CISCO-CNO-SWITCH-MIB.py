# SNMP MIB module (CISCO-CNO-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CNO-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:34 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCNOSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43)
)
ciscoCNOSwitchMIB.setRevisions(
        ("1998-10-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCNOSwitchMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCNOSwitchMIBObjects = _CiscoCNOSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1)
)
_CnosSysInfo_ObjectIdentity = ObjectIdentity
cnosSysInfo = _CnosSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 1)
)


class _CnosSysInfoSerialNo_Type(DisplayString):
    """Custom type cnosSysInfoSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnosSysInfoSerialNo_Type.__name__ = "DisplayString"
_CnosSysInfoSerialNo_Object = MibScalar
cnosSysInfoSerialNo = _CnosSysInfoSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 1, 1),
    _CnosSysInfoSerialNo_Type()
)
cnosSysInfoSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosSysInfoSerialNo.setStatus("current")


class _CnosSysInfoBoardRevision_Type(Integer32):
    """Custom type cnosSysInfoBoardRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnosSysInfoBoardRevision_Type.__name__ = "Integer32"
_CnosSysInfoBoardRevision_Object = MibScalar
cnosSysInfoBoardRevision = _CnosSysInfoBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 1, 2),
    _CnosSysInfoBoardRevision_Type()
)
cnosSysInfoBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosSysInfoBoardRevision.setStatus("current")


class _CnosSysInfoBootVersion_Type(DisplayString):
    """Custom type cnosSysInfoBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CnosSysInfoBootVersion_Type.__name__ = "DisplayString"
_CnosSysInfoBootVersion_Object = MibScalar
cnosSysInfoBootVersion = _CnosSysInfoBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 1, 3),
    _CnosSysInfoBootVersion_Type()
)
cnosSysInfoBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosSysInfoBootVersion.setStatus("current")


class _CnosSysInfoAddrCapacity_Type(Integer32):
    """Custom type cnosSysInfoAddrCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnosSysInfoAddrCapacity_Type.__name__ = "Integer32"
_CnosSysInfoAddrCapacity_Object = MibScalar
cnosSysInfoAddrCapacity = _CnosSysInfoAddrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 1, 4),
    _CnosSysInfoAddrCapacity_Type()
)
cnosSysInfoAddrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosSysInfoAddrCapacity.setStatus("current")
_CnosSysConfig_ObjectIdentity = ObjectIdentity
cnosSysConfig = _CnosSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 2)
)


class _CnosSysConfigReset_Type(Integer32):
    """Custom type cnosSysConfigReset based on Integer32"""
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


_CnosSysConfigReset_Type.__name__ = "Integer32"
_CnosSysConfigReset_Object = MibScalar
cnosSysConfigReset = _CnosSysConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 2, 1),
    _CnosSysConfigReset_Type()
)
cnosSysConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosSysConfigReset.setStatus("current")


class _CnosSysConfigDefaultReset_Type(Integer32):
    """Custom type cnosSysConfigDefaultReset based on Integer32"""
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


_CnosSysConfigDefaultReset_Type.__name__ = "Integer32"
_CnosSysConfigDefaultReset_Object = MibScalar
cnosSysConfigDefaultReset = _CnosSysConfigDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 2, 2),
    _CnosSysConfigDefaultReset_Type()
)
cnosSysConfigDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosSysConfigDefaultReset.setStatus("current")


class _CnosSysConfigMonitor_Type(Integer32):
    """Custom type cnosSysConfigMonitor based on Integer32"""
    defaultValue = 2

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


_CnosSysConfigMonitor_Type.__name__ = "Integer32"
_CnosSysConfigMonitor_Object = MibScalar
cnosSysConfigMonitor = _CnosSysConfigMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 2, 3),
    _CnosSysConfigMonitor_Type()
)
cnosSysConfigMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosSysConfigMonitor.setStatus("current")


class _CnosSysConfigMonitorPort_Type(Integer32):
    """Custom type cnosSysConfigMonitorPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CnosSysConfigMonitorPort_Type.__name__ = "Integer32"
_CnosSysConfigMonitorPort_Object = MibScalar
cnosSysConfigMonitorPort = _CnosSysConfigMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 2, 4),
    _CnosSysConfigMonitorPort_Type()
)
cnosSysConfigMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosSysConfigMonitorPort.setStatus("current")
_CnosPort_ObjectIdentity = ObjectIdentity
cnosPort = _CnosPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3)
)
_CnosPortTable_Object = MibTable
cnosPortTable = _CnosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cnosPortTable.setStatus("current")
_CnosPortEntry_Object = MibTableRow
cnosPortEntry = _CnosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1)
)
cnosPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnosPortEntry.setStatus("current")


class _CnosPortControllerRevision_Type(Integer32):
    """Custom type cnosPortControllerRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnosPortControllerRevision_Type.__name__ = "Integer32"
_CnosPortControllerRevision_Object = MibTableColumn
cnosPortControllerRevision = _CnosPortControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 1),
    _CnosPortControllerRevision_Type()
)
cnosPortControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosPortControllerRevision.setStatus("current")


class _CnosPortName_Type(DisplayString):
    """Custom type cnosPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CnosPortName_Type.__name__ = "DisplayString"
_CnosPortName_Object = MibTableColumn
cnosPortName = _CnosPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 2),
    _CnosPortName_Type()
)
cnosPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosPortName.setStatus("current")


class _CnosPortDuplexAdmin_Type(Integer32):
    """Custom type cnosPortDuplexAdmin based on Integer32"""
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


_CnosPortDuplexAdmin_Type.__name__ = "Integer32"
_CnosPortDuplexAdmin_Object = MibTableColumn
cnosPortDuplexAdmin = _CnosPortDuplexAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 3),
    _CnosPortDuplexAdmin_Type()
)
cnosPortDuplexAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosPortDuplexAdmin.setStatus("current")


class _CnosPortDuplexStatus_Type(Integer32):
    """Custom type cnosPortDuplexStatus based on Integer32"""
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


_CnosPortDuplexStatus_Type.__name__ = "Integer32"
_CnosPortDuplexStatus_Object = MibTableColumn
cnosPortDuplexStatus = _CnosPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 4),
    _CnosPortDuplexStatus_Type()
)
cnosPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosPortDuplexStatus.setStatus("current")


class _CnosPortSpeedAdmin_Type(Integer32):
    """Custom type cnosPortSpeedAdmin based on Integer32"""
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


_CnosPortSpeedAdmin_Type.__name__ = "Integer32"
_CnosPortSpeedAdmin_Object = MibTableColumn
cnosPortSpeedAdmin = _CnosPortSpeedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 5),
    _CnosPortSpeedAdmin_Type()
)
cnosPortSpeedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosPortSpeedAdmin.setStatus("current")


class _CnosPortSpeedStatus_Type(Integer32):
    """Custom type cnosPortSpeedStatus based on Integer32"""
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


_CnosPortSpeedStatus_Type.__name__ = "Integer32"
_CnosPortSpeedStatus_Object = MibTableColumn
cnosPortSpeedStatus = _CnosPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 6),
    _CnosPortSpeedStatus_Type()
)
cnosPortSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosPortSpeedStatus.setStatus("current")


class _CnosPortMonitoring_Type(Integer32):
    """Custom type cnosPortMonitoring based on Integer32"""
    defaultValue = 2

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


_CnosPortMonitoring_Type.__name__ = "Integer32"
_CnosPortMonitoring_Object = MibTableColumn
cnosPortMonitoring = _CnosPortMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 7),
    _CnosPortMonitoring_Type()
)
cnosPortMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosPortMonitoring.setStatus("current")


class _CnosPortLinkStatus_Type(Integer32):
    """Custom type cnosPortLinkStatus based on Integer32"""
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


_CnosPortLinkStatus_Type.__name__ = "Integer32"
_CnosPortLinkStatus_Object = MibTableColumn
cnosPortLinkStatus = _CnosPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 8),
    _CnosPortLinkStatus_Type()
)
cnosPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnosPortLinkStatus.setStatus("current")


class _CnosPortSTPPortFastMode_Type(Integer32):
    """Custom type cnosPortSTPPortFastMode based on Integer32"""
    defaultValue = 2

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


_CnosPortSTPPortFastMode_Type.__name__ = "Integer32"
_CnosPortSTPPortFastMode_Object = MibTableColumn
cnosPortSTPPortFastMode = _CnosPortSTPPortFastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 9),
    _CnosPortSTPPortFastMode_Type()
)
cnosPortSTPPortFastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosPortSTPPortFastMode.setStatus("current")


class _CnosPortVlanMember_Type(Integer32):
    """Custom type cnosPortVlanMember based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 5),
          ("vlan1", 1),
          ("vlan2", 2),
          ("vlan3", 3),
          ("vlan4", 4))
    )


_CnosPortVlanMember_Type.__name__ = "Integer32"
_CnosPortVlanMember_Object = MibTableColumn
cnosPortVlanMember = _CnosPortVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 3, 1, 1, 10),
    _CnosPortVlanMember_Type()
)
cnosPortVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosPortVlanMember.setStatus("current")
_CnosVlan_ObjectIdentity = ObjectIdentity
cnosVlan = _CnosVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 4)
)
_CnosVlanTable_Object = MibTable
cnosVlanTable = _CnosVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cnosVlanTable.setStatus("current")
_CnosVlanEntry_Object = MibTableRow
cnosVlanEntry = _CnosVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 4, 1, 1)
)
cnosVlanEntry.setIndexNames(
    (0, "CISCO-CNO-SWITCH-MIB", "cnosVlanIndex"),
)
if mibBuilder.loadTexts:
    cnosVlanEntry.setStatus("current")


class _CnosVlanIndex_Type(Integer32):
    """Custom type cnosVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CnosVlanIndex_Type.__name__ = "Integer32"
_CnosVlanIndex_Object = MibTableColumn
cnosVlanIndex = _CnosVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 4, 1, 1, 1),
    _CnosVlanIndex_Type()
)
cnosVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnosVlanIndex.setStatus("current")


class _CnosVlanSTPState_Type(Integer32):
    """Custom type cnosVlanSTPState based on Integer32"""
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


_CnosVlanSTPState_Type.__name__ = "Integer32"
_CnosVlanSTPState_Object = MibTableColumn
cnosVlanSTPState = _CnosVlanSTPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 1, 4, 1, 1, 2),
    _CnosVlanSTPState_Type()
)
cnosVlanSTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnosVlanSTPState.setStatus("current")
_CiscoCNOSwitchNotifications_ObjectIdentity = ObjectIdentity
ciscoCNOSwitchNotifications = _CiscoCNOSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 2)
)
_CiscoCNOSwitchNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoCNOSwitchNotificationsPrefix = _CiscoCNOSwitchNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 2, 0)
)
_CiscoCNOSwitchMIBComformance_ObjectIdentity = ObjectIdentity
ciscoCNOSwitchMIBComformance = _CiscoCNOSwitchMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3)
)
_CiscoCNOSwitchMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCNOSwitchMIBCompliances = _CiscoCNOSwitchMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 1)
)
_CiscoCNOSwitchMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCNOSwitchMIBGroups = _CiscoCNOSwitchMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 2)
)

# Managed Objects groups

ciscoCNOSwitchSysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 2, 1)
)
ciscoCNOSwitchSysInfoGroup.setObjects(
      *(("CISCO-CNO-SWITCH-MIB", "cnosSysInfoSerialNo"),
        ("CISCO-CNO-SWITCH-MIB", "cnosSysInfoBoardRevision"),
        ("CISCO-CNO-SWITCH-MIB", "cnosSysInfoBootVersion"),
        ("CISCO-CNO-SWITCH-MIB", "cnosSysInfoAddrCapacity"))
)
if mibBuilder.loadTexts:
    ciscoCNOSwitchSysInfoGroup.setStatus("current")

ciscoCNOSwitchConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 2, 2)
)
ciscoCNOSwitchConfigGroup.setObjects(
      *(("CISCO-CNO-SWITCH-MIB", "cnosSysConfigReset"),
        ("CISCO-CNO-SWITCH-MIB", "cnosSysConfigDefaultReset"))
)
if mibBuilder.loadTexts:
    ciscoCNOSwitchConfigGroup.setStatus("current")

ciscoCNOSwitchPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 2, 3)
)
ciscoCNOSwitchPortGroup.setObjects(
      *(("CISCO-CNO-SWITCH-MIB", "cnosPortName"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortControllerRevision"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortDuplexAdmin"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortDuplexStatus"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortSpeedAdmin"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortSpeedStatus"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortLinkStatus"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortSTPPortFastMode"))
)
if mibBuilder.loadTexts:
    ciscoCNOSwitchPortGroup.setStatus("current")

ciscoCNOSwitchMonitorPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 2, 4)
)
ciscoCNOSwitchMonitorPortGroup.setObjects(
      *(("CISCO-CNO-SWITCH-MIB", "cnosSysConfigMonitor"),
        ("CISCO-CNO-SWITCH-MIB", "cnosSysConfigMonitorPort"),
        ("CISCO-CNO-SWITCH-MIB", "cnosPortMonitoring"))
)
if mibBuilder.loadTexts:
    ciscoCNOSwitchMonitorPortGroup.setStatus("current")

ciscoCNOSwitchVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 2, 5)
)
ciscoCNOSwitchVlanGroup.setObjects(
      *(("CISCO-CNO-SWITCH-MIB", "cnosPortVlanMember"),
        ("CISCO-CNO-SWITCH-MIB", "cnosVlanSTPState"))
)
if mibBuilder.loadTexts:
    ciscoCNOSwitchVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCNOSwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 43, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCNOSwitchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CNO-SWITCH-MIB",
    **{"ciscoCNOSwitchMIB": ciscoCNOSwitchMIB,
       "ciscoCNOSwitchMIBObjects": ciscoCNOSwitchMIBObjects,
       "cnosSysInfo": cnosSysInfo,
       "cnosSysInfoSerialNo": cnosSysInfoSerialNo,
       "cnosSysInfoBoardRevision": cnosSysInfoBoardRevision,
       "cnosSysInfoBootVersion": cnosSysInfoBootVersion,
       "cnosSysInfoAddrCapacity": cnosSysInfoAddrCapacity,
       "cnosSysConfig": cnosSysConfig,
       "cnosSysConfigReset": cnosSysConfigReset,
       "cnosSysConfigDefaultReset": cnosSysConfigDefaultReset,
       "cnosSysConfigMonitor": cnosSysConfigMonitor,
       "cnosSysConfigMonitorPort": cnosSysConfigMonitorPort,
       "cnosPort": cnosPort,
       "cnosPortTable": cnosPortTable,
       "cnosPortEntry": cnosPortEntry,
       "cnosPortControllerRevision": cnosPortControllerRevision,
       "cnosPortName": cnosPortName,
       "cnosPortDuplexAdmin": cnosPortDuplexAdmin,
       "cnosPortDuplexStatus": cnosPortDuplexStatus,
       "cnosPortSpeedAdmin": cnosPortSpeedAdmin,
       "cnosPortSpeedStatus": cnosPortSpeedStatus,
       "cnosPortMonitoring": cnosPortMonitoring,
       "cnosPortLinkStatus": cnosPortLinkStatus,
       "cnosPortSTPPortFastMode": cnosPortSTPPortFastMode,
       "cnosPortVlanMember": cnosPortVlanMember,
       "cnosVlan": cnosVlan,
       "cnosVlanTable": cnosVlanTable,
       "cnosVlanEntry": cnosVlanEntry,
       "cnosVlanIndex": cnosVlanIndex,
       "cnosVlanSTPState": cnosVlanSTPState,
       "ciscoCNOSwitchNotifications": ciscoCNOSwitchNotifications,
       "ciscoCNOSwitchNotificationsPrefix": ciscoCNOSwitchNotificationsPrefix,
       "ciscoCNOSwitchMIBComformance": ciscoCNOSwitchMIBComformance,
       "ciscoCNOSwitchMIBCompliances": ciscoCNOSwitchMIBCompliances,
       "ciscoCNOSwitchCompliance": ciscoCNOSwitchCompliance,
       "ciscoCNOSwitchMIBGroups": ciscoCNOSwitchMIBGroups,
       "ciscoCNOSwitchSysInfoGroup": ciscoCNOSwitchSysInfoGroup,
       "ciscoCNOSwitchConfigGroup": ciscoCNOSwitchConfigGroup,
       "ciscoCNOSwitchPortGroup": ciscoCNOSwitchPortGroup,
       "ciscoCNOSwitchMonitorPortGroup": ciscoCNOSwitchMonitorPortGroup,
       "ciscoCNOSwitchVlanGroup": ciscoCNOSwitchVlanGroup}
)
