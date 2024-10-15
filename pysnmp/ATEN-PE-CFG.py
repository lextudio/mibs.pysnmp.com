# SNMP MIB module (ATEN-PE-CFG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATEN-PE-CFG
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:40 2024
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

(KeyChange,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "KeyChange")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aten = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21317)
)
aten.setRevisions(
        ("2013-10-31 11:10",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtenProducts_ObjectIdentity = ObjectIdentity
atenProducts = _AtenProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1)
)
_Overip_ObjectIdentity = ObjectIdentity
overip = _Overip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3)
)
_Poweroverip_ObjectIdentity = ObjectIdentity
poweroverip = _Poweroverip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2)
)
_Pe_ObjectIdentity = ObjectIdentity
pe = _Pe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2)
)
_UserManagement_ObjectIdentity = ObjectIdentity
userManagement = _UserManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1)
)
_UsrListTable_Object = MibTable
usrListTable = _UsrListTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usrListTable.setStatus("current")
_UsrListEntry_Object = MibTableRow
usrListEntry = _UsrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1)
)
usrListEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "usrIndex"),
)
if mibBuilder.loadTexts:
    usrListEntry.setStatus("current")


class _UsrIndex_Type(Integer32):
    """Custom type usrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_UsrIndex_Type.__name__ = "Integer32"
_UsrIndex_Object = MibTableColumn
usrIndex = _UsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 1),
    _UsrIndex_Type()
)
usrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrIndex.setStatus("current")


class _UsrType_Type(Integer32):
    """Custom type usrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 1),
          ("user", 2))
    )


_UsrType_Type.__name__ = "Integer32"
_UsrType_Object = MibTableColumn
usrType = _UsrType_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 2),
    _UsrType_Type()
)
usrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrType.setStatus("current")


class _UsrName_Type(DisplayString):
    """Custom type usrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UsrName_Type.__name__ = "DisplayString"
_UsrName_Object = MibTableColumn
usrName = _UsrName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 3),
    _UsrName_Type()
)
usrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrName.setStatus("current")


class _UsrPassword_Type(DisplayString):
    """Custom type usrPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UsrPassword_Type.__name__ = "DisplayString"
_UsrPassword_Object = MibTableColumn
usrPassword = _UsrPassword_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 4),
    _UsrPassword_Type()
)
usrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPassword.setStatus("current")


class _UsrPort1Auth_Type(Integer32):
    """Custom type usrPort1Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort1Auth_Type.__name__ = "Integer32"
_UsrPort1Auth_Object = MibTableColumn
usrPort1Auth = _UsrPort1Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 5),
    _UsrPort1Auth_Type()
)
usrPort1Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort1Auth.setStatus("current")


class _UsrPort2Auth_Type(Integer32):
    """Custom type usrPort2Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort2Auth_Type.__name__ = "Integer32"
_UsrPort2Auth_Object = MibTableColumn
usrPort2Auth = _UsrPort2Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 6),
    _UsrPort2Auth_Type()
)
usrPort2Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort2Auth.setStatus("current")


class _UsrPort3Auth_Type(Integer32):
    """Custom type usrPort3Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort3Auth_Type.__name__ = "Integer32"
_UsrPort3Auth_Object = MibTableColumn
usrPort3Auth = _UsrPort3Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 7),
    _UsrPort3Auth_Type()
)
usrPort3Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort3Auth.setStatus("current")


class _UsrPort4Auth_Type(Integer32):
    """Custom type usrPort4Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort4Auth_Type.__name__ = "Integer32"
_UsrPort4Auth_Object = MibTableColumn
usrPort4Auth = _UsrPort4Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 8),
    _UsrPort4Auth_Type()
)
usrPort4Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort4Auth.setStatus("current")


class _UsrPort5Auth_Type(Integer32):
    """Custom type usrPort5Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort5Auth_Type.__name__ = "Integer32"
_UsrPort5Auth_Object = MibTableColumn
usrPort5Auth = _UsrPort5Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 9),
    _UsrPort5Auth_Type()
)
usrPort5Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort5Auth.setStatus("current")


class _UsrPort6Auth_Type(Integer32):
    """Custom type usrPort6Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort6Auth_Type.__name__ = "Integer32"
_UsrPort6Auth_Object = MibTableColumn
usrPort6Auth = _UsrPort6Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 10),
    _UsrPort6Auth_Type()
)
usrPort6Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort6Auth.setStatus("current")


class _UsrPort7Auth_Type(Integer32):
    """Custom type usrPort7Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort7Auth_Type.__name__ = "Integer32"
_UsrPort7Auth_Object = MibTableColumn
usrPort7Auth = _UsrPort7Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 11),
    _UsrPort7Auth_Type()
)
usrPort7Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort7Auth.setStatus("current")


class _UsrPort8Auth_Type(Integer32):
    """Custom type usrPort8Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort8Auth_Type.__name__ = "Integer32"
_UsrPort8Auth_Object = MibTableColumn
usrPort8Auth = _UsrPort8Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 12),
    _UsrPort8Auth_Type()
)
usrPort8Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort8Auth.setStatus("current")


class _UsrPort9Auth_Type(Integer32):
    """Custom type usrPort9Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort9Auth_Type.__name__ = "Integer32"
_UsrPort9Auth_Object = MibTableColumn
usrPort9Auth = _UsrPort9Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 13),
    _UsrPort9Auth_Type()
)
usrPort9Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort9Auth.setStatus("current")


class _UsrPort10Auth_Type(Integer32):
    """Custom type usrPort10Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort10Auth_Type.__name__ = "Integer32"
_UsrPort10Auth_Object = MibTableColumn
usrPort10Auth = _UsrPort10Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 14),
    _UsrPort10Auth_Type()
)
usrPort10Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort10Auth.setStatus("current")


class _UsrPort11Auth_Type(Integer32):
    """Custom type usrPort11Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort11Auth_Type.__name__ = "Integer32"
_UsrPort11Auth_Object = MibTableColumn
usrPort11Auth = _UsrPort11Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 15),
    _UsrPort11Auth_Type()
)
usrPort11Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort11Auth.setStatus("current")


class _UsrPort12Auth_Type(Integer32):
    """Custom type usrPort12Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort12Auth_Type.__name__ = "Integer32"
_UsrPort12Auth_Object = MibTableColumn
usrPort12Auth = _UsrPort12Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 16),
    _UsrPort12Auth_Type()
)
usrPort12Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort12Auth.setStatus("current")


class _UsrPort13Auth_Type(Integer32):
    """Custom type usrPort13Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort13Auth_Type.__name__ = "Integer32"
_UsrPort13Auth_Object = MibTableColumn
usrPort13Auth = _UsrPort13Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 17),
    _UsrPort13Auth_Type()
)
usrPort13Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort13Auth.setStatus("current")


class _UsrPort14Auth_Type(Integer32):
    """Custom type usrPort14Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort14Auth_Type.__name__ = "Integer32"
_UsrPort14Auth_Object = MibTableColumn
usrPort14Auth = _UsrPort14Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 18),
    _UsrPort14Auth_Type()
)
usrPort14Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort14Auth.setStatus("current")


class _UsrPort15Auth_Type(Integer32):
    """Custom type usrPort15Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort15Auth_Type.__name__ = "Integer32"
_UsrPort15Auth_Object = MibTableColumn
usrPort15Auth = _UsrPort15Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 19),
    _UsrPort15Auth_Type()
)
usrPort15Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort15Auth.setStatus("current")


class _UsrPort16Auth_Type(Integer32):
    """Custom type usrPort16Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort16Auth_Type.__name__ = "Integer32"
_UsrPort16Auth_Object = MibTableColumn
usrPort16Auth = _UsrPort16Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 20),
    _UsrPort16Auth_Type()
)
usrPort16Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort16Auth.setStatus("current")


class _UsrPort17Auth_Type(Integer32):
    """Custom type usrPort17Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort17Auth_Type.__name__ = "Integer32"
_UsrPort17Auth_Object = MibTableColumn
usrPort17Auth = _UsrPort17Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 21),
    _UsrPort17Auth_Type()
)
usrPort17Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort17Auth.setStatus("current")


class _UsrPort18Auth_Type(Integer32):
    """Custom type usrPort18Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort18Auth_Type.__name__ = "Integer32"
_UsrPort18Auth_Object = MibTableColumn
usrPort18Auth = _UsrPort18Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 22),
    _UsrPort18Auth_Type()
)
usrPort18Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort18Auth.setStatus("current")


class _UsrPort19Auth_Type(Integer32):
    """Custom type usrPort19Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort19Auth_Type.__name__ = "Integer32"
_UsrPort19Auth_Object = MibTableColumn
usrPort19Auth = _UsrPort19Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 23),
    _UsrPort19Auth_Type()
)
usrPort19Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort19Auth.setStatus("current")


class _UsrPort20Auth_Type(Integer32):
    """Custom type usrPort20Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort20Auth_Type.__name__ = "Integer32"
_UsrPort20Auth_Object = MibTableColumn
usrPort20Auth = _UsrPort20Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 24),
    _UsrPort20Auth_Type()
)
usrPort20Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort20Auth.setStatus("current")


class _UsrPort21Auth_Type(Integer32):
    """Custom type usrPort21Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort21Auth_Type.__name__ = "Integer32"
_UsrPort21Auth_Object = MibTableColumn
usrPort21Auth = _UsrPort21Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 25),
    _UsrPort21Auth_Type()
)
usrPort21Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort21Auth.setStatus("current")


class _UsrPort22Auth_Type(Integer32):
    """Custom type usrPort22Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort22Auth_Type.__name__ = "Integer32"
_UsrPort22Auth_Object = MibTableColumn
usrPort22Auth = _UsrPort22Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 26),
    _UsrPort22Auth_Type()
)
usrPort22Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort22Auth.setStatus("current")


class _UsrPort23Auth_Type(Integer32):
    """Custom type usrPort23Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort23Auth_Type.__name__ = "Integer32"
_UsrPort23Auth_Object = MibTableColumn
usrPort23Auth = _UsrPort23Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 27),
    _UsrPort23Auth_Type()
)
usrPort23Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort23Auth.setStatus("current")


class _UsrPort24Auth_Type(Integer32):
    """Custom type usrPort24Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort24Auth_Type.__name__ = "Integer32"
_UsrPort24Auth_Object = MibTableColumn
usrPort24Auth = _UsrPort24Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 28),
    _UsrPort24Auth_Type()
)
usrPort24Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort24Auth.setStatus("current")


class _UsrPort25Auth_Type(Integer32):
    """Custom type usrPort25Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort25Auth_Type.__name__ = "Integer32"
_UsrPort25Auth_Object = MibTableColumn
usrPort25Auth = _UsrPort25Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 29),
    _UsrPort25Auth_Type()
)
usrPort25Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort25Auth.setStatus("current")


class _UsrPort26Auth_Type(Integer32):
    """Custom type usrPort26Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort26Auth_Type.__name__ = "Integer32"
_UsrPort26Auth_Object = MibTableColumn
usrPort26Auth = _UsrPort26Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 30),
    _UsrPort26Auth_Type()
)
usrPort26Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort26Auth.setStatus("current")


class _UsrPort27Auth_Type(Integer32):
    """Custom type usrPort27Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort27Auth_Type.__name__ = "Integer32"
_UsrPort27Auth_Object = MibTableColumn
usrPort27Auth = _UsrPort27Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 31),
    _UsrPort27Auth_Type()
)
usrPort27Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort27Auth.setStatus("current")


class _UsrPort28Auth_Type(Integer32):
    """Custom type usrPort28Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort28Auth_Type.__name__ = "Integer32"
_UsrPort28Auth_Object = MibTableColumn
usrPort28Auth = _UsrPort28Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 32),
    _UsrPort28Auth_Type()
)
usrPort28Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort28Auth.setStatus("current")


class _UsrPort29Auth_Type(Integer32):
    """Custom type usrPort29Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort29Auth_Type.__name__ = "Integer32"
_UsrPort29Auth_Object = MibTableColumn
usrPort29Auth = _UsrPort29Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 33),
    _UsrPort29Auth_Type()
)
usrPort29Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort29Auth.setStatus("current")


class _UsrPort30Auth_Type(Integer32):
    """Custom type usrPort30Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort30Auth_Type.__name__ = "Integer32"
_UsrPort30Auth_Object = MibTableColumn
usrPort30Auth = _UsrPort30Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 34),
    _UsrPort30Auth_Type()
)
usrPort30Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort30Auth.setStatus("current")


class _UsrPort31Auth_Type(Integer32):
    """Custom type usrPort31Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort31Auth_Type.__name__ = "Integer32"
_UsrPort31Auth_Object = MibTableColumn
usrPort31Auth = _UsrPort31Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 35),
    _UsrPort31Auth_Type()
)
usrPort31Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort31Auth.setStatus("current")


class _UsrPort32Auth_Type(Integer32):
    """Custom type usrPort32Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort32Auth_Type.__name__ = "Integer32"
_UsrPort32Auth_Object = MibTableColumn
usrPort32Auth = _UsrPort32Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 36),
    _UsrPort32Auth_Type()
)
usrPort32Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort32Auth.setStatus("current")


class _UsrPort33Auth_Type(Integer32):
    """Custom type usrPort33Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort33Auth_Type.__name__ = "Integer32"
_UsrPort33Auth_Object = MibTableColumn
usrPort33Auth = _UsrPort33Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 37),
    _UsrPort33Auth_Type()
)
usrPort33Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort33Auth.setStatus("current")


class _UsrPort34Auth_Type(Integer32):
    """Custom type usrPort34Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort34Auth_Type.__name__ = "Integer32"
_UsrPort34Auth_Object = MibTableColumn
usrPort34Auth = _UsrPort34Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 38),
    _UsrPort34Auth_Type()
)
usrPort34Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort34Auth.setStatus("current")


class _UsrPort35Auth_Type(Integer32):
    """Custom type usrPort35Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort35Auth_Type.__name__ = "Integer32"
_UsrPort35Auth_Object = MibTableColumn
usrPort35Auth = _UsrPort35Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 39),
    _UsrPort35Auth_Type()
)
usrPort35Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort35Auth.setStatus("current")


class _UsrPort36Auth_Type(Integer32):
    """Custom type usrPort36Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort36Auth_Type.__name__ = "Integer32"
_UsrPort36Auth_Object = MibTableColumn
usrPort36Auth = _UsrPort36Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 40),
    _UsrPort36Auth_Type()
)
usrPort36Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort36Auth.setStatus("current")


