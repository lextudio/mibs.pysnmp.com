# SNMP MIB module (HM2-DEVMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-DEVMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:52 2024
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

(HmEnabledStatus,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2DeviceMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10)
)
hm2DeviceMgmtMib.setRevisions(
        ("2012-10-10 00:00",
         "2011-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2DeviceExtNVMType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sd", 1),
          ("serial", 3),
          ("usb", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2DeviceMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtMibNotifications = _Hm2DeviceMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 0)
)
_Hm2DeviceMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtMibObjects = _Hm2DeviceMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1)
)
_Hm2DeviceMgmtGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtGroup = _Hm2DeviceMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 1)
)
_Hm2DevMgmtProductId_Type = ObjectIdentifier
_Hm2DevMgmtProductId_Object = MibScalar
hm2DevMgmtProductId = _Hm2DevMgmtProductId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 1, 1),
    _Hm2DevMgmtProductId_Type()
)
hm2DevMgmtProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtProductId.setStatus("current")
_Hm2DevMgmtProductDescr_Type = DisplayString
_Hm2DevMgmtProductDescr_Object = MibScalar
hm2DevMgmtProductDescr = _Hm2DevMgmtProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 1, 2),
    _Hm2DevMgmtProductDescr_Type()
)
hm2DevMgmtProductDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtProductDescr.setStatus("current")
_Hm2DevMgmtSerialNumber_Type = DisplayString
_Hm2DevMgmtSerialNumber_Object = MibScalar
hm2DevMgmtSerialNumber = _Hm2DevMgmtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 1, 3),
    _Hm2DevMgmtSerialNumber_Type()
)
hm2DevMgmtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSerialNumber.setStatus("current")
_Hm2DeviceMgmtActionGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtActionGroup = _Hm2DeviceMgmtActionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2)
)


class _Hm2DevMgmtActionReset_Type(Integer32):
    """Custom type hm2DevMgmtActionReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_Hm2DevMgmtActionReset_Type.__name__ = "Integer32"
_Hm2DevMgmtActionReset_Object = MibScalar
hm2DevMgmtActionReset = _Hm2DevMgmtActionReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 1),
    _Hm2DevMgmtActionReset_Type()
)
hm2DevMgmtActionReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionReset.setStatus("current")


class _Hm2DevMgmtActionFlushFDB_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushFDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushFDB", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushFDB_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushFDB_Object = MibScalar
hm2DevMgmtActionFlushFDB = _Hm2DevMgmtActionFlushFDB_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 2),
    _Hm2DevMgmtActionFlushFDB_Type()
)
hm2DevMgmtActionFlushFDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushFDB.setStatus("current")


class _Hm2DevMgmtActionFlushARP_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushARP", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushARP_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushARP_Object = MibScalar
hm2DevMgmtActionFlushARP = _Hm2DevMgmtActionFlushARP_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 3),
    _Hm2DevMgmtActionFlushARP_Type()
)
hm2DevMgmtActionFlushARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushARP.setStatus("current")


class _Hm2DevMgmtActionFlushIGS_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushIGS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushIGS", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushIGS_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushIGS_Object = MibScalar
hm2DevMgmtActionFlushIGS = _Hm2DevMgmtActionFlushIGS_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 4),
    _Hm2DevMgmtActionFlushIGS_Type()
)
hm2DevMgmtActionFlushIGS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushIGS.setStatus("current")


class _Hm2DevMgmtActionFlushPortStats_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushPortStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushPortStats", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushPortStats_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushPortStats_Object = MibScalar
hm2DevMgmtActionFlushPortStats = _Hm2DevMgmtActionFlushPortStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 5),
    _Hm2DevMgmtActionFlushPortStats_Type()
)
hm2DevMgmtActionFlushPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushPortStats.setStatus("current")


class _Hm2DevMgmtActionFlushEmailLogStats_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushEmailLogStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushEmailLogCounters", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushEmailLogStats_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushEmailLogStats_Object = MibScalar
hm2DevMgmtActionFlushEmailLogStats = _Hm2DevMgmtActionFlushEmailLogStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 6),
    _Hm2DevMgmtActionFlushEmailLogStats_Type()
)
hm2DevMgmtActionFlushEmailLogStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushEmailLogStats.setStatus("current")


class _Hm2DevMgmtActionFlushMMRP_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushMMRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushMMRP", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushMMRP_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushMMRP_Object = MibScalar
hm2DevMgmtActionFlushMMRP = _Hm2DevMgmtActionFlushMMRP_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 7),
    _Hm2DevMgmtActionFlushMMRP_Type()
)
hm2DevMgmtActionFlushMMRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushMMRP.setStatus("current")


class _Hm2DevMgmtActionFlushMVRP_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushMVRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushMVRP", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushMVRP_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushMVRP_Object = MibScalar
hm2DevMgmtActionFlushMVRP = _Hm2DevMgmtActionFlushMVRP_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 8),
    _Hm2DevMgmtActionFlushMVRP_Type()
)
hm2DevMgmtActionFlushMVRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushMVRP.setStatus("current")


class _Hm2DevMgmtActionFlushMSRP_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushMSRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushMSRP", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushMSRP_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushMSRP_Object = MibScalar
hm2DevMgmtActionFlushMSRP = _Hm2DevMgmtActionFlushMSRP_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 9),
    _Hm2DevMgmtActionFlushMSRP_Type()
)
hm2DevMgmtActionFlushMSRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushMSRP.setStatus("current")


class _Hm2DevMgmtActionFlushIeee8021AS_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushIeee8021AS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushIeee8021AS", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushIeee8021AS_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushIeee8021AS_Object = MibScalar
hm2DevMgmtActionFlushIeee8021AS = _Hm2DevMgmtActionFlushIeee8021AS_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 10),
    _Hm2DevMgmtActionFlushIeee8021AS_Type()
)
hm2DevMgmtActionFlushIeee8021AS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushIeee8021AS.setStatus("current")


class _Hm2DevMgmtActionFlushDnsClientCache_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushDnsClientCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushDnsClientCache", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushDnsClientCache_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushDnsClientCache_Object = MibScalar
hm2DevMgmtActionFlushDnsClientCache = _Hm2DevMgmtActionFlushDnsClientCache_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 11),
    _Hm2DevMgmtActionFlushDnsClientCache_Type()
)
hm2DevMgmtActionFlushDnsClientCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushDnsClientCache.setStatus("current")


class _Hm2DevMgmtActionFlushDnsCachingServerCache_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushDnsCachingServerCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushDnsCachingServerCache", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushDnsCachingServerCache_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushDnsCachingServerCache_Object = MibScalar
hm2DevMgmtActionFlushDnsCachingServerCache = _Hm2DevMgmtActionFlushDnsCachingServerCache_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 12),
    _Hm2DevMgmtActionFlushDnsCachingServerCache_Type()
)
hm2DevMgmtActionFlushDnsCachingServerCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushDnsCachingServerCache.setStatus("current")


class _Hm2DevMgmtActionFlushIpUdpHelperStats_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushIpUdpHelperStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushIpUdpHelperStats", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushIpUdpHelperStats_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushIpUdpHelperStats_Object = MibScalar
hm2DevMgmtActionFlushIpUdpHelperStats = _Hm2DevMgmtActionFlushIpUdpHelperStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 13),
    _Hm2DevMgmtActionFlushIpUdpHelperStats_Type()
)
hm2DevMgmtActionFlushIpUdpHelperStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushIpUdpHelperStats.setStatus("current")


class _Hm2DevMgmtActionFlushAclStats_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushAclStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flushAclMacStats", 3),
          ("flushAclStats", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushAclStats_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushAclStats_Object = MibScalar
hm2DevMgmtActionFlushAclStats = _Hm2DevMgmtActionFlushAclStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 14),
    _Hm2DevMgmtActionFlushAclStats_Type()
)
hm2DevMgmtActionFlushAclStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushAclStats.setStatus("current")


class _Hm2DevMgmtActionFlushLdapUserCache_Type(Integer32):
    """Custom type hm2DevMgmtActionFlushLdapUserCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushLdapUserCache", 2),
          ("other", 1))
    )


_Hm2DevMgmtActionFlushLdapUserCache_Type.__name__ = "Integer32"
_Hm2DevMgmtActionFlushLdapUserCache_Object = MibScalar
hm2DevMgmtActionFlushLdapUserCache = _Hm2DevMgmtActionFlushLdapUserCache_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 15),
    _Hm2DevMgmtActionFlushLdapUserCache_Type()
)
hm2DevMgmtActionFlushLdapUserCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionFlushLdapUserCache.setStatus("current")


class _Hm2DevMgmtActionDelayPreset_Type(Integer32):
    """Custom type hm2DevMgmtActionDelayPreset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483),
    )


_Hm2DevMgmtActionDelayPreset_Type.__name__ = "Integer32"
_Hm2DevMgmtActionDelayPreset_Object = MibScalar
hm2DevMgmtActionDelayPreset = _Hm2DevMgmtActionDelayPreset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 100),
    _Hm2DevMgmtActionDelayPreset_Type()
)
hm2DevMgmtActionDelayPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtActionDelayPreset.setStatus("current")


class _Hm2DevMgmtActionDelayCurrent_Type(Integer32):
    """Custom type hm2DevMgmtActionDelayCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483),
    )


_Hm2DevMgmtActionDelayCurrent_Type.__name__ = "Integer32"
_Hm2DevMgmtActionDelayCurrent_Object = MibScalar
hm2DevMgmtActionDelayCurrent = _Hm2DevMgmtActionDelayCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 2, 101),
    _Hm2DevMgmtActionDelayCurrent_Type()
)
hm2DevMgmtActionDelayCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtActionDelayCurrent.setStatus("current")
_Hm2DeviceMgmtSoftwareGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtSoftwareGroup = _Hm2DeviceMgmtSoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3)
)
_Hm2DeviceMgmtSoftwareVersionGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtSoftwareVersionGroup = _Hm2DeviceMgmtSoftwareVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1)
)
_Hm2DevMgmtSwVersBootcode_Type = DisplayString
_Hm2DevMgmtSwVersBootcode_Object = MibScalar
hm2DevMgmtSwVersBootcode = _Hm2DevMgmtSwVersBootcode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 1),
    _Hm2DevMgmtSwVersBootcode_Type()
)
hm2DevMgmtSwVersBootcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwVersBootcode.setStatus("current")
_Hm2DevMgmtSwVersTable_Object = MibTable
hm2DevMgmtSwVersTable = _Hm2DevMgmtSwVersTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hm2DevMgmtSwVersTable.setStatus("current")
_Hm2DevMgmtSwVersEntry_Object = MibTableRow
hm2DevMgmtSwVersEntry = _Hm2DevMgmtSwVersEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1)
)
hm2DevMgmtSwVersEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2DevMgmtSwFileLocation"),
    (0, "HM2-DEVMGMT-MIB", "hm2DevMgmtSwFileType"),
    (0, "HM2-DEVMGMT-MIB", "hm2DevMgmtSwFileIdx"),
)
if mibBuilder.loadTexts:
    hm2DevMgmtSwVersEntry.setStatus("current")


class _Hm2DevMgmtSwFileLocation_Type(Integer32):
    """Custom type hm2DevMgmtSwFileLocation based on Integer32"""
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
        *(("flash", 2),
          ("ram", 1),
          ("sd-card", 3),
          ("usb", 4))
    )


