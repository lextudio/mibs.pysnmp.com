# SNMP MIB module (ALCATEL-IND1-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://asn1/ALCATEL-IND1-AAA-MIB
# Produced by pysmi-1.5.4 at Tue Oct 15 00:49:07 2024
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

(softentIND1AAA,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1AAA")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1AAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1)
)
alcatelIND1AAAMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1AAAMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBObjects = _AlcatelIND1AAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBObjects.setStatus("current")
_AaaServerMIB_ObjectIdentity = ObjectIdentity
aaaServerMIB = _AaaServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1)
)
_AaaServerTable_Object = MibTable
aaaServerTable = _AaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aaaServerTable.setStatus("current")
_AaaServerEntry_Object = MibTableRow
aaaServerEntry = _AaaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1)
)
aaaServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaasName"),
)
if mibBuilder.loadTexts:
    aaaServerEntry.setStatus("current")


class _AaasName_Type(SnmpAdminString):
    """Custom type aaasName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasName_Type.__name__ = "SnmpAdminString"
_AaasName_Object = MibTableColumn
aaasName = _AaasName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 1),
    _AaasName_Type()
)
aaasName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaasName.setStatus("current")


class _AaasProtocol_Type(Integer32):
    """Custom type aaasProtocol based on Integer32"""
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
        *(("ace", 3),
          ("ldap", 2),
          ("radius", 1),
          ("tacacs", 4))
    )


_AaasProtocol_Type.__name__ = "Integer32"
_AaasProtocol_Object = MibTableColumn
aaasProtocol = _AaasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 2),
    _AaasProtocol_Type()
)
aaasProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasProtocol.setStatus("current")


class _AaasHostName_Type(SnmpAdminString):
    """Custom type aaasHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName_Type.__name__ = "SnmpAdminString"
_AaasHostName_Object = MibTableColumn
aaasHostName = _AaasHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 3),
    _AaasHostName_Type()
)
aaasHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName.setStatus("current")
_AaasIpAddress_Type = IpAddress
_AaasIpAddress_Object = MibTableColumn
aaasIpAddress = _AaasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 4),
    _AaasIpAddress_Type()
)
aaasIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress.setStatus("current")


class _AaasHostName2_Type(SnmpAdminString):
    """Custom type aaasHostName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName2_Type.__name__ = "SnmpAdminString"
_AaasHostName2_Object = MibTableColumn
aaasHostName2 = _AaasHostName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 5),
    _AaasHostName2_Type()
)
aaasHostName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName2.setStatus("current")
_AaasIpAddress2_Type = IpAddress
_AaasIpAddress2_Object = MibTableColumn
aaasIpAddress2 = _AaasIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 6),
    _AaasIpAddress2_Type()
)
aaasIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress2.setStatus("current")


class _AaasRetries_Type(Integer32):
    """Custom type aaasRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AaasRetries_Type.__name__ = "Integer32"
_AaasRetries_Object = MibTableColumn
aaasRetries = _AaasRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 7),
    _AaasRetries_Type()
)
aaasRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRetries.setStatus("current")


class _AaasTimout_Type(Integer32):
    """Custom type aaasTimout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AaasTimout_Type.__name__ = "Integer32"
_AaasTimout_Object = MibTableColumn
aaasTimout = _AaasTimout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 8),
    _AaasTimout_Type()
)
aaasTimout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTimout.setStatus("current")


class _AaasRadKey_Type(SnmpAdminString):
    """Custom type aaasRadKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasRadKey_Type.__name__ = "SnmpAdminString"
_AaasRadKey_Object = MibTableColumn
aaasRadKey = _AaasRadKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 9),
    _AaasRadKey_Type()
)
aaasRadKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKey.setStatus("current")


class _AaasRadAuthPort_Type(Integer32):
    """Custom type aaasRadAuthPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAuthPort_Type.__name__ = "Integer32"
_AaasRadAuthPort_Object = MibTableColumn
aaasRadAuthPort = _AaasRadAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 10),
    _AaasRadAuthPort_Type()
)
aaasRadAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAuthPort.setStatus("current")


class _AaasRadAcctPort_Type(Integer32):
    """Custom type aaasRadAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAcctPort_Type.__name__ = "Integer32"
_AaasRadAcctPort_Object = MibTableColumn
aaasRadAcctPort = _AaasRadAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 11),
    _AaasRadAcctPort_Type()
)
aaasRadAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAcctPort.setStatus("current")


class _AaasLdapPort_Type(Integer32):
    """Custom type aaasLdapPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasLdapPort_Type.__name__ = "Integer32"
_AaasLdapPort_Object = MibTableColumn
aaasLdapPort = _AaasLdapPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 12),
    _AaasLdapPort_Type()
)
aaasLdapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPort.setStatus("current")


class _AaasLdapDn_Type(SnmpAdminString):
    """Custom type aaasLdapDn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaasLdapDn_Type.__name__ = "SnmpAdminString"
_AaasLdapDn_Object = MibTableColumn
aaasLdapDn = _AaasLdapDn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 13),
    _AaasLdapDn_Type()
)
aaasLdapDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapDn.setStatus("current")


class _AaasLdapPasswd_Type(SnmpAdminString):
    """Custom type aaasLdapPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasLdapPasswd_Type.__name__ = "SnmpAdminString"
_AaasLdapPasswd_Object = MibTableColumn
aaasLdapPasswd = _AaasLdapPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 14),
    _AaasLdapPasswd_Type()
)
aaasLdapPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswd.setStatus("current")


class _AaasLdapSearchBase_Type(SnmpAdminString):
    """Custom type aaasLdapSearchBase based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasLdapSearchBase_Type.__name__ = "SnmpAdminString"
