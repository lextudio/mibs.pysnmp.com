# SNMP MIB module (ASCEND-MIBIPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:45 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibmibProfIpsec_ObjectIdentity = ObjectIdentity
mibmibProfIpsec = _MibmibProfIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 85)
)
_MibmibProfIpsecTable_Object = MibTable
mibmibProfIpsecTable = _MibmibProfIpsecTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1)
)
if mibBuilder.loadTexts:
    mibmibProfIpsecTable.setStatus("mandatory")
_MibmibProfIpsecEntry_Object = MibTableRow
mibmibProfIpsecEntry = _MibmibProfIpsecEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1)
)
mibmibProfIpsecEntry.setIndexNames(
    (0, "ASCEND-MIBIPSEC-MIB", "mibProfIpsec-Name"),
)
if mibBuilder.loadTexts:
    mibmibProfIpsecEntry.setStatus("mandatory")
_MibProfIpsec_Name_Type = DisplayString
_MibProfIpsec_Name_Object = MibScalar
mibProfIpsec_Name = _MibProfIpsec_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 1),
    _MibProfIpsec_Name_Type()
)
mibProfIpsec_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIpsec_Name.setStatus("mandatory")


class _MibProfIpsec_Active_Type(Integer32):
    """Custom type mibProfIpsec_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_Active_Type.__name__ = "Integer32"
_MibProfIpsec_Active_Object = MibScalar
mibProfIpsec_Active = _MibProfIpsec_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 2),
    _MibProfIpsec_Active_Type()
)
mibProfIpsec_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_Active.setStatus("mandatory")


class _MibProfIpsec_EncapMode_Type(Integer32):
    """Custom type mibProfIpsec_EncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("optimized", 1),
          ("transport", 2),
          ("tunnel", 3))
    )


_MibProfIpsec_EncapMode_Type.__name__ = "Integer32"
_MibProfIpsec_EncapMode_Object = MibScalar
mibProfIpsec_EncapMode = _MibProfIpsec_EncapMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 3),
    _MibProfIpsec_EncapMode_Type()
)
mibProfIpsec_EncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_EncapMode.setStatus("mandatory")
_MibProfIpsec_TunnelAddress_Type = IpAddress
_MibProfIpsec_TunnelAddress_Object = MibScalar
mibProfIpsec_TunnelAddress = _MibProfIpsec_TunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 4),
    _MibProfIpsec_TunnelAddress_Type()
)
mibProfIpsec_TunnelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_TunnelAddress.setStatus("mandatory")


class _MibProfIpsec_SendAh_Active_Type(Integer32):
    """Custom type mibProfIpsec_SendAh_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_SendAh_Active_Type.__name__ = "Integer32"
_MibProfIpsec_SendAh_Active_Object = MibScalar
mibProfIpsec_SendAh_Active = _MibProfIpsec_SendAh_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 5),
    _MibProfIpsec_SendAh_Active_Type()
)
mibProfIpsec_SendAh_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendAh_Active.setStatus("mandatory")
_MibProfIpsec_SendAh_Spi_Type = Integer32
_MibProfIpsec_SendAh_Spi_Object = MibScalar
mibProfIpsec_SendAh_Spi = _MibProfIpsec_SendAh_Spi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 6),
    _MibProfIpsec_SendAh_Spi_Type()
)
mibProfIpsec_SendAh_Spi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendAh_Spi.setStatus("mandatory")


class _MibProfIpsec_SendAh_AhType_Type(Integer32):
    """Custom type mibProfIpsec_SendAh_AhType based on Integer32"""
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
        *(("md5", 2),
          ("md5Hmac", 4),
          ("none", 1),
          ("sha1", 3),
          ("sha1Hmac", 5))
    )


_MibProfIpsec_SendAh_AhType_Type.__name__ = "Integer32"
_MibProfIpsec_SendAh_AhType_Object = MibScalar
mibProfIpsec_SendAh_AhType = _MibProfIpsec_SendAh_AhType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 7),
    _MibProfIpsec_SendAh_AhType_Type()
)
mibProfIpsec_SendAh_AhType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendAh_AhType.setStatus("mandatory")
_MibProfIpsec_SendAh_Key_Type = DisplayString
_MibProfIpsec_SendAh_Key_Object = MibScalar
mibProfIpsec_SendAh_Key = _MibProfIpsec_SendAh_Key_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 8),
    _MibProfIpsec_SendAh_Key_Type()
)
mibProfIpsec_SendAh_Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendAh_Key.setStatus("mandatory")


class _MibProfIpsec_SendAh_ReplayProtection_Type(Integer32):
    """Custom type mibProfIpsec_SendAh_ReplayProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_SendAh_ReplayProtection_Type.__name__ = "Integer32"