_Hm2DevMgmtSwFileLocation_Type.__name__ = "Integer32"
_Hm2DevMgmtSwFileLocation_Object = MibTableColumn
hm2DevMgmtSwFileLocation = _Hm2DevMgmtSwFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 1),
    _Hm2DevMgmtSwFileLocation_Type()
)
hm2DevMgmtSwFileLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DevMgmtSwFileLocation.setStatus("current")


class _Hm2DevMgmtSwFileType_Type(Integer32):
    """Custom type hm2DevMgmtSwFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applet", 2),
          ("firmware", 1),
          ("logic", 3))
    )


_Hm2DevMgmtSwFileType_Type.__name__ = "Integer32"
_Hm2DevMgmtSwFileType_Object = MibTableColumn
hm2DevMgmtSwFileType = _Hm2DevMgmtSwFileType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 2),
    _Hm2DevMgmtSwFileType_Type()
)
hm2DevMgmtSwFileType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DevMgmtSwFileType.setStatus("current")


class _Hm2DevMgmtSwFileIdx_Type(Integer32):
    """Custom type hm2DevMgmtSwFileIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Hm2DevMgmtSwFileIdx_Type.__name__ = "Integer32"
_Hm2DevMgmtSwFileIdx_Object = MibTableColumn
hm2DevMgmtSwFileIdx = _Hm2DevMgmtSwFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 3),
    _Hm2DevMgmtSwFileIdx_Type()
)
hm2DevMgmtSwFileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DevMgmtSwFileIdx.setStatus("current")
_Hm2DevMgmtSwFileName_Type = DisplayString
_Hm2DevMgmtSwFileName_Object = MibTableColumn
hm2DevMgmtSwFileName = _Hm2DevMgmtSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 4),
    _Hm2DevMgmtSwFileName_Type()
)
hm2DevMgmtSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwFileName.setStatus("current")
_Hm2DevMgmtSwVersion_Type = DisplayString
_Hm2DevMgmtSwVersion_Object = MibTableColumn
hm2DevMgmtSwVersion = _Hm2DevMgmtSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 5),
    _Hm2DevMgmtSwVersion_Type()
)
hm2DevMgmtSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwVersion.setStatus("current")
_Hm2DevMgmtSwMajorRelNum_Type = Integer32
_Hm2DevMgmtSwMajorRelNum_Object = MibTableColumn
hm2DevMgmtSwMajorRelNum = _Hm2DevMgmtSwMajorRelNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 6),
    _Hm2DevMgmtSwMajorRelNum_Type()
)
hm2DevMgmtSwMajorRelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwMajorRelNum.setStatus("current")
_Hm2DevMgmtSwMinorRelNum_Type = Integer32
_Hm2DevMgmtSwMinorRelNum_Object = MibTableColumn
hm2DevMgmtSwMinorRelNum = _Hm2DevMgmtSwMinorRelNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 7),
    _Hm2DevMgmtSwMinorRelNum_Type()
)
hm2DevMgmtSwMinorRelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwMinorRelNum.setStatus("current")
_Hm2DevMgmtSwBugfixRelNum_Type = Integer32
_Hm2DevMgmtSwBugfixRelNum_Object = MibTableColumn
hm2DevMgmtSwBugfixRelNum = _Hm2DevMgmtSwBugfixRelNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 3, 1, 10, 1, 8),
    _Hm2DevMgmtSwBugfixRelNum_Type()
)
hm2DevMgmtSwBugfixRelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwBugfixRelNum.setStatus("current")
_Hm2DeviceMgmtHardwareGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtHardwareGroup = _Hm2DeviceMgmtHardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4)
)
_Hm2DevMgmtHwVersion_Type = DisplayString
_Hm2DevMgmtHwVersion_Object = MibScalar
hm2DevMgmtHwVersion = _Hm2DevMgmtHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 1),
    _Hm2DevMgmtHwVersion_Type()
)
hm2DevMgmtHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtHwVersion.setStatus("current")
_Hm2DevMgmtSwitchingCoreVersion_Type = DisplayString
_Hm2DevMgmtSwitchingCoreVersion_Object = MibScalar
hm2DevMgmtSwitchingCoreVersion = _Hm2DevMgmtSwitchingCoreVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 2),
    _Hm2DevMgmtSwitchingCoreVersion_Type()
)
hm2DevMgmtSwitchingCoreVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtSwitchingCoreVersion.setStatus("current")
_Hm2DeviceMgmtLogicVersionGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtLogicVersionGroup = _Hm2DeviceMgmtLogicVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 5)
)
_Hm2DevMgmtLogicVersTable_Object = MibTable
hm2DevMgmtLogicVersTable = _Hm2DevMgmtLogicVersTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hm2DevMgmtLogicVersTable.setStatus("current")
_Hm2DevMgmtLogicVersEntry_Object = MibTableRow
hm2DevMgmtLogicVersEntry = _Hm2DevMgmtLogicVersEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 5, 1, 1)
)
hm2DevMgmtLogicVersEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2DevMgmtLogicIdx"),
)
if mibBuilder.loadTexts:
    hm2DevMgmtLogicVersEntry.setStatus("current")


class _Hm2DevMgmtLogicIdx_Type(Integer32):
    """Custom type hm2DevMgmtLogicIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hm2DevMgmtLogicIdx_Type.__name__ = "Integer32"
_Hm2DevMgmtLogicIdx_Object = MibTableColumn
hm2DevMgmtLogicIdx = _Hm2DevMgmtLogicIdx_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 5, 1, 1, 1),
    _Hm2DevMgmtLogicIdx_Type()
)
hm2DevMgmtLogicIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DevMgmtLogicIdx.setStatus("current")
_Hm2DevMgmtLogicAddress_Type = DisplayString
_Hm2DevMgmtLogicAddress_Object = MibTableColumn
hm2DevMgmtLogicAddress = _Hm2DevMgmtLogicAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 5, 1, 1, 2),
    _Hm2DevMgmtLogicAddress_Type()
)
hm2DevMgmtLogicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtLogicAddress.setStatus("current")
_Hm2DevMgmtLogicVersion_Type = DisplayString
_Hm2DevMgmtLogicVersion_Object = MibTableColumn
hm2DevMgmtLogicVersion = _Hm2DevMgmtLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 4, 5, 1, 1, 3),
    _Hm2DevMgmtLogicVersion_Type()
)
hm2DevMgmtLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtLogicVersion.setStatus("current")
_Hm2DeviceMgmtTemperatureGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMgmtTemperatureGroup = _Hm2DeviceMgmtTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 5)
)
_Hm2DevMgmtTemperature_Type = Integer32
_Hm2DevMgmtTemperature_Object = MibScalar
hm2DevMgmtTemperature = _Hm2DevMgmtTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 5, 1),
    _Hm2DevMgmtTemperature_Type()
)
hm2DevMgmtTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMgmtTemperature.setStatus("current")


class _Hm2DevMgmtTemperatureUpperLimit_Type(Integer32):
    """Custom type hm2DevMgmtTemperatureUpperLimit based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_Hm2DevMgmtTemperatureUpperLimit_Type.__name__ = "Integer32"
_Hm2DevMgmtTemperatureUpperLimit_Object = MibScalar
hm2DevMgmtTemperatureUpperLimit = _Hm2DevMgmtTemperatureUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 5, 2),
    _Hm2DevMgmtTemperatureUpperLimit_Type()
)
hm2DevMgmtTemperatureUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtTemperatureUpperLimit.setStatus("current")


class _Hm2DevMgmtTemperatureLowerLimit_Type(Integer32):
    """Custom type hm2DevMgmtTemperatureLowerLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_Hm2DevMgmtTemperatureLowerLimit_Type.__name__ = "Integer32"
_Hm2DevMgmtTemperatureLowerLimit_Object = MibScalar
hm2DevMgmtTemperatureLowerLimit = _Hm2DevMgmtTemperatureLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 5, 3),
    _Hm2DevMgmtTemperatureLowerLimit_Type()
)
hm2DevMgmtTemperatureLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMgmtTemperatureLowerLimit.setStatus("current")
_Hm2IfaceGroup_ObjectIdentity = ObjectIdentity
hm2IfaceGroup = _Hm2IfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6)
)
_Hm2IfaceTable_Object = MibTable
hm2IfaceTable = _Hm2IfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hm2IfaceTable.setStatus("current")
_Hm2IfaceEntry_Object = MibTableRow
hm2IfaceEntry = _Hm2IfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1)
)
hm2IfaceEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"),
)
if mibBuilder.loadTexts:
    hm2IfaceEntry.setStatus("current")
_Hm2IfacePhysIndex_Type = Integer32
_Hm2IfacePhysIndex_Object = MibTableColumn
hm2IfacePhysIndex = _Hm2IfacePhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1, 1),
    _Hm2IfacePhysIndex_Type()
)
hm2IfacePhysIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2IfacePhysIndex.setStatus("current")


class _Hm2IfacePortCapabilityBits_Type(Bits):
    """Custom type hm2IfacePortCapabilityBits based on Bits"""
    namedValues = NamedValues(
        *(("auto-mdix", 1),
          ("auto-power-down", 2),
          ("cable-test", 4),
          ("energy-efficient-ethernet", 3),
          ("manual-mdix", 0))
    )

_Hm2IfacePortCapabilityBits_Type.__name__ = "Bits"
_Hm2IfacePortCapabilityBits_Object = MibTableColumn
hm2IfacePortCapabilityBits = _Hm2IfacePortCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1, 2),
    _Hm2IfacePortCapabilityBits_Type()
)
hm2IfacePortCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfacePortCapabilityBits.setStatus("current")


class _Hm2IfaceCableCrossing_Type(Integer32):
    """Custom type hm2IfaceCableCrossing based on Integer32"""
    defaultValue = 2

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
        *(("auto-mdix", 3),
          ("mdi", 1),
          ("mdix", 2),
          ("unsupported", 4))
    )


_Hm2IfaceCableCrossing_Type.__name__ = "Integer32"
_Hm2IfaceCableCrossing_Object = MibTableColumn
hm2IfaceCableCrossing = _Hm2IfaceCableCrossing_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1, 3),
    _Hm2IfaceCableCrossing_Type()
)
hm2IfaceCableCrossing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IfaceCableCrossing.setStatus("current")


class _Hm2IfacePowerState_Type(HmEnabledStatus):
    """Custom type hm2IfacePowerState based on HmEnabledStatus"""


_Hm2IfacePowerState_Object = MibTableColumn
hm2IfacePowerState = _Hm2IfacePowerState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1, 4),
    _Hm2IfacePowerState_Type()
)
hm2IfacePowerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IfacePowerState.setStatus("current")


class _Hm2IfaceAutoPowerDown_Type(Integer32):
    """Custom type hm2IfaceAutoPowerDown based on Integer32"""
    defaultValue = 2

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
        *(("auto-power-down", 1),
          ("energy-efficient-ethernet", 3),
          ("no-power-save", 2),
          ("unsupported", 4))
    )


_Hm2IfaceAutoPowerDown_Type.__name__ = "Integer32"
_Hm2IfaceAutoPowerDown_Object = MibTableColumn
hm2IfaceAutoPowerDown = _Hm2IfaceAutoPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1, 5),
    _Hm2IfaceAutoPowerDown_Type()
)
hm2IfaceAutoPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IfaceAutoPowerDown.setStatus("current")


class _Hm2IfaceOperAdminStatus_Type(Integer32):
    """Custom type hm2IfaceOperAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Hm2IfaceOperAdminStatus_Type.__name__ = "Integer32"
