# SNMP MIB module (AT-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:20 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

cc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37)
)
cc.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CcDetailsTable_Object = MibTable
ccDetailsTable = _CcDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1)
)
if mibBuilder.loadTexts:
    ccDetailsTable.setStatus("current")
_CcDetailsEntry_Object = MibTableRow
ccDetailsEntry = _CcDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1)
)
ccDetailsEntry.setIndexNames(
    (0, "AT-ISDN-MIB", "ccDetailsIndex"),
)
if mibBuilder.loadTexts:
    ccDetailsEntry.setStatus("current")


class _CcDetailsIndex_Type(Integer32):
    """Custom type ccDetailsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcDetailsIndex_Type.__name__ = "Integer32"
_CcDetailsIndex_Object = MibTableColumn
ccDetailsIndex = _CcDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 1),
    _CcDetailsIndex_Type()
)
ccDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsIndex.setStatus("current")


class _CcDetailsName_Type(DisplayStringUnsized):
    """Custom type ccDetailsName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CcDetailsName_Type.__name__ = "DisplayStringUnsized"
_CcDetailsName_Object = MibTableColumn
ccDetailsName = _CcDetailsName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 2),
    _CcDetailsName_Type()
)
ccDetailsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsName.setStatus("current")


class _CcDetailsRemoteName_Type(DisplayStringUnsized):
    """Custom type ccDetailsRemoteName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CcDetailsRemoteName_Type.__name__ = "DisplayStringUnsized"
_CcDetailsRemoteName_Object = MibTableColumn
ccDetailsRemoteName = _CcDetailsRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 3),
    _CcDetailsRemoteName_Type()
)
ccDetailsRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRemoteName.setStatus("current")


class _CcDetailsCalledNumber_Type(DisplayStringUnsized):
    """Custom type ccDetailsCalledNumber based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsCalledNumber_Type.__name__ = "DisplayStringUnsized"
_CcDetailsCalledNumber_Object = MibTableColumn
ccDetailsCalledNumber = _CcDetailsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 4),
    _CcDetailsCalledNumber_Type()
)
ccDetailsCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCalledNumber.setStatus("current")


class _CcDetailsCallingNumber_Type(DisplayStringUnsized):
    """Custom type ccDetailsCallingNumber based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsCallingNumber_Type.__name__ = "DisplayStringUnsized"
_CcDetailsCallingNumber_Object = MibTableColumn
ccDetailsCallingNumber = _CcDetailsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 5),
    _CcDetailsCallingNumber_Type()
)
ccDetailsCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallingNumber.setStatus("current")


class _CcDetailsAlternateNumber_Type(DisplayStringUnsized):
    """Custom type ccDetailsAlternateNumber based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsAlternateNumber_Type.__name__ = "DisplayStringUnsized"
_CcDetailsAlternateNumber_Object = MibTableColumn
ccDetailsAlternateNumber = _CcDetailsAlternateNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 6),
    _CcDetailsAlternateNumber_Type()
)
ccDetailsAlternateNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsAlternateNumber.setStatus("current")


class _CcDetailsEnabled_Type(Integer32):
    """Custom type ccDetailsEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CcDetailsEnabled_Type.__name__ = "Integer32"
_CcDetailsEnabled_Object = MibTableColumn
ccDetailsEnabled = _CcDetailsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 7),
    _CcDetailsEnabled_Type()
)
ccDetailsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsEnabled.setStatus("current")


class _CcDetailsDirection_Type(Integer32):
    """Custom type ccDetailsDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inOnly", 1),
          ("outOnly", 2))
    )


_CcDetailsDirection_Type.__name__ = "Integer32"
_CcDetailsDirection_Object = MibTableColumn
ccDetailsDirection = _CcDetailsDirection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 8),
    _CcDetailsDirection_Type()
)
ccDetailsDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsDirection.setStatus("current")


class _CcDetailsPrecedence_Type(Integer32):
    """Custom type ccDetailsPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_CcDetailsPrecedence_Type.__name__ = "Integer32"
_CcDetailsPrecedence_Object = MibTableColumn
ccDetailsPrecedence = _CcDetailsPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 9),
    _CcDetailsPrecedence_Type()
)
ccDetailsPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPrecedence.setStatus("current")


class _CcDetailsHoldupTime_Type(Integer32):
    """Custom type ccDetailsHoldupTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_CcDetailsHoldupTime_Type.__name__ = "Integer32"
_CcDetailsHoldupTime_Object = MibTableColumn
ccDetailsHoldupTime = _CcDetailsHoldupTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 10),
    _CcDetailsHoldupTime_Type()
)
ccDetailsHoldupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsHoldupTime.setStatus("current")


class _CcDetailsPreferredIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ccDetailsPreferredIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CcDetailsPreferredIfIndex_Object = MibTableColumn
ccDetailsPreferredIfIndex = _CcDetailsPreferredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 11),
    _CcDetailsPreferredIfIndex_Type()
)
ccDetailsPreferredIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPreferredIfIndex.setStatus("current")


