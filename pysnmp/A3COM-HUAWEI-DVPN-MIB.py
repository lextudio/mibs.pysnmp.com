# SNMP MIB module (A3COM-HUAWEI-DVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:47 2024
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

h3cDvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57)
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

_H3cDvpnMibObjects_ObjectIdentity = ObjectIdentity
h3cDvpnMibObjects = _H3cDvpnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1)
)
_H3cDvpnMibGlobal_ObjectIdentity = ObjectIdentity
h3cDvpnMibGlobal = _H3cDvpnMibGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1)
)


class _H3cDvpnServiceEnable_Type(Integer32):
    """Custom type h3cDvpnServiceEnable based on Integer32"""
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


_H3cDvpnServiceEnable_Type.__name__ = "Integer32"
_H3cDvpnServiceEnable_Object = MibScalar
h3cDvpnServiceEnable = _H3cDvpnServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 1),
    _H3cDvpnServiceEnable_Type()
)
h3cDvpnServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnServiceEnable.setStatus("current")


class _H3cDvpnClassNumber_Type(Integer32):
    """Custom type h3cDvpnClassNumber based on Integer32"""
    defaultValue = 0


_H3cDvpnClassNumber_Object = MibScalar
h3cDvpnClassNumber = _H3cDvpnClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 2),
    _H3cDvpnClassNumber_Type()
)
h3cDvpnClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnClassNumber.setStatus("current")


class _H3cDvpnClientNumber_Type(Integer32):
    """Custom type h3cDvpnClientNumber based on Integer32"""
    defaultValue = 0


_H3cDvpnClientNumber_Object = MibScalar
h3cDvpnClientNumber = _H3cDvpnClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 3),
    _H3cDvpnClientNumber_Type()
)
h3cDvpnClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnClientNumber.setStatus("current")


class _H3cDvpnMapAgeTime_Type(Integer32):
    """Custom type h3cDvpnMapAgeTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_H3cDvpnMapAgeTime_Type.__name__ = "Integer32"
_H3cDvpnMapAgeTime_Object = MibScalar
h3cDvpnMapAgeTime = _H3cDvpnMapAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 4),
    _H3cDvpnMapAgeTime_Type()
)
h3cDvpnMapAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnMapAgeTime.setStatus("current")


class _H3cDvpnClientRegisterInterval_Type(Integer32):
    """Custom type h3cDvpnClientRegisterInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_H3cDvpnClientRegisterInterval_Type.__name__ = "Integer32"
_H3cDvpnClientRegisterInterval_Object = MibScalar
h3cDvpnClientRegisterInterval = _H3cDvpnClientRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 5),
    _H3cDvpnClientRegisterInterval_Type()
)
h3cDvpnClientRegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnClientRegisterInterval.setStatus("current")


class _H3cDvpnClientRegisterDumb_Type(Integer32):
    """Custom type h3cDvpnClientRegisterDumb based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_H3cDvpnClientRegisterDumb_Type.__name__ = "Integer32"
_H3cDvpnClientRegisterDumb_Object = MibScalar
h3cDvpnClientRegisterDumb = _H3cDvpnClientRegisterDumb_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 6),
    _H3cDvpnClientRegisterDumb_Type()
)
h3cDvpnClientRegisterDumb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnClientRegisterDumb.setStatus("current")


class _H3cDvpnClientRegisterRetry_Type(Integer32):
    """Custom type h3cDvpnClientRegisterRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_H3cDvpnClientRegisterRetry_Type.__name__ = "Integer32"
_H3cDvpnClientRegisterRetry_Object = MibScalar
h3cDvpnClientRegisterRetry = _H3cDvpnClientRegisterRetry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 7),
    _H3cDvpnClientRegisterRetry_Type()
)
h3cDvpnClientRegisterRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnClientRegisterRetry.setStatus("current")


class _H3cDvpnInputPkt_Type(Unsigned32):
    """Custom type h3cDvpnInputPkt based on Unsigned32"""
    defaultValue = 0


_H3cDvpnInputPkt_Object = MibScalar
h3cDvpnInputPkt = _H3cDvpnInputPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 8),
    _H3cDvpnInputPkt_Type()
)
h3cDvpnInputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnInputPkt.setStatus("current")


class _H3cDvpnDropPkt_Type(Unsigned32):
    """Custom type h3cDvpnDropPkt based on Unsigned32"""
    defaultValue = 0


_H3cDvpnDropPkt_Object = MibScalar
h3cDvpnDropPkt = _H3cDvpnDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 9),
    _H3cDvpnDropPkt_Type()
)
h3cDvpnDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDropPkt.setStatus("current")


class _H3cDvpnOutputPkt_Type(Unsigned32):
    """Custom type h3cDvpnOutputPkt based on Unsigned32"""
    defaultValue = 0


_H3cDvpnOutputPkt_Object = MibScalar
h3cDvpnOutputPkt = _H3cDvpnOutputPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 10),
    _H3cDvpnOutputPkt_Type()
)
h3cDvpnOutputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnOutputPkt.setStatus("current")


class _H3cDvpnOutputErrorPkt_Type(Unsigned32):
    """Custom type h3cDvpnOutputErrorPkt based on Unsigned32"""
    defaultValue = 0


_H3cDvpnOutputErrorPkt_Object = MibScalar
h3cDvpnOutputErrorPkt = _H3cDvpnOutputErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 11),
    _H3cDvpnOutputErrorPkt_Type()
)
h3cDvpnOutputErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnOutputErrorPkt.setStatus("current")


class _H3cDvpnEncryptErrorPkt_Type(Unsigned32):
    """Custom type h3cDvpnEncryptErrorPkt based on Unsigned32"""
    defaultValue = 0


_H3cDvpnEncryptErrorPkt_Object = MibScalar
h3cDvpnEncryptErrorPkt = _H3cDvpnEncryptErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 12),
    _H3cDvpnEncryptErrorPkt_Type()
)
h3cDvpnEncryptErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnEncryptErrorPkt.setStatus("current")


class _H3cDvpnCurrentDeviceRole_Type(Integer32):
    """Custom type h3cDvpnCurrentDeviceRole based on Integer32"""
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


_H3cDvpnCurrentDeviceRole_Type.__name__ = "Integer32"
_H3cDvpnCurrentDeviceRole_Object = MibScalar
h3cDvpnCurrentDeviceRole = _H3cDvpnCurrentDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 13),
    _H3cDvpnCurrentDeviceRole_Type()
)
h3cDvpnCurrentDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnCurrentDeviceRole.setStatus("current")


class _H3cDvpnDomainNumber_Type(Integer32):
    """Custom type h3cDvpnDomainNumber based on Integer32"""
    defaultValue = 0


_H3cDvpnDomainNumber_Object = MibScalar
h3cDvpnDomainNumber = _H3cDvpnDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 14),
    _H3cDvpnDomainNumber_Type()
)
h3cDvpnDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainNumber.setStatus("current")


class _H3cDvpnMapNumber_Type(Integer32):
    """Custom type h3cDvpnMapNumber based on Integer32"""
    defaultValue = 0


_H3cDvpnMapNumber_Object = MibScalar
h3cDvpnMapNumber = _H3cDvpnMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 15),
    _H3cDvpnMapNumber_Type()
)
h3cDvpnMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapNumber.setStatus("current")


class _H3cDvpnSessionNumber_Type(Integer32):
    """Custom type h3cDvpnSessionNumber based on Integer32"""
    defaultValue = 0


_H3cDvpnSessionNumber_Object = MibScalar
h3cDvpnSessionNumber = _H3cDvpnSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 16),
    _H3cDvpnSessionNumber_Type()
)
h3cDvpnSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionNumber.setStatus("current")


