# SNMP MIB module (HPN-ICF-DVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:00 2024
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

hpnicfDvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57)
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

_HpnicfDvpnMibObjects_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibObjects = _HpnicfDvpnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1)
)
_HpnicfDvpnMibGlobal_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibGlobal = _HpnicfDvpnMibGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1)
)


class _HpnicfDvpnServiceEnable_Type(Integer32):
    """Custom type hpnicfDvpnServiceEnable based on Integer32"""
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


_HpnicfDvpnServiceEnable_Type.__name__ = "Integer32"
_HpnicfDvpnServiceEnable_Object = MibScalar
hpnicfDvpnServiceEnable = _HpnicfDvpnServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 1),
    _HpnicfDvpnServiceEnable_Type()
)
hpnicfDvpnServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnServiceEnable.setStatus("current")


class _HpnicfDvpnClassNumber_Type(Integer32):
    """Custom type hpnicfDvpnClassNumber based on Integer32"""
    defaultValue = 0


_HpnicfDvpnClassNumber_Object = MibScalar
hpnicfDvpnClassNumber = _HpnicfDvpnClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 2),
    _HpnicfDvpnClassNumber_Type()
)
hpnicfDvpnClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnClassNumber.setStatus("current")


class _HpnicfDvpnClientNumber_Type(Integer32):
    """Custom type hpnicfDvpnClientNumber based on Integer32"""
    defaultValue = 0


_HpnicfDvpnClientNumber_Object = MibScalar
hpnicfDvpnClientNumber = _HpnicfDvpnClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 3),
    _HpnicfDvpnClientNumber_Type()
)
hpnicfDvpnClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnClientNumber.setStatus("current")


class _HpnicfDvpnMapAgeTime_Type(Integer32):
    """Custom type hpnicfDvpnMapAgeTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_HpnicfDvpnMapAgeTime_Type.__name__ = "Integer32"
_HpnicfDvpnMapAgeTime_Object = MibScalar
hpnicfDvpnMapAgeTime = _HpnicfDvpnMapAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 4),
    _HpnicfDvpnMapAgeTime_Type()
)
hpnicfDvpnMapAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnMapAgeTime.setStatus("current")


class _HpnicfDvpnClientRegisterInterval_Type(Integer32):
    """Custom type hpnicfDvpnClientRegisterInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_HpnicfDvpnClientRegisterInterval_Type.__name__ = "Integer32"
_HpnicfDvpnClientRegisterInterval_Object = MibScalar
hpnicfDvpnClientRegisterInterval = _HpnicfDvpnClientRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 5),
    _HpnicfDvpnClientRegisterInterval_Type()
)
hpnicfDvpnClientRegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnClientRegisterInterval.setStatus("current")


class _HpnicfDvpnClientRegisterDumb_Type(Integer32):
    """Custom type hpnicfDvpnClientRegisterDumb based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_HpnicfDvpnClientRegisterDumb_Type.__name__ = "Integer32"
_HpnicfDvpnClientRegisterDumb_Object = MibScalar
hpnicfDvpnClientRegisterDumb = _HpnicfDvpnClientRegisterDumb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 6),
    _HpnicfDvpnClientRegisterDumb_Type()
)
hpnicfDvpnClientRegisterDumb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnClientRegisterDumb.setStatus("current")


class _HpnicfDvpnClientRegisterRetry_Type(Integer32):
    """Custom type hpnicfDvpnClientRegisterRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_HpnicfDvpnClientRegisterRetry_Type.__name__ = "Integer32"
_HpnicfDvpnClientRegisterRetry_Object = MibScalar
hpnicfDvpnClientRegisterRetry = _HpnicfDvpnClientRegisterRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 7),
    _HpnicfDvpnClientRegisterRetry_Type()
)
hpnicfDvpnClientRegisterRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnClientRegisterRetry.setStatus("current")


class _HpnicfDvpnInputPkt_Type(Unsigned32):
    """Custom type hpnicfDvpnInputPkt based on Unsigned32"""
    defaultValue = 0


_HpnicfDvpnInputPkt_Object = MibScalar
hpnicfDvpnInputPkt = _HpnicfDvpnInputPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 8),
    _HpnicfDvpnInputPkt_Type()
)
hpnicfDvpnInputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnInputPkt.setStatus("current")


class _HpnicfDvpnDropPkt_Type(Unsigned32):
    """Custom type hpnicfDvpnDropPkt based on Unsigned32"""
    defaultValue = 0


_HpnicfDvpnDropPkt_Object = MibScalar
hpnicfDvpnDropPkt = _HpnicfDvpnDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 9),
    _HpnicfDvpnDropPkt_Type()
)
hpnicfDvpnDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDropPkt.setStatus("current")


class _HpnicfDvpnOutputPkt_Type(Unsigned32):
    """Custom type hpnicfDvpnOutputPkt based on Unsigned32"""
    defaultValue = 0


_HpnicfDvpnOutputPkt_Object = MibScalar
hpnicfDvpnOutputPkt = _HpnicfDvpnOutputPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 10),
    _HpnicfDvpnOutputPkt_Type()
)
hpnicfDvpnOutputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnOutputPkt.setStatus("current")


class _HpnicfDvpnOutputErrorPkt_Type(Unsigned32):
    """Custom type hpnicfDvpnOutputErrorPkt based on Unsigned32"""
    defaultValue = 0


_HpnicfDvpnOutputErrorPkt_Object = MibScalar
hpnicfDvpnOutputErrorPkt = _HpnicfDvpnOutputErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 11),
    _HpnicfDvpnOutputErrorPkt_Type()
)
hpnicfDvpnOutputErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnOutputErrorPkt.setStatus("current")


class _HpnicfDvpnEncryptErrorPkt_Type(Unsigned32):
    """Custom type hpnicfDvpnEncryptErrorPkt based on Unsigned32"""
    defaultValue = 0


_HpnicfDvpnEncryptErrorPkt_Object = MibScalar
hpnicfDvpnEncryptErrorPkt = _HpnicfDvpnEncryptErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 12),
    _HpnicfDvpnEncryptErrorPkt_Type()
)
hpnicfDvpnEncryptErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnEncryptErrorPkt.setStatus("current")


class _HpnicfDvpnCurrentDeviceRole_Type(Integer32):
    """Custom type hpnicfDvpnCurrentDeviceRole based on Integer32"""
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


_HpnicfDvpnCurrentDeviceRole_Type.__name__ = "Integer32"
_HpnicfDvpnCurrentDeviceRole_Object = MibScalar
hpnicfDvpnCurrentDeviceRole = _HpnicfDvpnCurrentDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 13),
    _HpnicfDvpnCurrentDeviceRole_Type()
)
hpnicfDvpnCurrentDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnCurrentDeviceRole.setStatus("current")


class _HpnicfDvpnDomainNumber_Type(Integer32):
    """Custom type hpnicfDvpnDomainNumber based on Integer32"""
    defaultValue = 0


_HpnicfDvpnDomainNumber_Object = MibScalar
hpnicfDvpnDomainNumber = _HpnicfDvpnDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 14),
    _HpnicfDvpnDomainNumber_Type()
)
hpnicfDvpnDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainNumber.setStatus("current")


class _HpnicfDvpnMapNumber_Type(Integer32):
    """Custom type hpnicfDvpnMapNumber based on Integer32"""
    defaultValue = 0


_HpnicfDvpnMapNumber_Object = MibScalar
hpnicfDvpnMapNumber = _HpnicfDvpnMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 15),
    _HpnicfDvpnMapNumber_Type()
)
hpnicfDvpnMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapNumber.setStatus("current")


class _HpnicfDvpnSessionNumber_Type(Integer32):
    """Custom type hpnicfDvpnSessionNumber based on Integer32"""
    defaultValue = 0


_HpnicfDvpnSessionNumber_Object = MibScalar
hpnicfDvpnSessionNumber = _HpnicfDvpnSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 16),
    _HpnicfDvpnSessionNumber_Type()
)
hpnicfDvpnSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionNumber.setStatus("current")


