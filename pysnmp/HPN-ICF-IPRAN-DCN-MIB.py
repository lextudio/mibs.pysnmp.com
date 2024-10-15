# SNMP MIB module (HPN-ICF-IPRAN-DCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IPRAN-DCN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:37 2024
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

hpnicfIpRanDcn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152)
)
hpnicfIpRanDcn.setRevisions(
        ("2013-07-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfIpRanNeId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfIpRanDcnMIB_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcnMIB = _HpnicfIpRanDcnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1)
)
_HpnicfIpRanDcnObjects_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcnObjects = _HpnicfIpRanDcnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1)
)
_HpnicfIpRanDcnInfoObject_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcnInfoObject = _HpnicfIpRanDcnInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 1)
)
_HpnicfIpRanDcnNeId_Type = HpnicfIpRanNeId
_HpnicfIpRanDcnNeId_Object = MibScalar
hpnicfIpRanDcnNeId = _HpnicfIpRanDcnNeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 1, 1),
    _HpnicfIpRanDcnNeId_Type()
)
hpnicfIpRanDcnNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeId.setStatus("current")
_HpnicfIpRanDcnNeIpType_Type = InetAddressType
_HpnicfIpRanDcnNeIpType_Object = MibScalar
hpnicfIpRanDcnNeIpType = _HpnicfIpRanDcnNeIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 1, 2),
    _HpnicfIpRanDcnNeIpType_Type()
)
hpnicfIpRanDcnNeIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeIpType.setStatus("current")
_HpnicfIpRanDcnNeIp_Type = InetAddress
_HpnicfIpRanDcnNeIp_Object = MibScalar
hpnicfIpRanDcnNeIp = _HpnicfIpRanDcnNeIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 1, 3),
    _HpnicfIpRanDcnNeIp_Type()
)
hpnicfIpRanDcnNeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeIp.setStatus("current")
_HpnicfIpRanDcnMask_Type = InetAddress
_HpnicfIpRanDcnMask_Object = MibScalar
hpnicfIpRanDcnMask = _HpnicfIpRanDcnMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 1, 4),
    _HpnicfIpRanDcnMask_Type()
)
hpnicfIpRanDcnMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnMask.setStatus("current")
_HpnicfIpRanDcnNeInfoTable_Object = MibTable
hpnicfIpRanDcnNeInfoTable = _HpnicfIpRanDcnNeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoTable.setStatus("current")
_HpnicfIpRanDcnNeInfoEntry_Object = MibTableRow
hpnicfIpRanDcnNeInfoEntry = _HpnicfIpRanDcnNeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2, 1)
)
hpnicfIpRanDcnNeInfoEntry.setIndexNames(
    (0, "HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeId"),
)
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoEntry.setStatus("current")
_HpnicfIpRanDcnNeInfoNeId_Type = HpnicfIpRanNeId
_HpnicfIpRanDcnNeInfoNeId_Object = MibTableColumn
hpnicfIpRanDcnNeInfoNeId = _HpnicfIpRanDcnNeInfoNeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2, 1, 1),
    _HpnicfIpRanDcnNeInfoNeId_Type()
)
hpnicfIpRanDcnNeInfoNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoNeId.setStatus("current")
_HpnicfIpRanDcnNeInfoNeIpType_Type = InetAddressType
_HpnicfIpRanDcnNeInfoNeIpType_Object = MibTableColumn
hpnicfIpRanDcnNeInfoNeIpType = _HpnicfIpRanDcnNeInfoNeIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2, 1, 2),
    _HpnicfIpRanDcnNeInfoNeIpType_Type()
)
hpnicfIpRanDcnNeInfoNeIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoNeIpType.setStatus("current")
_HpnicfIpRanDcnNeInfoNeIp_Type = InetAddress
_HpnicfIpRanDcnNeInfoNeIp_Object = MibTableColumn
hpnicfIpRanDcnNeInfoNeIp = _HpnicfIpRanDcnNeInfoNeIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2, 1, 3),
    _HpnicfIpRanDcnNeInfoNeIp_Type()
)
hpnicfIpRanDcnNeInfoNeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoNeIp.setStatus("current")
_HpnicfIpRanDcnNeInfoMetric_Type = Integer32
_HpnicfIpRanDcnNeInfoMetric_Object = MibTableColumn
hpnicfIpRanDcnNeInfoMetric = _HpnicfIpRanDcnNeInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2, 1, 4),
    _HpnicfIpRanDcnNeInfoMetric_Type()
)
hpnicfIpRanDcnNeInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoMetric.setStatus("current")


class _HpnicfIpRanDcnNeInfoDeviceType_Type(DisplayString):
    """Custom type hpnicfIpRanDcnNeInfoDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIpRanDcnNeInfoDeviceType_Type.__name__ = "DisplayString"
_HpnicfIpRanDcnNeInfoDeviceType_Object = MibTableColumn
hpnicfIpRanDcnNeInfoDeviceType = _HpnicfIpRanDcnNeInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 1, 2, 1, 5),
    _HpnicfIpRanDcnNeInfoDeviceType_Type()
)
hpnicfIpRanDcnNeInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeInfoDeviceType.setStatus("current")
_HpnicfIpRanDcnTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcnTrapObjects = _HpnicfIpRanDcnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 2)
)
_HpnicfIpRanDcnNeNumber_Type = Integer32
_HpnicfIpRanDcnNeNumber_Object = MibScalar
hpnicfIpRanDcnNeNumber = _HpnicfIpRanDcnNeNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 2, 1),
    _HpnicfIpRanDcnNeNumber_Type()
)
hpnicfIpRanDcnNeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeNumber.setStatus("current")


class _HpnicfIpRanDcnNeChangeMode_Type(Integer32):
    """Custom type hpnicfIpRanDcnNeChangeMode based on Integer32"""
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


_HpnicfIpRanDcnNeChangeMode_Type.__name__ = "Integer32"
_HpnicfIpRanDcnNeChangeMode_Object = MibScalar
hpnicfIpRanDcnNeChangeMode = _HpnicfIpRanDcnNeChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 2, 2),
    _HpnicfIpRanDcnNeChangeMode_Type()
)
hpnicfIpRanDcnNeChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeChangeMode.setStatus("current")


class _HpnicfIpRanDcnCompanyName_Type(DisplayString):
    """Custom type hpnicfIpRanDcnCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIpRanDcnCompanyName_Type.__name__ = "DisplayString"