class _H3cDvpnServerPreSharedKey_Type(OctetString):
    """Custom type h3cDvpnServerPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDvpnServerPreSharedKey_Type.__name__ = "OctetString"
_H3cDvpnServerPreSharedKey_Object = MibScalar
h3cDvpnServerPreSharedKey = _H3cDvpnServerPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 17),
    _H3cDvpnServerPreSharedKey_Type()
)
h3cDvpnServerPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnServerPreSharedKey.setStatus("current")


class _H3cDvpnMapTrapEnable_Type(Integer32):
    """Custom type h3cDvpnMapTrapEnable based on Integer32"""
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


_H3cDvpnMapTrapEnable_Type.__name__ = "Integer32"
_H3cDvpnMapTrapEnable_Object = MibScalar
h3cDvpnMapTrapEnable = _H3cDvpnMapTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 18),
    _H3cDvpnMapTrapEnable_Type()
)
h3cDvpnMapTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnMapTrapEnable.setStatus("current")


class _H3cDvpnSessionTrapEnable_Type(Integer32):
    """Custom type h3cDvpnSessionTrapEnable based on Integer32"""
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


_H3cDvpnSessionTrapEnable_Type.__name__ = "Integer32"
_H3cDvpnSessionTrapEnable_Object = MibScalar
h3cDvpnSessionTrapEnable = _H3cDvpnSessionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 19),
    _H3cDvpnSessionTrapEnable_Type()
)
h3cDvpnSessionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnSessionTrapEnable.setStatus("current")


class _H3cDvpnVersion_Type(Integer32):
    """Custom type h3cDvpnVersion based on Integer32"""
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


_H3cDvpnVersion_Type.__name__ = "Integer32"
_H3cDvpnVersion_Object = MibScalar
h3cDvpnVersion = _H3cDvpnVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 20),
    _H3cDvpnVersion_Type()
)
h3cDvpnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnVersion.setStatus("current")


class _H3cDvpnClearDomainAllConection_Type(Integer32):
    """Custom type h3cDvpnClearDomainAllConection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cDvpnClearDomainAllConection_Type.__name__ = "Integer32"
_H3cDvpnClearDomainAllConection_Object = MibScalar
h3cDvpnClearDomainAllConection = _H3cDvpnClearDomainAllConection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 21),
    _H3cDvpnClearDomainAllConection_Type()
)
h3cDvpnClearDomainAllConection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnClearDomainAllConection.setStatus("current")


class _H3cDvpnClearDvpnStaInfo_Type(Integer32):
    """Custom type h3cDvpnClearDvpnStaInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_H3cDvpnClearDvpnStaInfo_Type.__name__ = "Integer32"
_H3cDvpnClearDvpnStaInfo_Object = MibScalar
h3cDvpnClearDvpnStaInfo = _H3cDvpnClearDvpnStaInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 22),
    _H3cDvpnClearDvpnStaInfo_Type()
)
h3cDvpnClearDvpnStaInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnClearDvpnStaInfo.setStatus("current")


class _H3cDvpnTotalRedirectNumber_Type(Unsigned32):
    """Custom type h3cDvpnTotalRedirectNumber based on Unsigned32"""
    defaultValue = 0


_H3cDvpnTotalRedirectNumber_Object = MibScalar
h3cDvpnTotalRedirectNumber = _H3cDvpnTotalRedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 23),
    _H3cDvpnTotalRedirectNumber_Type()
)
h3cDvpnTotalRedirectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnTotalRedirectNumber.setStatus("current")


class _H3cDvpnGlobalAuthenClientType_Type(Integer32):
    """Custom type h3cDvpnGlobalAuthenClientType based on Integer32"""
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


_H3cDvpnGlobalAuthenClientType_Type.__name__ = "Integer32"
_H3cDvpnGlobalAuthenClientType_Object = MibScalar
h3cDvpnGlobalAuthenClientType = _H3cDvpnGlobalAuthenClientType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 24),
    _H3cDvpnGlobalAuthenClientType_Type()
)
h3cDvpnGlobalAuthenClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnGlobalAuthenClientType.setStatus("current")


class _H3cDvpnGlobalUserDefAAADomain_Type(OctetString):
    """Custom type h3cDvpnGlobalUserDefAAADomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_H3cDvpnGlobalUserDefAAADomain_Type.__name__ = "OctetString"
_H3cDvpnGlobalUserDefAAADomain_Object = MibScalar
h3cDvpnGlobalUserDefAAADomain = _H3cDvpnGlobalUserDefAAADomain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 25),
    _H3cDvpnGlobalUserDefAAADomain_Type()
)
h3cDvpnGlobalUserDefAAADomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnGlobalUserDefAAADomain.setStatus("current")
_H3cDvpnLocalDeviceId_Type = OctetString
_H3cDvpnLocalDeviceId_Object = MibScalar
h3cDvpnLocalDeviceId = _H3cDvpnLocalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 26),
    _H3cDvpnLocalDeviceId_Type()
)
h3cDvpnLocalDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnLocalDeviceId.setStatus("current")


class _H3cDvpnSessionHisAgeTime_Type(Integer32):
    """Custom type h3cDvpnSessionHisAgeTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cDvpnSessionHisAgeTime_Type.__name__ = "Integer32"
_H3cDvpnSessionHisAgeTime_Object = MibScalar
h3cDvpnSessionHisAgeTime = _H3cDvpnSessionHisAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 27),
    _H3cDvpnSessionHisAgeTime_Type()
)
h3cDvpnSessionHisAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisAgeTime.setStatus("current")


class _H3cDvpnSessionHisReset_Type(Integer32):
    """Custom type h3cDvpnSessionHisReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_H3cDvpnSessionHisReset_Type.__name__ = "Integer32"
_H3cDvpnSessionHisReset_Object = MibScalar
h3cDvpnSessionHisReset = _H3cDvpnSessionHisReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 1, 28),
    _H3cDvpnSessionHisReset_Type()
)
h3cDvpnSessionHisReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisReset.setStatus("current")
_H3cDvpnMibTableTroop_ObjectIdentity = ObjectIdentity
h3cDvpnMibTableTroop = _H3cDvpnMibTableTroop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2)
)
_H3cDvpnPolicyTable_Object = MibTable
h3cDvpnPolicyTable = _H3cDvpnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDvpnPolicyTable.setStatus("current")
_H3cDvpnPolicyEntry_Object = MibTableRow
h3cDvpnPolicyEntry = _H3cDvpnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1)
)
h3cDvpnPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPolicyName"),
)
if mibBuilder.loadTexts:
    h3cDvpnPolicyEntry.setStatus("current")


class _H3cDvpnPolicyName_Type(OctetString):
    """Custom type h3cDvpnPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cDvpnPolicyName_Type.__name__ = "OctetString"
_H3cDvpnPolicyName_Object = MibTableColumn
h3cDvpnPolicyName = _H3cDvpnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 1),
    _H3cDvpnPolicyName_Type()
)
h3cDvpnPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDvpnPolicyName.setStatus("current")


class _H3cDvpnPoAuthenClientType_Type(Integer32):
    """Custom type h3cDvpnPoAuthenClientType based on Integer32"""
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


_H3cDvpnPoAuthenClientType_Type.__name__ = "Integer32"
_H3cDvpnPoAuthenClientType_Object = MibTableColumn
h3cDvpnPoAuthenClientType = _H3cDvpnPoAuthenClientType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 2),
    _H3cDvpnPoAuthenClientType_Type()
)
h3cDvpnPoAuthenClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoAuthenClientType.setStatus("current")


class _H3cDvpnPoSessionAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type h3cDvpnPoSessionAlgorithmSuite based on DvpnAlgorithmSuite"""


_H3cDvpnPoSessionAlgorithmSuite_Object = MibTableColumn
h3cDvpnPoSessionAlgorithmSuite = _H3cDvpnPoSessionAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 3),
    _H3cDvpnPoSessionAlgorithmSuite_Type()
)
h3cDvpnPoSessionAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoSessionAlgorithmSuite.setStatus("current")


class _H3cDvpnPoSessionIdleTime_Type(Integer32):
    """Custom type h3cDvpnPoSessionIdleTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_H3cDvpnPoSessionIdleTime_Type.__name__ = "Integer32"
_H3cDvpnPoSessionIdleTime_Object = MibTableColumn
h3cDvpnPoSessionIdleTime = _H3cDvpnPoSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 4),
    _H3cDvpnPoSessionIdleTime_Type()
)
h3cDvpnPoSessionIdleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoSessionIdleTime.setStatus("current")


class _H3cDvpnPoSessionKeepTime_Type(Integer32):
    """Custom type h3cDvpnPoSessionKeepTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_H3cDvpnPoSessionKeepTime_Type.__name__ = "Integer32"
_H3cDvpnPoSessionKeepTime_Object = MibTableColumn
h3cDvpnPoSessionKeepTime = _H3cDvpnPoSessionKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 5),
    _H3cDvpnPoSessionKeepTime_Type()
)
h3cDvpnPoSessionKeepTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoSessionKeepTime.setStatus("current")


class _H3cDvpnPoSessionSetupInterval_Type(Integer32):
    """Custom type h3cDvpnPoSessionSetupInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_H3cDvpnPoSessionSetupInterval_Type.__name__ = "Integer32"
_H3cDvpnPoSessionSetupInterval_Object = MibTableColumn
h3cDvpnPoSessionSetupInterval = _H3cDvpnPoSessionSetupInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 6),
    _H3cDvpnPoSessionSetupInterval_Type()
)
h3cDvpnPoSessionSetupInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoSessionSetupInterval.setStatus("current")


class _H3cDvpnPoDataAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type h3cDvpnPoDataAlgorithmSuite based on DvpnAlgorithmSuite"""