class _CcDetailsRequiredIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ccDetailsRequiredIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CcDetailsRequiredIfIndex_Object = MibTableColumn
ccDetailsRequiredIfIndex = _CcDetailsRequiredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 12),
    _CcDetailsRequiredIfIndex_Type()
)
ccDetailsRequiredIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRequiredIfIndex.setStatus("current")


class _CcDetailsPriority_Type(Integer32):
    """Custom type ccDetailsPriority based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CcDetailsPriority_Type.__name__ = "Integer32"
_CcDetailsPriority_Object = MibTableColumn
ccDetailsPriority = _CcDetailsPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 13),
    _CcDetailsPriority_Type()
)
ccDetailsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPriority.setStatus("current")


class _CcDetailsRetryT1_Type(Integer32):
    """Custom type ccDetailsRetryT1 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_CcDetailsRetryT1_Type.__name__ = "Integer32"
_CcDetailsRetryT1_Object = MibTableColumn
ccDetailsRetryT1 = _CcDetailsRetryT1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 14),
    _CcDetailsRetryT1_Type()
)
ccDetailsRetryT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryT1.setStatus("current")


class _CcDetailsRetryN1_Type(Integer32):
    """Custom type ccDetailsRetryN1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcDetailsRetryN1_Type.__name__ = "Integer32"
_CcDetailsRetryN1_Object = MibTableColumn
ccDetailsRetryN1 = _CcDetailsRetryN1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 15),
    _CcDetailsRetryN1_Type()
)
ccDetailsRetryN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryN1.setStatus("current")


class _CcDetailsRetryT2_Type(Integer32):
    """Custom type ccDetailsRetryT2 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1200),
    )


_CcDetailsRetryT2_Type.__name__ = "Integer32"
_CcDetailsRetryT2_Object = MibTableColumn
ccDetailsRetryT2 = _CcDetailsRetryT2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 16),
    _CcDetailsRetryT2_Type()
)
ccDetailsRetryT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryT2.setStatus("current")


class _CcDetailsRetryN2_Type(Integer32):
    """Custom type ccDetailsRetryN2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CcDetailsRetryN2_Type.__name__ = "Integer32"
_CcDetailsRetryN2_Object = MibTableColumn
ccDetailsRetryN2 = _CcDetailsRetryN2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 17),
    _CcDetailsRetryN2_Type()
)
ccDetailsRetryN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryN2.setStatus("current")


class _CcDetailsKeepup_Type(Integer32):
    """Custom type ccDetailsKeepup based on Integer32"""
    defaultValue = 1

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


_CcDetailsKeepup_Type.__name__ = "Integer32"
_CcDetailsKeepup_Object = MibTableColumn
ccDetailsKeepup = _CcDetailsKeepup_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 18),
    _CcDetailsKeepup_Type()
)
ccDetailsKeepup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsKeepup.setStatus("current")


class _CcDetailsOutSetupCli_Type(Integer32):
    """Custom type ccDetailsOutSetupCli based on Integer32"""
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
        *(("calling", 2),
          ("interface", 3),
          ("nonumber", 4),
          ("off", 1))
    )


_CcDetailsOutSetupCli_Type.__name__ = "Integer32"
_CcDetailsOutSetupCli_Object = MibTableColumn
ccDetailsOutSetupCli = _CcDetailsOutSetupCli_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 19),
    _CcDetailsOutSetupCli_Type()
)
ccDetailsOutSetupCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupCli.setStatus("current")


class _CcDetailsOutSetupUser_Type(Integer32):
    """Custom type ccDetailsOutSetupUser based on Integer32"""
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
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsOutSetupUser_Type.__name__ = "Integer32"
_CcDetailsOutSetupUser_Object = MibTableColumn
ccDetailsOutSetupUser = _CcDetailsOutSetupUser_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 20),
    _CcDetailsOutSetupUser_Type()
)
ccDetailsOutSetupUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupUser.setStatus("current")


class _CcDetailsOutSetupCalledSub_Type(Integer32):
    """Custom type ccDetailsOutSetupCalledSub based on Integer32"""
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
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsOutSetupCalledSub_Type.__name__ = "Integer32"
_CcDetailsOutSetupCalledSub_Object = MibTableColumn
ccDetailsOutSetupCalledSub = _CcDetailsOutSetupCalledSub_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 21),
    _CcDetailsOutSetupCalledSub_Type()
)
ccDetailsOutSetupCalledSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupCalledSub.setStatus("current")


class _CcDetailsOutSubaddress_Type(DisplayStringUnsized):
    """Custom type ccDetailsOutSubaddress based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsOutSubaddress_Type.__name__ = "DisplayStringUnsized"
_CcDetailsOutSubaddress_Object = MibTableColumn
ccDetailsOutSubaddress = _CcDetailsOutSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 22),
    _CcDetailsOutSubaddress_Type()
)
ccDetailsOutSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSubaddress.setStatus("current")