_MibProfIpsec_SendAh_ReplayProtection_Object = MibScalar
mibProfIpsec_SendAh_ReplayProtection = _MibProfIpsec_SendAh_ReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 9),
    _MibProfIpsec_SendAh_ReplayProtection_Type()
)
mibProfIpsec_SendAh_ReplayProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendAh_ReplayProtection.setStatus("mandatory")


class _MibProfIpsec_RecvAh_Active_Type(Integer32):
    """Custom type mibProfIpsec_RecvAh_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_RecvAh_Active_Type.__name__ = "Integer32"
_MibProfIpsec_RecvAh_Active_Object = MibScalar
mibProfIpsec_RecvAh_Active = _MibProfIpsec_RecvAh_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 10),
    _MibProfIpsec_RecvAh_Active_Type()
)
mibProfIpsec_RecvAh_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvAh_Active.setStatus("mandatory")
_MibProfIpsec_RecvAh_Spi_Type = Integer32
_MibProfIpsec_RecvAh_Spi_Object = MibScalar
mibProfIpsec_RecvAh_Spi = _MibProfIpsec_RecvAh_Spi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 11),
    _MibProfIpsec_RecvAh_Spi_Type()
)
mibProfIpsec_RecvAh_Spi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvAh_Spi.setStatus("mandatory")


class _MibProfIpsec_RecvAh_AhType_Type(Integer32):
    """Custom type mibProfIpsec_RecvAh_AhType based on Integer32"""
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
        *(("md5", 2),
          ("md5Hmac", 4),
          ("none", 1),
          ("sha1", 3),
          ("sha1Hmac", 5))
    )


_MibProfIpsec_RecvAh_AhType_Type.__name__ = "Integer32"
_MibProfIpsec_RecvAh_AhType_Object = MibScalar
mibProfIpsec_RecvAh_AhType = _MibProfIpsec_RecvAh_AhType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 12),
    _MibProfIpsec_RecvAh_AhType_Type()
)
mibProfIpsec_RecvAh_AhType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvAh_AhType.setStatus("mandatory")
_MibProfIpsec_RecvAh_Key_Type = DisplayString
_MibProfIpsec_RecvAh_Key_Object = MibScalar
mibProfIpsec_RecvAh_Key = _MibProfIpsec_RecvAh_Key_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 13),
    _MibProfIpsec_RecvAh_Key_Type()
)
mibProfIpsec_RecvAh_Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvAh_Key.setStatus("mandatory")


class _MibProfIpsec_RecvAh_ReplayProtection_Type(Integer32):
    """Custom type mibProfIpsec_RecvAh_ReplayProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_RecvAh_ReplayProtection_Type.__name__ = "Integer32"
_MibProfIpsec_RecvAh_ReplayProtection_Object = MibScalar
mibProfIpsec_RecvAh_ReplayProtection = _MibProfIpsec_RecvAh_ReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 14),
    _MibProfIpsec_RecvAh_ReplayProtection_Type()
)
mibProfIpsec_RecvAh_ReplayProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvAh_ReplayProtection.setStatus("mandatory")