_AaasLdapSearchBase_Object = MibTableColumn
aaasLdapSearchBase = _AaasLdapSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 15),
    _AaasLdapSearchBase_Type()
)
aaasLdapSearchBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapSearchBase.setStatus("current")


class _AaasLdapServType_Type(Integer32):
    """Custom type aaasLdapServType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("generic", 1),
          ("microsoft", 5),
          ("netscape", 2),
          ("novell", 3),
          ("ns", 0),
          ("sun", 4))
    )


_AaasLdapServType_Type.__name__ = "Integer32"
_AaasLdapServType_Object = MibTableColumn
aaasLdapServType = _AaasLdapServType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 16),
    _AaasLdapServType_Type()
)
aaasLdapServType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapServType.setStatus("current")


class _AaasLdapEnableSsl_Type(Integer32):
    """Custom type aaasLdapEnableSsl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("ns", 0),
          ("true", 1))
    )


_AaasLdapEnableSsl_Type.__name__ = "Integer32"
_AaasLdapEnableSsl_Object = MibTableColumn
aaasLdapEnableSsl = _AaasLdapEnableSsl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 17),
    _AaasLdapEnableSsl_Type()
)
aaasLdapEnableSsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapEnableSsl.setStatus("current")


class _AaasRowStatus_Type(RowStatus):
    """Custom type aaasRowStatus based on RowStatus"""


_AaasRowStatus_Object = MibTableColumn
aaasRowStatus = _AaasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 18),
    _AaasRowStatus_Type()
)
aaasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRowStatus.setStatus("current")


class _AaasTacacsKey_Type(SnmpAdminString):
    """Custom type aaasTacacsKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasTacacsKey_Type.__name__ = "SnmpAdminString"
_AaasTacacsKey_Object = MibTableColumn
aaasTacacsKey = _AaasTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 19),
    _AaasTacacsKey_Type()
)
aaasTacacsKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKey.setStatus("current")


class _AaasTacacsPort_Type(Integer32):
    """Custom type aaasTacacsPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasTacacsPort_Type.__name__ = "Integer32"
_AaasTacacsPort_Object = MibTableColumn
aaasTacacsPort = _AaasTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 20),
    _AaasTacacsPort_Type()
)
aaasTacacsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsPort.setStatus("current")


class _AaasVrfName_Type(SnmpAdminString):
    """Custom type aaasVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasVrfName_Type.__name__ = "SnmpAdminString"
_AaasVrfName_Object = MibTableColumn
aaasVrfName = _AaasVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 21),
    _AaasVrfName_Type()
)
aaasVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasVrfName.setStatus("current")


class _AaasRadKeyHash_Type(SnmpAdminString):
    """Custom type aaasRadKeyHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AaasRadKeyHash_Type.__name__ = "SnmpAdminString"
_AaasRadKeyHash_Object = MibTableColumn
aaasRadKeyHash = _AaasRadKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 22),
    _AaasRadKeyHash_Type()
)
aaasRadKeyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKeyHash.setStatus("current")


class _AaasLdapPasswdHash_Type(SnmpAdminString):
    """Custom type aaasLdapPasswdHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AaasLdapPasswdHash_Type.__name__ = "SnmpAdminString"
_AaasLdapPasswdHash_Object = MibTableColumn
aaasLdapPasswdHash = _AaasLdapPasswdHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 23),
    _AaasLdapPasswdHash_Type()
)
aaasLdapPasswdHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswdHash.setStatus("current")


class _AaasTacacsKeyHash_Type(SnmpAdminString):
    """Custom type aaasTacacsKeyHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AaasTacacsKeyHash_Type.__name__ = "SnmpAdminString"
_AaasTacacsKeyHash_Object = MibTableColumn
aaasTacacsKeyHash = _AaasTacacsKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 24),
    _AaasTacacsKeyHash_Type()
)
aaasTacacsKeyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKeyHash.setStatus("current")
_AaaAuthAcctMIB_ObjectIdentity = ObjectIdentity
aaaAuthAcctMIB = _AaaAuthAcctMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2)
)
_AaaAuthSATable_Object = MibTable
aaaAuthSATable = _AaaAuthSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aaaAuthSATable.setStatus("current")
_AaaAuthSAEntry_Object = MibTableRow
aaaAuthSAEntry = _AaaAuthSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1)
)
aaaAuthSAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatsInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthSAEntry.setStatus("current")


class _AaatsInterface_Type(Integer32):
    """Custom type aaatsInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("default", 1),
          ("ftp", 4),
          ("http", 5),
          ("snmp", 6),
          ("ssh", 7),
          ("telnet", 3))
    )


_AaatsInterface_Type.__name__ = "Integer32"
_AaatsInterface_Object = MibTableColumn
aaatsInterface = _AaatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 1),
    _AaatsInterface_Type()
)
aaatsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaatsInterface.setStatus("current")


class _AaatsName1_Type(SnmpAdminString):
    """Custom type aaatsName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName1_Type.__name__ = "SnmpAdminString"
_AaatsName1_Object = MibTableColumn
aaatsName1 = _AaatsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 2),
    _AaatsName1_Type()
)
aaatsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName1.setStatus("current")


class _AaatsName2_Type(SnmpAdminString):
    """Custom type aaatsName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName2_Type.__name__ = "SnmpAdminString"
_AaatsName2_Object = MibTableColumn
aaatsName2 = _AaatsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 3),
    _AaatsName2_Type()
)
aaatsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName2.setStatus("current")


class _AaatsName3_Type(SnmpAdminString):
    """Custom type aaatsName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName3_Type.__name__ = "SnmpAdminString"
