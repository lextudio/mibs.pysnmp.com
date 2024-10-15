# SNMP MIB module (H3C-WEB-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-WEB-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:55 2024
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
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cWebAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93)
)
h3cWebAuthentication.setRevisions(
        ("2008-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cWaTrapObjects_ObjectIdentity = ObjectIdentity
h3cWaTrapObjects = _H3cWaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 1)
)
_H3cWaVlanID_Type = Integer32
_H3cWaVlanID_Object = MibScalar
h3cWaVlanID = _H3cWaVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 1, 1),
    _H3cWaVlanID_Type()
)
h3cWaVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaVlanID.setStatus("current")


class _H3cWaReasonCode_Type(Integer32):
    """Custom type h3cWaReasonCode based on Integer32"""
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


_H3cWaReasonCode_Type.__name__ = "Integer32"
_H3cWaReasonCode_Object = MibScalar
h3cWaReasonCode = _H3cWaReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 1, 2),
    _H3cWaReasonCode_Type()
)
h3cWaReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaReasonCode.setStatus("current")


class _H3cWaActionCode_Type(Integer32):
    """Custom type h3cWaActionCode based on Integer32"""
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


_H3cWaActionCode_Type.__name__ = "Integer32"
_H3cWaActionCode_Object = MibScalar
h3cWaActionCode = _H3cWaActionCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 1, 3),
    _H3cWaActionCode_Type()
)
h3cWaActionCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaActionCode.setStatus("current")
_H3cWaClientMacAddr_Type = MacAddress
_H3cWaClientMacAddr_Object = MibScalar
h3cWaClientMacAddr = _H3cWaClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 1, 4),
    _H3cWaClientMacAddr_Type()
)
h3cWaClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaClientMacAddr.setStatus("current")
_H3cWaTrap_ObjectIdentity = ObjectIdentity
h3cWaTrap = _H3cWaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 2)
)
_H3cWaTrapPrefix_ObjectIdentity = ObjectIdentity
h3cWaTrapPrefix = _H3cWaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cWaClientLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 2, 0, 1)
)
h3cWaClientLogon.setObjects(
      *(("H3C-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"))
)
if mibBuilder.loadTexts:
    h3cWaClientLogon.setStatus(
        "current"
    )

h3cWaClientLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 2, 0, 2)
)
h3cWaClientLogonFail.setObjects(
      *(("H3C-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"),
        ("H3C-WEB-AUTHENTICATION-MIB", "h3cWaReasonCode"))
)
if mibBuilder.loadTexts:
    h3cWaClientLogonFail.setStatus(
        "current"
    )

h3cWaClientLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 2, 0, 3)
)
h3cWaClientLogout.setObjects(
      *(("H3C-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"),
        ("H3C-WEB-AUTHENTICATION-MIB", "h3cWaReasonCode"))
)
if mibBuilder.loadTexts:
    h3cWaClientLogout.setStatus(
        "current"
    )

h3cWaSysAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93, 2, 0, 4)
)
h3cWaSysAction.setObjects(
    ("H3C-WEB-AUTHENTICATION-MIB", "h3cWaActionCode")
)
if mibBuilder.loadTexts:
    h3cWaSysAction.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-WEB-AUTHENTICATION-MIB",
    **{"h3cWebAuthentication": h3cWebAuthentication,
       "h3cWaTrapObjects": h3cWaTrapObjects,
       "h3cWaVlanID": h3cWaVlanID,
       "h3cWaReasonCode": h3cWaReasonCode,
       "h3cWaActionCode": h3cWaActionCode,
       "h3cWaClientMacAddr": h3cWaClientMacAddr,
       "h3cWaTrap": h3cWaTrap,
       "h3cWaTrapPrefix": h3cWaTrapPrefix,
       "h3cWaClientLogon": h3cWaClientLogon,
       "h3cWaClientLogonFail": h3cWaClientLogonFail,
       "h3cWaClientLogout": h3cWaClientLogout,
       "h3cWaSysAction": h3cWaSysAction}
)