class _UsrPort37Auth_Type(Integer32):
    """Custom type usrPort37Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort37Auth_Type.__name__ = "Integer32"
_UsrPort37Auth_Object = MibTableColumn
usrPort37Auth = _UsrPort37Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 41),
    _UsrPort37Auth_Type()
)
usrPort37Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort37Auth.setStatus("current")


class _UsrPort38Auth_Type(Integer32):
    """Custom type usrPort38Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort38Auth_Type.__name__ = "Integer32"
_UsrPort38Auth_Object = MibTableColumn
usrPort38Auth = _UsrPort38Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 42),
    _UsrPort38Auth_Type()
)
usrPort38Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort38Auth.setStatus("current")


class _UsrPort39Auth_Type(Integer32):
    """Custom type usrPort39Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort39Auth_Type.__name__ = "Integer32"
_UsrPort39Auth_Object = MibTableColumn
usrPort39Auth = _UsrPort39Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 43),
    _UsrPort39Auth_Type()
)
usrPort39Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort39Auth.setStatus("current")


class _UsrPort40Auth_Type(Integer32):
    """Custom type usrPort40Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort40Auth_Type.__name__ = "Integer32"
_UsrPort40Auth_Object = MibTableColumn
usrPort40Auth = _UsrPort40Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 44),
    _UsrPort40Auth_Type()
)
usrPort40Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort40Auth.setStatus("current")


class _UsrPort41Auth_Type(Integer32):
    """Custom type usrPort41Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort41Auth_Type.__name__ = "Integer32"
_UsrPort41Auth_Object = MibTableColumn
usrPort41Auth = _UsrPort41Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 45),
    _UsrPort41Auth_Type()
)
usrPort41Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort41Auth.setStatus("current")


class _UsrPort42Auth_Type(Integer32):
    """Custom type usrPort42Auth based on Integer32"""
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
        *(("disable", 1),
          ("modify", 3),
          ("not-support", 4),
          ("view", 2))
    )


_UsrPort42Auth_Type.__name__ = "Integer32"
_UsrPort42Auth_Object = MibTableColumn
usrPort42Auth = _UsrPort42Auth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 46),
    _UsrPort42Auth_Type()
)
usrPort42Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrPort42Auth.setStatus("current")


class _UsrEnable_Type(Integer32):
    """Custom type usrEnable based on Integer32"""
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


_UsrEnable_Type.__name__ = "Integer32"
_UsrEnable_Object = MibTableColumn
usrEnable = _UsrEnable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 1, 1, 1, 47),
    _UsrEnable_Type()
)
usrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrEnable.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1)
)
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 1),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceValueTable_Object = MibTable
deviceValueTable = _DeviceValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    deviceValueTable.setStatus("current")
_DeviceValueEntry_Object = MibTableRow
deviceValueEntry = _DeviceValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1)
)
deviceValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "deviceValueIndex"),
)
if mibBuilder.loadTexts:
    deviceValueEntry.setStatus("current")


class _DeviceValueIndex_Type(Integer32):
    """Custom type deviceValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DeviceValueIndex_Type.__name__ = "Integer32"
_DeviceValueIndex_Object = MibTableColumn
deviceValueIndex = _DeviceValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 1),
    _DeviceValueIndex_Type()
)
deviceValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceValueIndex.setStatus("current")
_DeviceCurrent_Type = DisplayString
_DeviceCurrent_Object = MibTableColumn
deviceCurrent = _DeviceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 2),
    _DeviceCurrent_Type()
)
deviceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCurrent.setStatus("current")
_DeviceVoltage_Type = DisplayString
_DeviceVoltage_Object = MibTableColumn
deviceVoltage = _DeviceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 3),
    _DeviceVoltage_Type()
)
deviceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVoltage.setStatus("current")
_DevicePower_Type = DisplayString
_DevicePower_Object = MibTableColumn
devicePower = _DevicePower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 4),
    _DevicePower_Type()
)
devicePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePower.setStatus("current")
_DevicePowerDissipation_Type = DisplayString
_DevicePowerDissipation_Object = MibTableColumn
devicePowerDissipation = _DevicePowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 5),
    _DevicePowerDissipation_Type()
)
devicePowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePowerDissipation.setStatus("current")
_InputMaxVoltage_Type = Integer32
_InputMaxVoltage_Object = MibTableColumn
inputMaxVoltage = _InputMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 6),
    _InputMaxVoltage_Type()
)
inputMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputMaxVoltage.setStatus("current")
_InputMaxCurrent_Type = Integer32
_InputMaxCurrent_Object = MibTableColumn
inputMaxCurrent = _InputMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 7),
    _InputMaxCurrent_Type()
)
inputMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputMaxCurrent.setStatus("current")
_PowerCapacity_Type = Integer32
_PowerCapacity_Object = MibTableColumn
powerCapacity = _PowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 8),
    _PowerCapacity_Type()
)
powerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCapacity.setStatus("current")
_DevicePowerFactor_Type = DisplayString
_DevicePowerFactor_Object = MibTableColumn
devicePowerFactor = _DevicePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 3, 1, 9),
    _DevicePowerFactor_Type()
)
devicePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePowerFactor.setStatus("current")
_SensorValueTable_Object = MibTable
sensorValueTable = _SensorValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sensorValueTable.setStatus("current")
_SensorValueEntry_Object = MibTableRow
sensorValueEntry = _SensorValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4, 1)
)
sensorValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "sensorValueIndex"),
)
if mibBuilder.loadTexts:
    sensorValueEntry.setStatus("current")


class _SensorValueIndex_Type(Integer32):
    """Custom type sensorValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SensorValueIndex_Type.__name__ = "Integer32"
_SensorValueIndex_Object = MibTableColumn
sensorValueIndex = _SensorValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4, 1, 1),
    _SensorValueIndex_Type()
)
sensorValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValueIndex.setStatus("current")
_SensorTemperature_Type = DisplayString
_SensorTemperature_Object = MibTableColumn
sensorTemperature = _SensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4, 1, 2),
    _SensorTemperature_Type()
)
sensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTemperature.setStatus("current")
_SensorHumidity_Type = DisplayString
_SensorHumidity_Object = MibTableColumn
sensorHumidity = _SensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4, 1, 3),
    _SensorHumidity_Type()
)
sensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorHumidity.setStatus("current")
_SensorPressure_Type = DisplayString
_SensorPressure_Object = MibTableColumn
sensorPressure = _SensorPressure_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4, 1, 4),
    _SensorPressure_Type()
)
sensorPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorPressure.setStatus("current")


class _SensorProperty_Type(Integer32):
    """Custom type sensorProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exhaust", 2),
          ("floor", 3),
          ("intake", 1))
    )


_SensorProperty_Type.__name__ = "Integer32"
_SensorProperty_Object = MibTableColumn
sensorProperty = _SensorProperty_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 4, 1, 5),
    _SensorProperty_Type()
)
sensorProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorProperty.setStatus("current")
_DeviceOutletStatusTable_Object = MibTable
deviceOutletStatusTable = _DeviceOutletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOutletStatusTable.setStatus("current")
_DeviceOutletStatusEntry_Object = MibTableRow
deviceOutletStatusEntry = _DeviceOutletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 5, 1)
)
deviceOutletStatusEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "deviceOutletStatusIndex"),
)
if mibBuilder.loadTexts:
    deviceOutletStatusEntry.setStatus("current")


class _DeviceOutletStatusIndex_Type(Integer32):
    """Custom type deviceOutletStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DeviceOutletStatusIndex_Type.__name__ = "Integer32"
_DeviceOutletStatusIndex_Object = MibTableColumn
deviceOutletStatusIndex = _DeviceOutletStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 5, 1, 1),
    _DeviceOutletStatusIndex_Type()
)
deviceOutletStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOutletStatusIndex.setStatus("current")


class _DisplayOutletStatus_Type(Integer32):
    """Custom type displayOutletStatus based on Integer32"""
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
        *(("fault", 4),
          ("noauth", 5),
          ("not-support", 6),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 7))
    )


_DisplayOutletStatus_Type.__name__ = "Integer32"
_DisplayOutletStatus_Object = MibTableColumn
displayOutletStatus = _DisplayOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 5, 1, 2),
    _DisplayOutletStatus_Type()
)
displayOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    displayOutletStatus.setStatus("current")
_DeviceConfigTable_Object = MibTable
deviceConfigTable = _DeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    deviceConfigTable.setStatus("current")
_DeviceConfigEntry_Object = MibTableRow
deviceConfigEntry = _DeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1)
)
deviceConfigEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "deviceConfigIndex"),
)
if mibBuilder.loadTexts:
    deviceConfigEntry.setStatus("current")


class _DeviceConfigIndex_Type(Integer32):
    """Custom type deviceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DeviceConfigIndex_Type.__name__ = "Integer32"
_DeviceConfigIndex_Object = MibTableColumn
deviceConfigIndex = _DeviceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 1),
    _DeviceConfigIndex_Type()
)
deviceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConfigIndex.setStatus("current")
_DeviceMinCurMT_Type = Integer32
_DeviceMinCurMT_Object = MibTableColumn
deviceMinCurMT = _DeviceMinCurMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 2),
    _DeviceMinCurMT_Type()
)
deviceMinCurMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMinCurMT.setStatus("current")
_DeviceMaxCurMT_Type = Integer32
_DeviceMaxCurMT_Object = MibTableColumn
deviceMaxCurMT = _DeviceMaxCurMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 3),
    _DeviceMaxCurMT_Type()
)
deviceMaxCurMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMaxCurMT.setStatus("current")


class _DeviceMinVolMT_Type(Integer32):
    """Custom type deviceMinVolMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 2600),
        ValueRangeConstraint(-3000, -3000),
    )


_DeviceMinVolMT_Type.__name__ = "Integer32"
_DeviceMinVolMT_Object = MibTableColumn
deviceMinVolMT = _DeviceMinVolMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 4),
    _DeviceMinVolMT_Type()
)
deviceMinVolMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMinVolMT.setStatus("current")


class _DeviceMaxVolMT_Type(Integer32):
    """Custom type deviceMaxVolMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 2600),
        ValueRangeConstraint(-3000, -3000),
    )


_DeviceMaxVolMT_Type.__name__ = "Integer32"
_DeviceMaxVolMT_Object = MibTableColumn
deviceMaxVolMT = _DeviceMaxVolMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 5),
    _DeviceMaxVolMT_Type()
)
deviceMaxVolMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMaxVolMT.setStatus("current")


class _DeviceMinPMT_Type(Integer32):
    """Custom type deviceMinPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
        ValueRangeConstraint(-3000, -3000),
    )


_DeviceMinPMT_Type.__name__ = "Integer32"
_DeviceMinPMT_Object = MibTableColumn
deviceMinPMT = _DeviceMinPMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 6),
    _DeviceMinPMT_Type()
)
deviceMinPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMinPMT.setStatus("current")


class _DeviceMaxPMT_Type(Integer32):
    """Custom type deviceMaxPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
        ValueRangeConstraint(-3000, -3000),
    )


_DeviceMaxPMT_Type.__name__ = "Integer32"
_DeviceMaxPMT_Object = MibTableColumn
deviceMaxPMT = _DeviceMaxPMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 7),
    _DeviceMaxPMT_Type()
)
deviceMaxPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMaxPMT.setStatus("current")


class _DeviceMaxPDMT_Type(Integer32):
    """Custom type deviceMaxPDMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
        ValueRangeConstraint(-3000, -3000),
    )


_DeviceMaxPDMT_Type.__name__ = "Integer32"
_DeviceMaxPDMT_Object = MibTableColumn
deviceMaxPDMT = _DeviceMaxPDMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 6, 1, 8),
    _DeviceMaxPDMT_Type()
)
deviceMaxPDMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMaxPDMT.setStatus("current")
_DeviceSensorTresholdTable_Object = MibTable
deviceSensorTresholdTable = _DeviceSensorTresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    deviceSensorTresholdTable.setStatus("current")
_DeviceSensorTresholdEntry_Object = MibTableRow
deviceSensorTresholdEntry = _DeviceSensorTresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1)
)
deviceSensorTresholdEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "deviceSensorTresholdIndex"),
)
if mibBuilder.loadTexts:
    deviceSensorTresholdEntry.setStatus("current")


class _DeviceSensorTresholdIndex_Type(Integer32):
    """Custom type deviceSensorTresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_DeviceSensorTresholdIndex_Type.__name__ = "Integer32"
_DeviceSensorTresholdIndex_Object = MibTableColumn
deviceSensorTresholdIndex = _DeviceSensorTresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 1),
    _DeviceSensorTresholdIndex_Type()
)
deviceSensorTresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorTresholdIndex.setStatus("current")


class _SensorMinTempMT_Type(Integer32):
    """Custom type sensorMinTempMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 600),
        ValueRangeConstraint(-3000, -3000),
    )


_SensorMinTempMT_Type.__name__ = "Integer32"
_SensorMinTempMT_Object = MibTableColumn
sensorMinTempMT = _SensorMinTempMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 2),
    _SensorMinTempMT_Type()
)
sensorMinTempMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorMinTempMT.setStatus("current")


class _SensorMaxTempMT_Type(Integer32):
    """Custom type sensorMaxTempMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 600),
        ValueRangeConstraint(-3000, -3000),
    )


_SensorMaxTempMT_Type.__name__ = "Integer32"
_SensorMaxTempMT_Object = MibTableColumn
sensorMaxTempMT = _SensorMaxTempMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 3),
    _SensorMaxTempMT_Type()
)
sensorMaxTempMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorMaxTempMT.setStatus("current")


class _SensorMinHumMT_Type(Integer32):
    """Custom type sensorMinHumMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 950),
        ValueRangeConstraint(-3000, -3000),
    )


_SensorMinHumMT_Type.__name__ = "Integer32"
_SensorMinHumMT_Object = MibTableColumn
sensorMinHumMT = _SensorMinHumMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 4),
    _SensorMinHumMT_Type()
)
sensorMinHumMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorMinHumMT.setStatus("current")


class _SensorMaxHumMT_Type(Integer32):
    """Custom type sensorMaxHumMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 950),
        ValueRangeConstraint(-3000, -3000),
    )


_SensorMaxHumMT_Type.__name__ = "Integer32"
_SensorMaxHumMT_Object = MibTableColumn
sensorMaxHumMT = _SensorMaxHumMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 5),
    _SensorMaxHumMT_Type()
)
sensorMaxHumMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorMaxHumMT.setStatus("current")