_Hm2IfaceOperAdminStatus_Object = MibTableColumn
hm2IfaceOperAdminStatus = _Hm2IfaceOperAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 1, 1, 6),
    _Hm2IfaceOperAdminStatus_Type()
)
hm2IfaceOperAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceOperAdminStatus.setStatus("current")
_Hm2IfaceLayoutTable_Object = MibTable
hm2IfaceLayoutTable = _Hm2IfaceLayoutTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hm2IfaceLayoutTable.setStatus("current")
_Hm2IfaceLayoutEntry_Object = MibTableRow
hm2IfaceLayoutEntry = _Hm2IfaceLayoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1)
)
hm2IfaceLayoutEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2IfaceLayoutIndex"),
)
if mibBuilder.loadTexts:
    hm2IfaceLayoutEntry.setStatus("current")
_Hm2IfaceLayoutIndex_Type = Integer32
_Hm2IfaceLayoutIndex_Object = MibTableColumn
hm2IfaceLayoutIndex = _Hm2IfaceLayoutIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 1),
    _Hm2IfaceLayoutIndex_Type()
)
hm2IfaceLayoutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IfaceLayoutIndex.setStatus("current")
_Hm2IfaceLayoutStartIfIndex_Type = InterfaceIndexOrZero
_Hm2IfaceLayoutStartIfIndex_Object = MibTableColumn
hm2IfaceLayoutStartIfIndex = _Hm2IfaceLayoutStartIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 2),
    _Hm2IfaceLayoutStartIfIndex_Type()
)
hm2IfaceLayoutStartIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceLayoutStartIfIndex.setStatus("current")
_Hm2IfaceLayoutEndIfIndex_Type = InterfaceIndexOrZero
_Hm2IfaceLayoutEndIfIndex_Object = MibTableColumn
hm2IfaceLayoutEndIfIndex = _Hm2IfaceLayoutEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 3),
    _Hm2IfaceLayoutEndIfIndex_Type()
)
hm2IfaceLayoutEndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceLayoutEndIfIndex.setStatus("current")
_Hm2IfaceLayoutModuleCapacity_Type = Unsigned32
_Hm2IfaceLayoutModuleCapacity_Object = MibTableColumn
hm2IfaceLayoutModuleCapacity = _Hm2IfaceLayoutModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 4),
    _Hm2IfaceLayoutModuleCapacity_Type()
)
hm2IfaceLayoutModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceLayoutModuleCapacity.setStatus("current")
_Hm2IfaceLayoutModulePortCapacity_Type = Unsigned32
_Hm2IfaceLayoutModulePortCapacity_Object = MibTableColumn
hm2IfaceLayoutModulePortCapacity = _Hm2IfaceLayoutModulePortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 5),
    _Hm2IfaceLayoutModulePortCapacity_Type()
)
hm2IfaceLayoutModulePortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceLayoutModulePortCapacity.setStatus("current")
_Hm2IfaceLayoutFormat_Type = SnmpAdminString
_Hm2IfaceLayoutFormat_Object = MibTableColumn
hm2IfaceLayoutFormat = _Hm2IfaceLayoutFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 6),
    _Hm2IfaceLayoutFormat_Type()
)
hm2IfaceLayoutFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceLayoutFormat.setStatus("current")
_Hm2IfaceLayoutIfIndexType_Type = IANAifType
_Hm2IfaceLayoutIfIndexType_Object = MibTableColumn
hm2IfaceLayoutIfIndexType = _Hm2IfaceLayoutIfIndexType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 2, 1, 7),
    _Hm2IfaceLayoutIfIndexType_Type()
)
hm2IfaceLayoutIfIndexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceLayoutIfIndexType.setStatus("current")
_Hm2IfaceExtTable_Object = MibTable
hm2IfaceExtTable = _Hm2IfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hm2IfaceExtTable.setStatus("current")
_Hm2IfaceExtEntry_Object = MibTableRow
hm2IfaceExtEntry = _Hm2IfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 3, 1)
)
hm2IfaceExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2IfaceExtEntry.setStatus("current")


class _Hm2IfaceExtIfRole_Type(Integer32):
    """Custom type hm2IfaceExtIfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              24,
              136,
              161,
              169,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1101,
              1102,
              1201,
              1202)
        )
    )
    namedValues = NamedValues(
        *(("couplingPort", 1003),
          ("cpuPort", 1006),
          ("ethernetCsmacd", 6),
          ("ieee8023adLag", 161),
          ("l3ipvlan", 136),
          ("lagMember", 1101),
          ("lreInterface", 1201),
          ("lreMember", 1102),
          ("outOfBandMgmtPort", 1008),
          ("probePort", 1005),
          ("ringLagInterface", 1202),
          ("ringPort", 1001),
          ("routerPort", 1004),
          ("servicePort", 1007),
          ("shdsl", 169),
          ("softwareLoopback", 24),
          ("subringPort", 1002))
    )


_Hm2IfaceExtIfRole_Type.__name__ = "Integer32"
_Hm2IfaceExtIfRole_Object = MibTableColumn
hm2IfaceExtIfRole = _Hm2IfaceExtIfRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 6, 3, 1, 1),
    _Hm2IfaceExtIfRole_Type()
)
hm2IfaceExtIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IfaceExtIfRole.setStatus("current")
_Hm2SfpGroup_ObjectIdentity = ObjectIdentity
hm2SfpGroup = _Hm2SfpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7)
)
_Hm2SfpInfoTable_Object = MibTable
hm2SfpInfoTable = _Hm2SfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hm2SfpInfoTable.setStatus("current")
_Hm2SfpInfoEntry_Object = MibTableRow
hm2SfpInfoEntry = _Hm2SfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1)
)
hm2SfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2SfpInfoEntry.setStatus("current")


class _Hm2SfpModuleType_Type(Integer32):
    """Custom type hm2SfpModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 3),
          ("xfp", 6))
    )


_Hm2SfpModuleType_Type.__name__ = "Integer32"
_Hm2SfpModuleType_Object = MibTableColumn
hm2SfpModuleType = _Hm2SfpModuleType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 1),
    _Hm2SfpModuleType_Type()
)
hm2SfpModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpModuleType.setStatus("current")


class _Hm2SfpMediaType_Type(Integer32):
    """Custom type hm2SfpMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              30,
              31,
              32,
              40,
              41,
              50)
        )
    )
    namedValues = NamedValues(
        *(("fe-100base-fx", 6),
          ("fe-100base-lx", 5),
          ("ge-1000-base-cx", 4),
          ("ge-1000-base-lx", 2),
          ("ge-1000-base-sx", 1),
          ("ge-1000-base-t", 8),
          ("m-sfp-2500", 50),
          ("microfx", 40),
          ("oc12-mm-sr", 13),
          ("oc12-sm-ir", 14),
          ("oc12-sm-lr", 15),
          ("oc3-mm-sr", 10),
          ("oc3-sm-ir", 11),
          ("oc3-sm-lr", 12),
          ("oc48-ir", 17),
          ("oc48-lr", 18),
          ("oc48-sr", 16),
          ("pof", 41),
          ("unsupported", 9),
          ("xfp-10gbase-er", 32),
          ("xfp-10gbase-lr", 31),
          ("xfp-10gbase-sr", 30))
    )


_Hm2SfpMediaType_Type.__name__ = "Integer32"
_Hm2SfpMediaType_Object = MibTableColumn
hm2SfpMediaType = _Hm2SfpMediaType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 2),
    _Hm2SfpMediaType_Type()
)
hm2SfpMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpMediaType.setStatus("current")


class _Hm2SfpConnector_Type(Integer32):
    """Custom type hm2SfpConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              11,
              33,
              34,
              128)
        )
    )
    namedValues = NamedValues(
        *(("copperPigtail", 33),
          ("fiberjack", 6),
          ("lc", 7),
          ("mtrj", 8),
          ("nonSfp", 1),
          ("opticalPigtail", 11),
          ("rj45", 34),
          ("vendorSpecific", 128))
    )


_Hm2SfpConnector_Type.__name__ = "Integer32"
_Hm2SfpConnector_Object = MibTableColumn
hm2SfpConnector = _Hm2SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 3),
    _Hm2SfpConnector_Type()
)
hm2SfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpConnector.setStatus("current")
_Hm2SfpVendorName_Type = SnmpAdminString
_Hm2SfpVendorName_Object = MibTableColumn
hm2SfpVendorName = _Hm2SfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 4),
    _Hm2SfpVendorName_Type()
)
hm2SfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpVendorName.setStatus("current")
_Hm2SfpVendorOUI_Type = OctetString
_Hm2SfpVendorOUI_Object = MibTableColumn
hm2SfpVendorOUI = _Hm2SfpVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 5),
    _Hm2SfpVendorOUI_Type()
)
hm2SfpVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpVendorOUI.setStatus("current")
_Hm2SfpPartNumber_Type = SnmpAdminString
_Hm2SfpPartNumber_Object = MibTableColumn
hm2SfpPartNumber = _Hm2SfpPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 6),
    _Hm2SfpPartNumber_Type()
)
hm2SfpPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpPartNumber.setStatus("current")
_Hm2SfpPartRev_Type = SnmpAdminString
_Hm2SfpPartRev_Object = MibTableColumn
hm2SfpPartRev = _Hm2SfpPartRev_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 7),
    _Hm2SfpPartRev_Type()
)
hm2SfpPartRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpPartRev.setStatus("current")
_Hm2SfpSerialNum_Type = SnmpAdminString
_Hm2SfpSerialNum_Object = MibTableColumn
hm2SfpSerialNum = _Hm2SfpSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 8),
    _Hm2SfpSerialNum_Type()
)
hm2SfpSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpSerialNum.setStatus("current")
_Hm2SfpDateCode_Type = SnmpAdminString
_Hm2SfpDateCode_Object = MibTableColumn
hm2SfpDateCode = _Hm2SfpDateCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 9),
    _Hm2SfpDateCode_Type()
)
hm2SfpDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpDateCode.setStatus("current")
_Hm2SfpInfoVersion_Type = Integer32
_Hm2SfpInfoVersion_Object = MibTableColumn
hm2SfpInfoVersion = _Hm2SfpInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 10),
    _Hm2SfpInfoVersion_Type()
)
hm2SfpInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpInfoVersion.setStatus("current")


class _Hm2SfpInfoPartNumber_Type(SnmpAdminString):
    """Custom type hm2SfpInfoPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Hm2SfpInfoPartNumber_Type.__name__ = "SnmpAdminString"
_Hm2SfpInfoPartNumber_Object = MibTableColumn
hm2SfpInfoPartNumber = _Hm2SfpInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 11),
    _Hm2SfpInfoPartNumber_Type()
)
hm2SfpInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpInfoPartNumber.setStatus("current")


class _Hm2SfpInfoPartId_Type(SnmpAdminString):
    """Custom type hm2SfpInfoPartId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hm2SfpInfoPartId_Type.__name__ = "SnmpAdminString"
