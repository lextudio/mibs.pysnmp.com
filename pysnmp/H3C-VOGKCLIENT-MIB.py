# SNMP MIB module (H3C-VOGKCLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOGKCLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:45 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

h3cVoiceGKClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8)
)
h3cVoiceGKClient.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoGKClientObjects_ObjectIdentity = ObjectIdentity
h3cVoGKClientObjects = _H3cVoGKClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1)
)


class _H3cVoRasOn_Type(Integer32):
    """Custom type h3cVoRasOn based on Integer32"""
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


_H3cVoRasOn_Type.__name__ = "Integer32"
_H3cVoRasOn_Object = MibScalar
h3cVoRasOn = _H3cVoRasOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 1),
    _H3cVoRasOn_Type()
)
h3cVoRasOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoRasOn.setStatus("current")
_H3cVoGwIPAddressType_Type = InetAddressType
_H3cVoGwIPAddressType_Object = MibScalar
h3cVoGwIPAddressType = _H3cVoGwIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 2),
    _H3cVoGwIPAddressType_Type()
)
h3cVoGwIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGwIPAddressType.setStatus("current")
_H3cVoGwIPAddress_Type = InetAddress
_H3cVoGwIPAddress_Object = MibScalar
h3cVoGwIPAddress = _H3cVoGwIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 3),
    _H3cVoGwIPAddress_Type()
)
h3cVoGwIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGwIPAddress.setStatus("current")


class _H3cVoH323GWID_Type(OctetString):
    """Custom type h3cVoH323GWID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_H3cVoH323GWID_Type.__name__ = "OctetString"
_H3cVoH323GWID_Object = MibScalar
h3cVoH323GWID = _H3cVoH323GWID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 4),
    _H3cVoH323GWID_Type()
)
h3cVoH323GWID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GWID.setStatus("current")


class _H3cVoH323GKID_Type(OctetString):
    """Custom type h3cVoH323GKID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_H3cVoH323GKID_Type.__name__ = "OctetString"
_H3cVoH323GKID_Object = MibScalar
h3cVoH323GKID = _H3cVoH323GKID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 5),
    _H3cVoH323GKID_Type()
)
h3cVoH323GKID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKID.setStatus("current")
_H3cVoH323GKIPAddressType_Type = InetAddressType
_H3cVoH323GKIPAddressType_Object = MibScalar
h3cVoH323GKIPAddressType = _H3cVoH323GKIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 6),
    _H3cVoH323GKIPAddressType_Type()
)
h3cVoH323GKIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKIPAddressType.setStatus("current")
_H3cVoH323GKIPAddress_Type = InetAddress
_H3cVoH323GKIPAddress_Object = MibScalar
h3cVoH323GKIPAddress = _H3cVoH323GKIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 7),
    _H3cVoH323GKIPAddress_Type()
)
h3cVoH323GKIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKIPAddress.setStatus("current")


class _H3cVoH323GKPort_Type(Integer32):
    """Custom type h3cVoH323GKPort based on Integer32"""
    defaultValue = 1719

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cVoH323GKPort_Type.__name__ = "Integer32"
_H3cVoH323GKPort_Object = MibScalar
h3cVoH323GKPort = _H3cVoH323GKPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 8),
    _H3cVoH323GKPort_Type()
)
h3cVoH323GKPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKPort.setStatus("current")