class _SensorMinPressMT_Type(Integer32):
    """Custom type sensorMinPressMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2500, 2500),
        ValueRangeConstraint(-3000, -3000),
    )


_SensorMinPressMT_Type.__name__ = "Integer32"
_SensorMinPressMT_Object = MibTableColumn
sensorMinPressMT = _SensorMinPressMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 6),
    _SensorMinPressMT_Type()
)
sensorMinPressMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorMinPressMT.setStatus("current")


class _SensorMaxPressMT_Type(Integer32):
    """Custom type sensorMaxPressMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2500, 2500),
        ValueRangeConstraint(-3000, -3000),
    )


_SensorMaxPressMT_Type.__name__ = "Integer32"
_SensorMaxPressMT_Object = MibTableColumn
sensorMaxPressMT = _SensorMaxPressMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 7, 1, 7),
    _SensorMaxPressMT_Type()
)
sensorMaxPressMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorMaxPressMT.setStatus("current")


class _DeviceOutletControl_Type(Integer32):
    """Custom type deviceOutletControl based on Integer32"""
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
        *(("nostatus", 3),
          ("not-support", 4),
          ("off", 1),
          ("on", 2))
    )


_DeviceOutletControl_Type.__name__ = "Integer32"
_DeviceOutletControl_Object = MibScalar
deviceOutletControl = _DeviceOutletControl_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 8),
    _DeviceOutletControl_Type()
)
deviceOutletControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceOutletControl.setStatus("current")


class _DeviceOutletReboot_Type(Integer32):
    """Custom type deviceOutletReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-support", 4),
          ("yes", 2))
    )


_DeviceOutletReboot_Type.__name__ = "Integer32"
_DeviceOutletReboot_Object = MibScalar
deviceOutletReboot = _DeviceOutletReboot_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 9),
    _DeviceOutletReboot_Type()
)
deviceOutletReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceOutletReboot.setStatus("current")


class _Switchable_Type(Integer32):
    """Custom type switchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mix", 3),
          ("no", 1),
          ("yes", 2))
    )


_Switchable_Type.__name__ = "Integer32"
_Switchable_Object = MibScalar
switchable = _Switchable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 10),
    _Switchable_Type()
)
switchable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchable.setStatus("current")


class _Perportreading_Type(Integer32):
    """Custom type perportreading based on Integer32"""
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


_Perportreading_Type.__name__ = "Integer32"
_Perportreading_Object = MibScalar
perportreading = _Perportreading_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 11),
    _Perportreading_Type()
)
perportreading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perportreading.setStatus("current")
_Sensornumber_Type = Integer32
_Sensornumber_Object = MibScalar
sensornumber = _Sensornumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 12),
    _Sensornumber_Type()
)
sensornumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensornumber.setStatus("current")
_Outletnumber_Type = Integer32
_Outletnumber_Object = MibScalar
outletnumber = _Outletnumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 13),
    _Outletnumber_Type()
)
outletnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletnumber.setStatus("current")
_Banknumber_Type = Integer32
_Banknumber_Object = MibScalar
banknumber = _Banknumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 14),
    _Banknumber_Type()
)
banknumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banknumber.setStatus("current")
_DoorSensor_ObjectIdentity = ObjectIdentity
doorSensor = _DoorSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 16)
)


class _DoorSensorStatus_Type(Integer32):
    """Custom type doorSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("not-attached", 2),
          ("not-support", 4),
          ("open", 1))
    )


_DoorSensorStatus_Type.__name__ = "Integer32"
_DoorSensorStatus_Object = MibScalar
doorSensorStatus = _DoorSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 16, 1),
    _DoorSensorStatus_Type()
)
doorSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorStatus.setStatus("current")


class _DoorSensorType_Type(Integer32):
    """Custom type doorSensorType based on Integer32"""
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
        *(("inductiveproximity", 2),
          ("notinstalled", 0),
          ("photo", 1),
          ("reed", 3))
    )


_DoorSensorType_Type.__name__ = "Integer32"
_DoorSensorType_Object = MibScalar
doorSensorType = _DoorSensorType_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 16, 2),
    _DoorSensorType_Type()
)
doorSensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doorSensorType.setStatus("current")
_Pop_ObjectIdentity = ObjectIdentity
pop = _Pop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 17)
)


class _EnablePOPmode_Type(Integer32):
    """Custom type enablePOPmode based on Integer32"""
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


_EnablePOPmode_Type.__name__ = "Integer32"
_EnablePOPmode_Object = MibScalar
enablePOPmode = _EnablePOPmode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 17, 1),
    _EnablePOPmode_Type()
)
enablePOPmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePOPmode.setStatus("current")
_PopThreshold_Type = Integer32
_PopThreshold_Object = MibScalar
popThreshold = _PopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 17, 2),
    _PopThreshold_Type()
)
popThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    popThreshold.setStatus("current")


class _EnableOutletPOPmode_Type(Integer32):
    """Custom type enableOutletPOPmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-support", 3),
          ("yes", 2))
    )


_EnableOutletPOPmode_Type.__name__ = "Integer32"
_EnableOutletPOPmode_Object = MibScalar
enableOutletPOPmode = _EnableOutletPOPmode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 17, 3),
    _EnableOutletPOPmode_Type()
)
enableOutletPOPmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableOutletPOPmode.setStatus("current")


class _EnableLIFOPOPmode_Type(Integer32):
    """Custom type enableLIFOPOPmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-support", 3),
          ("yes", 2))
    )


_EnableLIFOPOPmode_Type.__name__ = "Integer32"
_EnableLIFOPOPmode_Object = MibScalar
enableLIFOPOPmode = _EnableLIFOPOPmode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 17, 4),
    _EnableLIFOPOPmode_Type()
)
enableLIFOPOPmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLIFOPOPmode.setStatus("current")


class _EnablePriorityPOPmode_Type(Integer32):
    """Custom type enablePriorityPOPmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-support", 3),
          ("yes", 2))
    )


_EnablePriorityPOPmode_Type.__name__ = "Integer32"
_EnablePriorityPOPmode_Object = MibScalar
enablePriorityPOPmode = _EnablePriorityPOPmode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 17, 5),
    _EnablePriorityPOPmode_Type()
)
enablePriorityPOPmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePriorityPOPmode.setStatus("current")
_Cap_ObjectIdentity = ObjectIdentity
cap = _Cap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 18)
)


class _EnableCAPmode_Type(Integer32):
    """Custom type enableCAPmode based on Integer32"""
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


_EnableCAPmode_Type.__name__ = "Integer32"
_EnableCAPmode_Object = MibScalar
enableCAPmode = _EnableCAPmode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 18, 1),
    _EnableCAPmode_Type()
)
enableCAPmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableCAPmode.setStatus("current")
_OutletCAPTable_Object = MibTable
outletCAPTable = _OutletCAPTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 18, 2)
)
if mibBuilder.loadTexts:
    outletCAPTable.setStatus("current")
_OutletCAPEntry_Object = MibTableRow
outletCAPEntry = _OutletCAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 18, 2, 1)
)
outletCAPEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "outletCAPIndex"),
)
if mibBuilder.loadTexts:
    outletCAPEntry.setStatus("current")


class _OutletCAPIndex_Type(Integer32):
    """Custom type outletCAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_OutletCAPIndex_Type.__name__ = "Integer32"
_OutletCAPIndex_Object = MibTableColumn
outletCAPIndex = _OutletCAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 18, 2, 1, 1),
    _OutletCAPIndex_Type()
)
outletCAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCAPIndex.setStatus("current")


class _OutletCAPPriority_Type(Integer32):
    """Custom type outletCAPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OutletCAPPriority_Type.__name__ = "Integer32"
_OutletCAPPriority_Object = MibTableColumn
outletCAPPriority = _OutletCAPPriority_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 18, 2, 1, 2),
    _OutletCAPPriority_Type()
)
outletCAPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCAPPriority.setStatus("current")


class _OutletInitMode_Type(Integer32):
    """Custom type outletInitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delaytime", 2),
          ("no-delaytime", 1),
          ("not-support", 3))
    )


_OutletInitMode_Type.__name__ = "Integer32"
_OutletInitMode_Object = MibScalar
outletInitMode = _OutletInitMode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 19),
    _OutletInitMode_Type()
)
outletInitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletInitMode.setStatus("current")
_DeviceIntegerValueTable_Object = MibTable
deviceIntegerValueTable = _DeviceIntegerValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99)
)
if mibBuilder.loadTexts:
    deviceIntegerValueTable.setStatus("current")
_DeviceIntegerValueEntry_Object = MibTableRow
deviceIntegerValueEntry = _DeviceIntegerValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99, 1)
)
deviceIntegerValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "deviceIntegerValueIndex"),
)
if mibBuilder.loadTexts:
    deviceIntegerValueEntry.setStatus("current")


class _DeviceIntegerValueIndex_Type(Integer32):
    """Custom type deviceIntegerValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DeviceIntegerValueIndex_Type.__name__ = "Integer32"
_DeviceIntegerValueIndex_Object = MibTableColumn
deviceIntegerValueIndex = _DeviceIntegerValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99, 1, 1),
    _DeviceIntegerValueIndex_Type()
)
deviceIntegerValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIntegerValueIndex.setStatus("current")
_DeviceIntegerCurrent_Type = Integer32
_DeviceIntegerCurrent_Object = MibTableColumn
deviceIntegerCurrent = _DeviceIntegerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99, 1, 2),
    _DeviceIntegerCurrent_Type()
)
deviceIntegerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIntegerCurrent.setStatus("current")
_DeviceIntegerVoltage_Type = Integer32
_DeviceIntegerVoltage_Object = MibTableColumn
deviceIntegerVoltage = _DeviceIntegerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99, 1, 3),
    _DeviceIntegerVoltage_Type()
)
deviceIntegerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIntegerVoltage.setStatus("current")
_DeviceIntegerPower_Type = Integer32
_DeviceIntegerPower_Object = MibTableColumn
deviceIntegerPower = _DeviceIntegerPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99, 1, 4),
    _DeviceIntegerPower_Type()
)
deviceIntegerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIntegerPower.setStatus("current")
_DeviceIntegerPowerDissipation_Type = Integer32
_DeviceIntegerPowerDissipation_Object = MibTableColumn
deviceIntegerPowerDissipation = _DeviceIntegerPowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 99, 1, 5),
    _DeviceIntegerPowerDissipation_Type()
)
deviceIntegerPowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIntegerPowerDissipation.setStatus("current")
_SensorIntegerValueTable_Object = MibTable
sensorIntegerValueTable = _SensorIntegerValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 100)
)
if mibBuilder.loadTexts:
    sensorIntegerValueTable.setStatus("current")
_SensorIntegerValueEntry_Object = MibTableRow
sensorIntegerValueEntry = _SensorIntegerValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 100, 1)
)
sensorIntegerValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "sensorIntegerValueIndex"),
)
if mibBuilder.loadTexts:
    sensorIntegerValueEntry.setStatus("current")


class _SensorIntegerValueIndex_Type(Integer32):
    """Custom type sensorIntegerValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SensorIntegerValueIndex_Type.__name__ = "Integer32"
_SensorIntegerValueIndex_Object = MibTableColumn
sensorIntegerValueIndex = _SensorIntegerValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 100, 1, 1),
    _SensorIntegerValueIndex_Type()
)
sensorIntegerValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIntegerValueIndex.setStatus("current")
_SensorIntegerTemperature_Type = Integer32
_SensorIntegerTemperature_Object = MibTableColumn
sensorIntegerTemperature = _SensorIntegerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 100, 1, 2),
    _SensorIntegerTemperature_Type()
)
sensorIntegerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIntegerTemperature.setStatus("current")
_SensorIntegerHumidity_Type = Integer32
_SensorIntegerHumidity_Object = MibTableColumn
sensorIntegerHumidity = _SensorIntegerHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 100, 1, 3),
    _SensorIntegerHumidity_Type()
)
sensorIntegerHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIntegerHumidity.setStatus("current")
_SensorIntegerPressure_Type = Integer32
_SensorIntegerPressure_Object = MibTableColumn
sensorIntegerPressure = _SensorIntegerPressure_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 1, 100, 1, 4),
    _SensorIntegerPressure_Type()
)
sensorIntegerPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIntegerPressure.setStatus("current")
_Outlet_ObjectIdentity = ObjectIdentity
outlet = _Outlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2)
)
_OutletValueTable_Object = MibTable
outletValueTable = _OutletValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    outletValueTable.setStatus("current")
_OutletValueEntry_Object = MibTableRow
outletValueEntry = _OutletValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1)
)
outletValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "outletValueIndex"),
)
if mibBuilder.loadTexts:
    outletValueEntry.setStatus("current")


class _OutletValueIndex_Type(Integer32):
    """Custom type outletValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_OutletValueIndex_Type.__name__ = "Integer32"
_OutletValueIndex_Object = MibTableColumn
outletValueIndex = _OutletValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 1),
    _OutletValueIndex_Type()
)
outletValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletValueIndex.setStatus("current")
_OutletCurrent_Type = DisplayString
_OutletCurrent_Object = MibTableColumn
outletCurrent = _OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 2),
    _OutletCurrent_Type()
)
outletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrent.setStatus("current")
_OutletVoltage_Type = DisplayString
_OutletVoltage_Object = MibTableColumn
outletVoltage = _OutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 3),
    _OutletVoltage_Type()
)
outletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVoltage.setStatus("current")
_OutletPower_Type = DisplayString
_OutletPower_Object = MibTableColumn
outletPower = _OutletPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 4),
    _OutletPower_Type()
)
outletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPower.setStatus("current")
_OutletPowerDissipation_Type = DisplayString
_OutletPowerDissipation_Object = MibTableColumn
outletPowerDissipation = _OutletPowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 5),
    _OutletPowerDissipation_Type()
)
outletPowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerDissipation.setStatus("current")
_OutletMaxCurrent_Type = Integer32
_OutletMaxCurrent_Object = MibTableColumn
outletMaxCurrent = _OutletMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 6),
    _OutletMaxCurrent_Type()
)
outletMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletMaxCurrent.setStatus("current")
_OutletPowerFactor_Type = DisplayString
_OutletPowerFactor_Object = MibTableColumn
outletPowerFactor = _OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 1, 1, 7),
    _OutletPowerFactor_Type()
)
outletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerFactor.setStatus("current")


class _Outlet1Status_Type(Integer32):
    """Custom type outlet1Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet1Status_Type.__name__ = "Integer32"
_Outlet1Status_Object = MibScalar
outlet1Status = _Outlet1Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 2),
    _Outlet1Status_Type()
)
outlet1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Status.setStatus("current")


class _Outlet2Status_Type(Integer32):
    """Custom type outlet2Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet2Status_Type.__name__ = "Integer32"
