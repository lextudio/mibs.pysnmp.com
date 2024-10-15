# SNMP MIB module (SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:44 2024
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

(privateMgmt,) = mibBuilder.importSymbols(
    "SWPRIMGMT-MIB",
    "privateMgmt")


# MODULE-IDENTITY

swSSHMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSSHMgmt_ObjectIdentity = ObjectIdentity
swSSHMgmt = _SwSSHMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1)
)


class _SwSSHAdmin_Type(Integer32):
    """Custom type swSSHAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHAdmin_Type.__name__ = "Integer32"
_SwSSHAdmin_Object = MibScalar
swSSHAdmin = _SwSSHAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 1),
    _SwSSHAdmin_Type()
)
swSSHAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHAdmin.setStatus("current")


class _SwSSHMaxConnections_Type(Integer32):
    """Custom type swSSHMaxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwSSHMaxConnections_Type.__name__ = "Integer32"
_SwSSHMaxConnections_Object = MibScalar
swSSHMaxConnections = _SwSSHMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 2),
    _SwSSHMaxConnections_Type()
)
swSSHMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHMaxConnections.setStatus("current")


class _SwSSHConnectionTimeout_Type(Integer32):
    """Custom type swSSHConnectionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SwSSHConnectionTimeout_Type.__name__ = "Integer32"
_SwSSHConnectionTimeout_Object = MibScalar
swSSHConnectionTimeout = _SwSSHConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 3),
    _SwSSHConnectionTimeout_Type()
)
swSSHConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHConnectionTimeout.setStatus("current")


class _SwSSHMaxAuthFailAttempts_Type(Integer32):
    """Custom type swSSHMaxAuthFailAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_SwSSHMaxAuthFailAttempts_Type.__name__ = "Integer32"
_SwSSHMaxAuthFailAttempts_Object = MibScalar
swSSHMaxAuthFailAttempts = _SwSSHMaxAuthFailAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 4),
    _SwSSHMaxAuthFailAttempts_Type()
)
swSSHMaxAuthFailAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHMaxAuthFailAttempts.setStatus("current")


class _SwSSHSessionKeyRekeying_Type(Integer32):
    """Custom type swSSHSessionKeyRekeying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("sixty-min", 60),
          ("ten-min", 10),
          ("thirty-min", 30))
    )


_SwSSHSessionKeyRekeying_Type.__name__ = "Integer32"
_SwSSHSessionKeyRekeying_Object = MibScalar
swSSHSessionKeyRekeying = _SwSSHSessionKeyRekeying_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 5),
    _SwSSHSessionKeyRekeying_Type()
)
swSSHSessionKeyRekeying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHSessionKeyRekeying.setStatus("current")


class _SwSSHPortNumber_Type(Integer32):
    """Custom type swSSHPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwSSHPortNumber_Type.__name__ = "Integer32"
_SwSSHPortNumber_Object = MibScalar
swSSHPortNumber = _SwSSHPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 6),
    _SwSSHPortNumber_Type()
)
swSSHPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHPortNumber.setStatus("current")


class _SwSSHRegenerateHostKey_Type(Integer32):
    """Custom type swSSHRegenerateHostKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_SwSSHRegenerateHostKey_Type.__name__ = "Integer32"
_SwSSHRegenerateHostKey_Object = MibScalar
swSSHRegenerateHostKey = _SwSSHRegenerateHostKey_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 7),
    _SwSSHRegenerateHostKey_Type()
)
swSSHRegenerateHostKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHRegenerateHostKey.setStatus("current")
_SwSSHCtrlAlgGroup_ObjectIdentity = ObjectIdentity
swSSHCtrlAlgGroup = _SwSSHCtrlAlgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2)
)
_SwSSHEncryptAlgCtrl_ObjectIdentity = ObjectIdentity
swSSHEncryptAlgCtrl = _SwSSHEncryptAlgCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1)
)


class _SwSSHEncryptAlg3DESAdmin_Type(Integer32):
    """Custom type swSSHEncryptAlg3DESAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlg3DESAdmin_Type.__name__ = "Integer32"
_SwSSHEncryptAlg3DESAdmin_Object = MibScalar
swSSHEncryptAlg3DESAdmin = _SwSSHEncryptAlg3DESAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 1),
    _SwSSHEncryptAlg3DESAdmin_Type()
)
swSSHEncryptAlg3DESAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlg3DESAdmin.setStatus("current")


