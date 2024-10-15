# SNMP MIB module (BIANCA-BRICK-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-SEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:45 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bintecsec_ObjectIdentity = ObjectIdentity
bintecsec = _Bintecsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254)
)


class _BiboAdmAdminCommunity_Type(DisplayString):
    """Custom type biboAdmAdminCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmAdminCommunity_Type.__name__ = "DisplayString"
_BiboAdmAdminCommunity_Object = MibScalar
biboAdmAdminCommunity = _BiboAdmAdminCommunity_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 1),
    _BiboAdmAdminCommunity_Type()
)
biboAdmAdminCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmAdminCommunity.setStatus("mandatory")


class _BiboAdmReadCommunity_Type(DisplayString):
    """Custom type biboAdmReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmReadCommunity_Type.__name__ = "DisplayString"
_BiboAdmReadCommunity_Object = MibScalar
biboAdmReadCommunity = _BiboAdmReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 2),
    _BiboAdmReadCommunity_Type()
)
biboAdmReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmReadCommunity.setStatus("mandatory")


class _BiboAdmWriteCommunity_Type(DisplayString):
    """Custom type biboAdmWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmWriteCommunity_Type.__name__ = "DisplayString"
_BiboAdmWriteCommunity_Object = MibScalar
biboAdmWriteCommunity = _BiboAdmWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 3),
    _BiboAdmWriteCommunity_Type()
)
biboAdmWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmWriteCommunity.setStatus("mandatory")
_BiboAdmLicenseTable_Object = MibTable
biboAdmLicenseTable = _BiboAdmLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4)
)
if mibBuilder.loadTexts:
    biboAdmLicenseTable.setStatus("mandatory")
_BiboAdmLicenseEntry_Object = MibTableRow
biboAdmLicenseEntry = _BiboAdmLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1)
)
biboAdmLicenseEntry.setIndexNames(
    (0, "BIANCA-BRICK-SEC-MIB", "biboAdmLicenseKey"),
)
if mibBuilder.loadTexts:
    biboAdmLicenseEntry.setStatus("mandatory")


class _BiboAdmLicenseSerialNumber_Type(Integer32):
    """Custom type biboAdmLicenseSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BiboAdmLicenseSerialNumber_Type.__name__ = "Integer32"
_BiboAdmLicenseSerialNumber_Object = MibTableColumn
biboAdmLicenseSerialNumber = _BiboAdmLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 1),
    _BiboAdmLicenseSerialNumber_Type()
)
biboAdmLicenseSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLicenseSerialNumber.setStatus("mandatory")


class _BiboAdmLicenseMask_Type(Integer32):
    """Custom type biboAdmLicenseMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboAdmLicenseMask_Type.__name__ = "Integer32"
_BiboAdmLicenseMask_Object = MibTableColumn
biboAdmLicenseMask = _BiboAdmLicenseMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 2),
    _BiboAdmLicenseMask_Type()
)
biboAdmLicenseMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLicenseMask.setStatus("mandatory")
_BiboAdmLicenseKey_Type = DisplayString
_BiboAdmLicenseKey_Object = MibTableColumn
biboAdmLicenseKey = _BiboAdmLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 3),
    _BiboAdmLicenseKey_Type()
)
biboAdmLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLicenseKey.setStatus("mandatory")


class _BiboAdmLicenseState_Type(Integer32):
    """Custom type biboAdmLicenseState based on Integer32"""
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
        *(("delete", 3),
          ("internal-erase", 5),
          ("internal-ok", 4),
          ("not-ok", 2),
          ("not-supported", 6),
          ("ok", 1))
    )


_BiboAdmLicenseState_Type.__name__ = "Integer32"
_BiboAdmLicenseState_Object = MibTableColumn
biboAdmLicenseState = _BiboAdmLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 4),
    _BiboAdmLicenseState_Type()
)
biboAdmLicenseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLicenseState.setStatus("mandatory")
_BiboAdmLicenseSerialId_Type = DisplayString
_BiboAdmLicenseSerialId_Object = MibTableColumn
biboAdmLicenseSerialId = _BiboAdmLicenseSerialId_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 5),
    _BiboAdmLicenseSerialId_Type()
)
biboAdmLicenseSerialId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLicenseSerialId.setStatus("mandatory")
_BiboAdmLicenseHwSerial_Type = DisplayString
_BiboAdmLicenseHwSerial_Object = MibTableColumn
biboAdmLicenseHwSerial = _BiboAdmLicenseHwSerial_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 6),
    _BiboAdmLicenseHwSerial_Type()
)
biboAdmLicenseHwSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicenseHwSerial.setStatus("mandatory")


class _BiboAdmLicenseLicType_Type(Integer32):
    """Custom type biboAdmLicenseLicType based on Integer32"""
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
              33,
              128,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("bri", 129),
          ("bridge", 3),
          ("capi", 2),
          ("ethernet", 128),
          ("extended-lan", 10),
          ("extended-wan", 13),
          ("frame-relay", 7),
          ("g703", 130),
          ("ip", 1),
          ("ipsec", 33),
          ("ipx", 5),
          ("leased-line", 14),
          ("modem", 132),
          ("ospf", 9),
          ("pri", 131),
          ("stac", 6),
          ("taf", 12),
          ("tapi", 8),
          ("tunneling", 11),
          ("x25", 4))
    )


_BiboAdmLicenseLicType_Type.__name__ = "Integer32"
_BiboAdmLicenseLicType_Object = MibTableColumn
biboAdmLicenseLicType = _BiboAdmLicenseLicType_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 7),
    _BiboAdmLicenseLicType_Type()
)
biboAdmLicenseLicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicenseLicType.setStatus("mandatory")


class _BiboAdmRadiusSecret_Type(DisplayString):
    """Custom type biboAdmRadiusSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmRadiusSecret_Type.__name__ = "DisplayString"
