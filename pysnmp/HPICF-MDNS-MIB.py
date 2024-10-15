# SNMP MIB module (HPICF-MDNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPICF-MDNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:19 2024
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

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-FTRCO",
    "VidList")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfMdns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124)
)
hpicfMdns.setRevisions(
        ("2015-05-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfMdnsNotifications_ObjectIdentity = ObjectIdentity
hpicfMdnsNotifications = _HpicfMdnsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 0)
)
_HpicfMdnsObjects_ObjectIdentity = ObjectIdentity
hpicfMdnsObjects = _HpicfMdnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1)
)


class _HpicfMdnsAdminState_Type(Integer32):
    """Custom type hpicfMdnsAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfMdnsAdminState_Type.__name__ = "Integer32"
_HpicfMdnsAdminState_Object = MibScalar
hpicfMdnsAdminState = _HpicfMdnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 1),
    _HpicfMdnsAdminState_Type()
)
hpicfMdnsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMdnsAdminState.setStatus("current")


class _HpicfMdnsDefaultFilterInAction_Type(Integer32):
    """Custom type hpicfMdnsDefaultFilterInAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_HpicfMdnsDefaultFilterInAction_Type.__name__ = "Integer32"
_HpicfMdnsDefaultFilterInAction_Object = MibScalar
hpicfMdnsDefaultFilterInAction = _HpicfMdnsDefaultFilterInAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 2),
    _HpicfMdnsDefaultFilterInAction_Type()
)
hpicfMdnsDefaultFilterInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMdnsDefaultFilterInAction.setStatus("current")


class _HpicfMdnsDefaultFilterOutAction_Type(Integer32):
    """Custom type hpicfMdnsDefaultFilterOutAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_HpicfMdnsDefaultFilterOutAction_Type.__name__ = "Integer32"
_HpicfMdnsDefaultFilterOutAction_Object = MibScalar
hpicfMdnsDefaultFilterOutAction = _HpicfMdnsDefaultFilterOutAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 3),
    _HpicfMdnsDefaultFilterOutAction_Type()
)
hpicfMdnsDefaultFilterOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMdnsDefaultFilterOutAction.setStatus("current")
_HpicfMdnsGatewayVIDList_Type = VidList
_HpicfMdnsGatewayVIDList_Object = MibScalar
hpicfMdnsGatewayVIDList = _HpicfMdnsGatewayVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 4),
    _HpicfMdnsGatewayVIDList_Type()
)
hpicfMdnsGatewayVIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMdnsGatewayVIDList.setStatus("current")
_HpicfMdnsProfileTable_Object = MibTable
hpicfMdnsProfileTable = _HpicfMdnsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfMdnsProfileTable.setStatus("current")
_HpicfMdnsProfileEntry_Object = MibTableRow
hpicfMdnsProfileEntry = _HpicfMdnsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 5, 1)
)
hpicfMdnsProfileEntry.setIndexNames(
    (0, "HPICF-MDNS-MIB", "hpicfMdnsProfileName"),
)
if mibBuilder.loadTexts:
    hpicfMdnsProfileEntry.setStatus("current")


class _HpicfMdnsProfileName_Type(DisplayString):
    """Custom type hpicfMdnsProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfMdnsProfileName_Type.__name__ = "DisplayString"