class _SwSSHEncryptAlgBlowfishAdmin_Type(Integer32):
    """Custom type swSSHEncryptAlgBlowfishAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgBlowfishAdmin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgBlowfishAdmin_Object = MibScalar
swSSHEncryptAlgBlowfishAdmin = _SwSSHEncryptAlgBlowfishAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 2),
    _SwSSHEncryptAlgBlowfishAdmin_Type()
)
swSSHEncryptAlgBlowfishAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgBlowfishAdmin.setStatus("current")


class _SwSSHEncryptAlgAES128Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgAES128Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgAES128Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgAES128Admin_Object = MibScalar
swSSHEncryptAlgAES128Admin = _SwSSHEncryptAlgAES128Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 3),
    _SwSSHEncryptAlgAES128Admin_Type()
)
swSSHEncryptAlgAES128Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgAES128Admin.setStatus("current")


class _SwSSHEncryptAlgAES192Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgAES192Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgAES192Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgAES192Admin_Object = MibScalar
swSSHEncryptAlgAES192Admin = _SwSSHEncryptAlgAES192Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 4),
    _SwSSHEncryptAlgAES192Admin_Type()
)
swSSHEncryptAlgAES192Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgAES192Admin.setStatus("current")


class _SwSSHEncryptAlgAES256Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgAES256Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgAES256Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgAES256Admin_Object = MibScalar
swSSHEncryptAlgAES256Admin = _SwSSHEncryptAlgAES256Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 5),
    _SwSSHEncryptAlgAES256Admin_Type()
)
swSSHEncryptAlgAES256Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgAES256Admin.setStatus("current")


class _SwSSHEncryptAlgArcfourAdmin_Type(Integer32):
    """Custom type swSSHEncryptAlgArcfourAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgArcfourAdmin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgArcfourAdmin_Object = MibScalar
swSSHEncryptAlgArcfourAdmin = _SwSSHEncryptAlgArcfourAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 6),
    _SwSSHEncryptAlgArcfourAdmin_Type()
)
swSSHEncryptAlgArcfourAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgArcfourAdmin.setStatus("current")


class _SwSSHEncryptAlgCAST128Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgCAST128Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgCAST128Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgCAST128Admin_Object = MibScalar
swSSHEncryptAlgCAST128Admin = _SwSSHEncryptAlgCAST128Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 7),
    _SwSSHEncryptAlgCAST128Admin_Type()
)
swSSHEncryptAlgCAST128Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgCAST128Admin.setStatus("current")


class _SwSSHEncryptAlgTwofish128Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgTwofish128Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgTwofish128Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgTwofish128Admin_Object = MibScalar
swSSHEncryptAlgTwofish128Admin = _SwSSHEncryptAlgTwofish128Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 8),
    _SwSSHEncryptAlgTwofish128Admin_Type()
)
swSSHEncryptAlgTwofish128Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgTwofish128Admin.setStatus("current")


class _SwSSHEncryptAlgTwofish192Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgTwofish192Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgTwofish192Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgTwofish192Admin_Object = MibScalar
swSSHEncryptAlgTwofish192Admin = _SwSSHEncryptAlgTwofish192Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 9),
    _SwSSHEncryptAlgTwofish192Admin_Type()
)
swSSHEncryptAlgTwofish192Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgTwofish192Admin.setStatus("current")


class _SwSSHEncryptAlgTwofish256Admin_Type(Integer32):
    """Custom type swSSHEncryptAlgTwofish256Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHEncryptAlgTwofish256Admin_Type.__name__ = "Integer32"
_SwSSHEncryptAlgTwofish256Admin_Object = MibScalar
swSSHEncryptAlgTwofish256Admin = _SwSSHEncryptAlgTwofish256Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 10),
    _SwSSHEncryptAlgTwofish256Admin_Type()
)
swSSHEncryptAlgTwofish256Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHEncryptAlgTwofish256Admin.setStatus("current")
_SwSSHAuthenMethodCtrl_ObjectIdentity = ObjectIdentity
swSSHAuthenMethodCtrl = _SwSSHAuthenMethodCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2)
)


class _SwSSHAuthenMethodPasswdAdmin_Type(Integer32):
    """Custom type swSSHAuthenMethodPasswdAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHAuthenMethodPasswdAdmin_Type.__name__ = "Integer32"
_SwSSHAuthenMethodPasswdAdmin_Object = MibScalar
swSSHAuthenMethodPasswdAdmin = _SwSSHAuthenMethodPasswdAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2, 1),
    _SwSSHAuthenMethodPasswdAdmin_Type()
)
swSSHAuthenMethodPasswdAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHAuthenMethodPasswdAdmin.setStatus("current")