_Hm2SfpInfoPartId_Object = MibTableColumn
hm2SfpInfoPartId = _Hm2SfpInfoPartId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 12),
    _Hm2SfpInfoPartId_Type()
)
hm2SfpInfoPartId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpInfoPartId.setStatus("current")
_Hm2SfpBitRateNominal_Type = Integer32
_Hm2SfpBitRateNominal_Object = MibTableColumn
hm2SfpBitRateNominal = _Hm2SfpBitRateNominal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 13),
    _Hm2SfpBitRateNominal_Type()
)
hm2SfpBitRateNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpBitRateNominal.setStatus("current")
_Hm2SfpBitRateMin_Type = Integer32
_Hm2SfpBitRateMin_Object = MibTableColumn
hm2SfpBitRateMin = _Hm2SfpBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 14),
    _Hm2SfpBitRateMin_Type()
)
hm2SfpBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpBitRateMin.setStatus("current")
_Hm2SfpBitRateMax_Type = Integer32
_Hm2SfpBitRateMax_Object = MibTableColumn
hm2SfpBitRateMax = _Hm2SfpBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 15),
    _Hm2SfpBitRateMax_Type()
)
hm2SfpBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpBitRateMax.setStatus("current")
_Hm2SfpMaxLength_fiber_9_Type = Integer32
_Hm2SfpMaxLength_fiber_9_Object = MibScalar
hm2SfpMaxLength_fiber_9 = _Hm2SfpMaxLength_fiber_9_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 16),
    _Hm2SfpMaxLength_fiber_9_Type()
)
hm2SfpMaxLength_fiber_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpMaxLength_fiber_9.setStatus("current")
_Hm2SfpMaxLength_fiber_50_Type = Integer32
_Hm2SfpMaxLength_fiber_50_Object = MibScalar
hm2SfpMaxLength_fiber_50 = _Hm2SfpMaxLength_fiber_50_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 17),
    _Hm2SfpMaxLength_fiber_50_Type()
)
hm2SfpMaxLength_fiber_50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpMaxLength_fiber_50.setStatus("current")
_Hm2SfpMaxLength_fiber_e50_Type = Integer32
_Hm2SfpMaxLength_fiber_e50_Object = MibScalar
hm2SfpMaxLength_fiber_e50 = _Hm2SfpMaxLength_fiber_e50_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 18),
    _Hm2SfpMaxLength_fiber_e50_Type()
)
hm2SfpMaxLength_fiber_e50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpMaxLength_fiber_e50.setStatus("current")
_Hm2SfpMaxLength_fiber_62_5_Type = Integer32
_Hm2SfpMaxLength_fiber_62_5_Object = MibScalar
hm2SfpMaxLength_fiber_62_5 = _Hm2SfpMaxLength_fiber_62_5_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 19),
    _Hm2SfpMaxLength_fiber_62_5_Type()
)
hm2SfpMaxLength_fiber_62_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpMaxLength_fiber_62_5.setStatus("current")
_Hm2SfpMaxLength_copper_Type = Integer32
_Hm2SfpMaxLength_copper_Object = MibScalar
hm2SfpMaxLength_copper = _Hm2SfpMaxLength_copper_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 20),
    _Hm2SfpMaxLength_copper_Type()
)
hm2SfpMaxLength_copper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpMaxLength_copper.setStatus("current")
_Hm2SfpWaveLength_Type = Integer32
_Hm2SfpWaveLength_Object = MibTableColumn
hm2SfpWaveLength = _Hm2SfpWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 21),
    _Hm2SfpWaveLength_Type()
)
hm2SfpWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpWaveLength.setStatus("current")
_Hm2SfpWaveLengthTolerance_Type = Integer32
_Hm2SfpWaveLengthTolerance_Object = MibTableColumn
hm2SfpWaveLengthTolerance = _Hm2SfpWaveLengthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 22),
    _Hm2SfpWaveLengthTolerance_Type()
)
hm2SfpWaveLengthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpWaveLengthTolerance.setStatus("current")


class _Hm2SfpEnhancedOptions_Type(Bits):
    """Custom type hm2SfpEnhancedOptions based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_Hm2SfpEnhancedOptions_Type.__name__ = "Bits"
_Hm2SfpEnhancedOptions_Object = MibTableColumn
hm2SfpEnhancedOptions = _Hm2SfpEnhancedOptions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 23),
    _Hm2SfpEnhancedOptions_Type()
)
hm2SfpEnhancedOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpEnhancedOptions.setStatus("current")
_Hm2SfpSupported_Type = TruthValue
_Hm2SfpSupported_Object = MibTableColumn
hm2SfpSupported = _Hm2SfpSupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 24),
    _Hm2SfpSupported_Type()
)
hm2SfpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpSupported.setStatus("current")


class _Hm2SfpSupportedReason_Type(Integer32):
    """Custom type hm2SfpSupportedReason based on Integer32"""
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
        *(("hirschmannID", 1),
          ("noneEthernet", 4),
          ("tpSfpNotSupported", 5),
          ("whiteList", 2),
          ("wrongSpeed", 3))
    )


_Hm2SfpSupportedReason_Type.__name__ = "Integer32"
_Hm2SfpSupportedReason_Object = MibTableColumn
hm2SfpSupportedReason = _Hm2SfpSupportedReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 1, 1, 25),
    _Hm2SfpSupportedReason_Type()
)
hm2SfpSupportedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpSupportedReason.setStatus("current")
_Hm2SfpDiagTable_Object = MibTable
hm2SfpDiagTable = _Hm2SfpDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hm2SfpDiagTable.setStatus("current")
_Hm2SfpDiagEntry_Object = MibTableRow
hm2SfpDiagEntry = _Hm2SfpDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1)
)
hm2SfpDiagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2SfpDiagEntry.setStatus("current")
_Hm2SfpCurrentBitRate_Type = Integer32
_Hm2SfpCurrentBitRate_Object = MibTableColumn
hm2SfpCurrentBitRate = _Hm2SfpCurrentBitRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 1),
    _Hm2SfpCurrentBitRate_Type()
)
hm2SfpCurrentBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentBitRate.setStatus("current")
_Hm2SfpCurrentTemperature_Type = Integer32
_Hm2SfpCurrentTemperature_Object = MibTableColumn
hm2SfpCurrentTemperature = _Hm2SfpCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 2),
    _Hm2SfpCurrentTemperature_Type()
)
hm2SfpCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentTemperature.setStatus("current")
_Hm2SfpCurrentTxPower_Type = Integer32
_Hm2SfpCurrentTxPower_Object = MibTableColumn
hm2SfpCurrentTxPower = _Hm2SfpCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 3),
    _Hm2SfpCurrentTxPower_Type()
)
hm2SfpCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentTxPower.setStatus("current")
_Hm2SfpCurrentRxPower_Type = Integer32
_Hm2SfpCurrentRxPower_Object = MibTableColumn
hm2SfpCurrentRxPower = _Hm2SfpCurrentRxPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 4),
    _Hm2SfpCurrentRxPower_Type()
)
hm2SfpCurrentRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentRxPower.setStatus("current")
_Hm2SfpCurrentTxPowerdBm_Type = SnmpAdminString
_Hm2SfpCurrentTxPowerdBm_Object = MibTableColumn
hm2SfpCurrentTxPowerdBm = _Hm2SfpCurrentTxPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 5),
    _Hm2SfpCurrentTxPowerdBm_Type()
)
hm2SfpCurrentTxPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentTxPowerdBm.setStatus("current")
_Hm2SfpCurrentRxPowerdBm_Type = SnmpAdminString
_Hm2SfpCurrentRxPowerdBm_Object = MibTableColumn
hm2SfpCurrentRxPowerdBm = _Hm2SfpCurrentRxPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 6),
    _Hm2SfpCurrentRxPowerdBm_Type()
)
hm2SfpCurrentRxPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentRxPowerdBm.setStatus("current")


class _Hm2SfpCurrentRxPowerState_Type(Integer32):
    """Custom type hm2SfpCurrentRxPowerState based on Integer32"""
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
        *(("alarm", 3),
          ("ok", 1),
          ("unsupported", 4),
          ("warning", 2))
    )


_Hm2SfpCurrentRxPowerState_Type.__name__ = "Integer32"
_Hm2SfpCurrentRxPowerState_Object = MibTableColumn
hm2SfpCurrentRxPowerState = _Hm2SfpCurrentRxPowerState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 2, 1, 7),
    _Hm2SfpCurrentRxPowerState_Type()
)
hm2SfpCurrentRxPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpCurrentRxPowerState.setStatus("current")
_Hm2SfpWLGroup_ObjectIdentity = ObjectIdentity
hm2SfpWLGroup = _Hm2SfpWLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 3)
)


class _Hm2SfpWLStatus_Type(Integer32):
    """Custom type hm2SfpWLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("not-supported", 3),
          ("present", 1))
    )


_Hm2SfpWLStatus_Type.__name__ = "Integer32"
_Hm2SfpWLStatus_Object = MibScalar
hm2SfpWLStatus = _Hm2SfpWLStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 3, 1),
    _Hm2SfpWLStatus_Type()
)
hm2SfpWLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpWLStatus.setStatus("current")
_Hm2SfpThresholdTable_Object = MibTable
hm2SfpThresholdTable = _Hm2SfpThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4)
)
if mibBuilder.loadTexts:
    hm2SfpThresholdTable.setStatus("current")
