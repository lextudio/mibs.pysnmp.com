# SNMP MIB module (CISCO-L2-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:44 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

ciscoL2ControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313)
)
ciscoL2ControlMIB.setRevisions(
        ("2013-07-03 00:00",
         "2007-01-10 00:00",
         "2003-12-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacLimitExceededAction(Integer32, TextualConvention):
    status = "current"
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
        *(("limit", 2),
          ("limitNoFlood", 3),
          ("shutdown", 4),
          ("warning", 1))
    )



class ClcMacAddressStatsType(Integer32, TextualConvention):
    status = "current"
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
        *(("allMac", 1),
          ("dynamicMac", 2),
          ("mcastMac", 4),
          ("overlayMac", 6),
          ("pvlanCloneMac", 5),
          ("secureMac", 7),
          ("staticMac", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoL2ControlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoL2ControlMIBNotifs = _CiscoL2ControlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0)
)
_CiscoL2ControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoL2ControlMIBObjects = _CiscoL2ControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1)
)
_ClcMacAddressLimitObjects_ObjectIdentity = ObjectIdentity
clcMacAddressLimitObjects = _ClcMacAddressLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1)
)
_ClcMacLimitEnable_Type = TruthValue
_ClcMacLimitEnable_Object = MibScalar
clcMacLimitEnable = _ClcMacLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 1),
    _ClcMacLimitEnable_Type()
)
clcMacLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitEnable.setStatus("current")
_ClcMaxMacLimitDefault_Type = Unsigned32
_ClcMaxMacLimitDefault_Object = MibScalar
clcMaxMacLimitDefault = _ClcMaxMacLimitDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 2),
    _ClcMaxMacLimitDefault_Type()
)
clcMaxMacLimitDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMaxMacLimitDefault.setStatus("current")
_ClcMacLimitExceededActionDefault_Type = MacLimitExceededAction
_ClcMacLimitExceededActionDefault_Object = MibScalar
clcMacLimitExceededActionDefault = _ClcMacLimitExceededActionDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 3),
    _ClcMacLimitExceededActionDefault_Type()
)
clcMacLimitExceededActionDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitExceededActionDefault.setStatus("current")


class _ClcMacLimitExceedNotifOption_Type(Integer32):
    """Custom type clcMacLimitExceedNotifOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("snmpNotif", 2),
          ("sysLog", 1))
    )


_ClcMacLimitExceedNotifOption_Type.__name__ = "Integer32"
_ClcMacLimitExceedNotifOption_Object = MibScalar
clcMacLimitExceedNotifOption = _ClcMacLimitExceedNotifOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 4),
    _ClcMacLimitExceedNotifOption_Type()
)
clcMacLimitExceedNotifOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitExceedNotifOption.setStatus("current")
_ClcMacLimitNotifEnable_Type = TruthValue
_ClcMacLimitNotifEnable_Object = MibScalar
clcMacLimitNotifEnable = _ClcMacLimitNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 5),
    _ClcMacLimitNotifEnable_Type()
)
clcMacLimitNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitNotifEnable.setStatus("current")
_ClcVlanMacLimitTable_Object = MibTable
clcVlanMacLimitTable = _ClcVlanMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6)
)
if mibBuilder.loadTexts:
    clcVlanMacLimitTable.setStatus("current")
_ClcVlanMacLimitEntry_Object = MibTableRow
clcVlanMacLimitEntry = _ClcVlanMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1)
)
clcVlanMacLimitEntry.setIndexNames(
    (0, "CISCO-L2-CONTROL-MIB", "clcVlanMacLimitIndex"),
)
if mibBuilder.loadTexts:
    clcVlanMacLimitEntry.setStatus("current")


class _ClcVlanMacLimitIndex_Type(Unsigned32):
    """Custom type clcVlanMacLimitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ClcVlanMacLimitIndex_Type.__name__ = "Unsigned32"
_ClcVlanMacLimitIndex_Object = MibTableColumn
clcVlanMacLimitIndex = _ClcVlanMacLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 1),
    _ClcVlanMacLimitIndex_Type()
)
clcVlanMacLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcVlanMacLimitIndex.setStatus("current")


class _ClcVlanMacLimitGlobalConfig_Type(Bits):
    """Custom type clcVlanMacLimitGlobalConfig based on Bits"""
    namedValues = NamedValues(
        *(("vlanLimitExceededAction", 1),
          ("vlanLimitHighExceededAction", 3),
          ("vlanMacLimitHigh", 2),
          ("vlanMaxMacLimit", 0))
    )

