# SNMP MIB module (HP-DOT1X-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-DOT1X-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:59 2024
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

(HpAutzUserRoleName,) = mibBuilder.importSymbols(
    "HP-AUTZ-MIB",
    "HpAutzUserRoleName")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(dot1xAuthConfigEntry,
 dot1xPaePortEntry,
 dot1xPaePortNumber,
 dot1xSuppConfigEntry) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthConfigEntry",
    "dot1xPaePortEntry",
    "dot1xPaePortNumber",
    "dot1xSuppConfigEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfDot1xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25)
)
hpicfDot1xMIB.setRevisions(
        ("2017-10-12 00:00",
         "2017-09-28 00:00",
         "2017-09-13 00:00",
         "2016-02-25 00:00",
         "2016-01-21 00:00",
         "2013-06-12 00:00",
         "2013-01-10 00:00",
         "2012-11-15 00:00",
         "2011-08-29 00:00",
         "2011-07-21 00:00",
         "2011-02-12 00:00",
         "2010-04-15 00:00",
         "2009-07-08 00:00",
         "2009-07-02 00:00",
         "2007-02-02 00:00",
         "2005-09-21 00:00",
         "2005-08-05 00:00",
         "2004-08-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDot1xMIBObjects_ObjectIdentity = ObjectIdentity
hpicfDot1xMIBObjects = _HpicfDot1xMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1)
)
_HpicfDot1xSystem_ObjectIdentity = ObjectIdentity
hpicfDot1xSystem = _HpicfDot1xSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1)
)
_HpicfDot1xPaePortTable_Object = MibTable
hpicfDot1xPaePortTable = _HpicfDot1xPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xPaePortTable.setStatus("current")
_HpicfDot1xPaePortEntry_Object = MibTableRow
hpicfDot1xPaePortEntry = _HpicfDot1xPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xPaePortEntry.setStatus("current")
_HpicfDot1xPaePortAuth_Type = TruthValue
_HpicfDot1xPaePortAuth_Object = MibTableColumn
hpicfDot1xPaePortAuth = _HpicfDot1xPaePortAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 1),
    _HpicfDot1xPaePortAuth_Type()
)
hpicfDot1xPaePortAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortAuth.setStatus("current")
_HpicfDot1xPaePortSupp_Type = TruthValue
_HpicfDot1xPaePortSupp_Object = MibTableColumn
hpicfDot1xPaePortSupp = _HpicfDot1xPaePortSupp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 2),
    _HpicfDot1xPaePortSupp_Type()
)
hpicfDot1xPaePortSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortSupp.setStatus("current")


class _HpicfDot1xPaePortMixed_Type(TruthValue):
    """Custom type hpicfDot1xPaePortMixed based on TruthValue"""


_HpicfDot1xPaePortMixed_Object = MibTableColumn
hpicfDot1xPaePortMixed = _HpicfDot1xPaePortMixed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 3),
    _HpicfDot1xPaePortMixed_Type()
)
hpicfDot1xPaePortMixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortMixed.setStatus("current")


class _HpicfDot1xPaePortSpeedVSA_Type(TruthValue):
    """Custom type hpicfDot1xPaePortSpeedVSA based on TruthValue"""


_HpicfDot1xPaePortSpeedVSA_Object = MibTableColumn
hpicfDot1xPaePortSpeedVSA = _HpicfDot1xPaePortSpeedVSA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 4),
    _HpicfDot1xPaePortSpeedVSA_Type()
)
hpicfDot1xPaePortSpeedVSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortSpeedVSA.setStatus("current")


class _HpicfDot1xPaePortMBV_Type(TruthValue):
    """Custom type hpicfDot1xPaePortMBV based on TruthValue"""


_HpicfDot1xPaePortMBV_Object = MibTableColumn
hpicfDot1xPaePortMBV = _HpicfDot1xPaePortMBV_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 5),
    _HpicfDot1xPaePortMBV_Type()
)
hpicfDot1xPaePortMBV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortMBV.setStatus("current")
_HpicfDot1xPaePortCritAuthVoiceVid_Type = VlanIndex
_HpicfDot1xPaePortCritAuthVoiceVid_Object = MibTableColumn
hpicfDot1xPaePortCritAuthVoiceVid = _HpicfDot1xPaePortCritAuthVoiceVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 6),
    _HpicfDot1xPaePortCritAuthVoiceVid_Type()
)
hpicfDot1xPaePortCritAuthVoiceVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortCritAuthVoiceVid.setStatus("current")
_HpicfDot1xPaePortCritAuthDataVid_Type = VlanIndex
_HpicfDot1xPaePortCritAuthDataVid_Object = MibTableColumn
hpicfDot1xPaePortCritAuthDataVid = _HpicfDot1xPaePortCritAuthDataVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 7),
    _HpicfDot1xPaePortCritAuthDataVid_Type()
)
hpicfDot1xPaePortCritAuthDataVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortCritAuthDataVid.setStatus("current")


class _HpicfDot1xPaePortCritAuthUserRole_Type(DisplayString):
    """Custom type hpicfDot1xPaePortCritAuthUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDot1xPaePortCritAuthUserRole_Type.__name__ = "DisplayString"
_HpicfDot1xPaePortCritAuthUserRole_Object = MibTableColumn
hpicfDot1xPaePortCritAuthUserRole = _HpicfDot1xPaePortCritAuthUserRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 8),
    _HpicfDot1xPaePortCritAuthUserRole_Type()
)
hpicfDot1xPaePortCritAuthUserRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortCritAuthUserRole.setStatus("current")
_HpicfDot1xPaePortOpenAuthVoiceVid_Type = VlanIndex
_HpicfDot1xPaePortOpenAuthVoiceVid_Object = MibTableColumn
hpicfDot1xPaePortOpenAuthVoiceVid = _HpicfDot1xPaePortOpenAuthVoiceVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 9),
    _HpicfDot1xPaePortOpenAuthVoiceVid_Type()
)
hpicfDot1xPaePortOpenAuthVoiceVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortOpenAuthVoiceVid.setStatus("current")
_HpicfDot1xPaePortOpenAuthDataVid_Type = VlanIndex
_HpicfDot1xPaePortOpenAuthDataVid_Object = MibTableColumn
hpicfDot1xPaePortOpenAuthDataVid = _HpicfDot1xPaePortOpenAuthDataVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 10),
    _HpicfDot1xPaePortOpenAuthDataVid_Type()
)
hpicfDot1xPaePortOpenAuthDataVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortOpenAuthDataVid.setStatus("current")


class _HpicfDot1xPaePortOpenAuthUserRole_Type(DisplayString):
    """Custom type hpicfDot1xPaePortOpenAuthUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDot1xPaePortOpenAuthUserRole_Type.__name__ = "DisplayString"