_Hm2SfpThresholdEntry_Object = MibTableRow
hm2SfpThresholdEntry = _Hm2SfpThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1)
)
hm2SfpThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2SfpThresholdEntry.setStatus("current")
_Hm2SfpTemperatureHighAlarm_Type = Integer32
_Hm2SfpTemperatureHighAlarm_Object = MibTableColumn
hm2SfpTemperatureHighAlarm = _Hm2SfpTemperatureHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 1),
    _Hm2SfpTemperatureHighAlarm_Type()
)
hm2SfpTemperatureHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTemperatureHighAlarm.setStatus("current")
_Hm2SfpTemperatureHighWarning_Type = Integer32
_Hm2SfpTemperatureHighWarning_Object = MibTableColumn
hm2SfpTemperatureHighWarning = _Hm2SfpTemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 2),
    _Hm2SfpTemperatureHighWarning_Type()
)
hm2SfpTemperatureHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTemperatureHighWarning.setStatus("current")
_Hm2SfpTemperatureLowAlarm_Type = Integer32
_Hm2SfpTemperatureLowAlarm_Object = MibTableColumn
hm2SfpTemperatureLowAlarm = _Hm2SfpTemperatureLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 3),
    _Hm2SfpTemperatureLowAlarm_Type()
)
hm2SfpTemperatureLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTemperatureLowAlarm.setStatus("current")
_Hm2SfpTemperatureLowWarning_Type = Integer32
_Hm2SfpTemperatureLowWarning_Object = MibTableColumn
hm2SfpTemperatureLowWarning = _Hm2SfpTemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 4),
    _Hm2SfpTemperatureLowWarning_Type()
)
hm2SfpTemperatureLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTemperatureLowWarning.setStatus("current")
_Hm2SfpTxPowerHighAlarm_Type = Integer32
_Hm2SfpTxPowerHighAlarm_Object = MibTableColumn
hm2SfpTxPowerHighAlarm = _Hm2SfpTxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 5),
    _Hm2SfpTxPowerHighAlarm_Type()
)
hm2SfpTxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerHighAlarm.setStatus("current")
_Hm2SfpTxPowerHighWarning_Type = Integer32
_Hm2SfpTxPowerHighWarning_Object = MibTableColumn
hm2SfpTxPowerHighWarning = _Hm2SfpTxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 6),
    _Hm2SfpTxPowerHighWarning_Type()
)
hm2SfpTxPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerHighWarning.setStatus("current")
_Hm2SfpTxPowerLowAlarm_Type = Integer32
_Hm2SfpTxPowerLowAlarm_Object = MibTableColumn
hm2SfpTxPowerLowAlarm = _Hm2SfpTxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 7),
    _Hm2SfpTxPowerLowAlarm_Type()
)
hm2SfpTxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerLowAlarm.setStatus("current")
_Hm2SfpTxPowerLowWarning_Type = Integer32
_Hm2SfpTxPowerLowWarning_Object = MibTableColumn
hm2SfpTxPowerLowWarning = _Hm2SfpTxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 8),
    _Hm2SfpTxPowerLowWarning_Type()
)
hm2SfpTxPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerLowWarning.setStatus("current")
_Hm2SfpRxPowerHighAlarm_Type = Integer32
_Hm2SfpRxPowerHighAlarm_Object = MibTableColumn
hm2SfpRxPowerHighAlarm = _Hm2SfpRxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 9),
    _Hm2SfpRxPowerHighAlarm_Type()
)
hm2SfpRxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerHighAlarm.setStatus("current")
_Hm2SfpRxPowerHighWarning_Type = Integer32
_Hm2SfpRxPowerHighWarning_Object = MibTableColumn
hm2SfpRxPowerHighWarning = _Hm2SfpRxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 10),
    _Hm2SfpRxPowerHighWarning_Type()
)
hm2SfpRxPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerHighWarning.setStatus("current")
_Hm2SfpRxPowerLowAlarm_Type = Integer32
_Hm2SfpRxPowerLowAlarm_Object = MibTableColumn
hm2SfpRxPowerLowAlarm = _Hm2SfpRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 11),
    _Hm2SfpRxPowerLowAlarm_Type()
)
hm2SfpRxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerLowAlarm.setStatus("current")
_Hm2SfpRxPowerLowWarning_Type = Integer32
_Hm2SfpRxPowerLowWarning_Object = MibTableColumn
hm2SfpRxPowerLowWarning = _Hm2SfpRxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 12),
    _Hm2SfpRxPowerLowWarning_Type()
)
hm2SfpRxPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerLowWarning.setStatus("current")
_Hm2SfpTxPowerdBmHighAlarm_Type = SnmpAdminString
_Hm2SfpTxPowerdBmHighAlarm_Object = MibTableColumn
hm2SfpTxPowerdBmHighAlarm = _Hm2SfpTxPowerdBmHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 13),
    _Hm2SfpTxPowerdBmHighAlarm_Type()
)
hm2SfpTxPowerdBmHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerdBmHighAlarm.setStatus("current")
_Hm2SfpTxPowerdBmHighWarning_Type = SnmpAdminString
_Hm2SfpTxPowerdBmHighWarning_Object = MibTableColumn
hm2SfpTxPowerdBmHighWarning = _Hm2SfpTxPowerdBmHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 14),
    _Hm2SfpTxPowerdBmHighWarning_Type()
)
hm2SfpTxPowerdBmHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerdBmHighWarning.setStatus("current")
_Hm2SfpTxPowerdBmLowAlarm_Type = SnmpAdminString
_Hm2SfpTxPowerdBmLowAlarm_Object = MibTableColumn
hm2SfpTxPowerdBmLowAlarm = _Hm2SfpTxPowerdBmLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 15),
    _Hm2SfpTxPowerdBmLowAlarm_Type()
)
hm2SfpTxPowerdBmLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerdBmLowAlarm.setStatus("current")
_Hm2SfpTxPowerdBmLowWarning_Type = SnmpAdminString
_Hm2SfpTxPowerdBmLowWarning_Object = MibTableColumn
hm2SfpTxPowerdBmLowWarning = _Hm2SfpTxPowerdBmLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 16),
    _Hm2SfpTxPowerdBmLowWarning_Type()
)
hm2SfpTxPowerdBmLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpTxPowerdBmLowWarning.setStatus("current")
_Hm2SfpRxPowerdBmHighAlarm_Type = SnmpAdminString
_Hm2SfpRxPowerdBmHighAlarm_Object = MibTableColumn
hm2SfpRxPowerdBmHighAlarm = _Hm2SfpRxPowerdBmHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 17),
    _Hm2SfpRxPowerdBmHighAlarm_Type()
)
hm2SfpRxPowerdBmHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerdBmHighAlarm.setStatus("current")
_Hm2SfpRxPowerdBmHighWarning_Type = SnmpAdminString
_Hm2SfpRxPowerdBmHighWarning_Object = MibTableColumn
hm2SfpRxPowerdBmHighWarning = _Hm2SfpRxPowerdBmHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 18),
    _Hm2SfpRxPowerdBmHighWarning_Type()
)
hm2SfpRxPowerdBmHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerdBmHighWarning.setStatus("current")
_Hm2SfpRxPowerdBmLowAlarm_Type = SnmpAdminString
_Hm2SfpRxPowerdBmLowAlarm_Object = MibTableColumn
hm2SfpRxPowerdBmLowAlarm = _Hm2SfpRxPowerdBmLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 19),
    _Hm2SfpRxPowerdBmLowAlarm_Type()
)
hm2SfpRxPowerdBmLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerdBmLowAlarm.setStatus("current")
_Hm2SfpRxPowerdBmLowWarning_Type = SnmpAdminString
_Hm2SfpRxPowerdBmLowWarning_Object = MibTableColumn
hm2SfpRxPowerdBmLowWarning = _Hm2SfpRxPowerdBmLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 7, 4, 1, 20),
    _Hm2SfpRxPowerdBmLowWarning_Type()
)
hm2SfpRxPowerdBmLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SfpRxPowerdBmLowWarning.setStatus("current")
_Hm2ExtNvmGroup_ObjectIdentity = ObjectIdentity
hm2ExtNvmGroup = _Hm2ExtNvmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8)
)
_Hm2ExtNvmGeneralGroup_ObjectIdentity = ObjectIdentity
hm2ExtNvmGeneralGroup = _Hm2ExtNvmGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 1)
)


class _Hm2ExtNvmChooseActive_Type(Hm2DeviceExtNVMType):
    """Custom type hm2ExtNvmChooseActive based on Hm2DeviceExtNVMType"""


_Hm2ExtNvmChooseActive_Object = MibScalar
hm2ExtNvmChooseActive = _Hm2ExtNvmChooseActive_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 1, 1),
    _Hm2ExtNvmChooseActive_Type()
)
hm2ExtNvmChooseActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmChooseActive.setStatus("current")


class _Hm2ExtNvmLogDevice_Type(Hm2DeviceExtNVMType):
    """Custom type hm2ExtNvmLogDevice based on Hm2DeviceExtNVMType"""


_Hm2ExtNvmLogDevice_Object = MibScalar
hm2ExtNvmLogDevice = _Hm2ExtNvmLogDevice_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 1, 2),
    _Hm2ExtNvmLogDevice_Type()
)
hm2ExtNvmLogDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmLogDevice.setStatus("current")


class _Hm2ExtNvmAdminMode_Type(Integer32):
    """Custom type hm2ExtNvmAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatibility", 2),
          ("normal", 1))
    )


_Hm2ExtNvmAdminMode_Type.__name__ = "Integer32"
_Hm2ExtNvmAdminMode_Object = MibScalar
hm2ExtNvmAdminMode = _Hm2ExtNvmAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 1, 3),
    _Hm2ExtNvmAdminMode_Type()
)
hm2ExtNvmAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmAdminMode.setStatus("current")


class _Hm2ExtNvmOperMode_Type(Integer32):
    """Custom type hm2ExtNvmOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatibility", 2),
          ("normal", 1))
    )


_Hm2ExtNvmOperMode_Type.__name__ = "Integer32"
_Hm2ExtNvmOperMode_Object = MibScalar
hm2ExtNvmOperMode = _Hm2ExtNvmOperMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 1, 4),
    _Hm2ExtNvmOperMode_Type()
)
hm2ExtNvmOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmOperMode.setStatus("current")
_Hm2ExtNvmTable_Object = MibTable
hm2ExtNvmTable = _Hm2ExtNvmTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2)
)
if mibBuilder.loadTexts:
    hm2ExtNvmTable.setStatus("current")
_Hm2ExtNvmEntry_Object = MibTableRow
hm2ExtNvmEntry = _Hm2ExtNvmEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1)
)
hm2ExtNvmEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2ExtNvmTableIndex"),
)
if mibBuilder.loadTexts:
    hm2ExtNvmEntry.setStatus("current")
_Hm2ExtNvmTableIndex_Type = Hm2DeviceExtNVMType
_Hm2ExtNvmTableIndex_Object = MibTableColumn
hm2ExtNvmTableIndex = _Hm2ExtNvmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 1),
    _Hm2ExtNvmTableIndex_Type()
)
hm2ExtNvmTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2ExtNvmTableIndex.setStatus("current")


class _Hm2ExtNvmStatus_Type(Integer32):
    """Custom type hm2ExtNvmStatus based on Integer32"""
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
        *(("genericErr", 5),
          ("notPresent", 1),
          ("ok", 3),
          ("outOfMemory", 4),
          ("removed", 2))
    )


_Hm2ExtNvmStatus_Type.__name__ = "Integer32"
_Hm2ExtNvmStatus_Object = MibTableColumn
hm2ExtNvmStatus = _Hm2ExtNvmStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 2),
    _Hm2ExtNvmStatus_Type()
)
hm2ExtNvmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmStatus.setStatus("current")
_Hm2ExtNvmManufacturerId_Type = DisplayString
_Hm2ExtNvmManufacturerId_Object = MibTableColumn
hm2ExtNvmManufacturerId = _Hm2ExtNvmManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 3),
    _Hm2ExtNvmManufacturerId_Type()
)
hm2ExtNvmManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmManufacturerId.setStatus("current")
_Hm2ExtNvmHWRevision_Type = DisplayString
_Hm2ExtNvmHWRevision_Object = MibTableColumn
hm2ExtNvmHWRevision = _Hm2ExtNvmHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 4),
    _Hm2ExtNvmHWRevision_Type()
)
hm2ExtNvmHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmHWRevision.setStatus("current")
_Hm2ExtNvmProductName_Type = DisplayString
_Hm2ExtNvmProductName_Object = MibTableColumn
hm2ExtNvmProductName = _Hm2ExtNvmProductName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 5),
    _Hm2ExtNvmProductName_Type()
)
hm2ExtNvmProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmProductName.setStatus("current")
_Hm2ExtNvmVersion_Type = DisplayString
_Hm2ExtNvmVersion_Object = MibTableColumn
hm2ExtNvmVersion = _Hm2ExtNvmVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 6),
    _Hm2ExtNvmVersion_Type()
)
hm2ExtNvmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmVersion.setStatus("current")
_Hm2ExtNvmSerialNum_Type = DisplayString
_Hm2ExtNvmSerialNum_Object = MibTableColumn
hm2ExtNvmSerialNum = _Hm2ExtNvmSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 7),
    _Hm2ExtNvmSerialNum_Type()
)
hm2ExtNvmSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmSerialNum.setStatus("current")


class _Hm2ExtNvmAutomaticSoftwareLoad_Type(HmEnabledStatus):
    """Custom type hm2ExtNvmAutomaticSoftwareLoad based on HmEnabledStatus"""


_Hm2ExtNvmAutomaticSoftwareLoad_Object = MibTableColumn
hm2ExtNvmAutomaticSoftwareLoad = _Hm2ExtNvmAutomaticSoftwareLoad_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 8),
    _Hm2ExtNvmAutomaticSoftwareLoad_Type()
)
hm2ExtNvmAutomaticSoftwareLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmAutomaticSoftwareLoad.setStatus("current")