_HpicfMdnsProfileName_Object = MibTableColumn
hpicfMdnsProfileName = _HpicfMdnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 5, 1, 1),
    _HpicfMdnsProfileName_Type()
)
hpicfMdnsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMdnsProfileName.setStatus("current")
_HpicfMdnsProfileRowStatus_Type = RowStatus
_HpicfMdnsProfileRowStatus_Object = MibTableColumn
hpicfMdnsProfileRowStatus = _HpicfMdnsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 5, 1, 2),
    _HpicfMdnsProfileRowStatus_Type()
)
hpicfMdnsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMdnsProfileRowStatus.setStatus("current")
_HpicfMdnsProfileVIDList_Type = VidList
_HpicfMdnsProfileVIDList_Object = MibTableColumn
hpicfMdnsProfileVIDList = _HpicfMdnsProfileVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 5, 1, 3),
    _HpicfMdnsProfileVIDList_Type()
)
hpicfMdnsProfileVIDList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMdnsProfileVIDList.setStatus("current")
_HpicfMdnsProfileRuleTable_Object = MibTable
hpicfMdnsProfileRuleTable = _HpicfMdnsProfileRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleTable.setStatus("current")
_HpicfMdnsProfileRuleEntry_Object = MibTableRow
hpicfMdnsProfileRuleEntry = _HpicfMdnsProfileRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6, 1)
)
hpicfMdnsProfileRuleEntry.setIndexNames(
    (0, "HPICF-MDNS-MIB", "hpicfMdnsProfileName"),
    (0, "HPICF-MDNS-MIB", "hpicfMdnsProfileRuleIndex"),
)
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleEntry.setStatus("current")


class _HpicfMdnsProfileRuleIndex_Type(Integer32):
    """Custom type hpicfMdnsProfileRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_HpicfMdnsProfileRuleIndex_Type.__name__ = "Integer32"
_HpicfMdnsProfileRuleIndex_Object = MibTableColumn
hpicfMdnsProfileRuleIndex = _HpicfMdnsProfileRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6, 1, 1),
    _HpicfMdnsProfileRuleIndex_Type()
)
hpicfMdnsProfileRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleIndex.setStatus("current")


class _HpicfMdnsProfileRuleService_Type(OctetString):
    """Custom type hpicfMdnsProfileRuleService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfMdnsProfileRuleService_Type.__name__ = "OctetString"
_HpicfMdnsProfileRuleService_Object = MibTableColumn
hpicfMdnsProfileRuleService = _HpicfMdnsProfileRuleService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6, 1, 2),
    _HpicfMdnsProfileRuleService_Type()
)
hpicfMdnsProfileRuleService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleService.setStatus("current")


class _HpicfMdnsProfileRuleInstance_Type(OctetString):
    """Custom type hpicfMdnsProfileRuleInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfMdnsProfileRuleInstance_Type.__name__ = "OctetString"
_HpicfMdnsProfileRuleInstance_Object = MibTableColumn
hpicfMdnsProfileRuleInstance = _HpicfMdnsProfileRuleInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6, 1, 3),
    _HpicfMdnsProfileRuleInstance_Type()
)
hpicfMdnsProfileRuleInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleInstance.setStatus("current")


class _HpicfMdnsProfileRuleAction_Type(Integer32):
    """Custom type hpicfMdnsProfileRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_HpicfMdnsProfileRuleAction_Type.__name__ = "Integer32"
_HpicfMdnsProfileRuleAction_Object = MibTableColumn
hpicfMdnsProfileRuleAction = _HpicfMdnsProfileRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6, 1, 4),
    _HpicfMdnsProfileRuleAction_Type()
)
hpicfMdnsProfileRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleAction.setStatus("current")
_HpicfMdnsProfileRuleRowStatus_Type = RowStatus
_HpicfMdnsProfileRuleRowStatus_Object = MibTableColumn
hpicfMdnsProfileRuleRowStatus = _HpicfMdnsProfileRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 1, 6, 1, 5),
    _HpicfMdnsProfileRuleRowStatus_Type()
)
hpicfMdnsProfileRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleRowStatus.setStatus("current")
_HpicfMdnsConformance_ObjectIdentity = ObjectIdentity
hpicfMdnsConformance = _HpicfMdnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2)
)
_HpicfMdnsCompliances_ObjectIdentity = ObjectIdentity
hpicfMdnsCompliances = _HpicfMdnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2, 1)
)
_HpicfMdnsGroups_ObjectIdentity = ObjectIdentity
hpicfMdnsGroups = _HpicfMdnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2, 2)
)

