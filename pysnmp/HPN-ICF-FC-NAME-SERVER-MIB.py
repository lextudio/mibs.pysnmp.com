# SNMP MIB module (HPN-ICF-FC-NAME-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FC-NAME-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:16 2024
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

(HpnicfFcNameId,) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcNameId")

(hpnicfSan,
 hpnicfVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan",
    "hpnicfVsanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfFcNameServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10)
)
hpnicfFcNameServer.setRevisions(
        ("2014-03-03 10:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFcNameServerMibObjects_ObjectIdentity = ObjectIdentity
hpnicfFcNameServerMibObjects = _HpnicfFcNameServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1)
)
_HpnicfFcNsNotification_ObjectIdentity = ObjectIdentity
hpnicfFcNsNotification = _HpnicfFcNsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1)
)
_HpnicfFcNsNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfFcNsNotificationPrefix = _HpnicfFcNsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 0)
)
_HpnicfFcNsNotificationSwitch_ObjectIdentity = ObjectIdentity
hpnicfFcNsNotificationSwitch = _HpnicfFcNsNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 1)
)
_HpnicfFcNsPortLoginNotifyEnable_Type = TruthValue
_HpnicfFcNsPortLoginNotifyEnable_Object = MibScalar
hpnicfFcNsPortLoginNotifyEnable = _HpnicfFcNsPortLoginNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 1, 1),
    _HpnicfFcNsPortLoginNotifyEnable_Type()
)
hpnicfFcNsPortLoginNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcNsPortLoginNotifyEnable.setStatus("current")
_HpnicfFcNsPortLogoutNotifyEnable_Type = TruthValue
_HpnicfFcNsPortLogoutNotifyEnable_Object = MibScalar
hpnicfFcNsPortLogoutNotifyEnable = _HpnicfFcNsPortLogoutNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 1, 2),
    _HpnicfFcNsPortLogoutNotifyEnable_Type()
)
hpnicfFcNsPortLogoutNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcNsPortLogoutNotifyEnable.setStatus("current")
_HpnicfFcNsObjsForNotification_ObjectIdentity = ObjectIdentity
hpnicfFcNsObjsForNotification = _HpnicfFcNsObjsForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 2)
)
_HpnicfFcNsLocalSwitchWWN_Type = HpnicfFcNameId
_HpnicfFcNsLocalSwitchWWN_Object = MibScalar
hpnicfFcNsLocalSwitchWWN = _HpnicfFcNsLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 2, 1),
    _HpnicfFcNsLocalSwitchWWN_Type()
)
hpnicfFcNsLocalSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcNsLocalSwitchWWN.setStatus("current")
_HpnicfFcNsFloginPortWWN_Type = HpnicfFcNameId
_HpnicfFcNsFloginPortWWN_Object = MibScalar
hpnicfFcNsFloginPortWWN = _HpnicfFcNsFloginPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 2, 2),
    _HpnicfFcNsFloginPortWWN_Type()
)
hpnicfFcNsFloginPortWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcNsFloginPortWWN.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfFcNsPortLoginNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 0, 1)
)
hpnicfFcNsPortLoginNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-NAME-SERVER-MIB", "hpnicfFcNsLocalSwitchWWN"),
        ("HPN-ICF-FC-NAME-SERVER-MIB", "hpnicfFcNsFloginPortWWN"))
)
if mibBuilder.loadTexts:
    hpnicfFcNsPortLoginNotify.setStatus(
        "current"
    )

hpnicfFcNsPortLogoutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 10, 1, 1, 0, 2)
)
hpnicfFcNsPortLogoutNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-NAME-SERVER-MIB", "hpnicfFcNsLocalSwitchWWN"),
        ("HPN-ICF-FC-NAME-SERVER-MIB", "hpnicfFcNsFloginPortWWN"))
)
if mibBuilder.loadTexts:
    hpnicfFcNsPortLogoutNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FC-NAME-SERVER-MIB",
    **{"hpnicfFcNameServer": hpnicfFcNameServer,
       "hpnicfFcNameServerMibObjects": hpnicfFcNameServerMibObjects,
       "hpnicfFcNsNotification": hpnicfFcNsNotification,
       "hpnicfFcNsNotificationPrefix": hpnicfFcNsNotificationPrefix,
       "hpnicfFcNsPortLoginNotify": hpnicfFcNsPortLoginNotify,
       "hpnicfFcNsPortLogoutNotify": hpnicfFcNsPortLogoutNotify,
       "hpnicfFcNsNotificationSwitch": hpnicfFcNsNotificationSwitch,
       "hpnicfFcNsPortLoginNotifyEnable": hpnicfFcNsPortLoginNotifyEnable,
       "hpnicfFcNsPortLogoutNotifyEnable": hpnicfFcNsPortLogoutNotifyEnable,
       "hpnicfFcNsObjsForNotification": hpnicfFcNsObjsForNotification,
       "hpnicfFcNsLocalSwitchWWN": hpnicfFcNsLocalSwitchWWN,
       "hpnicfFcNsFloginPortWWN": hpnicfFcNsFloginPortWWN}
)