_AaatsName3_Object = MibTableColumn
aaatsName3 = _AaatsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 4),
    _AaatsName3_Type()
)
aaatsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName3.setStatus("current")


class _AaatsName4_Type(SnmpAdminString):
    """Custom type aaatsName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName4_Type.__name__ = "SnmpAdminString"
_AaatsName4_Object = MibTableColumn
aaatsName4 = _AaatsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 5),
    _AaatsName4_Type()
)
aaatsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName4.setStatus("current")


class _AaatsRowStatus_Type(RowStatus):
    """Custom type aaatsRowStatus based on RowStatus"""


_AaatsRowStatus_Object = MibTableColumn
aaatsRowStatus = _AaatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 7),
    _AaatsRowStatus_Type()
)
aaatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsRowStatus.setStatus("current")


class _AaatsCertificate_Type(Integer32):
    """Custom type aaatsCertificate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("certificateOnly", 1),
          ("certificateWithPassword", 2),
          ("noCertificate", 0))
    )


_AaatsCertificate_Type.__name__ = "Integer32"
_AaatsCertificate_Object = MibTableColumn
aaatsCertificate = _AaatsCertificate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 8),
    _AaatsCertificate_Type()
)
aaatsCertificate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsCertificate.setStatus("current")
_AaaAcctSATable_Object = MibTable
aaaAcctSATable = _AaaAcctSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aaaAcctSATable.setStatus("current")
_AaaAcctSAEntry_Object = MibTableRow
aaaAcctSAEntry = _AaaAcctSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1)
)
aaaAcctSAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacsInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctSAEntry.setStatus("current")


class _AaacsInterface_Type(Integer32):
    """Custom type aaacsInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacsInterface_Type.__name__ = "Integer32"
_AaacsInterface_Object = MibTableColumn
aaacsInterface = _AaacsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 1),
    _AaacsInterface_Type()
)
aaacsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaacsInterface.setStatus("current")


class _AaacsName1_Type(SnmpAdminString):
    """Custom type aaacsName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName1_Type.__name__ = "SnmpAdminString"
_AaacsName1_Object = MibTableColumn
aaacsName1 = _AaacsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 2),
    _AaacsName1_Type()
)
aaacsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName1.setStatus("current")


class _AaacsName2_Type(SnmpAdminString):
    """Custom type aaacsName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName2_Type.__name__ = "SnmpAdminString"
_AaacsName2_Object = MibTableColumn
aaacsName2 = _AaacsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 3),
    _AaacsName2_Type()
)
aaacsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName2.setStatus("current")


class _AaacsName3_Type(SnmpAdminString):
    """Custom type aaacsName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName3_Type.__name__ = "SnmpAdminString"
_AaacsName3_Object = MibTableColumn
aaacsName3 = _AaacsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 4),
    _AaacsName3_Type()
)
aaacsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName3.setStatus("current")


class _AaacsName4_Type(SnmpAdminString):
    """Custom type aaacsName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName4_Type.__name__ = "SnmpAdminString"
_AaacsName4_Object = MibTableColumn
aaacsName4 = _AaacsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 5),
    _AaacsName4_Type()
)
aaacsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName4.setStatus("current")


class _AaacsRowStatus_Type(RowStatus):
    """Custom type aaacsRowStatus based on RowStatus"""


_AaacsRowStatus_Object = MibTableColumn
aaacsRowStatus = _AaacsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 6),
    _AaacsRowStatus_Type()
)
aaacsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsRowStatus.setStatus("current")
_AaaAcctCmdTable_Object = MibTable
aaaAcctCmdTable = _AaaAcctCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aaaAcctCmdTable.setStatus("current")
_AaaAcctCmdEntry_Object = MibTableRow
aaaAcctCmdEntry = _AaaAcctCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1)
)
aaaAcctCmdEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacmdInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctCmdEntry.setStatus("current")


class _AaacmdInterface_Type(Integer32):
    """Custom type aaacmdInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacmdInterface_Type.__name__ = "Integer32"
_AaacmdInterface_Object = MibTableColumn
aaacmdInterface = _AaacmdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 1),
    _AaacmdInterface_Type()
)
aaacmdInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaacmdInterface.setStatus("current")


class _AaacmdSrvName1_Type(SnmpAdminString):
    """Custom type aaacmdSrvName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName1_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName1_Object = MibTableColumn
aaacmdSrvName1 = _AaacmdSrvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 2),
    _AaacmdSrvName1_Type()
)
aaacmdSrvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName1.setStatus("current")


class _AaacmdSrvName2_Type(SnmpAdminString):
    """Custom type aaacmdSrvName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName2_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName2_Object = MibTableColumn
aaacmdSrvName2 = _AaacmdSrvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 3),
    _AaacmdSrvName2_Type()
)
aaacmdSrvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName2.setStatus("current")


class _AaacmdSrvName3_Type(SnmpAdminString):
    """Custom type aaacmdSrvName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName3_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName3_Object = MibTableColumn
aaacmdSrvName3 = _AaacmdSrvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 4),
    _AaacmdSrvName3_Type()
)
aaacmdSrvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName3.setStatus("current")


class _AaacmdSrvName4_Type(SnmpAdminString):
    """Custom type aaacmdSrvName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName4_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName4_Object = MibTableColumn
aaacmdSrvName4 = _AaacmdSrvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 5),
    _AaacmdSrvName4_Type()
)
aaacmdSrvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName4.setStatus("current")