class _CcDetailsCallback_Type(Integer32):
    """Custom type ccDetailsCallback based on Integer32"""
    defaultValue = 1

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


_CcDetailsCallback_Type.__name__ = "Integer32"
_CcDetailsCallback_Object = MibTableColumn
ccDetailsCallback = _CcDetailsCallback_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 23),
    _CcDetailsCallback_Type()
)
ccDetailsCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallback.setStatus("current")


class _CcDetailsCallbackDelay_Type(Integer32):
    """Custom type ccDetailsCallbackDelay based on Integer32"""
    defaultValue = 41

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsCallbackDelay_Type.__name__ = "Integer32"
_CcDetailsCallbackDelay_Object = MibTableColumn
ccDetailsCallbackDelay = _CcDetailsCallbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 24),
    _CcDetailsCallbackDelay_Type()
)
ccDetailsCallbackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallbackDelay.setStatus("current")


class _CcDetailsInSetupCalledSubSearch_Type(Integer32):
    """Custom type ccDetailsInSetupCalledSubSearch based on Integer32"""
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
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupCalledSubSearch_Type.__name__ = "Integer32"
_CcDetailsInSetupCalledSubSearch_Object = MibTableColumn
ccDetailsInSetupCalledSubSearch = _CcDetailsInSetupCalledSubSearch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 25),
    _CcDetailsInSetupCalledSubSearch_Type()
)
ccDetailsInSetupCalledSubSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCalledSubSearch.setStatus("current")


class _CcDetailsInSetupUserSearch_Type(Integer32):
    """Custom type ccDetailsInSetupUserSearch based on Integer32"""
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
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupUserSearch_Type.__name__ = "Integer32"
_CcDetailsInSetupUserSearch_Object = MibTableColumn
ccDetailsInSetupUserSearch = _CcDetailsInSetupUserSearch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 26),
    _CcDetailsInSetupUserSearch_Type()
)
ccDetailsInSetupUserSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupUserSearch.setStatus("current")


class _CcDetailsInSetupCliSearch_Type(Integer32):
    """Custom type ccDetailsInSetupCliSearch based on Integer32"""
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
        *(("list", 3),
          ("off", 1),
          ("on", 2))
    )


_CcDetailsInSetupCliSearch_Type.__name__ = "Integer32"
_CcDetailsInSetupCliSearch_Object = MibTableColumn
ccDetailsInSetupCliSearch = _CcDetailsInSetupCliSearch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 27),
    _CcDetailsInSetupCliSearch_Type()
)
ccDetailsInSetupCliSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliSearch.setStatus("current")


class _CcDetailsInSetupCliSearchList_Type(Integer32):
    """Custom type ccDetailsInSetupCliSearchList based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsInSetupCliSearchList_Type.__name__ = "Integer32"
_CcDetailsInSetupCliSearchList_Object = MibTableColumn
ccDetailsInSetupCliSearchList = _CcDetailsInSetupCliSearchList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 28),
    _CcDetailsInSetupCliSearchList_Type()
)
ccDetailsInSetupCliSearchList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliSearchList.setStatus("current")


class _CcDetailsInAnyFlag_Type(Integer32):
    """Custom type ccDetailsInAnyFlag based on Integer32"""
    defaultValue = 1

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


_CcDetailsInAnyFlag_Type.__name__ = "Integer32"
_CcDetailsInAnyFlag_Object = MibTableColumn
ccDetailsInAnyFlag = _CcDetailsInAnyFlag_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 29),
    _CcDetailsInAnyFlag_Type()
)
ccDetailsInAnyFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInAnyFlag.setStatus("current")


class _CcDetailsInSetupCalledSubCheck_Type(Integer32):
    """Custom type ccDetailsInSetupCalledSubCheck based on Integer32"""
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
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupCalledSubCheck_Type.__name__ = "Integer32"
_CcDetailsInSetupCalledSubCheck_Object = MibTableColumn
ccDetailsInSetupCalledSubCheck = _CcDetailsInSetupCalledSubCheck_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 30),
    _CcDetailsInSetupCalledSubCheck_Type()
)
ccDetailsInSetupCalledSubCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCalledSubCheck.setStatus("current")


class _CcDetailsInSetupUserCheck_Type(Integer32):
    """Custom type ccDetailsInSetupUserCheck based on Integer32"""
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
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupUserCheck_Type.__name__ = "Integer32"
_CcDetailsInSetupUserCheck_Object = MibTableColumn
ccDetailsInSetupUserCheck = _CcDetailsInSetupUserCheck_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 31),
    _CcDetailsInSetupUserCheck_Type()
)
ccDetailsInSetupUserCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupUserCheck.setStatus("current")


class _CcDetailsInSetupCliCheck_Type(Integer32):
    """Custom type ccDetailsInSetupCliCheck based on Integer32"""
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
        *(("off", 1),
          ("present", 2),
          ("required", 3))
    )


_CcDetailsInSetupCliCheck_Type.__name__ = "Integer32"
_CcDetailsInSetupCliCheck_Object = MibTableColumn
ccDetailsInSetupCliCheck = _CcDetailsInSetupCliCheck_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 32),
    _CcDetailsInSetupCliCheck_Type()
)
ccDetailsInSetupCliCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliCheck.setStatus("current")


class _CcDetailsInSetupCliCheckList_Type(Integer32):
    """Custom type ccDetailsInSetupCliCheckList based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsInSetupCliCheckList_Type.__name__ = "Integer32"