_H3cDvpnPoDataAlgorithmSuite_Object = MibTableColumn
h3cDvpnPoDataAlgorithmSuite = _H3cDvpnPoDataAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 7),
    _H3cDvpnPoDataAlgorithmSuite_Type()
)
h3cDvpnPoDataAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoDataAlgorithmSuite.setStatus("current")


class _H3cDvpnPoSaSeconds_Type(Integer32):
    """Custom type h3cDvpnPoSaSeconds based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 604800),
    )


_H3cDvpnPoSaSeconds_Type.__name__ = "Integer32"
_H3cDvpnPoSaSeconds_Object = MibTableColumn
h3cDvpnPoSaSeconds = _H3cDvpnPoSaSeconds_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 8),
    _H3cDvpnPoSaSeconds_Type()
)
h3cDvpnPoSaSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoSaSeconds.setStatus("current")


class _H3cDvpnPoUserDefAAADomain_Type(OctetString):
    """Custom type h3cDvpnPoUserDefAAADomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_H3cDvpnPoUserDefAAADomain_Type.__name__ = "OctetString"
_H3cDvpnPoUserDefAAADomain_Object = MibTableColumn
h3cDvpnPoUserDefAAADomain = _H3cDvpnPoUserDefAAADomain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 9),
    _H3cDvpnPoUserDefAAADomain_Type()
)
h3cDvpnPoUserDefAAADomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoUserDefAAADomain.setStatus("current")
_H3cDvpnPoRefTimes_Type = Integer32
_H3cDvpnPoRefTimes_Object = MibTableColumn
h3cDvpnPoRefTimes = _H3cDvpnPoRefTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 10),
    _H3cDvpnPoRefTimes_Type()
)
h3cDvpnPoRefTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnPoRefTimes.setStatus("current")
_H3cDvpnPoRowStatus_Type = RowStatus
_H3cDvpnPoRowStatus_Object = MibTableColumn
h3cDvpnPoRowStatus = _H3cDvpnPoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 1, 1, 11),
    _H3cDvpnPoRowStatus_Type()
)
h3cDvpnPoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnPoRowStatus.setStatus("current")
_H3cDvpnDomainInfoTable_Object = MibTable
h3cDvpnDomainInfoTable = _H3cDvpnDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDvpnDomainInfoTable.setStatus("current")
_H3cDvpnDomainInfoEntry_Object = MibTableRow
h3cDvpnDomainInfoEntry = _H3cDvpnDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1)
)
h3cDvpnDomainInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainID"),
)
if mibBuilder.loadTexts:
    h3cDvpnDomainInfoEntry.setStatus("current")


class _H3cDvpnDomainID_Type(Integer32):
    """Custom type h3cDvpnDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cDvpnDomainID_Type.__name__ = "Integer32"
_H3cDvpnDomainID_Object = MibTableColumn
h3cDvpnDomainID = _H3cDvpnDomainID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 1),
    _H3cDvpnDomainID_Type()
)
h3cDvpnDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDvpnDomainID.setStatus("current")
_H3cDvpnDomainSessionNum_Type = Unsigned32
_H3cDvpnDomainSessionNum_Object = MibTableColumn
h3cDvpnDomainSessionNum = _H3cDvpnDomainSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 2),
    _H3cDvpnDomainSessionNum_Type()
)
h3cDvpnDomainSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainSessionNum.setStatus("current")
_H3cDvpnDomainRedirectNum_Type = Unsigned32
_H3cDvpnDomainRedirectNum_Object = MibTableColumn
h3cDvpnDomainRedirectNum = _H3cDvpnDomainRedirectNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 3),
    _H3cDvpnDomainRedirectNum_Type()
)
h3cDvpnDomainRedirectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainRedirectNum.setStatus("current")
_H3cDvpnDomainInputPkt_Type = Unsigned32
_H3cDvpnDomainInputPkt_Object = MibTableColumn
h3cDvpnDomainInputPkt = _H3cDvpnDomainInputPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 4),
    _H3cDvpnDomainInputPkt_Type()
)
h3cDvpnDomainInputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainInputPkt.setStatus("current")
_H3cDvpnDomainDropPkt_Type = Unsigned32
_H3cDvpnDomainDropPkt_Object = MibTableColumn
h3cDvpnDomainDropPkt = _H3cDvpnDomainDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 5),
    _H3cDvpnDomainDropPkt_Type()
)
h3cDvpnDomainDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainDropPkt.setStatus("current")
_H3cDvpnDomainOutputPkt_Type = Unsigned32
_H3cDvpnDomainOutputPkt_Object = MibTableColumn
h3cDvpnDomainOutputPkt = _H3cDvpnDomainOutputPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 6),
    _H3cDvpnDomainOutputPkt_Type()
)
h3cDvpnDomainOutputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainOutputPkt.setStatus("current")
_H3cDvpnDomainOutputErrorPkt_Type = Unsigned32
_H3cDvpnDomainOutputErrorPkt_Object = MibTableColumn
h3cDvpnDomainOutputErrorPkt = _H3cDvpnDomainOutputErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 7),
    _H3cDvpnDomainOutputErrorPkt_Type()
)
h3cDvpnDomainOutputErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainOutputErrorPkt.setStatus("current")
_H3cDvpnDomainEncryptErrorPkt_Type = Unsigned32
_H3cDvpnDomainEncryptErrorPkt_Object = MibTableColumn
h3cDvpnDomainEncryptErrorPkt = _H3cDvpnDomainEncryptErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 2, 1, 8),
    _H3cDvpnDomainEncryptErrorPkt_Type()
)
h3cDvpnDomainEncryptErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnDomainEncryptErrorPkt.setStatus("current")
_H3cDvpnClassTable_Object = MibTable
h3cDvpnClassTable = _H3cDvpnClassTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDvpnClassTable.setStatus("current")
_H3cDvpnClassEntry_Object = MibTableRow
h3cDvpnClassEntry = _H3cDvpnClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1)
)
h3cDvpnClassEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClassName"),
)
if mibBuilder.loadTexts:
    h3cDvpnClassEntry.setStatus("current")


class _H3cDvpnClassName_Type(OctetString):
    """Custom type h3cDvpnClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cDvpnClassName_Type.__name__ = "OctetString"
_H3cDvpnClassName_Object = MibTableColumn
h3cDvpnClassName = _H3cDvpnClassName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 1),
    _H3cDvpnClassName_Type()
)
h3cDvpnClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDvpnClassName.setStatus("current")
_H3cDvpnClServerPublicIpType_Type = InetAddressType
_H3cDvpnClServerPublicIpType_Object = MibTableColumn
h3cDvpnClServerPublicIpType = _H3cDvpnClServerPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 2),
    _H3cDvpnClServerPublicIpType_Type()
)
h3cDvpnClServerPublicIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClServerPublicIpType.setStatus("current")
_H3cDvpnClServerPublicIp_Type = InetAddress
_H3cDvpnClServerPublicIp_Object = MibTableColumn
h3cDvpnClServerPublicIp = _H3cDvpnClServerPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 3),
    _H3cDvpnClServerPublicIp_Type()
)
h3cDvpnClServerPublicIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClServerPublicIp.setStatus("current")
_H3cDvpnClServerPriIpType_Type = InetAddressType
_H3cDvpnClServerPriIpType_Object = MibTableColumn
h3cDvpnClServerPriIpType = _H3cDvpnClServerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 4),
    _H3cDvpnClServerPriIpType_Type()
)
h3cDvpnClServerPriIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClServerPriIpType.setStatus("current")
_H3cDvpnClServerPriIp_Type = InetAddress
_H3cDvpnClServerPriIp_Object = MibTableColumn
h3cDvpnClServerPriIp = _H3cDvpnClServerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 5),
    _H3cDvpnClServerPriIp_Type()
)
h3cDvpnClServerPriIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClServerPriIp.setStatus("current")


class _H3cDvpnClAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type h3cDvpnClAlgorithmSuite based on DvpnAlgorithmSuite"""


_H3cDvpnClAlgorithmSuite_Object = MibTableColumn
h3cDvpnClAlgorithmSuite = _H3cDvpnClAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 6),
    _H3cDvpnClAlgorithmSuite_Type()
)
h3cDvpnClAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClAlgorithmSuite.setStatus("current")


class _H3cDvpnClAuthenServerType_Type(Integer32):
    """Custom type h3cDvpnClAuthenServerType based on Integer32"""
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


_H3cDvpnClAuthenServerType_Type.__name__ = "Integer32"
_H3cDvpnClAuthenServerType_Object = MibTableColumn
h3cDvpnClAuthenServerType = _H3cDvpnClAuthenServerType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 7),
    _H3cDvpnClAuthenServerType_Type()
)
h3cDvpnClAuthenServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClAuthenServerType.setStatus("current")


class _H3cDvpnClPreShareKey_Type(OctetString):
    """Custom type h3cDvpnClPreShareKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDvpnClPreShareKey_Type.__name__ = "OctetString"
