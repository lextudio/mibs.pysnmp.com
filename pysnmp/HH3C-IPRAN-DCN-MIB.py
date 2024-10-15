# SNMP MIB module (HH3C-IPRAN-DCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IPRAN-DCN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:37 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cIpRanDcn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152)
)
hh3cIpRanDcn.setRevisions(
        ("2013-07-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cIpRanNeId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cIpRanDcnMIB_ObjectIdentity = ObjectIdentity
hh3cIpRanDcnMIB = _Hh3cIpRanDcnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1)
)
_Hh3cIpRanDcnObjects_ObjectIdentity = ObjectIdentity
hh3cIpRanDcnObjects = _Hh3cIpRanDcnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1)
)
_Hh3cIpRanDcnInfoObject_ObjectIdentity = ObjectIdentity
hh3cIpRanDcnInfoObject = _Hh3cIpRanDcnInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 1)
)
_Hh3cIpRanDcnNeId_Type = Hh3cIpRanNeId
_Hh3cIpRanDcnNeId_Object = MibScalar
hh3cIpRanDcnNeId = _Hh3cIpRanDcnNeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 1, 1),
    _Hh3cIpRanDcnNeId_Type()
)
hh3cIpRanDcnNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeId.setStatus("current")
_Hh3cIpRanDcnNeIpType_Type = InetAddressType
_Hh3cIpRanDcnNeIpType_Object = MibScalar
hh3cIpRanDcnNeIpType = _Hh3cIpRanDcnNeIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 1, 2),
    _Hh3cIpRanDcnNeIpType_Type()
)
hh3cIpRanDcnNeIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeIpType.setStatus("current")
_Hh3cIpRanDcnNeIp_Type = InetAddress
_Hh3cIpRanDcnNeIp_Object = MibScalar
hh3cIpRanDcnNeIp = _Hh3cIpRanDcnNeIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 1, 3),
    _Hh3cIpRanDcnNeIp_Type()
)
hh3cIpRanDcnNeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeIp.setStatus("current")
_Hh3cIpRanDcnMask_Type = InetAddress
_Hh3cIpRanDcnMask_Object = MibScalar
hh3cIpRanDcnMask = _Hh3cIpRanDcnMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 1, 4),
    _Hh3cIpRanDcnMask_Type()
)
hh3cIpRanDcnMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnMask.setStatus("current")
_Hh3cIpRanDcnNeInfoTable_Object = MibTable
hh3cIpRanDcnNeInfoTable = _Hh3cIpRanDcnNeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoTable.setStatus("current")
_Hh3cIpRanDcnNeInfoEntry_Object = MibTableRow
hh3cIpRanDcnNeInfoEntry = _Hh3cIpRanDcnNeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2, 1)
)
hh3cIpRanDcnNeInfoEntry.setIndexNames(
    (0, "HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeId"),
)
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoEntry.setStatus("current")
_Hh3cIpRanDcnNeInfoNeId_Type = Hh3cIpRanNeId
_Hh3cIpRanDcnNeInfoNeId_Object = MibTableColumn
hh3cIpRanDcnNeInfoNeId = _Hh3cIpRanDcnNeInfoNeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2, 1, 1),
    _Hh3cIpRanDcnNeInfoNeId_Type()
)
hh3cIpRanDcnNeInfoNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoNeId.setStatus("current")
_Hh3cIpRanDcnNeInfoNeIpType_Type = InetAddressType
_Hh3cIpRanDcnNeInfoNeIpType_Object = MibTableColumn
hh3cIpRanDcnNeInfoNeIpType = _Hh3cIpRanDcnNeInfoNeIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2, 1, 2),
    _Hh3cIpRanDcnNeInfoNeIpType_Type()
)
hh3cIpRanDcnNeInfoNeIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoNeIpType.setStatus("current")
_Hh3cIpRanDcnNeInfoNeIp_Type = InetAddress
_Hh3cIpRanDcnNeInfoNeIp_Object = MibTableColumn
hh3cIpRanDcnNeInfoNeIp = _Hh3cIpRanDcnNeInfoNeIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2, 1, 3),
    _Hh3cIpRanDcnNeInfoNeIp_Type()
)
hh3cIpRanDcnNeInfoNeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoNeIp.setStatus("current")
_Hh3cIpRanDcnNeInfoMetric_Type = Integer32
_Hh3cIpRanDcnNeInfoMetric_Object = MibTableColumn
hh3cIpRanDcnNeInfoMetric = _Hh3cIpRanDcnNeInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2, 1, 4),
    _Hh3cIpRanDcnNeInfoMetric_Type()
)
hh3cIpRanDcnNeInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoMetric.setStatus("current")


class _Hh3cIpRanDcnNeInfoDeviceType_Type(DisplayString):
    """Custom type hh3cIpRanDcnNeInfoDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIpRanDcnNeInfoDeviceType_Type.__name__ = "DisplayString"
_Hh3cIpRanDcnNeInfoDeviceType_Object = MibTableColumn
hh3cIpRanDcnNeInfoDeviceType = _Hh3cIpRanDcnNeInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 1, 2, 1, 5),
    _Hh3cIpRanDcnNeInfoDeviceType_Type()
)
hh3cIpRanDcnNeInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeInfoDeviceType.setStatus("current")
_Hh3cIpRanDcnTrapObjects_ObjectIdentity = ObjectIdentity
hh3cIpRanDcnTrapObjects = _Hh3cIpRanDcnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 2)
)
_Hh3cIpRanDcnNeNumber_Type = Integer32
_Hh3cIpRanDcnNeNumber_Object = MibScalar
hh3cIpRanDcnNeNumber = _Hh3cIpRanDcnNeNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 2, 1),
    _Hh3cIpRanDcnNeNumber_Type()
)
hh3cIpRanDcnNeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeNumber.setStatus("current")


class _Hh3cIpRanDcnNeChangeMode_Type(Integer32):
    """Custom type hh3cIpRanDcnNeChangeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_Hh3cIpRanDcnNeChangeMode_Type.__name__ = "Integer32"
