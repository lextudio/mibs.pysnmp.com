# SNMP MIB module (CISCO-OSCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OSCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:27 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoOscpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202)
)
ciscoOscpMIB.setRevisions(
        ("2001-05-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoscpSwitchId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class CoscpPortId(Unsigned32, TextualConvention):
    status = "current"


class CoscpBundleId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CoscpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("version1", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOscpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOscpMIBObjects = _CiscoOscpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1)
)
_CiscoOscpBaseGroup_ObjectIdentity = ObjectIdentity
ciscoOscpBaseGroup = _CiscoOscpBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1)
)
_CoscpHighestVersion_Type = CoscpVersion
_CoscpHighestVersion_Object = MibScalar
coscpHighestVersion = _CoscpHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 1),
    _CoscpHighestVersion_Type()
)
coscpHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpHighestVersion.setStatus("current")
_CoscpLowestVersion_Type = CoscpVersion
_CoscpLowestVersion_Object = MibScalar
coscpLowestVersion = _CoscpLowestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 2),
    _CoscpLowestVersion_Type()
)
coscpLowestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLowestVersion.setStatus("current")
_CoscpSwitchId_Type = CoscpSwitchId
_CoscpSwitchId_Object = MibScalar
coscpSwitchId = _CoscpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 3),
    _CoscpSwitchId_Type()
)
coscpSwitchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpSwitchId.setStatus("current")


class _CoscpPriorityChangeMode_Type(Integer32):
    """Custom type coscpPriorityChangeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delayed", 2),
          ("immediate", 1))
    )


_CoscpPriorityChangeMode_Type.__name__ = "Integer32"
_CoscpPriorityChangeMode_Object = MibScalar
coscpPriorityChangeMode = _CoscpPriorityChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 4),
    _CoscpPriorityChangeMode_Type()
)
coscpPriorityChangeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpPriorityChangeMode.setStatus("current")


class _CoscpHelloHoldDown_Type(Unsigned32):
    """Custom type coscpHelloHoldDown based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CoscpHelloHoldDown_Type.__name__ = "Unsigned32"
_CoscpHelloHoldDown_Object = MibScalar
coscpHelloHoldDown = _CoscpHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 5),
    _CoscpHelloHoldDown_Type()
)
coscpHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpHelloHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    coscpHelloHoldDown.setUnits("milliseconds")


class _CoscpHelloInterval_Type(Unsigned32):
    """Custom type coscpHelloInterval based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 30000),
    )


_CoscpHelloInterval_Type.__name__ = "Unsigned32"
_CoscpHelloInterval_Object = MibScalar
coscpHelloInterval = _CoscpHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 6),
    _CoscpHelloInterval_Type()
)
coscpHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    coscpHelloInterval.setUnits("milliseconds")


class _CoscpHelloInactivityFactor_Type(Unsigned32):
    """Custom type coscpHelloInactivityFactor based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_CoscpHelloInactivityFactor_Type.__name__ = "Unsigned32"
_CoscpHelloInactivityFactor_Object = MibScalar
coscpHelloInactivityFactor = _CoscpHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 7),
    _CoscpHelloInactivityFactor_Type()
)
coscpHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpHelloInactivityFactor.setStatus("current")


class _CoscpNotifiesEnabled_Type(TruthValue):
    """Custom type coscpNotifiesEnabled based on TruthValue"""


_CoscpNotifiesEnabled_Object = MibScalar
coscpNotifiesEnabled = _CoscpNotifiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 8),
    _CoscpNotifiesEnabled_Type()
)
coscpNotifiesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpNotifiesEnabled.setStatus("current")
_CoscpLinkTable_Object = MibTable
coscpLinkTable = _CoscpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2)
)
if mibBuilder.loadTexts:
    coscpLinkTable.setStatus("current")
_CoscpLinkEntry_Object = MibTableRow
coscpLinkEntry = _CoscpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1)
)
coscpLinkEntry.setIndexNames(
    (0, "CISCO-OSCP-MIB", "coscpLinkPortId"),
)
if mibBuilder.loadTexts:
    coscpLinkEntry.setStatus("current")
_CoscpLinkPortId_Type = CoscpPortId
_CoscpLinkPortId_Object = MibTableColumn
coscpLinkPortId = _CoscpLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 1),
    _CoscpLinkPortId_Type()
)
coscpLinkPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coscpLinkPortId.setStatus("current")