_HpicfDot1xPaePortOpenAuthUserRole_Object = MibTableColumn
hpicfDot1xPaePortOpenAuthUserRole = _HpicfDot1xPaePortOpenAuthUserRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 11),
    _HpicfDot1xPaePortOpenAuthUserRole_Type()
)
hpicfDot1xPaePortOpenAuthUserRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortOpenAuthUserRole.setStatus("current")


class _HpicfDot1xPaePortInitialRole_Type(DisplayString):
    """Custom type hpicfDot1xPaePortInitialRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDot1xPaePortInitialRole_Type.__name__ = "DisplayString"
_HpicfDot1xPaePortInitialRole_Object = MibTableColumn
hpicfDot1xPaePortInitialRole = _HpicfDot1xPaePortInitialRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 1, 1, 12),
    _HpicfDot1xPaePortInitialRole_Type()
)
hpicfDot1xPaePortInitialRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xPaePortInitialRole.setStatus("current")


class _HpicfDot1x2010_Type(Integer32):
    """Custom type hpicfDot1x2010 based on Integer32"""
    defaultValue = 0

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
        *(("authenticator", 1),
          ("authenticatorAndSupplicant", 3),
          ("disabled", 0),
          ("supplicant", 2))
    )


_HpicfDot1x2010_Type.__name__ = "Integer32"
_HpicfDot1x2010_Object = MibScalar
hpicfDot1x2010 = _HpicfDot1x2010_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 1, 2),
    _HpicfDot1x2010_Type()
)
hpicfDot1x2010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1x2010.setStatus("current")
_HpicfDot1xAuthenticator_ObjectIdentity = ObjectIdentity
hpicfDot1xAuthenticator = _HpicfDot1xAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2)
)
_HpicfDot1xAuthConfigTable_Object = MibTable
hpicfDot1xAuthConfigTable = _HpicfDot1xAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigTable.setStatus("current")
_HpicfDot1xAuthConfigEntry_Object = MibTableRow
hpicfDot1xAuthConfigEntry = _HpicfDot1xAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigEntry.setStatus("current")
_HpicfDot1xAuthAuthVid_Type = VlanIndex
_HpicfDot1xAuthAuthVid_Object = MibTableColumn
hpicfDot1xAuthAuthVid = _HpicfDot1xAuthAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 1),
    _HpicfDot1xAuthAuthVid_Type()
)
hpicfDot1xAuthAuthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthAuthVid.setStatus("current")
_HpicfDot1xAuthUnauthVid_Type = VlanIndex
_HpicfDot1xAuthUnauthVid_Object = MibTableColumn
hpicfDot1xAuthUnauthVid = _HpicfDot1xAuthUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 2),
    _HpicfDot1xAuthUnauthVid_Type()
)
hpicfDot1xAuthUnauthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthUnauthVid.setStatus("current")


class _HpicfDot1xAuthUnauthPeriod_Type(Unsigned32):
    """Custom type hpicfDot1xAuthUnauthPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfDot1xAuthUnauthPeriod_Type.__name__ = "Unsigned32"
_HpicfDot1xAuthUnauthPeriod_Object = MibTableColumn
hpicfDot1xAuthUnauthPeriod = _HpicfDot1xAuthUnauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 3),
    _HpicfDot1xAuthUnauthPeriod_Type()
)
hpicfDot1xAuthUnauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthUnauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDot1xAuthUnauthPeriod.setUnits("seconds")


class _HpicfDot1xAuthClientLimit_Type(Unsigned32):
    """Custom type hpicfDot1xAuthClientLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpicfDot1xAuthClientLimit_Type.__name__ = "Unsigned32"
_HpicfDot1xAuthClientLimit_Object = MibTableColumn
hpicfDot1xAuthClientLimit = _HpicfDot1xAuthClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 4),
    _HpicfDot1xAuthClientLimit_Type()
)
hpicfDot1xAuthClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthClientLimit.setStatus("deprecated")


class _HpicfDot1xAuthLogoffPeriod_Type(Unsigned32):
    """Custom type hpicfDot1xAuthLogoffPeriod based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999999),
    )


_HpicfDot1xAuthLogoffPeriod_Type.__name__ = "Unsigned32"
_HpicfDot1xAuthLogoffPeriod_Object = MibTableColumn
hpicfDot1xAuthLogoffPeriod = _HpicfDot1xAuthLogoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 5),
    _HpicfDot1xAuthLogoffPeriod_Type()
)
hpicfDot1xAuthLogoffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthLogoffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDot1xAuthLogoffPeriod.setUnits("seconds")


class _HpicfDot1xAuthClientLimit2_Type(Unsigned32):
    """Custom type hpicfDot1xAuthClientLimit2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HpicfDot1xAuthClientLimit2_Type.__name__ = "Unsigned32"
_HpicfDot1xAuthClientLimit2_Object = MibTableColumn
hpicfDot1xAuthClientLimit2 = _HpicfDot1xAuthClientLimit2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 6),
    _HpicfDot1xAuthClientLimit2_Type()
)
hpicfDot1xAuthClientLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthClientLimit2.setStatus("current")


class _HpicfDot1xAuthCachedReauthPeriod_Type(Unsigned32):
    """Custom type hpicfDot1xAuthCachedReauthPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfDot1xAuthCachedReauthPeriod_Type.__name__ = "Unsigned32"
_HpicfDot1xAuthCachedReauthPeriod_Object = MibTableColumn
hpicfDot1xAuthCachedReauthPeriod = _HpicfDot1xAuthCachedReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 7),
    _HpicfDot1xAuthCachedReauthPeriod_Type()
)
hpicfDot1xAuthCachedReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthCachedReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDot1xAuthCachedReauthPeriod.setUnits("seconds")


class _HpicfDot1xAuthEnforceCacheReauth_Type(TruthValue):
    """Custom type hpicfDot1xAuthEnforceCacheReauth based on TruthValue"""