_CcDetailsInSetupCliCheckList_Object = MibTableColumn
ccDetailsInSetupCliCheckList = _CcDetailsInSetupCliCheckList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 33),
    _CcDetailsInSetupCliCheckList_Type()
)
ccDetailsInSetupCliCheckList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliCheckList.setStatus("current")


class _CcDetailsUserType_Type(Integer32):
    """Custom type ccDetailsUserType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attach", 1),
          ("ppp", 2))
    )


_CcDetailsUserType_Type.__name__ = "Integer32"
_CcDetailsUserType_Object = MibTableColumn
ccDetailsUserType = _CcDetailsUserType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 34),
    _CcDetailsUserType_Type()
)
ccDetailsUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsUserType.setStatus("current")


class _CcDetailsLoginType_Type(Integer32):
    """Custom type ccDetailsLoginType based on Integer32"""
    defaultValue = 1

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
        *(("all", 8),
          ("chap", 5),
          ("none", 1),
          ("papRadius", 6),
          ("papTacacs", 4),
          ("radius", 3),
          ("tacacs", 7),
          ("userdb", 2))
    )


_CcDetailsLoginType_Type.__name__ = "Integer32"
_CcDetailsLoginType_Object = MibTableColumn
ccDetailsLoginType = _CcDetailsLoginType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 35),
    _CcDetailsLoginType_Type()
)
ccDetailsLoginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsLoginType.setStatus("current")


class _CcDetailsUsername_Type(Integer32):
    """Custom type ccDetailsUsername based on Integer32"""
    defaultValue = 1

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
        *(("calledsub", 3),
          ("callname", 5),
          ("cli", 2),
          ("none", 1),
          ("useruser", 4))
    )


_CcDetailsUsername_Type.__name__ = "Integer32"
_CcDetailsUsername_Object = MibTableColumn
ccDetailsUsername = _CcDetailsUsername_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 36),
    _CcDetailsUsername_Type()
)
ccDetailsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsUsername.setStatus("current")


class _CcDetailsPassword_Type(Integer32):
    """Custom type ccDetailsPassword based on Integer32"""
    defaultValue = 1

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
        *(("calledsub", 3),
          ("callname", 5),
          ("cli", 2),
          ("none", 1),
          ("useruser", 4))
    )


_CcDetailsPassword_Type.__name__ = "Integer32"
_CcDetailsPassword_Object = MibTableColumn
ccDetailsPassword = _CcDetailsPassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 37),
    _CcDetailsPassword_Type()
)
ccDetailsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPassword.setStatus("current")


class _CcDetailsBumpDelay_Type(Integer32):
    """Custom type ccDetailsBumpDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsBumpDelay_Type.__name__ = "Integer32"
_CcDetailsBumpDelay_Object = MibTableColumn
ccDetailsBumpDelay = _CcDetailsBumpDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 38),
    _CcDetailsBumpDelay_Type()
)
ccDetailsBumpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsBumpDelay.setStatus("current")


class _CcDetailsDataRate_Type(Integer32):
    """Custom type ccDetailsDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 2),
          ("rate-64k", 1))
    )


_CcDetailsDataRate_Type.__name__ = "Integer32"
_CcDetailsDataRate_Object = MibTableColumn
ccDetailsDataRate = _CcDetailsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 39),
    _CcDetailsDataRate_Type()
)
ccDetailsDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsDataRate.setStatus("current")


class _CcDetailsPppTemplate_Type(Integer32):
    """Custom type ccDetailsPppTemplate based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_CcDetailsPppTemplate_Type.__name__ = "Integer32"
_CcDetailsPppTemplate_Object = MibTableColumn
ccDetailsPppTemplate = _CcDetailsPppTemplate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 40),
    _CcDetailsPppTemplate_Type()
)
ccDetailsPppTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPppTemplate.setStatus("current")
_CcDetailsUserModule_Type = Integer32
_CcDetailsUserModule_Object = MibTableColumn
ccDetailsUserModule = _CcDetailsUserModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 41),
    _CcDetailsUserModule_Type()
)
ccDetailsUserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsUserModule.setStatus("current")
_CcDetailsNumberAttachments_Type = Integer32
_CcDetailsNumberAttachments_Object = MibTableColumn
ccDetailsNumberAttachments = _CcDetailsNumberAttachments_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 42),
    _CcDetailsNumberAttachments_Type()
)
ccDetailsNumberAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsNumberAttachments.setStatus("current")
_CcCliListTable_Object = MibTable
ccCliListTable = _CcCliListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2)
)
if mibBuilder.loadTexts:
    ccCliListTable.setStatus("current")