_HpnicfIpRanDcnCompanyName_Object = MibScalar
hpnicfIpRanDcnCompanyName = _HpnicfIpRanDcnCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 2, 3),
    _HpnicfIpRanDcnCompanyName_Type()
)
hpnicfIpRanDcnCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnCompanyName.setStatus("current")


class _HpnicfIpRanDcnDeviceType_Type(DisplayString):
    """Custom type hpnicfIpRanDcnDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIpRanDcnDeviceType_Type.__name__ = "DisplayString"
_HpnicfIpRanDcnDeviceType_Object = MibScalar
hpnicfIpRanDcnDeviceType = _HpnicfIpRanDcnDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 2, 4),
    _HpnicfIpRanDcnDeviceType_Type()
)
hpnicfIpRanDcnDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnDeviceType.setStatus("current")
_HpnicfIpRanDcnDeviceMac_Type = MacAddress
_HpnicfIpRanDcnDeviceMac_Object = MibScalar
hpnicfIpRanDcnDeviceMac = _HpnicfIpRanDcnDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 2, 5),
    _HpnicfIpRanDcnDeviceMac_Type()
)
hpnicfIpRanDcnDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpRanDcnDeviceMac.setStatus("current")
_HpnicfIpRanDcnTraps_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcnTraps = _HpnicfIpRanDcnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 3)
)
_HpnicfIpRanDcnTrapsPrefix_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcnTrapsPrefix = _HpnicfIpRanDcnTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfIpRanDcnNeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 3, 0, 1)
)
hpnicfIpRanDcnNeOnline.setObjects(
      *(("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeId"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeIpType"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeIp"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnCompanyName"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnDeviceType"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnDeviceMac"))
)
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeOnline.setStatus(
        "current"
    )

hpnicfIpRanDcnNeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152, 1, 3, 0, 2)
)
hpnicfIpRanDcnNeOffline.setObjects(
      *(("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeId"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeIpType"),
        ("HPN-ICF-IPRAN-DCN-MIB", "hpnicfIpRanDcnNeInfoNeIp"))
)
if mibBuilder.loadTexts:
    hpnicfIpRanDcnNeOffline.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IPRAN-DCN-MIB",
    **{"HpnicfIpRanNeId": HpnicfIpRanNeId,
       "hpnicfIpRanDcn": hpnicfIpRanDcn,
       "hpnicfIpRanDcnMIB": hpnicfIpRanDcnMIB,
       "hpnicfIpRanDcnObjects": hpnicfIpRanDcnObjects,
       "hpnicfIpRanDcnInfoObject": hpnicfIpRanDcnInfoObject,
       "hpnicfIpRanDcnNeId": hpnicfIpRanDcnNeId,
       "hpnicfIpRanDcnNeIpType": hpnicfIpRanDcnNeIpType,
       "hpnicfIpRanDcnNeIp": hpnicfIpRanDcnNeIp,
       "hpnicfIpRanDcnMask": hpnicfIpRanDcnMask,
       "hpnicfIpRanDcnNeInfoTable": hpnicfIpRanDcnNeInfoTable,
       "hpnicfIpRanDcnNeInfoEntry": hpnicfIpRanDcnNeInfoEntry,
       "hpnicfIpRanDcnNeInfoNeId": hpnicfIpRanDcnNeInfoNeId,
       "hpnicfIpRanDcnNeInfoNeIpType": hpnicfIpRanDcnNeInfoNeIpType,
       "hpnicfIpRanDcnNeInfoNeIp": hpnicfIpRanDcnNeInfoNeIp,
       "hpnicfIpRanDcnNeInfoMetric": hpnicfIpRanDcnNeInfoMetric,
       "hpnicfIpRanDcnNeInfoDeviceType": hpnicfIpRanDcnNeInfoDeviceType,
       "hpnicfIpRanDcnTrapObjects": hpnicfIpRanDcnTrapObjects,
       "hpnicfIpRanDcnNeNumber": hpnicfIpRanDcnNeNumber,
       "hpnicfIpRanDcnNeChangeMode": hpnicfIpRanDcnNeChangeMode,
       "hpnicfIpRanDcnCompanyName": hpnicfIpRanDcnCompanyName,
       "hpnicfIpRanDcnDeviceType": hpnicfIpRanDcnDeviceType,
       "hpnicfIpRanDcnDeviceMac": hpnicfIpRanDcnDeviceMac,
       "hpnicfIpRanDcnTraps": hpnicfIpRanDcnTraps,
       "hpnicfIpRanDcnTrapsPrefix": hpnicfIpRanDcnTrapsPrefix,
       "hpnicfIpRanDcnNeOnline": hpnicfIpRanDcnNeOnline,
       "hpnicfIpRanDcnNeOffline": hpnicfIpRanDcnNeOffline}
)