_HpicfDot1xAuthEnforceCacheReauth_Object = MibTableColumn
hpicfDot1xAuthEnforceCacheReauth = _HpicfDot1xAuthEnforceCacheReauth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 1, 1, 8),
    _HpicfDot1xAuthEnforceCacheReauth_Type()
)
hpicfDot1xAuthEnforceCacheReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEnforceCacheReauth.setStatus("current")
_HpicfDot1xSMAuthConfigTable_Object = MibTable
hpicfDot1xSMAuthConfigTable = _HpicfDot1xSMAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthConfigTable.setStatus("current")
_HpicfDot1xSMAuthConfigEntry_Object = MibTableRow
hpicfDot1xSMAuthConfigEntry = _HpicfDot1xSMAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1)
)
hpicfDot1xSMAuthConfigEntry.setIndexNames(
    (0, "HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthPaePort"),
    (0, "HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthConfigEntry.setStatus("current")
_HpicfDot1xSMAuthPaePort_Type = InterfaceIndex
_HpicfDot1xSMAuthPaePort_Object = MibTableColumn
hpicfDot1xSMAuthPaePort = _HpicfDot1xSMAuthPaePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 1),
    _HpicfDot1xSMAuthPaePort_Type()
)
hpicfDot1xSMAuthPaePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthPaePort.setStatus("current")
_HpicfDot1xSMAuthMacAddr_Type = MacAddress
_HpicfDot1xSMAuthMacAddr_Object = MibTableColumn
hpicfDot1xSMAuthMacAddr = _HpicfDot1xSMAuthMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 2),
    _HpicfDot1xSMAuthMacAddr_Type()
)
hpicfDot1xSMAuthMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthMacAddr.setStatus("current")
_HpicfDot1xSMAuthInitialize_Type = TruthValue
_HpicfDot1xSMAuthInitialize_Object = MibTableColumn
hpicfDot1xSMAuthInitialize = _HpicfDot1xSMAuthInitialize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 3),
    _HpicfDot1xSMAuthInitialize_Type()
)
hpicfDot1xSMAuthInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthInitialize.setStatus("current")
_HpicfDot1xSMAuthReauthenticate_Type = TruthValue
_HpicfDot1xSMAuthReauthenticate_Object = MibTableColumn
hpicfDot1xSMAuthReauthenticate = _HpicfDot1xSMAuthReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 4),
    _HpicfDot1xSMAuthReauthenticate_Type()
)
hpicfDot1xSMAuthReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthReauthenticate.setStatus("current")


class _HpicfDot1xSMAuthPaeState_Type(Integer32):
    """Custom type hpicfDot1xSMAuthPaeState based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("criticalAuth", 16),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("heldInitialRoleFailed", 15),
          ("heldNoVlan", 11),
          ("heldUnauthVlan", 12),
          ("initialRole", 14),
          ("initialize", 1),
          ("openAuth", 17),
          ("restart", 10))
    )


_HpicfDot1xSMAuthPaeState_Type.__name__ = "Integer32"
_HpicfDot1xSMAuthPaeState_Object = MibTableColumn
hpicfDot1xSMAuthPaeState = _HpicfDot1xSMAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 5),
    _HpicfDot1xSMAuthPaeState_Type()
)
hpicfDot1xSMAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthPaeState.setStatus("current")


class _HpicfDot1xSMAuthBackendAuthState_Type(Integer32):
    """Custom type hpicfDot1xSMAuthBackendAuthState based on Integer32"""
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
        *(("applyInitialRole", 9),
          ("fail", 4),
          ("idle", 6),
          ("ignore", 8),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_HpicfDot1xSMAuthBackendAuthState_Type.__name__ = "Integer32"
_HpicfDot1xSMAuthBackendAuthState_Object = MibTableColumn
hpicfDot1xSMAuthBackendAuthState = _HpicfDot1xSMAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 6),
    _HpicfDot1xSMAuthBackendAuthState_Type()
)
hpicfDot1xSMAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthBackendAuthState.setStatus("current")


class _HpicfDot1xSMAuthReAuthPeriod_Type(Unsigned32):
    """Custom type hpicfDot1xSMAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_HpicfDot1xSMAuthReAuthPeriod_Object = MibTableColumn
hpicfDot1xSMAuthReAuthPeriod = _HpicfDot1xSMAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 7),
    _HpicfDot1xSMAuthReAuthPeriod_Type()
)
hpicfDot1xSMAuthReAuthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthReAuthPeriod.setStatus("current")


class _HpicfDot1xSMAuthReAuthEnabled_Type(TruthValue):
    """Custom type hpicfDot1xSMAuthReAuthEnabled based on TruthValue"""


_HpicfDot1xSMAuthReAuthEnabled_Object = MibTableColumn
hpicfDot1xSMAuthReAuthEnabled = _HpicfDot1xSMAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 8),
    _HpicfDot1xSMAuthReAuthEnabled_Type()
)
hpicfDot1xSMAuthReAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthReAuthEnabled.setStatus("current")