_CcCliListEntry_Object = MibTableRow
ccCliListEntry = _CcCliListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1)
)
ccCliListEntry.setIndexNames(
    (0, "AT-ISDN-MIB", "ccCliListListIndex"),
    (0, "AT-ISDN-MIB", "ccCliListEntryIndex"),
)
if mibBuilder.loadTexts:
    ccCliListEntry.setStatus("current")


class _CcCliListListIndex_Type(Integer32):
    """Custom type ccCliListListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCliListListIndex_Type.__name__ = "Integer32"
_CcCliListListIndex_Object = MibTableColumn
ccCliListListIndex = _CcCliListListIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1, 1),
    _CcCliListListIndex_Type()
)
ccCliListListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCliListListIndex.setStatus("current")
_CcCliListEntryIndex_Type = Integer32
_CcCliListEntryIndex_Object = MibTableColumn
ccCliListEntryIndex = _CcCliListEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1, 2),
    _CcCliListEntryIndex_Type()
)
ccCliListEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCliListEntryIndex.setStatus("current")


class _CcCliListNumber_Type(DisplayStringUnsized):
    """Custom type ccCliListNumber based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcCliListNumber_Type.__name__ = "DisplayStringUnsized"
_CcCliListNumber_Object = MibTableColumn
ccCliListNumber = _CcCliListNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1, 3),
    _CcCliListNumber_Type()
)
ccCliListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCliListNumber.setStatus("current")
_CcActiveCallTable_Object = MibTable
ccActiveCallTable = _CcActiveCallTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3)
)
if mibBuilder.loadTexts:
    ccActiveCallTable.setStatus("current")
_CcActiveCallEntry_Object = MibTableRow
ccActiveCallEntry = _CcActiveCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1)
)
ccActiveCallEntry.setIndexNames(
    (0, "AT-ISDN-MIB", "ccActiveCallIndex"),
)
if mibBuilder.loadTexts:
    ccActiveCallEntry.setStatus("current")


class _CcActiveCallIndex_Type(Integer32):
    """Custom type ccActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcActiveCallIndex_Type.__name__ = "Integer32"
_CcActiveCallIndex_Object = MibTableColumn
ccActiveCallIndex = _CcActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 1),
    _CcActiveCallIndex_Type()
)
ccActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallIndex.setStatus("current")


class _CcActiveCallDetailsIndex_Type(Integer32):
    """Custom type ccActiveCallDetailsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcActiveCallDetailsIndex_Type.__name__ = "Integer32"
_CcActiveCallDetailsIndex_Object = MibTableColumn
ccActiveCallDetailsIndex = _CcActiveCallDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 2),
    _CcActiveCallDetailsIndex_Type()
)
ccActiveCallDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDetailsIndex.setStatus("current")
_CcActiveCallIfIndex_Type = InterfaceIndexOrZero
_CcActiveCallIfIndex_Object = MibTableColumn
ccActiveCallIfIndex = _CcActiveCallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 3),
    _CcActiveCallIfIndex_Type()
)
ccActiveCallIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallIfIndex.setStatus("current")


class _CcActiveCallDataRate_Type(Integer32):
    """Custom type ccActiveCallDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 2),
          ("rate-64k", 1))
    )


_CcActiveCallDataRate_Type.__name__ = "Integer32"
_CcActiveCallDataRate_Object = MibTableColumn
ccActiveCallDataRate = _CcActiveCallDataRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 4),
    _CcActiveCallDataRate_Type()
)
ccActiveCallDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDataRate.setStatus("current")


class _CcActiveCallState_Type(Integer32):
    """Custom type ccActiveCallState based on Integer32"""
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
        *(("await1", 6),
          ("null", 1),
          ("off", 2),
          ("on", 4),
          ("try", 3),
          ("wait", 5))
    )


_CcActiveCallState_Type.__name__ = "Integer32"
_CcActiveCallState_Object = MibTableColumn
ccActiveCallState = _CcActiveCallState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 5),
    _CcActiveCallState_Type()
)
ccActiveCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallState.setStatus("current")


class _CcActiveCallDirection_Type(Integer32):
    """Custom type ccActiveCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("undefined", 3))
    )


_CcActiveCallDirection_Type.__name__ = "Integer32"
_CcActiveCallDirection_Object = MibTableColumn
ccActiveCallDirection = _CcActiveCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 6),
    _CcActiveCallDirection_Type()
)
ccActiveCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDirection.setStatus("current")
_CcActiveCallUserModule_Type = Integer32
_CcActiveCallUserModule_Object = MibTableColumn
ccActiveCallUserModule = _CcActiveCallUserModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 7),
    _CcActiveCallUserModule_Type()
)
ccActiveCallUserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallUserModule.setStatus("current")
_CcActiveCallUserInstance_Type = Integer32
_CcActiveCallUserInstance_Object = MibTableColumn
ccActiveCallUserInstance = _CcActiveCallUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 8),
    _CcActiveCallUserInstance_Type()
)
ccActiveCallUserInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallUserInstance.setStatus("current")


