# SNMP MIB module (HP-ICF-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:12 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hpicfSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38)
)
hpicfSnmpMIB.setRevisions(
        ("2008-12-09 00:00",
         "2007-08-24 00:00",
         "2006-11-11 00:00",
         "2006-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSnmpNotification_ObjectIdentity = ObjectIdentity
hpicfSnmpNotification = _HpicfSnmpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 0)
)
_HpicfSnmpObjects_ObjectIdentity = ObjectIdentity
hpicfSnmpObjects = _HpicfSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1)
)
_HpicfSnmpConfig_ObjectIdentity = ObjectIdentity
hpicfSnmpConfig = _HpicfSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1)
)
_HpicfSnmpGlobalCfg_ObjectIdentity = ObjectIdentity
hpicfSnmpGlobalCfg = _HpicfSnmpGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1)
)
_HpicfSnmpResponseSourceAddrPolicyTable_Object = MibTable
hpicfSnmpResponseSourceAddrPolicyTable = _HpicfSnmpResponseSourceAddrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddrPolicyTable.setStatus("current")
_HpicfSnmpResponseSourceAddrPolicyEntry_Object = MibTableRow
hpicfSnmpResponseSourceAddrPolicyEntry = _HpicfSnmpResponseSourceAddrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 1, 1)
)
hpicfSnmpResponseSourceAddrPolicyEntry.setIndexNames(
    (0, "HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddressType"),
)
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddrPolicyEntry.setStatus("current")
_HpicfSnmpResponseSourceAddressType_Type = InetAddressType
_HpicfSnmpResponseSourceAddressType_Object = MibTableColumn
hpicfSnmpResponseSourceAddressType = _HpicfSnmpResponseSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 1, 1, 1),
    _HpicfSnmpResponseSourceAddressType_Type()
)
hpicfSnmpResponseSourceAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddressType.setStatus("current")


class _HpicfSnmpResponseSourceAddrPolicy_Type(Integer32):
    """Custom type hpicfSnmpResponseSourceAddrPolicy based on Integer32"""
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
        *(("configuredIP", 2),
          ("configuredInterface", 3),
          ("dstIpOfRequest", 4),
          ("rfc1517", 1))
    )


_HpicfSnmpResponseSourceAddrPolicy_Type.__name__ = "Integer32"
_HpicfSnmpResponseSourceAddrPolicy_Object = MibTableColumn
hpicfSnmpResponseSourceAddrPolicy = _HpicfSnmpResponseSourceAddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 1, 1, 2),
    _HpicfSnmpResponseSourceAddrPolicy_Type()
)
hpicfSnmpResponseSourceAddrPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddrPolicy.setStatus("current")
_HpicfSnmpResponseSourceAddress_Type = InetAddress
_HpicfSnmpResponseSourceAddress_Object = MibTableColumn
hpicfSnmpResponseSourceAddress = _HpicfSnmpResponseSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 1, 1, 3),
    _HpicfSnmpResponseSourceAddress_Type()
)
hpicfSnmpResponseSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddress.setStatus("current")
_HpicfSnmpResponseSourceAddrIfIndex_Type = InterfaceIndexOrZero
_HpicfSnmpResponseSourceAddrIfIndex_Object = MibTableColumn
hpicfSnmpResponseSourceAddrIfIndex = _HpicfSnmpResponseSourceAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 1, 1, 4),
    _HpicfSnmpResponseSourceAddrIfIndex_Type()
)
hpicfSnmpResponseSourceAddrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddrIfIndex.setStatus("current")
_HpicfSnmpTrapSourceAddrTable_Object = MibTable
hpicfSnmpTrapSourceAddrTable = _HpicfSnmpTrapSourceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddrTable.setStatus("current")
_HpicfSnmpTrapSourceAddrEntry_Object = MibTableRow
hpicfSnmpTrapSourceAddrEntry = _HpicfSnmpTrapSourceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 2, 1)
)
hpicfSnmpTrapSourceAddrEntry.setIndexNames(
    (0, "HP-ICF-SNMP-MIB", "hpicfSnmpTrapSourceAddressType"),
)
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddrEntry.setStatus("current")
_HpicfSnmpTrapSourceAddressType_Type = InetAddressType
_HpicfSnmpTrapSourceAddressType_Object = MibTableColumn
hpicfSnmpTrapSourceAddressType = _HpicfSnmpTrapSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 2, 1, 1),
    _HpicfSnmpTrapSourceAddressType_Type()
)
hpicfSnmpTrapSourceAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddressType.setStatus("current")


class _HpicfSnmpTrapSourceAddrPolicy_Type(Integer32):
    """Custom type hpicfSnmpTrapSourceAddrPolicy based on Integer32"""
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
        *(("configuredIP", 2),
          ("configuredInterface", 3),
          ("dstIpOfRequest", 4),
          ("rfc1517", 1))
    )


