# SNMP MIB module (NETSCREEN-SET-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:54 2024
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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


# MODULE-IDENTITY

netscreenSetAuthMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 2)
)
netscreenSetAuthMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-11-10 20:22",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2002-04-27 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetAuth_ObjectIdentity = ObjectIdentity
nsSetAuth = _NsSetAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2)
)
_NsSetAuthCfgTable_Object = MibTable
nsSetAuthCfgTable = _NsSetAuthCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1)
)
if mibBuilder.loadTexts:
    nsSetAuthCfgTable.setStatus("current")
_NsSetAuthCfgEntry_Object = MibTableRow
nsSetAuthCfgEntry = _NsSetAuthCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1)
)
nsSetAuthCfgEntry.setIndexNames(
    (0, "NETSCREEN-SET-AUTH-MIB", "nsSetAuthCfgIdx"),
)
if mibBuilder.loadTexts:
    nsSetAuthCfgEntry.setStatus("current")


class _NsSetAuthCfgIdx_Type(Integer32):
    """Custom type nsSetAuthCfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSetAuthCfgIdx_Type.__name__ = "Integer32"
_NsSetAuthCfgIdx_Object = MibTableColumn
nsSetAuthCfgIdx = _NsSetAuthCfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 1),
    _NsSetAuthCfgIdx_Type()
)
nsSetAuthCfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgIdx.setStatus("current")
_NsSetAuthCfgVsys_Type = Integer32
_NsSetAuthCfgVsys_Object = MibTableColumn
nsSetAuthCfgVsys = _NsSetAuthCfgVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 2),
    _NsSetAuthCfgVsys_Type()
)
nsSetAuthCfgVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgVsys.setStatus("current")


class _NsSetAuthCfgName_Type(DisplayString):
    """Custom type nsSetAuthCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetAuthCfgName_Type.__name__ = "DisplayString"
_NsSetAuthCfgName_Object = MibTableColumn
nsSetAuthCfgName = _NsSetAuthCfgName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 3),
    _NsSetAuthCfgName_Type()
)
nsSetAuthCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgName.setStatus("current")


class _NsSetAuthCfgPrimary_Type(DisplayString):
    """Custom type nsSetAuthCfgPrimary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetAuthCfgPrimary_Type.__name__ = "DisplayString"
_NsSetAuthCfgPrimary_Object = MibTableColumn
nsSetAuthCfgPrimary = _NsSetAuthCfgPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 4),
    _NsSetAuthCfgPrimary_Type()
)
nsSetAuthCfgPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgPrimary.setStatus("current")


class _NsSetAuthCfgBackup1_Type(DisplayString):
    """Custom type nsSetAuthCfgBackup1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetAuthCfgBackup1_Type.__name__ = "DisplayString"
_NsSetAuthCfgBackup1_Object = MibTableColumn
nsSetAuthCfgBackup1 = _NsSetAuthCfgBackup1_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 5),
    _NsSetAuthCfgBackup1_Type()
)
nsSetAuthCfgBackup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgBackup1.setStatus("current")


class _NsSetAuthCfgBackup2_Type(DisplayString):
    """Custom type nsSetAuthCfgBackup2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetAuthCfgBackup2_Type.__name__ = "DisplayString"
_NsSetAuthCfgBackup2_Object = MibTableColumn
nsSetAuthCfgBackup2 = _NsSetAuthCfgBackup2_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 6),
    _NsSetAuthCfgBackup2_Type()
)
nsSetAuthCfgBackup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgBackup2.setStatus("current")
_NsSetAuthCfgConnIdleTimeout_Type = Integer32
_NsSetAuthCfgConnIdleTimeout_Object = MibTableColumn
nsSetAuthCfgConnIdleTimeout = _NsSetAuthCfgConnIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 7),
    _NsSetAuthCfgConnIdleTimeout_Type()
)
nsSetAuthCfgConnIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgConnIdleTimeout.setStatus("current")


class _NsSetAuthCfgAuthAccount_Type(Integer32):
    """Custom type nsSetAuthCfgAuthAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgAuthAccount_Type.__name__ = "Integer32"
_NsSetAuthCfgAuthAccount_Object = MibTableColumn
nsSetAuthCfgAuthAccount = _NsSetAuthCfgAuthAccount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 8),
    _NsSetAuthCfgAuthAccount_Type()
)
nsSetAuthCfgAuthAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgAuthAccount.setStatus("current")