class _CcActiveCallBchannelIndex_Type(Integer32):
    """Custom type ccActiveCallBchannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CcActiveCallBchannelIndex_Type.__name__ = "Integer32"
_CcActiveCallBchannelIndex_Object = MibTableColumn
ccActiveCallBchannelIndex = _CcActiveCallBchannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 9),
    _CcActiveCallBchannelIndex_Type()
)
ccActiveCallBchannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallBchannelIndex.setStatus("current")
_CcCallLogTable_Object = MibTable
ccCallLogTable = _CcCallLogTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4)
)
if mibBuilder.loadTexts:
    ccCallLogTable.setStatus("current")
_CcCallLogEntry_Object = MibTableRow
ccCallLogEntry = _CcCallLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1)
)
ccCallLogEntry.setIndexNames(
    (0, "AT-ISDN-MIB", "ccCallLogIndex"),
)
if mibBuilder.loadTexts:
    ccCallLogEntry.setStatus("current")
_CcCallLogIndex_Type = Integer32
_CcCallLogIndex_Object = MibTableColumn
ccCallLogIndex = _CcCallLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 1),
    _CcCallLogIndex_Type()
)
ccCallLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogIndex.setStatus("current")
_CcCallLogName_Type = DisplayString
_CcCallLogName_Object = MibTableColumn
ccCallLogName = _CcCallLogName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 2),
    _CcCallLogName_Type()
)
ccCallLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogName.setStatus("current")


class _CcCallLogState_Type(Integer32):
    """Custom type ccCallLogState based on Integer32"""
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
        *(("active", 2),
          ("cleared", 4),
          ("disconnected", 3),
          ("initial", 1))
    )


_CcCallLogState_Type.__name__ = "Integer32"
_CcCallLogState_Object = MibTableColumn
ccCallLogState = _CcCallLogState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 3),
    _CcCallLogState_Type()
)
ccCallLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogState.setStatus("current")
_CcCallLogTimeStarted_Type = DisplayString
_CcCallLogTimeStarted_Object = MibTableColumn
ccCallLogTimeStarted = _CcCallLogTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 4),
    _CcCallLogTimeStarted_Type()
)
ccCallLogTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogTimeStarted.setStatus("current")


class _CcCallLogDirection_Type(Integer32):
    """Custom type ccCallLogDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_CcCallLogDirection_Type.__name__ = "Integer32"
_CcCallLogDirection_Object = MibTableColumn
ccCallLogDirection = _CcCallLogDirection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 5),
    _CcCallLogDirection_Type()
)
ccCallLogDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogDirection.setStatus("current")
_CcCallLogDuration_Type = Integer32
_CcCallLogDuration_Object = MibTableColumn
ccCallLogDuration = _CcCallLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 6),
    _CcCallLogDuration_Type()
)
ccCallLogDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogDuration.setStatus("current")
_CcCallLogRemoteNumber_Type = DisplayString
_CcCallLogRemoteNumber_Object = MibTableColumn
ccCallLogRemoteNumber = _CcCallLogRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 7),
    _CcCallLogRemoteNumber_Type()
)
ccCallLogRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogRemoteNumber.setStatus("current")
_CcAttachmentTable_Object = MibTable
ccAttachmentTable = _CcAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5)
)
if mibBuilder.loadTexts:
    ccAttachmentTable.setStatus("current")
_CcAttachmentEntry_Object = MibTableRow
ccAttachmentEntry = _CcAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1)
)
ccAttachmentEntry.setIndexNames(
    (0, "AT-ISDN-MIB", "ccAttachmentDetailsIndex"),
    (0, "AT-ISDN-MIB", "ccAttachmentEntryIndex"),
)
if mibBuilder.loadTexts:
    ccAttachmentEntry.setStatus("current")


class _CcAttachmentDetailsIndex_Type(Integer32):
    """Custom type ccAttachmentDetailsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcAttachmentDetailsIndex_Type.__name__ = "Integer32"
_CcAttachmentDetailsIndex_Object = MibTableColumn
ccAttachmentDetailsIndex = _CcAttachmentDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 1),
    _CcAttachmentDetailsIndex_Type()
)
ccAttachmentDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentDetailsIndex.setStatus("current")
_CcAttachmentEntryIndex_Type = Integer32
_CcAttachmentEntryIndex_Object = MibTableColumn
ccAttachmentEntryIndex = _CcAttachmentEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 2),
    _CcAttachmentEntryIndex_Type()
)
ccAttachmentEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentEntryIndex.setStatus("current")


class _CcAttachmentActiveCallIndex_Type(Integer32):
    """Custom type ccAttachmentActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CcAttachmentActiveCallIndex_Type.__name__ = "Integer32"
