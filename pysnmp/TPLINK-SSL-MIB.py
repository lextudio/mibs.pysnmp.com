# SNMP MIB module (TPLINK-SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:42 2024
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

tplinkSslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42)
)
tplinkSslMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSslMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSslMIBObjects = _TplinkSslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1)
)


class _TpHttpsEnable_Type(Integer32):
    """Custom type tpHttpsEnable based on Integer32"""
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


_TpHttpsEnable_Type.__name__ = "Integer32"
_TpHttpsEnable_Object = MibScalar
tpHttpsEnable = _TpHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 1),
    _TpHttpsEnable_Type()
)
tpHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsEnable.setStatus("current")


class _TpSslv3Enable_Type(Integer32):
    """Custom type tpSslv3Enable based on Integer32"""
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


_TpSslv3Enable_Type.__name__ = "Integer32"
_TpSslv3Enable_Object = MibScalar
tpSslv3Enable = _TpSslv3Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 2),
    _TpSslv3Enable_Type()
)
tpSslv3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSslv3Enable.setStatus("current")


class _TpTlsv1Enable_Type(Integer32):
    """Custom type tpTlsv1Enable based on Integer32"""
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


_TpTlsv1Enable_Type.__name__ = "Integer32"
_TpTlsv1Enable_Object = MibScalar
tpTlsv1Enable = _TpTlsv1Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 3),
    _TpTlsv1Enable_Type()
)
tpTlsv1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTlsv1Enable.setStatus("current")


class _TpRc4Md5_Type(Integer32):
    """Custom type tpRc4Md5 based on Integer32"""
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


_TpRc4Md5_Type.__name__ = "Integer32"
_TpRc4Md5_Object = MibScalar
tpRc4Md5 = _TpRc4Md5_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 4),
    _TpRc4Md5_Type()
)
tpRc4Md5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRc4Md5.setStatus("current")


class _TpRc4Sha_Type(Integer32):
    """Custom type tpRc4Sha based on Integer32"""
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


_TpRc4Sha_Type.__name__ = "Integer32"
_TpRc4Sha_Object = MibScalar
tpRc4Sha = _TpRc4Sha_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 5),
    _TpRc4Sha_Type()
)
tpRc4Sha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRc4Sha.setStatus("current")


class _TpDesCbcSha_Type(Integer32):
    """Custom type tpDesCbcSha based on Integer32"""
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


_TpDesCbcSha_Type.__name__ = "Integer32"
_TpDesCbcSha_Object = MibScalar
tpDesCbcSha = _TpDesCbcSha_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 6),
    _TpDesCbcSha_Type()
)
tpDesCbcSha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDesCbcSha.setStatus("current")


class _Tp3DesEdeCbcSha_Type(Integer32):
    """Custom type tp3DesEdeCbcSha based on Integer32"""
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


_Tp3DesEdeCbcSha_Type.__name__ = "Integer32"
_Tp3DesEdeCbcSha_Object = MibScalar
tp3DesEdeCbcSha = _Tp3DesEdeCbcSha_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 7),
    _Tp3DesEdeCbcSha_Type()
)
tp3DesEdeCbcSha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp3DesEdeCbcSha.setStatus("current")


class _TpHttpsSessionTimeOut_Type(Integer32):
    """Custom type tpHttpsSessionTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TpHttpsSessionTimeOut_Type.__name__ = "Integer32"
_TpHttpsSessionTimeOut_Object = MibScalar
tpHttpsSessionTimeOut = _TpHttpsSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 8),
    _TpHttpsSessionTimeOut_Type()
)
tpHttpsSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsSessionTimeOut.setStatus("current")


class _TpHttpsUserLimitEnable_Type(Integer32):
    """Custom type tpHttpsUserLimitEnable based on Integer32"""
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


_TpHttpsUserLimitEnable_Type.__name__ = "Integer32"
_TpHttpsUserLimitEnable_Object = MibScalar
tpHttpsUserLimitEnable = _TpHttpsUserLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 9),
    _TpHttpsUserLimitEnable_Type()
)
tpHttpsUserLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitEnable.setStatus("current")
_TpHttpsUserLimitMaxAdminNum_Type = Integer32
_TpHttpsUserLimitMaxAdminNum_Object = MibScalar
tpHttpsUserLimitMaxAdminNum = _TpHttpsUserLimitMaxAdminNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 10),
    _TpHttpsUserLimitMaxAdminNum_Type()
)
tpHttpsUserLimitMaxAdminNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitMaxAdminNum.setStatus("current")
_TpHttpsUserLimitMaxGuestNum_Type = Integer32
_TpHttpsUserLimitMaxGuestNum_Object = MibScalar
tpHttpsUserLimitMaxGuestNum = _TpHttpsUserLimitMaxGuestNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 11),
    _TpHttpsUserLimitMaxGuestNum_Type()
)
tpHttpsUserLimitMaxGuestNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitMaxGuestNum.setStatus("current")
_TplinkSslNotifications_ObjectIdentity = ObjectIdentity
tplinkSslNotifications = _TplinkSslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SSL-MIB",
    **{"tplinkSslMIB": tplinkSslMIB,
       "tplinkSslMIBObjects": tplinkSslMIBObjects,
       "tpHttpsEnable": tpHttpsEnable,
       "tpSslv3Enable": tpSslv3Enable,
       "tpTlsv1Enable": tpTlsv1Enable,
       "tpRc4Md5": tpRc4Md5,
       "tpRc4Sha": tpRc4Sha,
       "tpDesCbcSha": tpDesCbcSha,
       "tp3DesEdeCbcSha": tp3DesEdeCbcSha,
       "tpHttpsSessionTimeOut": tpHttpsSessionTimeOut,
       "tpHttpsUserLimitEnable": tpHttpsUserLimitEnable,
       "tpHttpsUserLimitMaxAdminNum": tpHttpsUserLimitMaxAdminNum,
       "tpHttpsUserLimitMaxGuestNum": tpHttpsUserLimitMaxGuestNum,
       "tplinkSslNotifications": tplinkSslNotifications}
)