class _CoscpLinkType_Type(Integer32):
    """Custom type coscpLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedWavelength", 2),
          ("inBand", 3),
          ("unknown", 1))
    )


_CoscpLinkType_Type.__name__ = "Integer32"
_CoscpLinkType_Object = MibTableColumn
coscpLinkType = _CoscpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 2),
    _CoscpLinkType_Type()
)
coscpLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkType.setStatus("current")
_CoscpLinkVersion_Type = CoscpVersion
_CoscpLinkVersion_Object = MibTableColumn
coscpLinkVersion = _CoscpLinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 3),
    _CoscpLinkVersion_Type()
)
coscpLinkVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkVersion.setStatus("current")


class _CoscpLinkHelloState_Type(Integer32):
    """Custom type coscpLinkHelloState based on Integer32"""
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
        *(("attempt", 2),
          ("down", 1),
          ("oneWay", 3),
          ("twoWay", 4))
    )


_CoscpLinkHelloState_Type.__name__ = "Integer32"
_CoscpLinkHelloState_Object = MibTableColumn
coscpLinkHelloState = _CoscpLinkHelloState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 4),
    _CoscpLinkHelloState_Type()
)
coscpLinkHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkHelloState.setStatus("current")
_CoscpLinkRemoteSwitchId_Type = CoscpSwitchId
_CoscpLinkRemoteSwitchId_Object = MibTableColumn
coscpLinkRemoteSwitchId = _CoscpLinkRemoteSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 5),
    _CoscpLinkRemoteSwitchId_Type()
)
coscpLinkRemoteSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkRemoteSwitchId.setStatus("current")
_CoscpLinkRemotePortId_Type = CoscpPortId
_CoscpLinkRemotePortId_Object = MibTableColumn
coscpLinkRemotePortId = _CoscpLinkRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 6),
    _CoscpLinkRemotePortId_Type()
)
coscpLinkRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkRemotePortId.setStatus("current")
_CoscpLinkDerivedBundleId_Type = CoscpBundleId
_CoscpLinkDerivedBundleId_Object = MibTableColumn
coscpLinkDerivedBundleId = _CoscpLinkDerivedBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 7),
    _CoscpLinkDerivedBundleId_Type()
)
coscpLinkDerivedBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkDerivedBundleId.setStatus("current")


class _CoscpLinkConfigBundleId_Type(CoscpBundleId):
    """Custom type coscpLinkConfigBundleId based on CoscpBundleId"""
    defaultValue = 0


_CoscpLinkConfigBundleId_Object = MibTableColumn
coscpLinkConfigBundleId = _CoscpLinkConfigBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 8),
    _CoscpLinkConfigBundleId_Type()
)
coscpLinkConfigBundleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpLinkConfigBundleId.setStatus("current")
_CoscpLinkIfIndex_Type = InterfaceIndex
_CoscpLinkIfIndex_Object = MibTableColumn
coscpLinkIfIndex = _CoscpLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 9),
    _CoscpLinkIfIndex_Type()
)
coscpLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkIfIndex.setStatus("current")


class _CoscpLinkSelPriority_Type(Unsigned32):
    """Custom type coscpLinkSelPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CoscpLinkSelPriority_Type.__name__ = "Unsigned32"
_CoscpLinkSelPriority_Object = MibTableColumn
coscpLinkSelPriority = _CoscpLinkSelPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 10),
    _CoscpLinkSelPriority_Type()
)
coscpLinkSelPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coscpLinkSelPriority.setStatus("current")
_CoscpLinkInHellos_Type = Counter32
_CoscpLinkInHellos_Object = MibTableColumn
coscpLinkInHellos = _CoscpLinkInHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 11),
    _CoscpLinkInHellos_Type()
)
coscpLinkInHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkInHellos.setStatus("current")
_CoscpLinkInDiscardedHellos_Type = Counter32
_CoscpLinkInDiscardedHellos_Object = MibTableColumn
coscpLinkInDiscardedHellos = _CoscpLinkInDiscardedHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 12),
    _CoscpLinkInDiscardedHellos_Type()
)
coscpLinkInDiscardedHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkInDiscardedHellos.setStatus("current")
_CoscpLinkOutHellos_Type = Counter32
_CoscpLinkOutHellos_Object = MibTableColumn
coscpLinkOutHellos = _CoscpLinkOutHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 13),
    _CoscpLinkOutHellos_Type()
)
coscpLinkOutHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkOutHellos.setStatus("current")
_CoscpLinkTransDown_Type = Counter32
_CoscpLinkTransDown_Object = MibTableColumn
coscpLinkTransDown = _CoscpLinkTransDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 14),
    _CoscpLinkTransDown_Type()
)
coscpLinkTransDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpLinkTransDown.setStatus("current")
_CoscpBundleTable_Object = MibTable
coscpBundleTable = _CoscpBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3)
)
if mibBuilder.loadTexts:
    coscpBundleTable.setStatus("current")