_CcAttachmentActiveCallIndex_Object = MibTableColumn
ccAttachmentActiveCallIndex = _CcAttachmentActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 3),
    _CcAttachmentActiveCallIndex_Type()
)
ccAttachmentActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentActiveCallIndex.setStatus("current")
_CcAttachmentUserInstance_Type = Integer32
_CcAttachmentUserInstance_Object = MibTableColumn
ccAttachmentUserInstance = _CcAttachmentUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 4),
    _CcAttachmentUserInstance_Type()
)
ccAttachmentUserInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentUserInstance.setStatus("current")
_CcBchannelTable_Object = MibTable
ccBchannelTable = _CcBchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6)
)
if mibBuilder.loadTexts:
    ccBchannelTable.setStatus("current")
_CcBchannelEntry_Object = MibTableRow
ccBchannelEntry = _CcBchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1)
)
ccBchannelEntry.setIndexNames(
    (0, "AT-ISDN-MIB", "ccBchannelIfIndex"),
    (0, "AT-ISDN-MIB", "ccBchannelChannelIndex"),
)
if mibBuilder.loadTexts:
    ccBchannelEntry.setStatus("current")
_CcBchannelIfIndex_Type = Integer32
_CcBchannelIfIndex_Object = MibTableColumn
ccBchannelIfIndex = _CcBchannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 1),
    _CcBchannelIfIndex_Type()
)
ccBchannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelIfIndex.setStatus("current")


class _CcBchannelChannelIndex_Type(Integer32):
    """Custom type ccBchannelChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcBchannelChannelIndex_Type.__name__ = "Integer32"
_CcBchannelChannelIndex_Object = MibTableColumn
ccBchannelChannelIndex = _CcBchannelChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 2),
    _CcBchannelChannelIndex_Type()
)
ccBchannelChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelChannelIndex.setStatus("current")


class _CcBchannelAllocated_Type(Integer32):
    """Custom type ccBchannelAllocated based on Integer32"""
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


_CcBchannelAllocated_Type.__name__ = "Integer32"
_CcBchannelAllocated_Object = MibTableColumn
ccBchannelAllocated = _CcBchannelAllocated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 3),
    _CcBchannelAllocated_Type()
)
ccBchannelAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelAllocated.setStatus("current")


class _CcBchannelCallType_Type(Integer32):
    """Custom type ccBchannelCallType based on Integer32"""
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
        *(("data", 2),
          ("undefined", 1),
          ("voice", 3),
          ("x25", 4))
    )


_CcBchannelCallType_Type.__name__ = "Integer32"
_CcBchannelCallType_Object = MibTableColumn
ccBchannelCallType = _CcBchannelCallType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 4),
    _CcBchannelCallType_Type()
)
ccBchannelCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelCallType.setStatus("current")


class _CcBchannelActiveCallIndex_Type(Integer32):
    """Custom type ccBchannelActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CcBchannelActiveCallIndex_Type.__name__ = "Integer32"
_CcBchannelActiveCallIndex_Object = MibTableColumn
ccBchannelActiveCallIndex = _CcBchannelActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 5),
    _CcBchannelActiveCallIndex_Type()
)
ccBchannelActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelActiveCallIndex.setStatus("current")
_CcBchannelPriority_Type = Integer32
_CcBchannelPriority_Object = MibTableColumn
ccBchannelPriority = _CcBchannelPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 6),
    _CcBchannelPriority_Type()
)
ccBchannelPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelPriority.setStatus("current")


