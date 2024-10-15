# SNMP MIB module (A3COM-HUAWEI-NET-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-NET-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:42 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cNetMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90)
)
h3cNetMan.setRevisions(
        ("2008-04-16 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cNMConfigObjects_ObjectIdentity = ObjectIdentity
h3cNMConfigObjects = _H3cNMConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 1)
)
_H3cNMMonitorObjects_ObjectIdentity = ObjectIdentity
h3cNMMonitorObjects = _H3cNMMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 2)
)
_H3cNMNotify_ObjectIdentity = ObjectIdentity
h3cNMNotify = _H3cNMNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3)
)
_H3cNMNotifyScalarObjects_ObjectIdentity = ObjectIdentity
h3cNMNotifyScalarObjects = _H3cNMNotifyScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1)
)
_H3cNMIpAddressType_Type = InetAddressType
_H3cNMIpAddressType_Object = MibScalar
h3cNMIpAddressType = _H3cNMIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 1),
    _H3cNMIpAddressType_Type()
)
h3cNMIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cNMIpAddressType.setStatus("current")
_H3cNMIpAddress_Type = InetAddress
_H3cNMIpAddress_Object = MibScalar
h3cNMIpAddress = _H3cNMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 2),
    _H3cNMIpAddress_Type()
)
h3cNMIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cNMIpAddress.setStatus("current")


class _H3cNMCustomBuildInfo_Type(OctetString):
    """Custom type h3cNMCustomBuildInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cNMCustomBuildInfo_Type.__name__ = "OctetString"
_H3cNMCustomBuildInfo_Object = MibScalar
h3cNMCustomBuildInfo = _H3cNMCustomBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 3),
    _H3cNMCustomBuildInfo_Type()
)
h3cNMCustomBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNMCustomBuildInfo.setStatus("current")


class _H3cNMSerialNum_Type(OctetString):
    """Custom type h3cNMSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cNMSerialNum_Type.__name__ = "OctetString"
_H3cNMSerialNum_Object = MibScalar
h3cNMSerialNum = _H3cNMSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 4),
    _H3cNMSerialNum_Type()
)
h3cNMSerialNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cNMSerialNum.setStatus("current")
_H3cNMNotifyObjects_ObjectIdentity = ObjectIdentity
h3cNMNotifyObjects = _H3cNMNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 2)
)
_H3cNMNotifyObjectsPrefix_ObjectIdentity = ObjectIdentity
h3cNMNotifyObjectsPrefix = _H3cNMNotifyObjectsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 2, 0)
)
_H3cNetManConformance_ObjectIdentity = ObjectIdentity
h3cNetManConformance = _H3cNetManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4)
)
_H3cNetManCompliances_ObjectIdentity = ObjectIdentity
h3cNetManCompliances = _H3cNetManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 1)
)
_H3cNetManGroups_ObjectIdentity = ObjectIdentity
h3cNetManGroups = _H3cNetManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 2)
)

# Managed Objects groups

h3cNMMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 2, 1)
)
h3cNMMonitorGroup.setObjects(
      *(("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddressType"),
        ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddress"),
        ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMCustomBuildInfo"),
        ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMSerialNum"))
)
if mibBuilder.loadTexts:
    h3cNMMonitorGroup.setStatus("current")


# Notification objects

h3cIpAddrChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 2, 0, 1)
)
h3cIpAddrChangeNotify.setObjects(
      *(("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddressType"),
        ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddress"),
        ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMCustomBuildInfo"),
        ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMSerialNum"))
)
if mibBuilder.loadTexts:
    h3cIpAddrChangeNotify.setStatus(
        "current"
    )


# Notifications groups

h3cNMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 2, 2)
)
h3cNMNotificationGroup.setObjects(
    ("A3COM-HUAWEI-NET-MAN-MIB", "h3cIpAddrChangeNotify")
)
if mibBuilder.loadTexts:
    h3cNMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cNetManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cNetManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-NET-MAN-MIB",
    **{"h3cNetMan": h3cNetMan,
       "h3cNMConfigObjects": h3cNMConfigObjects,
       "h3cNMMonitorObjects": h3cNMMonitorObjects,
       "h3cNMNotify": h3cNMNotify,
       "h3cNMNotifyScalarObjects": h3cNMNotifyScalarObjects,
       "h3cNMIpAddressType": h3cNMIpAddressType,
       "h3cNMIpAddress": h3cNMIpAddress,
       "h3cNMCustomBuildInfo": h3cNMCustomBuildInfo,
       "h3cNMSerialNum": h3cNMSerialNum,
       "h3cNMNotifyObjects": h3cNMNotifyObjects,
       "h3cNMNotifyObjectsPrefix": h3cNMNotifyObjectsPrefix,
       "h3cIpAddrChangeNotify": h3cIpAddrChangeNotify,
       "h3cNetManConformance": h3cNetManConformance,
       "h3cNetManCompliances": h3cNetManCompliances,
       "h3cNetManCompliance": h3cNetManCompliance,
       "h3cNetManGroups": h3cNetManGroups,
       "h3cNMMonitorGroup": h3cNMMonitorGroup,
       "h3cNMNotificationGroup": h3cNMNotificationGroup}
)
