# SNMP MIB module (HH3C-WEB-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-WEB-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:24 2024
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

(ifDescr,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr")

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

hh3cWebAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93)
)
hh3cWebAuthentication.setRevisions(
        ("2008-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cWaTrapObjects_ObjectIdentity = ObjectIdentity
hh3cWaTrapObjects = _Hh3cWaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 1)
)
_Hh3cWaVlanID_Type = Integer32
_Hh3cWaVlanID_Object = MibScalar
hh3cWaVlanID = _Hh3cWaVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 1),
    _Hh3cWaVlanID_Type()
)
hh3cWaVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWaVlanID.setStatus("current")


class _Hh3cWaReasonCode_Type(Integer32):
    """Custom type hh3cWaReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("authFail", 5),
          ("changeVlanFail", 7),
          ("configNumberMax", 2),
          ("cutOperation", 11),
          ("globalNumberMax", 1),
          ("invalidUsername", 4),
          ("noTransferData", 10),
          ("onlineOverTime", 9),
          ("other", 8),
          ("portDisabled", 12),
          ("portDown", 13),
          ("portNumberMax", 3),
          ("setACLFail", 6),
          ("userLogout", 14),
          ("vlanChanged", 15),
          ("vlanDelted", 16))
    )


_Hh3cWaReasonCode_Type.__name__ = "Integer32"
_Hh3cWaReasonCode_Object = MibScalar
hh3cWaReasonCode = _Hh3cWaReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 2),
    _Hh3cWaReasonCode_Type()
)
hh3cWaReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWaReasonCode.setStatus("current")


class _Hh3cWaActionCode_Type(Integer32):
    """Custom type hh3cWaActionCode based on Integer32"""
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


_Hh3cWaActionCode_Type.__name__ = "Integer32"
_Hh3cWaActionCode_Object = MibScalar
hh3cWaActionCode = _Hh3cWaActionCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 3),
    _Hh3cWaActionCode_Type()
)
hh3cWaActionCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWaActionCode.setStatus("current")
_Hh3cWaClientMacAddr_Type = MacAddress
_Hh3cWaClientMacAddr_Object = MibScalar
hh3cWaClientMacAddr = _Hh3cWaClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 4),
    _Hh3cWaClientMacAddr_Type()
)
hh3cWaClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWaClientMacAddr.setStatus("current")
_Hh3cWaTrap_ObjectIdentity = ObjectIdentity
hh3cWaTrap = _Hh3cWaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 2)
)
_Hh3cWaTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cWaTrapPrefix = _Hh3cWaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cWaClientLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 1)
)
hh3cWaClientLogon.setObjects(
      *(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaVlanID"))
)
if mibBuilder.loadTexts:
    hh3cWaClientLogon.setStatus(
        "current"
    )

hh3cWaClientLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 2)
)
hh3cWaClientLogonFail.setObjects(
      *(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaVlanID"),
        ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaReasonCode"))
)
if mibBuilder.loadTexts:
    hh3cWaClientLogonFail.setStatus(
        "current"
    )

hh3cWaClientLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 3)
)
hh3cWaClientLogout.setObjects(
      *(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaVlanID"),
        ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaReasonCode"))
)
if mibBuilder.loadTexts:
    hh3cWaClientLogout.setStatus(
        "current"
    )

hh3cWaSysAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 4)
)
hh3cWaSysAction.setObjects(
    ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaActionCode")
)
if mibBuilder.loadTexts:
    hh3cWaSysAction.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-WEB-AUTHENTICATION-MIB",
    **{"hh3cWebAuthentication": hh3cWebAuthentication,
       "hh3cWaTrapObjects": hh3cWaTrapObjects,
       "hh3cWaVlanID": hh3cWaVlanID,
       "hh3cWaReasonCode": hh3cWaReasonCode,
       "hh3cWaActionCode": hh3cWaActionCode,
       "hh3cWaClientMacAddr": hh3cWaClientMacAddr,
       "hh3cWaTrap": hh3cWaTrap,
       "hh3cWaTrapPrefix": hh3cWaTrapPrefix,
       "hh3cWaClientLogon": hh3cWaClientLogon,
       "hh3cWaClientLogonFail": hh3cWaClientLogonFail,
       "hh3cWaClientLogout": hh3cWaClientLogout,
       "hh3cWaSysAction": hh3cWaSysAction}
)