class _SwSSHAuthenMethodPubKeyAdmin_Type(Integer32):
    """Custom type swSSHAuthenMethodPubKeyAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHAuthenMethodPubKeyAdmin_Type.__name__ = "Integer32"
_SwSSHAuthenMethodPubKeyAdmin_Object = MibScalar
swSSHAuthenMethodPubKeyAdmin = _SwSSHAuthenMethodPubKeyAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2, 2),
    _SwSSHAuthenMethodPubKeyAdmin_Type()
)
swSSHAuthenMethodPubKeyAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHAuthenMethodPubKeyAdmin.setStatus("current")


class _SwSSHAuthenMethodHostBaseAdmin_Type(Integer32):
    """Custom type swSSHAuthenMethodHostBaseAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHAuthenMethodHostBaseAdmin_Type.__name__ = "Integer32"
_SwSSHAuthenMethodHostBaseAdmin_Object = MibScalar
swSSHAuthenMethodHostBaseAdmin = _SwSSHAuthenMethodHostBaseAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2, 3),
    _SwSSHAuthenMethodHostBaseAdmin_Type()
)
swSSHAuthenMethodHostBaseAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHAuthenMethodHostBaseAdmin.setStatus("current")
_SwSSHInteAlgCtrl_ObjectIdentity = ObjectIdentity
swSSHInteAlgCtrl = _SwSSHInteAlgCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 3)
)


class _SwSSHInteAlgSHA1Admin_Type(Integer32):
    """Custom type swSSHInteAlgSHA1Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHInteAlgSHA1Admin_Type.__name__ = "Integer32"
_SwSSHInteAlgSHA1Admin_Object = MibScalar
swSSHInteAlgSHA1Admin = _SwSSHInteAlgSHA1Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 3, 1),
    _SwSSHInteAlgSHA1Admin_Type()
)
swSSHInteAlgSHA1Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHInteAlgSHA1Admin.setStatus("current")


class _SwSSHInteAlgMD5Admin_Type(Integer32):
    """Custom type swSSHInteAlgMD5Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHInteAlgMD5Admin_Type.__name__ = "Integer32"
_SwSSHInteAlgMD5Admin_Object = MibScalar
swSSHInteAlgMD5Admin = _SwSSHInteAlgMD5Admin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 3, 2),
    _SwSSHInteAlgMD5Admin_Type()
)
swSSHInteAlgMD5Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHInteAlgMD5Admin.setStatus("current")
_SwSSHPubKeyAlgCtrl_ObjectIdentity = ObjectIdentity
swSSHPubKeyAlgCtrl = _SwSSHPubKeyAlgCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 4)
)


class _SwSSHPubKeyAlgDSAAdmin_Type(Integer32):
    """Custom type swSSHPubKeyAlgDSAAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHPubKeyAlgDSAAdmin_Type.__name__ = "Integer32"
_SwSSHPubKeyAlgDSAAdmin_Object = MibScalar
swSSHPubKeyAlgDSAAdmin = _SwSSHPubKeyAlgDSAAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 4, 1),
    _SwSSHPubKeyAlgDSAAdmin_Type()
)
swSSHPubKeyAlgDSAAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHPubKeyAlgDSAAdmin.setStatus("current")


class _SwSSHPubKeyAlgRSAAdmin_Type(Integer32):
    """Custom type swSSHPubKeyAlgRSAAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSHPubKeyAlgRSAAdmin_Type.__name__ = "Integer32"
_SwSSHPubKeyAlgRSAAdmin_Object = MibScalar
swSSHPubKeyAlgRSAAdmin = _SwSSHPubKeyAlgRSAAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 4, 2),
    _SwSSHPubKeyAlgRSAAdmin_Type()
)
swSSHPubKeyAlgRSAAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHPubKeyAlgRSAAdmin.setStatus("current")
_SwSSHUserCtrlTable_Object = MibTable
swSSHUserCtrlTable = _SwSSHUserCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3)
)
if mibBuilder.loadTexts:
    swSSHUserCtrlTable.setStatus("current")
_SwSSHUserCtrlEntry_Object = MibTableRow
swSSHUserCtrlEntry = _SwSSHUserCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1)
)
swSSHUserCtrlEntry.setIndexNames(
    (0, "SSH-MIB", "swSSHUserCtrlUserName"),
)
if mibBuilder.loadTexts:
    swSSHUserCtrlEntry.setStatus("current")


