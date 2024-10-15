# SNMP MIB module (ALCATEL-IND1-WEBMGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://asn1/ALCATEL-IND1-WEBMGT-MIB
# Produced by pysmi-1.5.4 at Tue Oct 15 00:57:44 2024
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

(softentIND1WebMgt,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1WebMgt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1WebMgtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1)
)
alcatelIND1WebMgtMIB.setRevisions(
        ("2010-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1WebMgtMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBNotifications = _AlcatelIND1WebMgtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBNotifications.setStatus("current")
_AlcatelIND1WebMgtMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBObjects = _AlcatelIND1WebMgtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBObjects.setStatus("current")


class _AlaIND1WebMgtAdminStatus_Type(Integer32):
    """Custom type alaIND1WebMgtAdminStatus based on Integer32"""
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


_AlaIND1WebMgtAdminStatus_Type.__name__ = "Integer32"
_AlaIND1WebMgtAdminStatus_Object = MibScalar
alaIND1WebMgtAdminStatus = _AlaIND1WebMgtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 1),
    _AlaIND1WebMgtAdminStatus_Type()
)
alaIND1WebMgtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtAdminStatus.setStatus("current")


class _AlaIND1WebMgtSSL_Type(Integer32):
    """Custom type alaIND1WebMgtSSL based on Integer32"""
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


_AlaIND1WebMgtSSL_Type.__name__ = "Integer32"
_AlaIND1WebMgtSSL_Object = MibScalar
alaIND1WebMgtSSL = _AlaIND1WebMgtSSL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 2),
    _AlaIND1WebMgtSSL_Type()
)
alaIND1WebMgtSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtSSL.setStatus("current")


class _AlaIND1WebMgtHttpPort_Type(Integer32):
    """Custom type alaIND1WebMgtHttpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIND1WebMgtHttpPort_Type.__name__ = "Integer32"
_AlaIND1WebMgtHttpPort_Object = MibScalar
alaIND1WebMgtHttpPort = _AlaIND1WebMgtHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 3),
    _AlaIND1WebMgtHttpPort_Type()
)
alaIND1WebMgtHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtHttpPort.setStatus("current")


class _AlaIND1WebMgtHttpsPort_Type(Integer32):
    """Custom type alaIND1WebMgtHttpsPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(443, 443),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIND1WebMgtHttpsPort_Type.__name__ = "Integer32"
_AlaIND1WebMgtHttpsPort_Object = MibScalar
alaIND1WebMgtHttpsPort = _AlaIND1WebMgtHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 4),
    _AlaIND1WebMgtHttpsPort_Type()
)
alaIND1WebMgtHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtHttpsPort.setStatus("current")


class _AlaIND1WebMgtServerStatus_Type(Integer32):
    """Custom type alaIND1WebMgtServerStatus based on Integer32"""
    defaultValue = 1

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
        *(("disable", 2),
          ("enable", 1),
          ("error", 4),
          ("restarting", 3))
    )


_AlaIND1WebMgtServerStatus_Type.__name__ = "Integer32"
_AlaIND1WebMgtServerStatus_Object = MibScalar
alaIND1WebMgtServerStatus = _AlaIND1WebMgtServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 5),
    _AlaIND1WebMgtServerStatus_Type()
)
alaIND1WebMgtServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtServerStatus.setStatus("current")


class _AlaIND1WebMgtServerError_Type(SnmpAdminString):
    """Custom type alaIND1WebMgtServerError based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaIND1WebMgtServerError_Type.__name__ = "SnmpAdminString"
_AlaIND1WebMgtServerError_Object = MibScalar
alaIND1WebMgtServerError = _AlaIND1WebMgtServerError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 6),
    _AlaIND1WebMgtServerError_Type()
)
alaIND1WebMgtServerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIND1WebMgtServerError.setStatus("current")
_WebMgtTrapsObj_ObjectIdentity = ObjectIdentity
webMgtTrapsObj = _WebMgtTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 7)
)


class _WebMgtServerError_Type(SnmpAdminString):
    """Custom type webMgtServerError based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WebMgtServerError_Type.__name__ = "SnmpAdminString"
_WebMgtServerError_Object = MibScalar
webMgtServerError = _WebMgtServerError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 7, 1),
    _WebMgtServerError_Type()
)
webMgtServerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webMgtServerError.setStatus("current")
_AlcatelIND1WebMgtCertObjects_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtCertObjects = _AlcatelIND1WebMgtCertObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtCertObjects.setStatus("current")


class _AlcatelIND1WebMgtCertFile_Type(Integer32):
    """Custom type alcatelIND1WebMgtCertFile based on Integer32"""
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
        *(("default", 2),
          ("none", 1),
          ("user", 3))
    )