class _H3cVoH323GK2ID_Type(OctetString):
    """Custom type h3cVoH323GK2ID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_H3cVoH323GK2ID_Type.__name__ = "OctetString"
_H3cVoH323GK2ID_Object = MibScalar
h3cVoH323GK2ID = _H3cVoH323GK2ID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 9),
    _H3cVoH323GK2ID_Type()
)
h3cVoH323GK2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GK2ID.setStatus("current")
_H3cVoH323GK2IPAddressType_Type = InetAddressType
_H3cVoH323GK2IPAddressType_Object = MibScalar
h3cVoH323GK2IPAddressType = _H3cVoH323GK2IPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 10),
    _H3cVoH323GK2IPAddressType_Type()
)
h3cVoH323GK2IPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GK2IPAddressType.setStatus("current")
_H3cVoH323GK2IPAddress_Type = InetAddress
_H3cVoH323GK2IPAddress_Object = MibScalar
h3cVoH323GK2IPAddress = _H3cVoH323GK2IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 11),
    _H3cVoH323GK2IPAddress_Type()
)
h3cVoH323GK2IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GK2IPAddress.setStatus("current")


class _H3cVoH323GK2Port_Type(Integer32):
    """Custom type h3cVoH323GK2Port based on Integer32"""
    defaultValue = 1719

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cVoH323GK2Port_Type.__name__ = "Integer32"
_H3cVoH323GK2Port_Object = MibScalar
h3cVoH323GK2Port = _H3cVoH323GK2Port_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 12),
    _H3cVoH323GK2Port_Type()
)
h3cVoH323GK2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GK2Port.setStatus("current")


class _H3cVoH323GKSecurityCall_Type(Integer32):
    """Custom type h3cVoH323GKSecurityCall based on Integer32"""
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


_H3cVoH323GKSecurityCall_Type.__name__ = "Integer32"
_H3cVoH323GKSecurityCall_Object = MibScalar
h3cVoH323GKSecurityCall = _H3cVoH323GKSecurityCall_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 13),
    _H3cVoH323GKSecurityCall_Type()
)
h3cVoH323GKSecurityCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKSecurityCall.setStatus("current")


class _H3cVoH323GKSecurityPWDType_Type(Integer32):
    """Custom type h3cVoH323GKSecurityPWDType based on Integer32"""
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


_H3cVoH323GKSecurityPWDType_Type.__name__ = "Integer32"
_H3cVoH323GKSecurityPWDType_Object = MibScalar
h3cVoH323GKSecurityPWDType = _H3cVoH323GKSecurityPWDType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 14),
    _H3cVoH323GKSecurityPWDType_Type()
)
h3cVoH323GKSecurityPWDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKSecurityPWDType.setStatus("current")
_H3cVoH323GKSecurityPWD_Type = OctetString
_H3cVoH323GKSecurityPWD_Object = MibScalar
h3cVoH323GKSecurityPWD = _H3cVoH323GKSecurityPWD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 8, 1, 15),
    _H3cVoH323GKSecurityPWD_Type()
)
h3cVoH323GKSecurityPWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoH323GKSecurityPWD.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOGKCLIENT-MIB",
    **{"h3cVoiceGKClient": h3cVoiceGKClient,
       "h3cVoGKClientObjects": h3cVoGKClientObjects,
       "h3cVoRasOn": h3cVoRasOn,
       "h3cVoGwIPAddressType": h3cVoGwIPAddressType,
       "h3cVoGwIPAddress": h3cVoGwIPAddress,
       "h3cVoH323GWID": h3cVoH323GWID,
       "h3cVoH323GKID": h3cVoH323GKID,
       "h3cVoH323GKIPAddressType": h3cVoH323GKIPAddressType,
       "h3cVoH323GKIPAddress": h3cVoH323GKIPAddress,
       "h3cVoH323GKPort": h3cVoH323GKPort,
       "h3cVoH323GK2ID": h3cVoH323GK2ID,
       "h3cVoH323GK2IPAddressType": h3cVoH323GK2IPAddressType,
       "h3cVoH323GK2IPAddress": h3cVoH323GK2IPAddress,
       "h3cVoH323GK2Port": h3cVoH323GK2Port,
       "h3cVoH323GKSecurityCall": h3cVoH323GKSecurityCall,
       "h3cVoH323GKSecurityPWDType": h3cVoH323GKSecurityPWDType,
       "h3cVoH323GKSecurityPWD": h3cVoH323GKSecurityPWD}
)