_Outlet2Status_Object = MibScalar
outlet2Status = _Outlet2Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 3),
    _Outlet2Status_Type()
)
outlet2Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Status.setStatus("current")


class _Outlet3Status_Type(Integer32):
    """Custom type outlet3Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet3Status_Type.__name__ = "Integer32"
_Outlet3Status_Object = MibScalar
outlet3Status = _Outlet3Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 4),
    _Outlet3Status_Type()
)
outlet3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Status.setStatus("current")


class _Outlet4Status_Type(Integer32):
    """Custom type outlet4Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet4Status_Type.__name__ = "Integer32"
_Outlet4Status_Object = MibScalar
outlet4Status = _Outlet4Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 5),
    _Outlet4Status_Type()
)
outlet4Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Status.setStatus("current")


class _Outlet5Status_Type(Integer32):
    """Custom type outlet5Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet5Status_Type.__name__ = "Integer32"
_Outlet5Status_Object = MibScalar
outlet5Status = _Outlet5Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 6),
    _Outlet5Status_Type()
)
outlet5Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Status.setStatus("current")


class _Outlet6Status_Type(Integer32):
    """Custom type outlet6Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet6Status_Type.__name__ = "Integer32"
_Outlet6Status_Object = MibScalar
outlet6Status = _Outlet6Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 7),
    _Outlet6Status_Type()
)
outlet6Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Status.setStatus("current")


class _Outlet7Status_Type(Integer32):
    """Custom type outlet7Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet7Status_Type.__name__ = "Integer32"
_Outlet7Status_Object = MibScalar
outlet7Status = _Outlet7Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 8),
    _Outlet7Status_Type()
)
outlet7Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Status.setStatus("current")


class _Outlet8Status_Type(Integer32):
    """Custom type outlet8Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet8Status_Type.__name__ = "Integer32"
_Outlet8Status_Object = MibScalar
outlet8Status = _Outlet8Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 9),
    _Outlet8Status_Type()
)
outlet8Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Status.setStatus("current")
_OutletConfigTable_Object = MibTable
outletConfigTable = _OutletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    outletConfigTable.setStatus("current")
_OutletConfigEntry_Object = MibTableRow
outletConfigEntry = _OutletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1)
)
outletConfigEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "outletConfigIndex"),
)
if mibBuilder.loadTexts:
    outletConfigEntry.setStatus("current")


class _OutletConfigIndex_Type(Integer32):
    """Custom type outletConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_OutletConfigIndex_Type.__name__ = "Integer32"
_OutletConfigIndex_Object = MibTableColumn
outletConfigIndex = _OutletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 1),
    _OutletConfigIndex_Type()
)
outletConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletConfigIndex.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 2),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")


class _OutletConfirmation_Type(Integer32):
    """Custom type outletConfirmation based on Integer32"""
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
        *(("no", 1),
          ("noauth", 3),
          ("not-support", 4),
          ("yes", 2))
    )


_OutletConfirmation_Type.__name__ = "Integer32"
_OutletConfirmation_Object = MibTableColumn
outletConfirmation = _OutletConfirmation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 3),
    _OutletConfirmation_Type()
)
outletConfirmation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfirmation.setStatus("current")


class _OutletOnDelayTime_Type(Integer32):
    """Custom type outletOnDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
        ValueRangeConstraint(-1, -1),
    )


_OutletOnDelayTime_Type.__name__ = "Integer32"
_OutletOnDelayTime_Object = MibTableColumn
outletOnDelayTime = _OutletOnDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 4),
    _OutletOnDelayTime_Type()
)
outletOnDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletOnDelayTime.setStatus("current")


class _OutletOffDelayTime_Type(Integer32):
    """Custom type outletOffDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
        ValueRangeConstraint(-1, -1),
    )


_OutletOffDelayTime_Type.__name__ = "Integer32"
_OutletOffDelayTime_Object = MibTableColumn
outletOffDelayTime = _OutletOffDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 5),
    _OutletOffDelayTime_Type()
)
outletOffDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletOffDelayTime.setStatus("current")


class _OutletShutdownMethod_Type(Integer32):
    """Custom type outletShutdownMethod based on Integer32"""
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
        *(("after-ac-back", 3),
          ("kill-the-power", 1),
          ("not-support", 4),
          ("wake-on-lan", 2))
    )


_OutletShutdownMethod_Type.__name__ = "Integer32"
_OutletShutdownMethod_Object = MibTableColumn
outletShutdownMethod = _OutletShutdownMethod_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 6),
    _OutletShutdownMethod_Type()
)
outletShutdownMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletShutdownMethod.setStatus("current")
_OutletMAC_Type = DisplayString
_OutletMAC_Object = MibTableColumn
outletMAC = _OutletMAC_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 7),
    _OutletMAC_Type()
)
outletMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMAC.setStatus("current")
_OutletMinCurMT_Type = Integer32
_OutletMinCurMT_Object = MibTableColumn
outletMinCurMT = _OutletMinCurMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 8),
    _OutletMinCurMT_Type()
)
outletMinCurMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMinCurMT.setStatus("current")
_OutletMaxCurMT_Type = Integer32
_OutletMaxCurMT_Object = MibTableColumn
outletMaxCurMT = _OutletMaxCurMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 9),
    _OutletMaxCurMT_Type()
)
outletMaxCurMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMaxCurMT.setStatus("current")


class _OutletMinVolMT_Type(Integer32):
    """Custom type outletMinVolMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 2600),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_OutletMinVolMT_Type.__name__ = "Integer32"
_OutletMinVolMT_Object = MibTableColumn
outletMinVolMT = _OutletMinVolMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 10),
    _OutletMinVolMT_Type()
)
outletMinVolMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMinVolMT.setStatus("current")


class _OutletMaxVolMT_Type(Integer32):
    """Custom type outletMaxVolMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 2600),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_OutletMaxVolMT_Type.__name__ = "Integer32"
_OutletMaxVolMT_Object = MibTableColumn
outletMaxVolMT = _OutletMaxVolMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 11),
    _OutletMaxVolMT_Type()
)
outletMaxVolMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMaxVolMT.setStatus("current")


class _OutletMinPMT_Type(Integer32):
    """Custom type outletMinPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_OutletMinPMT_Type.__name__ = "Integer32"
_OutletMinPMT_Object = MibTableColumn
outletMinPMT = _OutletMinPMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 12),
    _OutletMinPMT_Type()
)
outletMinPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMinPMT.setStatus("current")


class _OutletMaxPMT_Type(Integer32):
    """Custom type outletMaxPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_OutletMaxPMT_Type.__name__ = "Integer32"
_OutletMaxPMT_Object = MibTableColumn
outletMaxPMT = _OutletMaxPMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 13),
    _OutletMaxPMT_Type()
)
outletMaxPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMaxPMT.setStatus("current")


class _OutletMaxPDMT_Type(Integer32):
    """Custom type outletMaxPDMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_OutletMaxPDMT_Type.__name__ = "Integer32"
_OutletMaxPDMT_Object = MibTableColumn
outletMaxPDMT = _OutletMaxPDMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 10, 1, 14),
    _OutletMaxPDMT_Type()
)
outletMaxPDMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletMaxPDMT.setStatus("current")


class _Outlet9Status_Type(Integer32):
    """Custom type outlet9Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet9Status_Type.__name__ = "Integer32"
_Outlet9Status_Object = MibScalar
outlet9Status = _Outlet9Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 11),
    _Outlet9Status_Type()
)
outlet9Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9Status.setStatus("current")


class _Outlet10Status_Type(Integer32):
    """Custom type outlet10Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet10Status_Type.__name__ = "Integer32"
_Outlet10Status_Object = MibScalar
outlet10Status = _Outlet10Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 12),
    _Outlet10Status_Type()
)
outlet10Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10Status.setStatus("current")


class _Outlet11Status_Type(Integer32):
    """Custom type outlet11Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet11Status_Type.__name__ = "Integer32"
_Outlet11Status_Object = MibScalar
outlet11Status = _Outlet11Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 13),
    _Outlet11Status_Type()
)
outlet11Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11Status.setStatus("current")


class _Outlet12Status_Type(Integer32):
    """Custom type outlet12Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet12Status_Type.__name__ = "Integer32"
_Outlet12Status_Object = MibScalar
outlet12Status = _Outlet12Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 14),
    _Outlet12Status_Type()
)
outlet12Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12Status.setStatus("current")


class _Outlet13Status_Type(Integer32):
    """Custom type outlet13Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet13Status_Type.__name__ = "Integer32"
_Outlet13Status_Object = MibScalar
outlet13Status = _Outlet13Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 15),
    _Outlet13Status_Type()
)
outlet13Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13Status.setStatus("current")


class _Outlet14Status_Type(Integer32):
    """Custom type outlet14Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet14Status_Type.__name__ = "Integer32"
_Outlet14Status_Object = MibScalar
outlet14Status = _Outlet14Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 16),
    _Outlet14Status_Type()
)
outlet14Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14Status.setStatus("current")


class _Outlet15Status_Type(Integer32):
    """Custom type outlet15Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet15Status_Type.__name__ = "Integer32"
_Outlet15Status_Object = MibScalar
outlet15Status = _Outlet15Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 17),
    _Outlet15Status_Type()
)
outlet15Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15Status.setStatus("current")


class _Outlet16Status_Type(Integer32):
    """Custom type outlet16Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet16Status_Type.__name__ = "Integer32"
_Outlet16Status_Object = MibScalar
outlet16Status = _Outlet16Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 18),
    _Outlet16Status_Type()
)
outlet16Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16Status.setStatus("current")


class _Outlet17Status_Type(Integer32):
    """Custom type outlet17Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet17Status_Type.__name__ = "Integer32"
_Outlet17Status_Object = MibScalar
outlet17Status = _Outlet17Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 19),
    _Outlet17Status_Type()
)
outlet17Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17Status.setStatus("current")


class _Outlet18Status_Type(Integer32):
    """Custom type outlet18Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet18Status_Type.__name__ = "Integer32"
_Outlet18Status_Object = MibScalar
outlet18Status = _Outlet18Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 20),
    _Outlet18Status_Type()
)
outlet18Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18Status.setStatus("current")


class _Outlet19Status_Type(Integer32):
    """Custom type outlet19Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet19Status_Type.__name__ = "Integer32"
_Outlet19Status_Object = MibScalar
outlet19Status = _Outlet19Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 21),
    _Outlet19Status_Type()
)
outlet19Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19Status.setStatus("current")


class _Outlet20Status_Type(Integer32):
    """Custom type outlet20Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet20Status_Type.__name__ = "Integer32"
_Outlet20Status_Object = MibScalar
outlet20Status = _Outlet20Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 22),
    _Outlet20Status_Type()
)
outlet20Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20Status.setStatus("current")


class _Outlet21Status_Type(Integer32):
    """Custom type outlet21Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet21Status_Type.__name__ = "Integer32"
_Outlet21Status_Object = MibScalar
outlet21Status = _Outlet21Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 23),
    _Outlet21Status_Type()
)
outlet21Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21Status.setStatus("current")


class _Outlet22Status_Type(Integer32):
    """Custom type outlet22Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet22Status_Type.__name__ = "Integer32"
_Outlet22Status_Object = MibScalar
outlet22Status = _Outlet22Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 24),
    _Outlet22Status_Type()
)
outlet22Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22Status.setStatus("current")


class _Outlet23Status_Type(Integer32):
    """Custom type outlet23Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet23Status_Type.__name__ = "Integer32"
_Outlet23Status_Object = MibScalar
outlet23Status = _Outlet23Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 25),
    _Outlet23Status_Type()
)
outlet23Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23Status.setStatus("current")


class _Outlet24Status_Type(Integer32):
    """Custom type outlet24Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet24Status_Type.__name__ = "Integer32"
_Outlet24Status_Object = MibScalar
outlet24Status = _Outlet24Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 26),
    _Outlet24Status_Type()
)
outlet24Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24Status.setStatus("current")


class _Outlet25Status_Type(Integer32):
    """Custom type outlet25Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet25Status_Type.__name__ = "Integer32"
_Outlet25Status_Object = MibScalar
outlet25Status = _Outlet25Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 27),
    _Outlet25Status_Type()
)
outlet25Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25Status.setStatus("current")


class _Outlet26Status_Type(Integer32):
    """Custom type outlet26Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet26Status_Type.__name__ = "Integer32"
_Outlet26Status_Object = MibScalar
outlet26Status = _Outlet26Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 28),
    _Outlet26Status_Type()
)
outlet26Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26Status.setStatus("current")


class _Outlet27Status_Type(Integer32):
    """Custom type outlet27Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet27Status_Type.__name__ = "Integer32"
_Outlet27Status_Object = MibScalar
outlet27Status = _Outlet27Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 29),
    _Outlet27Status_Type()
)
outlet27Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27Status.setStatus("current")


class _Outlet28Status_Type(Integer32):
    """Custom type outlet28Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet28Status_Type.__name__ = "Integer32"
_Outlet28Status_Object = MibScalar
outlet28Status = _Outlet28Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 30),
    _Outlet28Status_Type()
)
outlet28Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28Status.setStatus("current")


class _Outlet29Status_Type(Integer32):
    """Custom type outlet29Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet29Status_Type.__name__ = "Integer32"
_Outlet29Status_Object = MibScalar
outlet29Status = _Outlet29Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 31),
    _Outlet29Status_Type()
)
outlet29Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29Status.setStatus("current")


class _Outlet30Status_Type(Integer32):
    """Custom type outlet30Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet30Status_Type.__name__ = "Integer32"
_Outlet30Status_Object = MibScalar
outlet30Status = _Outlet30Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 32),
    _Outlet30Status_Type()
)
outlet30Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30Status.setStatus("current")


class _Outlet31Status_Type(Integer32):
    """Custom type outlet31Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet31Status_Type.__name__ = "Integer32"
_Outlet31Status_Object = MibScalar
outlet31Status = _Outlet31Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 33),
    _Outlet31Status_Type()
)
outlet31Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31Status.setStatus("current")


class _Outlet32Status_Type(Integer32):
    """Custom type outlet32Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet32Status_Type.__name__ = "Integer32"
_Outlet32Status_Object = MibScalar
outlet32Status = _Outlet32Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 34),
    _Outlet32Status_Type()
)
outlet32Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32Status.setStatus("current")


class _Outlet33Status_Type(Integer32):
    """Custom type outlet33Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet33Status_Type.__name__ = "Integer32"
_Outlet33Status_Object = MibScalar
outlet33Status = _Outlet33Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 35),
    _Outlet33Status_Type()
)
outlet33Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33Status.setStatus("current")


class _Outlet34Status_Type(Integer32):
    """Custom type outlet34Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet34Status_Type.__name__ = "Integer32"