class _MibProfIpsec_SendEsp_Active_Type(Integer32):
    """Custom type mibProfIpsec_SendEsp_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_SendEsp_Active_Type.__name__ = "Integer32"
_MibProfIpsec_SendEsp_Active_Object = MibScalar
mibProfIpsec_SendEsp_Active = _MibProfIpsec_SendEsp_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 15),
    _MibProfIpsec_SendEsp_Active_Type()
)
mibProfIpsec_SendEsp_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_Active.setStatus("mandatory")
_MibProfIpsec_SendEsp_Spi_Type = Integer32
_MibProfIpsec_SendEsp_Spi_Object = MibScalar
mibProfIpsec_SendEsp_Spi = _MibProfIpsec_SendEsp_Spi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 16),
    _MibProfIpsec_SendEsp_Spi_Type()
)
mibProfIpsec_SendEsp_Spi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_Spi.setStatus("mandatory")
_MibProfIpsec_SendEsp_Version_Type = Integer32
_MibProfIpsec_SendEsp_Version_Object = MibScalar
mibProfIpsec_SendEsp_Version = _MibProfIpsec_SendEsp_Version_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 17),
    _MibProfIpsec_SendEsp_Version_Type()
)
mibProfIpsec_SendEsp_Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_Version.setStatus("mandatory")


class _MibProfIpsec_SendEsp_EspType_Type(Integer32):
    """Custom type mibProfIpsec_SendEsp_EspType based on Integer32"""
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
        *(("desCbc", 2),
          ("n-3desCbc", 3),
          ("n-40desCbc", 4),
          ("none", 1))
    )


_MibProfIpsec_SendEsp_EspType_Type.__name__ = "Integer32"
_MibProfIpsec_SendEsp_EspType_Object = MibScalar
mibProfIpsec_SendEsp_EspType = _MibProfIpsec_SendEsp_EspType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 18),
    _MibProfIpsec_SendEsp_EspType_Type()
)
mibProfIpsec_SendEsp_EspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_EspType.setStatus("mandatory")


class _MibProfIpsec_SendEsp_IvLen_Type(Integer32):
    """Custom type mibProfIpsec_SendEsp_IvLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-32", 2),
          ("n-64", 3))
    )


_MibProfIpsec_SendEsp_IvLen_Type.__name__ = "Integer32"
_MibProfIpsec_SendEsp_IvLen_Object = MibScalar
mibProfIpsec_SendEsp_IvLen = _MibProfIpsec_SendEsp_IvLen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 19),
    _MibProfIpsec_SendEsp_IvLen_Type()
)
mibProfIpsec_SendEsp_IvLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_IvLen.setStatus("mandatory")
_MibProfIpsec_SendEsp_Key_Type = DisplayString
_MibProfIpsec_SendEsp_Key_Object = MibScalar
mibProfIpsec_SendEsp_Key = _MibProfIpsec_SendEsp_Key_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 20),
    _MibProfIpsec_SendEsp_Key_Type()
)
mibProfIpsec_SendEsp_Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_Key.setStatus("mandatory")
_MibProfIpsec_SendEsp_Key2_Type = DisplayString
_MibProfIpsec_SendEsp_Key2_Object = MibScalar
mibProfIpsec_SendEsp_Key2 = _MibProfIpsec_SendEsp_Key2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 21),
    _MibProfIpsec_SendEsp_Key2_Type()
)
mibProfIpsec_SendEsp_Key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_Key2.setStatus("mandatory")
_MibProfIpsec_SendEsp_Key3_Type = DisplayString
_MibProfIpsec_SendEsp_Key3_Object = MibScalar
mibProfIpsec_SendEsp_Key3 = _MibProfIpsec_SendEsp_Key3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 22),
    _MibProfIpsec_SendEsp_Key3_Type()
)
mibProfIpsec_SendEsp_Key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_Key3.setStatus("mandatory")


class _MibProfIpsec_SendEsp_AuthType_Type(Integer32):
    """Custom type mibProfIpsec_SendEsp_AuthType based on Integer32"""
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
        *(("md5", 2),
          ("md5Hmac", 4),
          ("none", 1),
          ("sha1", 3),
          ("sha1Hmac", 5))
    )