class _Hm2ExtNvmConfigLoadPriority_Type(Integer32):
    """Custom type hm2ExtNvmConfigLoadPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("first", 1),
          ("second", 2),
          ("third", 3))
    )


_Hm2ExtNvmConfigLoadPriority_Type.__name__ = "Integer32"
_Hm2ExtNvmConfigLoadPriority_Object = MibTableColumn
hm2ExtNvmConfigLoadPriority = _Hm2ExtNvmConfigLoadPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 9),
    _Hm2ExtNvmConfigLoadPriority_Type()
)
hm2ExtNvmConfigLoadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmConfigLoadPriority.setStatus("current")


class _Hm2ExtNvmConfigSave_Type(HmEnabledStatus):
    """Custom type hm2ExtNvmConfigSave based on HmEnabledStatus"""


_Hm2ExtNvmConfigSave_Object = MibTableColumn
hm2ExtNvmConfigSave = _Hm2ExtNvmConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 10),
    _Hm2ExtNvmConfigSave_Type()
)
hm2ExtNvmConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmConfigSave.setStatus("current")
_Hm2ExtNvmWritable_Type = HmEnabledStatus
_Hm2ExtNvmWritable_Object = MibTableColumn
hm2ExtNvmWritable = _Hm2ExtNvmWritable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 11),
    _Hm2ExtNvmWritable_Type()
)
hm2ExtNvmWritable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ExtNvmWritable.setStatus("current")


class _Hm2ExtNvmAutomaticSshKeyLoad_Type(HmEnabledStatus):
    """Custom type hm2ExtNvmAutomaticSshKeyLoad based on HmEnabledStatus"""


_Hm2ExtNvmAutomaticSshKeyLoad_Object = MibTableColumn
hm2ExtNvmAutomaticSshKeyLoad = _Hm2ExtNvmAutomaticSshKeyLoad_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 8, 2, 1, 12),
    _Hm2ExtNvmAutomaticSshKeyLoad_Type()
)
hm2ExtNvmAutomaticSshKeyLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ExtNvmAutomaticSshKeyLoad.setStatus("current")
_Hm2AutoDisableGroup_ObjectIdentity = ObjectIdentity
hm2AutoDisableGroup = _Hm2AutoDisableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9)
)
_Hm2AutoDisableIntfTable_Object = MibTable
hm2AutoDisableIntfTable = _Hm2AutoDisableIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hm2AutoDisableIntfTable.setStatus("current")
_Hm2AutoDisableIntfEntry_Object = MibTableRow
hm2AutoDisableIntfEntry = _Hm2AutoDisableIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1)
)
hm2AutoDisableIntfEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"),
)
if mibBuilder.loadTexts:
    hm2AutoDisableIntfEntry.setStatus("current")


class _Hm2AutoDisableIntfRemainingTime_Type(Unsigned32):
    """Custom type hm2AutoDisableIntfRemainingTime based on Unsigned32"""
    defaultValue = 0


_Hm2AutoDisableIntfRemainingTime_Object = MibTableColumn
hm2AutoDisableIntfRemainingTime = _Hm2AutoDisableIntfRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 1),
    _Hm2AutoDisableIntfRemainingTime_Type()
)
hm2AutoDisableIntfRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfRemainingTime.setStatus("current")
_Hm2AutoDisableIntfComponentName_Type = SnmpAdminString
_Hm2AutoDisableIntfComponentName_Object = MibTableColumn
hm2AutoDisableIntfComponentName = _Hm2AutoDisableIntfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 2),
    _Hm2AutoDisableIntfComponentName_Type()
)
hm2AutoDisableIntfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfComponentName.setStatus("current")


class _Hm2AutoDisableIntfErrorReason_Type(Integer32):
    """Custom type hm2AutoDisableIntfErrorReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("arp-rate", 5),
          ("bpdu-rate", 6),
          ("crc-error", 2),
          ("dhcp-snooping", 4),
          ("duplex-mismatch", 3),
          ("link-flap", 1),
          ("mac-based-port-security", 7),
          ("none", 0),
          ("overload-detection", 8),
          ("speed-duplex", 9))
    )


_Hm2AutoDisableIntfErrorReason_Type.__name__ = "Integer32"
_Hm2AutoDisableIntfErrorReason_Object = MibTableColumn
hm2AutoDisableIntfErrorReason = _Hm2AutoDisableIntfErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 3),
    _Hm2AutoDisableIntfErrorReason_Type()
)
hm2AutoDisableIntfErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfErrorReason.setStatus("current")


class _Hm2AutoDisableIntfTimer_Type(Unsigned32):
    """Custom type hm2AutoDisableIntfTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 4294967295),
    )


_Hm2AutoDisableIntfTimer_Type.__name__ = "Unsigned32"
_Hm2AutoDisableIntfTimer_Object = MibTableColumn
hm2AutoDisableIntfTimer = _Hm2AutoDisableIntfTimer_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 4),
    _Hm2AutoDisableIntfTimer_Type()
)
hm2AutoDisableIntfTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfTimer.setStatus("current")


class _Hm2AutoDisableIntfReset_Type(TruthValue):
    """Custom type hm2AutoDisableIntfReset based on TruthValue"""


_Hm2AutoDisableIntfReset_Object = MibTableColumn
hm2AutoDisableIntfReset = _Hm2AutoDisableIntfReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 5),
    _Hm2AutoDisableIntfReset_Type()
)
hm2AutoDisableIntfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfReset.setStatus("current")


class _Hm2AutoDisableIntfOperState_Type(Integer32):
    """Custom type hm2AutoDisableIntfOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hm2AutoDisableIntfOperState_Type.__name__ = "Integer32"
_Hm2AutoDisableIntfOperState_Object = MibTableColumn
hm2AutoDisableIntfOperState = _Hm2AutoDisableIntfOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 6),
    _Hm2AutoDisableIntfOperState_Type()
)
hm2AutoDisableIntfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfOperState.setStatus("current")
_Hm2AutoDisableIntfErrorTime_Type = HmTimeSeconds1970
_Hm2AutoDisableIntfErrorTime_Object = MibTableColumn
hm2AutoDisableIntfErrorTime = _Hm2AutoDisableIntfErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 1, 1, 7),
    _Hm2AutoDisableIntfErrorTime_Type()
)
hm2AutoDisableIntfErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AutoDisableIntfErrorTime.setStatus("current")
_Hm2AutoDisableReasonTable_Object = MibTable
hm2AutoDisableReasonTable = _Hm2AutoDisableReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hm2AutoDisableReasonTable.setStatus("current")
_Hm2AutoDisableReasonEntry_Object = MibTableRow
hm2AutoDisableReasonEntry = _Hm2AutoDisableReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 2, 1)
)
hm2AutoDisableReasonEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2AutoDisableReasons"),
)
if mibBuilder.loadTexts:
    hm2AutoDisableReasonEntry.setStatus("current")