_ClcVlanMacLimitGlobalConfig_Type.__name__ = "Bits"
_ClcVlanMacLimitGlobalConfig_Object = MibTableColumn
clcVlanMacLimitGlobalConfig = _ClcVlanMacLimitGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 2),
    _ClcVlanMacLimitGlobalConfig_Type()
)
clcVlanMacLimitGlobalConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcVlanMacLimitGlobalConfig.setStatus("current")
_ClcVlanMaxMacLimit_Type = Unsigned32
_ClcVlanMaxMacLimit_Object = MibTableColumn
clcVlanMaxMacLimit = _ClcVlanMaxMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 3),
    _ClcVlanMaxMacLimit_Type()
)
clcVlanMaxMacLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcVlanMaxMacLimit.setStatus("current")
_ClcVlanMacLimitExceededAction_Type = MacLimitExceededAction
_ClcVlanMacLimitExceededAction_Object = MibTableColumn
clcVlanMacLimitExceededAction = _ClcVlanMacLimitExceededAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 4),
    _ClcVlanMacLimitExceededAction_Type()
)
clcVlanMacLimitExceededAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcVlanMacLimitExceededAction.setStatus("current")
_ClcVlanMacLimitStatus_Type = RowStatus
_ClcVlanMacLimitStatus_Object = MibTableColumn
clcVlanMacLimitStatus = _ClcVlanMacLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 5),
    _ClcVlanMacLimitStatus_Type()
)
clcVlanMacLimitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcVlanMacLimitStatus.setStatus("current")


class _ClcVlanMacLimitEnable_Type(TruthValue):
    """Custom type clcVlanMacLimitEnable based on TruthValue"""


_ClcVlanMacLimitEnable_Object = MibTableColumn
clcVlanMacLimitEnable = _ClcVlanMacLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 6),
    _ClcVlanMacLimitEnable_Type()
)
clcVlanMacLimitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcVlanMacLimitEnable.setStatus("current")
_ClcVlanMacLimitHigh_Type = Unsigned32
_ClcVlanMacLimitHigh_Object = MibTableColumn
clcVlanMacLimitHigh = _ClcVlanMacLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 7),
    _ClcVlanMacLimitHigh_Type()
)
clcVlanMacLimitHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcVlanMacLimitHigh.setStatus("current")
_ClcVlanMacLimitHighExceedAction_Type = MacLimitExceededAction
_ClcVlanMacLimitHighExceedAction_Object = MibTableColumn
clcVlanMacLimitHighExceedAction = _ClcVlanMacLimitHighExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 6, 1, 8),
    _ClcVlanMacLimitHighExceedAction_Type()
)
clcVlanMacLimitHighExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcVlanMacLimitHighExceedAction.setStatus("current")
_ClcFdbVlanInfoTable_Object = MibTable
clcFdbVlanInfoTable = _ClcFdbVlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 7)
)
if mibBuilder.loadTexts:
    clcFdbVlanInfoTable.setStatus("current")
_ClcFdbVlanInfoEntry_Object = MibTableRow
clcFdbVlanInfoEntry = _ClcFdbVlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 7, 1)
)
clcFdbVlanInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L2-CONTROL-MIB", "clcVlanMacLimitIndex"),
)
if mibBuilder.loadTexts:
    clcFdbVlanInfoEntry.setStatus("current")
_ClcFdbVlanMacUsage_Type = Unsigned32
_ClcFdbVlanMacUsage_Object = MibTableColumn
clcFdbVlanMacUsage = _ClcFdbVlanMacUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 7, 1, 1),
    _ClcFdbVlanMacUsage_Type()
)
clcFdbVlanMacUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcFdbVlanMacUsage.setStatus("current")
_ClcMacLimitInterval_Type = Unsigned32
_ClcMacLimitInterval_Object = MibScalar
clcMacLimitInterval = _ClcMacLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 8),
    _ClcMacLimitInterval_Type()
)
clcMacLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitInterval.setStatus("current")
if mibBuilder.loadTexts:
    clcMacLimitInterval.setUnits("seconds")
_ClcMacLimitHighDefault_Type = Unsigned32
_ClcMacLimitHighDefault_Object = MibScalar
clcMacLimitHighDefault = _ClcMacLimitHighDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 9),
    _ClcMacLimitHighDefault_Type()
)
clcMacLimitHighDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitHighDefault.setStatus("current")
_ClcMacLimitHighExceedActionDef_Type = MacLimitExceededAction
_ClcMacLimitHighExceedActionDef_Object = MibScalar
clcMacLimitHighExceedActionDef = _ClcMacLimitHighExceedActionDef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 10),
    _ClcMacLimitHighExceedActionDef_Type()
)
clcMacLimitHighExceedActionDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitHighExceedActionDef.setStatus("current")
_ClcMacLimitHighNotifEnable_Type = TruthValue
_ClcMacLimitHighNotifEnable_Object = MibScalar
clcMacLimitHighNotifEnable = _ClcMacLimitHighNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 1, 11),
    _ClcMacLimitHighNotifEnable_Type()
)
clcMacLimitHighNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcMacLimitHighNotifEnable.setStatus("current")
_ClcUnicastFloodObjects_ObjectIdentity = ObjectIdentity
clcUnicastFloodObjects = _ClcUnicastFloodObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 2)
)
_ClcUnicastFloodTable_Object = MibTable
clcUnicastFloodTable = _ClcUnicastFloodTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clcUnicastFloodTable.setStatus("current")
_ClcUnicastFloodEntry_Object = MibTableRow
clcUnicastFloodEntry = _ClcUnicastFloodEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 2, 1, 1)
)
clcUnicastFloodEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clcUnicastFloodEntry.setStatus("current")
_ClcUnicastFloodAdminEnable_Type = TruthValue
_ClcUnicastFloodAdminEnable_Object = MibTableColumn
clcUnicastFloodAdminEnable = _ClcUnicastFloodAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 2, 1, 1, 1),
    _ClcUnicastFloodAdminEnable_Type()
)
clcUnicastFloodAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcUnicastFloodAdminEnable.setStatus("current")
_ClcUnicastFloodOperEnable_Type = TruthValue
_ClcUnicastFloodOperEnable_Object = MibTableColumn
clcUnicastFloodOperEnable = _ClcUnicastFloodOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 2, 1, 1, 2),
    _ClcUnicastFloodOperEnable_Type()
)
clcUnicastFloodOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcUnicastFloodOperEnable.setStatus("current")
_ClcIfMacAddressLimitObjects_ObjectIdentity = ObjectIdentity
clcIfMacAddressLimitObjects = _ClcIfMacAddressLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3)
)
_ClcIfMacLimitTable_Object = MibTable
clcIfMacLimitTable = _ClcIfMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clcIfMacLimitTable.setStatus("current")
_ClcIfMacLimitEntry_Object = MibTableRow
clcIfMacLimitEntry = _ClcIfMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1)
)
clcIfMacLimitEntry.setIndexNames(
    (0, "CISCO-L2-CONTROL-MIB", "clcIfMacLimitIfIndex"),
)
if mibBuilder.loadTexts:
    clcIfMacLimitEntry.setStatus("current")