_MibProfIpsec_SendEsp_AuthType_Type.__name__ = "Integer32"
_MibProfIpsec_SendEsp_AuthType_Object = MibScalar
mibProfIpsec_SendEsp_AuthType = _MibProfIpsec_SendEsp_AuthType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 23),
    _MibProfIpsec_SendEsp_AuthType_Type()
)
mibProfIpsec_SendEsp_AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_AuthType.setStatus("mandatory")
_MibProfIpsec_SendEsp_AuthKey_Type = DisplayString
_MibProfIpsec_SendEsp_AuthKey_Object = MibScalar
mibProfIpsec_SendEsp_AuthKey = _MibProfIpsec_SendEsp_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 24),
    _MibProfIpsec_SendEsp_AuthKey_Type()
)
mibProfIpsec_SendEsp_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_AuthKey.setStatus("mandatory")


class _MibProfIpsec_SendEsp_ReplayProtection_Type(Integer32):
    """Custom type mibProfIpsec_SendEsp_ReplayProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_SendEsp_ReplayProtection_Type.__name__ = "Integer32"
_MibProfIpsec_SendEsp_ReplayProtection_Object = MibScalar
mibProfIpsec_SendEsp_ReplayProtection = _MibProfIpsec_SendEsp_ReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 25),
    _MibProfIpsec_SendEsp_ReplayProtection_Type()
)
mibProfIpsec_SendEsp_ReplayProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SendEsp_ReplayProtection.setStatus("mandatory")


class _MibProfIpsec_RecvEsp_Active_Type(Integer32):
    """Custom type mibProfIpsec_RecvEsp_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_RecvEsp_Active_Type.__name__ = "Integer32"
_MibProfIpsec_RecvEsp_Active_Object = MibScalar
mibProfIpsec_RecvEsp_Active = _MibProfIpsec_RecvEsp_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 26),
    _MibProfIpsec_RecvEsp_Active_Type()
)
mibProfIpsec_RecvEsp_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_Active.setStatus("mandatory")
_MibProfIpsec_RecvEsp_Spi_Type = Integer32
_MibProfIpsec_RecvEsp_Spi_Object = MibScalar
mibProfIpsec_RecvEsp_Spi = _MibProfIpsec_RecvEsp_Spi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 27),
    _MibProfIpsec_RecvEsp_Spi_Type()
)
mibProfIpsec_RecvEsp_Spi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_Spi.setStatus("mandatory")
_MibProfIpsec_RecvEsp_Version_Type = Integer32
_MibProfIpsec_RecvEsp_Version_Object = MibScalar
mibProfIpsec_RecvEsp_Version = _MibProfIpsec_RecvEsp_Version_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 28),
    _MibProfIpsec_RecvEsp_Version_Type()
)
mibProfIpsec_RecvEsp_Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_Version.setStatus("mandatory")


class _MibProfIpsec_RecvEsp_EspType_Type(Integer32):
    """Custom type mibProfIpsec_RecvEsp_EspType based on Integer32"""
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
        *(("desCbc", 2),
          ("n-3desCbc", 3),
          ("n-40desCbc", 4),
          ("none", 1))
    )


_MibProfIpsec_RecvEsp_EspType_Type.__name__ = "Integer32"
_MibProfIpsec_RecvEsp_EspType_Object = MibScalar
mibProfIpsec_RecvEsp_EspType = _MibProfIpsec_RecvEsp_EspType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 29),
    _MibProfIpsec_RecvEsp_EspType_Type()
)
mibProfIpsec_RecvEsp_EspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_EspType.setStatus("mandatory")