class _HpicfDot1xSMAuthSessionTimeout_Type(Unsigned32):
    """Custom type hpicfDot1xSMAuthSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfDot1xSMAuthSessionTimeout_Type.__name__ = "Unsigned32"
_HpicfDot1xSMAuthSessionTimeout_Object = MibTableColumn
hpicfDot1xSMAuthSessionTimeout = _HpicfDot1xSMAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 2, 1, 9),
    _HpicfDot1xSMAuthSessionTimeout_Type()
)
hpicfDot1xSMAuthSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthSessionTimeout.setUnits("seconds")
_HpicfDot1xAuthDiagTable_Object = MibTable
hpicfDot1xAuthDiagTable = _HpicfDot1xAuthDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthDiagTable.setStatus("current")
_HpicfDot1xAuthDiagEntry_Object = MibTableRow
hpicfDot1xAuthDiagEntry = _HpicfDot1xAuthDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 3, 1)
)
hpicfDot1xAuthDiagEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthDiagEntry.setStatus("current")
_HpicfDot1xAuthNumberOfSuccessAuthentication_Type = Counter32
_HpicfDot1xAuthNumberOfSuccessAuthentication_Object = MibTableColumn
hpicfDot1xAuthNumberOfSuccessAuthentication = _HpicfDot1xAuthNumberOfSuccessAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 3, 1, 1),
    _HpicfDot1xAuthNumberOfSuccessAuthentication_Type()
)
hpicfDot1xAuthNumberOfSuccessAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthNumberOfSuccessAuthentication.setStatus("current")
_HpicfDot1xAuthNumberOfFailedAuthentication_Type = Counter32
_HpicfDot1xAuthNumberOfFailedAuthentication_Object = MibTableColumn
hpicfDot1xAuthNumberOfFailedAuthentication = _HpicfDot1xAuthNumberOfFailedAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 3, 1, 2),
    _HpicfDot1xAuthNumberOfFailedAuthentication_Type()
)
hpicfDot1xAuthNumberOfFailedAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthNumberOfFailedAuthentication.setStatus("current")
_HpicfDot1xAuthStatsTable_Object = MibTable
hpicfDot1xAuthStatsTable = _HpicfDot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthStatsTable.setStatus("current")
_HpicfDot1xAuthStatsEntry_Object = MibTableRow
hpicfDot1xAuthStatsEntry = _HpicfDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1)
)
hpicfDot1xAuthStatsEntry.setIndexNames(
    (0, "HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthPaePort"),
    (0, "HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthStatsEntry.setStatus("current")
_HpicfDot1xAuthEapolFramesRx_Type = Counter32
_HpicfDot1xAuthEapolFramesRx_Object = MibTableColumn
hpicfDot1xAuthEapolFramesRx = _HpicfDot1xAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 1),
    _HpicfDot1xAuthEapolFramesRx_Type()
)
hpicfDot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolFramesRx.setStatus("current")
_HpicfDot1xAuthEapolFramesTx_Type = Counter32
_HpicfDot1xAuthEapolFramesTx_Object = MibTableColumn
hpicfDot1xAuthEapolFramesTx = _HpicfDot1xAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 2),
    _HpicfDot1xAuthEapolFramesTx_Type()
)
hpicfDot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolFramesTx.setStatus("current")
_HpicfDot1xAuthEapolStartFramesRx_Type = Counter32
_HpicfDot1xAuthEapolStartFramesRx_Object = MibTableColumn
hpicfDot1xAuthEapolStartFramesRx = _HpicfDot1xAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 3),
    _HpicfDot1xAuthEapolStartFramesRx_Type()
)
hpicfDot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolStartFramesRx.setStatus("current")
_HpicfDot1xAuthEapolLogoffFramesRx_Type = Counter32
_HpicfDot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
hpicfDot1xAuthEapolLogoffFramesRx = _HpicfDot1xAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 4),
    _HpicfDot1xAuthEapolLogoffFramesRx_Type()
)
hpicfDot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolLogoffFramesRx.setStatus("current")
_HpicfDot1xAuthEapolRespIdFramesRx_Type = Counter32
_HpicfDot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
hpicfDot1xAuthEapolRespIdFramesRx = _HpicfDot1xAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 5),
    _HpicfDot1xAuthEapolRespIdFramesRx_Type()
)
hpicfDot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolRespIdFramesRx.setStatus("current")
_HpicfDot1xAuthEapolRespFramesRx_Type = Counter32
_HpicfDot1xAuthEapolRespFramesRx_Object = MibTableColumn
hpicfDot1xAuthEapolRespFramesRx = _HpicfDot1xAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 6),
    _HpicfDot1xAuthEapolRespFramesRx_Type()
)
hpicfDot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolRespFramesRx.setStatus("current")
_HpicfDot1xAuthEapolReqIdFramesTx_Type = Counter32
_HpicfDot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
hpicfDot1xAuthEapolReqIdFramesTx = _HpicfDot1xAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 7),
    _HpicfDot1xAuthEapolReqIdFramesTx_Type()
)
hpicfDot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolReqIdFramesTx.setStatus("current")
_HpicfDot1xAuthEapolReqFramesTx_Type = Counter32
_HpicfDot1xAuthEapolReqFramesTx_Object = MibTableColumn
hpicfDot1xAuthEapolReqFramesTx = _HpicfDot1xAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 8),
    _HpicfDot1xAuthEapolReqFramesTx_Type()
)
hpicfDot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapolReqFramesTx.setStatus("current")
_HpicfDot1xAuthInvalidEapolFramesRx_Type = Counter32
_HpicfDot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
hpicfDot1xAuthInvalidEapolFramesRx = _HpicfDot1xAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 9),
    _HpicfDot1xAuthInvalidEapolFramesRx_Type()
)
hpicfDot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthInvalidEapolFramesRx.setStatus("current")
_HpicfDot1xAuthEapLengthErrorFramesRx_Type = Counter32
_HpicfDot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
hpicfDot1xAuthEapLengthErrorFramesRx = _HpicfDot1xAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 10),
    _HpicfDot1xAuthEapLengthErrorFramesRx_Type()
)
hpicfDot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthEapLengthErrorFramesRx.setStatus("current")
_HpicfDot1xAuthLastEapolFrameVersion_Type = Unsigned32
_HpicfDot1xAuthLastEapolFrameVersion_Object = MibTableColumn
hpicfDot1xAuthLastEapolFrameVersion = _HpicfDot1xAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 11),
    _HpicfDot1xAuthLastEapolFrameVersion_Type()
)
hpicfDot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthLastEapolFrameVersion.setStatus("current")
_HpicfDot1xAuthLastEapolFrameSource_Type = MacAddress
_HpicfDot1xAuthLastEapolFrameSource_Object = MibTableColumn
hpicfDot1xAuthLastEapolFrameSource = _HpicfDot1xAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 4, 1, 12),
    _HpicfDot1xAuthLastEapolFrameSource_Type()
)
hpicfDot1xAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthLastEapolFrameSource.setStatus("current")
_HpicfDot1xAuthSessionStatsTable_Object = MibTable
hpicfDot1xAuthSessionStatsTable = _HpicfDot1xAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionStatsTable.setStatus("current")
_HpicfDot1xAuthSessionStatsEntry_Object = MibTableRow
hpicfDot1xAuthSessionStatsEntry = _HpicfDot1xAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1)
)
hpicfDot1xAuthSessionStatsEntry.setIndexNames(
    (0, "HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthPaePort"),
    (0, "HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionStatsEntry.setStatus("current")
_HpicfDot1xAuthSessionPerPAECountersEnabled_Type = TruthValue
_HpicfDot1xAuthSessionPerPAECountersEnabled_Object = MibTableColumn
hpicfDot1xAuthSessionPerPAECountersEnabled = _HpicfDot1xAuthSessionPerPAECountersEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 1),
    _HpicfDot1xAuthSessionPerPAECountersEnabled_Type()
)
hpicfDot1xAuthSessionPerPAECountersEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionPerPAECountersEnabled.setStatus("current")
_HpicfDot1xAuthSessionOctetsRx_Type = Counter64
_HpicfDot1xAuthSessionOctetsRx_Object = MibTableColumn
hpicfDot1xAuthSessionOctetsRx = _HpicfDot1xAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 2),
    _HpicfDot1xAuthSessionOctetsRx_Type()
)
hpicfDot1xAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionOctetsRx.setStatus("current")
_HpicfDot1xAuthSessionOctetsTx_Type = Counter64
_HpicfDot1xAuthSessionOctetsTx_Object = MibTableColumn
hpicfDot1xAuthSessionOctetsTx = _HpicfDot1xAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 3),
    _HpicfDot1xAuthSessionOctetsTx_Type()
)
hpicfDot1xAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionOctetsTx.setStatus("current")
_HpicfDot1xAuthSessionFramesRx_Type = Counter32
_HpicfDot1xAuthSessionFramesRx_Object = MibTableColumn
hpicfDot1xAuthSessionFramesRx = _HpicfDot1xAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 4),
    _HpicfDot1xAuthSessionFramesRx_Type()
)
hpicfDot1xAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionFramesRx.setStatus("current")
_HpicfDot1xAuthSessionFramesTx_Type = Counter32
_HpicfDot1xAuthSessionFramesTx_Object = MibTableColumn
hpicfDot1xAuthSessionFramesTx = _HpicfDot1xAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 5),
    _HpicfDot1xAuthSessionFramesTx_Type()
)
hpicfDot1xAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionFramesTx.setStatus("current")
_HpicfDot1xAuthSessionId_Type = SnmpAdminString
_HpicfDot1xAuthSessionId_Object = MibTableColumn
hpicfDot1xAuthSessionId = _HpicfDot1xAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 6),
    _HpicfDot1xAuthSessionId_Type()
)
hpicfDot1xAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionId.setStatus("current")


class _HpicfDot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type hpicfDot1xAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("localandremoteAuthServer", 3),
          ("remoteAuthServer", 1))
    )


_HpicfDot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_HpicfDot1xAuthSessionAuthenticMethod_Object = MibTableColumn
hpicfDot1xAuthSessionAuthenticMethod = _HpicfDot1xAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 7),
    _HpicfDot1xAuthSessionAuthenticMethod_Type()
)
hpicfDot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionAuthenticMethod.setStatus("current")
_HpicfDot1xAuthSessionTime_Type = TimeTicks
_HpicfDot1xAuthSessionTime_Object = MibTableColumn
hpicfDot1xAuthSessionTime = _HpicfDot1xAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 8),
    _HpicfDot1xAuthSessionTime_Type()
)
hpicfDot1xAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionTime.setStatus("current")
_HpicfDot1xAuthSessionStartTime_Type = TimeStamp
_HpicfDot1xAuthSessionStartTime_Object = MibTableColumn
hpicfDot1xAuthSessionStartTime = _HpicfDot1xAuthSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 9),
    _HpicfDot1xAuthSessionStartTime_Type()
)
hpicfDot1xAuthSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionStartTime.setStatus("current")
_HpicfDot1xAuthSessionStopTime_Type = TimeStamp
_HpicfDot1xAuthSessionStopTime_Object = MibTableColumn
hpicfDot1xAuthSessionStopTime = _HpicfDot1xAuthSessionStopTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 10),
    _HpicfDot1xAuthSessionStopTime_Type()
)
hpicfDot1xAuthSessionStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionStopTime.setStatus("current")
_HpicfDot1xAuthSessionInactiveTime_Type = TimeTicks
_HpicfDot1xAuthSessionInactiveTime_Object = MibTableColumn
hpicfDot1xAuthSessionInactiveTime = _HpicfDot1xAuthSessionInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 11),
    _HpicfDot1xAuthSessionInactiveTime_Type()
)
hpicfDot1xAuthSessionInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionInactiveTime.setStatus("current")


class _HpicfDot1xAuthSessionTerminateCause_Type(Integer32):
    """Custom type hpicfDot1xAuthSessionTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 5),
          ("notTerminatedYet", 999),
          ("portAdminDisabled", 7),
          ("portFailure", 2),
          ("portReInit", 6),
          ("reauthFailed", 4),
          ("supplicantLogoff", 1),
          ("supplicantRestart", 3))
    )


