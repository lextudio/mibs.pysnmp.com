# SNMP MIB module (HUAWEI-VO-GK-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-GK-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:31 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwVoiceGKClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8)
)
hwVoiceGKClientMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoGKClientObjects_ObjectIdentity = ObjectIdentity
hwVoGKClientObjects = _HwVoGKClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1)
)


class _HwVoRasOn_Type(Integer32):
    """Custom type hwVoRasOn based on Integer32"""
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


_HwVoRasOn_Type.__name__ = "Integer32"
_HwVoRasOn_Object = MibScalar
hwVoRasOn = _HwVoRasOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 1),
    _HwVoRasOn_Type()
)
hwVoRasOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoRasOn.setStatus("current")
_HwVoH323InterfaceIndex_Type = Integer32
_HwVoH323InterfaceIndex_Object = MibScalar
hwVoH323InterfaceIndex = _HwVoH323InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 2),
    _HwVoH323InterfaceIndex_Type()
)
hwVoH323InterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323InterfaceIndex.setStatus("obsolete")
_HwVoGwIPAddress_Type = IpAddress
_HwVoGwIPAddress_Object = MibScalar
hwVoGwIPAddress = _HwVoGwIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 3),
    _HwVoGwIPAddress_Type()
)
hwVoGwIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGwIPAddress.setStatus("current")


class _HwVoH323GWID_Type(OctetString):
    """Custom type hwVoH323GWID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwVoH323GWID_Type.__name__ = "OctetString"
_HwVoH323GWID_Object = MibScalar
hwVoH323GWID = _HwVoH323GWID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 4),
    _HwVoH323GWID_Type()
)
hwVoH323GWID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GWID.setStatus("current")


class _HwVoH323GWSupportMode_Type(Integer32):
    """Custom type hwVoH323GWSupportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("huawei", 2),
          ("nonstandard-compatible", 1))
    )


_HwVoH323GWSupportMode_Type.__name__ = "Integer32"
_HwVoH323GWSupportMode_Object = MibScalar
hwVoH323GWSupportMode = _HwVoH323GWSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 5),
    _HwVoH323GWSupportMode_Type()
)
hwVoH323GWSupportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GWSupportMode.setStatus("obsolete")


class _HwVoH323GWAreaID_Type(OctetString):
    """Custom type hwVoH323GWAreaID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 960),
    )


_HwVoH323GWAreaID_Type.__name__ = "OctetString"
_HwVoH323GWAreaID_Object = MibScalar
hwVoH323GWAreaID = _HwVoH323GWAreaID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 6),
    _HwVoH323GWAreaID_Type()
)
hwVoH323GWAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GWAreaID.setStatus("current")


class _HwVoH323GKID_Type(OctetString):
    """Custom type hwVoH323GKID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwVoH323GKID_Type.__name__ = "OctetString"
_HwVoH323GKID_Object = MibScalar
hwVoH323GKID = _HwVoH323GKID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 7),
    _HwVoH323GKID_Type()
)
hwVoH323GKID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GKID.setStatus("current")
_HwVoH323GKIPAddress_Type = IpAddress
_HwVoH323GKIPAddress_Object = MibScalar
hwVoH323GKIPAddress = _HwVoH323GKIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 8),
    _HwVoH323GKIPAddress_Type()
)
hwVoH323GKIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GKIPAddress.setStatus("current")


class _HwVoH323GKPort_Type(Integer32):
    """Custom type hwVoH323GKPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwVoH323GKPort_Type.__name__ = "Integer32"
_HwVoH323GKPort_Object = MibScalar
hwVoH323GKPort = _HwVoH323GKPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 9),
    _HwVoH323GKPort_Type()
)
hwVoH323GKPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GKPort.setStatus("current")


class _HwVoH323GK2ID_Type(OctetString):
    """Custom type hwVoH323GK2ID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwVoH323GK2ID_Type.__name__ = "OctetString"