_HpicfSnmpTrapSourceAddrPolicy_Type.__name__ = "Integer32"
_HpicfSnmpTrapSourceAddrPolicy_Object = MibTableColumn
hpicfSnmpTrapSourceAddrPolicy = _HpicfSnmpTrapSourceAddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 2, 1, 2),
    _HpicfSnmpTrapSourceAddrPolicy_Type()
)
hpicfSnmpTrapSourceAddrPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddrPolicy.setStatus("current")
_HpicfSnmpTrapSourceAddress_Type = InetAddress
_HpicfSnmpTrapSourceAddress_Object = MibTableColumn
hpicfSnmpTrapSourceAddress = _HpicfSnmpTrapSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 2, 1, 3),
    _HpicfSnmpTrapSourceAddress_Type()
)
hpicfSnmpTrapSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddress.setStatus("current")
_HpicfSnmpTrapSourceAddrIfIndex_Type = InterfaceIndexOrZero
_HpicfSnmpTrapSourceAddrIfIndex_Object = MibTableColumn
hpicfSnmpTrapSourceAddrIfIndex = _HpicfSnmpTrapSourceAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 2, 1, 4),
    _HpicfSnmpTrapSourceAddrIfIndex_Type()
)
hpicfSnmpTrapSourceAddrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddrIfIndex.setStatus("current")


class _HpicfSnmpAuthNotifyEnable_Type(Integer32):
    """Custom type hpicfSnmpAuthNotifyEnable based on Integer32"""
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


_HpicfSnmpAuthNotifyEnable_Type.__name__ = "Integer32"
_HpicfSnmpAuthNotifyEnable_Object = MibScalar
hpicfSnmpAuthNotifyEnable = _HpicfSnmpAuthNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 1, 1, 3),
    _HpicfSnmpAuthNotifyEnable_Type()
)
hpicfSnmpAuthNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSnmpAuthNotifyEnable.setStatus("current")
_HpicfSnmpNotificationObjects_ObjectIdentity = ObjectIdentity
hpicfSnmpNotificationObjects = _HpicfSnmpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 2)
)
_HpicfSnmpAuthFailCount_Type = Counter32
_HpicfSnmpAuthFailCount_Object = MibScalar
hpicfSnmpAuthFailCount = _HpicfSnmpAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 2, 1),
    _HpicfSnmpAuthFailCount_Type()
)
hpicfSnmpAuthFailCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSnmpAuthFailCount.setStatus("current")
_HpicfSnmpAuthFailIPType_Type = InetAddressType
_HpicfSnmpAuthFailIPType_Object = MibScalar
hpicfSnmpAuthFailIPType = _HpicfSnmpAuthFailIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 2, 2),
    _HpicfSnmpAuthFailIPType_Type()
)
hpicfSnmpAuthFailIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSnmpAuthFailIPType.setStatus("current")
_HpicfSnmpAuthFailIP_Type = InetAddress
_HpicfSnmpAuthFailIP_Object = MibScalar
hpicfSnmpAuthFailIP = _HpicfSnmpAuthFailIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 1, 2, 3),
    _HpicfSnmpAuthFailIP_Type()
)
hpicfSnmpAuthFailIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSnmpAuthFailIP.setStatus("current")
_HpicfSnmpConformance_ObjectIdentity = ObjectIdentity
hpicfSnmpConformance = _HpicfSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2)
)
_HpicfSnmpCompliances_ObjectIdentity = ObjectIdentity
hpicfSnmpCompliances = _HpicfSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 1)
)
_HpicfSnmpCompliancesGroups_ObjectIdentity = ObjectIdentity
hpicfSnmpCompliancesGroups = _HpicfSnmpCompliancesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2)
)

# Managed Objects groups