class _AaacmdRowStatus_Type(RowStatus):
    """Custom type aaacmdRowStatus based on RowStatus"""


_AaacmdRowStatus_Object = MibTableColumn
aaacmdRowStatus = _AaacmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 6),
    _AaacmdRowStatus_Type()
)
aaacmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdRowStatus.setStatus("current")
_AaaAuthDATable_Object = MibTable
aaaAuthDATable = _AaaAuthDATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aaaAuthDATable.setStatus("current")
_AaaAuthDAEntry_Object = MibTableRow
aaaAuthDAEntry = _AaaAuthDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1)
)
aaaAuthDAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaadaInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthDAEntry.setStatus("current")


class _AaadaInterface_Type(Integer32):
    """Custom type aaadaInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AaadaInterface_Type.__name__ = "Integer32"
_AaadaInterface_Object = MibTableColumn
aaadaInterface = _AaadaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 1),
    _AaadaInterface_Type()
)
aaadaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaadaInterface.setStatus("current")


class _AaadaName1_Type(SnmpAdminString):
    """Custom type aaadaName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName1_Type.__name__ = "SnmpAdminString"
_AaadaName1_Object = MibTableColumn
aaadaName1 = _AaadaName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 2),
    _AaadaName1_Type()
)
aaadaName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName1.setStatus("current")


class _AaadaName2_Type(SnmpAdminString):
    """Custom type aaadaName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName2_Type.__name__ = "SnmpAdminString"
_AaadaName2_Object = MibTableColumn
aaadaName2 = _AaadaName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 3),
    _AaadaName2_Type()
)
aaadaName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName2.setStatus("current")


class _AaadaName3_Type(SnmpAdminString):
    """Custom type aaadaName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName3_Type.__name__ = "SnmpAdminString"
_AaadaName3_Object = MibTableColumn
aaadaName3 = _AaadaName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 4),
    _AaadaName3_Type()
)
aaadaName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName3.setStatus("current")


class _AaadaName4_Type(SnmpAdminString):
    """Custom type aaadaName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName4_Type.__name__ = "SnmpAdminString"
_AaadaName4_Object = MibTableColumn
aaadaName4 = _AaadaName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 5),
    _AaadaName4_Type()
)
aaadaName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName4.setStatus("current")


class _AaadaRowStatus_Type(RowStatus):
    """Custom type aaadaRowStatus based on RowStatus"""


_AaadaRowStatus_Object = MibTableColumn
aaadaRowStatus = _AaadaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 6),
    _AaadaRowStatus_Type()
)
aaadaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaRowStatus.setStatus("current")
_AaaAcctDATable_Object = MibTable
aaaAcctDATable = _AaaAcctDATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aaaAcctDATable.setStatus("current")
_AaaAcctDAEntry_Object = MibTableRow
aaaAcctDAEntry = _AaaAcctDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1)
)
aaaAcctDAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacdInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctDAEntry.setStatus("current")


class _AaacdInterface_Type(Integer32):
    """Custom type aaacdInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacdInterface_Type.__name__ = "Integer32"
_AaacdInterface_Object = MibTableColumn
aaacdInterface = _AaacdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 1),
    _AaacdInterface_Type()
)
aaacdInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaacdInterface.setStatus("current")


class _AaacdName1_Type(SnmpAdminString):
    """Custom type aaacdName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName1_Type.__name__ = "SnmpAdminString"
_AaacdName1_Object = MibTableColumn
aaacdName1 = _AaacdName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 2),
    _AaacdName1_Type()
)
aaacdName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName1.setStatus("current")


class _AaacdName2_Type(SnmpAdminString):
    """Custom type aaacdName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName2_Type.__name__ = "SnmpAdminString"
_AaacdName2_Object = MibTableColumn
aaacdName2 = _AaacdName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 3),
    _AaacdName2_Type()
)
aaacdName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName2.setStatus("current")


class _AaacdName3_Type(SnmpAdminString):
    """Custom type aaacdName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName3_Type.__name__ = "SnmpAdminString"
_AaacdName3_Object = MibTableColumn
aaacdName3 = _AaacdName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 4),
    _AaacdName3_Type()
)
aaacdName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName3.setStatus("current")


class _AaacdName4_Type(SnmpAdminString):
    """Custom type aaacdName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName4_Type.__name__ = "SnmpAdminString"
_AaacdName4_Object = MibTableColumn
aaacdName4 = _AaacdName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 5),
    _AaacdName4_Type()
)
aaacdName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName4.setStatus("current")


class _AaacdRowStatus_Type(RowStatus):
    """Custom type aaacdRowStatus based on RowStatus"""


_AaacdRowStatus_Object = MibTableColumn
aaacdRowStatus = _AaacdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 6),
    _AaacdRowStatus_Type()
)
aaacdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdRowStatus.setStatus("current")
_AaaUserMIB_ObjectIdentity = ObjectIdentity
aaaUserMIB = _AaaUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3)
)
_AaaUserTable_Object = MibTable
aaaUserTable = _AaaUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aaaUserTable.setStatus("current")
_AaaUserEntry_Object = MibTableRow
aaaUserEntry = _AaaUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1)
)
aaaUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaauUserName"),
)
if mibBuilder.loadTexts:
    aaaUserEntry.setStatus("current")


class _AaauUserName_Type(SnmpAdminString):
    """Custom type aaauUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AaauUserName_Type.__name__ = "SnmpAdminString"
_AaauUserName_Object = MibTableColumn
aaauUserName = _AaauUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 1),
    _AaauUserName_Type()
)
aaauUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaauUserName.setStatus("current")


class _AaauPassword_Type(SnmpAdminString):
    """Custom type aaauPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauPassword_Type.__name__ = "SnmpAdminString"