_HwVoH323GK2ID_Object = MibScalar
hwVoH323GK2ID = _HwVoH323GK2ID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 10),
    _HwVoH323GK2ID_Type()
)
hwVoH323GK2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GK2ID.setStatus("current")
_HwVoH323GK2IPAddress_Type = IpAddress
_HwVoH323GK2IPAddress_Object = MibScalar
hwVoH323GK2IPAddress = _HwVoH323GK2IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 11),
    _HwVoH323GK2IPAddress_Type()
)
hwVoH323GK2IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GK2IPAddress.setStatus("current")


class _HwVoH323GK2Port_Type(Integer32):
    """Custom type hwVoH323GK2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwVoH323GK2Port_Type.__name__ = "Integer32"
_HwVoH323GK2Port_Object = MibScalar
hwVoH323GK2Port = _HwVoH323GK2Port_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 12),
    _HwVoH323GK2Port_Type()
)
hwVoH323GK2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GK2Port.setStatus("current")


class _HwVoH323GKSecurityCall_Type(Integer32):
    """Custom type hwVoH323GKSecurityCall based on Integer32"""
    defaultValue = 1

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


_HwVoH323GKSecurityCall_Type.__name__ = "Integer32"
_HwVoH323GKSecurityCall_Object = MibScalar
hwVoH323GKSecurityCall = _HwVoH323GKSecurityCall_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 13),
    _HwVoH323GKSecurityCall_Type()
)
hwVoH323GKSecurityCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GKSecurityCall.setStatus("current")


class _HwVoH323GKSecurityPWDType_Type(Integer32):
    """Custom type hwVoH323GKSecurityPWDType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 2))
    )


_HwVoH323GKSecurityPWDType_Type.__name__ = "Integer32"
_HwVoH323GKSecurityPWDType_Object = MibScalar
hwVoH323GKSecurityPWDType = _HwVoH323GKSecurityPWDType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 14),
    _HwVoH323GKSecurityPWDType_Type()
)
hwVoH323GKSecurityPWDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GKSecurityPWDType.setStatus("current")


class _HwVoH323GKSecurityPWD_Type(OctetString):
    """Custom type hwVoH323GKSecurityPWD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HwVoH323GKSecurityPWD_Type.__name__ = "OctetString"
_HwVoH323GKSecurityPWD_Object = MibScalar
hwVoH323GKSecurityPWD = _HwVoH323GKSecurityPWD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8, 1, 15),
    _HwVoH323GKSecurityPWD_Type()
)
hwVoH323GKSecurityPWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoH323GKSecurityPWD.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-GK-CLIENT-MIB",
    **{"hwVoiceGKClientMIB": hwVoiceGKClientMIB,
       "hwVoGKClientObjects": hwVoGKClientObjects,
       "hwVoRasOn": hwVoRasOn,
       "hwVoH323InterfaceIndex": hwVoH323InterfaceIndex,
       "hwVoGwIPAddress": hwVoGwIPAddress,
       "hwVoH323GWID": hwVoH323GWID,
       "hwVoH323GWSupportMode": hwVoH323GWSupportMode,
       "hwVoH323GWAreaID": hwVoH323GWAreaID,
       "hwVoH323GKID": hwVoH323GKID,
       "hwVoH323GKIPAddress": hwVoH323GKIPAddress,
       "hwVoH323GKPort": hwVoH323GKPort,
       "hwVoH323GK2ID": hwVoH323GK2ID,
       "hwVoH323GK2IPAddress": hwVoH323GK2IPAddress,
       "hwVoH323GK2Port": hwVoH323GK2Port,
       "hwVoH323GKSecurityCall": hwVoH323GKSecurityCall,
       "hwVoH323GKSecurityPWDType": hwVoH323GKSecurityPWDType,
       "hwVoH323GKSecurityPWD": hwVoH323GKSecurityPWD}
)
