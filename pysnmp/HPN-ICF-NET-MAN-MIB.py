# SNMP MIB module (HPN-ICF-NET-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NET-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:18 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfNetMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90)
)
hpnicfNetMan.setRevisions(
        ("2008-04-16 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfNMConfigObjects_ObjectIdentity = ObjectIdentity
hpnicfNMConfigObjects = _HpnicfNMConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 1)
)
_HpnicfNMMonitorObjects_ObjectIdentity = ObjectIdentity
hpnicfNMMonitorObjects = _HpnicfNMMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 2)
)
_HpnicfNMNotify_ObjectIdentity = ObjectIdentity
hpnicfNMNotify = _HpnicfNMNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3)
)
_HpnicfNMNotifyScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfNMNotifyScalarObjects = _HpnicfNMNotifyScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1)
)
_HpnicfNMIpAddressType_Type = InetAddressType
_HpnicfNMIpAddressType_Object = MibScalar
hpnicfNMIpAddressType = _HpnicfNMIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 1),
    _HpnicfNMIpAddressType_Type()
)
hpnicfNMIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNMIpAddressType.setStatus("current")
_HpnicfNMIpAddress_Type = InetAddress
_HpnicfNMIpAddress_Object = MibScalar
hpnicfNMIpAddress = _HpnicfNMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 2),
    _HpnicfNMIpAddress_Type()
)
hpnicfNMIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNMIpAddress.setStatus("current")


class _HpnicfNMCustomBuildInfo_Type(OctetString):
    """Custom type hpnicfNMCustomBuildInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfNMCustomBuildInfo_Type.__name__ = "OctetString"
_HpnicfNMCustomBuildInfo_Object = MibScalar
hpnicfNMCustomBuildInfo = _HpnicfNMCustomBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 3),
    _HpnicfNMCustomBuildInfo_Type()
)
hpnicfNMCustomBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNMCustomBuildInfo.setStatus("current")


class _HpnicfNMSerialNum_Type(OctetString):
    """Custom type hpnicfNMSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfNMSerialNum_Type.__name__ = "OctetString"
_HpnicfNMSerialNum_Object = MibScalar
hpnicfNMSerialNum = _HpnicfNMSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 4),
    _HpnicfNMSerialNum_Type()
)
hpnicfNMSerialNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNMSerialNum.setStatus("current")
_HpnicfNMNotifyObjects_ObjectIdentity = ObjectIdentity
hpnicfNMNotifyObjects = _HpnicfNMNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2)
)
_HpnicfNMNotifyObjectsPrefix_ObjectIdentity = ObjectIdentity
hpnicfNMNotifyObjectsPrefix = _HpnicfNMNotifyObjectsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2, 0)
)
_HpnicfNetManConformance_ObjectIdentity = ObjectIdentity
hpnicfNetManConformance = _HpnicfNetManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4)
)
_HpnicfNetManCompliances_ObjectIdentity = ObjectIdentity
hpnicfNetManCompliances = _HpnicfNetManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 1)
)
_HpnicfNetManGroups_ObjectIdentity = ObjectIdentity
hpnicfNetManGroups = _HpnicfNetManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2)
)

# Managed Objects groups

hpnicfNMMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2, 1)
)
hpnicfNMMonitorGroup.setObjects(
      *(("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddressType"),
        ("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddress"),
        ("HPN-ICF-NET-MAN-MIB", "hpnicfNMCustomBuildInfo"),
        ("HPN-ICF-NET-MAN-MIB", "hpnicfNMSerialNum"))
)
if mibBuilder.loadTexts:
    hpnicfNMMonitorGroup.setStatus("current")


# Notification objects

hpnicfIpAddrChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2, 0, 1)
)
hpnicfIpAddrChangeNotify.setObjects(
      *(("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddressType"),
        ("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddress"),
        ("HPN-ICF-NET-MAN-MIB", "hpnicfNMCustomBuildInfo"),
        ("HPN-ICF-NET-MAN-MIB", "hpnicfNMSerialNum"))
)
if mibBuilder.loadTexts:
    hpnicfIpAddrChangeNotify.setStatus(
        "current"
    )


# Notifications groups

hpnicfNMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2, 2)
)
hpnicfNMNotificationGroup.setObjects(
    ("HPN-ICF-NET-MAN-MIB", "hpnicfIpAddrChangeNotify")
)
if mibBuilder.loadTexts:
    hpnicfNMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfNetManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfNetManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NET-MAN-MIB",
    **{"hpnicfNetMan": hpnicfNetMan,
       "hpnicfNMConfigObjects": hpnicfNMConfigObjects,
       "hpnicfNMMonitorObjects": hpnicfNMMonitorObjects,
       "hpnicfNMNotify": hpnicfNMNotify,
       "hpnicfNMNotifyScalarObjects": hpnicfNMNotifyScalarObjects,
       "hpnicfNMIpAddressType": hpnicfNMIpAddressType,
       "hpnicfNMIpAddress": hpnicfNMIpAddress,
       "hpnicfNMCustomBuildInfo": hpnicfNMCustomBuildInfo,
       "hpnicfNMSerialNum": hpnicfNMSerialNum,
       "hpnicfNMNotifyObjects": hpnicfNMNotifyObjects,
       "hpnicfNMNotifyObjectsPrefix": hpnicfNMNotifyObjectsPrefix,
       "hpnicfIpAddrChangeNotify": hpnicfIpAddrChangeNotify,
       "hpnicfNetManConformance": hpnicfNetManConformance,
       "hpnicfNetManCompliances": hpnicfNetManCompliances,
       "hpnicfNetManCompliance": hpnicfNetManCompliance,
       "hpnicfNetManGroups": hpnicfNetManGroups,
       "hpnicfNMMonitorGroup": hpnicfNMMonitorGroup,
       "hpnicfNMNotificationGroup": hpnicfNMNotificationGroup}
)