_AaauPassword_Object = MibTableColumn
aaauPassword = _AaauPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 2),
    _AaauPassword_Type()
)
aaauPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPassword.setStatus("current")


class _AaauReadRight1_Type(Unsigned32):
    """Custom type aaauReadRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight1_Type.__name__ = "Unsigned32"
_AaauReadRight1_Object = MibTableColumn
aaauReadRight1 = _AaauReadRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 3),
    _AaauReadRight1_Type()
)
aaauReadRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight1.setStatus("current")


class _AaauReadRight2_Type(Unsigned32):
    """Custom type aaauReadRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight2_Type.__name__ = "Unsigned32"
_AaauReadRight2_Object = MibTableColumn
aaauReadRight2 = _AaauReadRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 4),
    _AaauReadRight2_Type()
)
aaauReadRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight2.setStatus("current")


class _AaauWriteRight1_Type(Unsigned32):
    """Custom type aaauWriteRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight1_Type.__name__ = "Unsigned32"
_AaauWriteRight1_Object = MibTableColumn
aaauWriteRight1 = _AaauWriteRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 5),
    _AaauWriteRight1_Type()
)
aaauWriteRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight1.setStatus("current")


class _AaauWriteRight2_Type(Unsigned32):
    """Custom type aaauWriteRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight2_Type.__name__ = "Unsigned32"
_AaauWriteRight2_Object = MibTableColumn
aaauWriteRight2 = _AaauWriteRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 6),
    _AaauWriteRight2_Type()
)
aaauWriteRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight2.setStatus("current")


class _AaauSnmpLevel_Type(Integer32):
    """Custom type aaauSnmpLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("md5", 4),
          ("md5Des", 6),
          ("no", 1),
          ("noauth", 2),
          ("sha", 3),
          ("shaDes", 5))
    )


_AaauSnmpLevel_Type.__name__ = "Integer32"
_AaauSnmpLevel_Object = MibTableColumn
aaauSnmpLevel = _AaauSnmpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 7),
    _AaauSnmpLevel_Type()
)
aaauSnmpLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauSnmpLevel.setStatus("current")


class _AaauSnmpAuthKey_Type(OctetString):
    """Custom type aaauSnmpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaauSnmpAuthKey_Type.__name__ = "OctetString"
_AaauSnmpAuthKey_Object = MibTableColumn
aaauSnmpAuthKey = _AaauSnmpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 8),
    _AaauSnmpAuthKey_Type()
)
aaauSnmpAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauSnmpAuthKey.setStatus("current")


class _AaauRowStatus_Type(RowStatus):
    """Custom type aaauRowStatus based on RowStatus"""


_AaauRowStatus_Object = MibTableColumn
aaauRowStatus = _AaauRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 9),
    _AaauRowStatus_Type()
)
aaauRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauRowStatus.setStatus("current")


class _AaauOldPassword_Type(SnmpAdminString):
    """Custom type aaauOldPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauOldPassword_Type.__name__ = "SnmpAdminString"
_AaauOldPassword_Object = MibTableColumn
aaauOldPassword = _AaauOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 10),
    _AaauOldPassword_Type()
)
aaauOldPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauOldPassword.setStatus("current")


class _AaauPasswordExpirationDate_Type(SnmpAdminString):
    """Custom type aaauPasswordExpirationDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordExpirationDate_Type.__name__ = "SnmpAdminString"
_AaauPasswordExpirationDate_Object = MibTableColumn
aaauPasswordExpirationDate = _AaauPasswordExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 11),
    _AaauPasswordExpirationDate_Type()
)
aaauPasswordExpirationDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationDate.setStatus("current")


class _AaauPasswordExpirationInMinute_Type(Integer32):
    """Custom type aaauPasswordExpirationInMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 216000),
    )


_AaauPasswordExpirationInMinute_Type.__name__ = "Integer32"
_AaauPasswordExpirationInMinute_Object = MibTableColumn
aaauPasswordExpirationInMinute = _AaauPasswordExpirationInMinute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 12),
    _AaauPasswordExpirationInMinute_Type()
)
aaauPasswordExpirationInMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationInMinute.setStatus("current")


class _AaauPasswordAllowModifyDate_Type(SnmpAdminString):
    """Custom type aaauPasswordAllowModifyDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordAllowModifyDate_Type.__name__ = "SnmpAdminString"
_AaauPasswordAllowModifyDate_Object = MibTableColumn
aaauPasswordAllowModifyDate = _AaauPasswordAllowModifyDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 13),
    _AaauPasswordAllowModifyDate_Type()
)
aaauPasswordAllowModifyDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauPasswordAllowModifyDate.setStatus("current")


class _AaauPasswordLockoutEnable_Type(Integer32):
    """Custom type aaauPasswordLockoutEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expired", 3),
          ("lockout", 1),
          ("unlock", 2))
    )


_AaauPasswordLockoutEnable_Type.__name__ = "Integer32"
_AaauPasswordLockoutEnable_Object = MibTableColumn
aaauPasswordLockoutEnable = _AaauPasswordLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 14),
    _AaauPasswordLockoutEnable_Type()
)
aaauPasswordLockoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordLockoutEnable.setStatus("current")


class _AaauBadAtempts_Type(Integer32):
    """Custom type aaauBadAtempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaauBadAtempts_Type.__name__ = "Integer32"