_H3cDvpnClPreShareKey_Object = MibTableColumn
h3cDvpnClPreShareKey = _H3cDvpnClPreShareKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 8),
    _H3cDvpnClPreShareKey_Type()
)
h3cDvpnClPreShareKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClPreShareKey.setStatus("current")


class _H3cDvpnClUserName_Type(OctetString):
    """Custom type h3cDvpnClUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_H3cDvpnClUserName_Type.__name__ = "OctetString"
_H3cDvpnClUserName_Object = MibTableColumn
h3cDvpnClUserName = _H3cDvpnClUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 9),
    _H3cDvpnClUserName_Type()
)
h3cDvpnClUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClUserName.setStatus("current")


class _H3cDvpnClPwdEncrypted_Type(Integer32):
    """Custom type h3cDvpnClPwdEncrypted based on Integer32"""
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


_H3cDvpnClPwdEncrypted_Type.__name__ = "Integer32"
_H3cDvpnClPwdEncrypted_Object = MibTableColumn
h3cDvpnClPwdEncrypted = _H3cDvpnClPwdEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 10),
    _H3cDvpnClPwdEncrypted_Type()
)
h3cDvpnClPwdEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClPwdEncrypted.setStatus("current")
_H3cDvpnClPasswd_Type = OctetString
_H3cDvpnClPasswd_Object = MibTableColumn
h3cDvpnClPasswd = _H3cDvpnClPasswd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 11),
    _H3cDvpnClPasswd_Type()
)
h3cDvpnClPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClPasswd.setStatus("current")
_H3cDvpnClassRowStatus_Type = RowStatus
_H3cDvpnClassRowStatus_Object = MibTableColumn
h3cDvpnClassRowStatus = _H3cDvpnClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 3, 1, 12),
    _H3cDvpnClassRowStatus_Type()
)
h3cDvpnClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDvpnClassRowStatus.setStatus("current")
_H3cDvpnTunnelTable_Object = MibTable
h3cDvpnTunnelTable = _H3cDvpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cDvpnTunnelTable.setStatus("current")
_H3cDvpnTunnelEntry_Object = MibTableRow
h3cDvpnTunnelEntry = _H3cDvpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1)
)
h3cDvpnTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDvpnTunnelEntry.setStatus("current")


class _H3cDvpnTunnelInterfaceType_Type(Integer32):
    """Custom type h3cDvpnTunnelInterfaceType based on Integer32"""
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


_H3cDvpnTunnelInterfaceType_Type.__name__ = "Integer32"
_H3cDvpnTunnelInterfaceType_Object = MibTableColumn
h3cDvpnTunnelInterfaceType = _H3cDvpnTunnelInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1, 1),
    _H3cDvpnTunnelInterfaceType_Type()
)
h3cDvpnTunnelInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnTunnelInterfaceType.setStatus("current")
_H3cDvpnTunnelAcl_Type = Integer32
_H3cDvpnTunnelAcl_Object = MibTableColumn
h3cDvpnTunnelAcl = _H3cDvpnTunnelAcl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1, 2),
    _H3cDvpnTunnelAcl_Type()
)
h3cDvpnTunnelAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnTunnelAcl.setStatus("current")


class _H3cDvpnTunnelClientRegType_Type(Integer32):
    """Custom type h3cDvpnTunnelClientRegType based on Integer32"""
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


_H3cDvpnTunnelClientRegType_Type.__name__ = "Integer32"
_H3cDvpnTunnelClientRegType_Object = MibTableColumn
h3cDvpnTunnelClientRegType = _H3cDvpnTunnelClientRegType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1, 3),
    _H3cDvpnTunnelClientRegType_Type()
)
h3cDvpnTunnelClientRegType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnTunnelClientRegType.setStatus("current")


class _H3cDvpnTunnelDvpnId_Type(Integer32):
    """Custom type h3cDvpnTunnelDvpnId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDvpnTunnelDvpnId_Type.__name__ = "Integer32"
_H3cDvpnTunnelDvpnId_Object = MibTableColumn
h3cDvpnTunnelDvpnId = _H3cDvpnTunnelDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1, 4),
    _H3cDvpnTunnelDvpnId_Type()
)
h3cDvpnTunnelDvpnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnTunnelDvpnId.setStatus("current")


class _H3cDvpnTunnelPolicy_Type(OctetString):
    """Custom type h3cDvpnTunnelPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cDvpnTunnelPolicy_Type.__name__ = "OctetString"
_H3cDvpnTunnelPolicy_Object = MibTableColumn
h3cDvpnTunnelPolicy = _H3cDvpnTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1, 5),
    _H3cDvpnTunnelPolicy_Type()
)
h3cDvpnTunnelPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnTunnelPolicy.setStatus("current")


class _H3cDvpnTunnelClass_Type(OctetString):
    """Custom type h3cDvpnTunnelClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cDvpnTunnelClass_Type.__name__ = "OctetString"
_H3cDvpnTunnelClass_Object = MibTableColumn
h3cDvpnTunnelClass = _H3cDvpnTunnelClass_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 4, 1, 6),
    _H3cDvpnTunnelClass_Type()
)
h3cDvpnTunnelClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDvpnTunnelClass.setStatus("current")
_H3cDvpnMapTable_Object = MibTable
h3cDvpnMapTable = _H3cDvpnMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5)
)
if mibBuilder.loadTexts:
    h3cDvpnMapTable.setStatus("current")
_H3cDvpnMapEntry_Object = MibTableRow
h3cDvpnMapEntry = _H3cDvpnMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1)
)
h3cDvpnMapEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapIndex"),
)
if mibBuilder.loadTexts:
    h3cDvpnMapEntry.setStatus("current")