# Managed Objects groups

hpicfMdnsScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2, 2, 1)
)
hpicfMdnsScalarGroup.setObjects(
      *(("HPICF-MDNS-MIB", "hpicfMdnsAdminState"),
        ("HPICF-MDNS-MIB", "hpicfMdnsDefaultFilterInAction"),
        ("HPICF-MDNS-MIB", "hpicfMdnsDefaultFilterOutAction"),
        ("HPICF-MDNS-MIB", "hpicfMdnsGatewayVIDList"))
)
if mibBuilder.loadTexts:
    hpicfMdnsScalarGroup.setStatus("current")

hpicfMdnsProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2, 2, 2)
)
hpicfMdnsProfileGroup.setObjects(
      *(("HPICF-MDNS-MIB", "hpicfMdnsProfileRowStatus"),
        ("HPICF-MDNS-MIB", "hpicfMdnsProfileVIDList"))
)
if mibBuilder.loadTexts:
    hpicfMdnsProfileGroup.setStatus("current")

hpicfMdnsProfileRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2, 2, 3)
)
hpicfMdnsProfileRuleGroup.setObjects(
      *(("HPICF-MDNS-MIB", "hpicfMdnsProfileRuleService"),
        ("HPICF-MDNS-MIB", "hpicfMdnsProfileRuleInstance"),
        ("HPICF-MDNS-MIB", "hpicfMdnsProfileRuleAction"),
        ("HPICF-MDNS-MIB", "hpicfMdnsProfileRuleRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfMdnsProfileRuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfMdnsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfMdnsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-MDNS-MIB",
    **{"hpicfMdns": hpicfMdns,
       "hpicfMdnsNotifications": hpicfMdnsNotifications,
       "hpicfMdnsObjects": hpicfMdnsObjects,
       "hpicfMdnsAdminState": hpicfMdnsAdminState,
       "hpicfMdnsDefaultFilterInAction": hpicfMdnsDefaultFilterInAction,
       "hpicfMdnsDefaultFilterOutAction": hpicfMdnsDefaultFilterOutAction,
       "hpicfMdnsGatewayVIDList": hpicfMdnsGatewayVIDList,
       "hpicfMdnsProfileTable": hpicfMdnsProfileTable,
       "hpicfMdnsProfileEntry": hpicfMdnsProfileEntry,
       "hpicfMdnsProfileName": hpicfMdnsProfileName,
       "hpicfMdnsProfileRowStatus": hpicfMdnsProfileRowStatus,
       "hpicfMdnsProfileVIDList": hpicfMdnsProfileVIDList,
       "hpicfMdnsProfileRuleTable": hpicfMdnsProfileRuleTable,
       "hpicfMdnsProfileRuleEntry": hpicfMdnsProfileRuleEntry,
       "hpicfMdnsProfileRuleIndex": hpicfMdnsProfileRuleIndex,
       "hpicfMdnsProfileRuleService": hpicfMdnsProfileRuleService,
       "hpicfMdnsProfileRuleInstance": hpicfMdnsProfileRuleInstance,
       "hpicfMdnsProfileRuleAction": hpicfMdnsProfileRuleAction,
       "hpicfMdnsProfileRuleRowStatus": hpicfMdnsProfileRuleRowStatus,
       "hpicfMdnsConformance": hpicfMdnsConformance,
       "hpicfMdnsCompliances": hpicfMdnsCompliances,
       "hpicfMdnsCompliance": hpicfMdnsCompliance,
       "hpicfMdnsGroups": hpicfMdnsGroups,
       "hpicfMdnsScalarGroup": hpicfMdnsScalarGroup,
       "hpicfMdnsProfileGroup": hpicfMdnsProfileGroup,
       "hpicfMdnsProfileRuleGroup": hpicfMdnsProfileRuleGroup}
)