_AaauBadAtempts_Object = MibTableColumn
aaauBadAtempts = _AaauBadAtempts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 15),
    _AaauBadAtempts_Type()
)
aaauBadAtempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauBadAtempts.setStatus("current")


class _AaauReadRight3_Type(Unsigned32):
    """Custom type aaauReadRight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight3_Type.__name__ = "Unsigned32"
_AaauReadRight3_Object = MibTableColumn
aaauReadRight3 = _AaauReadRight3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 16),
    _AaauReadRight3_Type()
)
aaauReadRight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight3.setStatus("current")


class _AaauReadRight4_Type(Unsigned32):
    """Custom type aaauReadRight4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight4_Type.__name__ = "Unsigned32"
_AaauReadRight4_Object = MibTableColumn
aaauReadRight4 = _AaauReadRight4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 17),
    _AaauReadRight4_Type()
)
aaauReadRight4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight4.setStatus("current")


class _AaauWriteRight3_Type(Unsigned32):
    """Custom type aaauWriteRight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight3_Type.__name__ = "Unsigned32"
_AaauWriteRight3_Object = MibTableColumn
aaauWriteRight3 = _AaauWriteRight3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 18),
    _AaauWriteRight3_Type()
)
aaauWriteRight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight3.setStatus("current")


class _AaauWriteRight4_Type(Unsigned32):
    """Custom type aaauWriteRight4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight4_Type.__name__ = "Unsigned32"
_AaauWriteRight4_Object = MibTableColumn
aaauWriteRight4 = _AaauWriteRight4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 19),
    _AaauWriteRight4_Type()
)
aaauWriteRight4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight4.setStatus("current")
_AaaAsaConfig_ObjectIdentity = ObjectIdentity
aaaAsaConfig = _AaaAsaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4)
)


class _AaaAsaPasswordSizeMin_Type(Integer32):
    """Custom type aaaAsaPasswordSizeMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_AaaAsaPasswordSizeMin_Type.__name__ = "Integer32"
_AaaAsaPasswordSizeMin_Object = MibScalar
aaaAsaPasswordSizeMin = _AaaAsaPasswordSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 1),
    _AaaAsaPasswordSizeMin_Type()
)
aaaAsaPasswordSizeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordSizeMin.setStatus("current")


class _AaaAsaDefaultPasswordExpirationInDays_Type(Integer32):
    """Custom type aaaAsaDefaultPasswordExpirationInDays based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaDefaultPasswordExpirationInDays_Type.__name__ = "Integer32"
_AaaAsaDefaultPasswordExpirationInDays_Object = MibScalar
aaaAsaDefaultPasswordExpirationInDays = _AaaAsaDefaultPasswordExpirationInDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 2),
    _AaaAsaDefaultPasswordExpirationInDays_Type()
)
aaaAsaDefaultPasswordExpirationInDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaDefaultPasswordExpirationInDays.setStatus("current")


class _AaaAsaPasswordContainUserName_Type(Integer32):
    """Custom type aaaAsaPasswordContainUserName based on Integer32"""
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


_AaaAsaPasswordContainUserName_Type.__name__ = "Integer32"
_AaaAsaPasswordContainUserName_Object = MibScalar
aaaAsaPasswordContainUserName = _AaaAsaPasswordContainUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 3),
    _AaaAsaPasswordContainUserName_Type()
)
aaaAsaPasswordContainUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordContainUserName.setStatus("current")


class _AaaAsaPasswordMinUpperCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinUpperCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinUpperCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinUpperCase_Object = MibScalar
aaaAsaPasswordMinUpperCase = _AaaAsaPasswordMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 4),
    _AaaAsaPasswordMinUpperCase_Type()
)
aaaAsaPasswordMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinUpperCase.setStatus("current")


class _AaaAsaPasswordMinLowerCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinLowerCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinLowerCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinLowerCase_Object = MibScalar
aaaAsaPasswordMinLowerCase = _AaaAsaPasswordMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 5),
    _AaaAsaPasswordMinLowerCase_Type()
)
aaaAsaPasswordMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinLowerCase.setStatus("current")


class _AaaAsaPasswordMinDigit_Type(Integer32):
    """Custom type aaaAsaPasswordMinDigit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinDigit_Type.__name__ = "Integer32"
_AaaAsaPasswordMinDigit_Object = MibScalar
aaaAsaPasswordMinDigit = _AaaAsaPasswordMinDigit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 6),
    _AaaAsaPasswordMinDigit_Type()
)
aaaAsaPasswordMinDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinDigit.setStatus("current")


class _AaaAsaPasswordMinNonAlphan_Type(Integer32):
    """Custom type aaaAsaPasswordMinNonAlphan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinNonAlphan_Type.__name__ = "Integer32"
_AaaAsaPasswordMinNonAlphan_Object = MibScalar
aaaAsaPasswordMinNonAlphan = _AaaAsaPasswordMinNonAlphan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 7),
    _AaaAsaPasswordMinNonAlphan_Type()
)
aaaAsaPasswordMinNonAlphan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinNonAlphan.setStatus("current")


class _AaaAsaPasswordHistory_Type(Integer32):
    """Custom type aaaAsaPasswordHistory based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AaaAsaPasswordHistory_Type.__name__ = "Integer32"
_AaaAsaPasswordHistory_Object = MibScalar
aaaAsaPasswordHistory = _AaaAsaPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 8),
    _AaaAsaPasswordHistory_Type()
)
aaaAsaPasswordHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordHistory.setStatus("current")


class _AaaAsaPasswordMinAge_Type(Integer32):
    """Custom type aaaAsaPasswordMinAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaPasswordMinAge_Type.__name__ = "Integer32"