_BiboAdmRadiusSecret_Object = MibScalar
biboAdmRadiusSecret = _BiboAdmRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 5),
    _BiboAdmRadiusSecret_Type()
)
biboAdmRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmRadiusSecret.setStatus("mandatory")


class _BiboAdmHttpPassword_Type(DisplayString):
    """Custom type biboAdmHttpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmHttpPassword_Type.__name__ = "DisplayString"
_BiboAdmHttpPassword_Object = MibScalar
biboAdmHttpPassword = _BiboAdmHttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 6),
    _BiboAdmHttpPassword_Type()
)
biboAdmHttpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmHttpPassword.setStatus("mandatory")
_BiboAdmLoginTable_Object = MibTable
biboAdmLoginTable = _BiboAdmLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 7)
)
if mibBuilder.loadTexts:
    biboAdmLoginTable.setStatus("mandatory")
_BiboAdmLoginEntry_Object = MibTableRow
biboAdmLoginEntry = _BiboAdmLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 7, 1)
)
biboAdmLoginEntry.setIndexNames(
    (0, "BIANCA-BRICK-SEC-MIB", "biboAdmLoginUser"),
)
if mibBuilder.loadTexts:
    biboAdmLoginEntry.setStatus("mandatory")
_BiboAdmLoginUser_Type = DisplayString
_BiboAdmLoginUser_Object = MibTableColumn
biboAdmLoginUser = _BiboAdmLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 1),
    _BiboAdmLoginUser_Type()
)
biboAdmLoginUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLoginUser.setStatus("mandatory")
_BiboAdmLoginPassword_Type = DisplayString
_BiboAdmLoginPassword_Object = MibTableColumn
biboAdmLoginPassword = _BiboAdmLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 2),
    _BiboAdmLoginPassword_Type()
)
biboAdmLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLoginPassword.setStatus("mandatory")
_BiboAdmLoginCommand_Type = DisplayString
_BiboAdmLoginCommand_Object = MibTableColumn
biboAdmLoginCommand = _BiboAdmLoginCommand_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 3),
    _BiboAdmLoginCommand_Type()
)
biboAdmLoginCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLoginCommand.setStatus("mandatory")


class _BiboAdmLoginState_Type(Integer32):
    """Custom type biboAdmLoginState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("invalid", 3),
          ("valid", 1))
    )


_BiboAdmLoginState_Type.__name__ = "Integer32"
_BiboAdmLoginState_Object = MibTableColumn
biboAdmLoginState = _BiboAdmLoginState_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 4),
    _BiboAdmLoginState_Type()
)
biboAdmLoginState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLoginState.setStatus("mandatory")
_BiboAdmPublicKey_Type = OctetString
_BiboAdmPublicKey_Object = MibScalar
biboAdmPublicKey = _BiboAdmPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 10),
    _BiboAdmPublicKey_Type()
)
biboAdmPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmPublicKey.setStatus("mandatory")
_BiboAdmPrivateKey_Type = OctetString
_BiboAdmPrivateKey_Object = MibScalar
biboAdmPrivateKey = _BiboAdmPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 11),
    _BiboAdmPrivateKey_Type()
)
biboAdmPrivateKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    biboAdmPrivateKey.setStatus("mandatory")


class _BiboAdmActMonPassword_Type(DisplayString):
    """Custom type biboAdmActMonPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmActMonPassword_Type.__name__ = "DisplayString"
_BiboAdmActMonPassword_Object = MibScalar
biboAdmActMonPassword = _BiboAdmActMonPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 12),
    _BiboAdmActMonPassword_Type()
)
biboAdmActMonPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmActMonPassword.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-SEC-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bintecsec": bintecsec,
       "biboAdmAdminCommunity": biboAdmAdminCommunity,
       "biboAdmReadCommunity": biboAdmReadCommunity,
       "biboAdmWriteCommunity": biboAdmWriteCommunity,
       "biboAdmLicenseTable": biboAdmLicenseTable,
       "biboAdmLicenseEntry": biboAdmLicenseEntry,
       "biboAdmLicenseSerialNumber": biboAdmLicenseSerialNumber,
       "biboAdmLicenseMask": biboAdmLicenseMask,
       "biboAdmLicenseKey": biboAdmLicenseKey,
       "biboAdmLicenseState": biboAdmLicenseState,
       "biboAdmLicenseSerialId": biboAdmLicenseSerialId,
       "biboAdmLicenseHwSerial": biboAdmLicenseHwSerial,
       "biboAdmLicenseLicType": biboAdmLicenseLicType,
       "biboAdmRadiusSecret": biboAdmRadiusSecret,
       "biboAdmHttpPassword": biboAdmHttpPassword,
       "biboAdmLoginTable": biboAdmLoginTable,
       "biboAdmLoginEntry": biboAdmLoginEntry,
       "biboAdmLoginUser": biboAdmLoginUser,
       "biboAdmLoginPassword": biboAdmLoginPassword,
       "biboAdmLoginCommand": biboAdmLoginCommand,
       "biboAdmLoginState": biboAdmLoginState,
       "biboAdmPublicKey": biboAdmPublicKey,
       "biboAdmPrivateKey": biboAdmPrivateKey,
       "biboAdmActMonPassword": biboAdmActMonPassword}
)