class _CcBchannelDirection_Type(Integer32):
    """Custom type ccBchannelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("unallocated", 3))
    )


_CcBchannelDirection_Type.__name__ = "Integer32"
_CcBchannelDirection_Object = MibTableColumn
ccBchannelDirection = _CcBchannelDirection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 7),
    _CcBchannelDirection_Type()
)
ccBchannelDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelDirection.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ISDN-MIB",
    **{"cc": cc,
       "ccDetailsTable": ccDetailsTable,
       "ccDetailsEntry": ccDetailsEntry,
       "ccDetailsIndex": ccDetailsIndex,
       "ccDetailsName": ccDetailsName,
       "ccDetailsRemoteName": ccDetailsRemoteName,
       "ccDetailsCalledNumber": ccDetailsCalledNumber,
       "ccDetailsCallingNumber": ccDetailsCallingNumber,
       "ccDetailsAlternateNumber": ccDetailsAlternateNumber,
       "ccDetailsEnabled": ccDetailsEnabled,
       "ccDetailsDirection": ccDetailsDirection,
       "ccDetailsPrecedence": ccDetailsPrecedence,
       "ccDetailsHoldupTime": ccDetailsHoldupTime,
       "ccDetailsPreferredIfIndex": ccDetailsPreferredIfIndex,
       "ccDetailsRequiredIfIndex": ccDetailsRequiredIfIndex,
       "ccDetailsPriority": ccDetailsPriority,
       "ccDetailsRetryT1": ccDetailsRetryT1,
       "ccDetailsRetryN1": ccDetailsRetryN1,
       "ccDetailsRetryT2": ccDetailsRetryT2,
       "ccDetailsRetryN2": ccDetailsRetryN2,
       "ccDetailsKeepup": ccDetailsKeepup,
       "ccDetailsOutSetupCli": ccDetailsOutSetupCli,
       "ccDetailsOutSetupUser": ccDetailsOutSetupUser,
       "ccDetailsOutSetupCalledSub": ccDetailsOutSetupCalledSub,
       "ccDetailsOutSubaddress": ccDetailsOutSubaddress,
       "ccDetailsCallback": ccDetailsCallback,
       "ccDetailsCallbackDelay": ccDetailsCallbackDelay,
       "ccDetailsInSetupCalledSubSearch": ccDetailsInSetupCalledSubSearch,
       "ccDetailsInSetupUserSearch": ccDetailsInSetupUserSearch,
       "ccDetailsInSetupCliSearch": ccDetailsInSetupCliSearch,
       "ccDetailsInSetupCliSearchList": ccDetailsInSetupCliSearchList,
       "ccDetailsInAnyFlag": ccDetailsInAnyFlag,
       "ccDetailsInSetupCalledSubCheck": ccDetailsInSetupCalledSubCheck,
       "ccDetailsInSetupUserCheck": ccDetailsInSetupUserCheck,
       "ccDetailsInSetupCliCheck": ccDetailsInSetupCliCheck,
       "ccDetailsInSetupCliCheckList": ccDetailsInSetupCliCheckList,
       "ccDetailsUserType": ccDetailsUserType,
       "ccDetailsLoginType": ccDetailsLoginType,
       "ccDetailsUsername": ccDetailsUsername,
       "ccDetailsPassword": ccDetailsPassword,
       "ccDetailsBumpDelay": ccDetailsBumpDelay,
       "ccDetailsDataRate": ccDetailsDataRate,
       "ccDetailsPppTemplate": ccDetailsPppTemplate,
       "ccDetailsUserModule": ccDetailsUserModule,
       "ccDetailsNumberAttachments": ccDetailsNumberAttachments,
       "ccCliListTable": ccCliListTable,
       "ccCliListEntry": ccCliListEntry,
       "ccCliListListIndex": ccCliListListIndex,
       "ccCliListEntryIndex": ccCliListEntryIndex,
       "ccCliListNumber": ccCliListNumber,
       "ccActiveCallTable": ccActiveCallTable,
       "ccActiveCallEntry": ccActiveCallEntry,
       "ccActiveCallIndex": ccActiveCallIndex,
       "ccActiveCallDetailsIndex": ccActiveCallDetailsIndex,
       "ccActiveCallIfIndex": ccActiveCallIfIndex,
       "ccActiveCallDataRate": ccActiveCallDataRate,
       "ccActiveCallState": ccActiveCallState,
       "ccActiveCallDirection": ccActiveCallDirection,
       "ccActiveCallUserModule": ccActiveCallUserModule,
       "ccActiveCallUserInstance": ccActiveCallUserInstance,
       "ccActiveCallBchannelIndex": ccActiveCallBchannelIndex,
       "ccCallLogTable": ccCallLogTable,
       "ccCallLogEntry": ccCallLogEntry,
       "ccCallLogIndex": ccCallLogIndex,
       "ccCallLogName": ccCallLogName,
       "ccCallLogState": ccCallLogState,
       "ccCallLogTimeStarted": ccCallLogTimeStarted,
       "ccCallLogDirection": ccCallLogDirection,
       "ccCallLogDuration": ccCallLogDuration,
       "ccCallLogRemoteNumber": ccCallLogRemoteNumber,
       "ccAttachmentTable": ccAttachmentTable,
       "ccAttachmentEntry": ccAttachmentEntry,
       "ccAttachmentDetailsIndex": ccAttachmentDetailsIndex,
       "ccAttachmentEntryIndex": ccAttachmentEntryIndex,
       "ccAttachmentActiveCallIndex": ccAttachmentActiveCallIndex,
       "ccAttachmentUserInstance": ccAttachmentUserInstance,
       "ccBchannelTable": ccBchannelTable,
       "ccBchannelEntry": ccBchannelEntry,
       "ccBchannelIfIndex": ccBchannelIfIndex,
       "ccBchannelChannelIndex": ccBchannelChannelIndex,
       "ccBchannelAllocated": ccBchannelAllocated,
       "ccBchannelCallType": ccBchannelCallType,
       "ccBchannelActiveCallIndex": ccBchannelActiveCallIndex,
       "ccBchannelPriority": ccBchannelPriority,
       "ccBchannelDirection": ccBchannelDirection}
)