_H3cDvpnMapIndex_Type = Unsigned32
_H3cDvpnMapIndex_Object = MibTableColumn
h3cDvpnMapIndex = _H3cDvpnMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 1),
    _H3cDvpnMapIndex_Type()
)
h3cDvpnMapIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDvpnMapIndex.setStatus("current")
_H3cDvpnMapPeerDeviceId_Type = OctetString
_H3cDvpnMapPeerDeviceId_Object = MibTableColumn
h3cDvpnMapPeerDeviceId = _H3cDvpnMapPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 2),
    _H3cDvpnMapPeerDeviceId_Type()
)
h3cDvpnMapPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapPeerDeviceId.setStatus("current")
_H3cDvpnMapDvpnId_Type = Unsigned32
_H3cDvpnMapDvpnId_Object = MibTableColumn
h3cDvpnMapDvpnId = _H3cDvpnMapDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 3),
    _H3cDvpnMapDvpnId_Type()
)
h3cDvpnMapDvpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapDvpnId.setStatus("current")
_H3cDvpnMapBuildTime_Type = TimeTicks
_H3cDvpnMapBuildTime_Object = MibTableColumn
h3cDvpnMapBuildTime = _H3cDvpnMapBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 4),
    _H3cDvpnMapBuildTime_Type()
)
h3cDvpnMapBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapBuildTime.setStatus("current")
_H3cDvpnMapPeerPriIpType_Type = InetAddressType
_H3cDvpnMapPeerPriIpType_Object = MibTableColumn
h3cDvpnMapPeerPriIpType = _H3cDvpnMapPeerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 5),
    _H3cDvpnMapPeerPriIpType_Type()
)
h3cDvpnMapPeerPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapPeerPriIpType.setStatus("current")
_H3cDvpnMapPeerPriIp_Type = InetAddress
_H3cDvpnMapPeerPriIp_Object = MibTableColumn
h3cDvpnMapPeerPriIp = _H3cDvpnMapPeerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 6),
    _H3cDvpnMapPeerPriIp_Type()
)
h3cDvpnMapPeerPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapPeerPriIp.setStatus("current")
_H3cDvpnMapPeerPublicIpType_Type = InetAddressType
_H3cDvpnMapPeerPublicIpType_Object = MibTableColumn
h3cDvpnMapPeerPublicIpType = _H3cDvpnMapPeerPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 7),
    _H3cDvpnMapPeerPublicIpType_Type()
)
h3cDvpnMapPeerPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapPeerPublicIpType.setStatus("current")
_H3cDvpnMapPeerPublicIp_Type = InetAddress
_H3cDvpnMapPeerPublicIp_Object = MibTableColumn
h3cDvpnMapPeerPublicIp = _H3cDvpnMapPeerPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 8),
    _H3cDvpnMapPeerPublicIp_Type()
)
h3cDvpnMapPeerPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapPeerPublicIp.setStatus("current")
_H3cDvpnMapLocalPriIpType_Type = InetAddressType
_H3cDvpnMapLocalPriIpType_Object = MibTableColumn
h3cDvpnMapLocalPriIpType = _H3cDvpnMapLocalPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 9),
    _H3cDvpnMapLocalPriIpType_Type()
)
h3cDvpnMapLocalPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapLocalPriIpType.setStatus("current")
_H3cDvpnMapLocalPriIp_Type = InetAddress
_H3cDvpnMapLocalPriIp_Object = MibTableColumn
h3cDvpnMapLocalPriIp = _H3cDvpnMapLocalPriIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 10),
    _H3cDvpnMapLocalPriIp_Type()
)
h3cDvpnMapLocalPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapLocalPriIp.setStatus("current")
_H3cDvpnMapLocalPublicIpType_Type = InetAddressType
_H3cDvpnMapLocalPublicIpType_Object = MibTableColumn
h3cDvpnMapLocalPublicIpType = _H3cDvpnMapLocalPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 11),
    _H3cDvpnMapLocalPublicIpType_Type()
)
h3cDvpnMapLocalPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapLocalPublicIpType.setStatus("current")
_H3cDvpnMapLocalPublicIp_Type = InetAddress
_H3cDvpnMapLocalPublicIp_Object = MibTableColumn
h3cDvpnMapLocalPublicIp = _H3cDvpnMapLocalPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 12),
    _H3cDvpnMapLocalPublicIp_Type()
)
h3cDvpnMapLocalPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapLocalPublicIp.setStatus("current")
_H3cDvpnMapUserName_Type = OctetString
_H3cDvpnMapUserName_Object = MibTableColumn
h3cDvpnMapUserName = _H3cDvpnMapUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 13),
    _H3cDvpnMapUserName_Type()
)
h3cDvpnMapUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapUserName.setStatus("current")
_H3cDvpnMapUdpPort_Type = Integer32
_H3cDvpnMapUdpPort_Object = MibTableColumn
h3cDvpnMapUdpPort = _H3cDvpnMapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 14),
    _H3cDvpnMapUdpPort_Type()
)
h3cDvpnMapUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapUdpPort.setStatus("current")
_H3cDvpnMapControlId_Type = Unsigned32
_H3cDvpnMapControlId_Object = MibTableColumn
h3cDvpnMapControlId = _H3cDvpnMapControlId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 15),
    _H3cDvpnMapControlId_Type()
)
h3cDvpnMapControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapControlId.setStatus("current")
_H3cDvpnMapType_Type = DvpnCommunicateType
_H3cDvpnMapType_Object = MibTableColumn
h3cDvpnMapType = _H3cDvpnMapType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 16),
    _H3cDvpnMapType_Type()
)
h3cDvpnMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapType.setStatus("current")


class _H3cDvpnMapState_Type(Integer32):
    """Custom type h3cDvpnMapState based on Integer32"""
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


_H3cDvpnMapState_Type.__name__ = "Integer32"
_H3cDvpnMapState_Object = MibTableColumn
h3cDvpnMapState = _H3cDvpnMapState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 5, 1, 17),
    _H3cDvpnMapState_Type()
)
h3cDvpnMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnMapState.setStatus("current")
_H3cDvpnSessionTable_Object = MibTable
h3cDvpnSessionTable = _H3cDvpnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6)
)
if mibBuilder.loadTexts:
    h3cDvpnSessionTable.setStatus("current")
_H3cDvpnSessionEntry_Object = MibTableRow
h3cDvpnSessionEntry = _H3cDvpnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1)
)
h3cDvpnSessionEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionDvpnId"),
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIpType"),
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIp"),
)
if mibBuilder.loadTexts:
    h3cDvpnSessionEntry.setStatus("current")
_H3cDvpnSessionDvpnId_Type = Integer32
_H3cDvpnSessionDvpnId_Object = MibTableColumn
h3cDvpnSessionDvpnId = _H3cDvpnSessionDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 1),
    _H3cDvpnSessionDvpnId_Type()
)
h3cDvpnSessionDvpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDvpnSessionDvpnId.setStatus("current")
_H3cDvpnSessionPeerPriIpType_Type = InetAddressType
_H3cDvpnSessionPeerPriIpType_Object = MibTableColumn
h3cDvpnSessionPeerPriIpType = _H3cDvpnSessionPeerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 2),
    _H3cDvpnSessionPeerPriIpType_Type()
)
h3cDvpnSessionPeerPriIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerPriIpType.setStatus("current")
_H3cDvpnSessionPeerPriIp_Type = InetAddress
_H3cDvpnSessionPeerPriIp_Object = MibTableColumn
h3cDvpnSessionPeerPriIp = _H3cDvpnSessionPeerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 3),
    _H3cDvpnSessionPeerPriIp_Type()
)
h3cDvpnSessionPeerPriIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerPriIp.setStatus("current")
_H3cDvpnSessionPeerDeviceId_Type = OctetString
_H3cDvpnSessionPeerDeviceId_Object = MibTableColumn
h3cDvpnSessionPeerDeviceId = _H3cDvpnSessionPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 4),
    _H3cDvpnSessionPeerDeviceId_Type()
)
h3cDvpnSessionPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerDeviceId.setStatus("current")
_H3cDvpnSessionBuildTime_Type = TimeTicks
_H3cDvpnSessionBuildTime_Object = MibTableColumn
h3cDvpnSessionBuildTime = _H3cDvpnSessionBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 5),
    _H3cDvpnSessionBuildTime_Type()
)
h3cDvpnSessionBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionBuildTime.setStatus("current")
_H3cDvpnSessionPeerPubIpType_Type = InetAddressType
_H3cDvpnSessionPeerPubIpType_Object = MibTableColumn
h3cDvpnSessionPeerPubIpType = _H3cDvpnSessionPeerPubIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 6),
    _H3cDvpnSessionPeerPubIpType_Type()
)
h3cDvpnSessionPeerPubIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerPubIpType.setStatus("current")
_H3cDvpnSessionPeerPubIp_Type = InetAddress
_H3cDvpnSessionPeerPubIp_Object = MibTableColumn
h3cDvpnSessionPeerPubIp = _H3cDvpnSessionPeerPubIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 7),
    _H3cDvpnSessionPeerPubIp_Type()
)
h3cDvpnSessionPeerPubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerPubIp.setStatus("current")
_H3cDvpnSessionLocalPubIpType_Type = InetAddressType
_H3cDvpnSessionLocalPubIpType_Object = MibTableColumn
h3cDvpnSessionLocalPubIpType = _H3cDvpnSessionLocalPubIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 8),
    _H3cDvpnSessionLocalPubIpType_Type()
)
h3cDvpnSessionLocalPubIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionLocalPubIpType.setStatus("current")
_H3cDvpnSessionLocalPubIp_Type = InetAddress
_H3cDvpnSessionLocalPubIp_Object = MibTableColumn
h3cDvpnSessionLocalPubIp = _H3cDvpnSessionLocalPubIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 9),
    _H3cDvpnSessionLocalPubIp_Type()
)
h3cDvpnSessionLocalPubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionLocalPubIp.setStatus("current")
_H3cDvpnSessionLocalPriIpType_Type = InetAddressType
_H3cDvpnSessionLocalPriIpType_Object = MibTableColumn
h3cDvpnSessionLocalPriIpType = _H3cDvpnSessionLocalPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 10),
    _H3cDvpnSessionLocalPriIpType_Type()
)
h3cDvpnSessionLocalPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionLocalPriIpType.setStatus("current")
_H3cDvpnSessionLocalPriIp_Type = InetAddress
_H3cDvpnSessionLocalPriIp_Object = MibTableColumn
h3cDvpnSessionLocalPriIp = _H3cDvpnSessionLocalPriIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 11),
    _H3cDvpnSessionLocalPriIp_Type()
)
h3cDvpnSessionLocalPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionLocalPriIp.setStatus("current")
_H3cDvpnSessionPeerUdpPort_Type = Integer32
_H3cDvpnSessionPeerUdpPort_Object = MibTableColumn
h3cDvpnSessionPeerUdpPort = _H3cDvpnSessionPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 12),
    _H3cDvpnSessionPeerUdpPort_Type()
)
h3cDvpnSessionPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerUdpPort.setStatus("current")