class _MibProfIpsec_RecvEsp_IvLen_Type(Integer32):
    """Custom type mibProfIpsec_RecvEsp_IvLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-32", 2),
          ("n-64", 3))
    )


_MibProfIpsec_RecvEsp_IvLen_Type.__name__ = "Integer32"
_MibProfIpsec_RecvEsp_IvLen_Object = MibScalar
mibProfIpsec_RecvEsp_IvLen = _MibProfIpsec_RecvEsp_IvLen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 30),
    _MibProfIpsec_RecvEsp_IvLen_Type()
)
mibProfIpsec_RecvEsp_IvLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_IvLen.setStatus("mandatory")
_MibProfIpsec_RecvEsp_Key_Type = DisplayString
_MibProfIpsec_RecvEsp_Key_Object = MibScalar
mibProfIpsec_RecvEsp_Key = _MibProfIpsec_RecvEsp_Key_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 31),
    _MibProfIpsec_RecvEsp_Key_Type()
)
mibProfIpsec_RecvEsp_Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_Key.setStatus("mandatory")
_MibProfIpsec_RecvEsp_Key2_Type = DisplayString
_MibProfIpsec_RecvEsp_Key2_Object = MibScalar
mibProfIpsec_RecvEsp_Key2 = _MibProfIpsec_RecvEsp_Key2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 32),
    _MibProfIpsec_RecvEsp_Key2_Type()
)
mibProfIpsec_RecvEsp_Key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_Key2.setStatus("mandatory")
_MibProfIpsec_RecvEsp_Key3_Type = DisplayString
_MibProfIpsec_RecvEsp_Key3_Object = MibScalar
mibProfIpsec_RecvEsp_Key3 = _MibProfIpsec_RecvEsp_Key3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 33),
    _MibProfIpsec_RecvEsp_Key3_Type()
)
mibProfIpsec_RecvEsp_Key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_Key3.setStatus("mandatory")


class _MibProfIpsec_RecvEsp_AuthType_Type(Integer32):
    """Custom type mibProfIpsec_RecvEsp_AuthType based on Integer32"""
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
        *(("md5", 2),
          ("md5Hmac", 4),
          ("none", 1),
          ("sha1", 3),
          ("sha1Hmac", 5))
    )


_MibProfIpsec_RecvEsp_AuthType_Type.__name__ = "Integer32"
_MibProfIpsec_RecvEsp_AuthType_Object = MibScalar
mibProfIpsec_RecvEsp_AuthType = _MibProfIpsec_RecvEsp_AuthType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 34),
    _MibProfIpsec_RecvEsp_AuthType_Type()
)
mibProfIpsec_RecvEsp_AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_AuthType.setStatus("mandatory")
_MibProfIpsec_RecvEsp_AuthKey_Type = DisplayString
_MibProfIpsec_RecvEsp_AuthKey_Object = MibScalar
mibProfIpsec_RecvEsp_AuthKey = _MibProfIpsec_RecvEsp_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 35),
    _MibProfIpsec_RecvEsp_AuthKey_Type()
)
mibProfIpsec_RecvEsp_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_AuthKey.setStatus("mandatory")


class _MibProfIpsec_RecvEsp_ReplayProtection_Type(Integer32):
    """Custom type mibProfIpsec_RecvEsp_ReplayProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfIpsec_RecvEsp_ReplayProtection_Type.__name__ = "Integer32"
_MibProfIpsec_RecvEsp_ReplayProtection_Object = MibScalar
mibProfIpsec_RecvEsp_ReplayProtection = _MibProfIpsec_RecvEsp_ReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 36),
    _MibProfIpsec_RecvEsp_ReplayProtection_Type()
)
mibProfIpsec_RecvEsp_ReplayProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_RecvEsp_ReplayProtection.setStatus("mandatory")


class _MibProfIpsec_Action_o_Type(Integer32):
    """Custom type mibProfIpsec_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MibProfIpsec_Action_o_Type.__name__ = "Integer32"
_MibProfIpsec_Action_o_Object = MibScalar
mibProfIpsec_Action_o = _MibProfIpsec_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 37),
    _MibProfIpsec_Action_o_Type()
)
mibProfIpsec_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_Action_o.setStatus("mandatory")


class _MibProfIpsec_PfsMode_Type(Integer32):
    """Custom type mibProfIpsec_PfsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keys", 2),
          ("keysAndId", 3),
          ("no", 1))
    )