_ClcIfMacLimitIfIndex_Type = InterfaceIndex
_ClcIfMacLimitIfIndex_Object = MibTableColumn
clcIfMacLimitIfIndex = _ClcIfMacLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 1),
    _ClcIfMacLimitIfIndex_Type()
)
clcIfMacLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcIfMacLimitIfIndex.setStatus("current")


class _ClcIfMacLimitEnable_Type(TruthValue):
    """Custom type clcIfMacLimitEnable based on TruthValue"""


_ClcIfMacLimitEnable_Object = MibTableColumn
clcIfMacLimitEnable = _ClcIfMacLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 2),
    _ClcIfMacLimitEnable_Type()
)
clcIfMacLimitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfMacLimitEnable.setStatus("current")


class _ClcIfMacLimitGlobalConfig_Type(Bits):
    """Custom type clcIfMacLimitGlobalConfig based on Bits"""
    namedValues = NamedValues(
        *(("ifLimitHighExceededAction", 3),
          ("ifLimitLowExceededAction", 1),
          ("ifMacLimitHigh", 2),
          ("ifMacLimitLow", 0))
    )

_ClcIfMacLimitGlobalConfig_Type.__name__ = "Bits"
_ClcIfMacLimitGlobalConfig_Object = MibTableColumn
clcIfMacLimitGlobalConfig = _ClcIfMacLimitGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 3),
    _ClcIfMacLimitGlobalConfig_Type()
)
clcIfMacLimitGlobalConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcIfMacLimitGlobalConfig.setStatus("current")
_ClcIfMacLimitLow_Type = Unsigned32
_ClcIfMacLimitLow_Object = MibTableColumn
clcIfMacLimitLow = _ClcIfMacLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 4),
    _ClcIfMacLimitLow_Type()
)
clcIfMacLimitLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfMacLimitLow.setStatus("current")
_ClcIfMacLimitLowExceedAction_Type = MacLimitExceededAction
_ClcIfMacLimitLowExceedAction_Object = MibTableColumn
clcIfMacLimitLowExceedAction = _ClcIfMacLimitLowExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 5),
    _ClcIfMacLimitLowExceedAction_Type()
)
clcIfMacLimitLowExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfMacLimitLowExceedAction.setStatus("current")
_ClcIfMacLimitHigh_Type = Unsigned32
_ClcIfMacLimitHigh_Object = MibTableColumn
clcIfMacLimitHigh = _ClcIfMacLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 6),
    _ClcIfMacLimitHigh_Type()
)
clcIfMacLimitHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfMacLimitHigh.setStatus("current")
_ClcIfMacLimitHighExceedAction_Type = MacLimitExceededAction
_ClcIfMacLimitHighExceedAction_Object = MibTableColumn
clcIfMacLimitHighExceedAction = _ClcIfMacLimitHighExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 7),
    _ClcIfMacLimitHighExceedAction_Type()
)
clcIfMacLimitHighExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfMacLimitHighExceedAction.setStatus("current")
_ClcIfMacLimitStatus_Type = RowStatus
_ClcIfMacLimitStatus_Object = MibTableColumn
clcIfMacLimitStatus = _ClcIfMacLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 1, 1, 8),
    _ClcIfMacLimitStatus_Type()
)
clcIfMacLimitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfMacLimitStatus.setStatus("current")
_ClcFdbIfInfoTable_Object = MibTable
clcFdbIfInfoTable = _ClcFdbIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clcFdbIfInfoTable.setStatus("current")
_ClcFdbIfInfoEntry_Object = MibTableRow
clcFdbIfInfoEntry = _ClcFdbIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 2, 1)
)
clcFdbIfInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L2-CONTROL-MIB", "clcIfMacLimitIfIndex"),
)
if mibBuilder.loadTexts:
    clcFdbIfInfoEntry.setStatus("current")