class _H3cDvpnSessionInitiator_Type(Integer32):
    """Custom type h3cDvpnSessionInitiator based on Integer32"""
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


_H3cDvpnSessionInitiator_Type.__name__ = "Integer32"
_H3cDvpnSessionInitiator_Object = MibTableColumn
h3cDvpnSessionInitiator = _H3cDvpnSessionInitiator_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 13),
    _H3cDvpnSessionInitiator_Type()
)
h3cDvpnSessionInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionInitiator.setStatus("current")
_H3cDvpnSessionUserName_Type = OctetString
_H3cDvpnSessionUserName_Object = MibTableColumn
h3cDvpnSessionUserName = _H3cDvpnSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 14),
    _H3cDvpnSessionUserName_Type()
)
h3cDvpnSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionUserName.setStatus("current")


class _H3cDvpnSessionState_Type(Integer32):
    """Custom type h3cDvpnSessionState based on Integer32"""
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


_H3cDvpnSessionState_Type.__name__ = "Integer32"
_H3cDvpnSessionState_Object = MibTableColumn
h3cDvpnSessionState = _H3cDvpnSessionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 15),
    _H3cDvpnSessionState_Type()
)
h3cDvpnSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionState.setStatus("current")
_H3cDvpnSessionType_Type = DvpnCommunicateType
_H3cDvpnSessionType_Object = MibTableColumn
h3cDvpnSessionType = _H3cDvpnSessionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 16),
    _H3cDvpnSessionType_Type()
)
h3cDvpnSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionType.setStatus("current")


class _H3cDvpnSessionPeerType_Type(Integer32):
    """Custom type h3cDvpnSessionPeerType based on Integer32"""
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


_H3cDvpnSessionPeerType_Type.__name__ = "Integer32"
_H3cDvpnSessionPeerType_Object = MibTableColumn
h3cDvpnSessionPeerType = _H3cDvpnSessionPeerType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 6, 1, 17),
    _H3cDvpnSessionPeerType_Type()
)
h3cDvpnSessionPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionPeerType.setStatus("current")
_H3cDvpnSessionHisTable_Object = MibTable
h3cDvpnSessionHisTable = _H3cDvpnSessionHisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7)
)
if mibBuilder.loadTexts:
    h3cDvpnSessionHisTable.setStatus("current")
_H3cDvpnSessionHisEntry_Object = MibTableRow
h3cDvpnSessionHisEntry = _H3cDvpnSessionHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1)
)
h3cDvpnSessionHisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisDvpnID"),
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisPeerPriIPType"),
    (0, "A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisPeerPriIP"),
)
if mibBuilder.loadTexts:
    h3cDvpnSessionHisEntry.setStatus("current")