class _NsSetAuthCfgIkeAccount_Type(Integer32):
    """Custom type nsSetAuthCfgIkeAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgIkeAccount_Type.__name__ = "Integer32"
_NsSetAuthCfgIkeAccount_Object = MibTableColumn
nsSetAuthCfgIkeAccount = _NsSetAuthCfgIkeAccount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 9),
    _NsSetAuthCfgIkeAccount_Type()
)
nsSetAuthCfgIkeAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgIkeAccount.setStatus("current")


class _NsSetAuthCfgL2tpAccount_Type(Integer32):
    """Custom type nsSetAuthCfgL2tpAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgL2tpAccount_Type.__name__ = "Integer32"
_NsSetAuthCfgL2tpAccount_Object = MibTableColumn
nsSetAuthCfgL2tpAccount = _NsSetAuthCfgL2tpAccount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 10),
    _NsSetAuthCfgL2tpAccount_Type()
)
nsSetAuthCfgL2tpAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgL2tpAccount.setStatus("current")


class _NsSetAuthCfgAdminAccount_Type(Integer32):
    """Custom type nsSetAuthCfgAdminAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgAdminAccount_Type.__name__ = "Integer32"
_NsSetAuthCfgAdminAccount_Object = MibTableColumn
nsSetAuthCfgAdminAccount = _NsSetAuthCfgAdminAccount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 11),
    _NsSetAuthCfgAdminAccount_Type()
)
nsSetAuthCfgAdminAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgAdminAccount.setStatus("current")


class _NsSetAuthCfgXauthAccount_Type(Integer32):
    """Custom type nsSetAuthCfgXauthAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgXauthAccount_Type.__name__ = "Integer32"
_NsSetAuthCfgXauthAccount_Object = MibTableColumn
nsSetAuthCfgXauthAccount = _NsSetAuthCfgXauthAccount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 12),
    _NsSetAuthCfgXauthAccount_Type()
)
nsSetAuthCfgXauthAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgXauthAccount.setStatus("current")


class _NsSetAuthCfgMethod_Type(Integer32):
    """Custom type nsSetAuthCfgMethod based on Integer32"""
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
        *(("build-in-user-db", 0),
          ("ldap-server", 3),
          ("radius-server", 1),
          ("secureId-server", 2))
    )


_NsSetAuthCfgMethod_Type.__name__ = "Integer32"
_NsSetAuthCfgMethod_Object = MibTableColumn
nsSetAuthCfgMethod = _NsSetAuthCfgMethod_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 13),
    _NsSetAuthCfgMethod_Type()
)
nsSetAuthCfgMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgMethod.setStatus("current")
_NsSetAuthCfgPort_Type = Integer32
_NsSetAuthCfgPort_Object = MibTableColumn
nsSetAuthCfgPort = _NsSetAuthCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 14),
    _NsSetAuthCfgPort_Type()
)
nsSetAuthCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgPort.setStatus("current")
_NsSetAuthCfgSecCliRetry_Type = Integer32
_NsSetAuthCfgSecCliRetry_Object = MibTableColumn
nsSetAuthCfgSecCliRetry = _NsSetAuthCfgSecCliRetry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 15),
    _NsSetAuthCfgSecCliRetry_Type()
)
nsSetAuthCfgSecCliRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSecCliRetry.setStatus("current")
_NsSetAuthCfgSecCliTimeout_Type = Integer32
_NsSetAuthCfgSecCliTimeout_Object = MibTableColumn
nsSetAuthCfgSecCliTimeout = _NsSetAuthCfgSecCliTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 16),
    _NsSetAuthCfgSecCliTimeout_Type()
)
nsSetAuthCfgSecCliTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSecCliTimeout.setStatus("current")


class _NsSetAuthCfgSecEncType_Type(Integer32):
    """Custom type nsSetAuthCfgSecEncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("sdi", 0))
    )


_NsSetAuthCfgSecEncType_Type.__name__ = "Integer32"
_NsSetAuthCfgSecEncType_Object = MibTableColumn
nsSetAuthCfgSecEncType = _NsSetAuthCfgSecEncType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 17),
    _NsSetAuthCfgSecEncType_Type()
)
nsSetAuthCfgSecEncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSecEncType.setStatus("current")


class _NsSetAuthCfgSecUseDuress_Type(Integer32):
    """Custom type nsSetAuthCfgSecUseDuress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgSecUseDuress_Type.__name__ = "Integer32"
_NsSetAuthCfgSecUseDuress_Object = MibTableColumn
nsSetAuthCfgSecUseDuress = _NsSetAuthCfgSecUseDuress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 18),
    _NsSetAuthCfgSecUseDuress_Type()
)
nsSetAuthCfgSecUseDuress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSecUseDuress.setStatus("current")