_MibProfIpsec_PfsMode_Type.__name__ = "Integer32"
_MibProfIpsec_PfsMode_Object = MibScalar
mibProfIpsec_PfsMode = _MibProfIpsec_PfsMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 38),
    _MibProfIpsec_PfsMode_Type()
)
mibProfIpsec_PfsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_PfsMode.setStatus("mandatory")
_MibProfIpsec_SaLife_TimeLimit_Type = Integer32
_MibProfIpsec_SaLife_TimeLimit_Object = MibScalar
mibProfIpsec_SaLife_TimeLimit = _MibProfIpsec_SaLife_TimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 39),
    _MibProfIpsec_SaLife_TimeLimit_Type()
)
mibProfIpsec_SaLife_TimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SaLife_TimeLimit.setStatus("mandatory")
_MibProfIpsec_SaLife_SizeLimit_Type = Integer32
_MibProfIpsec_SaLife_SizeLimit_Object = MibScalar
mibProfIpsec_SaLife_SizeLimit = _MibProfIpsec_SaLife_SizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 40),
    _MibProfIpsec_SaLife_SizeLimit_Type()
)
mibProfIpsec_SaLife_SizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SaLife_SizeLimit.setStatus("mandatory")
_MibProfIpsec_SaLife_AnticipateRekey_Type = Integer32
_MibProfIpsec_SaLife_AnticipateRekey_Object = MibScalar
mibProfIpsec_SaLife_AnticipateRekey = _MibProfIpsec_SaLife_AnticipateRekey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 41),
    _MibProfIpsec_SaLife_AnticipateRekey_Type()
)
mibProfIpsec_SaLife_AnticipateRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SaLife_AnticipateRekey.setStatus("mandatory")