_Outlet34Status_Object = MibScalar
outlet34Status = _Outlet34Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 36),
    _Outlet34Status_Type()
)
outlet34Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34Status.setStatus("current")


class _Outlet35Status_Type(Integer32):
    """Custom type outlet35Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet35Status_Type.__name__ = "Integer32"
_Outlet35Status_Object = MibScalar
outlet35Status = _Outlet35Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 37),
    _Outlet35Status_Type()
)
outlet35Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35Status.setStatus("current")


class _Outlet36Status_Type(Integer32):
    """Custom type outlet36Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet36Status_Type.__name__ = "Integer32"
_Outlet36Status_Object = MibScalar
outlet36Status = _Outlet36Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 38),
    _Outlet36Status_Type()
)
outlet36Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36Status.setStatus("current")


class _Outlet37Status_Type(Integer32):
    """Custom type outlet37Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet37Status_Type.__name__ = "Integer32"
_Outlet37Status_Object = MibScalar
outlet37Status = _Outlet37Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 39),
    _Outlet37Status_Type()
)
outlet37Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet37Status.setStatus("current")


class _Outlet38Status_Type(Integer32):
    """Custom type outlet38Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet38Status_Type.__name__ = "Integer32"
_Outlet38Status_Object = MibScalar
outlet38Status = _Outlet38Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 40),
    _Outlet38Status_Type()
)
outlet38Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet38Status.setStatus("current")


class _Outlet39Status_Type(Integer32):
    """Custom type outlet39Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet39Status_Type.__name__ = "Integer32"
_Outlet39Status_Object = MibScalar
outlet39Status = _Outlet39Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 41),
    _Outlet39Status_Type()
)
outlet39Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet39Status.setStatus("current")


class _Outlet40Status_Type(Integer32):
    """Custom type outlet40Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet40Status_Type.__name__ = "Integer32"
_Outlet40Status_Object = MibScalar
outlet40Status = _Outlet40Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 42),
    _Outlet40Status_Type()
)
outlet40Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet40Status.setStatus("current")


class _Outlet41Status_Type(Integer32):
    """Custom type outlet41Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet41Status_Type.__name__ = "Integer32"
_Outlet41Status_Object = MibScalar
outlet41Status = _Outlet41Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 43),
    _Outlet41Status_Type()
)
outlet41Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet41Status.setStatus("current")


class _Outlet42Status_Type(Integer32):
    """Custom type outlet42Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("noauth", 6),
          ("not-support", 7),
          ("off", 1),
          ("on", 2),
          ("pending", 3),
          ("pop", 8),
          ("reboot", 4))
    )


_Outlet42Status_Type.__name__ = "Integer32"
_Outlet42Status_Object = MibScalar
outlet42Status = _Outlet42Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 44),
    _Outlet42Status_Type()
)
outlet42Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet42Status.setStatus("current")
_OutletSwitchableTable_Object = MibTable
outletSwitchableTable = _OutletSwitchableTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 70)
)
if mibBuilder.loadTexts:
    outletSwitchableTable.setStatus("current")
_OutletSwitchableEntry_Object = MibTableRow
outletSwitchableEntry = _OutletSwitchableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 70, 1)
)
outletSwitchableEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "outletSwitchableIndex"),
)
if mibBuilder.loadTexts:
    outletSwitchableEntry.setStatus("current")


class _OutletSwitchableIndex_Type(Integer32):
    """Custom type outletSwitchableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_OutletSwitchableIndex_Type.__name__ = "Integer32"
_OutletSwitchableIndex_Object = MibTableColumn
outletSwitchableIndex = _OutletSwitchableIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 70, 1, 1),
    _OutletSwitchableIndex_Type()
)
outletSwitchableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSwitchableIndex.setStatus("current")


class _OutletSwitchable_Type(Integer32):
    """Custom type outletSwitchable based on Integer32"""
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


_OutletSwitchable_Type.__name__ = "Integer32"
_OutletSwitchable_Object = MibTableColumn
outletSwitchable = _OutletSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 70, 1, 2),
    _OutletSwitchable_Type()
)
outletSwitchable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSwitchable.setStatus("current")
_OutletIntegerValueTable_Object = MibTable
outletIntegerValueTable = _OutletIntegerValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99)
)
if mibBuilder.loadTexts:
    outletIntegerValueTable.setStatus("current")
_OutletIntegerValueEntry_Object = MibTableRow
outletIntegerValueEntry = _OutletIntegerValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99, 1)
)
outletIntegerValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "outletIntegerValueIndex"),
)
if mibBuilder.loadTexts:
    outletIntegerValueEntry.setStatus("current")


class _OutletIntegerValueIndex_Type(Integer32):
    """Custom type outletIntegerValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_OutletIntegerValueIndex_Type.__name__ = "Integer32"
_OutletIntegerValueIndex_Object = MibTableColumn
outletIntegerValueIndex = _OutletIntegerValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99, 1, 1),
    _OutletIntegerValueIndex_Type()
)
outletIntegerValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIntegerValueIndex.setStatus("current")
_OutletIntegerCurrent_Type = Integer32
_OutletIntegerCurrent_Object = MibTableColumn
outletIntegerCurrent = _OutletIntegerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99, 1, 2),
    _OutletIntegerCurrent_Type()
)
outletIntegerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIntegerCurrent.setStatus("current")
_OutletIntegerVoltage_Type = Integer32
_OutletIntegerVoltage_Object = MibTableColumn
outletIntegerVoltage = _OutletIntegerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99, 1, 3),
    _OutletIntegerVoltage_Type()
)
outletIntegerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIntegerVoltage.setStatus("current")
_OutletIntegerPower_Type = Integer32
_OutletIntegerPower_Object = MibTableColumn
outletIntegerPower = _OutletIntegerPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99, 1, 4),
    _OutletIntegerPower_Type()
)
outletIntegerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIntegerPower.setStatus("current")
_OutletIntegerPowerDissipation_Type = Integer32
_OutletIntegerPowerDissipation_Object = MibTableColumn
outletIntegerPowerDissipation = _OutletIntegerPowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 2, 99, 1, 5),
    _OutletIntegerPowerDissipation_Type()
)
outletIntegerPowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIntegerPowerDissipation.setStatus("current")
_Bank_ObjectIdentity = ObjectIdentity
bank = _Bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3)
)
_BreakerStatusTable_Object = MibTable
breakerStatusTable = _BreakerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    breakerStatusTable.setStatus("current")
_BreakerStatusEntry_Object = MibTableRow
breakerStatusEntry = _BreakerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 1, 1)
)
breakerStatusEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "breakerStatusIndex"),
)
if mibBuilder.loadTexts:
    breakerStatusEntry.setStatus("current")


class _BreakerStatusIndex_Type(Integer32):
    """Custom type breakerStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BreakerStatusIndex_Type.__name__ = "Integer32"
_BreakerStatusIndex_Object = MibTableColumn
breakerStatusIndex = _BreakerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 1, 1, 1),
    _BreakerStatusIndex_Type()
)
breakerStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerStatusIndex.setStatus("current")


class _BreakerStatus_Type(Integer32):
    """Custom type breakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 3),
          ("off", 1),
          ("on", 2))
    )


_BreakerStatus_Type.__name__ = "Integer32"
_BreakerStatus_Object = MibTableColumn
breakerStatus = _BreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 1, 1, 2),
    _BreakerStatus_Type()
)
breakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerStatus.setStatus("current")
_BankValueTable_Object = MibTable
bankValueTable = _BankValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    bankValueTable.setStatus("current")
_BankValueEntry_Object = MibTableRow
bankValueEntry = _BankValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1)
)
bankValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "bankValueIndex"),
)
if mibBuilder.loadTexts:
    bankValueEntry.setStatus("current")


class _BankValueIndex_Type(Integer32):
    """Custom type bankValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BankValueIndex_Type.__name__ = "Integer32"
_BankValueIndex_Object = MibTableColumn
bankValueIndex = _BankValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 1),
    _BankValueIndex_Type()
)
bankValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankValueIndex.setStatus("current")
_BankCurrent_Type = DisplayString
_BankCurrent_Object = MibTableColumn
bankCurrent = _BankCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 2),
    _BankCurrent_Type()
)
bankCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankCurrent.setStatus("current")
_BankVoltage_Type = DisplayString
_BankVoltage_Object = MibTableColumn
bankVoltage = _BankVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 3),
    _BankVoltage_Type()
)
bankVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankVoltage.setStatus("current")
_BankPower_Type = DisplayString
_BankPower_Object = MibTableColumn
bankPower = _BankPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 4),
    _BankPower_Type()
)
bankPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankPower.setStatus("current")
_BankPowerDissipation_Type = DisplayString
_BankPowerDissipation_Object = MibTableColumn
bankPowerDissipation = _BankPowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 5),
    _BankPowerDissipation_Type()
)
bankPowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankPowerDissipation.setStatus("current")
_BankMaxCurrent_Type = Integer32
_BankMaxCurrent_Object = MibTableColumn
bankMaxCurrent = _BankMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 6),
    _BankMaxCurrent_Type()
)
bankMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankMaxCurrent.setStatus("current")


class _BankAttachStatus_Type(Integer32):
    """Custom type bankAttachStatus based on Integer32"""
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
        *(("attached", 2),
          ("error", 3),
          ("noattached", 1),
          ("noexisted", 4))
    )


_BankAttachStatus_Type.__name__ = "Integer32"
_BankAttachStatus_Object = MibTableColumn
bankAttachStatus = _BankAttachStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 7),
    _BankAttachStatus_Type()
)
bankAttachStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankAttachStatus.setStatus("current")
_BankPowerFactor_Type = DisplayString
_BankPowerFactor_Object = MibTableColumn
bankPowerFactor = _BankPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 2, 1, 8),
    _BankPowerFactor_Type()
)
bankPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankPowerFactor.setStatus("current")
_BankConfigTable_Object = MibTable
bankConfigTable = _BankConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    bankConfigTable.setStatus("current")
_BankConfigEntry_Object = MibTableRow
bankConfigEntry = _BankConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1)
)
bankConfigEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "bankConfigIndex"),
)
if mibBuilder.loadTexts:
    bankConfigEntry.setStatus("current")


class _BankConfigIndex_Type(Integer32):
    """Custom type bankConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BankConfigIndex_Type.__name__ = "Integer32"
_BankConfigIndex_Object = MibTableColumn
bankConfigIndex = _BankConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 1),
    _BankConfigIndex_Type()
)
bankConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankConfigIndex.setStatus("current")
_BankName_Type = DisplayString
_BankName_Object = MibTableColumn
bankName = _BankName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 2),
    _BankName_Type()
)
bankName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankName.setStatus("current")
_BankMinCurMT_Type = Integer32
_BankMinCurMT_Object = MibTableColumn
bankMinCurMT = _BankMinCurMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 3),
    _BankMinCurMT_Type()
)
bankMinCurMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMinCurMT.setStatus("current")
_BankMaxCurMT_Type = Integer32
_BankMaxCurMT_Object = MibTableColumn
bankMaxCurMT = _BankMaxCurMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 4),
    _BankMaxCurMT_Type()
)
bankMaxCurMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMaxCurMT.setStatus("current")


class _BankMinVolMT_Type(Integer32):
    """Custom type bankMinVolMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 2600),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_BankMinVolMT_Type.__name__ = "Integer32"
_BankMinVolMT_Object = MibTableColumn
bankMinVolMT = _BankMinVolMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 5),
    _BankMinVolMT_Type()
)
bankMinVolMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMinVolMT.setStatus("current")


class _BankMaxVolMT_Type(Integer32):
    """Custom type bankMaxVolMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 2600),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_BankMaxVolMT_Type.__name__ = "Integer32"
_BankMaxVolMT_Object = MibTableColumn
bankMaxVolMT = _BankMaxVolMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 6),
    _BankMaxVolMT_Type()
)
bankMaxVolMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMaxVolMT.setStatus("current")


class _BankMinPMT_Type(Integer32):
    """Custom type bankMinPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_BankMinPMT_Type.__name__ = "Integer32"
_BankMinPMT_Object = MibTableColumn
bankMinPMT = _BankMinPMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 7),
    _BankMinPMT_Type()
)
bankMinPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMinPMT.setStatus("current")


class _BankMaxPMT_Type(Integer32):
    """Custom type bankMaxPMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_BankMaxPMT_Type.__name__ = "Integer32"
_BankMaxPMT_Object = MibTableColumn
bankMaxPMT = _BankMaxPMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 8),
    _BankMaxPMT_Type()
)
bankMaxPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMaxPMT.setStatus("current")


class _BankMaxPDMT_Type(Integer32):
    """Custom type bankMaxPDMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
        ValueRangeConstraint(-3000, -3000),
        ValueRangeConstraint(-2000000, -2000000),
    )


_BankMaxPDMT_Type.__name__ = "Integer32"
_BankMaxPDMT_Object = MibTableColumn
bankMaxPDMT = _BankMaxPDMT_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 3, 1, 9),
    _BankMaxPDMT_Type()
)
bankMaxPDMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankMaxPDMT.setStatus("current")
_BankControlTable_Object = MibTable
bankControlTable = _BankControlTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    bankControlTable.setStatus("current")
_BankControlEntry_Object = MibTableRow
bankControlEntry = _BankControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 4, 1)
)
bankControlEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "bankControlIndex"),
)
if mibBuilder.loadTexts:
    bankControlEntry.setStatus("current")


class _BankControlIndex_Type(Integer32):
    """Custom type bankControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BankControlIndex_Type.__name__ = "Integer32"
_BankControlIndex_Object = MibTableColumn
bankControlIndex = _BankControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 4, 1, 1),
    _BankControlIndex_Type()
)
bankControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankControlIndex.setStatus("current")


class _BankControlStatus_Type(Integer32):
    """Custom type bankControlStatus based on Integer32"""
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
        *(("nostatus", 4),
          ("not-support", 5),
          ("off", 1),
          ("on", 2),
          ("reboot", 3))
    )


_BankControlStatus_Type.__name__ = "Integer32"
_BankControlStatus_Object = MibTableColumn
bankControlStatus = _BankControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 4, 1, 2),
    _BankControlStatus_Type()
)
bankControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankControlStatus.setStatus("current")
_BankIntegerValueTable_Object = MibTable
bankIntegerValueTable = _BankIntegerValueTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99)
)
if mibBuilder.loadTexts:
    bankIntegerValueTable.setStatus("current")
_BankIntegerValueEntry_Object = MibTableRow
bankIntegerValueEntry = _BankIntegerValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99, 1)
)
bankIntegerValueEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "bankIntegerValueIndex"),
)
if mibBuilder.loadTexts:
    bankIntegerValueEntry.setStatus("current")


