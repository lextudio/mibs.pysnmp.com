# SNMP MIB module (HH3C-DVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:01 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DvpnAlgorithmSuite(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dvpn3DesCbcMd5PreShaModp1024", 6),
          ("dvpn3DesCbcMd5PreShaModp768", 5),
          ("dvpn3DesCbcSha1PreShaModp1024", 8),
          ("dvpn3DesCbcSha1PreShaModp768", 7),
          ("dvpnAesCbcMd5PreShaModp1024", 10),
          ("dvpnAesCbcMd5PreShaModp768", 9),
          ("dvpnAesCbcSHA1Sha1PreShaModp1024", 12),
          ("dvpnAesCbcSHA1Sha1PreShaModp768", 11),
          ("dvpnAlgorithmNone", 13),
          ("dvpnDesCbcMd5PreShaModp1024", 2),
          ("dvpnDesCbcMd5PreShaModp768", 1),
          ("dvpnDesCbcSha1PreShaModp1024", 4),
          ("dvpnDesCbcSha1PreShaModp768", 3))
    )



class DvpnCommunicateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clientToclient", 4),
          ("clientToserver", 1),
          ("serverToclient", 2),
          ("serverToserver", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDvpnMibObjects_ObjectIdentity = ObjectIdentity
hh3cDvpnMibObjects = _Hh3cDvpnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1)
)
_Hh3cDvpnMibGlobal_ObjectIdentity = ObjectIdentity
hh3cDvpnMibGlobal = _Hh3cDvpnMibGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1)
)


class _Hh3cDvpnServiceEnable_Type(Integer32):
    """Custom type hh3cDvpnServiceEnable based on Integer32"""
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


_Hh3cDvpnServiceEnable_Type.__name__ = "Integer32"
_Hh3cDvpnServiceEnable_Object = MibScalar
hh3cDvpnServiceEnable = _Hh3cDvpnServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 1),
    _Hh3cDvpnServiceEnable_Type()
)
hh3cDvpnServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnServiceEnable.setStatus("current")


class _Hh3cDvpnClassNumber_Type(Integer32):
    """Custom type hh3cDvpnClassNumber based on Integer32"""
    defaultValue = 0


_Hh3cDvpnClassNumber_Object = MibScalar
hh3cDvpnClassNumber = _Hh3cDvpnClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 2),
    _Hh3cDvpnClassNumber_Type()
)
hh3cDvpnClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnClassNumber.setStatus("current")


class _Hh3cDvpnClientNumber_Type(Integer32):
    """Custom type hh3cDvpnClientNumber based on Integer32"""
    defaultValue = 0


_Hh3cDvpnClientNumber_Object = MibScalar
hh3cDvpnClientNumber = _Hh3cDvpnClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 3),
    _Hh3cDvpnClientNumber_Type()
)
hh3cDvpnClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnClientNumber.setStatus("current")


class _Hh3cDvpnMapAgeTime_Type(Integer32):
    """Custom type hh3cDvpnMapAgeTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_Hh3cDvpnMapAgeTime_Type.__name__ = "Integer32"
_Hh3cDvpnMapAgeTime_Object = MibScalar
hh3cDvpnMapAgeTime = _Hh3cDvpnMapAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 4),
    _Hh3cDvpnMapAgeTime_Type()
)
hh3cDvpnMapAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnMapAgeTime.setStatus("current")


class _Hh3cDvpnClientRegisterInterval_Type(Integer32):
    """Custom type hh3cDvpnClientRegisterInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_Hh3cDvpnClientRegisterInterval_Type.__name__ = "Integer32"
_Hh3cDvpnClientRegisterInterval_Object = MibScalar
hh3cDvpnClientRegisterInterval = _Hh3cDvpnClientRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 5),
    _Hh3cDvpnClientRegisterInterval_Type()
)
hh3cDvpnClientRegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnClientRegisterInterval.setStatus("current")


class _Hh3cDvpnClientRegisterDumb_Type(Integer32):
    """Custom type hh3cDvpnClientRegisterDumb based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Hh3cDvpnClientRegisterDumb_Type.__name__ = "Integer32"
_Hh3cDvpnClientRegisterDumb_Object = MibScalar
hh3cDvpnClientRegisterDumb = _Hh3cDvpnClientRegisterDumb_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 6),
    _Hh3cDvpnClientRegisterDumb_Type()
)
hh3cDvpnClientRegisterDumb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnClientRegisterDumb.setStatus("current")


class _Hh3cDvpnClientRegisterRetry_Type(Integer32):
    """Custom type hh3cDvpnClientRegisterRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Hh3cDvpnClientRegisterRetry_Type.__name__ = "Integer32"
_Hh3cDvpnClientRegisterRetry_Object = MibScalar
hh3cDvpnClientRegisterRetry = _Hh3cDvpnClientRegisterRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 7),
    _Hh3cDvpnClientRegisterRetry_Type()
)
hh3cDvpnClientRegisterRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnClientRegisterRetry.setStatus("current")


class _Hh3cDvpnInputPkt_Type(Unsigned32):
    """Custom type hh3cDvpnInputPkt based on Unsigned32"""
    defaultValue = 0


_Hh3cDvpnInputPkt_Object = MibScalar
hh3cDvpnInputPkt = _Hh3cDvpnInputPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 8),
    _Hh3cDvpnInputPkt_Type()
)
hh3cDvpnInputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnInputPkt.setStatus("current")


class _Hh3cDvpnDropPkt_Type(Unsigned32):
    """Custom type hh3cDvpnDropPkt based on Unsigned32"""
    defaultValue = 0


_Hh3cDvpnDropPkt_Object = MibScalar
hh3cDvpnDropPkt = _Hh3cDvpnDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 9),
    _Hh3cDvpnDropPkt_Type()
)
hh3cDvpnDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDropPkt.setStatus("current")


class _Hh3cDvpnOutputPkt_Type(Unsigned32):
    """Custom type hh3cDvpnOutputPkt based on Unsigned32"""
    defaultValue = 0


_Hh3cDvpnOutputPkt_Object = MibScalar
hh3cDvpnOutputPkt = _Hh3cDvpnOutputPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 10),
    _Hh3cDvpnOutputPkt_Type()
)
hh3cDvpnOutputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnOutputPkt.setStatus("current")


class _Hh3cDvpnOutputErrorPkt_Type(Unsigned32):
    """Custom type hh3cDvpnOutputErrorPkt based on Unsigned32"""
    defaultValue = 0


_Hh3cDvpnOutputErrorPkt_Object = MibScalar
hh3cDvpnOutputErrorPkt = _Hh3cDvpnOutputErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 11),
    _Hh3cDvpnOutputErrorPkt_Type()
)
hh3cDvpnOutputErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnOutputErrorPkt.setStatus("current")


class _Hh3cDvpnEncryptErrorPkt_Type(Unsigned32):
    """Custom type hh3cDvpnEncryptErrorPkt based on Unsigned32"""
    defaultValue = 0


_Hh3cDvpnEncryptErrorPkt_Object = MibScalar
hh3cDvpnEncryptErrorPkt = _Hh3cDvpnEncryptErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 12),
    _Hh3cDvpnEncryptErrorPkt_Type()
)
hh3cDvpnEncryptErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnEncryptErrorPkt.setStatus("current")


class _Hh3cDvpnCurrentDeviceRole_Type(Integer32):
    """Custom type hh3cDvpnCurrentDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("client", 3),
          ("none", 1),
          ("server", 2))
    )


_Hh3cDvpnCurrentDeviceRole_Type.__name__ = "Integer32"
_Hh3cDvpnCurrentDeviceRole_Object = MibScalar
hh3cDvpnCurrentDeviceRole = _Hh3cDvpnCurrentDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 13),
    _Hh3cDvpnCurrentDeviceRole_Type()
)
hh3cDvpnCurrentDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnCurrentDeviceRole.setStatus("current")


class _Hh3cDvpnDomainNumber_Type(Integer32):
    """Custom type hh3cDvpnDomainNumber based on Integer32"""
    defaultValue = 0


_Hh3cDvpnDomainNumber_Object = MibScalar
hh3cDvpnDomainNumber = _Hh3cDvpnDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 14),
    _Hh3cDvpnDomainNumber_Type()
)
hh3cDvpnDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainNumber.setStatus("current")


class _Hh3cDvpnMapNumber_Type(Integer32):
    """Custom type hh3cDvpnMapNumber based on Integer32"""
    defaultValue = 0


_Hh3cDvpnMapNumber_Object = MibScalar
hh3cDvpnMapNumber = _Hh3cDvpnMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 15),
    _Hh3cDvpnMapNumber_Type()
)
hh3cDvpnMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapNumber.setStatus("current")


class _Hh3cDvpnSessionNumber_Type(Integer32):
    """Custom type hh3cDvpnSessionNumber based on Integer32"""
    defaultValue = 0


_Hh3cDvpnSessionNumber_Object = MibScalar
hh3cDvpnSessionNumber = _Hh3cDvpnSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 16),
    _Hh3cDvpnSessionNumber_Type()
)
hh3cDvpnSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionNumber.setStatus("current")


class _Hh3cDvpnServerPreSharedKey_Type(OctetString):
    """Custom type hh3cDvpnServerPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDvpnServerPreSharedKey_Type.__name__ = "OctetString"