class _HpnicfDvpnServerPreSharedKey_Type(OctetString):
    """Custom type hpnicfDvpnServerPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDvpnServerPreSharedKey_Type.__name__ = "OctetString"
_HpnicfDvpnServerPreSharedKey_Object = MibScalar
hpnicfDvpnServerPreSharedKey = _HpnicfDvpnServerPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 17),
    _HpnicfDvpnServerPreSharedKey_Type()
)
hpnicfDvpnServerPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnServerPreSharedKey.setStatus("current")


class _HpnicfDvpnMapTrapEnable_Type(Integer32):
    """Custom type hpnicfDvpnMapTrapEnable based on Integer32"""
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


_HpnicfDvpnMapTrapEnable_Type.__name__ = "Integer32"
_HpnicfDvpnMapTrapEnable_Object = MibScalar
hpnicfDvpnMapTrapEnable = _HpnicfDvpnMapTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 18),
    _HpnicfDvpnMapTrapEnable_Type()
)
hpnicfDvpnMapTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnMapTrapEnable.setStatus("current")


class _HpnicfDvpnSessionTrapEnable_Type(Integer32):
    """Custom type hpnicfDvpnSessionTrapEnable based on Integer32"""
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


_HpnicfDvpnSessionTrapEnable_Type.__name__ = "Integer32"
_HpnicfDvpnSessionTrapEnable_Object = MibScalar
hpnicfDvpnSessionTrapEnable = _HpnicfDvpnSessionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 19),
    _HpnicfDvpnSessionTrapEnable_Type()
)
hpnicfDvpnSessionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionTrapEnable.setStatus("current")


class _HpnicfDvpnVersion_Type(Integer32):
    """Custom type hpnicfDvpnVersion based on Integer32"""
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


_HpnicfDvpnVersion_Type.__name__ = "Integer32"
_HpnicfDvpnVersion_Object = MibScalar
hpnicfDvpnVersion = _HpnicfDvpnVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 20),
    _HpnicfDvpnVersion_Type()
)
hpnicfDvpnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnVersion.setStatus("current")


class _HpnicfDvpnClearDomainAllConection_Type(Integer32):
    """Custom type hpnicfDvpnClearDomainAllConection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfDvpnClearDomainAllConection_Type.__name__ = "Integer32"
_HpnicfDvpnClearDomainAllConection_Object = MibScalar
hpnicfDvpnClearDomainAllConection = _HpnicfDvpnClearDomainAllConection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 21),
    _HpnicfDvpnClearDomainAllConection_Type()
)
hpnicfDvpnClearDomainAllConection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnClearDomainAllConection.setStatus("current")


class _HpnicfDvpnClearDvpnStaInfo_Type(Integer32):
    """Custom type hpnicfDvpnClearDvpnStaInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HpnicfDvpnClearDvpnStaInfo_Type.__name__ = "Integer32"
_HpnicfDvpnClearDvpnStaInfo_Object = MibScalar
hpnicfDvpnClearDvpnStaInfo = _HpnicfDvpnClearDvpnStaInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 22),
    _HpnicfDvpnClearDvpnStaInfo_Type()
)
hpnicfDvpnClearDvpnStaInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnClearDvpnStaInfo.setStatus("current")


class _HpnicfDvpnTotalRedirectNumber_Type(Unsigned32):
    """Custom type hpnicfDvpnTotalRedirectNumber based on Unsigned32"""
    defaultValue = 0


_HpnicfDvpnTotalRedirectNumber_Object = MibScalar
hpnicfDvpnTotalRedirectNumber = _HpnicfDvpnTotalRedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 23),
    _HpnicfDvpnTotalRedirectNumber_Type()
)
hpnicfDvpnTotalRedirectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnTotalRedirectNumber.setStatus("current")


class _HpnicfDvpnGlobalAuthenClientType_Type(Integer32):
    """Custom type hpnicfDvpnGlobalAuthenClientType based on Integer32"""
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


_HpnicfDvpnGlobalAuthenClientType_Type.__name__ = "Integer32"
_HpnicfDvpnGlobalAuthenClientType_Object = MibScalar
hpnicfDvpnGlobalAuthenClientType = _HpnicfDvpnGlobalAuthenClientType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 24),
    _HpnicfDvpnGlobalAuthenClientType_Type()
)
hpnicfDvpnGlobalAuthenClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnGlobalAuthenClientType.setStatus("current")


class _HpnicfDvpnGlobalUserDefAAADomain_Type(OctetString):
    """Custom type hpnicfDvpnGlobalUserDefAAADomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HpnicfDvpnGlobalUserDefAAADomain_Type.__name__ = "OctetString"
_HpnicfDvpnGlobalUserDefAAADomain_Object = MibScalar
hpnicfDvpnGlobalUserDefAAADomain = _HpnicfDvpnGlobalUserDefAAADomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 25),
    _HpnicfDvpnGlobalUserDefAAADomain_Type()
)
hpnicfDvpnGlobalUserDefAAADomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnGlobalUserDefAAADomain.setStatus("current")
_HpnicfDvpnLocalDeviceId_Type = OctetString
_HpnicfDvpnLocalDeviceId_Object = MibScalar
hpnicfDvpnLocalDeviceId = _HpnicfDvpnLocalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 26),
    _HpnicfDvpnLocalDeviceId_Type()
)
hpnicfDvpnLocalDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnLocalDeviceId.setStatus("current")


class _HpnicfDvpnSessionHisAgeTime_Type(Integer32):
    """Custom type hpnicfDvpnSessionHisAgeTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfDvpnSessionHisAgeTime_Type.__name__ = "Integer32"
_HpnicfDvpnSessionHisAgeTime_Object = MibScalar
hpnicfDvpnSessionHisAgeTime = _HpnicfDvpnSessionHisAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 27),
    _HpnicfDvpnSessionHisAgeTime_Type()
)
hpnicfDvpnSessionHisAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisAgeTime.setStatus("current")


class _HpnicfDvpnSessionHisReset_Type(Integer32):
    """Custom type hpnicfDvpnSessionHisReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDvpnSessionHisReset_Type.__name__ = "Integer32"
_HpnicfDvpnSessionHisReset_Object = MibScalar
hpnicfDvpnSessionHisReset = _HpnicfDvpnSessionHisReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 1, 28),
    _HpnicfDvpnSessionHisReset_Type()
)
hpnicfDvpnSessionHisReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisReset.setStatus("current")
_HpnicfDvpnMibTableTroop_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibTableTroop = _HpnicfDvpnMibTableTroop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2)
)
_HpnicfDvpnPolicyTable_Object = MibTable
hpnicfDvpnPolicyTable = _HpnicfDvpnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDvpnPolicyTable.setStatus("current")
_HpnicfDvpnPolicyEntry_Object = MibTableRow
hpnicfDvpnPolicyEntry = _HpnicfDvpnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1)
)
hpnicfDvpnPolicyEntry.setIndexNames(
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnPolicyName"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnPolicyEntry.setStatus("current")


class _HpnicfDvpnPolicyName_Type(OctetString):
    """Custom type hpnicfDvpnPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfDvpnPolicyName_Type.__name__ = "OctetString"
_HpnicfDvpnPolicyName_Object = MibTableColumn
hpnicfDvpnPolicyName = _HpnicfDvpnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 1),
    _HpnicfDvpnPolicyName_Type()
)
hpnicfDvpnPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDvpnPolicyName.setStatus("current")


class _HpnicfDvpnPoAuthenClientType_Type(Integer32):
    """Custom type hpnicfDvpnPoAuthenClientType based on Integer32"""
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


_HpnicfDvpnPoAuthenClientType_Type.__name__ = "Integer32"
_HpnicfDvpnPoAuthenClientType_Object = MibTableColumn
hpnicfDvpnPoAuthenClientType = _HpnicfDvpnPoAuthenClientType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 2),
    _HpnicfDvpnPoAuthenClientType_Type()
)
hpnicfDvpnPoAuthenClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoAuthenClientType.setStatus("current")


class _HpnicfDvpnPoSessionAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type hpnicfDvpnPoSessionAlgorithmSuite based on DvpnAlgorithmSuite"""


_HpnicfDvpnPoSessionAlgorithmSuite_Object = MibTableColumn
hpnicfDvpnPoSessionAlgorithmSuite = _HpnicfDvpnPoSessionAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 3),
    _HpnicfDvpnPoSessionAlgorithmSuite_Type()
)
hpnicfDvpnPoSessionAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoSessionAlgorithmSuite.setStatus("current")


class _HpnicfDvpnPoSessionIdleTime_Type(Integer32):
    """Custom type hpnicfDvpnPoSessionIdleTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_HpnicfDvpnPoSessionIdleTime_Type.__name__ = "Integer32"
_HpnicfDvpnPoSessionIdleTime_Object = MibTableColumn
hpnicfDvpnPoSessionIdleTime = _HpnicfDvpnPoSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 4),
    _HpnicfDvpnPoSessionIdleTime_Type()
)
hpnicfDvpnPoSessionIdleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoSessionIdleTime.setStatus("current")


class _HpnicfDvpnPoSessionKeepTime_Type(Integer32):
    """Custom type hpnicfDvpnPoSessionKeepTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HpnicfDvpnPoSessionKeepTime_Type.__name__ = "Integer32"
_HpnicfDvpnPoSessionKeepTime_Object = MibTableColumn
hpnicfDvpnPoSessionKeepTime = _HpnicfDvpnPoSessionKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 5),
    _HpnicfDvpnPoSessionKeepTime_Type()
)
hpnicfDvpnPoSessionKeepTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoSessionKeepTime.setStatus("current")


class _HpnicfDvpnPoSessionSetupInterval_Type(Integer32):
    """Custom type hpnicfDvpnPoSessionSetupInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_HpnicfDvpnPoSessionSetupInterval_Type.__name__ = "Integer32"
_HpnicfDvpnPoSessionSetupInterval_Object = MibTableColumn
hpnicfDvpnPoSessionSetupInterval = _HpnicfDvpnPoSessionSetupInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 6),
    _HpnicfDvpnPoSessionSetupInterval_Type()
)
hpnicfDvpnPoSessionSetupInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoSessionSetupInterval.setStatus("current")


class _HpnicfDvpnPoDataAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type hpnicfDvpnPoDataAlgorithmSuite based on DvpnAlgorithmSuite"""