_ClcFdbIfMacUsage_Type = Unsigned32
_ClcFdbIfMacUsage_Object = MibTableColumn
clcFdbIfMacUsage = _ClcFdbIfMacUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 2, 1, 1),
    _ClcFdbIfMacUsage_Type()
)
clcFdbIfMacUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcFdbIfMacUsage.setStatus("current")
_ClcIfMacLimitLowNotifEnable_Type = TruthValue
_ClcIfMacLimitLowNotifEnable_Object = MibScalar
clcIfMacLimitLowNotifEnable = _ClcIfMacLimitLowNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 3),
    _ClcIfMacLimitLowNotifEnable_Type()
)
clcIfMacLimitLowNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcIfMacLimitLowNotifEnable.setStatus("current")
_ClcIfMacLimitHighNotifEnable_Type = TruthValue
_ClcIfMacLimitHighNotifEnable_Object = MibScalar
clcIfMacLimitHighNotifEnable = _ClcIfMacLimitHighNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 3, 4),
    _ClcIfMacLimitHighNotifEnable_Type()
)
clcIfMacLimitHighNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcIfMacLimitHighNotifEnable.setStatus("current")
_ClcIfVlanMacAddressLimitObjects_ObjectIdentity = ObjectIdentity
clcIfVlanMacAddressLimitObjects = _ClcIfVlanMacAddressLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4)
)
_ClcIfVlanMacLimitTable_Object = MibTable
clcIfVlanMacLimitTable = _ClcIfVlanMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitTable.setStatus("current")
_ClcIfVlanMacLimitEntry_Object = MibTableRow
clcIfVlanMacLimitEntry = _ClcIfVlanMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1)
)
clcIfVlanMacLimitEntry.setIndexNames(
    (0, "CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitIfIndex"),
    (0, "CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitVlanIndex"),
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitEntry.setStatus("current")
_ClcIfVlanMacLimitIfIndex_Type = InterfaceIndex
_ClcIfVlanMacLimitIfIndex_Object = MibTableColumn
clcIfVlanMacLimitIfIndex = _ClcIfVlanMacLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 1),
    _ClcIfVlanMacLimitIfIndex_Type()
)
clcIfVlanMacLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitIfIndex.setStatus("current")
_ClcIfVlanMacLimitVlanIndex_Type = VlanIndex
_ClcIfVlanMacLimitVlanIndex_Object = MibTableColumn
clcIfVlanMacLimitVlanIndex = _ClcIfVlanMacLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 2),
    _ClcIfVlanMacLimitVlanIndex_Type()
)
clcIfVlanMacLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitVlanIndex.setStatus("current")


class _ClcIfVlanMacLimitEnable_Type(TruthValue):
    """Custom type clcIfVlanMacLimitEnable based on TruthValue"""


_ClcIfVlanMacLimitEnable_Object = MibTableColumn
clcIfVlanMacLimitEnable = _ClcIfVlanMacLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 3),
    _ClcIfVlanMacLimitEnable_Type()
)
clcIfVlanMacLimitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitEnable.setStatus("current")


class _ClcIfVlanMacLimitGlobalConfig_Type(Bits):
    """Custom type clcIfVlanMacLimitGlobalConfig based on Bits"""
    namedValues = NamedValues(
        *(("ifVlanLimitHighExceededAction", 3),
          ("ifVlanLimitLowExceededAction", 1),
          ("ifVlanMacLimitHigh", 2),
          ("ifVlanMacLimitLow", 0))
    )

_ClcIfVlanMacLimitGlobalConfig_Type.__name__ = "Bits"
_ClcIfVlanMacLimitGlobalConfig_Object = MibTableColumn
clcIfVlanMacLimitGlobalConfig = _ClcIfVlanMacLimitGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 4),
    _ClcIfVlanMacLimitGlobalConfig_Type()
)
clcIfVlanMacLimitGlobalConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitGlobalConfig.setStatus("current")
_ClcIfVlanMacLimitLow_Type = Unsigned32
_ClcIfVlanMacLimitLow_Object = MibTableColumn
clcIfVlanMacLimitLow = _ClcIfVlanMacLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 5),
    _ClcIfVlanMacLimitLow_Type()
)
clcIfVlanMacLimitLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitLow.setStatus("current")
_ClcIfVlanMacLimitLowExceedAction_Type = MacLimitExceededAction
_ClcIfVlanMacLimitLowExceedAction_Object = MibTableColumn
clcIfVlanMacLimitLowExceedAction = _ClcIfVlanMacLimitLowExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 6),
    _ClcIfVlanMacLimitLowExceedAction_Type()
)
clcIfVlanMacLimitLowExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitLowExceedAction.setStatus("current")
_ClcIfVlanMacLimitHigh_Type = Unsigned32
_ClcIfVlanMacLimitHigh_Object = MibTableColumn
clcIfVlanMacLimitHigh = _ClcIfVlanMacLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 7),
    _ClcIfVlanMacLimitHigh_Type()
)
clcIfVlanMacLimitHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitHigh.setStatus("current")
_ClcIfVlanMacLimitHiExceedAction_Type = MacLimitExceededAction
_ClcIfVlanMacLimitHiExceedAction_Object = MibTableColumn
clcIfVlanMacLimitHiExceedAction = _ClcIfVlanMacLimitHiExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 8),
    _ClcIfVlanMacLimitHiExceedAction_Type()
)
clcIfVlanMacLimitHiExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitHiExceedAction.setStatus("current")
_ClcIfVlanMacLimitStatus_Type = RowStatus
_ClcIfVlanMacLimitStatus_Object = MibTableColumn
clcIfVlanMacLimitStatus = _ClcIfVlanMacLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 1, 1, 9),
    _ClcIfVlanMacLimitStatus_Type()
)
clcIfVlanMacLimitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitStatus.setStatus("current")
_ClcFdbIfVlanInfoTable_Object = MibTable
clcFdbIfVlanInfoTable = _ClcFdbIfVlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 2)
)
if mibBuilder.loadTexts:
    clcFdbIfVlanInfoTable.setStatus("current")