_Hh3cDvpnServerPreSharedKey_Object = MibScalar
hh3cDvpnServerPreSharedKey = _Hh3cDvpnServerPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 17),
    _Hh3cDvpnServerPreSharedKey_Type()
)
hh3cDvpnServerPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnServerPreSharedKey.setStatus("current")


class _Hh3cDvpnMapTrapEnable_Type(Integer32):
    """Custom type hh3cDvpnMapTrapEnable based on Integer32"""
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


_Hh3cDvpnMapTrapEnable_Type.__name__ = "Integer32"
_Hh3cDvpnMapTrapEnable_Object = MibScalar
hh3cDvpnMapTrapEnable = _Hh3cDvpnMapTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 18),
    _Hh3cDvpnMapTrapEnable_Type()
)
hh3cDvpnMapTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnMapTrapEnable.setStatus("current")


class _Hh3cDvpnSessionTrapEnable_Type(Integer32):
    """Custom type hh3cDvpnSessionTrapEnable based on Integer32"""
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


_Hh3cDvpnSessionTrapEnable_Type.__name__ = "Integer32"
_Hh3cDvpnSessionTrapEnable_Object = MibScalar
hh3cDvpnSessionTrapEnable = _Hh3cDvpnSessionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 19),
    _Hh3cDvpnSessionTrapEnable_Type()
)
hh3cDvpnSessionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnSessionTrapEnable.setStatus("current")


class _Hh3cDvpnVersion_Type(Integer32):
    """Custom type hh3cDvpnVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version2", 1),
          ("version3", 2))
    )


_Hh3cDvpnVersion_Type.__name__ = "Integer32"
_Hh3cDvpnVersion_Object = MibScalar
hh3cDvpnVersion = _Hh3cDvpnVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 20),
    _Hh3cDvpnVersion_Type()
)
hh3cDvpnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnVersion.setStatus("current")


class _Hh3cDvpnClearDomainAllConection_Type(Integer32):
    """Custom type hh3cDvpnClearDomainAllConection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDvpnClearDomainAllConection_Type.__name__ = "Integer32"
_Hh3cDvpnClearDomainAllConection_Object = MibScalar
hh3cDvpnClearDomainAllConection = _Hh3cDvpnClearDomainAllConection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 21),
    _Hh3cDvpnClearDomainAllConection_Type()
)
hh3cDvpnClearDomainAllConection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnClearDomainAllConection.setStatus("current")


class _Hh3cDvpnClearDvpnStaInfo_Type(Integer32):
    """Custom type hh3cDvpnClearDvpnStaInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Hh3cDvpnClearDvpnStaInfo_Type.__name__ = "Integer32"
_Hh3cDvpnClearDvpnStaInfo_Object = MibScalar
hh3cDvpnClearDvpnStaInfo = _Hh3cDvpnClearDvpnStaInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 22),
    _Hh3cDvpnClearDvpnStaInfo_Type()
)
hh3cDvpnClearDvpnStaInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnClearDvpnStaInfo.setStatus("current")


class _Hh3cDvpnTotalRedirectNumber_Type(Unsigned32):
    """Custom type hh3cDvpnTotalRedirectNumber based on Unsigned32"""
    defaultValue = 0


_Hh3cDvpnTotalRedirectNumber_Object = MibScalar
hh3cDvpnTotalRedirectNumber = _Hh3cDvpnTotalRedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 23),
    _Hh3cDvpnTotalRedirectNumber_Type()
)
hh3cDvpnTotalRedirectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnTotalRedirectNumber.setStatus("current")


class _Hh3cDvpnGlobalAuthenClientType_Type(Integer32):
    """Custom type hh3cDvpnGlobalAuthenClientType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_Hh3cDvpnGlobalAuthenClientType_Type.__name__ = "Integer32"
_Hh3cDvpnGlobalAuthenClientType_Object = MibScalar
hh3cDvpnGlobalAuthenClientType = _Hh3cDvpnGlobalAuthenClientType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 24),
    _Hh3cDvpnGlobalAuthenClientType_Type()
)
hh3cDvpnGlobalAuthenClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnGlobalAuthenClientType.setStatus("current")


class _Hh3cDvpnGlobalUserDefAAADomain_Type(OctetString):
    """Custom type hh3cDvpnGlobalUserDefAAADomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Hh3cDvpnGlobalUserDefAAADomain_Type.__name__ = "OctetString"
_Hh3cDvpnGlobalUserDefAAADomain_Object = MibScalar
hh3cDvpnGlobalUserDefAAADomain = _Hh3cDvpnGlobalUserDefAAADomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 25),
    _Hh3cDvpnGlobalUserDefAAADomain_Type()
)
hh3cDvpnGlobalUserDefAAADomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnGlobalUserDefAAADomain.setStatus("current")
_Hh3cDvpnLocalDeviceId_Type = OctetString
_Hh3cDvpnLocalDeviceId_Object = MibScalar
hh3cDvpnLocalDeviceId = _Hh3cDvpnLocalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 26),
    _Hh3cDvpnLocalDeviceId_Type()
)
hh3cDvpnLocalDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnLocalDeviceId.setStatus("current")


class _Hh3cDvpnSessionHisAgeTime_Type(Integer32):
    """Custom type hh3cDvpnSessionHisAgeTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cDvpnSessionHisAgeTime_Type.__name__ = "Integer32"
_Hh3cDvpnSessionHisAgeTime_Object = MibScalar
hh3cDvpnSessionHisAgeTime = _Hh3cDvpnSessionHisAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 27),
    _Hh3cDvpnSessionHisAgeTime_Type()
)
hh3cDvpnSessionHisAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisAgeTime.setStatus("current")


class _Hh3cDvpnSessionHisReset_Type(Integer32):
    """Custom type hh3cDvpnSessionHisReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDvpnSessionHisReset_Type.__name__ = "Integer32"
_Hh3cDvpnSessionHisReset_Object = MibScalar
hh3cDvpnSessionHisReset = _Hh3cDvpnSessionHisReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 1, 28),
    _Hh3cDvpnSessionHisReset_Type()
)
hh3cDvpnSessionHisReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisReset.setStatus("current")
_Hh3cDvpnMibTableTroop_ObjectIdentity = ObjectIdentity
hh3cDvpnMibTableTroop = _Hh3cDvpnMibTableTroop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2)
)
_Hh3cDvpnPolicyTable_Object = MibTable
hh3cDvpnPolicyTable = _Hh3cDvpnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDvpnPolicyTable.setStatus("current")
_Hh3cDvpnPolicyEntry_Object = MibTableRow
hh3cDvpnPolicyEntry = _Hh3cDvpnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1)
)
hh3cDvpnPolicyEntry.setIndexNames(
    (0, "HH3C-DVPN-MIB", "hh3cDvpnPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDvpnPolicyEntry.setStatus("current")


class _Hh3cDvpnPolicyName_Type(OctetString):
    """Custom type hh3cDvpnPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cDvpnPolicyName_Type.__name__ = "OctetString"
_Hh3cDvpnPolicyName_Object = MibTableColumn
hh3cDvpnPolicyName = _Hh3cDvpnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 1),
    _Hh3cDvpnPolicyName_Type()
)
hh3cDvpnPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDvpnPolicyName.setStatus("current")


class _Hh3cDvpnPoAuthenClientType_Type(Integer32):
    """Custom type hh3cDvpnPoAuthenClientType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_Hh3cDvpnPoAuthenClientType_Type.__name__ = "Integer32"
_Hh3cDvpnPoAuthenClientType_Object = MibTableColumn
hh3cDvpnPoAuthenClientType = _Hh3cDvpnPoAuthenClientType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 2),
    _Hh3cDvpnPoAuthenClientType_Type()
)
hh3cDvpnPoAuthenClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoAuthenClientType.setStatus("current")


class _Hh3cDvpnPoSessionAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type hh3cDvpnPoSessionAlgorithmSuite based on DvpnAlgorithmSuite"""


_Hh3cDvpnPoSessionAlgorithmSuite_Object = MibTableColumn
hh3cDvpnPoSessionAlgorithmSuite = _Hh3cDvpnPoSessionAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 3),
    _Hh3cDvpnPoSessionAlgorithmSuite_Type()
)
hh3cDvpnPoSessionAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoSessionAlgorithmSuite.setStatus("current")


class _Hh3cDvpnPoSessionIdleTime_Type(Integer32):
    """Custom type hh3cDvpnPoSessionIdleTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_Hh3cDvpnPoSessionIdleTime_Type.__name__ = "Integer32"
_Hh3cDvpnPoSessionIdleTime_Object = MibTableColumn
hh3cDvpnPoSessionIdleTime = _Hh3cDvpnPoSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 4),
    _Hh3cDvpnPoSessionIdleTime_Type()
)
hh3cDvpnPoSessionIdleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoSessionIdleTime.setStatus("current")


class _Hh3cDvpnPoSessionKeepTime_Type(Integer32):
    """Custom type hh3cDvpnPoSessionKeepTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Hh3cDvpnPoSessionKeepTime_Type.__name__ = "Integer32"
_Hh3cDvpnPoSessionKeepTime_Object = MibTableColumn
hh3cDvpnPoSessionKeepTime = _Hh3cDvpnPoSessionKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 5),
    _Hh3cDvpnPoSessionKeepTime_Type()
)
hh3cDvpnPoSessionKeepTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoSessionKeepTime.setStatus("current")