class _BankIntegerValueIndex_Type(Integer32):
    """Custom type bankIntegerValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BankIntegerValueIndex_Type.__name__ = "Integer32"
_BankIntegerValueIndex_Object = MibTableColumn
bankIntegerValueIndex = _BankIntegerValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99, 1, 1),
    _BankIntegerValueIndex_Type()
)
bankIntegerValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankIntegerValueIndex.setStatus("current")
_BankIntegerCurrent_Type = Integer32
_BankIntegerCurrent_Object = MibTableColumn
bankIntegerCurrent = _BankIntegerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99, 1, 2),
    _BankIntegerCurrent_Type()
)
bankIntegerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankIntegerCurrent.setStatus("current")
_BankIntegerVoltage_Type = Integer32
_BankIntegerVoltage_Object = MibTableColumn
bankIntegerVoltage = _BankIntegerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99, 1, 3),
    _BankIntegerVoltage_Type()
)
bankIntegerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankIntegerVoltage.setStatus("current")
_BankIntegerPower_Type = Integer32
_BankIntegerPower_Object = MibTableColumn
bankIntegerPower = _BankIntegerPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99, 1, 4),
    _BankIntegerPower_Type()
)
bankIntegerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankIntegerPower.setStatus("current")
_BankIntegerPowerDissipation_Type = Integer32
_BankIntegerPowerDissipation_Object = MibTableColumn
bankIntegerPowerDissipation = _BankIntegerPowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 2, 3, 99, 1, 5),
    _BankIntegerPowerDissipation_Type()
)
bankIntegerPowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankIntegerPowerDissipation.setStatus("current")
_DeviceManagement_ObjectIdentity = ObjectIdentity
deviceManagement = _DeviceManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4)
)
_DeviceMAC_Type = DisplayString
_DeviceMAC_Object = MibScalar
deviceMAC = _DeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 1),
    _DeviceMAC_Type()
)
deviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMAC.setStatus("current")
_DeviceIPv4_Type = IpAddress
_DeviceIPv4_Object = MibScalar
deviceIPv4 = _DeviceIPv4_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 2),
    _DeviceIPv4_Type()
)
deviceIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIPv4.setStatus("current")
_DeviceFWversion_Type = DisplayString
_DeviceFWversion_Object = MibScalar
deviceFWversion = _DeviceFWversion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 3),
    _DeviceFWversion_Type()
)
deviceFWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFWversion.setStatus("current")
_DashBoard_ObjectIdentity = ObjectIdentity
dashBoard = _DashBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 4)
)


class _DashboardRow_Type(Integer32):
    """Custom type dashboardRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_DashboardRow_Type.__name__ = "Integer32"
_DashboardRow_Object = MibScalar
dashboardRow = _DashboardRow_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 4, 1),
    _DashboardRow_Type()
)
dashboardRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dashboardRow.setStatus("current")


class _DashboardColumn_Type(Integer32):
    """Custom type dashboardColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_DashboardColumn_Type.__name__ = "Integer32"
_DashboardColumn_Object = MibScalar
dashboardColumn = _DashboardColumn_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 4, 2),
    _DashboardColumn_Type()
)
dashboardColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dashboardColumn.setStatus("current")
_DashboardRackName_Type = DisplayString
_DashboardRackName_Object = MibScalar
dashboardRackName = _DashboardRackName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 4, 3),
    _DashboardRackName_Type()
)
dashboardRackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dashboardRackName.setStatus("current")
_ServicePorts_ObjectIdentity = ObjectIdentity
servicePorts = _ServicePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 5)
)


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 5, 1),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _HttpsPort_Type(Integer32):
    """Custom type httpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpsPort_Type.__name__ = "Integer32"
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 5, 2),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPort.setStatus("current")


class _HttpsOnlyEnable_Type(Integer32):
    """Custom type httpsOnlyEnable based on Integer32"""
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


_HttpsOnlyEnable_Type.__name__ = "Integer32"
_HttpsOnlyEnable_Object = MibScalar
httpsOnlyEnable = _HttpsOnlyEnable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 5, 3),
    _HttpsOnlyEnable_Type()
)
httpsOnlyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsOnlyEnable.setStatus("current")
_Ipv4config_ObjectIdentity = ObjectIdentity
ipv4config = _Ipv4config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6)
)


class _StaticIPEnabled_Type(Integer32):
    """Custom type staticIPEnabled based on Integer32"""
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


_StaticIPEnabled_Type.__name__ = "Integer32"
_StaticIPEnabled_Object = MibScalar
staticIPEnabled = _StaticIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 1),
    _StaticIPEnabled_Type()
)
staticIPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIPEnabled.setStatus("current")
_FixedIPv4_Type = IpAddress
_FixedIPv4_Object = MibScalar
fixedIPv4 = _FixedIPv4_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 2),
    _FixedIPv4_Type()
)
fixedIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedIPv4.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 3),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 4),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")


class _StaticDNSEnabled_Type(Integer32):
    """Custom type staticDNSEnabled based on Integer32"""
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


_StaticDNSEnabled_Type.__name__ = "Integer32"
_StaticDNSEnabled_Object = MibScalar
staticDNSEnabled = _StaticDNSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 5),
    _StaticDNSEnabled_Type()
)
staticDNSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDNSEnabled.setStatus("current")
_DnsPreferIPv4_Type = IpAddress
_DnsPreferIPv4_Object = MibScalar
dnsPreferIPv4 = _DnsPreferIPv4_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 6),
    _DnsPreferIPv4_Type()
)
dnsPreferIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsPreferIPv4.setStatus("current")
_DnsAlternateIPv4_Type = IpAddress
_DnsAlternateIPv4_Object = MibScalar
dnsAlternateIPv4 = _DnsAlternateIPv4_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 6, 7),
    _DnsAlternateIPv4_Type()
)
dnsAlternateIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsAlternateIPv4.setStatus("current")
_EventNotification_ObjectIdentity = ObjectIdentity
eventNotification = _EventNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7)
)
_Devicesnmp_ObjectIdentity = ObjectIdentity
devicesnmp = _Devicesnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1)
)


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
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


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibScalar
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 1),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("current")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibScalar
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 2),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("current")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "trapReceiverNumber"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("current")


class _TrapReceiverNumber_Type(Integer32):
    """Custom type trapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TrapReceiverNumber_Type.__name__ = "Integer32"
_TrapReceiverNumber_Object = MibTableColumn
trapReceiverNumber = _TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 1),
    _TrapReceiverNumber_Type()
)
trapReceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapReceiverNumber.setStatus("current")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibTableColumn
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 2),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("current")


class _TrapPort_Type(Integer32):
    """Custom type trapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapPort_Type.__name__ = "Integer32"
_TrapPort_Object = MibTableColumn
trapPort = _TrapPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 3),
    _TrapPort_Type()
)
trapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapPort.setStatus("current")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 4),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")


class _TrapUsername_Type(DisplayString):
    """Custom type trapUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrapUsername_Type.__name__ = "DisplayString"
_TrapUsername_Object = MibTableColumn
trapUsername = _TrapUsername_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 5),
    _TrapUsername_Type()
)
trapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapUsername.setStatus("current")


class _TrapAuthpassword_Type(DisplayString):
    """Custom type trapAuthpassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 20),
    )


_TrapAuthpassword_Type.__name__ = "DisplayString"
_TrapAuthpassword_Object = MibTableColumn
trapAuthpassword = _TrapAuthpassword_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 6),
    _TrapAuthpassword_Type()
)
trapAuthpassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAuthpassword.setStatus("current")


class _TrapPrivpassword_Type(DisplayString):
    """Custom type trapPrivpassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 20),
    )


_TrapPrivpassword_Type.__name__ = "DisplayString"
_TrapPrivpassword_Object = MibTableColumn
trapPrivpassword = _TrapPrivpassword_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 1, 3, 1, 7),
    _TrapPrivpassword_Type()
)
trapPrivpassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapPrivpassword.setStatus("current")
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 2)
)


class _SysLogServerEnabled_Type(Integer32):
    """Custom type sysLogServerEnabled based on Integer32"""
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


_SysLogServerEnabled_Type.__name__ = "Integer32"
_SysLogServerEnabled_Object = MibScalar
sysLogServerEnabled = _SysLogServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 2, 1),
    _SysLogServerEnabled_Type()
)
sysLogServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerEnabled.setStatus("current")
_SysLogServerIPv4_Type = IpAddress
_SysLogServerIPv4_Object = MibScalar
sysLogServerIPv4 = _SysLogServerIPv4_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 2, 2),
    _SysLogServerIPv4_Type()
)
sysLogServerIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerIPv4.setStatus("current")


class _SysLogServerPort_Type(Integer32):
    """Custom type sysLogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLogServerPort_Type.__name__ = "Integer32"
_SysLogServerPort_Object = MibScalar
sysLogServerPort = _SysLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 2, 3),
    _SysLogServerPort_Type()
)
sysLogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerPort.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3)
)


class _SmtpServerEnabled_Type(Integer32):
    """Custom type smtpServerEnabled based on Integer32"""
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


_SmtpServerEnabled_Type.__name__ = "Integer32"
_SmtpServerEnabled_Object = MibScalar
smtpServerEnabled = _SmtpServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 1),
    _SmtpServerEnabled_Type()
)
smtpServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerEnabled.setStatus("current")
_SmtpServerName_Type = DisplayString
_SmtpServerName_Object = MibScalar
smtpServerName = _SmtpServerName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 2),
    _SmtpServerName_Type()
)
smtpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerName.setStatus("current")


class _SmtpAuthEnabled_Type(Integer32):
    """Custom type smtpAuthEnabled based on Integer32"""
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


_SmtpAuthEnabled_Type.__name__ = "Integer32"
_SmtpAuthEnabled_Object = MibScalar
smtpAuthEnabled = _SmtpAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 3),
    _SmtpAuthEnabled_Type()
)
smtpAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpAuthEnabled.setStatus("current")
_SmtpAccountName_Type = DisplayString
_SmtpAccountName_Object = MibScalar
smtpAccountName = _SmtpAccountName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 4),
    _SmtpAccountName_Type()
)
smtpAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpAccountName.setStatus("current")
_SmtpAccountPwd_Type = DisplayString
_SmtpAccountPwd_Object = MibScalar
smtpAccountPwd = _SmtpAccountPwd_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 5),
    _SmtpAccountPwd_Type()
)
smtpAccountPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpAccountPwd.setStatus("current")
_SmtpMailFrom_Type = DisplayString
_SmtpMailFrom_Object = MibScalar
smtpMailFrom = _SmtpMailFrom_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 6),
    _SmtpMailFrom_Type()
)
smtpMailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpMailFrom.setStatus("current")
_SmtpMailTo_Type = DisplayString
_SmtpMailTo_Object = MibScalar
smtpMailTo = _SmtpMailTo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 3, 7),
    _SmtpMailTo_Type()
)
smtpMailTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpMailTo.setStatus("current")
_ConfigurationNotification_ObjectIdentity = ObjectIdentity
configurationNotification = _ConfigurationNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 9)
)


class _ConfigurationNotifyEnabled_Type(Integer32):
    """Custom type configurationNotifyEnabled based on Integer32"""
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


_ConfigurationNotifyEnabled_Type.__name__ = "Integer32"
_ConfigurationNotifyEnabled_Object = MibScalar
configurationNotifyEnabled = _ConfigurationNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 9, 1),
    _ConfigurationNotifyEnabled_Type()
)
configurationNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationNotifyEnabled.setStatus("current")
_DateTime_ObjectIdentity = ObjectIdentity
dateTime = _DateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8)
)
_TimeZone_ObjectIdentity = ObjectIdentity
timeZone = _TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 1)
)
_TimeZoneSetting_Type = Integer32
_TimeZoneSetting_Object = MibScalar
timeZoneSetting = _TimeZoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 1, 1),
    _TimeZoneSetting_Type()
)
timeZoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZoneSetting.setStatus("current")


class _DstEnabled_Type(Integer32):
    """Custom type dstEnabled based on Integer32"""
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


_DstEnabled_Type.__name__ = "Integer32"
_DstEnabled_Object = MibScalar
dstEnabled = _DstEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 1, 2),
    _DstEnabled_Type()
)
dstEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dstEnabled.setStatus("current")
_ManualInput_ObjectIdentity = ObjectIdentity
manualInput = _ManualInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 2)
)
_DateSetting_Type = DisplayString
_DateSetting_Object = MibScalar
dateSetting = _DateSetting_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 2, 1),
    _DateSetting_Type()
)
dateSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateSetting.setStatus("current")
_TimeSetting_Type = DisplayString
_TimeSetting_Object = MibScalar
timeSetting = _TimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 2, 2),
    _TimeSetting_Type()
)
timeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSetting.setStatus("current")
_NetworkTime_ObjectIdentity = ObjectIdentity
networkTime = _NetworkTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3)
)


class _AutoAdjustEnabled_Type(Integer32):
    """Custom type autoAdjustEnabled based on Integer32"""
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


_AutoAdjustEnabled_Type.__name__ = "Integer32"
_AutoAdjustEnabled_Object = MibScalar
autoAdjustEnabled = _AutoAdjustEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 1),
    _AutoAdjustEnabled_Type()
)
autoAdjustEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoAdjustEnabled.setStatus("current")
_PreferNTP_Type = Integer32
_PreferNTP_Object = MibScalar
preferNTP = _PreferNTP_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 2),
    _PreferNTP_Type()
)
preferNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferNTP.setStatus("current")


class _PreferServerIPenable_Type(Integer32):
    """Custom type preferServerIPenable based on Integer32"""
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


_PreferServerIPenable_Type.__name__ = "Integer32"
_PreferServerIPenable_Object = MibScalar
preferServerIPenable = _PreferServerIPenable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 3),
    _PreferServerIPenable_Type()
)
preferServerIPenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferServerIPenable.setStatus("current")
_PreferNTPIp_Type = IpAddress
_PreferNTPIp_Object = MibScalar
preferNTPIp = _PreferNTPIp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 4),
    _PreferNTPIp_Type()
)
preferNTPIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferNTPIp.setStatus("current")


class _AlternateNtpEnabled_Type(Integer32):
    """Custom type alternateNtpEnabled based on Integer32"""
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


_AlternateNtpEnabled_Type.__name__ = "Integer32"
_AlternateNtpEnabled_Object = MibScalar
alternateNtpEnabled = _AlternateNtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 5),
    _AlternateNtpEnabled_Type()
)
alternateNtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateNtpEnabled.setStatus("current")
_AlternateNtp_Type = Integer32
_AlternateNtp_Object = MibScalar
alternateNtp = _AlternateNtp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 6),
    _AlternateNtp_Type()
)
alternateNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateNtp.setStatus("current")