_HpicfDot1xAuthSessionTerminateCause_Type.__name__ = "Integer32"
_HpicfDot1xAuthSessionTerminateCause_Object = MibTableColumn
hpicfDot1xAuthSessionTerminateCause = _HpicfDot1xAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 12),
    _HpicfDot1xAuthSessionTerminateCause_Type()
)
hpicfDot1xAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionTerminateCause.setStatus("current")
_HpicfDot1xAuthSessionUserName_Type = SnmpAdminString
_HpicfDot1xAuthSessionUserName_Object = MibTableColumn
hpicfDot1xAuthSessionUserName = _HpicfDot1xAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 13),
    _HpicfDot1xAuthSessionUserName_Type()
)
hpicfDot1xAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionUserName.setStatus("current")
_HpicfDot1xAuthSessionIsForwarding_Type = TruthValue
_HpicfDot1xAuthSessionIsForwarding_Object = MibTableColumn
hpicfDot1xAuthSessionIsForwarding = _HpicfDot1xAuthSessionIsForwarding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 14),
    _HpicfDot1xAuthSessionIsForwarding_Type()
)
hpicfDot1xAuthSessionIsForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionIsForwarding.setStatus("current")
_HpicfDot1xAuthSessionVid_Type = VlanIndex
_HpicfDot1xAuthSessionVid_Object = MibTableColumn
hpicfDot1xAuthSessionVid = _HpicfDot1xAuthSessionVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 15),
    _HpicfDot1xAuthSessionVid_Type()
)
hpicfDot1xAuthSessionVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionVid.setStatus("current")
_HpicfDot1xAuthSessionRoleName_Type = HpAutzUserRoleName
_HpicfDot1xAuthSessionRoleName_Object = MibTableColumn
hpicfDot1xAuthSessionRoleName = _HpicfDot1xAuthSessionRoleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 5, 1, 16),
    _HpicfDot1xAuthSessionRoleName_Type()
)
hpicfDot1xAuthSessionRoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionRoleName.setStatus("current")
_HpicfDot1xAuthAllowGvrpVlans_Type = TruthValue
_HpicfDot1xAuthAllowGvrpVlans_Object = MibScalar
hpicfDot1xAuthAllowGvrpVlans = _HpicfDot1xAuthAllowGvrpVlans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 6),
    _HpicfDot1xAuthAllowGvrpVlans_Type()
)
hpicfDot1xAuthAllowGvrpVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthAllowGvrpVlans.setStatus("current")


class _HpicfDot1xAuthCachedReauthDelay_Type(Unsigned32):
    """Custom type hpicfDot1xAuthCachedReauthDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfDot1xAuthCachedReauthDelay_Type.__name__ = "Unsigned32"
_HpicfDot1xAuthCachedReauthDelay_Object = MibScalar
hpicfDot1xAuthCachedReauthDelay = _HpicfDot1xAuthCachedReauthDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 2, 7),
    _HpicfDot1xAuthCachedReauthDelay_Type()
)
hpicfDot1xAuthCachedReauthDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xAuthCachedReauthDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDot1xAuthCachedReauthDelay.setUnits("seconds")
_HpicfDot1xSupplicant_ObjectIdentity = ObjectIdentity
hpicfDot1xSupplicant = _HpicfDot1xSupplicant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 3)
)
_HpicfDot1xSuppConfigTable_Object = MibTable
hpicfDot1xSuppConfigTable = _HpicfDot1xSuppConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xSuppConfigTable.setStatus("current")
_HpicfDot1xSuppConfigEntry_Object = MibTableRow
hpicfDot1xSuppConfigEntry = _HpicfDot1xSuppConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xSuppConfigEntry.setStatus("current")


class _HpicfDot1xSuppConfigIdentity_Type(DisplayString):
    """Custom type hpicfDot1xSuppConfigIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDot1xSuppConfigIdentity_Type.__name__ = "DisplayString"