class _Hh3cDvpnPoSessionSetupInterval_Type(Integer32):
    """Custom type hh3cDvpnPoSessionSetupInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_Hh3cDvpnPoSessionSetupInterval_Type.__name__ = "Integer32"
_Hh3cDvpnPoSessionSetupInterval_Object = MibTableColumn
hh3cDvpnPoSessionSetupInterval = _Hh3cDvpnPoSessionSetupInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 6),
    _Hh3cDvpnPoSessionSetupInterval_Type()
)
hh3cDvpnPoSessionSetupInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoSessionSetupInterval.setStatus("current")


class _Hh3cDvpnPoDataAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type hh3cDvpnPoDataAlgorithmSuite based on DvpnAlgorithmSuite"""


_Hh3cDvpnPoDataAlgorithmSuite_Object = MibTableColumn
hh3cDvpnPoDataAlgorithmSuite = _Hh3cDvpnPoDataAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 7),
    _Hh3cDvpnPoDataAlgorithmSuite_Type()
)
hh3cDvpnPoDataAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoDataAlgorithmSuite.setStatus("current")


class _Hh3cDvpnPoSaSeconds_Type(Integer32):
    """Custom type hh3cDvpnPoSaSeconds based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 604800),
    )


_Hh3cDvpnPoSaSeconds_Type.__name__ = "Integer32"
_Hh3cDvpnPoSaSeconds_Object = MibTableColumn
hh3cDvpnPoSaSeconds = _Hh3cDvpnPoSaSeconds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 8),
    _Hh3cDvpnPoSaSeconds_Type()
)
hh3cDvpnPoSaSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoSaSeconds.setStatus("current")


class _Hh3cDvpnPoUserDefAAADomain_Type(OctetString):
    """Custom type hh3cDvpnPoUserDefAAADomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Hh3cDvpnPoUserDefAAADomain_Type.__name__ = "OctetString"
_Hh3cDvpnPoUserDefAAADomain_Object = MibTableColumn
hh3cDvpnPoUserDefAAADomain = _Hh3cDvpnPoUserDefAAADomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 9),
    _Hh3cDvpnPoUserDefAAADomain_Type()
)
hh3cDvpnPoUserDefAAADomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoUserDefAAADomain.setStatus("current")
_Hh3cDvpnPoRefTimes_Type = Integer32
_Hh3cDvpnPoRefTimes_Object = MibTableColumn
hh3cDvpnPoRefTimes = _Hh3cDvpnPoRefTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 10),
    _Hh3cDvpnPoRefTimes_Type()
)
hh3cDvpnPoRefTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnPoRefTimes.setStatus("current")
_Hh3cDvpnPoRowStatus_Type = RowStatus
_Hh3cDvpnPoRowStatus_Object = MibTableColumn
hh3cDvpnPoRowStatus = _Hh3cDvpnPoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 1, 1, 11),
    _Hh3cDvpnPoRowStatus_Type()
)
hh3cDvpnPoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnPoRowStatus.setStatus("current")
_Hh3cDvpnDomainInfoTable_Object = MibTable
hh3cDvpnDomainInfoTable = _Hh3cDvpnDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDvpnDomainInfoTable.setStatus("current")
_Hh3cDvpnDomainInfoEntry_Object = MibTableRow
hh3cDvpnDomainInfoEntry = _Hh3cDvpnDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1)
)
hh3cDvpnDomainInfoEntry.setIndexNames(
    (0, "HH3C-DVPN-MIB", "hh3cDvpnDomainID"),
)
if mibBuilder.loadTexts:
    hh3cDvpnDomainInfoEntry.setStatus("current")


class _Hh3cDvpnDomainID_Type(Integer32):
    """Custom type hh3cDvpnDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDvpnDomainID_Type.__name__ = "Integer32"
_Hh3cDvpnDomainID_Object = MibTableColumn
hh3cDvpnDomainID = _Hh3cDvpnDomainID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 1),
    _Hh3cDvpnDomainID_Type()
)
hh3cDvpnDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDvpnDomainID.setStatus("current")
_Hh3cDvpnDomainSessionNum_Type = Unsigned32
_Hh3cDvpnDomainSessionNum_Object = MibTableColumn
hh3cDvpnDomainSessionNum = _Hh3cDvpnDomainSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 2),
    _Hh3cDvpnDomainSessionNum_Type()
)
hh3cDvpnDomainSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainSessionNum.setStatus("current")
_Hh3cDvpnDomainRedirectNum_Type = Unsigned32
_Hh3cDvpnDomainRedirectNum_Object = MibTableColumn
hh3cDvpnDomainRedirectNum = _Hh3cDvpnDomainRedirectNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 3),
    _Hh3cDvpnDomainRedirectNum_Type()
)
hh3cDvpnDomainRedirectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainRedirectNum.setStatus("current")
_Hh3cDvpnDomainInputPkt_Type = Unsigned32
_Hh3cDvpnDomainInputPkt_Object = MibTableColumn
hh3cDvpnDomainInputPkt = _Hh3cDvpnDomainInputPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 4),
    _Hh3cDvpnDomainInputPkt_Type()
)
hh3cDvpnDomainInputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainInputPkt.setStatus("current")
_Hh3cDvpnDomainDropPkt_Type = Unsigned32
_Hh3cDvpnDomainDropPkt_Object = MibTableColumn
hh3cDvpnDomainDropPkt = _Hh3cDvpnDomainDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 5),
    _Hh3cDvpnDomainDropPkt_Type()
)
hh3cDvpnDomainDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainDropPkt.setStatus("current")
_Hh3cDvpnDomainOutputPkt_Type = Unsigned32
_Hh3cDvpnDomainOutputPkt_Object = MibTableColumn
hh3cDvpnDomainOutputPkt = _Hh3cDvpnDomainOutputPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 6),
    _Hh3cDvpnDomainOutputPkt_Type()
)
hh3cDvpnDomainOutputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainOutputPkt.setStatus("current")
_Hh3cDvpnDomainOutputErrorPkt_Type = Unsigned32
_Hh3cDvpnDomainOutputErrorPkt_Object = MibTableColumn
hh3cDvpnDomainOutputErrorPkt = _Hh3cDvpnDomainOutputErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 7),
    _Hh3cDvpnDomainOutputErrorPkt_Type()
)
hh3cDvpnDomainOutputErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainOutputErrorPkt.setStatus("current")
_Hh3cDvpnDomainEncryptErrorPkt_Type = Unsigned32
_Hh3cDvpnDomainEncryptErrorPkt_Object = MibTableColumn
hh3cDvpnDomainEncryptErrorPkt = _Hh3cDvpnDomainEncryptErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 2, 1, 8),
    _Hh3cDvpnDomainEncryptErrorPkt_Type()
)
hh3cDvpnDomainEncryptErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnDomainEncryptErrorPkt.setStatus("current")
_Hh3cDvpnClassTable_Object = MibTable
hh3cDvpnClassTable = _Hh3cDvpnClassTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDvpnClassTable.setStatus("current")
_Hh3cDvpnClassEntry_Object = MibTableRow
hh3cDvpnClassEntry = _Hh3cDvpnClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1)
)
hh3cDvpnClassEntry.setIndexNames(
    (0, "HH3C-DVPN-MIB", "hh3cDvpnClassName"),
)
if mibBuilder.loadTexts:
    hh3cDvpnClassEntry.setStatus("current")


class _Hh3cDvpnClassName_Type(OctetString):
    """Custom type hh3cDvpnClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cDvpnClassName_Type.__name__ = "OctetString"
_Hh3cDvpnClassName_Object = MibTableColumn
hh3cDvpnClassName = _Hh3cDvpnClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 1),
    _Hh3cDvpnClassName_Type()
)
hh3cDvpnClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDvpnClassName.setStatus("current")
_Hh3cDvpnClServerPublicIpType_Type = InetAddressType
_Hh3cDvpnClServerPublicIpType_Object = MibTableColumn
hh3cDvpnClServerPublicIpType = _Hh3cDvpnClServerPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 2),
    _Hh3cDvpnClServerPublicIpType_Type()
)
hh3cDvpnClServerPublicIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClServerPublicIpType.setStatus("current")
_Hh3cDvpnClServerPublicIp_Type = InetAddress
_Hh3cDvpnClServerPublicIp_Object = MibTableColumn
hh3cDvpnClServerPublicIp = _Hh3cDvpnClServerPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 3),
    _Hh3cDvpnClServerPublicIp_Type()
)
hh3cDvpnClServerPublicIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClServerPublicIp.setStatus("current")
_Hh3cDvpnClServerPriIpType_Type = InetAddressType
_Hh3cDvpnClServerPriIpType_Object = MibTableColumn
hh3cDvpnClServerPriIpType = _Hh3cDvpnClServerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 4),
    _Hh3cDvpnClServerPriIpType_Type()
)
hh3cDvpnClServerPriIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClServerPriIpType.setStatus("current")
_Hh3cDvpnClServerPriIp_Type = InetAddress
_Hh3cDvpnClServerPriIp_Object = MibTableColumn
hh3cDvpnClServerPriIp = _Hh3cDvpnClServerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 5),
    _Hh3cDvpnClServerPriIp_Type()
)
hh3cDvpnClServerPriIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClServerPriIp.setStatus("current")


class _Hh3cDvpnClAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type hh3cDvpnClAlgorithmSuite based on DvpnAlgorithmSuite"""


_Hh3cDvpnClAlgorithmSuite_Object = MibTableColumn
hh3cDvpnClAlgorithmSuite = _Hh3cDvpnClAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 6),
    _Hh3cDvpnClAlgorithmSuite_Type()
)
hh3cDvpnClAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClAlgorithmSuite.setStatus("current")


class _Hh3cDvpnClAuthenServerType_Type(Integer32):
    """Custom type hh3cDvpnClAuthenServerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("preShareKey", 2))
    )