class _SwSSHUserCtrlUserName_Type(DisplayString):
    """Custom type swSSHUserCtrlUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwSSHUserCtrlUserName_Type.__name__ = "DisplayString"
_SwSSHUserCtrlUserName_Object = MibTableColumn
swSSHUserCtrlUserName = _SwSSHUserCtrlUserName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 1),
    _SwSSHUserCtrlUserName_Type()
)
swSSHUserCtrlUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSSHUserCtrlUserName.setStatus("current")


class _SwSSHUserCtrlAuthMode_Type(Integer32):
    """Custom type swSSHUserCtrlAuthMode based on Integer32"""
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
        *(("hostbased", 4),
          ("none", 1),
          ("password", 3),
          ("publickey", 2))
    )


_SwSSHUserCtrlAuthMode_Type.__name__ = "Integer32"
_SwSSHUserCtrlAuthMode_Object = MibTableColumn
swSSHUserCtrlAuthMode = _SwSSHUserCtrlAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 2),
    _SwSSHUserCtrlAuthMode_Type()
)
swSSHUserCtrlAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHUserCtrlAuthMode.setStatus("current")


class _SwSSHUserCtrlHostName_Type(DisplayString):
    """Custom type swSSHUserCtrlHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSSHUserCtrlHostName_Type.__name__ = "DisplayString"
_SwSSHUserCtrlHostName_Object = MibTableColumn
swSSHUserCtrlHostName = _SwSSHUserCtrlHostName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 3),
    _SwSSHUserCtrlHostName_Type()
)
swSSHUserCtrlHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHUserCtrlHostName.setStatus("current")
_SwSSHUserCtrlHostIp_Type = IpAddress
_SwSSHUserCtrlHostIp_Object = MibTableColumn
swSSHUserCtrlHostIp = _SwSSHUserCtrlHostIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 4),
    _SwSSHUserCtrlHostIp_Type()
)
swSSHUserCtrlHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSHUserCtrlHostIp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SSH-MIB",
    **{"swSSHMIB": swSSHMIB,
       "swSSHMgmt": swSSHMgmt,
       "swSSHAdmin": swSSHAdmin,
       "swSSHMaxConnections": swSSHMaxConnections,
       "swSSHConnectionTimeout": swSSHConnectionTimeout,
       "swSSHMaxAuthFailAttempts": swSSHMaxAuthFailAttempts,
       "swSSHSessionKeyRekeying": swSSHSessionKeyRekeying,
       "swSSHPortNumber": swSSHPortNumber,
       "swSSHRegenerateHostKey": swSSHRegenerateHostKey,
       "swSSHCtrlAlgGroup": swSSHCtrlAlgGroup,
       "swSSHEncryptAlgCtrl": swSSHEncryptAlgCtrl,
       "swSSHEncryptAlg3DESAdmin": swSSHEncryptAlg3DESAdmin,
       "swSSHEncryptAlgBlowfishAdmin": swSSHEncryptAlgBlowfishAdmin,
       "swSSHEncryptAlgAES128Admin": swSSHEncryptAlgAES128Admin,
       "swSSHEncryptAlgAES192Admin": swSSHEncryptAlgAES192Admin,
       "swSSHEncryptAlgAES256Admin": swSSHEncryptAlgAES256Admin,
       "swSSHEncryptAlgArcfourAdmin": swSSHEncryptAlgArcfourAdmin,
       "swSSHEncryptAlgCAST128Admin": swSSHEncryptAlgCAST128Admin,
       "swSSHEncryptAlgTwofish128Admin": swSSHEncryptAlgTwofish128Admin,
       "swSSHEncryptAlgTwofish192Admin": swSSHEncryptAlgTwofish192Admin,
       "swSSHEncryptAlgTwofish256Admin": swSSHEncryptAlgTwofish256Admin,
       "swSSHAuthenMethodCtrl": swSSHAuthenMethodCtrl,
       "swSSHAuthenMethodPasswdAdmin": swSSHAuthenMethodPasswdAdmin,
       "swSSHAuthenMethodPubKeyAdmin": swSSHAuthenMethodPubKeyAdmin,
       "swSSHAuthenMethodHostBaseAdmin": swSSHAuthenMethodHostBaseAdmin,
       "swSSHInteAlgCtrl": swSSHInteAlgCtrl,
       "swSSHInteAlgSHA1Admin": swSSHInteAlgSHA1Admin,
       "swSSHInteAlgMD5Admin": swSSHInteAlgMD5Admin,
       "swSSHPubKeyAlgCtrl": swSSHPubKeyAlgCtrl,
       "swSSHPubKeyAlgDSAAdmin": swSSHPubKeyAlgDSAAdmin,
       "swSSHPubKeyAlgRSAAdmin": swSSHPubKeyAlgRSAAdmin,
       "swSSHUserCtrlTable": swSSHUserCtrlTable,
       "swSSHUserCtrlEntry": swSSHUserCtrlEntry,
       "swSSHUserCtrlUserName": swSSHUserCtrlUserName,
       "swSSHUserCtrlAuthMode": swSSHUserCtrlAuthMode,
       "swSSHUserCtrlHostName": swSSHUserCtrlHostName,
       "swSSHUserCtrlHostIp": swSSHUserCtrlHostIp}
)