_HpicfDot1xSuppConfigIdentity_Object = MibTableColumn
hpicfDot1xSuppConfigIdentity = _HpicfDot1xSuppConfigIdentity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 3, 1, 1, 1),
    _HpicfDot1xSuppConfigIdentity_Type()
)
hpicfDot1xSuppConfigIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xSuppConfigIdentity.setStatus("current")


class _HpicfDot1xSuppConfigPassword_Type(DisplayString):
    """Custom type hpicfDot1xSuppConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDot1xSuppConfigPassword_Type.__name__ = "DisplayString"
_HpicfDot1xSuppConfigPassword_Object = MibTableColumn
hpicfDot1xSuppConfigPassword = _HpicfDot1xSuppConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 3, 1, 1, 2),
    _HpicfDot1xSuppConfigPassword_Type()
)
hpicfDot1xSuppConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xSuppConfigPassword.setStatus("current")


class _HpicfDot1xSuppConfigPasswordEncrypted_Type(OctetString):
    """Custom type hpicfDot1xSuppConfigPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfDot1xSuppConfigPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfDot1xSuppConfigPasswordEncrypted_Object = MibTableColumn
hpicfDot1xSuppConfigPasswordEncrypted = _HpicfDot1xSuppConfigPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 1, 3, 1, 1, 3),
    _HpicfDot1xSuppConfigPasswordEncrypted_Type()
)
hpicfDot1xSuppConfigPasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDot1xSuppConfigPasswordEncrypted.setStatus("current")
_HpicfDot1xConformance_ObjectIdentity = ObjectIdentity
hpicfDot1xConformance = _HpicfDot1xConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2)
)
_HpicfDot1xGroups_ObjectIdentity = ObjectIdentity
hpicfDot1xGroups = _HpicfDot1xGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1)
)
_HpicfDot1xCompliances_ObjectIdentity = ObjectIdentity
hpicfDot1xCompliances = _HpicfDot1xCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2)
)
dot1xPaePortEntry.registerAugmentions(
    ("HP-DOT1X-EXTENSIONS-MIB",
     "hpicfDot1xPaePortEntry")
)
hpicfDot1xPaePortEntry.setIndexNames(*dot1xPaePortEntry.getIndexNames())
dot1xAuthConfigEntry.registerAugmentions(
    ("HP-DOT1X-EXTENSIONS-MIB",
     "hpicfDot1xAuthConfigEntry")
)
hpicfDot1xAuthConfigEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
dot1xSuppConfigEntry.registerAugmentions(
    ("HP-DOT1X-EXTENSIONS-MIB",
     "hpicfDot1xSuppConfigEntry")
)
hpicfDot1xSuppConfigEntry.setIndexNames(*dot1xSuppConfigEntry.getIndexNames())

# Managed Objects groups

hpicfDot1xPaePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 1)
)
hpicfDot1xPaePortGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortAuth"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortSupp"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortMBV"))
)
if mibBuilder.loadTexts:
    hpicfDot1xPaePortGroup.setStatus("current")

hpicfDot1xAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 2)
)
hpicfDot1xAuthConfigGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAuthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthClientLimit"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLogoffPeriod"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigGroup.setStatus("deprecated")

hpicfDot1xSMAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 3)
)
hpicfDot1xSMAuthConfigGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthInitialize"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthReauthenticate"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthPaeState"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthBackendAuthState"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthReAuthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthReAuthEnabled"))
)
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthConfigGroup.setStatus("current")

hpicfDot1xAuthDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 4)
)
hpicfDot1xAuthDiagGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthNumberOfSuccessAuthentication"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthNumberOfFailedAuthentication"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthDiagGroup.setStatus("current")

hpicfDot1xAuthStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 5)
)
hpicfDot1xAuthStatsGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolFramesTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolStartFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolLogoffFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolRespIdFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolRespFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolReqIdFramesTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapolReqFramesTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthInvalidEapolFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthEapLengthErrorFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLastEapolFrameVersion"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLastEapolFrameSource"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthStatsGroup.setStatus("current")

hpicfDot1xAuthSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 6)
)
hpicfDot1xAuthSessionStatsGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionOctetsRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionOctetsTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionFramesTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionId"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionAuthenticMethod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionStartTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionStopTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionInactiveTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionTerminateCause"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionUserName"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionIsForwarding"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionVid"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionStatsGroup.setStatus("deprecated")

hpicfDot1xAuthConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 7)
)
hpicfDot1xAuthConfigGroup2.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAuthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLogoffPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthClientLimit2"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigGroup2.setStatus("current")

hpicfDot1xAuthConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 8)
)
hpicfDot1xAuthConfigGroup3.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAuthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLogoffPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthClientLimit2"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAllowGvrpVlans"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigGroup3.setStatus("current")

hpicfDot1xAuthConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 9)
)
hpicfDot1xAuthConfigGroup4.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAuthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLogoffPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthClientLimit2"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAllowGvrpVlans"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthCachedReauthPeriod"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigGroup4.setStatus("deprecated")

hpicfDot1xAuthConfigGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 10)
)
hpicfDot1xAuthConfigGroup5.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAuthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthUnauthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthLogoffPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthClientLimit2"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthAllowGvrpVlans"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthCachedReauthPeriod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthCachedReauthDelay"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthConfigGroup5.setStatus("current")

hpicfDot1xSuppConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 11)
)
hpicfDot1xSuppConfigGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSuppConfigIdentity"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSuppConfigPassword"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSuppConfigPasswordEncrypted"))
)
if mibBuilder.loadTexts:
    hpicfDot1xSuppConfigGroup.setStatus("current")

hpicfDot1xPaeAuthSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 12)
)
hpicfDot1xPaeAuthSessionGroup.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthMacAddr"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortMixed"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionPerPAECountersEnabled"))
)
if mibBuilder.loadTexts:
    hpicfDot1xPaeAuthSessionGroup.setStatus("deprecated")

hpicfDot1xSMAuthSessionTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 13)
)
hpicfDot1xSMAuthSessionTimeoutGroup.setObjects(
    ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthSessionTimeout")
)
if mibBuilder.loadTexts:
    hpicfDot1xSMAuthSessionTimeoutGroup.setStatus("current")

hpicfDot1xPaeAuthSessionGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 14)
)
hpicfDot1xPaeAuthSessionGroup1.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xSMAuthMacAddr"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortMixed"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortSpeedVSA"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionPerPAECountersEnabled"))
)
if mibBuilder.loadTexts:
    hpicfDot1xPaeAuthSessionGroup1.setStatus("current")