class _H3cDvpnSessionHisDvpnID_Type(Integer32):
    """Custom type h3cDvpnSessionHisDvpnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cDvpnSessionHisDvpnID_Type.__name__ = "Integer32"
_H3cDvpnSessionHisDvpnID_Object = MibTableColumn
h3cDvpnSessionHisDvpnID = _H3cDvpnSessionHisDvpnID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 1),
    _H3cDvpnSessionHisDvpnID_Type()
)
h3cDvpnSessionHisDvpnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisDvpnID.setStatus("current")
_H3cDvpnSessionHisPeerPriIPType_Type = InetAddressType
_H3cDvpnSessionHisPeerPriIPType_Object = MibTableColumn
h3cDvpnSessionHisPeerPriIPType = _H3cDvpnSessionHisPeerPriIPType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 2),
    _H3cDvpnSessionHisPeerPriIPType_Type()
)
h3cDvpnSessionHisPeerPriIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisPeerPriIPType.setStatus("current")
_H3cDvpnSessionHisPeerPriIP_Type = InetAddress
_H3cDvpnSessionHisPeerPriIP_Object = MibTableColumn
h3cDvpnSessionHisPeerPriIP = _H3cDvpnSessionHisPeerPriIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 3),
    _H3cDvpnSessionHisPeerPriIP_Type()
)
h3cDvpnSessionHisPeerPriIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisPeerPriIP.setStatus("current")
_H3cDvpnSessionHisSendPkt_Type = Unsigned32
_H3cDvpnSessionHisSendPkt_Object = MibTableColumn
h3cDvpnSessionHisSendPkt = _H3cDvpnSessionHisSendPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 4),
    _H3cDvpnSessionHisSendPkt_Type()
)
h3cDvpnSessionHisSendPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisSendPkt.setStatus("current")
_H3cDvpnSessionHisRcvPkt_Type = Unsigned32
_H3cDvpnSessionHisRcvPkt_Object = MibTableColumn
h3cDvpnSessionHisRcvPkt = _H3cDvpnSessionHisRcvPkt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 5),
    _H3cDvpnSessionHisRcvPkt_Type()
)
h3cDvpnSessionHisRcvPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisRcvPkt.setStatus("current")
_H3cDvpnSessionHisOnlineNumber_Type = Unsigned32
_H3cDvpnSessionHisOnlineNumber_Object = MibTableColumn
h3cDvpnSessionHisOnlineNumber = _H3cDvpnSessionHisOnlineNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 6),
    _H3cDvpnSessionHisOnlineNumber_Type()
)
h3cDvpnSessionHisOnlineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisOnlineNumber.setStatus("current")
_H3cDvpnSessionHisFirstUpTime_Type = TimeTicks
_H3cDvpnSessionHisFirstUpTime_Object = MibTableColumn
h3cDvpnSessionHisFirstUpTime = _H3cDvpnSessionHisFirstUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 7),
    _H3cDvpnSessionHisFirstUpTime_Type()
)
h3cDvpnSessionHisFirstUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisFirstUpTime.setStatus("current")
_H3cDvpnSessionHisLastUpTime_Type = TimeTicks
_H3cDvpnSessionHisLastUpTime_Object = MibTableColumn
h3cDvpnSessionHisLastUpTime = _H3cDvpnSessionHisLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 8),
    _H3cDvpnSessionHisLastUpTime_Type()
)
h3cDvpnSessionHisLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisLastUpTime.setStatus("current")
_H3cDvpnSessionHisLastDownTime_Type = TimeTicks
_H3cDvpnSessionHisLastDownTime_Object = MibTableColumn
h3cDvpnSessionHisLastDownTime = _H3cDvpnSessionHisLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 9),
    _H3cDvpnSessionHisLastDownTime_Type()
)
h3cDvpnSessionHisLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisLastDownTime.setStatus("current")


class _H3cDvpnSessionHisOnlineFlag_Type(Integer32):
    """Custom type h3cDvpnSessionHisOnlineFlag based on Integer32"""
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


_H3cDvpnSessionHisOnlineFlag_Type.__name__ = "Integer32"
_H3cDvpnSessionHisOnlineFlag_Object = MibTableColumn
h3cDvpnSessionHisOnlineFlag = _H3cDvpnSessionHisOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 10),
    _H3cDvpnSessionHisOnlineFlag_Type()
)
h3cDvpnSessionHisOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisOnlineFlag.setStatus("current")
_H3cDvpnSessionHisPeerDeviceId_Type = OctetString
_H3cDvpnSessionHisPeerDeviceId_Object = MibTableColumn
h3cDvpnSessionHisPeerDeviceId = _H3cDvpnSessionHisPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 2, 7, 1, 11),
    _H3cDvpnSessionHisPeerDeviceId_Type()
)
h3cDvpnSessionHisPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDvpnSessionHisPeerDeviceId.setStatus("current")
_H3cDvpnMibNotification_ObjectIdentity = ObjectIdentity
h3cDvpnMibNotification = _H3cDvpnMibNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 3)
)
_H3cDvpnNotification_ObjectIdentity = ObjectIdentity
h3cDvpnNotification = _H3cDvpnNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 3, 0)
)
_H3cDvpnMibConformance_ObjectIdentity = ObjectIdentity
h3cDvpnMibConformance = _H3cDvpnMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4)
)
_H3cDvpnMibCompliances_ObjectIdentity = ObjectIdentity
h3cDvpnMibCompliances = _H3cDvpnMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 1)
)
_H3cDvpnMibGroups_ObjectIdentity = ObjectIdentity
h3cDvpnMibGroups = _H3cDvpnMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2)
)

# Managed Objects groups

h3cDvpnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 1)
)
h3cDvpnGlobalGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnServiceEnable"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClassNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClientNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapAgeTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClientRegisterInterval"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClientRegisterDumb"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClientRegisterRetry"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnInputPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDropPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnOutputPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnOutputErrorPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnEncryptErrorPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnCurrentDeviceRole"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnServerPreSharedKey"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapTrapEnable"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionTrapEnable"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnVersion"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClearDomainAllConection"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClearDvpnStaInfo"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTotalRedirectNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnGlobalAuthenClientType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnGlobalUserDefAAADomain"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnLocalDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisAgeTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisReset"))
)
if mibBuilder.loadTexts:
    h3cDvpnGlobalGroup.setStatus("current")

h3cDvpnPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 2)
)
h3cDvpnPolicyGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoAuthenClientType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoSessionAlgorithmSuite"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoSessionIdleTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoSessionKeepTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoSessionSetupInterval"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoDataAlgorithmSuite"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoSaSeconds"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoUserDefAAADomain"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoRefTimes"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnPoRowStatus"))
)
if mibBuilder.loadTexts:
    h3cDvpnPolicyGroup.setStatus("current")

h3cDvpnDomainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 3)
)
h3cDvpnDomainInfoGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainSessionNum"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainRedirectNum"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainInputPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainDropPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainOutputPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainOutputErrorPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnDomainEncryptErrorPkt"))
)
if mibBuilder.loadTexts:
    h3cDvpnDomainInfoGroup.setStatus("current")

h3cDvpnClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 4)
)
h3cDvpnClassGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClServerPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClServerPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClServerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClServerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClAlgorithmSuite"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClAuthenServerType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClPreShareKey"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClUserName"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClPwdEncrypted"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClPasswd"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnClassRowStatus"))
)
if mibBuilder.loadTexts:
    h3cDvpnClassGroup.setStatus("current")

h3cDvpnTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 5)
)
h3cDvpnTunnelGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTunnelInterfaceType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTunnelAcl"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTunnelClientRegType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTunnelDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTunnelPolicy"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnTunnelClass"))
)
if mibBuilder.loadTexts:
    h3cDvpnTunnelGroup.setStatus("current")

h3cDvpnMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 6)
)
h3cDvpnMapGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapIndex"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapBuildTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapUserName"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapUdpPort"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapControlId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapState"))
)
if mibBuilder.loadTexts:
    h3cDvpnMapGroup.setStatus("current")

h3cDvpnSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 7)
)
h3cDvpnSessionGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionBuildTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPubIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPubIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPubIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPubIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerUdpPort"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionInitiator"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionUserName"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionState"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerType"))
)
if mibBuilder.loadTexts:
    h3cDvpnSessionGroup.setStatus("current")

h3cDvpnSessionHisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 8)
)
h3cDvpnSessionHisGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisPeerPriIPType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisSendPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisRcvPkt"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisOnlineNumber"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisFirstUpTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisLastUpTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisLastDownTime"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisOnlineFlag"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionHisPeerDeviceId"))
)
if mibBuilder.loadTexts:
    h3cDvpnSessionHisGroup.setStatus("current")

h3cDvpnNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 2, 9)
)
h3cDvpnNotificationGroup.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionBuildNotification"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionDelNotification"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapBuildNotification"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapDelNotification"))
)
if mibBuilder.loadTexts:
    h3cDvpnNotificationGroup.setStatus("current")


# Notification objects

h3cDvpnSessionBuildNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 3, 0, 1)
)
h3cDvpnSessionBuildNotification.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnLocalDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPubIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPubIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPubIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPubIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerUdpPort"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionUserName"))
)
if mibBuilder.loadTexts:
    h3cDvpnSessionBuildNotification.setStatus(
        "current"
    )

h3cDvpnSessionDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 3, 0, 2)
)
h3cDvpnSessionDelNotification.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnLocalDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPubIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionLocalPubIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPubIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerPubIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerUdpPort"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionPeerType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnSessionUserName"))
)
if mibBuilder.loadTexts:
    h3cDvpnSessionDelNotification.setStatus(
        "current"
    )

h3cDvpnMapBuildNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 3, 0, 3)
)
h3cDvpnMapBuildNotification.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapIndex"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnLocalDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapUserName"))
)
if mibBuilder.loadTexts:
    h3cDvpnMapBuildNotification.setStatus(
        "current"
    )

h3cDvpnMapDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 3, 0, 4)
)
h3cDvpnMapDelNotification.setObjects(
      *(("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapIndex"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapDvpnId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapPeerPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnLocalDeviceId"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPriIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPriIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPublicIpType"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapLocalPublicIp"),
        ("A3COM-HUAWEI-DVPN-MIB", "h3cDvpnMapUserName"))
)
if mibBuilder.loadTexts:
    h3cDvpnMapDelNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

h3cDvpnMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDvpnMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DVPN-MIB",
    **{"DvpnAlgorithmSuite": DvpnAlgorithmSuite,
       "DvpnCommunicateType": DvpnCommunicateType,
       "h3cDvpn": h3cDvpn,
       "h3cDvpnMibObjects": h3cDvpnMibObjects,
       "h3cDvpnMibGlobal": h3cDvpnMibGlobal,
       "h3cDvpnServiceEnable": h3cDvpnServiceEnable,
       "h3cDvpnClassNumber": h3cDvpnClassNumber,
       "h3cDvpnClientNumber": h3cDvpnClientNumber,
       "h3cDvpnMapAgeTime": h3cDvpnMapAgeTime,
       "h3cDvpnClientRegisterInterval": h3cDvpnClientRegisterInterval,
       "h3cDvpnClientRegisterDumb": h3cDvpnClientRegisterDumb,
       "h3cDvpnClientRegisterRetry": h3cDvpnClientRegisterRetry,
       "h3cDvpnInputPkt": h3cDvpnInputPkt,
       "h3cDvpnDropPkt": h3cDvpnDropPkt,
       "h3cDvpnOutputPkt": h3cDvpnOutputPkt,
       "h3cDvpnOutputErrorPkt": h3cDvpnOutputErrorPkt,
       "h3cDvpnEncryptErrorPkt": h3cDvpnEncryptErrorPkt,
       "h3cDvpnCurrentDeviceRole": h3cDvpnCurrentDeviceRole,
       "h3cDvpnDomainNumber": h3cDvpnDomainNumber,
       "h3cDvpnMapNumber": h3cDvpnMapNumber,
       "h3cDvpnSessionNumber": h3cDvpnSessionNumber,
       "h3cDvpnServerPreSharedKey": h3cDvpnServerPreSharedKey,
       "h3cDvpnMapTrapEnable": h3cDvpnMapTrapEnable,
       "h3cDvpnSessionTrapEnable": h3cDvpnSessionTrapEnable,
       "h3cDvpnVersion": h3cDvpnVersion,
       "h3cDvpnClearDomainAllConection": h3cDvpnClearDomainAllConection,
       "h3cDvpnClearDvpnStaInfo": h3cDvpnClearDvpnStaInfo,
       "h3cDvpnTotalRedirectNumber": h3cDvpnTotalRedirectNumber,
       "h3cDvpnGlobalAuthenClientType": h3cDvpnGlobalAuthenClientType,
       "h3cDvpnGlobalUserDefAAADomain": h3cDvpnGlobalUserDefAAADomain,
       "h3cDvpnLocalDeviceId": h3cDvpnLocalDeviceId,
       "h3cDvpnSessionHisAgeTime": h3cDvpnSessionHisAgeTime,
       "h3cDvpnSessionHisReset": h3cDvpnSessionHisReset,
       "h3cDvpnMibTableTroop": h3cDvpnMibTableTroop,
       "h3cDvpnPolicyTable": h3cDvpnPolicyTable,
       "h3cDvpnPolicyEntry": h3cDvpnPolicyEntry,
       "h3cDvpnPolicyName": h3cDvpnPolicyName,
       "h3cDvpnPoAuthenClientType": h3cDvpnPoAuthenClientType,
       "h3cDvpnPoSessionAlgorithmSuite": h3cDvpnPoSessionAlgorithmSuite,
       "h3cDvpnPoSessionIdleTime": h3cDvpnPoSessionIdleTime,
       "h3cDvpnPoSessionKeepTime": h3cDvpnPoSessionKeepTime,
       "h3cDvpnPoSessionSetupInterval": h3cDvpnPoSessionSetupInterval,
       "h3cDvpnPoDataAlgorithmSuite": h3cDvpnPoDataAlgorithmSuite,
       "h3cDvpnPoSaSeconds": h3cDvpnPoSaSeconds,
       "h3cDvpnPoUserDefAAADomain": h3cDvpnPoUserDefAAADomain,
       "h3cDvpnPoRefTimes": h3cDvpnPoRefTimes,
       "h3cDvpnPoRowStatus": h3cDvpnPoRowStatus,
       "h3cDvpnDomainInfoTable": h3cDvpnDomainInfoTable,
       "h3cDvpnDomainInfoEntry": h3cDvpnDomainInfoEntry,
       "h3cDvpnDomainID": h3cDvpnDomainID,
       "h3cDvpnDomainSessionNum": h3cDvpnDomainSessionNum,
       "h3cDvpnDomainRedirectNum": h3cDvpnDomainRedirectNum,
       "h3cDvpnDomainInputPkt": h3cDvpnDomainInputPkt,
       "h3cDvpnDomainDropPkt": h3cDvpnDomainDropPkt,
       "h3cDvpnDomainOutputPkt": h3cDvpnDomainOutputPkt,
       "h3cDvpnDomainOutputErrorPkt": h3cDvpnDomainOutputErrorPkt,
       "h3cDvpnDomainEncryptErrorPkt": h3cDvpnDomainEncryptErrorPkt,
       "h3cDvpnClassTable": h3cDvpnClassTable,
       "h3cDvpnClassEntry": h3cDvpnClassEntry,
       "h3cDvpnClassName": h3cDvpnClassName,
       "h3cDvpnClServerPublicIpType": h3cDvpnClServerPublicIpType,
       "h3cDvpnClServerPublicIp": h3cDvpnClServerPublicIp,
       "h3cDvpnClServerPriIpType": h3cDvpnClServerPriIpType,
       "h3cDvpnClServerPriIp": h3cDvpnClServerPriIp,
       "h3cDvpnClAlgorithmSuite": h3cDvpnClAlgorithmSuite,
       "h3cDvpnClAuthenServerType": h3cDvpnClAuthenServerType,
       "h3cDvpnClPreShareKey": h3cDvpnClPreShareKey,
       "h3cDvpnClUserName": h3cDvpnClUserName,
       "h3cDvpnClPwdEncrypted": h3cDvpnClPwdEncrypted,
       "h3cDvpnClPasswd": h3cDvpnClPasswd,
       "h3cDvpnClassRowStatus": h3cDvpnClassRowStatus,
       "h3cDvpnTunnelTable": h3cDvpnTunnelTable,
       "h3cDvpnTunnelEntry": h3cDvpnTunnelEntry,
       "h3cDvpnTunnelInterfaceType": h3cDvpnTunnelInterfaceType,
       "h3cDvpnTunnelAcl": h3cDvpnTunnelAcl,
       "h3cDvpnTunnelClientRegType": h3cDvpnTunnelClientRegType,
       "h3cDvpnTunnelDvpnId": h3cDvpnTunnelDvpnId,
       "h3cDvpnTunnelPolicy": h3cDvpnTunnelPolicy,
       "h3cDvpnTunnelClass": h3cDvpnTunnelClass,
       "h3cDvpnMapTable": h3cDvpnMapTable,
       "h3cDvpnMapEntry": h3cDvpnMapEntry,
       "h3cDvpnMapIndex": h3cDvpnMapIndex,
       "h3cDvpnMapPeerDeviceId": h3cDvpnMapPeerDeviceId,
       "h3cDvpnMapDvpnId": h3cDvpnMapDvpnId,
       "h3cDvpnMapBuildTime": h3cDvpnMapBuildTime,
       "h3cDvpnMapPeerPriIpType": h3cDvpnMapPeerPriIpType,
       "h3cDvpnMapPeerPriIp": h3cDvpnMapPeerPriIp,
       "h3cDvpnMapPeerPublicIpType": h3cDvpnMapPeerPublicIpType,
       "h3cDvpnMapPeerPublicIp": h3cDvpnMapPeerPublicIp,
       "h3cDvpnMapLocalPriIpType": h3cDvpnMapLocalPriIpType,
       "h3cDvpnMapLocalPriIp": h3cDvpnMapLocalPriIp,
       "h3cDvpnMapLocalPublicIpType": h3cDvpnMapLocalPublicIpType,
       "h3cDvpnMapLocalPublicIp": h3cDvpnMapLocalPublicIp,
       "h3cDvpnMapUserName": h3cDvpnMapUserName,
       "h3cDvpnMapUdpPort": h3cDvpnMapUdpPort,
       "h3cDvpnMapControlId": h3cDvpnMapControlId,
       "h3cDvpnMapType": h3cDvpnMapType,
       "h3cDvpnMapState": h3cDvpnMapState,
       "h3cDvpnSessionTable": h3cDvpnSessionTable,
       "h3cDvpnSessionEntry": h3cDvpnSessionEntry,
       "h3cDvpnSessionDvpnId": h3cDvpnSessionDvpnId,
       "h3cDvpnSessionPeerPriIpType": h3cDvpnSessionPeerPriIpType,
       "h3cDvpnSessionPeerPriIp": h3cDvpnSessionPeerPriIp,
       "h3cDvpnSessionPeerDeviceId": h3cDvpnSessionPeerDeviceId,
       "h3cDvpnSessionBuildTime": h3cDvpnSessionBuildTime,
       "h3cDvpnSessionPeerPubIpType": h3cDvpnSessionPeerPubIpType,
       "h3cDvpnSessionPeerPubIp": h3cDvpnSessionPeerPubIp,
       "h3cDvpnSessionLocalPubIpType": h3cDvpnSessionLocalPubIpType,
       "h3cDvpnSessionLocalPubIp": h3cDvpnSessionLocalPubIp,
       "h3cDvpnSessionLocalPriIpType": h3cDvpnSessionLocalPriIpType,
       "h3cDvpnSessionLocalPriIp": h3cDvpnSessionLocalPriIp,
       "h3cDvpnSessionPeerUdpPort": h3cDvpnSessionPeerUdpPort,
       "h3cDvpnSessionInitiator": h3cDvpnSessionInitiator,
       "h3cDvpnSessionUserName": h3cDvpnSessionUserName,
       "h3cDvpnSessionState": h3cDvpnSessionState,
       "h3cDvpnSessionType": h3cDvpnSessionType,
       "h3cDvpnSessionPeerType": h3cDvpnSessionPeerType,
       "h3cDvpnSessionHisTable": h3cDvpnSessionHisTable,
       "h3cDvpnSessionHisEntry": h3cDvpnSessionHisEntry,
       "h3cDvpnSessionHisDvpnID": h3cDvpnSessionHisDvpnID,
       "h3cDvpnSessionHisPeerPriIPType": h3cDvpnSessionHisPeerPriIPType,
       "h3cDvpnSessionHisPeerPriIP": h3cDvpnSessionHisPeerPriIP,
       "h3cDvpnSessionHisSendPkt": h3cDvpnSessionHisSendPkt,
       "h3cDvpnSessionHisRcvPkt": h3cDvpnSessionHisRcvPkt,
       "h3cDvpnSessionHisOnlineNumber": h3cDvpnSessionHisOnlineNumber,
       "h3cDvpnSessionHisFirstUpTime": h3cDvpnSessionHisFirstUpTime,
       "h3cDvpnSessionHisLastUpTime": h3cDvpnSessionHisLastUpTime,
       "h3cDvpnSessionHisLastDownTime": h3cDvpnSessionHisLastDownTime,
       "h3cDvpnSessionHisOnlineFlag": h3cDvpnSessionHisOnlineFlag,
       "h3cDvpnSessionHisPeerDeviceId": h3cDvpnSessionHisPeerDeviceId,
       "h3cDvpnMibNotification": h3cDvpnMibNotification,
       "h3cDvpnNotification": h3cDvpnNotification,
       "h3cDvpnSessionBuildNotification": h3cDvpnSessionBuildNotification,
       "h3cDvpnSessionDelNotification": h3cDvpnSessionDelNotification,
       "h3cDvpnMapBuildNotification": h3cDvpnMapBuildNotification,
       "h3cDvpnMapDelNotification": h3cDvpnMapDelNotification,
       "h3cDvpnMibConformance": h3cDvpnMibConformance,
       "h3cDvpnMibCompliances": h3cDvpnMibCompliances,
       "h3cDvpnMibCompliance": h3cDvpnMibCompliance,
       "h3cDvpnMibGroups": h3cDvpnMibGroups,
       "h3cDvpnGlobalGroup": h3cDvpnGlobalGroup,
       "h3cDvpnPolicyGroup": h3cDvpnPolicyGroup,
       "h3cDvpnDomainInfoGroup": h3cDvpnDomainInfoGroup,
       "h3cDvpnClassGroup": h3cDvpnClassGroup,
       "h3cDvpnTunnelGroup": h3cDvpnTunnelGroup,
       "h3cDvpnMapGroup": h3cDvpnMapGroup,
       "h3cDvpnSessionGroup": h3cDvpnSessionGroup,
       "h3cDvpnSessionHisGroup": h3cDvpnSessionHisGroup,
       "h3cDvpnNotificationGroup": h3cDvpnNotificationGroup}
)