class _NsSetAuthCfgLDAPCni_Type(DisplayString):
    """Custom type nsSetAuthCfgLDAPCni based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_NsSetAuthCfgLDAPCni_Type.__name__ = "DisplayString"
_NsSetAuthCfgLDAPCni_Object = MibTableColumn
nsSetAuthCfgLDAPCni = _NsSetAuthCfgLDAPCni_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 19),
    _NsSetAuthCfgLDAPCni_Type()
)
nsSetAuthCfgLDAPCni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgLDAPCni.setStatus("current")


class _NsSetAuthCfgLDAPDn_Type(DisplayString):
    """Custom type nsSetAuthCfgLDAPDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetAuthCfgLDAPDn_Type.__name__ = "DisplayString"
_NsSetAuthCfgLDAPDn_Object = MibTableColumn
nsSetAuthCfgLDAPDn = _NsSetAuthCfgLDAPDn_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 20),
    _NsSetAuthCfgLDAPDn_Type()
)
nsSetAuthCfgLDAPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgLDAPDn.setStatus("current")


class _NsSetAuthCfgSepChar_Type(DisplayString):
    """Custom type nsSetAuthCfgSepChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_NsSetAuthCfgSepChar_Type.__name__ = "DisplayString"
_NsSetAuthCfgSepChar_Object = MibTableColumn
nsSetAuthCfgSepChar = _NsSetAuthCfgSepChar_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 21),
    _NsSetAuthCfgSepChar_Type()
)
nsSetAuthCfgSepChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSepChar.setStatus("mandatory")
_NsSetAuthCfgSepNumber_Type = Integer32
_NsSetAuthCfgSepNumber_Object = MibTableColumn
nsSetAuthCfgSepNumber = _NsSetAuthCfgSepNumber_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 22),
    _NsSetAuthCfgSepNumber_Type()
)
nsSetAuthCfgSepNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSepNumber.setStatus("mandatory")
_NsSetAuthCfgRevInterval_Type = Integer32
_NsSetAuthCfgRevInterval_Object = MibTableColumn
nsSetAuthCfgRevInterval = _NsSetAuthCfgRevInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 23),
    _NsSetAuthCfgRevInterval_Type()
)
nsSetAuthCfgRevInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgRevInterval.setStatus("mandatory")
_NsSetAuthCfgRadRetries_Type = Integer32
_NsSetAuthCfgRadRetries_Object = MibTableColumn
nsSetAuthCfgRadRetries = _NsSetAuthCfgRadRetries_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 24),
    _NsSetAuthCfgRadRetries_Type()
)
nsSetAuthCfgRadRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgRadRetries.setStatus("mandatory")


class _NsSetAuthCfgEnableStnID_Type(Integer32):
    """Custom type nsSetAuthCfgEnableStnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgEnableStnID_Type.__name__ = "Integer32"
_NsSetAuthCfgEnableStnID_Object = MibTableColumn
nsSetAuthCfgEnableStnID = _NsSetAuthCfgEnableStnID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 25),
    _NsSetAuthCfgEnableStnID_Type()
)
nsSetAuthCfgEnableStnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgEnableStnID.setStatus("mandatory")


class _NsSetAuthCfgDomainName_Type(DisplayString):
    """Custom type nsSetAuthCfgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetAuthCfgDomainName_Type.__name__ = "DisplayString"
_NsSetAuthCfgDomainName_Object = MibTableColumn
nsSetAuthCfgDomainName = _NsSetAuthCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 26),
    _NsSetAuthCfgDomainName_Type()
)
nsSetAuthCfgDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgDomainName.setStatus("mandatory")
_NsSetAuthCfgAcctSessIdLen_Type = Integer32
_NsSetAuthCfgAcctSessIdLen_Object = MibTableColumn
nsSetAuthCfgAcctSessIdLen = _NsSetAuthCfgAcctSessIdLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 27),
    _NsSetAuthCfgAcctSessIdLen_Type()
)
nsSetAuthCfgAcctSessIdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgAcctSessIdLen.setStatus("mandatory")


class _NsSetAuthCfgRFC2138Compatibility_Type(Integer32):
    """Custom type nsSetAuthCfgRFC2138Compatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetAuthCfgRFC2138Compatibility_Type.__name__ = "Integer32"
_NsSetAuthCfgRFC2138Compatibility_Object = MibTableColumn
nsSetAuthCfgRFC2138Compatibility = _NsSetAuthCfgRFC2138Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 28),
    _NsSetAuthCfgRFC2138Compatibility_Type()
)
nsSetAuthCfgRFC2138Compatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgRFC2138Compatibility.setStatus("mandatory")


