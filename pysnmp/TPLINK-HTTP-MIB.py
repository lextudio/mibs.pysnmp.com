# SNMP MIB module (TPLINK-HTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-HTTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:08 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkHttp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51)
)
tplinkHttp.setRevisions(
        ("2015-01-21 10:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkHttpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkHttpMIBObjects = _TplinkHttpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1)
)


class _HttpEnable_Type(Integer32):
    """Custom type httpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpEnable_Type.__name__ = "Integer32"
_HttpEnable_Object = MibScalar
httpEnable = _HttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 1),
    _HttpEnable_Type()
)
httpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpEnable.setStatus("current")


class _HttpSessionTimeOut_Type(Integer32):
    """Custom type httpSessionTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_HttpSessionTimeOut_Type.__name__ = "Integer32"
_HttpSessionTimeOut_Object = MibScalar
httpSessionTimeOut = _HttpSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 2),
    _HttpSessionTimeOut_Type()
)
httpSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpSessionTimeOut.setStatus("current")


class _HttpUserLimitEnable_Type(Integer32):
    """Custom type httpUserLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpUserLimitEnable_Type.__name__ = "Integer32"
_HttpUserLimitEnable_Object = MibScalar
httpUserLimitEnable = _HttpUserLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 3),
    _HttpUserLimitEnable_Type()
)
httpUserLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitEnable.setStatus("current")
_HttpUserLimitMaxAdminNum_Type = Integer32
_HttpUserLimitMaxAdminNum_Object = MibScalar
httpUserLimitMaxAdminNum = _HttpUserLimitMaxAdminNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 4),
    _HttpUserLimitMaxAdminNum_Type()
)
httpUserLimitMaxAdminNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitMaxAdminNum.setStatus("current")
_HttpUserLimitMaxGuestNum_Type = Integer32
_HttpUserLimitMaxGuestNum_Object = MibScalar
httpUserLimitMaxGuestNum = _HttpUserLimitMaxGuestNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 5),
    _HttpUserLimitMaxGuestNum_Type()
)
httpUserLimitMaxGuestNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitMaxGuestNum.setStatus("current")
_TplinkHttpMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkHttpMIBNotifications = _TplinkHttpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-HTTP-MIB",
    **{"tplinkHttp": tplinkHttp,
       "tplinkHttpMIBObjects": tplinkHttpMIBObjects,
       "httpEnable": httpEnable,
       "httpSessionTimeOut": httpSessionTimeOut,
       "httpUserLimitEnable": httpUserLimitEnable,
       "httpUserLimitMaxAdminNum": httpUserLimitMaxAdminNum,
       "httpUserLimitMaxGuestNum": httpUserLimitMaxGuestNum,
       "tplinkHttpMIBNotifications": tplinkHttpMIBNotifications}
)