_Hh3cIpRanDcnNeChangeMode_Object = MibScalar
hh3cIpRanDcnNeChangeMode = _Hh3cIpRanDcnNeChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 2, 2),
    _Hh3cIpRanDcnNeChangeMode_Type()
)
hh3cIpRanDcnNeChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeChangeMode.setStatus("current")


class _Hh3cIpRanDcnCompanyName_Type(DisplayString):
    """Custom type hh3cIpRanDcnCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIpRanDcnCompanyName_Type.__name__ = "DisplayString"
_Hh3cIpRanDcnCompanyName_Object = MibScalar
hh3cIpRanDcnCompanyName = _Hh3cIpRanDcnCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 2, 3),
    _Hh3cIpRanDcnCompanyName_Type()
)
hh3cIpRanDcnCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnCompanyName.setStatus("current")


class _Hh3cIpRanDcnDeviceType_Type(DisplayString):
    """Custom type hh3cIpRanDcnDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIpRanDcnDeviceType_Type.__name__ = "DisplayString"
_Hh3cIpRanDcnDeviceType_Object = MibScalar
hh3cIpRanDcnDeviceType = _Hh3cIpRanDcnDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 2, 4),
    _Hh3cIpRanDcnDeviceType_Type()
)
hh3cIpRanDcnDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnDeviceType.setStatus("current")
_Hh3cIpRanDcnDeviceMac_Type = MacAddress
_Hh3cIpRanDcnDeviceMac_Object = MibScalar
hh3cIpRanDcnDeviceMac = _Hh3cIpRanDcnDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 2, 5),
    _Hh3cIpRanDcnDeviceMac_Type()
)
hh3cIpRanDcnDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpRanDcnDeviceMac.setStatus("current")
_Hh3cIpRanDcnTraps_ObjectIdentity = ObjectIdentity
hh3cIpRanDcnTraps = _Hh3cIpRanDcnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 3)
)
_Hh3cIpRanDcnTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cIpRanDcnTrapsPrefix = _Hh3cIpRanDcnTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cIpRanDcnNeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 3, 0, 1)
)
hh3cIpRanDcnNeOnline.setObjects(
      *(("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeId"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeIpType"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeIp"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnCompanyName"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnDeviceType"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnDeviceMac"))
)
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeOnline.setStatus(
        "current"
    )

hh3cIpRanDcnNeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152, 1, 3, 0, 2)
)
hh3cIpRanDcnNeOffline.setObjects(
      *(("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeId"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeIpType"),
        ("HH3C-IPRAN-DCN-MIB", "hh3cIpRanDcnNeInfoNeIp"))
)
if mibBuilder.loadTexts:
    hh3cIpRanDcnNeOffline.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IPRAN-DCN-MIB",
    **{"Hh3cIpRanNeId": Hh3cIpRanNeId,
       "hh3cIpRanDcn": hh3cIpRanDcn,
       "hh3cIpRanDcnMIB": hh3cIpRanDcnMIB,
       "hh3cIpRanDcnObjects": hh3cIpRanDcnObjects,
       "hh3cIpRanDcnInfoObject": hh3cIpRanDcnInfoObject,
       "hh3cIpRanDcnNeId": hh3cIpRanDcnNeId,
       "hh3cIpRanDcnNeIpType": hh3cIpRanDcnNeIpType,
       "hh3cIpRanDcnNeIp": hh3cIpRanDcnNeIp,
       "hh3cIpRanDcnMask": hh3cIpRanDcnMask,
       "hh3cIpRanDcnNeInfoTable": hh3cIpRanDcnNeInfoTable,
       "hh3cIpRanDcnNeInfoEntry": hh3cIpRanDcnNeInfoEntry,
       "hh3cIpRanDcnNeInfoNeId": hh3cIpRanDcnNeInfoNeId,
       "hh3cIpRanDcnNeInfoNeIpType": hh3cIpRanDcnNeInfoNeIpType,
       "hh3cIpRanDcnNeInfoNeIp": hh3cIpRanDcnNeInfoNeIp,
       "hh3cIpRanDcnNeInfoMetric": hh3cIpRanDcnNeInfoMetric,
       "hh3cIpRanDcnNeInfoDeviceType": hh3cIpRanDcnNeInfoDeviceType,
       "hh3cIpRanDcnTrapObjects": hh3cIpRanDcnTrapObjects,
       "hh3cIpRanDcnNeNumber": hh3cIpRanDcnNeNumber,
       "hh3cIpRanDcnNeChangeMode": hh3cIpRanDcnNeChangeMode,
       "hh3cIpRanDcnCompanyName": hh3cIpRanDcnCompanyName,
       "hh3cIpRanDcnDeviceType": hh3cIpRanDcnDeviceType,
       "hh3cIpRanDcnDeviceMac": hh3cIpRanDcnDeviceMac,
       "hh3cIpRanDcnTraps": hh3cIpRanDcnTraps,
       "hh3cIpRanDcnTrapsPrefix": hh3cIpRanDcnTrapsPrefix,
       "hh3cIpRanDcnNeOnline": hh3cIpRanDcnNeOnline,
       "hh3cIpRanDcnNeOffline": hh3cIpRanDcnNeOffline}
)