class _Hm2AutoDisableReasons_Type(Integer32):
    """Custom type hm2AutoDisableReasons based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("arp-rate", 5),
          ("bpdu-rate", 6),
          ("crc-error", 2),
          ("dhcp-snooping", 4),
          ("duplex-mismatch", 3),
          ("link-flap", 1),
          ("mac-based-port-security", 7),
          ("overload-detection", 8),
          ("speed-duplex", 9))
    )


_Hm2AutoDisableReasons_Type.__name__ = "Integer32"
_Hm2AutoDisableReasons_Object = MibTableColumn
hm2AutoDisableReasons = _Hm2AutoDisableReasons_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 2, 1, 1),
    _Hm2AutoDisableReasons_Type()
)
hm2AutoDisableReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AutoDisableReasons.setStatus("current")


class _Hm2AutoDisableReasonOperation_Type(HmEnabledStatus):
    """Custom type hm2AutoDisableReasonOperation based on HmEnabledStatus"""


_Hm2AutoDisableReasonOperation_Object = MibTableColumn
hm2AutoDisableReasonOperation = _Hm2AutoDisableReasonOperation_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 2, 1, 2),
    _Hm2AutoDisableReasonOperation_Type()
)
hm2AutoDisableReasonOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AutoDisableReasonOperation.setStatus("current")


class _Hm2AutoDisableReasonCategory_Type(Integer32):
    """Custom type hm2AutoDisableReasonCategory based on Integer32"""
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
        *(("l2-redundancy", 4),
          ("network-security", 3),
          ("other", 1),
          ("port-monitor", 2))
    )


_Hm2AutoDisableReasonCategory_Type.__name__ = "Integer32"
_Hm2AutoDisableReasonCategory_Object = MibTableColumn
hm2AutoDisableReasonCategory = _Hm2AutoDisableReasonCategory_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 9, 2, 1, 3),
    _Hm2AutoDisableReasonCategory_Type()
)
hm2AutoDisableReasonCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AutoDisableReasonCategory.setStatus("current")
_Hm2UnitGroup_ObjectIdentity = ObjectIdentity
hm2UnitGroup = _Hm2UnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 10)
)
_Hm2UnitTable_Object = MibTable
hm2UnitTable = _Hm2UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 10, 100)
)
if mibBuilder.loadTexts:
    hm2UnitTable.setStatus("current")
_Hm2UnitEntry_Object = MibTableRow
hm2UnitEntry = _Hm2UnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 10, 100, 1)
)
hm2UnitEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2UnitIndex"),
)
if mibBuilder.loadTexts:
    hm2UnitEntry.setStatus("current")
_Hm2UnitIndex_Type = Integer32
_Hm2UnitIndex_Object = MibTableColumn
hm2UnitIndex = _Hm2UnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 10, 100, 1, 1),
    _Hm2UnitIndex_Type()
)
hm2UnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2UnitIndex.setStatus("current")
_Hm2UnitMaxModuleCapacity_Type = Integer32
_Hm2UnitMaxModuleCapacity_Object = MibTableColumn
hm2UnitMaxModuleCapacity = _Hm2UnitMaxModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 10, 100, 1, 2),
    _Hm2UnitMaxModuleCapacity_Type()
)
hm2UnitMaxModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2UnitMaxModuleCapacity.setStatus("current")
_Hm2UnitMaxModulePortCapacity_Type = Integer32
_Hm2UnitMaxModulePortCapacity_Object = MibTableColumn
hm2UnitMaxModulePortCapacity = _Hm2UnitMaxModulePortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 10, 100, 1, 3),
    _Hm2UnitMaxModulePortCapacity_Type()
)
hm2UnitMaxModulePortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2UnitMaxModulePortCapacity.setStatus("current")
_Hm2ModuleGroup_ObjectIdentity = ObjectIdentity
hm2ModuleGroup = _Hm2ModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11)
)
_Hm2ModuleTable_Object = MibTable
hm2ModuleTable = _Hm2ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100)
)
if mibBuilder.loadTexts:
    hm2ModuleTable.setStatus("current")
_Hm2ModuleEntry_Object = MibTableRow
hm2ModuleEntry = _Hm2ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1)
)
hm2ModuleEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2UnitIndex"),
    (0, "HM2-DEVMGMT-MIB", "hm2ModuleIndex"),
)
if mibBuilder.loadTexts:
    hm2ModuleEntry.setStatus("current")
_Hm2ModuleIndex_Type = Integer32
_Hm2ModuleIndex_Object = MibTableColumn
hm2ModuleIndex = _Hm2ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 1),
    _Hm2ModuleIndex_Type()
)
hm2ModuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2ModuleIndex.setStatus("current")
_Hm2ModuleId_Type = ObjectIdentifier
_Hm2ModuleId_Object = MibTableColumn
hm2ModuleId = _Hm2ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 2),
    _Hm2ModuleId_Type()
)
hm2ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleId.setStatus("current")
_Hm2ModuleDescription_Type = SnmpAdminString
_Hm2ModuleDescription_Object = MibTableColumn
hm2ModuleDescription = _Hm2ModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 3),
    _Hm2ModuleDescription_Type()
)
hm2ModuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModuleDescription.setStatus("current")
_Hm2ModuleProductCode_Type = SnmpAdminString
_Hm2ModuleProductCode_Object = MibTableColumn
hm2ModuleProductCode = _Hm2ModuleProductCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 4),
    _Hm2ModuleProductCode_Type()
)
hm2ModuleProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleProductCode.setStatus("current")
_Hm2ModuleVersion_Type = SnmpAdminString
_Hm2ModuleVersion_Object = MibTableColumn
hm2ModuleVersion = _Hm2ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 5),
    _Hm2ModuleVersion_Type()
)
hm2ModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleVersion.setStatus("current")
_Hm2ModuleNumOfPorts_Type = Integer32
_Hm2ModuleNumOfPorts_Object = MibTableColumn
hm2ModuleNumOfPorts = _Hm2ModuleNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 6),
    _Hm2ModuleNumOfPorts_Type()
)
hm2ModuleNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleNumOfPorts.setStatus("current")
_Hm2ModuleFirstMauIndex_Type = Integer32
_Hm2ModuleFirstMauIndex_Object = MibTableColumn
hm2ModuleFirstMauIndex = _Hm2ModuleFirstMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 7),
    _Hm2ModuleFirstMauIndex_Type()
)
hm2ModuleFirstMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleFirstMauIndex.setStatus("obsolete")


class _Hm2ModuleStatus_Type(Integer32):
    """Custom type hm2ModuleStatus based on Integer32"""
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
        *(("configurable", 2),
          ("fix", 4),
          ("physical", 1),
          ("remove", 3))
    )


_Hm2ModuleStatus_Type.__name__ = "Integer32"
_Hm2ModuleStatus_Object = MibTableColumn
hm2ModuleStatus = _Hm2ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 8),
    _Hm2ModuleStatus_Type()
)
hm2ModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModuleStatus.setStatus("current")
_Hm2ModuleSerialNum_Type = SnmpAdminString
_Hm2ModuleSerialNum_Object = MibTableColumn
hm2ModuleSerialNum = _Hm2ModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 9),
    _Hm2ModuleSerialNum_Type()
)
hm2ModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleSerialNum.setStatus("current")
_Hm2ModuleMinSWVersion_Type = Integer32
_Hm2ModuleMinSWVersion_Object = MibTableColumn
hm2ModuleMinSWVersion = _Hm2ModuleMinSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 10),
    _Hm2ModuleMinSWVersion_Type()
)
hm2ModuleMinSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleMinSWVersion.setStatus("current")


class _Hm2ModuleCapability_Type(Bits):
    """Custom type hm2ModuleCapability based on Bits"""
    namedValues = NamedValues(
        *(("fpga", 1),
          ("io-module", 3),
          ("poe", 0),
          ("ptp", 2))
    )

_Hm2ModuleCapability_Type.__name__ = "Bits"
_Hm2ModuleCapability_Object = MibTableColumn
hm2ModuleCapability = _Hm2ModuleCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 11),
    _Hm2ModuleCapability_Type()
)
hm2ModuleCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModuleCapability.setStatus("current")


class _Hm2ModuleInternalID_Type(Integer32):
    """Custom type hm2ModuleInternalID based on Integer32"""
    defaultValue = 0


_Hm2ModuleInternalID_Object = MibTableColumn
hm2ModuleInternalID = _Hm2ModuleInternalID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 12),
    _Hm2ModuleInternalID_Type()
)
hm2ModuleInternalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModuleInternalID.setStatus("current")


class _Hm2ModuleInternalIDVariant_Type(Integer32):
    """Custom type hm2ModuleInternalIDVariant based on Integer32"""
    defaultValue = 0


_Hm2ModuleInternalIDVariant_Object = MibTableColumn
hm2ModuleInternalIDVariant = _Hm2ModuleInternalIDVariant_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 13),
    _Hm2ModuleInternalIDVariant_Type()
)
hm2ModuleInternalIDVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModuleInternalIDVariant.setStatus("obsolete")
_Hm2ModuleFirstIfIndex_Type = Integer32
_Hm2ModuleFirstIfIndex_Object = MibTableColumn
hm2ModuleFirstIfIndex = _Hm2ModuleFirstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 14),
    _Hm2ModuleFirstIfIndex_Type()
)
hm2ModuleFirstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModuleFirstIfIndex.setStatus("current")


class _Hm2ModuleAdminState_Type(HmEnabledStatus):
    """Custom type hm2ModuleAdminState based on HmEnabledStatus"""


_Hm2ModuleAdminState_Object = MibTableColumn
hm2ModuleAdminState = _Hm2ModuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 1, 11, 100, 1, 15),
    _Hm2ModuleAdminState_Type()
)
hm2ModuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModuleAdminState.setStatus("current")

# Managed Objects groups


# Notification objects

hm2SfpChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 0, 1)
)
hm2SfpChangeTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hm2SfpChangeTrap.setStatus(
        "current"
    )

hm2AutoDisablePortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 0, 2)
)
hm2AutoDisablePortTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HM2-DEVMGMT-MIB", "hm2IfaceOperAdminStatus"),
        ("HM2-DEVMGMT-MIB", "hm2AutoDisableIntfErrorReason"))
)
if mibBuilder.loadTexts:
    hm2AutoDisablePortTrap.setStatus(
        "current"
    )

hm2ModulePluggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 0, 3)
)
hm2ModulePluggedTrap.setObjects(
      *(("HM2-DEVMGMT-MIB", "hm2UnitIndex"),
        ("HM2-DEVMGMT-MIB", "hm2ModuleIndex"))
)
if mibBuilder.loadTexts:
    hm2ModulePluggedTrap.setStatus(
        "current"
    )

hm2ModuleRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 0, 4)
)
hm2ModuleRemovedTrap.setObjects(
      *(("HM2-DEVMGMT-MIB", "hm2UnitIndex"),
        ("HM2-DEVMGMT-MIB", "hm2ModuleIndex"))
)
if mibBuilder.loadTexts:
    hm2ModuleRemovedTrap.setStatus(
        "current"
    )

hm2SFPRxPowerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 10, 0, 5)
)
hm2SFPRxPowerChangeTrap.setObjects(
    ("HM2-DEVMGMT-MIB", "hm2SfpCurrentRxPowerState")
)
if mibBuilder.loadTexts:
    hm2SFPRxPowerChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-DEVMGMT-MIB",
    **{"Hm2DeviceExtNVMType": Hm2DeviceExtNVMType,
       "hm2DeviceMgmtMib": hm2DeviceMgmtMib,
       "hm2DeviceMgmtMibNotifications": hm2DeviceMgmtMibNotifications,
       "hm2SfpChangeTrap": hm2SfpChangeTrap,
       "hm2AutoDisablePortTrap": hm2AutoDisablePortTrap,
       "hm2ModulePluggedTrap": hm2ModulePluggedTrap,
       "hm2ModuleRemovedTrap": hm2ModuleRemovedTrap,
       "hm2SFPRxPowerChangeTrap": hm2SFPRxPowerChangeTrap,
       "hm2DeviceMgmtMibObjects": hm2DeviceMgmtMibObjects,
       "hm2DeviceMgmtGroup": hm2DeviceMgmtGroup,
       "hm2DevMgmtProductId": hm2DevMgmtProductId,
       "hm2DevMgmtProductDescr": hm2DevMgmtProductDescr,
       "hm2DevMgmtSerialNumber": hm2DevMgmtSerialNumber,
       "hm2DeviceMgmtActionGroup": hm2DeviceMgmtActionGroup,
       "hm2DevMgmtActionReset": hm2DevMgmtActionReset,
       "hm2DevMgmtActionFlushFDB": hm2DevMgmtActionFlushFDB,
       "hm2DevMgmtActionFlushARP": hm2DevMgmtActionFlushARP,
       "hm2DevMgmtActionFlushIGS": hm2DevMgmtActionFlushIGS,
       "hm2DevMgmtActionFlushPortStats": hm2DevMgmtActionFlushPortStats,
       "hm2DevMgmtActionFlushEmailLogStats": hm2DevMgmtActionFlushEmailLogStats,
       "hm2DevMgmtActionFlushMMRP": hm2DevMgmtActionFlushMMRP,
       "hm2DevMgmtActionFlushMVRP": hm2DevMgmtActionFlushMVRP,
       "hm2DevMgmtActionFlushMSRP": hm2DevMgmtActionFlushMSRP,
       "hm2DevMgmtActionFlushIeee8021AS": hm2DevMgmtActionFlushIeee8021AS,
       "hm2DevMgmtActionFlushDnsClientCache": hm2DevMgmtActionFlushDnsClientCache,
       "hm2DevMgmtActionFlushDnsCachingServerCache": hm2DevMgmtActionFlushDnsCachingServerCache,
       "hm2DevMgmtActionFlushIpUdpHelperStats": hm2DevMgmtActionFlushIpUdpHelperStats,
       "hm2DevMgmtActionFlushAclStats": hm2DevMgmtActionFlushAclStats,
       "hm2DevMgmtActionFlushLdapUserCache": hm2DevMgmtActionFlushLdapUserCache,
       "hm2DevMgmtActionDelayPreset": hm2DevMgmtActionDelayPreset,
       "hm2DevMgmtActionDelayCurrent": hm2DevMgmtActionDelayCurrent,
       "hm2DeviceMgmtSoftwareGroup": hm2DeviceMgmtSoftwareGroup,
       "hm2DeviceMgmtSoftwareVersionGroup": hm2DeviceMgmtSoftwareVersionGroup,
       "hm2DevMgmtSwVersBootcode": hm2DevMgmtSwVersBootcode,
       "hm2DevMgmtSwVersTable": hm2DevMgmtSwVersTable,
       "hm2DevMgmtSwVersEntry": hm2DevMgmtSwVersEntry,
       "hm2DevMgmtSwFileLocation": hm2DevMgmtSwFileLocation,
       "hm2DevMgmtSwFileType": hm2DevMgmtSwFileType,
       "hm2DevMgmtSwFileIdx": hm2DevMgmtSwFileIdx,
       "hm2DevMgmtSwFileName": hm2DevMgmtSwFileName,
       "hm2DevMgmtSwVersion": hm2DevMgmtSwVersion,
       "hm2DevMgmtSwMajorRelNum": hm2DevMgmtSwMajorRelNum,
       "hm2DevMgmtSwMinorRelNum": hm2DevMgmtSwMinorRelNum,
       "hm2DevMgmtSwBugfixRelNum": hm2DevMgmtSwBugfixRelNum,
       "hm2DeviceMgmtHardwareGroup": hm2DeviceMgmtHardwareGroup,
       "hm2DevMgmtHwVersion": hm2DevMgmtHwVersion,
       "hm2DevMgmtSwitchingCoreVersion": hm2DevMgmtSwitchingCoreVersion,
       "hm2DeviceMgmtLogicVersionGroup": hm2DeviceMgmtLogicVersionGroup,
       "hm2DevMgmtLogicVersTable": hm2DevMgmtLogicVersTable,
       "hm2DevMgmtLogicVersEntry": hm2DevMgmtLogicVersEntry,
       "hm2DevMgmtLogicIdx": hm2DevMgmtLogicIdx,
       "hm2DevMgmtLogicAddress": hm2DevMgmtLogicAddress,
       "hm2DevMgmtLogicVersion": hm2DevMgmtLogicVersion,
       "hm2DeviceMgmtTemperatureGroup": hm2DeviceMgmtTemperatureGroup,
       "hm2DevMgmtTemperature": hm2DevMgmtTemperature,
       "hm2DevMgmtTemperatureUpperLimit": hm2DevMgmtTemperatureUpperLimit,
       "hm2DevMgmtTemperatureLowerLimit": hm2DevMgmtTemperatureLowerLimit,
       "hm2IfaceGroup": hm2IfaceGroup,
       "hm2IfaceTable": hm2IfaceTable,
       "hm2IfaceEntry": hm2IfaceEntry,
       "hm2IfacePhysIndex": hm2IfacePhysIndex,
       "hm2IfacePortCapabilityBits": hm2IfacePortCapabilityBits,
       "hm2IfaceCableCrossing": hm2IfaceCableCrossing,
       "hm2IfacePowerState": hm2IfacePowerState,
       "hm2IfaceAutoPowerDown": hm2IfaceAutoPowerDown,
       "hm2IfaceOperAdminStatus": hm2IfaceOperAdminStatus,
       "hm2IfaceLayoutTable": hm2IfaceLayoutTable,
       "hm2IfaceLayoutEntry": hm2IfaceLayoutEntry,
       "hm2IfaceLayoutIndex": hm2IfaceLayoutIndex,
       "hm2IfaceLayoutStartIfIndex": hm2IfaceLayoutStartIfIndex,
       "hm2IfaceLayoutEndIfIndex": hm2IfaceLayoutEndIfIndex,
       "hm2IfaceLayoutModuleCapacity": hm2IfaceLayoutModuleCapacity,
       "hm2IfaceLayoutModulePortCapacity": hm2IfaceLayoutModulePortCapacity,
       "hm2IfaceLayoutFormat": hm2IfaceLayoutFormat,
       "hm2IfaceLayoutIfIndexType": hm2IfaceLayoutIfIndexType,
       "hm2IfaceExtTable": hm2IfaceExtTable,
       "hm2IfaceExtEntry": hm2IfaceExtEntry,
       "hm2IfaceExtIfRole": hm2IfaceExtIfRole,
       "hm2SfpGroup": hm2SfpGroup,
       "hm2SfpInfoTable": hm2SfpInfoTable,
       "hm2SfpInfoEntry": hm2SfpInfoEntry,
       "hm2SfpModuleType": hm2SfpModuleType,
       "hm2SfpMediaType": hm2SfpMediaType,
       "hm2SfpConnector": hm2SfpConnector,
       "hm2SfpVendorName": hm2SfpVendorName,
       "hm2SfpVendorOUI": hm2SfpVendorOUI,
       "hm2SfpPartNumber": hm2SfpPartNumber,
       "hm2SfpPartRev": hm2SfpPartRev,
       "hm2SfpSerialNum": hm2SfpSerialNum,
       "hm2SfpDateCode": hm2SfpDateCode,
       "hm2SfpInfoVersion": hm2SfpInfoVersion,
       "hm2SfpInfoPartNumber": hm2SfpInfoPartNumber,
       "hm2SfpInfoPartId": hm2SfpInfoPartId,
       "hm2SfpBitRateNominal": hm2SfpBitRateNominal,
       "hm2SfpBitRateMin": hm2SfpBitRateMin,
       "hm2SfpBitRateMax": hm2SfpBitRateMax,
       "hm2SfpMaxLength-fiber-9": hm2SfpMaxLength_fiber_9,
       "hm2SfpMaxLength-fiber-50": hm2SfpMaxLength_fiber_50,
       "hm2SfpMaxLength-fiber-e50": hm2SfpMaxLength_fiber_e50,
       "hm2SfpMaxLength-fiber-62-5": hm2SfpMaxLength_fiber_62_5,
       "hm2SfpMaxLength-copper": hm2SfpMaxLength_copper,
       "hm2SfpWaveLength": hm2SfpWaveLength,
       "hm2SfpWaveLengthTolerance": hm2SfpWaveLengthTolerance,
       "hm2SfpEnhancedOptions": hm2SfpEnhancedOptions,
       "hm2SfpSupported": hm2SfpSupported,
       "hm2SfpSupportedReason": hm2SfpSupportedReason,
       "hm2SfpDiagTable": hm2SfpDiagTable,
       "hm2SfpDiagEntry": hm2SfpDiagEntry,
       "hm2SfpCurrentBitRate": hm2SfpCurrentBitRate,
       "hm2SfpCurrentTemperature": hm2SfpCurrentTemperature,
       "hm2SfpCurrentTxPower": hm2SfpCurrentTxPower,
       "hm2SfpCurrentRxPower": hm2SfpCurrentRxPower,
       "hm2SfpCurrentTxPowerdBm": hm2SfpCurrentTxPowerdBm,
       "hm2SfpCurrentRxPowerdBm": hm2SfpCurrentRxPowerdBm,
       "hm2SfpCurrentRxPowerState": hm2SfpCurrentRxPowerState,
       "hm2SfpWLGroup": hm2SfpWLGroup,
       "hm2SfpWLStatus": hm2SfpWLStatus,
       "hm2SfpThresholdTable": hm2SfpThresholdTable,
       "hm2SfpThresholdEntry": hm2SfpThresholdEntry,
       "hm2SfpTemperatureHighAlarm": hm2SfpTemperatureHighAlarm,
       "hm2SfpTemperatureHighWarning": hm2SfpTemperatureHighWarning,
       "hm2SfpTemperatureLowAlarm": hm2SfpTemperatureLowAlarm,
       "hm2SfpTemperatureLowWarning": hm2SfpTemperatureLowWarning,
       "hm2SfpTxPowerHighAlarm": hm2SfpTxPowerHighAlarm,
       "hm2SfpTxPowerHighWarning": hm2SfpTxPowerHighWarning,
       "hm2SfpTxPowerLowAlarm": hm2SfpTxPowerLowAlarm,
       "hm2SfpTxPowerLowWarning": hm2SfpTxPowerLowWarning,
       "hm2SfpRxPowerHighAlarm": hm2SfpRxPowerHighAlarm,
       "hm2SfpRxPowerHighWarning": hm2SfpRxPowerHighWarning,
       "hm2SfpRxPowerLowAlarm": hm2SfpRxPowerLowAlarm,
       "hm2SfpRxPowerLowWarning": hm2SfpRxPowerLowWarning,
       "hm2SfpTxPowerdBmHighAlarm": hm2SfpTxPowerdBmHighAlarm,
       "hm2SfpTxPowerdBmHighWarning": hm2SfpTxPowerdBmHighWarning,
       "hm2SfpTxPowerdBmLowAlarm": hm2SfpTxPowerdBmLowAlarm,
       "hm2SfpTxPowerdBmLowWarning": hm2SfpTxPowerdBmLowWarning,
       "hm2SfpRxPowerdBmHighAlarm": hm2SfpRxPowerdBmHighAlarm,
       "hm2SfpRxPowerdBmHighWarning": hm2SfpRxPowerdBmHighWarning,
       "hm2SfpRxPowerdBmLowAlarm": hm2SfpRxPowerdBmLowAlarm,
       "hm2SfpRxPowerdBmLowWarning": hm2SfpRxPowerdBmLowWarning,
       "hm2ExtNvmGroup": hm2ExtNvmGroup,
       "hm2ExtNvmGeneralGroup": hm2ExtNvmGeneralGroup,
       "hm2ExtNvmChooseActive": hm2ExtNvmChooseActive,
       "hm2ExtNvmLogDevice": hm2ExtNvmLogDevice,
       "hm2ExtNvmAdminMode": hm2ExtNvmAdminMode,
       "hm2ExtNvmOperMode": hm2ExtNvmOperMode,
       "hm2ExtNvmTable": hm2ExtNvmTable,
       "hm2ExtNvmEntry": hm2ExtNvmEntry,
       "hm2ExtNvmTableIndex": hm2ExtNvmTableIndex,
       "hm2ExtNvmStatus": hm2ExtNvmStatus,
       "hm2ExtNvmManufacturerId": hm2ExtNvmManufacturerId,
       "hm2ExtNvmHWRevision": hm2ExtNvmHWRevision,
       "hm2ExtNvmProductName": hm2ExtNvmProductName,
       "hm2ExtNvmVersion": hm2ExtNvmVersion,
       "hm2ExtNvmSerialNum": hm2ExtNvmSerialNum,
       "hm2ExtNvmAutomaticSoftwareLoad": hm2ExtNvmAutomaticSoftwareLoad,
       "hm2ExtNvmConfigLoadPriority": hm2ExtNvmConfigLoadPriority,
       "hm2ExtNvmConfigSave": hm2ExtNvmConfigSave,
       "hm2ExtNvmWritable": hm2ExtNvmWritable,
       "hm2ExtNvmAutomaticSshKeyLoad": hm2ExtNvmAutomaticSshKeyLoad,
       "hm2AutoDisableGroup": hm2AutoDisableGroup,
       "hm2AutoDisableIntfTable": hm2AutoDisableIntfTable,
       "hm2AutoDisableIntfEntry": hm2AutoDisableIntfEntry,
       "hm2AutoDisableIntfRemainingTime": hm2AutoDisableIntfRemainingTime,
       "hm2AutoDisableIntfComponentName": hm2AutoDisableIntfComponentName,
       "hm2AutoDisableIntfErrorReason": hm2AutoDisableIntfErrorReason,
       "hm2AutoDisableIntfTimer": hm2AutoDisableIntfTimer,
       "hm2AutoDisableIntfReset": hm2AutoDisableIntfReset,
       "hm2AutoDisableIntfOperState": hm2AutoDisableIntfOperState,
       "hm2AutoDisableIntfErrorTime": hm2AutoDisableIntfErrorTime,
       "hm2AutoDisableReasonTable": hm2AutoDisableReasonTable,
       "hm2AutoDisableReasonEntry": hm2AutoDisableReasonEntry,
       "hm2AutoDisableReasons": hm2AutoDisableReasons,
       "hm2AutoDisableReasonOperation": hm2AutoDisableReasonOperation,
       "hm2AutoDisableReasonCategory": hm2AutoDisableReasonCategory,
       "hm2UnitGroup": hm2UnitGroup,
       "hm2UnitTable": hm2UnitTable,
       "hm2UnitEntry": hm2UnitEntry,
       "hm2UnitIndex": hm2UnitIndex,
       "hm2UnitMaxModuleCapacity": hm2UnitMaxModuleCapacity,
       "hm2UnitMaxModulePortCapacity": hm2UnitMaxModulePortCapacity,
       "hm2ModuleGroup": hm2ModuleGroup,
       "hm2ModuleTable": hm2ModuleTable,
       "hm2ModuleEntry": hm2ModuleEntry,
       "hm2ModuleIndex": hm2ModuleIndex,
       "hm2ModuleId": hm2ModuleId,
       "hm2ModuleDescription": hm2ModuleDescription,
       "hm2ModuleProductCode": hm2ModuleProductCode,
       "hm2ModuleVersion": hm2ModuleVersion,
       "hm2ModuleNumOfPorts": hm2ModuleNumOfPorts,
       "hm2ModuleFirstMauIndex": hm2ModuleFirstMauIndex,
       "hm2ModuleStatus": hm2ModuleStatus,
       "hm2ModuleSerialNum": hm2ModuleSerialNum,
       "hm2ModuleMinSWVersion": hm2ModuleMinSWVersion,
       "hm2ModuleCapability": hm2ModuleCapability,
       "hm2ModuleInternalID": hm2ModuleInternalID,
       "hm2ModuleInternalIDVariant": hm2ModuleInternalIDVariant,
       "hm2ModuleFirstIfIndex": hm2ModuleFirstIfIndex,
       "hm2ModuleAdminState": hm2ModuleAdminState}
)