_Hh3cDvpnClAuthenServerType_Type.__name__ = "Integer32"
_Hh3cDvpnClAuthenServerType_Object = MibTableColumn
hh3cDvpnClAuthenServerType = _Hh3cDvpnClAuthenServerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 7),
    _Hh3cDvpnClAuthenServerType_Type()
)
hh3cDvpnClAuthenServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClAuthenServerType.setStatus("current")


class _Hh3cDvpnClPreShareKey_Type(OctetString):
    """Custom type hh3cDvpnClPreShareKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDvpnClPreShareKey_Type.__name__ = "OctetString"
_Hh3cDvpnClPreShareKey_Object = MibTableColumn
hh3cDvpnClPreShareKey = _Hh3cDvpnClPreShareKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 8),
    _Hh3cDvpnClPreShareKey_Type()
)
hh3cDvpnClPreShareKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClPreShareKey.setStatus("current")


class _Hh3cDvpnClUserName_Type(OctetString):
    """Custom type hh3cDvpnClUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hh3cDvpnClUserName_Type.__name__ = "OctetString"
_Hh3cDvpnClUserName_Object = MibTableColumn
hh3cDvpnClUserName = _Hh3cDvpnClUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 9),
    _Hh3cDvpnClUserName_Type()
)
hh3cDvpnClUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClUserName.setStatus("current")


class _Hh3cDvpnClPwdEncrypted_Type(Integer32):
    """Custom type hh3cDvpnClPwdEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_Hh3cDvpnClPwdEncrypted_Type.__name__ = "Integer32"
_Hh3cDvpnClPwdEncrypted_Object = MibTableColumn
hh3cDvpnClPwdEncrypted = _Hh3cDvpnClPwdEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 10),
    _Hh3cDvpnClPwdEncrypted_Type()
)
hh3cDvpnClPwdEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClPwdEncrypted.setStatus("current")
_Hh3cDvpnClPasswd_Type = OctetString
_Hh3cDvpnClPasswd_Object = MibTableColumn
hh3cDvpnClPasswd = _Hh3cDvpnClPasswd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 11),
    _Hh3cDvpnClPasswd_Type()
)
hh3cDvpnClPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClPasswd.setStatus("current")
_Hh3cDvpnClassRowStatus_Type = RowStatus
_Hh3cDvpnClassRowStatus_Object = MibTableColumn
hh3cDvpnClassRowStatus = _Hh3cDvpnClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 3, 1, 12),
    _Hh3cDvpnClassRowStatus_Type()
)
hh3cDvpnClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDvpnClassRowStatus.setStatus("current")
_Hh3cDvpnTunnelTable_Object = MibTable
hh3cDvpnTunnelTable = _Hh3cDvpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDvpnTunnelTable.setStatus("current")
_Hh3cDvpnTunnelEntry_Object = MibTableRow
hh3cDvpnTunnelEntry = _Hh3cDvpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1)
)
hh3cDvpnTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDvpnTunnelEntry.setStatus("current")


class _Hh3cDvpnTunnelInterfaceType_Type(Integer32):
    """Custom type hh3cDvpnTunnelInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_Hh3cDvpnTunnelInterfaceType_Type.__name__ = "Integer32"
_Hh3cDvpnTunnelInterfaceType_Object = MibTableColumn
hh3cDvpnTunnelInterfaceType = _Hh3cDvpnTunnelInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1, 1),
    _Hh3cDvpnTunnelInterfaceType_Type()
)
hh3cDvpnTunnelInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnTunnelInterfaceType.setStatus("current")
_Hh3cDvpnTunnelAcl_Type = Integer32
_Hh3cDvpnTunnelAcl_Object = MibTableColumn
hh3cDvpnTunnelAcl = _Hh3cDvpnTunnelAcl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1, 2),
    _Hh3cDvpnTunnelAcl_Type()
)
hh3cDvpnTunnelAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnTunnelAcl.setStatus("current")


class _Hh3cDvpnTunnelClientRegType_Type(Integer32):
    """Custom type hh3cDvpnTunnelClientRegType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("normal", 4),
          ("undistributed", 1),
          ("undistributedandforward", 3))
    )


_Hh3cDvpnTunnelClientRegType_Type.__name__ = "Integer32"
_Hh3cDvpnTunnelClientRegType_Object = MibTableColumn
hh3cDvpnTunnelClientRegType = _Hh3cDvpnTunnelClientRegType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1, 3),
    _Hh3cDvpnTunnelClientRegType_Type()
)
hh3cDvpnTunnelClientRegType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnTunnelClientRegType.setStatus("current")


class _Hh3cDvpnTunnelDvpnId_Type(Integer32):
    """Custom type hh3cDvpnTunnelDvpnId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDvpnTunnelDvpnId_Type.__name__ = "Integer32"
_Hh3cDvpnTunnelDvpnId_Object = MibTableColumn
hh3cDvpnTunnelDvpnId = _Hh3cDvpnTunnelDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1, 4),
    _Hh3cDvpnTunnelDvpnId_Type()
)
hh3cDvpnTunnelDvpnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnTunnelDvpnId.setStatus("current")


class _Hh3cDvpnTunnelPolicy_Type(OctetString):
    """Custom type hh3cDvpnTunnelPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDvpnTunnelPolicy_Type.__name__ = "OctetString"
_Hh3cDvpnTunnelPolicy_Object = MibTableColumn
hh3cDvpnTunnelPolicy = _Hh3cDvpnTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1, 5),
    _Hh3cDvpnTunnelPolicy_Type()
)
hh3cDvpnTunnelPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnTunnelPolicy.setStatus("current")


class _Hh3cDvpnTunnelClass_Type(OctetString):
    """Custom type hh3cDvpnTunnelClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDvpnTunnelClass_Type.__name__ = "OctetString"
_Hh3cDvpnTunnelClass_Object = MibTableColumn
hh3cDvpnTunnelClass = _Hh3cDvpnTunnelClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 4, 1, 6),
    _Hh3cDvpnTunnelClass_Type()
)
hh3cDvpnTunnelClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDvpnTunnelClass.setStatus("current")
_Hh3cDvpnMapTable_Object = MibTable
hh3cDvpnMapTable = _Hh3cDvpnMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDvpnMapTable.setStatus("current")
_Hh3cDvpnMapEntry_Object = MibTableRow
hh3cDvpnMapEntry = _Hh3cDvpnMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1)
)
hh3cDvpnMapEntry.setIndexNames(
    (0, "HH3C-DVPN-MIB", "hh3cDvpnMapIndex"),
)
if mibBuilder.loadTexts:
    hh3cDvpnMapEntry.setStatus("current")