_AlcatelIND1WebMgtCertFile_Type.__name__ = "Integer32"
_AlcatelIND1WebMgtCertFile_Object = MibScalar
alcatelIND1WebMgtCertFile = _AlcatelIND1WebMgtCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 8, 1),
    _AlcatelIND1WebMgtCertFile_Type()
)
alcatelIND1WebMgtCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1WebMgtCertFile.setStatus("current")


class _AlcatelIND1WebMgtCertMD5_Type(SnmpAdminString):
    """Custom type alcatelIND1WebMgtCertMD5 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlcatelIND1WebMgtCertMD5_Type.__name__ = "SnmpAdminString"
_AlcatelIND1WebMgtCertMD5_Object = MibScalar
alcatelIND1WebMgtCertMD5 = _AlcatelIND1WebMgtCertMD5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 1, 8, 2),
    _AlcatelIND1WebMgtCertMD5_Type()
)
alcatelIND1WebMgtCertMD5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1WebMgtCertMD5.setStatus("current")
_AlcatelIND1WebMgtMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBConformance = _AlcatelIND1WebMgtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBConformance.setStatus("current")
_AlcatelIND1WebMgtMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBGroups = _AlcatelIND1WebMgtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBGroups.setStatus("current")
_AlcatelIND1WebMgtMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBCompliances = _AlcatelIND1WebMgtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBCompliances.setStatus("current")

# Managed Objects groups

alaIND1WebMgtConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2, 1, 1)
)
alaIND1WebMgtConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtAdminStatus"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtSSL"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtHttpPort"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtHttpsPort"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtServerStatus"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtServerError"),
        ("ALCATEL-IND1-WEBMGT-MIB", "webMgtServerError"))
)
if mibBuilder.loadTexts:
    alaIND1WebMgtConfigMIBGroup.setStatus("current")

alaIND1WebMgtConfigMIBCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2, 1, 3)
)
alaIND1WebMgtConfigMIBCertGroup.setObjects(
      *(("ALCATEL-IND1-WEBMGT-MIB", "alcatelIND1WebMgtCertFile"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alcatelIND1WebMgtCertMD5"))
)
if mibBuilder.loadTexts:
    alaIND1WebMgtConfigMIBCertGroup.setStatus("current")


# Notification objects

webMgtServerErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 0, 1)
)
webMgtServerErrorTrap.setObjects(
    ("ALCATEL-IND1-WEBMGT-MIB", "webMgtServerError")
)
if mibBuilder.loadTexts:
    webMgtServerErrorTrap.setStatus(
        "current"
    )


# Notifications groups

alaIND1WebMgtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2, 1, 2)
)
alaIND1WebMgtNotificationGroup.setObjects(
    ("ALCATEL-IND1-WEBMGT-MIB", "webMgtServerErrorTrap")
)
if mibBuilder.loadTexts:
    alaIND1WebMgtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIND1WebMgtConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1WebMgtConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-WEBMGT-MIB",
    **{"alcatelIND1WebMgtMIB": alcatelIND1WebMgtMIB,
       "alcatelIND1WebMgtMIBNotifications": alcatelIND1WebMgtMIBNotifications,
       "webMgtServerErrorTrap": webMgtServerErrorTrap,
       "alcatelIND1WebMgtMIBObjects": alcatelIND1WebMgtMIBObjects,
       "alaIND1WebMgtAdminStatus": alaIND1WebMgtAdminStatus,
       "alaIND1WebMgtSSL": alaIND1WebMgtSSL,
       "alaIND1WebMgtHttpPort": alaIND1WebMgtHttpPort,
       "alaIND1WebMgtHttpsPort": alaIND1WebMgtHttpsPort,
       "alaIND1WebMgtServerStatus": alaIND1WebMgtServerStatus,
       "alaIND1WebMgtServerError": alaIND1WebMgtServerError,
       "webMgtTrapsObj": webMgtTrapsObj,
       "webMgtServerError": webMgtServerError,
       "alcatelIND1WebMgtCertObjects": alcatelIND1WebMgtCertObjects,
       "alcatelIND1WebMgtCertFile": alcatelIND1WebMgtCertFile,
       "alcatelIND1WebMgtCertMD5": alcatelIND1WebMgtCertMD5,
       "alcatelIND1WebMgtMIBConformance": alcatelIND1WebMgtMIBConformance,
       "alcatelIND1WebMgtMIBGroups": alcatelIND1WebMgtMIBGroups,
       "alaIND1WebMgtConfigMIBGroup": alaIND1WebMgtConfigMIBGroup,
       "alaIND1WebMgtNotificationGroup": alaIND1WebMgtNotificationGroup,
       "alaIND1WebMgtConfigMIBCertGroup": alaIND1WebMgtConfigMIBCertGroup,
       "alcatelIND1WebMgtMIBCompliances": alcatelIND1WebMgtMIBCompliances,
       "alaIND1WebMgtConfigMIBCompliance": alaIND1WebMgtConfigMIBCompliance}
)