_CoscpBundleEntry_Object = MibTableRow
coscpBundleEntry = _CoscpBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1)
)
coscpBundleEntry.setIndexNames(
    (0, "CISCO-OSCP-MIB", "coscpBundleRemoteSwitchId"),
    (0, "CISCO-OSCP-MIB", "coscpBundleId"),
)
if mibBuilder.loadTexts:
    coscpBundleEntry.setStatus("current")
_CoscpBundleRemoteSwitchId_Type = CoscpSwitchId
_CoscpBundleRemoteSwitchId_Object = MibTableColumn
coscpBundleRemoteSwitchId = _CoscpBundleRemoteSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 1),
    _CoscpBundleRemoteSwitchId_Type()
)
coscpBundleRemoteSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coscpBundleRemoteSwitchId.setStatus("current")
_CoscpBundleId_Type = CoscpBundleId
_CoscpBundleId_Object = MibTableColumn
coscpBundleId = _CoscpBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 2),
    _CoscpBundleId_Type()
)
coscpBundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coscpBundleId.setStatus("current")
_CoscpBundleActivePortId_Type = CoscpPortId
_CoscpBundleActivePortId_Object = MibTableColumn
coscpBundleActivePortId = _CoscpBundleActivePortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 3),
    _CoscpBundleActivePortId_Type()
)
coscpBundleActivePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpBundleActivePortId.setStatus("current")
_CoscpBundleIfIndex_Type = InterfaceIndex
_CoscpBundleIfIndex_Object = MibTableColumn
coscpBundleIfIndex = _CoscpBundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 4),
    _CoscpBundleIfIndex_Type()
)
coscpBundleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpBundleIfIndex.setStatus("current")
_CoscpBundlePortCount_Type = Gauge32
_CoscpBundlePortCount_Object = MibTableColumn
coscpBundlePortCount = _CoscpBundlePortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 5),
    _CoscpBundlePortCount_Type()
)
coscpBundlePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coscpBundlePortCount.setStatus("current")
_CoscpBundleRowStatus_Type = RowStatus
_CoscpBundleRowStatus_Object = MibTableColumn
coscpBundleRowStatus = _CoscpBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 6),
    _CoscpBundleRowStatus_Type()
)
coscpBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coscpBundleRowStatus.setStatus("current")
_CiscoOscpMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoOscpMIBNotifications = _CiscoOscpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 2)
)
_CiscoOscpNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoOscpNotificationsPrefix = _CiscoOscpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0)
)
_CiscoOscpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOscpMIBConformance = _CiscoOscpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3)
)
_CiscoOscpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOscpMIBCompliances = _CiscoOscpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1)
)
_CiscoOscpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOscpMIBGroups = _CiscoOscpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2)
)

# Managed Objects groups

ciscoOscpBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 1)
)
ciscoOscpBasicGroup.setObjects(
      *(("CISCO-OSCP-MIB", "coscpHighestVersion"),
        ("CISCO-OSCP-MIB", "coscpLowestVersion"),
        ("CISCO-OSCP-MIB", "coscpSwitchId"),
        ("CISCO-OSCP-MIB", "coscpHelloHoldDown"),
        ("CISCO-OSCP-MIB", "coscpHelloInterval"),
        ("CISCO-OSCP-MIB", "coscpHelloInactivityFactor"),
        ("CISCO-OSCP-MIB", "coscpNotifiesEnabled"),
        ("CISCO-OSCP-MIB", "coscpLinkType"),
        ("CISCO-OSCP-MIB", "coscpLinkVersion"),
        ("CISCO-OSCP-MIB", "coscpLinkHelloState"),
        ("CISCO-OSCP-MIB", "coscpLinkRemoteSwitchId"),
        ("CISCO-OSCP-MIB", "coscpLinkRemotePortId"),
        ("CISCO-OSCP-MIB", "coscpLinkIfIndex"),
        ("CISCO-OSCP-MIB", "coscpLinkInHellos"),
        ("CISCO-OSCP-MIB", "coscpLinkInDiscardedHellos"),
        ("CISCO-OSCP-MIB", "coscpLinkOutHellos"),
        ("CISCO-OSCP-MIB", "coscpLinkTransDown"))
)
if mibBuilder.loadTexts:
    ciscoOscpBasicGroup.setStatus("current")

ciscoOscpBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 2)
)
ciscoOscpBundleGroup.setObjects(
      *(("CISCO-OSCP-MIB", "coscpPriorityChangeMode"),
        ("CISCO-OSCP-MIB", "coscpLinkDerivedBundleId"),
        ("CISCO-OSCP-MIB", "coscpLinkConfigBundleId"),
        ("CISCO-OSCP-MIB", "coscpLinkSelPriority"),
        ("CISCO-OSCP-MIB", "coscpBundleActivePortId"),
        ("CISCO-OSCP-MIB", "coscpBundleIfIndex"),
        ("CISCO-OSCP-MIB", "coscpBundlePortCount"),
        ("CISCO-OSCP-MIB", "coscpBundleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoOscpBundleGroup.setStatus("current")


# Notification objects

coscpNotifyTransDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0, 1)
)
coscpNotifyTransDown.setObjects(
    ("CISCO-OSCP-MIB", "coscpLinkTransDown")
)
if mibBuilder.loadTexts:
    coscpNotifyTransDown.setStatus(
        "current"
    )


# Notifications groups

ciscoOscpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 3)
)
ciscoOscpNotificationsGroup.setObjects(
    ("CISCO-OSCP-MIB", "coscpNotifyTransDown")
)
if mibBuilder.loadTexts:
    ciscoOscpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOscpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOscpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OSCP-MIB",
    **{"CoscpSwitchId": CoscpSwitchId,
       "CoscpPortId": CoscpPortId,
       "CoscpBundleId": CoscpBundleId,
       "CoscpVersion": CoscpVersion,
       "ciscoOscpMIB": ciscoOscpMIB,
       "ciscoOscpMIBObjects": ciscoOscpMIBObjects,
       "ciscoOscpBaseGroup": ciscoOscpBaseGroup,
       "coscpHighestVersion": coscpHighestVersion,
       "coscpLowestVersion": coscpLowestVersion,
       "coscpSwitchId": coscpSwitchId,
       "coscpPriorityChangeMode": coscpPriorityChangeMode,
       "coscpHelloHoldDown": coscpHelloHoldDown,
       "coscpHelloInterval": coscpHelloInterval,
       "coscpHelloInactivityFactor": coscpHelloInactivityFactor,
       "coscpNotifiesEnabled": coscpNotifiesEnabled,
       "coscpLinkTable": coscpLinkTable,
       "coscpLinkEntry": coscpLinkEntry,
       "coscpLinkPortId": coscpLinkPortId,
       "coscpLinkType": coscpLinkType,
       "coscpLinkVersion": coscpLinkVersion,
       "coscpLinkHelloState": coscpLinkHelloState,
       "coscpLinkRemoteSwitchId": coscpLinkRemoteSwitchId,
       "coscpLinkRemotePortId": coscpLinkRemotePortId,
       "coscpLinkDerivedBundleId": coscpLinkDerivedBundleId,
       "coscpLinkConfigBundleId": coscpLinkConfigBundleId,
       "coscpLinkIfIndex": coscpLinkIfIndex,
       "coscpLinkSelPriority": coscpLinkSelPriority,
       "coscpLinkInHellos": coscpLinkInHellos,
       "coscpLinkInDiscardedHellos": coscpLinkInDiscardedHellos,
       "coscpLinkOutHellos": coscpLinkOutHellos,
       "coscpLinkTransDown": coscpLinkTransDown,
       "coscpBundleTable": coscpBundleTable,
       "coscpBundleEntry": coscpBundleEntry,
       "coscpBundleRemoteSwitchId": coscpBundleRemoteSwitchId,
       "coscpBundleId": coscpBundleId,
       "coscpBundleActivePortId": coscpBundleActivePortId,
       "coscpBundleIfIndex": coscpBundleIfIndex,
       "coscpBundlePortCount": coscpBundlePortCount,
       "coscpBundleRowStatus": coscpBundleRowStatus,
       "ciscoOscpMIBNotifications": ciscoOscpMIBNotifications,
       "ciscoOscpNotificationsPrefix": ciscoOscpNotificationsPrefix,
       "coscpNotifyTransDown": coscpNotifyTransDown,
       "ciscoOscpMIBConformance": ciscoOscpMIBConformance,
       "ciscoOscpMIBCompliances": ciscoOscpMIBCompliances,
       "ciscoOscpMIBCompliance": ciscoOscpMIBCompliance,
       "ciscoOscpMIBGroups": ciscoOscpMIBGroups,
       "ciscoOscpBasicGroup": ciscoOscpBasicGroup,
       "ciscoOscpBundleGroup": ciscoOscpBundleGroup,
       "ciscoOscpNotificationsGroup": ciscoOscpNotificationsGroup}
)