_Hh3cDvpnMapIndex_Type = Unsigned32
_Hh3cDvpnMapIndex_Object = MibTableColumn
hh3cDvpnMapIndex = _Hh3cDvpnMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 1),
    _Hh3cDvpnMapIndex_Type()
)
hh3cDvpnMapIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDvpnMapIndex.setStatus("current")
_Hh3cDvpnMapPeerDeviceId_Type = OctetString
_Hh3cDvpnMapPeerDeviceId_Object = MibTableColumn
hh3cDvpnMapPeerDeviceId = _Hh3cDvpnMapPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 2),
    _Hh3cDvpnMapPeerDeviceId_Type()
)
hh3cDvpnMapPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapPeerDeviceId.setStatus("current")
_Hh3cDvpnMapDvpnId_Type = Unsigned32
_Hh3cDvpnMapDvpnId_Object = MibTableColumn
hh3cDvpnMapDvpnId = _Hh3cDvpnMapDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 3),
    _Hh3cDvpnMapDvpnId_Type()
)
hh3cDvpnMapDvpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapDvpnId.setStatus("current")
_Hh3cDvpnMapBuildTime_Type = TimeTicks
_Hh3cDvpnMapBuildTime_Object = MibTableColumn
hh3cDvpnMapBuildTime = _Hh3cDvpnMapBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 4),
    _Hh3cDvpnMapBuildTime_Type()
)
hh3cDvpnMapBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapBuildTime.setStatus("current")
_Hh3cDvpnMapPeerPriIpType_Type = InetAddressType
_Hh3cDvpnMapPeerPriIpType_Object = MibTableColumn
hh3cDvpnMapPeerPriIpType = _Hh3cDvpnMapPeerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 5),
    _Hh3cDvpnMapPeerPriIpType_Type()
)
hh3cDvpnMapPeerPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapPeerPriIpType.setStatus("current")
_Hh3cDvpnMapPeerPriIp_Type = InetAddress
_Hh3cDvpnMapPeerPriIp_Object = MibTableColumn
hh3cDvpnMapPeerPriIp = _Hh3cDvpnMapPeerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 6),
    _Hh3cDvpnMapPeerPriIp_Type()
)
hh3cDvpnMapPeerPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapPeerPriIp.setStatus("current")
_Hh3cDvpnMapPeerPublicIpType_Type = InetAddressType
_Hh3cDvpnMapPeerPublicIpType_Object = MibTableColumn
hh3cDvpnMapPeerPublicIpType = _Hh3cDvpnMapPeerPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 7),
    _Hh3cDvpnMapPeerPublicIpType_Type()
)
hh3cDvpnMapPeerPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapPeerPublicIpType.setStatus("current")
_Hh3cDvpnMapPeerPublicIp_Type = InetAddress
_Hh3cDvpnMapPeerPublicIp_Object = MibTableColumn
hh3cDvpnMapPeerPublicIp = _Hh3cDvpnMapPeerPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 8),
    _Hh3cDvpnMapPeerPublicIp_Type()
)
hh3cDvpnMapPeerPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapPeerPublicIp.setStatus("current")
_Hh3cDvpnMapLocalPriIpType_Type = InetAddressType
_Hh3cDvpnMapLocalPriIpType_Object = MibTableColumn
hh3cDvpnMapLocalPriIpType = _Hh3cDvpnMapLocalPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 9),
    _Hh3cDvpnMapLocalPriIpType_Type()
)
hh3cDvpnMapLocalPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapLocalPriIpType.setStatus("current")
_Hh3cDvpnMapLocalPriIp_Type = InetAddress
_Hh3cDvpnMapLocalPriIp_Object = MibTableColumn
hh3cDvpnMapLocalPriIp = _Hh3cDvpnMapLocalPriIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 10),
    _Hh3cDvpnMapLocalPriIp_Type()
)
hh3cDvpnMapLocalPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapLocalPriIp.setStatus("current")
_Hh3cDvpnMapLocalPublicIpType_Type = InetAddressType
_Hh3cDvpnMapLocalPublicIpType_Object = MibTableColumn
hh3cDvpnMapLocalPublicIpType = _Hh3cDvpnMapLocalPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 11),
    _Hh3cDvpnMapLocalPublicIpType_Type()
)
hh3cDvpnMapLocalPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapLocalPublicIpType.setStatus("current")
_Hh3cDvpnMapLocalPublicIp_Type = InetAddress
_Hh3cDvpnMapLocalPublicIp_Object = MibTableColumn
hh3cDvpnMapLocalPublicIp = _Hh3cDvpnMapLocalPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 12),
    _Hh3cDvpnMapLocalPublicIp_Type()
)
hh3cDvpnMapLocalPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapLocalPublicIp.setStatus("current")
_Hh3cDvpnMapUserName_Type = OctetString
_Hh3cDvpnMapUserName_Object = MibTableColumn
hh3cDvpnMapUserName = _Hh3cDvpnMapUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 13),
    _Hh3cDvpnMapUserName_Type()
)
hh3cDvpnMapUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapUserName.setStatus("current")
_Hh3cDvpnMapUdpPort_Type = Integer32
_Hh3cDvpnMapUdpPort_Object = MibTableColumn
hh3cDvpnMapUdpPort = _Hh3cDvpnMapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 14),
    _Hh3cDvpnMapUdpPort_Type()
)
hh3cDvpnMapUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapUdpPort.setStatus("current")
_Hh3cDvpnMapControlId_Type = Unsigned32
_Hh3cDvpnMapControlId_Object = MibTableColumn
hh3cDvpnMapControlId = _Hh3cDvpnMapControlId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 15),
    _Hh3cDvpnMapControlId_Type()
)
hh3cDvpnMapControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapControlId.setStatus("current")
_Hh3cDvpnMapType_Type = DvpnCommunicateType
_Hh3cDvpnMapType_Object = MibTableColumn
hh3cDvpnMapType = _Hh3cDvpnMapType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 16),
    _Hh3cDvpnMapType_Type()
)
hh3cDvpnMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapType.setStatus("current")


class _Hh3cDvpnMapState_Type(Integer32):
    """Custom type hh3cDvpnMapState based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("mapClientAlgreq", 3),
          ("mapClientAuthenReq", 5),
          ("mapClientBegin", 2),
          ("mapClientConfigReq", 6),
          ("mapClientInit", 1),
          ("mapClientKexReq", 4),
          ("mapClientReq", 7),
          ("mapClientSuccess", 8),
          ("mapServerAlgorithm", 10),
          ("mapServerAuthenInit", 12),
          ("mapServerBegin", 9),
          ("mapServerConfigInit", 13),
          ("mapServerFinished", 15),
          ("mapServerInit", 14),
          ("mapServerKexInit", 11))
    )


_Hh3cDvpnMapState_Type.__name__ = "Integer32"
_Hh3cDvpnMapState_Object = MibTableColumn
hh3cDvpnMapState = _Hh3cDvpnMapState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 5, 1, 17),
    _Hh3cDvpnMapState_Type()
)
hh3cDvpnMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnMapState.setStatus("current")
_Hh3cDvpnSessionTable_Object = MibTable
hh3cDvpnSessionTable = _Hh3cDvpnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionTable.setStatus("current")
_Hh3cDvpnSessionEntry_Object = MibTableRow
hh3cDvpnSessionEntry = _Hh3cDvpnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1)
)
hh3cDvpnSessionEntry.setIndexNames(
    (0, "HH3C-DVPN-MIB", "hh3cDvpnSessionDvpnId"),
    (0, "HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIpType"),
    (0, "HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIp"),
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionEntry.setStatus("current")
_Hh3cDvpnSessionDvpnId_Type = Integer32
_Hh3cDvpnSessionDvpnId_Object = MibTableColumn
hh3cDvpnSessionDvpnId = _Hh3cDvpnSessionDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 1),
    _Hh3cDvpnSessionDvpnId_Type()
)
hh3cDvpnSessionDvpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDvpnSessionDvpnId.setStatus("current")
_Hh3cDvpnSessionPeerPriIpType_Type = InetAddressType
_Hh3cDvpnSessionPeerPriIpType_Object = MibTableColumn
hh3cDvpnSessionPeerPriIpType = _Hh3cDvpnSessionPeerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 2),
    _Hh3cDvpnSessionPeerPriIpType_Type()
)
hh3cDvpnSessionPeerPriIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerPriIpType.setStatus("current")
_Hh3cDvpnSessionPeerPriIp_Type = InetAddress
_Hh3cDvpnSessionPeerPriIp_Object = MibTableColumn
hh3cDvpnSessionPeerPriIp = _Hh3cDvpnSessionPeerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 3),
    _Hh3cDvpnSessionPeerPriIp_Type()
)
hh3cDvpnSessionPeerPriIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerPriIp.setStatus("current")
_Hh3cDvpnSessionPeerDeviceId_Type = OctetString
_Hh3cDvpnSessionPeerDeviceId_Object = MibTableColumn
hh3cDvpnSessionPeerDeviceId = _Hh3cDvpnSessionPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 4),
    _Hh3cDvpnSessionPeerDeviceId_Type()
)
hh3cDvpnSessionPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerDeviceId.setStatus("current")
_Hh3cDvpnSessionBuildTime_Type = TimeTicks
_Hh3cDvpnSessionBuildTime_Object = MibTableColumn
hh3cDvpnSessionBuildTime = _Hh3cDvpnSessionBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 5),
    _Hh3cDvpnSessionBuildTime_Type()
)
hh3cDvpnSessionBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionBuildTime.setStatus("current")
_Hh3cDvpnSessionPeerPubIpType_Type = InetAddressType
_Hh3cDvpnSessionPeerPubIpType_Object = MibTableColumn
hh3cDvpnSessionPeerPubIpType = _Hh3cDvpnSessionPeerPubIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 6),
    _Hh3cDvpnSessionPeerPubIpType_Type()
)
hh3cDvpnSessionPeerPubIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerPubIpType.setStatus("current")
_Hh3cDvpnSessionPeerPubIp_Type = InetAddress
_Hh3cDvpnSessionPeerPubIp_Object = MibTableColumn
hh3cDvpnSessionPeerPubIp = _Hh3cDvpnSessionPeerPubIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 7),
    _Hh3cDvpnSessionPeerPubIp_Type()
)
hh3cDvpnSessionPeerPubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerPubIp.setStatus("current")
_Hh3cDvpnSessionLocalPubIpType_Type = InetAddressType
_Hh3cDvpnSessionLocalPubIpType_Object = MibTableColumn
hh3cDvpnSessionLocalPubIpType = _Hh3cDvpnSessionLocalPubIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 8),
    _Hh3cDvpnSessionLocalPubIpType_Type()
)
hh3cDvpnSessionLocalPubIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionLocalPubIpType.setStatus("current")
_Hh3cDvpnSessionLocalPubIp_Type = InetAddress
_Hh3cDvpnSessionLocalPubIp_Object = MibTableColumn
hh3cDvpnSessionLocalPubIp = _Hh3cDvpnSessionLocalPubIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 9),
    _Hh3cDvpnSessionLocalPubIp_Type()
)
hh3cDvpnSessionLocalPubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionLocalPubIp.setStatus("current")
_Hh3cDvpnSessionLocalPriIpType_Type = InetAddressType
_Hh3cDvpnSessionLocalPriIpType_Object = MibTableColumn
hh3cDvpnSessionLocalPriIpType = _Hh3cDvpnSessionLocalPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 10),
    _Hh3cDvpnSessionLocalPriIpType_Type()
)
hh3cDvpnSessionLocalPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionLocalPriIpType.setStatus("current")
_Hh3cDvpnSessionLocalPriIp_Type = InetAddress
_Hh3cDvpnSessionLocalPriIp_Object = MibTableColumn
hh3cDvpnSessionLocalPriIp = _Hh3cDvpnSessionLocalPriIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 11),
    _Hh3cDvpnSessionLocalPriIp_Type()
)
hh3cDvpnSessionLocalPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionLocalPriIp.setStatus("current")
_Hh3cDvpnSessionPeerUdpPort_Type = Integer32
_Hh3cDvpnSessionPeerUdpPort_Object = MibTableColumn
hh3cDvpnSessionPeerUdpPort = _Hh3cDvpnSessionPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 12),
    _Hh3cDvpnSessionPeerUdpPort_Type()
)
hh3cDvpnSessionPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerUdpPort.setStatus("current")


class _Hh3cDvpnSessionInitiator_Type(Integer32):
    """Custom type hh3cDvpnSessionInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Hh3cDvpnSessionInitiator_Type.__name__ = "Integer32"