_AaaAsaPasswordMinAge_Object = MibScalar
aaaAsaPasswordMinAge = _AaaAsaPasswordMinAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 9),
    _AaaAsaPasswordMinAge_Type()
)
aaaAsaPasswordMinAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinAge.setStatus("current")


class _AaaAsaLockoutWindow_Type(Integer32):
    """Custom type aaaAsaLockoutWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutWindow_Type.__name__ = "Integer32"
_AaaAsaLockoutWindow_Object = MibScalar
aaaAsaLockoutWindow = _AaaAsaLockoutWindow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 10),
    _AaaAsaLockoutWindow_Type()
)
aaaAsaLockoutWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutWindow.setStatus("current")


class _AaaAsaLockoutDuration_Type(Integer32):
    """Custom type aaaAsaLockoutDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutDuration_Type.__name__ = "Integer32"
_AaaAsaLockoutDuration_Object = MibScalar
aaaAsaLockoutDuration = _AaaAsaLockoutDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 11),
    _AaaAsaLockoutDuration_Type()
)
aaaAsaLockoutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutDuration.setStatus("current")


class _AaaAsaLockoutThreshold_Type(Integer32):
    """Custom type aaaAsaLockoutThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaaAsaLockoutThreshold_Type.__name__ = "Integer32"
_AaaAsaLockoutThreshold_Object = MibScalar
aaaAsaLockoutThreshold = _AaaAsaLockoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 12),
    _AaaAsaLockoutThreshold_Type()
)
aaaAsaLockoutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutThreshold.setStatus("current")


class _AaaAsaAccessPolicyAdminConsoleOnly_Type(Integer32):
    """Custom type aaaAsaAccessPolicyAdminConsoleOnly based on Integer32"""
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


_AaaAsaAccessPolicyAdminConsoleOnly_Type.__name__ = "Integer32"
_AaaAsaAccessPolicyAdminConsoleOnly_Object = MibScalar
aaaAsaAccessPolicyAdminConsoleOnly = _AaaAsaAccessPolicyAdminConsoleOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 13),
    _AaaAsaAccessPolicyAdminConsoleOnly_Type()
)
aaaAsaAccessPolicyAdminConsoleOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessPolicyAdminConsoleOnly.setStatus("current")
_AlcatelIND1AAAMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBConformance = _AlcatelIND1AAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBConformance.setStatus("current")
_AlcatelIND1AAAMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBGroups = _AlcatelIND1AAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBGroups.setStatus("current")
_AlcatelIND1AAAMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBCompliances = _AlcatelIND1AAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliances.setStatus("current")

# Managed Objects groups

aaaServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 1)
)
aaaServerMIBGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaasProtocol"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHostName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHostName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress2"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRetries"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTimout"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadAuthPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadAcctPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapDn"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPasswd"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapSearchBase"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapServType"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapEnableSsl"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasVrfName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadKeyHash"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPasswdHash"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsKeyHash"))
)
if mibBuilder.loadTexts:
    aaaServerMIBGroup.setStatus("current")

aaaAuthAcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 2)
)
aaaAuthAcctGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaatsName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsCertificate"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaadaInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaadaName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaadaName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaadaName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaadaName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaadaRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacdName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacdName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacdName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacdName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacdRowStatus"))
)
if mibBuilder.loadTexts:
    aaaAuthAcctGroup.setStatus("current")

aaaUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 3)
)
aaaUserMIBGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaauPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight1"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight2"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight1"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight2"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpLevel"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpAuthKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaauRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaauOldPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordExpirationDate"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordExpirationInMinute"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordAllowModifyDate"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordLockoutEnable"),
        ("ALCATEL-IND1-AAA-MIB", "aaauBadAtempts"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight3"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight4"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight3"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight4"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordSizeMin"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaDefaultPasswordExpirationInDays"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordContainUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinUpperCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinLowerCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinDigit"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinNonAlphan"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordHistory"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinAge"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutWindow"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutDuration"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutThreshold"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaAccessPolicyAdminConsoleOnly"))
)
if mibBuilder.loadTexts:
    aaaUserMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1AAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-AAA-MIB",
    **{"alcatelIND1AAAMIB": alcatelIND1AAAMIB,
       "alcatelIND1AAAMIBObjects": alcatelIND1AAAMIBObjects,
       "aaaServerMIB": aaaServerMIB,
       "aaaServerTable": aaaServerTable,
       "aaaServerEntry": aaaServerEntry,
       "aaasName": aaasName,
       "aaasProtocol": aaasProtocol,
       "aaasHostName": aaasHostName,
       "aaasIpAddress": aaasIpAddress,
       "aaasHostName2": aaasHostName2,
       "aaasIpAddress2": aaasIpAddress2,
       "aaasRetries": aaasRetries,
       "aaasTimout": aaasTimout,
       "aaasRadKey": aaasRadKey,
       "aaasRadAuthPort": aaasRadAuthPort,
       "aaasRadAcctPort": aaasRadAcctPort,
       "aaasLdapPort": aaasLdapPort,
       "aaasLdapDn": aaasLdapDn,
       "aaasLdapPasswd": aaasLdapPasswd,
       "aaasLdapSearchBase": aaasLdapSearchBase,
       "aaasLdapServType": aaasLdapServType,
       "aaasLdapEnableSsl": aaasLdapEnableSsl,
       "aaasRowStatus": aaasRowStatus,
       "aaasTacacsKey": aaasTacacsKey,
       "aaasTacacsPort": aaasTacacsPort,
       "aaasVrfName": aaasVrfName,
       "aaasRadKeyHash": aaasRadKeyHash,
       "aaasLdapPasswdHash": aaasLdapPasswdHash,
       "aaasTacacsKeyHash": aaasTacacsKeyHash,
       "aaaAuthAcctMIB": aaaAuthAcctMIB,
       "aaaAuthSATable": aaaAuthSATable,
       "aaaAuthSAEntry": aaaAuthSAEntry,
       "aaatsInterface": aaatsInterface,
       "aaatsName1": aaatsName1,
       "aaatsName2": aaatsName2,
       "aaatsName3": aaatsName3,
       "aaatsName4": aaatsName4,
       "aaatsRowStatus": aaatsRowStatus,
       "aaatsCertificate": aaatsCertificate,
       "aaaAcctSATable": aaaAcctSATable,
       "aaaAcctSAEntry": aaaAcctSAEntry,
       "aaacsInterface": aaacsInterface,
       "aaacsName1": aaacsName1,
       "aaacsName2": aaacsName2,
       "aaacsName3": aaacsName3,
       "aaacsName4": aaacsName4,
       "aaacsRowStatus": aaacsRowStatus,
       "aaaAcctCmdTable": aaaAcctCmdTable,
       "aaaAcctCmdEntry": aaaAcctCmdEntry,
       "aaacmdInterface": aaacmdInterface,
       "aaacmdSrvName1": aaacmdSrvName1,
       "aaacmdSrvName2": aaacmdSrvName2,
       "aaacmdSrvName3": aaacmdSrvName3,
       "aaacmdSrvName4": aaacmdSrvName4,
       "aaacmdRowStatus": aaacmdRowStatus,
       "aaaAuthDATable": aaaAuthDATable,
       "aaaAuthDAEntry": aaaAuthDAEntry,
       "aaadaInterface": aaadaInterface,
       "aaadaName1": aaadaName1,
       "aaadaName2": aaadaName2,
       "aaadaName3": aaadaName3,
       "aaadaName4": aaadaName4,
       "aaadaRowStatus": aaadaRowStatus,
       "aaaAcctDATable": aaaAcctDATable,
       "aaaAcctDAEntry": aaaAcctDAEntry,
       "aaacdInterface": aaacdInterface,
       "aaacdName1": aaacdName1,
       "aaacdName2": aaacdName2,
       "aaacdName3": aaacdName3,
       "aaacdName4": aaacdName4,
       "aaacdRowStatus": aaacdRowStatus,
       "aaaUserMIB": aaaUserMIB,
       "aaaUserTable": aaaUserTable,
       "aaaUserEntry": aaaUserEntry,
       "aaauUserName": aaauUserName,
       "aaauPassword": aaauPassword,
       "aaauReadRight1": aaauReadRight1,
       "aaauReadRight2": aaauReadRight2,
       "aaauWriteRight1": aaauWriteRight1,
       "aaauWriteRight2": aaauWriteRight2,
       "aaauSnmpLevel": aaauSnmpLevel,
       "aaauSnmpAuthKey": aaauSnmpAuthKey,
       "aaauRowStatus": aaauRowStatus,
       "aaauOldPassword": aaauOldPassword,
       "aaauPasswordExpirationDate": aaauPasswordExpirationDate,
       "aaauPasswordExpirationInMinute": aaauPasswordExpirationInMinute,
       "aaauPasswordAllowModifyDate": aaauPasswordAllowModifyDate,
       "aaauPasswordLockoutEnable": aaauPasswordLockoutEnable,
       "aaauBadAtempts": aaauBadAtempts,
       "aaauReadRight3": aaauReadRight3,
       "aaauReadRight4": aaauReadRight4,
       "aaauWriteRight3": aaauWriteRight3,
       "aaauWriteRight4": aaauWriteRight4,
       "aaaAsaConfig": aaaAsaConfig,
       "aaaAsaPasswordSizeMin": aaaAsaPasswordSizeMin,
       "aaaAsaDefaultPasswordExpirationInDays": aaaAsaDefaultPasswordExpirationInDays,
       "aaaAsaPasswordContainUserName": aaaAsaPasswordContainUserName,
       "aaaAsaPasswordMinUpperCase": aaaAsaPasswordMinUpperCase,
       "aaaAsaPasswordMinLowerCase": aaaAsaPasswordMinLowerCase,
       "aaaAsaPasswordMinDigit": aaaAsaPasswordMinDigit,
       "aaaAsaPasswordMinNonAlphan": aaaAsaPasswordMinNonAlphan,
       "aaaAsaPasswordHistory": aaaAsaPasswordHistory,
       "aaaAsaPasswordMinAge": aaaAsaPasswordMinAge,
       "aaaAsaLockoutWindow": aaaAsaLockoutWindow,
       "aaaAsaLockoutDuration": aaaAsaLockoutDuration,
       "aaaAsaLockoutThreshold": aaaAsaLockoutThreshold,
       "aaaAsaAccessPolicyAdminConsoleOnly": aaaAsaAccessPolicyAdminConsoleOnly,
       "alcatelIND1AAAMIBConformance": alcatelIND1AAAMIBConformance,
       "alcatelIND1AAAMIBGroups": alcatelIND1AAAMIBGroups,
       "aaaServerMIBGroup": aaaServerMIBGroup,
       "aaaAuthAcctGroup": aaaAuthAcctGroup,
       "aaaUserMIBGroup": aaaUserMIBGroup,
       "alcatelIND1AAAMIBCompliances": alcatelIND1AAAMIBCompliances,
       "alcatelIND1AAAMIBCompliance": alcatelIND1AAAMIBCompliance}
)
