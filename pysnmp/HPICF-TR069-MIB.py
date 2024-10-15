# SNMP MIB module (HPICF-TR069-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPICF-TR069-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:20 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfTR069MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98)
)
hpicfTR069MIB.setRevisions(
        ("2014-03-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfTR069Notifications_ObjectIdentity = ObjectIdentity
hpicfTR069Notifications = _HpicfTR069Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 0)
)
_HpicfTR069Objects_ObjectIdentity = ObjectIdentity
hpicfTR069Objects = _HpicfTR069Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1)
)


class _HpicfTR069EnableCWMP_Type(Integer32):
    """Custom type hpicfTR069EnableCWMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HpicfTR069EnableCWMP_Type.__name__ = "Integer32"
_HpicfTR069EnableCWMP_Object = MibScalar
hpicfTR069EnableCWMP = _HpicfTR069EnableCWMP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 1),
    _HpicfTR069EnableCWMP_Type()
)
hpicfTR069EnableCWMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069EnableCWMP.setStatus("current")


class _HpicfTR069CWMPDeviceType_Type(Integer32):
    """Custom type hpicfTR069CWMPDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("gateway", 2))
    )


_HpicfTR069CWMPDeviceType_Type.__name__ = "Integer32"
_HpicfTR069CWMPDeviceType_Object = MibScalar
hpicfTR069CWMPDeviceType = _HpicfTR069CWMPDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 2),
    _HpicfTR069CWMPDeviceType_Type()
)
hpicfTR069CWMPDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069CWMPDeviceType.setStatus("current")


class _HpicfTR069AcsUrl_Type(OctetString):
    """Custom type hpicfTR069AcsUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTR069AcsUrl_Type.__name__ = "OctetString"
_HpicfTR069AcsUrl_Object = MibScalar
hpicfTR069AcsUrl = _HpicfTR069AcsUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 3),
    _HpicfTR069AcsUrl_Type()
)
hpicfTR069AcsUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069AcsUrl.setStatus("current")


class _HpicfTR069AcsUrlOrigin_Type(Integer32):
    """Custom type hpicfTR069AcsUrlOrigin based on Integer32"""
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
        *(("acs", 4),
          ("config", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_HpicfTR069AcsUrlOrigin_Type.__name__ = "Integer32"
_HpicfTR069AcsUrlOrigin_Object = MibScalar
hpicfTR069AcsUrlOrigin = _HpicfTR069AcsUrlOrigin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 4),
    _HpicfTR069AcsUrlOrigin_Type()
)
hpicfTR069AcsUrlOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTR069AcsUrlOrigin.setStatus("current")


class _HpicfTR069AcsProxyUrl_Type(OctetString):
    """Custom type hpicfTR069AcsProxyUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTR069AcsProxyUrl_Type.__name__ = "OctetString"
_HpicfTR069AcsProxyUrl_Object = MibScalar
hpicfTR069AcsProxyUrl = _HpicfTR069AcsProxyUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 5),
    _HpicfTR069AcsProxyUrl_Type()
)
hpicfTR069AcsProxyUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069AcsProxyUrl.setStatus("current")


class _HpicfTR069AcsUsername_Type(OctetString):
    """Custom type hpicfTR069AcsUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTR069AcsUsername_Type.__name__ = "OctetString"
_HpicfTR069AcsUsername_Object = MibScalar
hpicfTR069AcsUsername = _HpicfTR069AcsUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 6),
    _HpicfTR069AcsUsername_Type()
)
hpicfTR069AcsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069AcsUsername.setStatus("current")


class _HpicfTR069AcsPassword_Type(OctetString):
    """Custom type hpicfTR069AcsPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTR069AcsPassword_Type.__name__ = "OctetString"
_HpicfTR069AcsPassword_Object = MibScalar
hpicfTR069AcsPassword = _HpicfTR069AcsPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 7),
    _HpicfTR069AcsPassword_Type()
)
hpicfTR069AcsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069AcsPassword.setStatus("current")


class _HpicfTR069AcsPasswordEncrypted_Type(OctetString):
    """Custom type hpicfTR069AcsPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 384),
    )


_HpicfTR069AcsPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfTR069AcsPasswordEncrypted_Object = MibScalar
hpicfTR069AcsPasswordEncrypted = _HpicfTR069AcsPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 8),
    _HpicfTR069AcsPasswordEncrypted_Type()
)
hpicfTR069AcsPasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069AcsPasswordEncrypted.setStatus("current")
_HpicfTR069AcsConnectRetryInterval_Type = Unsigned32
_HpicfTR069AcsConnectRetryInterval_Object = MibScalar
hpicfTR069AcsConnectRetryInterval = _HpicfTR069AcsConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 9),
    _HpicfTR069AcsConnectRetryInterval_Type()
)
hpicfTR069AcsConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTR069AcsConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTR069AcsConnectRetryInterval.setUnits("seconds")


class _HpicfTR069CpeUsername_Type(OctetString):
    """Custom type hpicfTR069CpeUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTR069CpeUsername_Type.__name__ = "OctetString"
_HpicfTR069CpeUsername_Object = MibScalar
hpicfTR069CpeUsername = _HpicfTR069CpeUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 10),
    _HpicfTR069CpeUsername_Type()
)
hpicfTR069CpeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069CpeUsername.setStatus("current")


class _HpicfTR069CpePassword_Type(OctetString):
    """Custom type hpicfTR069CpePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTR069CpePassword_Type.__name__ = "OctetString"
_HpicfTR069CpePassword_Object = MibScalar
hpicfTR069CpePassword = _HpicfTR069CpePassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 11),
    _HpicfTR069CpePassword_Type()
)
hpicfTR069CpePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069CpePassword.setStatus("current")


class _HpicfTR069CpePasswordEncrypted_Type(OctetString):
    """Custom type hpicfTR069CpePasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 384),
    )