class _AlternateServerIPenable_Type(Integer32):
    """Custom type alternateServerIPenable based on Integer32"""
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


_AlternateServerIPenable_Type.__name__ = "Integer32"
_AlternateServerIPenable_Object = MibScalar
alternateServerIPenable = _AlternateServerIPenable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 7),
    _AlternateServerIPenable_Type()
)
alternateServerIPenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateServerIPenable.setStatus("current")
_AlternateNtpIp_Type = IpAddress
_AlternateNtpIp_Object = MibScalar
alternateNtpIp = _AlternateNtpIp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 8),
    _AlternateNtpIp_Type()
)
alternateNtpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateNtpIp.setStatus("current")
_AdjustTimeEveryDays_Type = Integer32
_AdjustTimeEveryDays_Object = MibScalar
adjustTimeEveryDays = _AdjustTimeEveryDays_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 8, 3, 9),
    _AdjustTimeEveryDays_Type()
)
adjustTimeEveryDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adjustTimeEveryDays.setStatus("current")
_Devicesecurity_ObjectIdentity = ObjectIdentity
devicesecurity = _Devicesecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5)
)
_LoginFailures_ObjectIdentity = ObjectIdentity
loginFailures = _LoginFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 1)
)


class _LoginAllowTimes_Type(Integer32):
    """Custom type loginAllowTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LoginAllowTimes_Type.__name__ = "Integer32"
_LoginAllowTimes_Object = MibScalar
loginAllowTimes = _LoginAllowTimes_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 1, 1),
    _LoginAllowTimes_Type()
)
loginAllowTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginAllowTimes.setStatus("current")


class _LoginTimeOut_Type(Integer32):
    """Custom type loginTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_LoginTimeOut_Type.__name__ = "Integer32"
_LoginTimeOut_Object = MibScalar
loginTimeOut = _LoginTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 1, 2),
    _LoginTimeOut_Type()
)
loginTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginTimeOut.setStatus("current")
_WorkingMode_ObjectIdentity = ObjectIdentity
workingMode = _WorkingMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 2)
)


class _IcmpEnabled_Type(Integer32):
    """Custom type icmpEnabled based on Integer32"""
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


_IcmpEnabled_Type.__name__ = "Integer32"
_IcmpEnabled_Object = MibScalar
icmpEnabled = _IcmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 2, 1),
    _IcmpEnabled_Type()
)
icmpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpEnabled.setStatus("current")
_AccountPolicy_ObjectIdentity = ObjectIdentity
accountPolicy = _AccountPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3)
)


class _MinUserNameLen_Type(Integer32):
    """Custom type minUserNameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MinUserNameLen_Type.__name__ = "Integer32"
_MinUserNameLen_Object = MibScalar
minUserNameLen = _MinUserNameLen_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3, 1),
    _MinUserNameLen_Type()
)
minUserNameLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minUserNameLen.setStatus("current")


class _MinUserPwdLen_Type(Integer32):
    """Custom type minUserPwdLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MinUserPwdLen_Type.__name__ = "Integer32"
_MinUserPwdLen_Object = MibScalar
minUserPwdLen = _MinUserPwdLen_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3, 2),
    _MinUserPwdLen_Type()
)
minUserPwdLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minUserPwdLen.setStatus("current")


class _UpperCaseEnabled_Type(Integer32):
    """Custom type upperCaseEnabled based on Integer32"""
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


_UpperCaseEnabled_Type.__name__ = "Integer32"
_UpperCaseEnabled_Object = MibScalar
upperCaseEnabled = _UpperCaseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3, 3),
    _UpperCaseEnabled_Type()
)
upperCaseEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperCaseEnabled.setStatus("current")


class _LowerCaseEnabled_Type(Integer32):
    """Custom type lowerCaseEnabled based on Integer32"""
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


_LowerCaseEnabled_Type.__name__ = "Integer32"
_LowerCaseEnabled_Object = MibScalar
lowerCaseEnabled = _LowerCaseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3, 4),
    _LowerCaseEnabled_Type()
)
lowerCaseEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowerCaseEnabled.setStatus("current")


class _NumberEnabled_Type(Integer32):
    """Custom type numberEnabled based on Integer32"""
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


_NumberEnabled_Type.__name__ = "Integer32"
_NumberEnabled_Object = MibScalar
numberEnabled = _NumberEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3, 5),
    _NumberEnabled_Type()
)
numberEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberEnabled.setStatus("current")


class _DisableDuplicateLogin_Type(Integer32):
    """Custom type disableDuplicateLogin based on Integer32"""
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


_DisableDuplicateLogin_Type.__name__ = "Integer32"
_DisableDuplicateLogin_Object = MibScalar
disableDuplicateLogin = _DisableDuplicateLogin_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 3, 6),
    _DisableDuplicateLogin_Type()
)
disableDuplicateLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disableDuplicateLogin.setStatus("current")
_LoginRestriction_ObjectIdentity = ObjectIdentity
loginRestriction = _LoginRestriction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4)
)
_LoginString_Type = DisplayString
_LoginString_Object = MibScalar
loginString = _LoginString_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 1),
    _LoginString_Type()
)
loginString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginString.setStatus("current")
_IpFilter_ObjectIdentity = ObjectIdentity
ipFilter = _IpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2)
)


class _IpFilterEnabled_Type(Integer32):
    """Custom type ipFilterEnabled based on Integer32"""
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


_IpFilterEnabled_Type.__name__ = "Integer32"
_IpFilterEnabled_Object = MibScalar
ipFilterEnabled = _IpFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 1),
    _IpFilterEnabled_Type()
)
ipFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterEnabled.setStatus("current")


class _IpFilterRule_Type(Integer32):
    """Custom type ipFilterRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_IpFilterRule_Type.__name__ = "Integer32"
_IpFilterRule_Object = MibScalar
ipFilterRule = _IpFilterRule_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 2),
    _IpFilterRule_Type()
)
ipFilterRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterRule.setStatus("current")
_IpFilterTable_Object = MibTable
ipFilterTable = _IpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    ipFilterTable.setStatus("current")
_IpFilterEntry_Object = MibTableRow
ipFilterEntry = _IpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 3, 1)
)
ipFilterEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "ipFilterIndex"),
)
if mibBuilder.loadTexts:
    ipFilterEntry.setStatus("current")


class _IpFilterIndex_Type(Integer32):
    """Custom type ipFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IpFilterIndex_Type.__name__ = "Integer32"
_IpFilterIndex_Object = MibTableColumn
ipFilterIndex = _IpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 3, 1, 1),
    _IpFilterIndex_Type()
)
ipFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterIndex.setStatus("current")
_IpFilterFrom_Type = IpAddress
_IpFilterFrom_Object = MibTableColumn
ipFilterFrom = _IpFilterFrom_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 3, 1, 2),
    _IpFilterFrom_Type()
)
ipFilterFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterFrom.setStatus("current")
_IpFilterTo_Type = IpAddress
_IpFilterTo_Object = MibTableColumn
ipFilterTo = _IpFilterTo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 2, 3, 1, 3),
    _IpFilterTo_Type()
)
ipFilterTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterTo.setStatus("current")
_MacFilter_ObjectIdentity = ObjectIdentity
macFilter = _MacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3)
)


class _MacFilterEnabled_Type(Integer32):
    """Custom type macFilterEnabled based on Integer32"""
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


_MacFilterEnabled_Type.__name__ = "Integer32"
_MacFilterEnabled_Object = MibScalar
macFilterEnabled = _MacFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3, 1),
    _MacFilterEnabled_Type()
)
macFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterEnabled.setStatus("current")


class _MacFilterRule_Type(Integer32):
    """Custom type macFilterRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_MacFilterRule_Type.__name__ = "Integer32"
_MacFilterRule_Object = MibScalar
macFilterRule = _MacFilterRule_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3, 2),
    _MacFilterRule_Type()
)
macFilterRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterRule.setStatus("current")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3, 3)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("current")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3, 3, 1)
)
macFilterEntry.setIndexNames(
    (0, "ATEN-PE-CFG", "macFilterIndex"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("current")


class _MacFilterIndex_Type(Integer32):
    """Custom type macFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MacFilterIndex_Type.__name__ = "Integer32"
_MacFilterIndex_Object = MibTableColumn
macFilterIndex = _MacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3, 3, 1, 1),
    _MacFilterIndex_Type()
)
macFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterIndex.setStatus("current")
_MacFilterSet_Type = DisplayString
_MacFilterSet_Object = MibTableColumn
macFilterSet = _MacFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 4, 3, 3, 1, 2),
    _MacFilterSet_Type()
)
macFilterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterSet.setStatus("current")
_Authentication_ObjectIdentity = ObjectIdentity
authentication = _Authentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5)
)
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1)
)


class _RadiusEnabled_Type(Integer32):
    """Custom type radiusEnabled based on Integer32"""
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


_RadiusEnabled_Type.__name__ = "Integer32"
_RadiusEnabled_Object = MibScalar
radiusEnabled = _RadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 1),
    _RadiusEnabled_Type()
)
radiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusEnabled.setStatus("current")
_PreferRadiusIp_Type = IpAddress
_PreferRadiusIp_Object = MibScalar
preferRadiusIp = _PreferRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 2),
    _PreferRadiusIp_Type()
)
preferRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferRadiusIp.setStatus("current")


class _PreferRadiusPort_Type(Integer32):
    """Custom type preferRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PreferRadiusPort_Type.__name__ = "Integer32"
_PreferRadiusPort_Object = MibScalar
preferRadiusPort = _PreferRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 3),
    _PreferRadiusPort_Type()
)
preferRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferRadiusPort.setStatus("current")
_AlternateRadiusIp_Type = IpAddress
_AlternateRadiusIp_Object = MibScalar
alternateRadiusIp = _AlternateRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 4),
    _AlternateRadiusIp_Type()
)
alternateRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateRadiusIp.setStatus("current")


class _AlternateRadiusPort_Type(Integer32):
    """Custom type alternateRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlternateRadiusPort_Type.__name__ = "Integer32"
_AlternateRadiusPort_Object = MibScalar
alternateRadiusPort = _AlternateRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 5),
    _AlternateRadiusPort_Type()
)
alternateRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateRadiusPort.setStatus("current")


class _RadiusTimeOut_Type(Integer32):
    """Custom type radiusTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RadiusTimeOut_Type.__name__ = "Integer32"
_RadiusTimeOut_Object = MibScalar
radiusTimeOut = _RadiusTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 6),
    _RadiusTimeOut_Type()
)
radiusTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusTimeOut.setStatus("current")


class _RadiusRetry_Type(Integer32):
    """Custom type radiusRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RadiusRetry_Type.__name__ = "Integer32"
_RadiusRetry_Object = MibScalar
radiusRetry = _RadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 7),
    _RadiusRetry_Type()
)
radiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusRetry.setStatus("current")
_RadiusSecret_Type = DisplayString
_RadiusSecret_Object = MibScalar
radiusSecret = _RadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 5, 5, 1, 8),
    _RadiusSecret_Type()
)
radiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSecret.setStatus("current")


class _RebootDevice_Type(Integer32):
    """Custom type rebootDevice based on Integer32"""
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


_RebootDevice_Type.__name__ = "Integer32"
_RebootDevice_Object = MibScalar
rebootDevice = _RebootDevice_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 6),
    _RebootDevice_Type()
)
rebootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootDevice.setStatus("current")

# Managed Objects groups


# Notification objects

configurationNotifyTrapMSG = NotificationType(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 3, 4, 7, 9, 2)
)
if mibBuilder.loadTexts:
    configurationNotifyTrapMSG.setStatus(
        "current"
    )