class _MibProfIpsec_SaLife_LifeNegotiationFallback_Type(Integer32):
    """Custom type mibProfIpsec_SaLife_LifeNegotiationFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("fail", 1),
          ("notification", 3))
    )


_MibProfIpsec_SaLife_LifeNegotiationFallback_Type.__name__ = "Integer32"
_MibProfIpsec_SaLife_LifeNegotiationFallback_Object = MibScalar
mibProfIpsec_SaLife_LifeNegotiationFallback = _MibProfIpsec_SaLife_LifeNegotiationFallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 42),
    _MibProfIpsec_SaLife_LifeNegotiationFallback_Type()
)
mibProfIpsec_SaLife_LifeNegotiationFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SaLife_LifeNegotiationFallback.setStatus("mandatory")
_MibProfIpsec_SaLife_IdleTimeout_Type = Integer32
_MibProfIpsec_SaLife_IdleTimeout_Object = MibScalar
mibProfIpsec_SaLife_IdleTimeout = _MibProfIpsec_SaLife_IdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 43),
    _MibProfIpsec_SaLife_IdleTimeout_Type()
)
mibProfIpsec_SaLife_IdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_SaLife_IdleTimeout.setStatus("mandatory")
_MibProfIpsec_Next_Type = DisplayString
_MibProfIpsec_Next_Object = MibScalar
mibProfIpsec_Next = _MibProfIpsec_Next_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 85, 1, 1, 44),
    _MibProfIpsec_Next_Type()
)
mibProfIpsec_Next.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsec_Next.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPSEC-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfIpsec": mibmibProfIpsec,
       "mibmibProfIpsecTable": mibmibProfIpsecTable,
       "mibmibProfIpsecEntry": mibmibProfIpsecEntry,
       "mibProfIpsec-Name": mibProfIpsec_Name,
       "mibProfIpsec-Active": mibProfIpsec_Active,
       "mibProfIpsec-EncapMode": mibProfIpsec_EncapMode,
       "mibProfIpsec-TunnelAddress": mibProfIpsec_TunnelAddress,
       "mibProfIpsec-SendAh-Active": mibProfIpsec_SendAh_Active,
       "mibProfIpsec-SendAh-Spi": mibProfIpsec_SendAh_Spi,
       "mibProfIpsec-SendAh-AhType": mibProfIpsec_SendAh_AhType,
       "mibProfIpsec-SendAh-Key": mibProfIpsec_SendAh_Key,
       "mibProfIpsec-SendAh-ReplayProtection": mibProfIpsec_SendAh_ReplayProtection,
       "mibProfIpsec-RecvAh-Active": mibProfIpsec_RecvAh_Active,
       "mibProfIpsec-RecvAh-Spi": mibProfIpsec_RecvAh_Spi,
       "mibProfIpsec-RecvAh-AhType": mibProfIpsec_RecvAh_AhType,
       "mibProfIpsec-RecvAh-Key": mibProfIpsec_RecvAh_Key,
       "mibProfIpsec-RecvAh-ReplayProtection": mibProfIpsec_RecvAh_ReplayProtection,
       "mibProfIpsec-SendEsp-Active": mibProfIpsec_SendEsp_Active,
       "mibProfIpsec-SendEsp-Spi": mibProfIpsec_SendEsp_Spi,
       "mibProfIpsec-SendEsp-Version": mibProfIpsec_SendEsp_Version,
       "mibProfIpsec-SendEsp-EspType": mibProfIpsec_SendEsp_EspType,
       "mibProfIpsec-SendEsp-IvLen": mibProfIpsec_SendEsp_IvLen,
       "mibProfIpsec-SendEsp-Key": mibProfIpsec_SendEsp_Key,
       "mibProfIpsec-SendEsp-Key2": mibProfIpsec_SendEsp_Key2,
       "mibProfIpsec-SendEsp-Key3": mibProfIpsec_SendEsp_Key3,
       "mibProfIpsec-SendEsp-AuthType": mibProfIpsec_SendEsp_AuthType,
       "mibProfIpsec-SendEsp-AuthKey": mibProfIpsec_SendEsp_AuthKey,
       "mibProfIpsec-SendEsp-ReplayProtection": mibProfIpsec_SendEsp_ReplayProtection,
       "mibProfIpsec-RecvEsp-Active": mibProfIpsec_RecvEsp_Active,
       "mibProfIpsec-RecvEsp-Spi": mibProfIpsec_RecvEsp_Spi,
       "mibProfIpsec-RecvEsp-Version": mibProfIpsec_RecvEsp_Version,
       "mibProfIpsec-RecvEsp-EspType": mibProfIpsec_RecvEsp_EspType,
       "mibProfIpsec-RecvEsp-IvLen": mibProfIpsec_RecvEsp_IvLen,
       "mibProfIpsec-RecvEsp-Key": mibProfIpsec_RecvEsp_Key,
       "mibProfIpsec-RecvEsp-Key2": mibProfIpsec_RecvEsp_Key2,
       "mibProfIpsec-RecvEsp-Key3": mibProfIpsec_RecvEsp_Key3,
       "mibProfIpsec-RecvEsp-AuthType": mibProfIpsec_RecvEsp_AuthType,
       "mibProfIpsec-RecvEsp-AuthKey": mibProfIpsec_RecvEsp_AuthKey,
       "mibProfIpsec-RecvEsp-ReplayProtection": mibProfIpsec_RecvEsp_ReplayProtection,
       "mibProfIpsec-Action-o": mibProfIpsec_Action_o,
       "mibProfIpsec-PfsMode": mibProfIpsec_PfsMode,
       "mibProfIpsec-SaLife-TimeLimit": mibProfIpsec_SaLife_TimeLimit,
       "mibProfIpsec-SaLife-SizeLimit": mibProfIpsec_SaLife_SizeLimit,
       "mibProfIpsec-SaLife-AnticipateRekey": mibProfIpsec_SaLife_AnticipateRekey,
       "mibProfIpsec-SaLife-LifeNegotiationFallback": mibProfIpsec_SaLife_LifeNegotiationFallback,
       "mibProfIpsec-SaLife-IdleTimeout": mibProfIpsec_SaLife_IdleTimeout,
       "mibProfIpsec-Next": mibProfIpsec_Next}
)