_HpnicfDvpnPoDataAlgorithmSuite_Object = MibTableColumn
hpnicfDvpnPoDataAlgorithmSuite = _HpnicfDvpnPoDataAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 7),
    _HpnicfDvpnPoDataAlgorithmSuite_Type()
)
hpnicfDvpnPoDataAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoDataAlgorithmSuite.setStatus("current")


class _HpnicfDvpnPoSaSeconds_Type(Integer32):
    """Custom type hpnicfDvpnPoSaSeconds based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 604800),
    )


_HpnicfDvpnPoSaSeconds_Type.__name__ = "Integer32"
_HpnicfDvpnPoSaSeconds_Object = MibTableColumn
hpnicfDvpnPoSaSeconds = _HpnicfDvpnPoSaSeconds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 8),
    _HpnicfDvpnPoSaSeconds_Type()
)
hpnicfDvpnPoSaSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoSaSeconds.setStatus("current")


class _HpnicfDvpnPoUserDefAAADomain_Type(OctetString):
    """Custom type hpnicfDvpnPoUserDefAAADomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HpnicfDvpnPoUserDefAAADomain_Type.__name__ = "OctetString"
_HpnicfDvpnPoUserDefAAADomain_Object = MibTableColumn
hpnicfDvpnPoUserDefAAADomain = _HpnicfDvpnPoUserDefAAADomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 9),
    _HpnicfDvpnPoUserDefAAADomain_Type()
)
hpnicfDvpnPoUserDefAAADomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoUserDefAAADomain.setStatus("current")
_HpnicfDvpnPoRefTimes_Type = Integer32
_HpnicfDvpnPoRefTimes_Object = MibTableColumn
hpnicfDvpnPoRefTimes = _HpnicfDvpnPoRefTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 10),
    _HpnicfDvpnPoRefTimes_Type()
)
hpnicfDvpnPoRefTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnPoRefTimes.setStatus("current")
_HpnicfDvpnPoRowStatus_Type = RowStatus
_HpnicfDvpnPoRowStatus_Object = MibTableColumn
hpnicfDvpnPoRowStatus = _HpnicfDvpnPoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 1, 1, 11),
    _HpnicfDvpnPoRowStatus_Type()
)
hpnicfDvpnPoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnPoRowStatus.setStatus("current")
_HpnicfDvpnDomainInfoTable_Object = MibTable
hpnicfDvpnDomainInfoTable = _HpnicfDvpnDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDvpnDomainInfoTable.setStatus("current")
_HpnicfDvpnDomainInfoEntry_Object = MibTableRow
hpnicfDvpnDomainInfoEntry = _HpnicfDvpnDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1)
)
hpnicfDvpnDomainInfoEntry.setIndexNames(
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainID"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnDomainInfoEntry.setStatus("current")


class _HpnicfDvpnDomainID_Type(Integer32):
    """Custom type hpnicfDvpnDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfDvpnDomainID_Type.__name__ = "Integer32"
_HpnicfDvpnDomainID_Object = MibTableColumn
hpnicfDvpnDomainID = _HpnicfDvpnDomainID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 1),
    _HpnicfDvpnDomainID_Type()
)
hpnicfDvpnDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainID.setStatus("current")
_HpnicfDvpnDomainSessionNum_Type = Unsigned32
_HpnicfDvpnDomainSessionNum_Object = MibTableColumn
hpnicfDvpnDomainSessionNum = _HpnicfDvpnDomainSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 2),
    _HpnicfDvpnDomainSessionNum_Type()
)
hpnicfDvpnDomainSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainSessionNum.setStatus("current")
_HpnicfDvpnDomainRedirectNum_Type = Unsigned32
_HpnicfDvpnDomainRedirectNum_Object = MibTableColumn
hpnicfDvpnDomainRedirectNum = _HpnicfDvpnDomainRedirectNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 3),
    _HpnicfDvpnDomainRedirectNum_Type()
)
hpnicfDvpnDomainRedirectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainRedirectNum.setStatus("current")
_HpnicfDvpnDomainInputPkt_Type = Unsigned32
_HpnicfDvpnDomainInputPkt_Object = MibTableColumn
hpnicfDvpnDomainInputPkt = _HpnicfDvpnDomainInputPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 4),
    _HpnicfDvpnDomainInputPkt_Type()
)
hpnicfDvpnDomainInputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainInputPkt.setStatus("current")
_HpnicfDvpnDomainDropPkt_Type = Unsigned32
_HpnicfDvpnDomainDropPkt_Object = MibTableColumn
hpnicfDvpnDomainDropPkt = _HpnicfDvpnDomainDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 5),
    _HpnicfDvpnDomainDropPkt_Type()
)
hpnicfDvpnDomainDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainDropPkt.setStatus("current")
_HpnicfDvpnDomainOutputPkt_Type = Unsigned32
_HpnicfDvpnDomainOutputPkt_Object = MibTableColumn
hpnicfDvpnDomainOutputPkt = _HpnicfDvpnDomainOutputPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 6),
    _HpnicfDvpnDomainOutputPkt_Type()
)
hpnicfDvpnDomainOutputPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainOutputPkt.setStatus("current")
_HpnicfDvpnDomainOutputErrorPkt_Type = Unsigned32
_HpnicfDvpnDomainOutputErrorPkt_Object = MibTableColumn
hpnicfDvpnDomainOutputErrorPkt = _HpnicfDvpnDomainOutputErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 7),
    _HpnicfDvpnDomainOutputErrorPkt_Type()
)
hpnicfDvpnDomainOutputErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainOutputErrorPkt.setStatus("current")
_HpnicfDvpnDomainEncryptErrorPkt_Type = Unsigned32
_HpnicfDvpnDomainEncryptErrorPkt_Object = MibTableColumn
hpnicfDvpnDomainEncryptErrorPkt = _HpnicfDvpnDomainEncryptErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 2, 1, 8),
    _HpnicfDvpnDomainEncryptErrorPkt_Type()
)
hpnicfDvpnDomainEncryptErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnDomainEncryptErrorPkt.setStatus("current")
_HpnicfDvpnClassTable_Object = MibTable
hpnicfDvpnClassTable = _HpnicfDvpnClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDvpnClassTable.setStatus("current")
_HpnicfDvpnClassEntry_Object = MibTableRow
hpnicfDvpnClassEntry = _HpnicfDvpnClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1)
)
hpnicfDvpnClassEntry.setIndexNames(
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnClassName"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnClassEntry.setStatus("current")


class _HpnicfDvpnClassName_Type(OctetString):
    """Custom type hpnicfDvpnClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfDvpnClassName_Type.__name__ = "OctetString"
_HpnicfDvpnClassName_Object = MibTableColumn
hpnicfDvpnClassName = _HpnicfDvpnClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 1),
    _HpnicfDvpnClassName_Type()
)
hpnicfDvpnClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDvpnClassName.setStatus("current")
_HpnicfDvpnClServerPublicIpType_Type = InetAddressType
_HpnicfDvpnClServerPublicIpType_Object = MibTableColumn
hpnicfDvpnClServerPublicIpType = _HpnicfDvpnClServerPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 2),
    _HpnicfDvpnClServerPublicIpType_Type()
)
hpnicfDvpnClServerPublicIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClServerPublicIpType.setStatus("current")
_HpnicfDvpnClServerPublicIp_Type = InetAddress
_HpnicfDvpnClServerPublicIp_Object = MibTableColumn
hpnicfDvpnClServerPublicIp = _HpnicfDvpnClServerPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 3),
    _HpnicfDvpnClServerPublicIp_Type()
)
hpnicfDvpnClServerPublicIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClServerPublicIp.setStatus("current")
_HpnicfDvpnClServerPriIpType_Type = InetAddressType
_HpnicfDvpnClServerPriIpType_Object = MibTableColumn
hpnicfDvpnClServerPriIpType = _HpnicfDvpnClServerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 4),
    _HpnicfDvpnClServerPriIpType_Type()
)
hpnicfDvpnClServerPriIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClServerPriIpType.setStatus("current")
_HpnicfDvpnClServerPriIp_Type = InetAddress
_HpnicfDvpnClServerPriIp_Object = MibTableColumn
hpnicfDvpnClServerPriIp = _HpnicfDvpnClServerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 5),
    _HpnicfDvpnClServerPriIp_Type()
)
hpnicfDvpnClServerPriIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClServerPriIp.setStatus("current")


class _HpnicfDvpnClAlgorithmSuite_Type(DvpnAlgorithmSuite):
    """Custom type hpnicfDvpnClAlgorithmSuite based on DvpnAlgorithmSuite"""


_HpnicfDvpnClAlgorithmSuite_Object = MibTableColumn
hpnicfDvpnClAlgorithmSuite = _HpnicfDvpnClAlgorithmSuite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 6),
    _HpnicfDvpnClAlgorithmSuite_Type()
)
hpnicfDvpnClAlgorithmSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClAlgorithmSuite.setStatus("current")