_HpicfTR069CpePasswordEncrypted_Type.__name__ = "OctetString"
_HpicfTR069CpePasswordEncrypted_Object = MibScalar
hpicfTR069CpePasswordEncrypted = _HpicfTR069CpePasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 12),
    _HpicfTR069CpePasswordEncrypted_Type()
)
hpicfTR069CpePasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTR069CpePasswordEncrypted.setStatus("current")
_HpicfTR069CpeWaitTimeout_Type = Unsigned32
_HpicfTR069CpeWaitTimeout_Object = MibScalar
hpicfTR069CpeWaitTimeout = _HpicfTR069CpeWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 13),
    _HpicfTR069CpeWaitTimeout_Type()
)
hpicfTR069CpeWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTR069CpeWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTR069CpeWaitTimeout.setUnits("seconds")


class _HpicfTR069PeriodicInformEnable_Type(Integer32):
    """Custom type hpicfTR069PeriodicInformEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HpicfTR069PeriodicInformEnable_Type.__name__ = "Integer32"
_HpicfTR069PeriodicInformEnable_Object = MibScalar
hpicfTR069PeriodicInformEnable = _HpicfTR069PeriodicInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 14),
    _HpicfTR069PeriodicInformEnable_Type()
)
hpicfTR069PeriodicInformEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTR069PeriodicInformEnable.setStatus("current")
_HpicfTR069PeriodicInformInterval_Type = Unsigned32
_HpicfTR069PeriodicInformInterval_Object = MibScalar
hpicfTR069PeriodicInformInterval = _HpicfTR069PeriodicInformInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 15),
    _HpicfTR069PeriodicInformInterval_Type()
)
hpicfTR069PeriodicInformInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTR069PeriodicInformInterval.setStatus("current")
_HpicfTR069PeriodicInformTime_Type = DateAndTime
_HpicfTR069PeriodicInformTime_Object = MibScalar
hpicfTR069PeriodicInformTime = _HpicfTR069PeriodicInformTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 16),
    _HpicfTR069PeriodicInformTime_Type()
)
hpicfTR069PeriodicInformTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTR069PeriodicInformTime.setStatus("current")
_HpicfTR069Conformance_ObjectIdentity = ObjectIdentity
hpicfTR069Conformance = _HpicfTR069Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2)
)
_HpicfTR069MIBCompliances_ObjectIdentity = ObjectIdentity
hpicfTR069MIBCompliances = _HpicfTR069MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 1)
)
_HpicfTR069MIBGroups_ObjectIdentity = ObjectIdentity
hpicfTR069MIBGroups = _HpicfTR069MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 2)
)

# Managed Objects groups

hpicfTR069Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 2, 1)
)
hpicfTR069Group.setObjects(
      *(("HPICF-TR069-MIB", "hpicfTR069EnableCWMP"),
        ("HPICF-TR069-MIB", "hpicfTR069CWMPDeviceType"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsUrl"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsUrlOrigin"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsProxyUrl"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsUsername"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsPassword"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsPasswordEncrypted"),
        ("HPICF-TR069-MIB", "hpicfTR069AcsConnectRetryInterval"),
        ("HPICF-TR069-MIB", "hpicfTR069CpeUsername"),
        ("HPICF-TR069-MIB", "hpicfTR069CpePassword"),
        ("HPICF-TR069-MIB", "hpicfTR069CpePasswordEncrypted"),
        ("HPICF-TR069-MIB", "hpicfTR069CpeWaitTimeout"),
        ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformEnable"),
        ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformInterval"),
        ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformTime"))
)
if mibBuilder.loadTexts:
    hpicfTR069Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfTR069MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTR069MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-TR069-MIB",
    **{"hpicfTR069MIB": hpicfTR069MIB,
       "hpicfTR069Notifications": hpicfTR069Notifications,
       "hpicfTR069Objects": hpicfTR069Objects,
       "hpicfTR069EnableCWMP": hpicfTR069EnableCWMP,
       "hpicfTR069CWMPDeviceType": hpicfTR069CWMPDeviceType,
       "hpicfTR069AcsUrl": hpicfTR069AcsUrl,
       "hpicfTR069AcsUrlOrigin": hpicfTR069AcsUrlOrigin,
       "hpicfTR069AcsProxyUrl": hpicfTR069AcsProxyUrl,
       "hpicfTR069AcsUsername": hpicfTR069AcsUsername,
       "hpicfTR069AcsPassword": hpicfTR069AcsPassword,
       "hpicfTR069AcsPasswordEncrypted": hpicfTR069AcsPasswordEncrypted,
       "hpicfTR069AcsConnectRetryInterval": hpicfTR069AcsConnectRetryInterval,
       "hpicfTR069CpeUsername": hpicfTR069CpeUsername,
       "hpicfTR069CpePassword": hpicfTR069CpePassword,
       "hpicfTR069CpePasswordEncrypted": hpicfTR069CpePasswordEncrypted,
       "hpicfTR069CpeWaitTimeout": hpicfTR069CpeWaitTimeout,
       "hpicfTR069PeriodicInformEnable": hpicfTR069PeriodicInformEnable,
       "hpicfTR069PeriodicInformInterval": hpicfTR069PeriodicInformInterval,
       "hpicfTR069PeriodicInformTime": hpicfTR069PeriodicInformTime,
       "hpicfTR069Conformance": hpicfTR069Conformance,
       "hpicfTR069MIBCompliances": hpicfTR069MIBCompliances,
       "hpicfTR069MIBCompliance": hpicfTR069MIBCompliance,
       "hpicfTR069MIBGroups": hpicfTR069MIBGroups,
       "hpicfTR069Group": hpicfTR069Group}
)