_ClcFdbIfVlanInfoEntry_Object = MibTableRow
clcFdbIfVlanInfoEntry = _ClcFdbIfVlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 2, 1)
)
clcFdbIfVlanInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitIfIndex"),
    (0, "CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitVlanIndex"),
)
if mibBuilder.loadTexts:
    clcFdbIfVlanInfoEntry.setStatus("current")
_ClcFdbIfVlanMacUsage_Type = Unsigned32
_ClcFdbIfVlanMacUsage_Object = MibTableColumn
clcFdbIfVlanMacUsage = _ClcFdbIfVlanMacUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 2, 1, 1),
    _ClcFdbIfVlanMacUsage_Type()
)
clcFdbIfVlanMacUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcFdbIfVlanMacUsage.setStatus("current")
_ClcIfVlanMacLimitLowNotifEnable_Type = TruthValue
_ClcIfVlanMacLimitLowNotifEnable_Object = MibScalar
clcIfVlanMacLimitLowNotifEnable = _ClcIfVlanMacLimitLowNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 3),
    _ClcIfVlanMacLimitLowNotifEnable_Type()
)
clcIfVlanMacLimitLowNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitLowNotifEnable.setStatus("current")
_ClcIfVlanMacLimitHighNotifEnable_Type = TruthValue
_ClcIfVlanMacLimitHighNotifEnable_Object = MibScalar
clcIfVlanMacLimitHighNotifEnable = _ClcIfVlanMacLimitHighNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 4, 4),
    _ClcIfVlanMacLimitHighNotifEnable_Type()
)
clcIfVlanMacLimitHighNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcIfVlanMacLimitHighNotifEnable.setStatus("current")
_ClcMacAddressStatsObjects_ObjectIdentity = ObjectIdentity
clcMacAddressStatsObjects = _ClcMacAddressStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 5)
)
_ClcFdbMacAddressStatsTable_Object = MibTable
clcFdbMacAddressStatsTable = _ClcFdbMacAddressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clcFdbMacAddressStatsTable.setStatus("current")
_ClcFdbMacAddressStatsEntry_Object = MibTableRow
clcFdbMacAddressStatsEntry = _ClcFdbMacAddressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 5, 1, 1)
)
clcFdbMacAddressStatsEntry.setIndexNames(
    (0, "CISCO-L2-CONTROL-MIB", "clcFdbMacAddressStatsType"),
)
if mibBuilder.loadTexts:
    clcFdbMacAddressStatsEntry.setStatus("current")
_ClcFdbMacAddressStatsType_Type = ClcMacAddressStatsType
_ClcFdbMacAddressStatsType_Object = MibTableColumn
clcFdbMacAddressStatsType = _ClcFdbMacAddressStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 5, 1, 1, 1),
    _ClcFdbMacAddressStatsType_Type()
)
clcFdbMacAddressStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcFdbMacAddressStatsType.setStatus("current")
_ClcFdbMacAddressStatsNumber_Type = Unsigned32
_ClcFdbMacAddressStatsNumber_Object = MibTableColumn
clcFdbMacAddressStatsNumber = _ClcFdbMacAddressStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 1, 5, 1, 1, 2),
    _ClcFdbMacAddressStatsNumber_Type()
)
clcFdbMacAddressStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcFdbMacAddressStatsNumber.setStatus("current")
_CiscoL2ControlMIBConformance_ObjectIdentity = ObjectIdentity
ciscoL2ControlMIBConformance = _CiscoL2ControlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2)
)
_CiscoL2ControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoL2ControlMIBCompliances = _CiscoL2ControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 1)
)
_CiscoL2ControlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoL2ControlMIBGroups = _CiscoL2ControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2)
)

# Managed Objects groups

clcMacAddressLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 1)
)
clcMacAddressLimitGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcMacLimitEnable"),
        ("CISCO-L2-CONTROL-MIB", "clcMaxMacLimitDefault"),
        ("CISCO-L2-CONTROL-MIB", "clcMacLimitExceededActionDefault"),
        ("CISCO-L2-CONTROL-MIB", "clcMacLimitExceedNotifOption"))
)
if mibBuilder.loadTexts:
    clcMacAddressLimitGroup.setStatus("current")

clcVlanMacAddressLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 2)
)
clcVlanMacAddressLimitGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitGlobalConfig"),
        ("CISCO-L2-CONTROL-MIB", "clcVlanMaxMacLimit"),
        ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitExceededAction"),
        ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitStatus"),
        ("CISCO-L2-CONTROL-MIB", "clcFdbVlanMacUsage"))
)
if mibBuilder.loadTexts:
    clcVlanMacAddressLimitGroup.setStatus("current")

clcUnicastFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 4)
)
clcUnicastFloodGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcUnicastFloodAdminEnable"),
        ("CISCO-L2-CONTROL-MIB", "clcUnicastFloodOperEnable"))
)
if mibBuilder.loadTexts:
    clcUnicastFloodGroup.setStatus("current")

clcMacAddressLimitIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 5)
)
clcMacAddressLimitIntervalGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcMacLimitInterval")
)
if mibBuilder.loadTexts:
    clcMacAddressLimitIntervalGroup.setStatus("current")

clcMacAddressLimitGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 6)
)
clcMacAddressLimitGroup1.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcMacLimitHighDefault"),
        ("CISCO-L2-CONTROL-MIB", "clcMacLimitHighExceedActionDef"))
)
if mibBuilder.loadTexts:
    clcMacAddressLimitGroup1.setStatus("current")

clcVlanMacAddressLimitGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 7)
)
clcVlanMacAddressLimitGroup1.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitHigh"),
        ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitHighExceedAction"))
)
if mibBuilder.loadTexts:
    clcVlanMacAddressLimitGroup1.setStatus("current")

clcVlanMacLimitEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 8)
)
clcVlanMacLimitEnableGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitEnable")
)
if mibBuilder.loadTexts:
    clcVlanMacLimitEnableGroup.setStatus("current")

clcVlanMacLimitNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 9)
)
clcVlanMacLimitNotifControlGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcMacLimitNotifEnable")
)
if mibBuilder.loadTexts:
    clcVlanMacLimitNotifControlGroup.setStatus("current")

clcVlanMacLimitNotifControlGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 10)
)
clcVlanMacLimitNotifControlGroup1.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcMacLimitHighNotifEnable")
)
if mibBuilder.loadTexts:
    clcVlanMacLimitNotifControlGroup1.setStatus("current")

clcIfMacAddressLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 12)
)
clcIfMacAddressLimitGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcIfMacLimitGlobalConfig"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitLow"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitLowExceedAction"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitHigh"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitHighExceedAction"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitStatus"),
        ("CISCO-L2-CONTROL-MIB", "clcFdbIfMacUsage"))
)
if mibBuilder.loadTexts:
    clcIfMacAddressLimitGroup.setStatus("current")

clcIfMacLimitEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 13)
)
clcIfMacLimitEnableGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitEnable")
)
if mibBuilder.loadTexts:
    clcIfMacLimitEnableGroup.setStatus("current")

clcIfMacLimitNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 14)
)
clcIfMacLimitNotifControlGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcIfMacLimitLowNotifEnable"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitHighNotifEnable"))
)
if mibBuilder.loadTexts:
    clcIfMacLimitNotifControlGroup.setStatus("current")

clcIfVlanMacAddressLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 16)
)
clcIfVlanMacAddressLimitGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitGlobalConfig"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitLow"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitLowExceedAction"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitHigh"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitHiExceedAction"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitStatus"),
        ("CISCO-L2-CONTROL-MIB", "clcFdbIfVlanMacUsage"))
)
if mibBuilder.loadTexts:
    clcIfVlanMacAddressLimitGroup.setStatus("current")

clcIfVlanMacLimitEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 17)
)
clcIfVlanMacLimitEnableGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitEnable")
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitEnableGroup.setStatus("current")

clcIfVlanMacLimitNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 18)
)
clcIfVlanMacLimitNotifControlGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitLowNotifEnable"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitHighNotifEnable"))
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitNotifControlGroup.setStatus("current")

clcMacAddressStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 20)
)
clcMacAddressStatsGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcFdbMacAddressStatsNumber")
)
if mibBuilder.loadTexts:
    clcMacAddressStatsGroup.setStatus("current")


# Notification objects

clcVlanMacLimitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0, 1)
)
clcVlanMacLimitNotif.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcFdbVlanMacUsage"),
        ("CISCO-L2-CONTROL-MIB", "clcVlanMaxMacLimit"))
)
if mibBuilder.loadTexts:
    clcVlanMacLimitNotif.setStatus(
        "current"
    )

clcVlanMacLimitHighNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0, 2)
)
clcVlanMacLimitHighNotif.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcFdbVlanMacUsage"),
        ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitHigh"))
)
if mibBuilder.loadTexts:
    clcVlanMacLimitHighNotif.setStatus(
        "current"
    )

clcIfMacLimitLowNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0, 3)
)
clcIfMacLimitLowNotif.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcFdbIfMacUsage"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitLow"))
)
if mibBuilder.loadTexts:
    clcIfMacLimitLowNotif.setStatus(
        "current"
    )

clcIfMacLimitHighNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0, 4)
)
clcIfMacLimitHighNotif.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcFdbIfMacUsage"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitHigh"))
)
if mibBuilder.loadTexts:
    clcIfMacLimitHighNotif.setStatus(
        "current"
    )

clcIfVlanMacLimitLowNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0, 5)
)
clcIfVlanMacLimitLowNotif.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcFdbIfVlanMacUsage"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitLow"))
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitLowNotif.setStatus(
        "current"
    )

clcIfVlanMacLimitHighNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 0, 6)
)
clcIfVlanMacLimitHighNotif.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcFdbIfVlanMacUsage"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitHigh"))
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitHighNotif.setStatus(
        "current"
    )