class _HpnicfDvpnClAuthenServerType_Type(Integer32):
    """Custom type hpnicfDvpnClAuthenServerType based on Integer32"""
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


_HpnicfDvpnClAuthenServerType_Type.__name__ = "Integer32"
_HpnicfDvpnClAuthenServerType_Object = MibTableColumn
hpnicfDvpnClAuthenServerType = _HpnicfDvpnClAuthenServerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 7),
    _HpnicfDvpnClAuthenServerType_Type()
)
hpnicfDvpnClAuthenServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClAuthenServerType.setStatus("current")


class _HpnicfDvpnClPreShareKey_Type(OctetString):
    """Custom type hpnicfDvpnClPreShareKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDvpnClPreShareKey_Type.__name__ = "OctetString"
_HpnicfDvpnClPreShareKey_Object = MibTableColumn
hpnicfDvpnClPreShareKey = _HpnicfDvpnClPreShareKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 8),
    _HpnicfDvpnClPreShareKey_Type()
)
hpnicfDvpnClPreShareKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClPreShareKey.setStatus("current")


class _HpnicfDvpnClUserName_Type(OctetString):
    """Custom type hpnicfDvpnClUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnicfDvpnClUserName_Type.__name__ = "OctetString"
_HpnicfDvpnClUserName_Object = MibTableColumn
hpnicfDvpnClUserName = _HpnicfDvpnClUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 9),
    _HpnicfDvpnClUserName_Type()
)
hpnicfDvpnClUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClUserName.setStatus("current")


class _HpnicfDvpnClPwdEncrypted_Type(Integer32):
    """Custom type hpnicfDvpnClPwdEncrypted based on Integer32"""
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


_HpnicfDvpnClPwdEncrypted_Type.__name__ = "Integer32"
_HpnicfDvpnClPwdEncrypted_Object = MibTableColumn
hpnicfDvpnClPwdEncrypted = _HpnicfDvpnClPwdEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 10),
    _HpnicfDvpnClPwdEncrypted_Type()
)
hpnicfDvpnClPwdEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClPwdEncrypted.setStatus("current")
_HpnicfDvpnClPasswd_Type = OctetString
_HpnicfDvpnClPasswd_Object = MibTableColumn
hpnicfDvpnClPasswd = _HpnicfDvpnClPasswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 11),
    _HpnicfDvpnClPasswd_Type()
)
hpnicfDvpnClPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClPasswd.setStatus("current")
_HpnicfDvpnClassRowStatus_Type = RowStatus
_HpnicfDvpnClassRowStatus_Object = MibTableColumn
hpnicfDvpnClassRowStatus = _HpnicfDvpnClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 3, 1, 12),
    _HpnicfDvpnClassRowStatus_Type()
)
hpnicfDvpnClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDvpnClassRowStatus.setStatus("current")
_HpnicfDvpnTunnelTable_Object = MibTable
hpnicfDvpnTunnelTable = _HpnicfDvpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelTable.setStatus("current")
_HpnicfDvpnTunnelEntry_Object = MibTableRow
hpnicfDvpnTunnelEntry = _HpnicfDvpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1)
)
hpnicfDvpnTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelEntry.setStatus("current")


class _HpnicfDvpnTunnelInterfaceType_Type(Integer32):
    """Custom type hpnicfDvpnTunnelInterfaceType based on Integer32"""
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


_HpnicfDvpnTunnelInterfaceType_Type.__name__ = "Integer32"
_HpnicfDvpnTunnelInterfaceType_Object = MibTableColumn
hpnicfDvpnTunnelInterfaceType = _HpnicfDvpnTunnelInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1, 1),
    _HpnicfDvpnTunnelInterfaceType_Type()
)
hpnicfDvpnTunnelInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelInterfaceType.setStatus("current")
_HpnicfDvpnTunnelAcl_Type = Integer32
_HpnicfDvpnTunnelAcl_Object = MibTableColumn
hpnicfDvpnTunnelAcl = _HpnicfDvpnTunnelAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1, 2),
    _HpnicfDvpnTunnelAcl_Type()
)
hpnicfDvpnTunnelAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelAcl.setStatus("current")


class _HpnicfDvpnTunnelClientRegType_Type(Integer32):
    """Custom type hpnicfDvpnTunnelClientRegType based on Integer32"""
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


_HpnicfDvpnTunnelClientRegType_Type.__name__ = "Integer32"
_HpnicfDvpnTunnelClientRegType_Object = MibTableColumn
hpnicfDvpnTunnelClientRegType = _HpnicfDvpnTunnelClientRegType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1, 3),
    _HpnicfDvpnTunnelClientRegType_Type()
)
hpnicfDvpnTunnelClientRegType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelClientRegType.setStatus("current")


class _HpnicfDvpnTunnelDvpnId_Type(Integer32):
    """Custom type hpnicfDvpnTunnelDvpnId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDvpnTunnelDvpnId_Type.__name__ = "Integer32"
_HpnicfDvpnTunnelDvpnId_Object = MibTableColumn
hpnicfDvpnTunnelDvpnId = _HpnicfDvpnTunnelDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1, 4),
    _HpnicfDvpnTunnelDvpnId_Type()
)
hpnicfDvpnTunnelDvpnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelDvpnId.setStatus("current")


class _HpnicfDvpnTunnelPolicy_Type(OctetString):
    """Custom type hpnicfDvpnTunnelPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfDvpnTunnelPolicy_Type.__name__ = "OctetString"
_HpnicfDvpnTunnelPolicy_Object = MibTableColumn
hpnicfDvpnTunnelPolicy = _HpnicfDvpnTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1, 5),
    _HpnicfDvpnTunnelPolicy_Type()
)
hpnicfDvpnTunnelPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelPolicy.setStatus("current")