hpicfDot1xAuthSessionStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 18)
)
hpicfDot1xAuthSessionStatsGroup1.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionOctetsRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionOctetsTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionFramesRx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionFramesTx"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionId"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionAuthenticMethod"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionStartTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionStopTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionInactiveTime"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionTerminateCause"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionUserName"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionIsForwarding"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xAuthSessionRoleName"))
)
if mibBuilder.loadTexts:
    hpicfDot1xAuthSessionStatsGroup1.setStatus("current")

hpicfDot1xSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 19)
)
hpicfDot1xSystemGroup.setObjects(
    ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1x2010")
)
if mibBuilder.loadTexts:
    hpicfDot1xSystemGroup.setStatus("current")

hpicfDot1xPaePortGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 1, 20)
)
hpicfDot1xPaePortGroup1.setObjects(
      *(("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortCritAuthVoiceVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortCritAuthDataVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortCritAuthUserRole"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortOpenAuthVoiceVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortOpenAuthDataVid"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortOpenAuthUserRole"),
        ("HP-DOT1X-EXTENSIONS-MIB", "hpicfDot1xPaePortInitialRole"))
)
if mibBuilder.loadTexts:
    hpicfDot1xPaePortGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDot1xCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance2.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance3.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance4.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance5.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance6.setStatus(
        "current"
    )

hpicfDot1xCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance7.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance8.setStatus(
        "current"
    )

hpicfDot1xCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance9.setStatus(
        "current"
    )

hpicfDot1xCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 11)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance11.setStatus(
        "deprecated"
    )

hpicfDot1xCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 12)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance12.setStatus(
        "current"
    )

hpicfDot1xCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 13)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance13.setStatus(
        "current"
    )