# Notifications groups

clcVlanMacLimitNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 3)
)
clcVlanMacLimitNotifsGroup.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitNotif")
)
if mibBuilder.loadTexts:
    clcVlanMacLimitNotifsGroup.setStatus(
        "current"
    )

clcVlanMacLimitNotifsGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 11)
)
clcVlanMacLimitNotifsGroup1.setObjects(
    ("CISCO-L2-CONTROL-MIB", "clcVlanMacLimitHighNotif")
)
if mibBuilder.loadTexts:
    clcVlanMacLimitNotifsGroup1.setStatus(
        "current"
    )

clcIfMacLimitNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 15)
)
clcIfMacLimitNotifsGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcIfMacLimitLowNotif"),
        ("CISCO-L2-CONTROL-MIB", "clcIfMacLimitHighNotif"))
)
if mibBuilder.loadTexts:
    clcIfMacLimitNotifsGroup.setStatus(
        "current"
    )

clcIfVlanMacLimitNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 2, 19)
)
clcIfVlanMacLimitNotifsGroup.setObjects(
      *(("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitLowNotif"),
        ("CISCO-L2-CONTROL-MIB", "clcIfVlanMacLimitHighNotif"))
)
if mibBuilder.loadTexts:
    clcIfVlanMacLimitNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoL2ControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoL2ControlMIBCompliance.setStatus(
        "deprecated"
    )