_Hh3cDvpnSessionInitiator_Object = MibTableColumn
hh3cDvpnSessionInitiator = _Hh3cDvpnSessionInitiator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 13),
    _Hh3cDvpnSessionInitiator_Type()
)
hh3cDvpnSessionInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionInitiator.setStatus("current")
_Hh3cDvpnSessionUserName_Type = OctetString
_Hh3cDvpnSessionUserName_Object = MibTableColumn
hh3cDvpnSessionUserName = _Hh3cDvpnSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 14),
    _Hh3cDvpnSessionUserName_Type()
)
hh3cDvpnSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionUserName.setStatus("current")


class _Hh3cDvpnSessionState_Type(Integer32):
    """Custom type hh3cDvpnSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sessionRekeyRep", 5),
          ("sessionRekeyReq", 4),
          ("sessionSetupInit", 1),
          ("sessionSetupReq", 2),
          ("sessionSetupSuccess", 3))
    )


_Hh3cDvpnSessionState_Type.__name__ = "Integer32"
_Hh3cDvpnSessionState_Object = MibTableColumn
hh3cDvpnSessionState = _Hh3cDvpnSessionState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 15),
    _Hh3cDvpnSessionState_Type()
)
hh3cDvpnSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionState.setStatus("current")
_Hh3cDvpnSessionType_Type = DvpnCommunicateType
_Hh3cDvpnSessionType_Object = MibTableColumn
hh3cDvpnSessionType = _Hh3cDvpnSessionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 16),
    _Hh3cDvpnSessionType_Type()
)
hh3cDvpnSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionType.setStatus("current")


class _Hh3cDvpnSessionPeerType_Type(Integer32):
    """Custom type hh3cDvpnSessionPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pcClient", 2),
          ("router", 1))
    )


_Hh3cDvpnSessionPeerType_Type.__name__ = "Integer32"
_Hh3cDvpnSessionPeerType_Object = MibTableColumn
hh3cDvpnSessionPeerType = _Hh3cDvpnSessionPeerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 6, 1, 17),
    _Hh3cDvpnSessionPeerType_Type()
)
hh3cDvpnSessionPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionPeerType.setStatus("current")
_Hh3cDvpnSessionHisTable_Object = MibTable
hh3cDvpnSessionHisTable = _Hh3cDvpnSessionHisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisTable.setStatus("current")
_Hh3cDvpnSessionHisEntry_Object = MibTableRow
hh3cDvpnSessionHisEntry = _Hh3cDvpnSessionHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1)
)
hh3cDvpnSessionHisEntry.setIndexNames(
    (0, "HH3C-DVPN-MIB", "hh3cDvpnSessionHisDvpnID"),
    (0, "HH3C-DVPN-MIB", "hh3cDvpnSessionHisPeerPriIPType"),
    (0, "HH3C-DVPN-MIB", "hh3cDvpnSessionHisPeerPriIP"),
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisEntry.setStatus("current")


class _Hh3cDvpnSessionHisDvpnID_Type(Integer32):
    """Custom type hh3cDvpnSessionHisDvpnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDvpnSessionHisDvpnID_Type.__name__ = "Integer32"
_Hh3cDvpnSessionHisDvpnID_Object = MibTableColumn
hh3cDvpnSessionHisDvpnID = _Hh3cDvpnSessionHisDvpnID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 1),
    _Hh3cDvpnSessionHisDvpnID_Type()
)
hh3cDvpnSessionHisDvpnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisDvpnID.setStatus("current")
_Hh3cDvpnSessionHisPeerPriIPType_Type = InetAddressType
_Hh3cDvpnSessionHisPeerPriIPType_Object = MibTableColumn
hh3cDvpnSessionHisPeerPriIPType = _Hh3cDvpnSessionHisPeerPriIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 2),
    _Hh3cDvpnSessionHisPeerPriIPType_Type()
)
hh3cDvpnSessionHisPeerPriIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisPeerPriIPType.setStatus("current")
_Hh3cDvpnSessionHisPeerPriIP_Type = InetAddress
_Hh3cDvpnSessionHisPeerPriIP_Object = MibTableColumn
hh3cDvpnSessionHisPeerPriIP = _Hh3cDvpnSessionHisPeerPriIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 3),
    _Hh3cDvpnSessionHisPeerPriIP_Type()
)
hh3cDvpnSessionHisPeerPriIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisPeerPriIP.setStatus("current")
_Hh3cDvpnSessionHisSendPkt_Type = Unsigned32
_Hh3cDvpnSessionHisSendPkt_Object = MibTableColumn
hh3cDvpnSessionHisSendPkt = _Hh3cDvpnSessionHisSendPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 4),
    _Hh3cDvpnSessionHisSendPkt_Type()
)
hh3cDvpnSessionHisSendPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisSendPkt.setStatus("current")
_Hh3cDvpnSessionHisRcvPkt_Type = Unsigned32
_Hh3cDvpnSessionHisRcvPkt_Object = MibTableColumn
hh3cDvpnSessionHisRcvPkt = _Hh3cDvpnSessionHisRcvPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 5),
    _Hh3cDvpnSessionHisRcvPkt_Type()
)
hh3cDvpnSessionHisRcvPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisRcvPkt.setStatus("current")
_Hh3cDvpnSessionHisOnlineNumber_Type = Unsigned32
_Hh3cDvpnSessionHisOnlineNumber_Object = MibTableColumn
hh3cDvpnSessionHisOnlineNumber = _Hh3cDvpnSessionHisOnlineNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 6),
    _Hh3cDvpnSessionHisOnlineNumber_Type()
)
hh3cDvpnSessionHisOnlineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisOnlineNumber.setStatus("current")
_Hh3cDvpnSessionHisFirstUpTime_Type = TimeTicks
_Hh3cDvpnSessionHisFirstUpTime_Object = MibTableColumn
hh3cDvpnSessionHisFirstUpTime = _Hh3cDvpnSessionHisFirstUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 7),
    _Hh3cDvpnSessionHisFirstUpTime_Type()
)
hh3cDvpnSessionHisFirstUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisFirstUpTime.setStatus("current")
_Hh3cDvpnSessionHisLastUpTime_Type = TimeTicks
_Hh3cDvpnSessionHisLastUpTime_Object = MibTableColumn
hh3cDvpnSessionHisLastUpTime = _Hh3cDvpnSessionHisLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 8),
    _Hh3cDvpnSessionHisLastUpTime_Type()
)
hh3cDvpnSessionHisLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisLastUpTime.setStatus("current")
_Hh3cDvpnSessionHisLastDownTime_Type = TimeTicks
_Hh3cDvpnSessionHisLastDownTime_Object = MibTableColumn
hh3cDvpnSessionHisLastDownTime = _Hh3cDvpnSessionHisLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 9),
    _Hh3cDvpnSessionHisLastDownTime_Type()
)
hh3cDvpnSessionHisLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisLastDownTime.setStatus("current")


class _Hh3cDvpnSessionHisOnlineFlag_Type(Integer32):
    """Custom type hh3cDvpnSessionHisOnlineFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Hh3cDvpnSessionHisOnlineFlag_Type.__name__ = "Integer32"
_Hh3cDvpnSessionHisOnlineFlag_Object = MibTableColumn
hh3cDvpnSessionHisOnlineFlag = _Hh3cDvpnSessionHisOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 10),
    _Hh3cDvpnSessionHisOnlineFlag_Type()
)
hh3cDvpnSessionHisOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisOnlineFlag.setStatus("current")
_Hh3cDvpnSessionHisPeerDeviceId_Type = OctetString
_Hh3cDvpnSessionHisPeerDeviceId_Object = MibTableColumn
hh3cDvpnSessionHisPeerDeviceId = _Hh3cDvpnSessionHisPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 2, 7, 1, 11),
    _Hh3cDvpnSessionHisPeerDeviceId_Type()
)
hh3cDvpnSessionHisPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisPeerDeviceId.setStatus("current")
_Hh3cDvpnMibNotification_ObjectIdentity = ObjectIdentity
hh3cDvpnMibNotification = _Hh3cDvpnMibNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 3)
)
_Hh3cDvpnNotification_ObjectIdentity = ObjectIdentity
hh3cDvpnNotification = _Hh3cDvpnNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 3, 0)
)
_Hh3cDvpnMibConformance_ObjectIdentity = ObjectIdentity
hh3cDvpnMibConformance = _Hh3cDvpnMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4)
)
_Hh3cDvpnMibCompliances_ObjectIdentity = ObjectIdentity
hh3cDvpnMibCompliances = _Hh3cDvpnMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 1)
)
_Hh3cDvpnMibGroups_ObjectIdentity = ObjectIdentity
hh3cDvpnMibGroups = _Hh3cDvpnMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2)
)

# Managed Objects groups