class _HpnicfDvpnTunnelClass_Type(OctetString):
    """Custom type hpnicfDvpnTunnelClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfDvpnTunnelClass_Type.__name__ = "OctetString"
_HpnicfDvpnTunnelClass_Object = MibTableColumn
hpnicfDvpnTunnelClass = _HpnicfDvpnTunnelClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 4, 1, 6),
    _HpnicfDvpnTunnelClass_Type()
)
hpnicfDvpnTunnelClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelClass.setStatus("current")
_HpnicfDvpnMapTable_Object = MibTable
hpnicfDvpnMapTable = _HpnicfDvpnMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfDvpnMapTable.setStatus("current")
_HpnicfDvpnMapEntry_Object = MibTableRow
hpnicfDvpnMapEntry = _HpnicfDvpnMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1)
)
hpnicfDvpnMapEntry.setIndexNames(
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnMapIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnMapEntry.setStatus("current")
_HpnicfDvpnMapIndex_Type = Unsigned32
_HpnicfDvpnMapIndex_Object = MibTableColumn
hpnicfDvpnMapIndex = _HpnicfDvpnMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 1),
    _HpnicfDvpnMapIndex_Type()
)
hpnicfDvpnMapIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDvpnMapIndex.setStatus("current")
_HpnicfDvpnMapPeerDeviceId_Type = OctetString
_HpnicfDvpnMapPeerDeviceId_Object = MibTableColumn
hpnicfDvpnMapPeerDeviceId = _HpnicfDvpnMapPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 2),
    _HpnicfDvpnMapPeerDeviceId_Type()
)
hpnicfDvpnMapPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapPeerDeviceId.setStatus("current")
_HpnicfDvpnMapDvpnId_Type = Unsigned32
_HpnicfDvpnMapDvpnId_Object = MibTableColumn
hpnicfDvpnMapDvpnId = _HpnicfDvpnMapDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 3),
    _HpnicfDvpnMapDvpnId_Type()
)
hpnicfDvpnMapDvpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapDvpnId.setStatus("current")
_HpnicfDvpnMapBuildTime_Type = TimeTicks
_HpnicfDvpnMapBuildTime_Object = MibTableColumn
hpnicfDvpnMapBuildTime = _HpnicfDvpnMapBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 4),
    _HpnicfDvpnMapBuildTime_Type()
)
hpnicfDvpnMapBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapBuildTime.setStatus("current")
_HpnicfDvpnMapPeerPriIpType_Type = InetAddressType
_HpnicfDvpnMapPeerPriIpType_Object = MibTableColumn
hpnicfDvpnMapPeerPriIpType = _HpnicfDvpnMapPeerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 5),
    _HpnicfDvpnMapPeerPriIpType_Type()
)
hpnicfDvpnMapPeerPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapPeerPriIpType.setStatus("current")
_HpnicfDvpnMapPeerPriIp_Type = InetAddress
_HpnicfDvpnMapPeerPriIp_Object = MibTableColumn
hpnicfDvpnMapPeerPriIp = _HpnicfDvpnMapPeerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 6),
    _HpnicfDvpnMapPeerPriIp_Type()
)
hpnicfDvpnMapPeerPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapPeerPriIp.setStatus("current")
_HpnicfDvpnMapPeerPublicIpType_Type = InetAddressType
_HpnicfDvpnMapPeerPublicIpType_Object = MibTableColumn
hpnicfDvpnMapPeerPublicIpType = _HpnicfDvpnMapPeerPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 7),
    _HpnicfDvpnMapPeerPublicIpType_Type()
)
hpnicfDvpnMapPeerPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapPeerPublicIpType.setStatus("current")
_HpnicfDvpnMapPeerPublicIp_Type = InetAddress
_HpnicfDvpnMapPeerPublicIp_Object = MibTableColumn
hpnicfDvpnMapPeerPublicIp = _HpnicfDvpnMapPeerPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 8),
    _HpnicfDvpnMapPeerPublicIp_Type()
)
hpnicfDvpnMapPeerPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapPeerPublicIp.setStatus("current")
_HpnicfDvpnMapLocalPriIpType_Type = InetAddressType
_HpnicfDvpnMapLocalPriIpType_Object = MibTableColumn
hpnicfDvpnMapLocalPriIpType = _HpnicfDvpnMapLocalPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 9),
    _HpnicfDvpnMapLocalPriIpType_Type()
)
hpnicfDvpnMapLocalPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapLocalPriIpType.setStatus("current")
_HpnicfDvpnMapLocalPriIp_Type = InetAddress
_HpnicfDvpnMapLocalPriIp_Object = MibTableColumn
hpnicfDvpnMapLocalPriIp = _HpnicfDvpnMapLocalPriIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 10),
    _HpnicfDvpnMapLocalPriIp_Type()
)
hpnicfDvpnMapLocalPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapLocalPriIp.setStatus("current")
_HpnicfDvpnMapLocalPublicIpType_Type = InetAddressType
_HpnicfDvpnMapLocalPublicIpType_Object = MibTableColumn
hpnicfDvpnMapLocalPublicIpType = _HpnicfDvpnMapLocalPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 11),
    _HpnicfDvpnMapLocalPublicIpType_Type()
)
hpnicfDvpnMapLocalPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapLocalPublicIpType.setStatus("current")
_HpnicfDvpnMapLocalPublicIp_Type = InetAddress
_HpnicfDvpnMapLocalPublicIp_Object = MibTableColumn
hpnicfDvpnMapLocalPublicIp = _HpnicfDvpnMapLocalPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 12),
    _HpnicfDvpnMapLocalPublicIp_Type()
)
hpnicfDvpnMapLocalPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapLocalPublicIp.setStatus("current")
_HpnicfDvpnMapUserName_Type = OctetString
_HpnicfDvpnMapUserName_Object = MibTableColumn
hpnicfDvpnMapUserName = _HpnicfDvpnMapUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 13),
    _HpnicfDvpnMapUserName_Type()
)
hpnicfDvpnMapUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapUserName.setStatus("current")
_HpnicfDvpnMapUdpPort_Type = Integer32
_HpnicfDvpnMapUdpPort_Object = MibTableColumn
hpnicfDvpnMapUdpPort = _HpnicfDvpnMapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 14),
    _HpnicfDvpnMapUdpPort_Type()
)
hpnicfDvpnMapUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapUdpPort.setStatus("current")
_HpnicfDvpnMapControlId_Type = Unsigned32
_HpnicfDvpnMapControlId_Object = MibTableColumn
hpnicfDvpnMapControlId = _HpnicfDvpnMapControlId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 15),
    _HpnicfDvpnMapControlId_Type()
)
hpnicfDvpnMapControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapControlId.setStatus("current")
_HpnicfDvpnMapType_Type = DvpnCommunicateType
_HpnicfDvpnMapType_Object = MibTableColumn
hpnicfDvpnMapType = _HpnicfDvpnMapType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 16),
    _HpnicfDvpnMapType_Type()
)
hpnicfDvpnMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapType.setStatus("current")


class _HpnicfDvpnMapState_Type(Integer32):
    """Custom type hpnicfDvpnMapState based on Integer32"""
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


_HpnicfDvpnMapState_Type.__name__ = "Integer32"
_HpnicfDvpnMapState_Object = MibTableColumn
hpnicfDvpnMapState = _HpnicfDvpnMapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 5, 1, 17),
    _HpnicfDvpnMapState_Type()
)
hpnicfDvpnMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnMapState.setStatus("current")
_HpnicfDvpnSessionTable_Object = MibTable
hpnicfDvpnSessionTable = _HpnicfDvpnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionTable.setStatus("current")
_HpnicfDvpnSessionEntry_Object = MibTableRow
hpnicfDvpnSessionEntry = _HpnicfDvpnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1)
)
hpnicfDvpnSessionEntry.setIndexNames(
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionDvpnId"),
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIpType"),
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIp"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionEntry.setStatus("current")
_HpnicfDvpnSessionDvpnId_Type = Integer32
_HpnicfDvpnSessionDvpnId_Object = MibTableColumn
hpnicfDvpnSessionDvpnId = _HpnicfDvpnSessionDvpnId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 1),
    _HpnicfDvpnSessionDvpnId_Type()
)
hpnicfDvpnSessionDvpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionDvpnId.setStatus("current")
_HpnicfDvpnSessionPeerPriIpType_Type = InetAddressType
_HpnicfDvpnSessionPeerPriIpType_Object = MibTableColumn
hpnicfDvpnSessionPeerPriIpType = _HpnicfDvpnSessionPeerPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 2),
    _HpnicfDvpnSessionPeerPriIpType_Type()
)
hpnicfDvpnSessionPeerPriIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerPriIpType.setStatus("current")
_HpnicfDvpnSessionPeerPriIp_Type = InetAddress
_HpnicfDvpnSessionPeerPriIp_Object = MibTableColumn
hpnicfDvpnSessionPeerPriIp = _HpnicfDvpnSessionPeerPriIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 3),
    _HpnicfDvpnSessionPeerPriIp_Type()
)
hpnicfDvpnSessionPeerPriIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerPriIp.setStatus("current")
_HpnicfDvpnSessionPeerDeviceId_Type = OctetString
_HpnicfDvpnSessionPeerDeviceId_Object = MibTableColumn
hpnicfDvpnSessionPeerDeviceId = _HpnicfDvpnSessionPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 4),
    _HpnicfDvpnSessionPeerDeviceId_Type()
)
hpnicfDvpnSessionPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerDeviceId.setStatus("current")
_HpnicfDvpnSessionBuildTime_Type = TimeTicks
_HpnicfDvpnSessionBuildTime_Object = MibTableColumn
hpnicfDvpnSessionBuildTime = _HpnicfDvpnSessionBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 5),
    _HpnicfDvpnSessionBuildTime_Type()
)
hpnicfDvpnSessionBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionBuildTime.setStatus("current")
_HpnicfDvpnSessionPeerPubIpType_Type = InetAddressType
_HpnicfDvpnSessionPeerPubIpType_Object = MibTableColumn
hpnicfDvpnSessionPeerPubIpType = _HpnicfDvpnSessionPeerPubIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 6),
    _HpnicfDvpnSessionPeerPubIpType_Type()
)
hpnicfDvpnSessionPeerPubIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerPubIpType.setStatus("current")
_HpnicfDvpnSessionPeerPubIp_Type = InetAddress
_HpnicfDvpnSessionPeerPubIp_Object = MibTableColumn
hpnicfDvpnSessionPeerPubIp = _HpnicfDvpnSessionPeerPubIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 7),
    _HpnicfDvpnSessionPeerPubIp_Type()
)
hpnicfDvpnSessionPeerPubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerPubIp.setStatus("current")
_HpnicfDvpnSessionLocalPubIpType_Type = InetAddressType
_HpnicfDvpnSessionLocalPubIpType_Object = MibTableColumn
hpnicfDvpnSessionLocalPubIpType = _HpnicfDvpnSessionLocalPubIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 8),
    _HpnicfDvpnSessionLocalPubIpType_Type()
)
hpnicfDvpnSessionLocalPubIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionLocalPubIpType.setStatus("current")
_HpnicfDvpnSessionLocalPubIp_Type = InetAddress
_HpnicfDvpnSessionLocalPubIp_Object = MibTableColumn
hpnicfDvpnSessionLocalPubIp = _HpnicfDvpnSessionLocalPubIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 9),
    _HpnicfDvpnSessionLocalPubIp_Type()
)
hpnicfDvpnSessionLocalPubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionLocalPubIp.setStatus("current")
_HpnicfDvpnSessionLocalPriIpType_Type = InetAddressType
_HpnicfDvpnSessionLocalPriIpType_Object = MibTableColumn
hpnicfDvpnSessionLocalPriIpType = _HpnicfDvpnSessionLocalPriIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 10),
    _HpnicfDvpnSessionLocalPriIpType_Type()
)
hpnicfDvpnSessionLocalPriIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionLocalPriIpType.setStatus("current")
_HpnicfDvpnSessionLocalPriIp_Type = InetAddress
_HpnicfDvpnSessionLocalPriIp_Object = MibTableColumn
hpnicfDvpnSessionLocalPriIp = _HpnicfDvpnSessionLocalPriIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 11),
    _HpnicfDvpnSessionLocalPriIp_Type()
)
hpnicfDvpnSessionLocalPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionLocalPriIp.setStatus("current")
_HpnicfDvpnSessionPeerUdpPort_Type = Integer32
_HpnicfDvpnSessionPeerUdpPort_Object = MibTableColumn
hpnicfDvpnSessionPeerUdpPort = _HpnicfDvpnSessionPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 12),
    _HpnicfDvpnSessionPeerUdpPort_Type()
)
hpnicfDvpnSessionPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerUdpPort.setStatus("current")


class _HpnicfDvpnSessionInitiator_Type(Integer32):
    """Custom type hpnicfDvpnSessionInitiator based on Integer32"""
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


_HpnicfDvpnSessionInitiator_Type.__name__ = "Integer32"
_HpnicfDvpnSessionInitiator_Object = MibTableColumn
hpnicfDvpnSessionInitiator = _HpnicfDvpnSessionInitiator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 13),
    _HpnicfDvpnSessionInitiator_Type()
)
hpnicfDvpnSessionInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionInitiator.setStatus("current")
_HpnicfDvpnSessionUserName_Type = OctetString
_HpnicfDvpnSessionUserName_Object = MibTableColumn
hpnicfDvpnSessionUserName = _HpnicfDvpnSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 14),
    _HpnicfDvpnSessionUserName_Type()
)
hpnicfDvpnSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionUserName.setStatus("current")


class _HpnicfDvpnSessionState_Type(Integer32):
    """Custom type hpnicfDvpnSessionState based on Integer32"""
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


_HpnicfDvpnSessionState_Type.__name__ = "Integer32"
_HpnicfDvpnSessionState_Object = MibTableColumn
hpnicfDvpnSessionState = _HpnicfDvpnSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 15),
    _HpnicfDvpnSessionState_Type()
)
hpnicfDvpnSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionState.setStatus("current")
_HpnicfDvpnSessionType_Type = DvpnCommunicateType
_HpnicfDvpnSessionType_Object = MibTableColumn
hpnicfDvpnSessionType = _HpnicfDvpnSessionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 16),
    _HpnicfDvpnSessionType_Type()
)
hpnicfDvpnSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionType.setStatus("current")


class _HpnicfDvpnSessionPeerType_Type(Integer32):
    """Custom type hpnicfDvpnSessionPeerType based on Integer32"""
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


_HpnicfDvpnSessionPeerType_Type.__name__ = "Integer32"
_HpnicfDvpnSessionPeerType_Object = MibTableColumn
hpnicfDvpnSessionPeerType = _HpnicfDvpnSessionPeerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 6, 1, 17),
    _HpnicfDvpnSessionPeerType_Type()
)
hpnicfDvpnSessionPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionPeerType.setStatus("current")
_HpnicfDvpnSessionHisTable_Object = MibTable
hpnicfDvpnSessionHisTable = _HpnicfDvpnSessionHisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisTable.setStatus("current")
_HpnicfDvpnSessionHisEntry_Object = MibTableRow
hpnicfDvpnSessionHisEntry = _HpnicfDvpnSessionHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1)
)
hpnicfDvpnSessionHisEntry.setIndexNames(
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisDvpnID"),
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisPeerPriIPType"),
    (0, "HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisPeerPriIP"),
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisEntry.setStatus("current")


class _HpnicfDvpnSessionHisDvpnID_Type(Integer32):
    """Custom type hpnicfDvpnSessionHisDvpnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfDvpnSessionHisDvpnID_Type.__name__ = "Integer32"