ciscoL2ControlMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoL2ControlMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoL2ControlMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 313, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoL2ControlMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2-CONTROL-MIB",
    **{"MacLimitExceededAction": MacLimitExceededAction,
       "ClcMacAddressStatsType": ClcMacAddressStatsType,
       "ciscoL2ControlMIB": ciscoL2ControlMIB,
       "ciscoL2ControlMIBNotifs": ciscoL2ControlMIBNotifs,
       "clcVlanMacLimitNotif": clcVlanMacLimitNotif,
       "clcVlanMacLimitHighNotif": clcVlanMacLimitHighNotif,
       "clcIfMacLimitLowNotif": clcIfMacLimitLowNotif,
       "clcIfMacLimitHighNotif": clcIfMacLimitHighNotif,
       "clcIfVlanMacLimitLowNotif": clcIfVlanMacLimitLowNotif,
       "clcIfVlanMacLimitHighNotif": clcIfVlanMacLimitHighNotif,
       "ciscoL2ControlMIBObjects": ciscoL2ControlMIBObjects,
       "clcMacAddressLimitObjects": clcMacAddressLimitObjects,
       "clcMacLimitEnable": clcMacLimitEnable,
       "clcMaxMacLimitDefault": clcMaxMacLimitDefault,
       "clcMacLimitExceededActionDefault": clcMacLimitExceededActionDefault,
       "clcMacLimitExceedNotifOption": clcMacLimitExceedNotifOption,
       "clcMacLimitNotifEnable": clcMacLimitNotifEnable,
       "clcVlanMacLimitTable": clcVlanMacLimitTable,
       "clcVlanMacLimitEntry": clcVlanMacLimitEntry,
       "clcVlanMacLimitIndex": clcVlanMacLimitIndex,
       "clcVlanMacLimitGlobalConfig": clcVlanMacLimitGlobalConfig,
       "clcVlanMaxMacLimit": clcVlanMaxMacLimit,
       "clcVlanMacLimitExceededAction": clcVlanMacLimitExceededAction,
       "clcVlanMacLimitStatus": clcVlanMacLimitStatus,
       "clcVlanMacLimitEnable": clcVlanMacLimitEnable,
       "clcVlanMacLimitHigh": clcVlanMacLimitHigh,
       "clcVlanMacLimitHighExceedAction": clcVlanMacLimitHighExceedAction,
       "clcFdbVlanInfoTable": clcFdbVlanInfoTable,
       "clcFdbVlanInfoEntry": clcFdbVlanInfoEntry,
       "clcFdbVlanMacUsage": clcFdbVlanMacUsage,
       "clcMacLimitInterval": clcMacLimitInterval,
       "clcMacLimitHighDefault": clcMacLimitHighDefault,
       "clcMacLimitHighExceedActionDef": clcMacLimitHighExceedActionDef,
       "clcMacLimitHighNotifEnable": clcMacLimitHighNotifEnable,
       "clcUnicastFloodObjects": clcUnicastFloodObjects,
       "clcUnicastFloodTable": clcUnicastFloodTable,
       "clcUnicastFloodEntry": clcUnicastFloodEntry,
       "clcUnicastFloodAdminEnable": clcUnicastFloodAdminEnable,
       "clcUnicastFloodOperEnable": clcUnicastFloodOperEnable,
       "clcIfMacAddressLimitObjects": clcIfMacAddressLimitObjects,
       "clcIfMacLimitTable": clcIfMacLimitTable,
       "clcIfMacLimitEntry": clcIfMacLimitEntry,
       "clcIfMacLimitIfIndex": clcIfMacLimitIfIndex,
       "clcIfMacLimitEnable": clcIfMacLimitEnable,
       "clcIfMacLimitGlobalConfig": clcIfMacLimitGlobalConfig,
       "clcIfMacLimitLow": clcIfMacLimitLow,
       "clcIfMacLimitLowExceedAction": clcIfMacLimitLowExceedAction,
       "clcIfMacLimitHigh": clcIfMacLimitHigh,
       "clcIfMacLimitHighExceedAction": clcIfMacLimitHighExceedAction,
       "clcIfMacLimitStatus": clcIfMacLimitStatus,
       "clcFdbIfInfoTable": clcFdbIfInfoTable,
       "clcFdbIfInfoEntry": clcFdbIfInfoEntry,
       "clcFdbIfMacUsage": clcFdbIfMacUsage,
       "clcIfMacLimitLowNotifEnable": clcIfMacLimitLowNotifEnable,
       "clcIfMacLimitHighNotifEnable": clcIfMacLimitHighNotifEnable,
       "clcIfVlanMacAddressLimitObjects": clcIfVlanMacAddressLimitObjects,
       "clcIfVlanMacLimitTable": clcIfVlanMacLimitTable,
       "clcIfVlanMacLimitEntry": clcIfVlanMacLimitEntry,
       "clcIfVlanMacLimitIfIndex": clcIfVlanMacLimitIfIndex,
       "clcIfVlanMacLimitVlanIndex": clcIfVlanMacLimitVlanIndex,
       "clcIfVlanMacLimitEnable": clcIfVlanMacLimitEnable,
       "clcIfVlanMacLimitGlobalConfig": clcIfVlanMacLimitGlobalConfig,
       "clcIfVlanMacLimitLow": clcIfVlanMacLimitLow,
       "clcIfVlanMacLimitLowExceedAction": clcIfVlanMacLimitLowExceedAction,
       "clcIfVlanMacLimitHigh": clcIfVlanMacLimitHigh,
       "clcIfVlanMacLimitHiExceedAction": clcIfVlanMacLimitHiExceedAction,
       "clcIfVlanMacLimitStatus": clcIfVlanMacLimitStatus,
       "clcFdbIfVlanInfoTable": clcFdbIfVlanInfoTable,
       "clcFdbIfVlanInfoEntry": clcFdbIfVlanInfoEntry,
       "clcFdbIfVlanMacUsage": clcFdbIfVlanMacUsage,
       "clcIfVlanMacLimitLowNotifEnable": clcIfVlanMacLimitLowNotifEnable,
       "clcIfVlanMacLimitHighNotifEnable": clcIfVlanMacLimitHighNotifEnable,
       "clcMacAddressStatsObjects": clcMacAddressStatsObjects,
       "clcFdbMacAddressStatsTable": clcFdbMacAddressStatsTable,
       "clcFdbMacAddressStatsEntry": clcFdbMacAddressStatsEntry,
       "clcFdbMacAddressStatsType": clcFdbMacAddressStatsType,
       "clcFdbMacAddressStatsNumber": clcFdbMacAddressStatsNumber,
       "ciscoL2ControlMIBConformance": ciscoL2ControlMIBConformance,
       "ciscoL2ControlMIBCompliances": ciscoL2ControlMIBCompliances,
       "ciscoL2ControlMIBCompliance": ciscoL2ControlMIBCompliance,
       "ciscoL2ControlMIBCompliance2": ciscoL2ControlMIBCompliance2,
       "ciscoL2ControlMIBCompliance3": ciscoL2ControlMIBCompliance3,
       "ciscoL2ControlMIBGroups": ciscoL2ControlMIBGroups,
       "clcMacAddressLimitGroup": clcMacAddressLimitGroup,
       "clcVlanMacAddressLimitGroup": clcVlanMacAddressLimitGroup,
       "clcVlanMacLimitNotifsGroup": clcVlanMacLimitNotifsGroup,
       "clcUnicastFloodGroup": clcUnicastFloodGroup,
       "clcMacAddressLimitIntervalGroup": clcMacAddressLimitIntervalGroup,
       "clcMacAddressLimitGroup1": clcMacAddressLimitGroup1,
       "clcVlanMacAddressLimitGroup1": clcVlanMacAddressLimitGroup1,
       "clcVlanMacLimitEnableGroup": clcVlanMacLimitEnableGroup,
       "clcVlanMacLimitNotifControlGroup": clcVlanMacLimitNotifControlGroup,
       "clcVlanMacLimitNotifControlGroup1": clcVlanMacLimitNotifControlGroup1,
       "clcVlanMacLimitNotifsGroup1": clcVlanMacLimitNotifsGroup1,
       "clcIfMacAddressLimitGroup": clcIfMacAddressLimitGroup,
       "clcIfMacLimitEnableGroup": clcIfMacLimitEnableGroup,
       "clcIfMacLimitNotifControlGroup": clcIfMacLimitNotifControlGroup,
       "clcIfMacLimitNotifsGroup": clcIfMacLimitNotifsGroup,
       "clcIfVlanMacAddressLimitGroup": clcIfVlanMacAddressLimitGroup,
       "clcIfVlanMacLimitEnableGroup": clcIfVlanMacLimitEnableGroup,
       "clcIfVlanMacLimitNotifControlGroup": clcIfVlanMacLimitNotifControlGroup,
       "clcIfVlanMacLimitNotifsGroup": clcIfVlanMacLimitNotifsGroup,
       "clcMacAddressStatsGroup": clcMacAddressStatsGroup}
)