class _NsSetAuthCfgSourceIfName_Type(DisplayString):
    """Custom type nsSetAuthCfgSourceIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetAuthCfgSourceIfName_Type.__name__ = "DisplayString"
_NsSetAuthCfgSourceIfName_Object = MibTableColumn
nsSetAuthCfgSourceIfName = _NsSetAuthCfgSourceIfName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 29),
    _NsSetAuthCfgSourceIfName_Type()
)
nsSetAuthCfgSourceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSourceIfName.setStatus("mandatory")
_NsSetAuthCfgAcctPort_Type = Integer32
_NsSetAuthCfgAcctPort_Object = MibTableColumn
nsSetAuthCfgAcctPort = _NsSetAuthCfgAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 30),
    _NsSetAuthCfgAcctPort_Type()
)
nsSetAuthCfgAcctPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgAcctPort.setStatus("mandatory")


class _NsSetAuthCfgAcctListActn_Type(Integer32):
    """Custom type nsSetAuthCfgAcctListActn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cleanup-sess", 1),
          ("none", 0))
    )


_NsSetAuthCfgAcctListActn_Type.__name__ = "Integer32"
_NsSetAuthCfgAcctListActn_Object = MibTableColumn
nsSetAuthCfgAcctListActn = _NsSetAuthCfgAcctListActn_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 31),
    _NsSetAuthCfgAcctListActn_Type()
)
nsSetAuthCfgAcctListActn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgAcctListActn.setStatus("mandatory")
_NsSetAuthCfgSourceIfInfo_Type = Integer32
_NsSetAuthCfgSourceIfInfo_Object = MibTableColumn
nsSetAuthCfgSourceIfInfo = _NsSetAuthCfgSourceIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 2, 1, 1, 32),
    _NsSetAuthCfgSourceIfInfo_Type()
)
nsSetAuthCfgSourceIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetAuthCfgSourceIfInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-AUTH-MIB",
    **{"netscreenSetAuthMibModule": netscreenSetAuthMibModule,
       "nsSetAuth": nsSetAuth,
       "nsSetAuthCfgTable": nsSetAuthCfgTable,
       "nsSetAuthCfgEntry": nsSetAuthCfgEntry,
       "nsSetAuthCfgIdx": nsSetAuthCfgIdx,
       "nsSetAuthCfgVsys": nsSetAuthCfgVsys,
       "nsSetAuthCfgName": nsSetAuthCfgName,
       "nsSetAuthCfgPrimary": nsSetAuthCfgPrimary,
       "nsSetAuthCfgBackup1": nsSetAuthCfgBackup1,
       "nsSetAuthCfgBackup2": nsSetAuthCfgBackup2,
       "nsSetAuthCfgConnIdleTimeout": nsSetAuthCfgConnIdleTimeout,
       "nsSetAuthCfgAuthAccount": nsSetAuthCfgAuthAccount,
       "nsSetAuthCfgIkeAccount": nsSetAuthCfgIkeAccount,
       "nsSetAuthCfgL2tpAccount": nsSetAuthCfgL2tpAccount,
       "nsSetAuthCfgAdminAccount": nsSetAuthCfgAdminAccount,
       "nsSetAuthCfgXauthAccount": nsSetAuthCfgXauthAccount,
       "nsSetAuthCfgMethod": nsSetAuthCfgMethod,
       "nsSetAuthCfgPort": nsSetAuthCfgPort,
       "nsSetAuthCfgSecCliRetry": nsSetAuthCfgSecCliRetry,
       "nsSetAuthCfgSecCliTimeout": nsSetAuthCfgSecCliTimeout,
       "nsSetAuthCfgSecEncType": nsSetAuthCfgSecEncType,
       "nsSetAuthCfgSecUseDuress": nsSetAuthCfgSecUseDuress,
       "nsSetAuthCfgLDAPCni": nsSetAuthCfgLDAPCni,
       "nsSetAuthCfgLDAPDn": nsSetAuthCfgLDAPDn,
       "nsSetAuthCfgSepChar": nsSetAuthCfgSepChar,
       "nsSetAuthCfgSepNumber": nsSetAuthCfgSepNumber,
       "nsSetAuthCfgRevInterval": nsSetAuthCfgRevInterval,
       "nsSetAuthCfgRadRetries": nsSetAuthCfgRadRetries,
       "nsSetAuthCfgEnableStnID": nsSetAuthCfgEnableStnID,
       "nsSetAuthCfgDomainName": nsSetAuthCfgDomainName,
       "nsSetAuthCfgAcctSessIdLen": nsSetAuthCfgAcctSessIdLen,
       "nsSetAuthCfgRFC2138Compatibility": nsSetAuthCfgRFC2138Compatibility,
       "nsSetAuthCfgSourceIfName": nsSetAuthCfgSourceIfName,
       "nsSetAuthCfgAcctPort": nsSetAuthCfgAcctPort,
       "nsSetAuthCfgAcctListActn": nsSetAuthCfgAcctListActn,
       "nsSetAuthCfgSourceIfInfo": nsSetAuthCfgSourceIfInfo}
)