_HpnicfDvpnSessionHisDvpnID_Object = MibTableColumn
hpnicfDvpnSessionHisDvpnID = _HpnicfDvpnSessionHisDvpnID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 1),
    _HpnicfDvpnSessionHisDvpnID_Type()
)
hpnicfDvpnSessionHisDvpnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisDvpnID.setStatus("current")
_HpnicfDvpnSessionHisPeerPriIPType_Type = InetAddressType
_HpnicfDvpnSessionHisPeerPriIPType_Object = MibTableColumn
hpnicfDvpnSessionHisPeerPriIPType = _HpnicfDvpnSessionHisPeerPriIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 2),
    _HpnicfDvpnSessionHisPeerPriIPType_Type()
)
hpnicfDvpnSessionHisPeerPriIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisPeerPriIPType.setStatus("current")
_HpnicfDvpnSessionHisPeerPriIP_Type = InetAddress
_HpnicfDvpnSessionHisPeerPriIP_Object = MibTableColumn
hpnicfDvpnSessionHisPeerPriIP = _HpnicfDvpnSessionHisPeerPriIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 3),
    _HpnicfDvpnSessionHisPeerPriIP_Type()
)
hpnicfDvpnSessionHisPeerPriIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisPeerPriIP.setStatus("current")
_HpnicfDvpnSessionHisSendPkt_Type = Unsigned32
_HpnicfDvpnSessionHisSendPkt_Object = MibTableColumn
hpnicfDvpnSessionHisSendPkt = _HpnicfDvpnSessionHisSendPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 4),
    _HpnicfDvpnSessionHisSendPkt_Type()
)
hpnicfDvpnSessionHisSendPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisSendPkt.setStatus("current")
_HpnicfDvpnSessionHisRcvPkt_Type = Unsigned32
_HpnicfDvpnSessionHisRcvPkt_Object = MibTableColumn
hpnicfDvpnSessionHisRcvPkt = _HpnicfDvpnSessionHisRcvPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 5),
    _HpnicfDvpnSessionHisRcvPkt_Type()
)
hpnicfDvpnSessionHisRcvPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisRcvPkt.setStatus("current")
_HpnicfDvpnSessionHisOnlineNumber_Type = Unsigned32
_HpnicfDvpnSessionHisOnlineNumber_Object = MibTableColumn
hpnicfDvpnSessionHisOnlineNumber = _HpnicfDvpnSessionHisOnlineNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 6),
    _HpnicfDvpnSessionHisOnlineNumber_Type()
)
hpnicfDvpnSessionHisOnlineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisOnlineNumber.setStatus("current")
_HpnicfDvpnSessionHisFirstUpTime_Type = TimeTicks
_HpnicfDvpnSessionHisFirstUpTime_Object = MibTableColumn
hpnicfDvpnSessionHisFirstUpTime = _HpnicfDvpnSessionHisFirstUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 7),
    _HpnicfDvpnSessionHisFirstUpTime_Type()
)
hpnicfDvpnSessionHisFirstUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisFirstUpTime.setStatus("current")
_HpnicfDvpnSessionHisLastUpTime_Type = TimeTicks
_HpnicfDvpnSessionHisLastUpTime_Object = MibTableColumn
hpnicfDvpnSessionHisLastUpTime = _HpnicfDvpnSessionHisLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 8),
    _HpnicfDvpnSessionHisLastUpTime_Type()
)
hpnicfDvpnSessionHisLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisLastUpTime.setStatus("current")
_HpnicfDvpnSessionHisLastDownTime_Type = TimeTicks
_HpnicfDvpnSessionHisLastDownTime_Object = MibTableColumn
hpnicfDvpnSessionHisLastDownTime = _HpnicfDvpnSessionHisLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 9),
    _HpnicfDvpnSessionHisLastDownTime_Type()
)
hpnicfDvpnSessionHisLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisLastDownTime.setStatus("current")


class _HpnicfDvpnSessionHisOnlineFlag_Type(Integer32):
    """Custom type hpnicfDvpnSessionHisOnlineFlag based on Integer32"""
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


_HpnicfDvpnSessionHisOnlineFlag_Type.__name__ = "Integer32"
_HpnicfDvpnSessionHisOnlineFlag_Object = MibTableColumn
hpnicfDvpnSessionHisOnlineFlag = _HpnicfDvpnSessionHisOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 10),
    _HpnicfDvpnSessionHisOnlineFlag_Type()
)
hpnicfDvpnSessionHisOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisOnlineFlag.setStatus("current")
_HpnicfDvpnSessionHisPeerDeviceId_Type = OctetString
_HpnicfDvpnSessionHisPeerDeviceId_Object = MibTableColumn
hpnicfDvpnSessionHisPeerDeviceId = _HpnicfDvpnSessionHisPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 2, 7, 1, 11),
    _HpnicfDvpnSessionHisPeerDeviceId_Type()
)
hpnicfDvpnSessionHisPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisPeerDeviceId.setStatus("current")
_HpnicfDvpnMibNotification_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibNotification = _HpnicfDvpnMibNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 3)
)
_HpnicfDvpnNotification_ObjectIdentity = ObjectIdentity
hpnicfDvpnNotification = _HpnicfDvpnNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 3, 0)
)
_HpnicfDvpnMibConformance_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibConformance = _HpnicfDvpnMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4)
)
_HpnicfDvpnMibCompliances_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibCompliances = _HpnicfDvpnMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 1)
)
_HpnicfDvpnMibGroups_ObjectIdentity = ObjectIdentity
hpnicfDvpnMibGroups = _HpnicfDvpnMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2)
)

# Managed Objects groups

hpnicfDvpnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 1)
)
hpnicfDvpnGlobalGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnServiceEnable"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClassNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClientNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapAgeTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClientRegisterInterval"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClientRegisterDumb"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClientRegisterRetry"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnInputPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDropPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnOutputPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnOutputErrorPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnEncryptErrorPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnCurrentDeviceRole"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnServerPreSharedKey"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapTrapEnable"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionTrapEnable"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnVersion"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClearDomainAllConection"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClearDvpnStaInfo"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnTotalRedirectNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnGlobalAuthenClientType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnGlobalUserDefAAADomain"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnLocalDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisAgeTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisReset"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnGlobalGroup.setStatus("current")

hpnicfDvpnPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 2)
)
hpnicfDvpnPolicyGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoAuthenClientType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoSessionAlgorithmSuite"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoSessionIdleTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoSessionKeepTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoSessionSetupInterval"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoDataAlgorithmSuite"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoSaSeconds"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoUserDefAAADomain"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoRefTimes"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnPoRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnPolicyGroup.setStatus("current")

hpnicfDvpnDomainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 3)
)
hpnicfDvpnDomainInfoGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainSessionNum"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainRedirectNum"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainInputPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainDropPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainOutputPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainOutputErrorPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnDomainEncryptErrorPkt"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnDomainInfoGroup.setStatus("current")

hpnicfDvpnClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 4)
)
hpnicfDvpnClassGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnClServerPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClServerPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClServerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClServerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClAlgorithmSuite"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClAuthenServerType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClPreShareKey"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClUserName"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClPwdEncrypted"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClPasswd"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnClassRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnClassGroup.setStatus("current")

hpnicfDvpnTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 5)
)
hpnicfDvpnTunnelGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnTunnelInterfaceType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnTunnelAcl"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnTunnelClientRegType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnTunnelDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnTunnelPolicy"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnTunnelClass"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnTunnelGroup.setStatus("current")

hpnicfDvpnMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 6)
)
hpnicfDvpnMapGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapIndex"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapBuildTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapUserName"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapUdpPort"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapControlId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapState"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnMapGroup.setStatus("current")

hpnicfDvpnSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 7)
)
hpnicfDvpnSessionGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionBuildTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPubIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPubIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPubIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPubIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerUdpPort"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionInitiator"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionUserName"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionState"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerType"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionGroup.setStatus("current")

hpnicfDvpnSessionHisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 8)
)
hpnicfDvpnSessionHisGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisPeerPriIPType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisSendPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisRcvPkt"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisOnlineNumber"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisFirstUpTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisLastUpTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisLastDownTime"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisOnlineFlag"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionHisPeerDeviceId"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionHisGroup.setStatus("current")

hpnicfDvpnNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 2, 9)
)
hpnicfDvpnNotificationGroup.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionBuildNotification"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionDelNotification"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapBuildNotification"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapDelNotification"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnNotificationGroup.setStatus("current")


# Notification objects

hpnicfDvpnSessionBuildNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 3, 0, 1)
)
hpnicfDvpnSessionBuildNotification.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnLocalDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPubIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPubIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPubIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPubIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerUdpPort"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionUserName"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionBuildNotification.setStatus(
        "current"
    )

hpnicfDvpnSessionDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 3, 0, 2)
)
hpnicfDvpnSessionDelNotification.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnLocalDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPubIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionLocalPubIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPubIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerPubIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerUdpPort"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionPeerType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnSessionUserName"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnSessionDelNotification.setStatus(
        "current"
    )

hpnicfDvpnMapBuildNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 3, 0, 3)
)
hpnicfDvpnMapBuildNotification.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapIndex"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnLocalDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapUserName"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnMapBuildNotification.setStatus(
        "current"
    )

hpnicfDvpnMapDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 3, 0, 4)
)
hpnicfDvpnMapDelNotification.setObjects(
      *(("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapIndex"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapDvpnId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapPeerPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnLocalDeviceId"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPriIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPriIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPublicIpType"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapLocalPublicIp"),
        ("HPN-ICF-DVPN-MIB", "hpnicfDvpnMapUserName"))
)
if mibBuilder.loadTexts:
    hpnicfDvpnMapDelNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfDvpnMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDvpnMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DVPN-MIB",
    **{"DvpnAlgorithmSuite": DvpnAlgorithmSuite,
       "DvpnCommunicateType": DvpnCommunicateType,
       "hpnicfDvpn": hpnicfDvpn,
       "hpnicfDvpnMibObjects": hpnicfDvpnMibObjects,
       "hpnicfDvpnMibGlobal": hpnicfDvpnMibGlobal,
       "hpnicfDvpnServiceEnable": hpnicfDvpnServiceEnable,
       "hpnicfDvpnClassNumber": hpnicfDvpnClassNumber,
       "hpnicfDvpnClientNumber": hpnicfDvpnClientNumber,
       "hpnicfDvpnMapAgeTime": hpnicfDvpnMapAgeTime,
       "hpnicfDvpnClientRegisterInterval": hpnicfDvpnClientRegisterInterval,
       "hpnicfDvpnClientRegisterDumb": hpnicfDvpnClientRegisterDumb,
       "hpnicfDvpnClientRegisterRetry": hpnicfDvpnClientRegisterRetry,
       "hpnicfDvpnInputPkt": hpnicfDvpnInputPkt,
       "hpnicfDvpnDropPkt": hpnicfDvpnDropPkt,
       "hpnicfDvpnOutputPkt": hpnicfDvpnOutputPkt,
       "hpnicfDvpnOutputErrorPkt": hpnicfDvpnOutputErrorPkt,
       "hpnicfDvpnEncryptErrorPkt": hpnicfDvpnEncryptErrorPkt,
       "hpnicfDvpnCurrentDeviceRole": hpnicfDvpnCurrentDeviceRole,
       "hpnicfDvpnDomainNumber": hpnicfDvpnDomainNumber,
       "hpnicfDvpnMapNumber": hpnicfDvpnMapNumber,
       "hpnicfDvpnSessionNumber": hpnicfDvpnSessionNumber,
       "hpnicfDvpnServerPreSharedKey": hpnicfDvpnServerPreSharedKey,
       "hpnicfDvpnMapTrapEnable": hpnicfDvpnMapTrapEnable,
       "hpnicfDvpnSessionTrapEnable": hpnicfDvpnSessionTrapEnable,
       "hpnicfDvpnVersion": hpnicfDvpnVersion,
       "hpnicfDvpnClearDomainAllConection": hpnicfDvpnClearDomainAllConection,
       "hpnicfDvpnClearDvpnStaInfo": hpnicfDvpnClearDvpnStaInfo,
       "hpnicfDvpnTotalRedirectNumber": hpnicfDvpnTotalRedirectNumber,
       "hpnicfDvpnGlobalAuthenClientType": hpnicfDvpnGlobalAuthenClientType,
       "hpnicfDvpnGlobalUserDefAAADomain": hpnicfDvpnGlobalUserDefAAADomain,
       "hpnicfDvpnLocalDeviceId": hpnicfDvpnLocalDeviceId,
       "hpnicfDvpnSessionHisAgeTime": hpnicfDvpnSessionHisAgeTime,
       "hpnicfDvpnSessionHisReset": hpnicfDvpnSessionHisReset,
       "hpnicfDvpnMibTableTroop": hpnicfDvpnMibTableTroop,
       "hpnicfDvpnPolicyTable": hpnicfDvpnPolicyTable,
       "hpnicfDvpnPolicyEntry": hpnicfDvpnPolicyEntry,
       "hpnicfDvpnPolicyName": hpnicfDvpnPolicyName,
       "hpnicfDvpnPoAuthenClientType": hpnicfDvpnPoAuthenClientType,
       "hpnicfDvpnPoSessionAlgorithmSuite": hpnicfDvpnPoSessionAlgorithmSuite,
       "hpnicfDvpnPoSessionIdleTime": hpnicfDvpnPoSessionIdleTime,
       "hpnicfDvpnPoSessionKeepTime": hpnicfDvpnPoSessionKeepTime,
       "hpnicfDvpnPoSessionSetupInterval": hpnicfDvpnPoSessionSetupInterval,
       "hpnicfDvpnPoDataAlgorithmSuite": hpnicfDvpnPoDataAlgorithmSuite,
       "hpnicfDvpnPoSaSeconds": hpnicfDvpnPoSaSeconds,
       "hpnicfDvpnPoUserDefAAADomain": hpnicfDvpnPoUserDefAAADomain,
       "hpnicfDvpnPoRefTimes": hpnicfDvpnPoRefTimes,
       "hpnicfDvpnPoRowStatus": hpnicfDvpnPoRowStatus,
       "hpnicfDvpnDomainInfoTable": hpnicfDvpnDomainInfoTable,
       "hpnicfDvpnDomainInfoEntry": hpnicfDvpnDomainInfoEntry,
       "hpnicfDvpnDomainID": hpnicfDvpnDomainID,
       "hpnicfDvpnDomainSessionNum": hpnicfDvpnDomainSessionNum,
       "hpnicfDvpnDomainRedirectNum": hpnicfDvpnDomainRedirectNum,
       "hpnicfDvpnDomainInputPkt": hpnicfDvpnDomainInputPkt,
       "hpnicfDvpnDomainDropPkt": hpnicfDvpnDomainDropPkt,
       "hpnicfDvpnDomainOutputPkt": hpnicfDvpnDomainOutputPkt,
       "hpnicfDvpnDomainOutputErrorPkt": hpnicfDvpnDomainOutputErrorPkt,
       "hpnicfDvpnDomainEncryptErrorPkt": hpnicfDvpnDomainEncryptErrorPkt,
       "hpnicfDvpnClassTable": hpnicfDvpnClassTable,
       "hpnicfDvpnClassEntry": hpnicfDvpnClassEntry,
       "hpnicfDvpnClassName": hpnicfDvpnClassName,
       "hpnicfDvpnClServerPublicIpType": hpnicfDvpnClServerPublicIpType,
       "hpnicfDvpnClServerPublicIp": hpnicfDvpnClServerPublicIp,
       "hpnicfDvpnClServerPriIpType": hpnicfDvpnClServerPriIpType,
       "hpnicfDvpnClServerPriIp": hpnicfDvpnClServerPriIp,
       "hpnicfDvpnClAlgorithmSuite": hpnicfDvpnClAlgorithmSuite,
       "hpnicfDvpnClAuthenServerType": hpnicfDvpnClAuthenServerType,
       "hpnicfDvpnClPreShareKey": hpnicfDvpnClPreShareKey,
       "hpnicfDvpnClUserName": hpnicfDvpnClUserName,
       "hpnicfDvpnClPwdEncrypted": hpnicfDvpnClPwdEncrypted,
       "hpnicfDvpnClPasswd": hpnicfDvpnClPasswd,
       "hpnicfDvpnClassRowStatus": hpnicfDvpnClassRowStatus,
       "hpnicfDvpnTunnelTable": hpnicfDvpnTunnelTable,
       "hpnicfDvpnTunnelEntry": hpnicfDvpnTunnelEntry,
       "hpnicfDvpnTunnelInterfaceType": hpnicfDvpnTunnelInterfaceType,
       "hpnicfDvpnTunnelAcl": hpnicfDvpnTunnelAcl,
       "hpnicfDvpnTunnelClientRegType": hpnicfDvpnTunnelClientRegType,
       "hpnicfDvpnTunnelDvpnId": hpnicfDvpnTunnelDvpnId,
       "hpnicfDvpnTunnelPolicy": hpnicfDvpnTunnelPolicy,
       "hpnicfDvpnTunnelClass": hpnicfDvpnTunnelClass,
       "hpnicfDvpnMapTable": hpnicfDvpnMapTable,
       "hpnicfDvpnMapEntry": hpnicfDvpnMapEntry,
       "hpnicfDvpnMapIndex": hpnicfDvpnMapIndex,
       "hpnicfDvpnMapPeerDeviceId": hpnicfDvpnMapPeerDeviceId,
       "hpnicfDvpnMapDvpnId": hpnicfDvpnMapDvpnId,
       "hpnicfDvpnMapBuildTime": hpnicfDvpnMapBuildTime,
       "hpnicfDvpnMapPeerPriIpType": hpnicfDvpnMapPeerPriIpType,
       "hpnicfDvpnMapPeerPriIp": hpnicfDvpnMapPeerPriIp,
       "hpnicfDvpnMapPeerPublicIpType": hpnicfDvpnMapPeerPublicIpType,
       "hpnicfDvpnMapPeerPublicIp": hpnicfDvpnMapPeerPublicIp,
       "hpnicfDvpnMapLocalPriIpType": hpnicfDvpnMapLocalPriIpType,
       "hpnicfDvpnMapLocalPriIp": hpnicfDvpnMapLocalPriIp,
       "hpnicfDvpnMapLocalPublicIpType": hpnicfDvpnMapLocalPublicIpType,
       "hpnicfDvpnMapLocalPublicIp": hpnicfDvpnMapLocalPublicIp,
       "hpnicfDvpnMapUserName": hpnicfDvpnMapUserName,
       "hpnicfDvpnMapUdpPort": hpnicfDvpnMapUdpPort,
       "hpnicfDvpnMapControlId": hpnicfDvpnMapControlId,
       "hpnicfDvpnMapType": hpnicfDvpnMapType,
       "hpnicfDvpnMapState": hpnicfDvpnMapState,
       "hpnicfDvpnSessionTable": hpnicfDvpnSessionTable,
       "hpnicfDvpnSessionEntry": hpnicfDvpnSessionEntry,
       "hpnicfDvpnSessionDvpnId": hpnicfDvpnSessionDvpnId,
       "hpnicfDvpnSessionPeerPriIpType": hpnicfDvpnSessionPeerPriIpType,
       "hpnicfDvpnSessionPeerPriIp": hpnicfDvpnSessionPeerPriIp,
       "hpnicfDvpnSessionPeerDeviceId": hpnicfDvpnSessionPeerDeviceId,
       "hpnicfDvpnSessionBuildTime": hpnicfDvpnSessionBuildTime,
       "hpnicfDvpnSessionPeerPubIpType": hpnicfDvpnSessionPeerPubIpType,
       "hpnicfDvpnSessionPeerPubIp": hpnicfDvpnSessionPeerPubIp,
       "hpnicfDvpnSessionLocalPubIpType": hpnicfDvpnSessionLocalPubIpType,
       "hpnicfDvpnSessionLocalPubIp": hpnicfDvpnSessionLocalPubIp,
       "hpnicfDvpnSessionLocalPriIpType": hpnicfDvpnSessionLocalPriIpType,
       "hpnicfDvpnSessionLocalPriIp": hpnicfDvpnSessionLocalPriIp,
       "hpnicfDvpnSessionPeerUdpPort": hpnicfDvpnSessionPeerUdpPort,
       "hpnicfDvpnSessionInitiator": hpnicfDvpnSessionInitiator,
       "hpnicfDvpnSessionUserName": hpnicfDvpnSessionUserName,
       "hpnicfDvpnSessionState": hpnicfDvpnSessionState,
       "hpnicfDvpnSessionType": hpnicfDvpnSessionType,
       "hpnicfDvpnSessionPeerType": hpnicfDvpnSessionPeerType,
       "hpnicfDvpnSessionHisTable": hpnicfDvpnSessionHisTable,
       "hpnicfDvpnSessionHisEntry": hpnicfDvpnSessionHisEntry,
       "hpnicfDvpnSessionHisDvpnID": hpnicfDvpnSessionHisDvpnID,
       "hpnicfDvpnSessionHisPeerPriIPType": hpnicfDvpnSessionHisPeerPriIPType,
       "hpnicfDvpnSessionHisPeerPriIP": hpnicfDvpnSessionHisPeerPriIP,
       "hpnicfDvpnSessionHisSendPkt": hpnicfDvpnSessionHisSendPkt,
       "hpnicfDvpnSessionHisRcvPkt": hpnicfDvpnSessionHisRcvPkt,
       "hpnicfDvpnSessionHisOnlineNumber": hpnicfDvpnSessionHisOnlineNumber,
       "hpnicfDvpnSessionHisFirstUpTime": hpnicfDvpnSessionHisFirstUpTime,
       "hpnicfDvpnSessionHisLastUpTime": hpnicfDvpnSessionHisLastUpTime,
       "hpnicfDvpnSessionHisLastDownTime": hpnicfDvpnSessionHisLastDownTime,
       "hpnicfDvpnSessionHisOnlineFlag": hpnicfDvpnSessionHisOnlineFlag,
       "hpnicfDvpnSessionHisPeerDeviceId": hpnicfDvpnSessionHisPeerDeviceId,
       "hpnicfDvpnMibNotification": hpnicfDvpnMibNotification,
       "hpnicfDvpnNotification": hpnicfDvpnNotification,
       "hpnicfDvpnSessionBuildNotification": hpnicfDvpnSessionBuildNotification,
       "hpnicfDvpnSessionDelNotification": hpnicfDvpnSessionDelNotification,
       "hpnicfDvpnMapBuildNotification": hpnicfDvpnMapBuildNotification,
       "hpnicfDvpnMapDelNotification": hpnicfDvpnMapDelNotification,
       "hpnicfDvpnMibConformance": hpnicfDvpnMibConformance,
       "hpnicfDvpnMibCompliances": hpnicfDvpnMibCompliances,
       "hpnicfDvpnMibCompliance": hpnicfDvpnMibCompliance,
       "hpnicfDvpnMibGroups": hpnicfDvpnMibGroups,
       "hpnicfDvpnGlobalGroup": hpnicfDvpnGlobalGroup,
       "hpnicfDvpnPolicyGroup": hpnicfDvpnPolicyGroup,
       "hpnicfDvpnDomainInfoGroup": hpnicfDvpnDomainInfoGroup,
       "hpnicfDvpnClassGroup": hpnicfDvpnClassGroup,
       "hpnicfDvpnTunnelGroup": hpnicfDvpnTunnelGroup,
       "hpnicfDvpnMapGroup": hpnicfDvpnMapGroup,
       "hpnicfDvpnSessionGroup": hpnicfDvpnSessionGroup,
       "hpnicfDvpnSessionHisGroup": hpnicfDvpnSessionHisGroup,
       "hpnicfDvpnNotificationGroup": hpnicfDvpnNotificationGroup}
)