hpicfDot1xCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25, 2, 2, 14)
)
if mibBuilder.loadTexts:
    hpicfDot1xCompliance14.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-DOT1X-EXTENSIONS-MIB",
    **{"hpicfDot1xMIB": hpicfDot1xMIB,
       "hpicfDot1xMIBObjects": hpicfDot1xMIBObjects,
       "hpicfDot1xSystem": hpicfDot1xSystem,
       "hpicfDot1xPaePortTable": hpicfDot1xPaePortTable,
       "hpicfDot1xPaePortEntry": hpicfDot1xPaePortEntry,
       "hpicfDot1xPaePortAuth": hpicfDot1xPaePortAuth,
       "hpicfDot1xPaePortSupp": hpicfDot1xPaePortSupp,
       "hpicfDot1xPaePortMixed": hpicfDot1xPaePortMixed,
       "hpicfDot1xPaePortSpeedVSA": hpicfDot1xPaePortSpeedVSA,
       "hpicfDot1xPaePortMBV": hpicfDot1xPaePortMBV,
       "hpicfDot1xPaePortCritAuthVoiceVid": hpicfDot1xPaePortCritAuthVoiceVid,
       "hpicfDot1xPaePortCritAuthDataVid": hpicfDot1xPaePortCritAuthDataVid,
       "hpicfDot1xPaePortCritAuthUserRole": hpicfDot1xPaePortCritAuthUserRole,
       "hpicfDot1xPaePortOpenAuthVoiceVid": hpicfDot1xPaePortOpenAuthVoiceVid,
       "hpicfDot1xPaePortOpenAuthDataVid": hpicfDot1xPaePortOpenAuthDataVid,
       "hpicfDot1xPaePortOpenAuthUserRole": hpicfDot1xPaePortOpenAuthUserRole,
       "hpicfDot1xPaePortInitialRole": hpicfDot1xPaePortInitialRole,
       "hpicfDot1x2010": hpicfDot1x2010,
       "hpicfDot1xAuthenticator": hpicfDot1xAuthenticator,
       "hpicfDot1xAuthConfigTable": hpicfDot1xAuthConfigTable,
       "hpicfDot1xAuthConfigEntry": hpicfDot1xAuthConfigEntry,
       "hpicfDot1xAuthAuthVid": hpicfDot1xAuthAuthVid,
       "hpicfDot1xAuthUnauthVid": hpicfDot1xAuthUnauthVid,
       "hpicfDot1xAuthUnauthPeriod": hpicfDot1xAuthUnauthPeriod,
       "hpicfDot1xAuthClientLimit": hpicfDot1xAuthClientLimit,
       "hpicfDot1xAuthLogoffPeriod": hpicfDot1xAuthLogoffPeriod,
       "hpicfDot1xAuthClientLimit2": hpicfDot1xAuthClientLimit2,
       "hpicfDot1xAuthCachedReauthPeriod": hpicfDot1xAuthCachedReauthPeriod,
       "hpicfDot1xAuthEnforceCacheReauth": hpicfDot1xAuthEnforceCacheReauth,
       "hpicfDot1xSMAuthConfigTable": hpicfDot1xSMAuthConfigTable,
       "hpicfDot1xSMAuthConfigEntry": hpicfDot1xSMAuthConfigEntry,
       "hpicfDot1xSMAuthPaePort": hpicfDot1xSMAuthPaePort,
       "hpicfDot1xSMAuthMacAddr": hpicfDot1xSMAuthMacAddr,
       "hpicfDot1xSMAuthInitialize": hpicfDot1xSMAuthInitialize,
       "hpicfDot1xSMAuthReauthenticate": hpicfDot1xSMAuthReauthenticate,
       "hpicfDot1xSMAuthPaeState": hpicfDot1xSMAuthPaeState,
       "hpicfDot1xSMAuthBackendAuthState": hpicfDot1xSMAuthBackendAuthState,
       "hpicfDot1xSMAuthReAuthPeriod": hpicfDot1xSMAuthReAuthPeriod,
       "hpicfDot1xSMAuthReAuthEnabled": hpicfDot1xSMAuthReAuthEnabled,
       "hpicfDot1xSMAuthSessionTimeout": hpicfDot1xSMAuthSessionTimeout,
       "hpicfDot1xAuthDiagTable": hpicfDot1xAuthDiagTable,
       "hpicfDot1xAuthDiagEntry": hpicfDot1xAuthDiagEntry,
       "hpicfDot1xAuthNumberOfSuccessAuthentication": hpicfDot1xAuthNumberOfSuccessAuthentication,
       "hpicfDot1xAuthNumberOfFailedAuthentication": hpicfDot1xAuthNumberOfFailedAuthentication,
       "hpicfDot1xAuthStatsTable": hpicfDot1xAuthStatsTable,
       "hpicfDot1xAuthStatsEntry": hpicfDot1xAuthStatsEntry,
       "hpicfDot1xAuthEapolFramesRx": hpicfDot1xAuthEapolFramesRx,
       "hpicfDot1xAuthEapolFramesTx": hpicfDot1xAuthEapolFramesTx,
       "hpicfDot1xAuthEapolStartFramesRx": hpicfDot1xAuthEapolStartFramesRx,
       "hpicfDot1xAuthEapolLogoffFramesRx": hpicfDot1xAuthEapolLogoffFramesRx,
       "hpicfDot1xAuthEapolRespIdFramesRx": hpicfDot1xAuthEapolRespIdFramesRx,
       "hpicfDot1xAuthEapolRespFramesRx": hpicfDot1xAuthEapolRespFramesRx,
       "hpicfDot1xAuthEapolReqIdFramesTx": hpicfDot1xAuthEapolReqIdFramesTx,
       "hpicfDot1xAuthEapolReqFramesTx": hpicfDot1xAuthEapolReqFramesTx,
       "hpicfDot1xAuthInvalidEapolFramesRx": hpicfDot1xAuthInvalidEapolFramesRx,
       "hpicfDot1xAuthEapLengthErrorFramesRx": hpicfDot1xAuthEapLengthErrorFramesRx,
       "hpicfDot1xAuthLastEapolFrameVersion": hpicfDot1xAuthLastEapolFrameVersion,
       "hpicfDot1xAuthLastEapolFrameSource": hpicfDot1xAuthLastEapolFrameSource,
       "hpicfDot1xAuthSessionStatsTable": hpicfDot1xAuthSessionStatsTable,
       "hpicfDot1xAuthSessionStatsEntry": hpicfDot1xAuthSessionStatsEntry,
       "hpicfDot1xAuthSessionPerPAECountersEnabled": hpicfDot1xAuthSessionPerPAECountersEnabled,
       "hpicfDot1xAuthSessionOctetsRx": hpicfDot1xAuthSessionOctetsRx,
       "hpicfDot1xAuthSessionOctetsTx": hpicfDot1xAuthSessionOctetsTx,
       "hpicfDot1xAuthSessionFramesRx": hpicfDot1xAuthSessionFramesRx,
       "hpicfDot1xAuthSessionFramesTx": hpicfDot1xAuthSessionFramesTx,
       "hpicfDot1xAuthSessionId": hpicfDot1xAuthSessionId,
       "hpicfDot1xAuthSessionAuthenticMethod": hpicfDot1xAuthSessionAuthenticMethod,
       "hpicfDot1xAuthSessionTime": hpicfDot1xAuthSessionTime,
       "hpicfDot1xAuthSessionStartTime": hpicfDot1xAuthSessionStartTime,
       "hpicfDot1xAuthSessionStopTime": hpicfDot1xAuthSessionStopTime,
       "hpicfDot1xAuthSessionInactiveTime": hpicfDot1xAuthSessionInactiveTime,
       "hpicfDot1xAuthSessionTerminateCause": hpicfDot1xAuthSessionTerminateCause,
       "hpicfDot1xAuthSessionUserName": hpicfDot1xAuthSessionUserName,
       "hpicfDot1xAuthSessionIsForwarding": hpicfDot1xAuthSessionIsForwarding,
       "hpicfDot1xAuthSessionVid": hpicfDot1xAuthSessionVid,
       "hpicfDot1xAuthSessionRoleName": hpicfDot1xAuthSessionRoleName,
       "hpicfDot1xAuthAllowGvrpVlans": hpicfDot1xAuthAllowGvrpVlans,
       "hpicfDot1xAuthCachedReauthDelay": hpicfDot1xAuthCachedReauthDelay,
       "hpicfDot1xSupplicant": hpicfDot1xSupplicant,
       "hpicfDot1xSuppConfigTable": hpicfDot1xSuppConfigTable,
       "hpicfDot1xSuppConfigEntry": hpicfDot1xSuppConfigEntry,
       "hpicfDot1xSuppConfigIdentity": hpicfDot1xSuppConfigIdentity,
       "hpicfDot1xSuppConfigPassword": hpicfDot1xSuppConfigPassword,
       "hpicfDot1xSuppConfigPasswordEncrypted": hpicfDot1xSuppConfigPasswordEncrypted,
       "hpicfDot1xConformance": hpicfDot1xConformance,
       "hpicfDot1xGroups": hpicfDot1xGroups,
       "hpicfDot1xPaePortGroup": hpicfDot1xPaePortGroup,
       "hpicfDot1xAuthConfigGroup": hpicfDot1xAuthConfigGroup,
       "hpicfDot1xSMAuthConfigGroup": hpicfDot1xSMAuthConfigGroup,
       "hpicfDot1xAuthDiagGroup": hpicfDot1xAuthDiagGroup,
       "hpicfDot1xAuthStatsGroup": hpicfDot1xAuthStatsGroup,
       "hpicfDot1xAuthSessionStatsGroup": hpicfDot1xAuthSessionStatsGroup,
       "hpicfDot1xAuthConfigGroup2": hpicfDot1xAuthConfigGroup2,
       "hpicfDot1xAuthConfigGroup3": hpicfDot1xAuthConfigGroup3,
       "hpicfDot1xAuthConfigGroup4": hpicfDot1xAuthConfigGroup4,
       "hpicfDot1xAuthConfigGroup5": hpicfDot1xAuthConfigGroup5,
       "hpicfDot1xSuppConfigGroup": hpicfDot1xSuppConfigGroup,
       "hpicfDot1xPaeAuthSessionGroup": hpicfDot1xPaeAuthSessionGroup,
       "hpicfDot1xSMAuthSessionTimeoutGroup": hpicfDot1xSMAuthSessionTimeoutGroup,
       "hpicfDot1xPaeAuthSessionGroup1": hpicfDot1xPaeAuthSessionGroup1,
       "hpicfDot1xAuthSessionStatsGroup1": hpicfDot1xAuthSessionStatsGroup1,
       "hpicfDot1xSystemGroup": hpicfDot1xSystemGroup,
       "hpicfDot1xPaePortGroup1": hpicfDot1xPaePortGroup1,
       "hpicfDot1xCompliances": hpicfDot1xCompliances,
       "hpicfDot1xCompliance": hpicfDot1xCompliance,
       "hpicfDot1xCompliance2": hpicfDot1xCompliance2,
       "hpicfDot1xCompliance3": hpicfDot1xCompliance3,
       "hpicfDot1xCompliance4": hpicfDot1xCompliance4,
       "hpicfDot1xCompliance5": hpicfDot1xCompliance5,
       "hpicfDot1xCompliance6": hpicfDot1xCompliance6,
       "hpicfDot1xCompliance7": hpicfDot1xCompliance7,
       "hpicfDot1xCompliance8": hpicfDot1xCompliance8,
       "hpicfDot1xCompliance9": hpicfDot1xCompliance9,
       "hpicfDot1xCompliance11": hpicfDot1xCompliance11,
       "hpicfDot1xCompliance12": hpicfDot1xCompliance12,
       "hpicfDot1xCompliance13": hpicfDot1xCompliance13,
       "hpicfDot1xCompliance14": hpicfDot1xCompliance14}
)