hh3cDvpnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 1)
)
hh3cDvpnGlobalGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnServiceEnable"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClassNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClientNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapAgeTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClientRegisterInterval"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClientRegisterDumb"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClientRegisterRetry"),
        ("HH3C-DVPN-MIB", "hh3cDvpnInputPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDropPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnOutputPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnOutputErrorPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnEncryptErrorPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnCurrentDeviceRole"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnServerPreSharedKey"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapTrapEnable"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionTrapEnable"),
        ("HH3C-DVPN-MIB", "hh3cDvpnVersion"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClearDomainAllConection"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClearDvpnStaInfo"),
        ("HH3C-DVPN-MIB", "hh3cDvpnTotalRedirectNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnGlobalAuthenClientType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnGlobalUserDefAAADomain"),
        ("HH3C-DVPN-MIB", "hh3cDvpnLocalDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisAgeTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisReset"))
)
if mibBuilder.loadTexts:
    hh3cDvpnGlobalGroup.setStatus("current")

hh3cDvpnPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 2)
)
hh3cDvpnPolicyGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnPoAuthenClientType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoSessionAlgorithmSuite"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoSessionIdleTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoSessionKeepTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoSessionSetupInterval"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoDataAlgorithmSuite"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoSaSeconds"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoUserDefAAADomain"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoRefTimes"),
        ("HH3C-DVPN-MIB", "hh3cDvpnPoRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cDvpnPolicyGroup.setStatus("current")

hh3cDvpnDomainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 3)
)
hh3cDvpnDomainInfoGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnDomainSessionNum"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainRedirectNum"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainInputPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainDropPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainOutputPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainOutputErrorPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnDomainEncryptErrorPkt"))
)
if mibBuilder.loadTexts:
    hh3cDvpnDomainInfoGroup.setStatus("current")

hh3cDvpnClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 4)
)
hh3cDvpnClassGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnClServerPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClServerPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClServerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClServerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClAlgorithmSuite"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClAuthenServerType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClPreShareKey"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClUserName"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClPwdEncrypted"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClPasswd"),
        ("HH3C-DVPN-MIB", "hh3cDvpnClassRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cDvpnClassGroup.setStatus("current")

hh3cDvpnTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 5)
)
hh3cDvpnTunnelGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnTunnelInterfaceType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnTunnelAcl"),
        ("HH3C-DVPN-MIB", "hh3cDvpnTunnelClientRegType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnTunnelDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnTunnelPolicy"),
        ("HH3C-DVPN-MIB", "hh3cDvpnTunnelClass"))
)
if mibBuilder.loadTexts:
    hh3cDvpnTunnelGroup.setStatus("current")

hh3cDvpnMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 6)
)
hh3cDvpnMapGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnMapIndex"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapBuildTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapUserName"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapUdpPort"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapControlId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapState"))
)
if mibBuilder.loadTexts:
    hh3cDvpnMapGroup.setStatus("current")

hh3cDvpnSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 7)
)
hh3cDvpnSessionGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnSessionDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionBuildTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPubIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPubIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPubIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPubIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerUdpPort"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionInitiator"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionUserName"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionState"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerType"))
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionGroup.setStatus("current")

hh3cDvpnSessionHisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 8)
)
hh3cDvpnSessionHisGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnSessionHisPeerPriIPType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisSendPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisRcvPkt"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisOnlineNumber"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisFirstUpTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisLastUpTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisLastDownTime"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisOnlineFlag"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionHisPeerDeviceId"))
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionHisGroup.setStatus("current")

hh3cDvpnNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 2, 9)
)
hh3cDvpnNotificationGroup.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnSessionBuildNotification"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionDelNotification"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapBuildNotification"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapDelNotification"))
)
if mibBuilder.loadTexts:
    hh3cDvpnNotificationGroup.setStatus("current")


# Notification objects

hh3cDvpnSessionBuildNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 3, 0, 1)
)
hh3cDvpnSessionBuildNotification.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnSessionDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnLocalDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPubIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPubIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPubIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPubIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerUdpPort"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionUserName"))
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionBuildNotification.setStatus(
        "current"
    )

hh3cDvpnSessionDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 3, 0, 2)
)
hh3cDvpnSessionDelNotification.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnSessionDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnLocalDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPubIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionLocalPubIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPubIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerPubIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerUdpPort"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionPeerType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnSessionUserName"))
)
if mibBuilder.loadTexts:
    hh3cDvpnSessionDelNotification.setStatus(
        "current"
    )

hh3cDvpnMapBuildNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 3, 0, 3)
)
hh3cDvpnMapBuildNotification.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnMapIndex"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnLocalDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapUserName"))
)
if mibBuilder.loadTexts:
    hh3cDvpnMapBuildNotification.setStatus(
        "current"
    )