customTrapMSG = NotificationType(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    customTrapMSG.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATEN-PE-CFG",
    **{"aten": aten,
       "atenProducts": atenProducts,
       "overip": overip,
       "poweroverip": poweroverip,
       "pe": pe,
       "userManagement": userManagement,
       "usrListTable": usrListTable,
       "usrListEntry": usrListEntry,
       "usrIndex": usrIndex,
       "usrType": usrType,
       "usrName": usrName,
       "usrPassword": usrPassword,
       "usrPort1Auth": usrPort1Auth,
       "usrPort2Auth": usrPort2Auth,
       "usrPort3Auth": usrPort3Auth,
       "usrPort4Auth": usrPort4Auth,
       "usrPort5Auth": usrPort5Auth,
       "usrPort6Auth": usrPort6Auth,
       "usrPort7Auth": usrPort7Auth,
       "usrPort8Auth": usrPort8Auth,
       "usrPort9Auth": usrPort9Auth,
       "usrPort10Auth": usrPort10Auth,
       "usrPort11Auth": usrPort11Auth,
       "usrPort12Auth": usrPort12Auth,
       "usrPort13Auth": usrPort13Auth,
       "usrPort14Auth": usrPort14Auth,
       "usrPort15Auth": usrPort15Auth,
       "usrPort16Auth": usrPort16Auth,
       "usrPort17Auth": usrPort17Auth,
       "usrPort18Auth": usrPort18Auth,
       "usrPort19Auth": usrPort19Auth,
       "usrPort20Auth": usrPort20Auth,
       "usrPort21Auth": usrPort21Auth,
       "usrPort22Auth": usrPort22Auth,
       "usrPort23Auth": usrPort23Auth,
       "usrPort24Auth": usrPort24Auth,
       "usrPort25Auth": usrPort25Auth,
       "usrPort26Auth": usrPort26Auth,
       "usrPort27Auth": usrPort27Auth,
       "usrPort28Auth": usrPort28Auth,
       "usrPort29Auth": usrPort29Auth,
       "usrPort30Auth": usrPort30Auth,
       "usrPort31Auth": usrPort31Auth,
       "usrPort32Auth": usrPort32Auth,
       "usrPort33Auth": usrPort33Auth,
       "usrPort34Auth": usrPort34Auth,
       "usrPort35Auth": usrPort35Auth,
       "usrPort36Auth": usrPort36Auth,
       "usrPort37Auth": usrPort37Auth,
       "usrPort38Auth": usrPort38Auth,
       "usrPort39Auth": usrPort39Auth,
       "usrPort40Auth": usrPort40Auth,
       "usrPort41Auth": usrPort41Auth,
       "usrPort42Auth": usrPort42Auth,
       "usrEnable": usrEnable,
       "control": control,
       "device": device,
       "modelName": modelName,
       "deviceName": deviceName,
       "deviceValueTable": deviceValueTable,
       "deviceValueEntry": deviceValueEntry,
       "deviceValueIndex": deviceValueIndex,
       "deviceCurrent": deviceCurrent,
       "deviceVoltage": deviceVoltage,
       "devicePower": devicePower,
       "devicePowerDissipation": devicePowerDissipation,
       "inputMaxVoltage": inputMaxVoltage,
       "inputMaxCurrent": inputMaxCurrent,
       "powerCapacity": powerCapacity,
       "devicePowerFactor": devicePowerFactor,
       "sensorValueTable": sensorValueTable,
       "sensorValueEntry": sensorValueEntry,
       "sensorValueIndex": sensorValueIndex,
       "sensorTemperature": sensorTemperature,
       "sensorHumidity": sensorHumidity,
       "sensorPressure": sensorPressure,
       "sensorProperty": sensorProperty,
       "deviceOutletStatusTable": deviceOutletStatusTable,
       "deviceOutletStatusEntry": deviceOutletStatusEntry,
       "deviceOutletStatusIndex": deviceOutletStatusIndex,
       "displayOutletStatus": displayOutletStatus,
       "deviceConfigTable": deviceConfigTable,
       "deviceConfigEntry": deviceConfigEntry,
       "deviceConfigIndex": deviceConfigIndex,
       "deviceMinCurMT": deviceMinCurMT,
       "deviceMaxCurMT": deviceMaxCurMT,
       "deviceMinVolMT": deviceMinVolMT,
       "deviceMaxVolMT": deviceMaxVolMT,
       "deviceMinPMT": deviceMinPMT,
       "deviceMaxPMT": deviceMaxPMT,
       "deviceMaxPDMT": deviceMaxPDMT,
       "deviceSensorTresholdTable": deviceSensorTresholdTable,
       "deviceSensorTresholdEntry": deviceSensorTresholdEntry,
       "deviceSensorTresholdIndex": deviceSensorTresholdIndex,
       "sensorMinTempMT": sensorMinTempMT,
       "sensorMaxTempMT": sensorMaxTempMT,
       "sensorMinHumMT": sensorMinHumMT,
       "sensorMaxHumMT": sensorMaxHumMT,
       "sensorMinPressMT": sensorMinPressMT,
       "sensorMaxPressMT": sensorMaxPressMT,
       "deviceOutletControl": deviceOutletControl,
       "deviceOutletReboot": deviceOutletReboot,
       "switchable": switchable,
       "perportreading": perportreading,
       "sensornumber": sensornumber,
       "outletnumber": outletnumber,
       "banknumber": banknumber,
       "doorSensor": doorSensor,
       "doorSensorStatus": doorSensorStatus,
       "doorSensorType": doorSensorType,
       "pop": pop,
       "enablePOPmode": enablePOPmode,
       "popThreshold": popThreshold,
       "enableOutletPOPmode": enableOutletPOPmode,
       "enableLIFOPOPmode": enableLIFOPOPmode,
       "enablePriorityPOPmode": enablePriorityPOPmode,
       "cap": cap,
       "enableCAPmode": enableCAPmode,
       "outletCAPTable": outletCAPTable,
       "outletCAPEntry": outletCAPEntry,
       "outletCAPIndex": outletCAPIndex,
       "outletCAPPriority": outletCAPPriority,
       "outletInitMode": outletInitMode,
       "deviceIntegerValueTable": deviceIntegerValueTable,
       "deviceIntegerValueEntry": deviceIntegerValueEntry,
       "deviceIntegerValueIndex": deviceIntegerValueIndex,
       "deviceIntegerCurrent": deviceIntegerCurrent,
       "deviceIntegerVoltage": deviceIntegerVoltage,
       "deviceIntegerPower": deviceIntegerPower,
       "deviceIntegerPowerDissipation": deviceIntegerPowerDissipation,
       "sensorIntegerValueTable": sensorIntegerValueTable,
       "sensorIntegerValueEntry": sensorIntegerValueEntry,
       "sensorIntegerValueIndex": sensorIntegerValueIndex,
       "sensorIntegerTemperature": sensorIntegerTemperature,
       "sensorIntegerHumidity": sensorIntegerHumidity,
       "sensorIntegerPressure": sensorIntegerPressure,
       "outlet": outlet,
       "outletValueTable": outletValueTable,
       "outletValueEntry": outletValueEntry,
       "outletValueIndex": outletValueIndex,
       "outletCurrent": outletCurrent,
       "outletVoltage": outletVoltage,
       "outletPower": outletPower,
       "outletPowerDissipation": outletPowerDissipation,
       "outletMaxCurrent": outletMaxCurrent,
       "outletPowerFactor": outletPowerFactor,
       "outlet1Status": outlet1Status,
       "outlet2Status": outlet2Status,
       "outlet3Status": outlet3Status,
       "outlet4Status": outlet4Status,
       "outlet5Status": outlet5Status,
       "outlet6Status": outlet6Status,
       "outlet7Status": outlet7Status,
       "outlet8Status": outlet8Status,
       "outletConfigTable": outletConfigTable,
       "outletConfigEntry": outletConfigEntry,
       "outletConfigIndex": outletConfigIndex,
       "outletName": outletName,
       "outletConfirmation": outletConfirmation,
       "outletOnDelayTime": outletOnDelayTime,
       "outletOffDelayTime": outletOffDelayTime,
       "outletShutdownMethod": outletShutdownMethod,
       "outletMAC": outletMAC,
       "outletMinCurMT": outletMinCurMT,
       "outletMaxCurMT": outletMaxCurMT,
       "outletMinVolMT": outletMinVolMT,
       "outletMaxVolMT": outletMaxVolMT,
       "outletMinPMT": outletMinPMT,
       "outletMaxPMT": outletMaxPMT,
       "outletMaxPDMT": outletMaxPDMT,
       "outlet9Status": outlet9Status,
       "outlet10Status": outlet10Status,
       "outlet11Status": outlet11Status,
       "outlet12Status": outlet12Status,
       "outlet13Status": outlet13Status,
       "outlet14Status": outlet14Status,
       "outlet15Status": outlet15Status,
       "outlet16Status": outlet16Status,
       "outlet17Status": outlet17Status,
       "outlet18Status": outlet18Status,
       "outlet19Status": outlet19Status,
       "outlet20Status": outlet20Status,
       "outlet21Status": outlet21Status,
       "outlet22Status": outlet22Status,
       "outlet23Status": outlet23Status,
       "outlet24Status": outlet24Status,
       "outlet25Status": outlet25Status,
       "outlet26Status": outlet26Status,
       "outlet27Status": outlet27Status,
       "outlet28Status": outlet28Status,
       "outlet29Status": outlet29Status,
       "outlet30Status": outlet30Status,
       "outlet31Status": outlet31Status,
       "outlet32Status": outlet32Status,
       "outlet33Status": outlet33Status,
       "outlet34Status": outlet34Status,
       "outlet35Status": outlet35Status,
       "outlet36Status": outlet36Status,
       "outlet37Status": outlet37Status,
       "outlet38Status": outlet38Status,
       "outlet39Status": outlet39Status,
       "outlet40Status": outlet40Status,
       "outlet41Status": outlet41Status,
       "outlet42Status": outlet42Status,
       "outletSwitchableTable": outletSwitchableTable,
       "outletSwitchableEntry": outletSwitchableEntry,
       "outletSwitchableIndex": outletSwitchableIndex,
       "outletSwitchable": outletSwitchable,
       "outletIntegerValueTable": outletIntegerValueTable,
       "outletIntegerValueEntry": outletIntegerValueEntry,
       "outletIntegerValueIndex": outletIntegerValueIndex,
       "outletIntegerCurrent": outletIntegerCurrent,
       "outletIntegerVoltage": outletIntegerVoltage,
       "outletIntegerPower": outletIntegerPower,
       "outletIntegerPowerDissipation": outletIntegerPowerDissipation,
       "bank": bank,
       "breakerStatusTable": breakerStatusTable,
       "breakerStatusEntry": breakerStatusEntry,
       "breakerStatusIndex": breakerStatusIndex,
       "breakerStatus": breakerStatus,
       "bankValueTable": bankValueTable,
       "bankValueEntry": bankValueEntry,
       "bankValueIndex": bankValueIndex,
       "bankCurrent": bankCurrent,
       "bankVoltage": bankVoltage,
       "bankPower": bankPower,
       "bankPowerDissipation": bankPowerDissipation,
       "bankMaxCurrent": bankMaxCurrent,
       "bankAttachStatus": bankAttachStatus,
       "bankPowerFactor": bankPowerFactor,
       "bankConfigTable": bankConfigTable,
       "bankConfigEntry": bankConfigEntry,
       "bankConfigIndex": bankConfigIndex,
       "bankName": bankName,
       "bankMinCurMT": bankMinCurMT,
       "bankMaxCurMT": bankMaxCurMT,
       "bankMinVolMT": bankMinVolMT,
       "bankMaxVolMT": bankMaxVolMT,
       "bankMinPMT": bankMinPMT,
       "bankMaxPMT": bankMaxPMT,
       "bankMaxPDMT": bankMaxPDMT,
       "bankControlTable": bankControlTable,
       "bankControlEntry": bankControlEntry,
       "bankControlIndex": bankControlIndex,
       "bankControlStatus": bankControlStatus,
       "bankIntegerValueTable": bankIntegerValueTable,
       "bankIntegerValueEntry": bankIntegerValueEntry,
       "bankIntegerValueIndex": bankIntegerValueIndex,
       "bankIntegerCurrent": bankIntegerCurrent,
       "bankIntegerVoltage": bankIntegerVoltage,
       "bankIntegerPower": bankIntegerPower,
       "bankIntegerPowerDissipation": bankIntegerPowerDissipation,
       "deviceManagement": deviceManagement,
       "config": config,
       "deviceMAC": deviceMAC,
       "deviceIPv4": deviceIPv4,
       "deviceFWversion": deviceFWversion,
       "dashBoard": dashBoard,
       "dashboardRow": dashboardRow,
       "dashboardColumn": dashboardColumn,
       "dashboardRackName": dashboardRackName,
       "servicePorts": servicePorts,
       "httpPort": httpPort,
       "httpsPort": httpsPort,
       "httpsOnlyEnable": httpsOnlyEnable,
       "ipv4config": ipv4config,
       "staticIPEnabled": staticIPEnabled,
       "fixedIPv4": fixedIPv4,
       "subnetMask": subnetMask,
       "gateway": gateway,
       "staticDNSEnabled": staticDNSEnabled,
       "dnsPreferIPv4": dnsPreferIPv4,
       "dnsAlternateIPv4": dnsAlternateIPv4,
       "eventNotification": eventNotification,
       "devicesnmp": devicesnmp,
       "trapEnabled": trapEnabled,
       "trapVersion": trapVersion,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "trapReceiverNumber": trapReceiverNumber,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapPort": trapPort,
       "trapCommunity": trapCommunity,
       "trapUsername": trapUsername,
       "trapAuthpassword": trapAuthpassword,
       "trapPrivpassword": trapPrivpassword,
       "syslog": syslog,
       "sysLogServerEnabled": sysLogServerEnabled,
       "sysLogServerIPv4": sysLogServerIPv4,
       "sysLogServerPort": sysLogServerPort,
       "smtp": smtp,
       "smtpServerEnabled": smtpServerEnabled,
       "smtpServerName": smtpServerName,
       "smtpAuthEnabled": smtpAuthEnabled,
       "smtpAccountName": smtpAccountName,
       "smtpAccountPwd": smtpAccountPwd,
       "smtpMailFrom": smtpMailFrom,
       "smtpMailTo": smtpMailTo,
       "configurationNotification": configurationNotification,
       "configurationNotifyEnabled": configurationNotifyEnabled,
       "configurationNotifyTrapMSG": configurationNotifyTrapMSG,
       "dateTime": dateTime,
       "timeZone": timeZone,
       "timeZoneSetting": timeZoneSetting,
       "dstEnabled": dstEnabled,
       "manualInput": manualInput,
       "dateSetting": dateSetting,
       "timeSetting": timeSetting,
       "networkTime": networkTime,
       "autoAdjustEnabled": autoAdjustEnabled,
       "preferNTP": preferNTP,
       "preferServerIPenable": preferServerIPenable,
       "preferNTPIp": preferNTPIp,
       "alternateNtpEnabled": alternateNtpEnabled,
       "alternateNtp": alternateNtp,
       "alternateServerIPenable": alternateServerIPenable,
       "alternateNtpIp": alternateNtpIp,
       "adjustTimeEveryDays": adjustTimeEveryDays,
       "devicesecurity": devicesecurity,
       "loginFailures": loginFailures,
       "loginAllowTimes": loginAllowTimes,
       "loginTimeOut": loginTimeOut,
       "workingMode": workingMode,
       "icmpEnabled": icmpEnabled,
       "accountPolicy": accountPolicy,
       "minUserNameLen": minUserNameLen,
       "minUserPwdLen": minUserPwdLen,
       "upperCaseEnabled": upperCaseEnabled,
       "lowerCaseEnabled": lowerCaseEnabled,
       "numberEnabled": numberEnabled,
       "disableDuplicateLogin": disableDuplicateLogin,
       "loginRestriction": loginRestriction,
       "loginString": loginString,
       "ipFilter": ipFilter,
       "ipFilterEnabled": ipFilterEnabled,
       "ipFilterRule": ipFilterRule,
       "ipFilterTable": ipFilterTable,
       "ipFilterEntry": ipFilterEntry,
       "ipFilterIndex": ipFilterIndex,
       "ipFilterFrom": ipFilterFrom,
       "ipFilterTo": ipFilterTo,
       "macFilter": macFilter,
       "macFilterEnabled": macFilterEnabled,
       "macFilterRule": macFilterRule,
       "macFilterTable": macFilterTable,
       "macFilterEntry": macFilterEntry,
       "macFilterIndex": macFilterIndex,
       "macFilterSet": macFilterSet,
       "authentication": authentication,
       "radius": radius,
       "radiusEnabled": radiusEnabled,
       "preferRadiusIp": preferRadiusIp,
       "preferRadiusPort": preferRadiusPort,
       "alternateRadiusIp": alternateRadiusIp,
       "alternateRadiusPort": alternateRadiusPort,
       "radiusTimeOut": radiusTimeOut,
       "radiusRetry": radiusRetry,
       "radiusSecret": radiusSecret,
       "customTrapMSG": customTrapMSG,
       "rebootDevice": rebootDevice}
)