hpicfSnmpResponseSourceAddrTableCompliancesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2, 1)
)
hpicfSnmpResponseSourceAddrTableCompliancesGroup.setObjects(
      *(("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddressType"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddrPolicy"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddress"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddrIfIndex"))
)
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddrTableCompliancesGroup.setStatus("current")

hpicfSnmpTrapSourceAddrTableCompliancesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2, 2)
)
hpicfSnmpTrapSourceAddrTableCompliancesGroup.setObjects(
      *(("HP-ICF-SNMP-MIB", "hpicfSnmpTrapSourceAddressType"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpTrapSourceAddrPolicy"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpTrapSourceAddress"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpTrapSourceAddrIfIndex"))
)
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddrTableCompliancesGroup.setStatus("current")

hpicfSnmpResponseSourceAddrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2, 3)
)
hpicfSnmpResponseSourceAddrTableGroup.setObjects(
      *(("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddressType"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddrPolicy"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddress"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddrIfIndex"))
)
if mibBuilder.loadTexts:
    hpicfSnmpResponseSourceAddrTableGroup.setStatus("current")

hpicfSnmpTrapSourceAddrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2, 4)
)
hpicfSnmpTrapSourceAddrTableGroup.setObjects(
      *(("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddressType"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddrPolicy"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddress"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpResponseSourceAddrIfIndex"))
)
if mibBuilder.loadTexts:
    hpicfSnmpTrapSourceAddrTableGroup.setStatus("current")

hpicfSnmpNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2, 5)
)
hpicfSnmpNotifyObjectGroup.setObjects(
      *(("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFailCount"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFailIPType"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFailIP"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpAuthNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpicfSnmpNotifyObjectGroup.setStatus("current")


# Notification objects

hpicfSnmpAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 0, 1)
)
hpicfSnmpAuthFail.setObjects(
      *(("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFailCount"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFailIPType"),
        ("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFailIP"))
)
if mibBuilder.loadTexts:
    hpicfSnmpAuthFail.setStatus(
        "current"
    )


# Notifications groups

hpicfSnmpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 2, 6)
)
hpicfSnmpNotificationGroup.setObjects(
    ("HP-ICF-SNMP-MIB", "hpicfSnmpAuthFail")
)
if mibBuilder.loadTexts:
    hpicfSnmpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfSnmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSnmpCompliance.setStatus(
        "current"
    )

hpicfSnmpCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfSnmpCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SNMP-MIB",
    **{"hpicfSnmpMIB": hpicfSnmpMIB,
       "hpicfSnmpNotification": hpicfSnmpNotification,
       "hpicfSnmpAuthFail": hpicfSnmpAuthFail,
       "hpicfSnmpObjects": hpicfSnmpObjects,
       "hpicfSnmpConfig": hpicfSnmpConfig,
       "hpicfSnmpGlobalCfg": hpicfSnmpGlobalCfg,
       "hpicfSnmpResponseSourceAddrPolicyTable": hpicfSnmpResponseSourceAddrPolicyTable,
       "hpicfSnmpResponseSourceAddrPolicyEntry": hpicfSnmpResponseSourceAddrPolicyEntry,
       "hpicfSnmpResponseSourceAddressType": hpicfSnmpResponseSourceAddressType,
       "hpicfSnmpResponseSourceAddrPolicy": hpicfSnmpResponseSourceAddrPolicy,
       "hpicfSnmpResponseSourceAddress": hpicfSnmpResponseSourceAddress,
       "hpicfSnmpResponseSourceAddrIfIndex": hpicfSnmpResponseSourceAddrIfIndex,
       "hpicfSnmpTrapSourceAddrTable": hpicfSnmpTrapSourceAddrTable,
       "hpicfSnmpTrapSourceAddrEntry": hpicfSnmpTrapSourceAddrEntry,
       "hpicfSnmpTrapSourceAddressType": hpicfSnmpTrapSourceAddressType,
       "hpicfSnmpTrapSourceAddrPolicy": hpicfSnmpTrapSourceAddrPolicy,
       "hpicfSnmpTrapSourceAddress": hpicfSnmpTrapSourceAddress,
       "hpicfSnmpTrapSourceAddrIfIndex": hpicfSnmpTrapSourceAddrIfIndex,
       "hpicfSnmpAuthNotifyEnable": hpicfSnmpAuthNotifyEnable,
       "hpicfSnmpNotificationObjects": hpicfSnmpNotificationObjects,
       "hpicfSnmpAuthFailCount": hpicfSnmpAuthFailCount,
       "hpicfSnmpAuthFailIPType": hpicfSnmpAuthFailIPType,
       "hpicfSnmpAuthFailIP": hpicfSnmpAuthFailIP,
       "hpicfSnmpConformance": hpicfSnmpConformance,
       "hpicfSnmpCompliances": hpicfSnmpCompliances,
       "hpicfSnmpCompliance": hpicfSnmpCompliance,
       "hpicfSnmpCompliance1": hpicfSnmpCompliance1,
       "hpicfSnmpCompliancesGroups": hpicfSnmpCompliancesGroups,
       "hpicfSnmpResponseSourceAddrTableCompliancesGroup": hpicfSnmpResponseSourceAddrTableCompliancesGroup,
       "hpicfSnmpTrapSourceAddrTableCompliancesGroup": hpicfSnmpTrapSourceAddrTableCompliancesGroup,
       "hpicfSnmpResponseSourceAddrTableGroup": hpicfSnmpResponseSourceAddrTableGroup,
       "hpicfSnmpTrapSourceAddrTableGroup": hpicfSnmpTrapSourceAddrTableGroup,
       "hpicfSnmpNotifyObjectGroup": hpicfSnmpNotifyObjectGroup,
       "hpicfSnmpNotificationGroup": hpicfSnmpNotificationGroup}
)