hh3cDvpnMapDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 3, 0, 4)
)
hh3cDvpnMapDelNotification.setObjects(
      *(("HH3C-DVPN-MIB", "hh3cDvpnMapIndex"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapDvpnId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapPeerPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnLocalDeviceId"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPriIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPriIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPublicIpType"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapLocalPublicIp"),
        ("HH3C-DVPN-MIB", "hh3cDvpnMapUserName"))
)
if mibBuilder.loadTexts:
    hh3cDvpnMapDelNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hh3cDvpnMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDvpnMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DVPN-MIB",
    **{"DvpnAlgorithmSuite": DvpnAlgorithmSuite,
       "DvpnCommunicateType": DvpnCommunicateType,
       "hh3cDvpn": hh3cDvpn,
       "hh3cDvpnMibObjects": hh3cDvpnMibObjects,
       "hh3cDvpnMibGlobal": hh3cDvpnMibGlobal,
       "hh3cDvpnServiceEnable": hh3cDvpnServiceEnable,
       "hh3cDvpnClassNumber": hh3cDvpnClassNumber,
       "hh3cDvpnClientNumber": hh3cDvpnClientNumber,
       "hh3cDvpnMapAgeTime": hh3cDvpnMapAgeTime,
       "hh3cDvpnClientRegisterInterval": hh3cDvpnClientRegisterInterval,
       "hh3cDvpnClientRegisterDumb": hh3cDvpnClientRegisterDumb,
       "hh3cDvpnClientRegisterRetry": hh3cDvpnClientRegisterRetry,
       "hh3cDvpnInputPkt": hh3cDvpnInputPkt,
       "hh3cDvpnDropPkt": hh3cDvpnDropPkt,
       "hh3cDvpnOutputPkt": hh3cDvpnOutputPkt,
       "hh3cDvpnOutputErrorPkt": hh3cDvpnOutputErrorPkt,
       "hh3cDvpnEncryptErrorPkt": hh3cDvpnEncryptErrorPkt,
       "hh3cDvpnCurrentDeviceRole": hh3cDvpnCurrentDeviceRole,
       "hh3cDvpnDomainNumber": hh3cDvpnDomainNumber,
       "hh3cDvpnMapNumber": hh3cDvpnMapNumber,
       "hh3cDvpnSessionNumber": hh3cDvpnSessionNumber,
       "hh3cDvpnServerPreSharedKey": hh3cDvpnServerPreSharedKey,
       "hh3cDvpnMapTrapEnable": hh3cDvpnMapTrapEnable,
       "hh3cDvpnSessionTrapEnable": hh3cDvpnSessionTrapEnable,
       "hh3cDvpnVersion": hh3cDvpnVersion,
       "hh3cDvpnClearDomainAllConection": hh3cDvpnClearDomainAllConection,
       "hh3cDvpnClearDvpnStaInfo": hh3cDvpnClearDvpnStaInfo,
       "hh3cDvpnTotalRedirectNumber": hh3cDvpnTotalRedirectNumber,
       "hh3cDvpnGlobalAuthenClientType": hh3cDvpnGlobalAuthenClientType,
       "hh3cDvpnGlobalUserDefAAADomain": hh3cDvpnGlobalUserDefAAADomain,
       "hh3cDvpnLocalDeviceId": hh3cDvpnLocalDeviceId,
       "hh3cDvpnSessionHisAgeTime": hh3cDvpnSessionHisAgeTime,
       "hh3cDvpnSessionHisReset": hh3cDvpnSessionHisReset,
       "hh3cDvpnMibTableTroop": hh3cDvpnMibTableTroop,
       "hh3cDvpnPolicyTable": hh3cDvpnPolicyTable,
       "hh3cDvpnPolicyEntry": hh3cDvpnPolicyEntry,
       "hh3cDvpnPolicyName": hh3cDvpnPolicyName,
       "hh3cDvpnPoAuthenClientType": hh3cDvpnPoAuthenClientType,
       "hh3cDvpnPoSessionAlgorithmSuite": hh3cDvpnPoSessionAlgorithmSuite,
       "hh3cDvpnPoSessionIdleTime": hh3cDvpnPoSessionIdleTime,
       "hh3cDvpnPoSessionKeepTime": hh3cDvpnPoSessionKeepTime,
       "hh3cDvpnPoSessionSetupInterval": hh3cDvpnPoSessionSetupInterval,
       "hh3cDvpnPoDataAlgorithmSuite": hh3cDvpnPoDataAlgorithmSuite,
       "hh3cDvpnPoSaSeconds": hh3cDvpnPoSaSeconds,
       "hh3cDvpnPoUserDefAAADomain": hh3cDvpnPoUserDefAAADomain,
       "hh3cDvpnPoRefTimes": hh3cDvpnPoRefTimes,
       "hh3cDvpnPoRowStatus": hh3cDvpnPoRowStatus,
       "hh3cDvpnDomainInfoTable": hh3cDvpnDomainInfoTable,
       "hh3cDvpnDomainInfoEntry": hh3cDvpnDomainInfoEntry,
       "hh3cDvpnDomainID": hh3cDvpnDomainID,
       "hh3cDvpnDomainSessionNum": hh3cDvpnDomainSessionNum,
       "hh3cDvpnDomainRedirectNum": hh3cDvpnDomainRedirectNum,
       "hh3cDvpnDomainInputPkt": hh3cDvpnDomainInputPkt,
       "hh3cDvpnDomainDropPkt": hh3cDvpnDomainDropPkt,
       "hh3cDvpnDomainOutputPkt": hh3cDvpnDomainOutputPkt,
       "hh3cDvpnDomainOutputErrorPkt": hh3cDvpnDomainOutputErrorPkt,
       "hh3cDvpnDomainEncryptErrorPkt": hh3cDvpnDomainEncryptErrorPkt,
       "hh3cDvpnClassTable": hh3cDvpnClassTable,
       "hh3cDvpnClassEntry": hh3cDvpnClassEntry,
       "hh3cDvpnClassName": hh3cDvpnClassName,
       "hh3cDvpnClServerPublicIpType": hh3cDvpnClServerPublicIpType,
       "hh3cDvpnClServerPublicIp": hh3cDvpnClServerPublicIp,
       "hh3cDvpnClServerPriIpType": hh3cDvpnClServerPriIpType,
       "hh3cDvpnClServerPriIp": hh3cDvpnClServerPriIp,
       "hh3cDvpnClAlgorithmSuite": hh3cDvpnClAlgorithmSuite,
       "hh3cDvpnClAuthenServerType": hh3cDvpnClAuthenServerType,
       "hh3cDvpnClPreShareKey": hh3cDvpnClPreShareKey,
       "hh3cDvpnClUserName": hh3cDvpnClUserName,
       "hh3cDvpnClPwdEncrypted": hh3cDvpnClPwdEncrypted,
       "hh3cDvpnClPasswd": hh3cDvpnClPasswd,
       "hh3cDvpnClassRowStatus": hh3cDvpnClassRowStatus,
       "hh3cDvpnTunnelTable": hh3cDvpnTunnelTable,
       "hh3cDvpnTunnelEntry": hh3cDvpnTunnelEntry,
       "hh3cDvpnTunnelInterfaceType": hh3cDvpnTunnelInterfaceType,
       "hh3cDvpnTunnelAcl": hh3cDvpnTunnelAcl,
       "hh3cDvpnTunnelClientRegType": hh3cDvpnTunnelClientRegType,
       "hh3cDvpnTunnelDvpnId": hh3cDvpnTunnelDvpnId,
       "hh3cDvpnTunnelPolicy": hh3cDvpnTunnelPolicy,
       "hh3cDvpnTunnelClass": hh3cDvpnTunnelClass,
       "hh3cDvpnMapTable": hh3cDvpnMapTable,
       "hh3cDvpnMapEntry": hh3cDvpnMapEntry,
       "hh3cDvpnMapIndex": hh3cDvpnMapIndex,
       "hh3cDvpnMapPeerDeviceId": hh3cDvpnMapPeerDeviceId,
       "hh3cDvpnMapDvpnId": hh3cDvpnMapDvpnId,
       "hh3cDvpnMapBuildTime": hh3cDvpnMapBuildTime,
       "hh3cDvpnMapPeerPriIpType": hh3cDvpnMapPeerPriIpType,
       "hh3cDvpnMapPeerPriIp": hh3cDvpnMapPeerPriIp,
       "hh3cDvpnMapPeerPublicIpType": hh3cDvpnMapPeerPublicIpType,
       "hh3cDvpnMapPeerPublicIp": hh3cDvpnMapPeerPublicIp,
       "hh3cDvpnMapLocalPriIpType": hh3cDvpnMapLocalPriIpType,
       "hh3cDvpnMapLocalPriIp": hh3cDvpnMapLocalPriIp,
       "hh3cDvpnMapLocalPublicIpType": hh3cDvpnMapLocalPublicIpType,
       "hh3cDvpnMapLocalPublicIp": hh3cDvpnMapLocalPublicIp,
       "hh3cDvpnMapUserName": hh3cDvpnMapUserName,
       "hh3cDvpnMapUdpPort": hh3cDvpnMapUdpPort,
       "hh3cDvpnMapControlId": hh3cDvpnMapControlId,
       "hh3cDvpnMapType": hh3cDvpnMapType,
       "hh3cDvpnMapState": hh3cDvpnMapState,
       "hh3cDvpnSessionTable": hh3cDvpnSessionTable,
       "hh3cDvpnSessionEntry": hh3cDvpnSessionEntry,
       "hh3cDvpnSessionDvpnId": hh3cDvpnSessionDvpnId,
       "hh3cDvpnSessionPeerPriIpType": hh3cDvpnSessionPeerPriIpType,
       "hh3cDvpnSessionPeerPriIp": hh3cDvpnSessionPeerPriIp,
       "hh3cDvpnSessionPeerDeviceId": hh3cDvpnSessionPeerDeviceId,
       "hh3cDvpnSessionBuildTime": hh3cDvpnSessionBuildTime,
       "hh3cDvpnSessionPeerPubIpType": hh3cDvpnSessionPeerPubIpType,
       "hh3cDvpnSessionPeerPubIp": hh3cDvpnSessionPeerPubIp,
       "hh3cDvpnSessionLocalPubIpType": hh3cDvpnSessionLocalPubIpType,
       "hh3cDvpnSessionLocalPubIp": hh3cDvpnSessionLocalPubIp,
       "hh3cDvpnSessionLocalPriIpType": hh3cDvpnSessionLocalPriIpType,
       "hh3cDvpnSessionLocalPriIp": hh3cDvpnSessionLocalPriIp,
       "hh3cDvpnSessionPeerUdpPort": hh3cDvpnSessionPeerUdpPort,
       "hh3cDvpnSessionInitiator": hh3cDvpnSessionInitiator,
       "hh3cDvpnSessionUserName": hh3cDvpnSessionUserName,
       "hh3cDvpnSessionState": hh3cDvpnSessionState,
       "hh3cDvpnSessionType": hh3cDvpnSessionType,
       "hh3cDvpnSessionPeerType": hh3cDvpnSessionPeerType,
       "hh3cDvpnSessionHisTable": hh3cDvpnSessionHisTable,
       "hh3cDvpnSessionHisEntry": hh3cDvpnSessionHisEntry,
       "hh3cDvpnSessionHisDvpnID": hh3cDvpnSessionHisDvpnID,
       "hh3cDvpnSessionHisPeerPriIPType": hh3cDvpnSessionHisPeerPriIPType,
       "hh3cDvpnSessionHisPeerPriIP": hh3cDvpnSessionHisPeerPriIP,
       "hh3cDvpnSessionHisSendPkt": hh3cDvpnSessionHisSendPkt,
       "hh3cDvpnSessionHisRcvPkt": hh3cDvpnSessionHisRcvPkt,
       "hh3cDvpnSessionHisOnlineNumber": hh3cDvpnSessionHisOnlineNumber,
       "hh3cDvpnSessionHisFirstUpTime": hh3cDvpnSessionHisFirstUpTime,
       "hh3cDvpnSessionHisLastUpTime": hh3cDvpnSessionHisLastUpTime,
       "hh3cDvpnSessionHisLastDownTime": hh3cDvpnSessionHisLastDownTime,
       "hh3cDvpnSessionHisOnlineFlag": hh3cDvpnSessionHisOnlineFlag,
       "hh3cDvpnSessionHisPeerDeviceId": hh3cDvpnSessionHisPeerDeviceId,
       "hh3cDvpnMibNotification": hh3cDvpnMibNotification,
       "hh3cDvpnNotification": hh3cDvpnNotification,
       "hh3cDvpnSessionBuildNotification": hh3cDvpnSessionBuildNotification,
       "hh3cDvpnSessionDelNotification": hh3cDvpnSessionDelNotification,
       "hh3cDvpnMapBuildNotification": hh3cDvpnMapBuildNotification,
       "hh3cDvpnMapDelNotification": hh3cDvpnMapDelNotification,
       "hh3cDvpnMibConformance": hh3cDvpnMibConformance,
       "hh3cDvpnMibCompliances": hh3cDvpnMibCompliances,
       "hh3cDvpnMibCompliance": hh3cDvpnMibCompliance,
       "hh3cDvpnMibGroups": hh3cDvpnMibGroups,
       "hh3cDvpnGlobalGroup": hh3cDvpnGlobalGroup,
       "hh3cDvpnPolicyGroup": hh3cDvpnPolicyGroup,
       "hh3cDvpnDomainInfoGroup": hh3cDvpnDomainInfoGroup,
       "hh3cDvpnClassGroup": hh3cDvpnClassGroup,
       "hh3cDvpnTunnelGroup": hh3cDvpnTunnelGroup,
       "hh3cDvpnMapGroup": hh3cDvpnMapGroup,
       "hh3cDvpnSessionGroup": hh3cDvpnSessionGroup,
       "hh3cDvpnSessionHisGroup": hh3cDvpnSessionHisGroup,
       "hh3cDvpnNotificationGroup": hh3cDvpnNotificationGroup}
)
