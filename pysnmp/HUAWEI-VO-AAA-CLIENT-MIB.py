# SNMP MIB module (HUAWEI-VO-AAA-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-AAA-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:26 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

hwVoiceAAAClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9)
)
hwVoiceAAAClientMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoAAAClientObjects_ObjectIdentity = ObjectIdentity
hwVoAAAClientObjects = _HwVoAAAClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1)
)
_HwVoAAAClientCfgObjects_ObjectIdentity = ObjectIdentity
hwVoAAAClientCfgObjects = _HwVoAAAClientCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1)
)


class _HwVoAAAEnable_Type(Integer32):
    """Custom type hwVoAAAEnable based on Integer32"""
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


_HwVoAAAEnable_Type.__name__ = "Integer32"
_HwVoAAAEnable_Object = MibScalar
hwVoAAAEnable = _HwVoAAAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1, 1),
    _HwVoAAAEnable_Type()
)
hwVoAAAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAEnable.setStatus("current")


class _HwVoAAAClienttype_Type(Integer32):
    """Custom type hwVoAAAClienttype based on Integer32"""
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
        *(("huawei", 1),
          ("ietf-rfc", 4),
          ("nonstandard-compatible-overload", 3),
          ("nonstandard-compatible-vsa", 2))
    )


_HwVoAAAClienttype_Type.__name__ = "Integer32"
_HwVoAAAClienttype_Object = MibScalar
hwVoAAAClienttype = _HwVoAAAClienttype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1, 2),
    _HwVoAAAClienttype_Type()
)
hwVoAAAClienttype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAClienttype.setStatus("current")


class _HwVoAAAGwAuthenDidH323_Type(Integer32):
    """Custom type hwVoAAAGwAuthenDidH323 based on Integer32"""
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


_HwVoAAAGwAuthenDidH323_Type.__name__ = "Integer32"
_HwVoAAAGwAuthenDidH323_Object = MibScalar
hwVoAAAGwAuthenDidH323 = _HwVoAAAGwAuthenDidH323_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1, 3),
    _HwVoAAAGwAuthenDidH323_Type()
)
hwVoAAAGwAuthenDidH323.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwAuthenDidH323.setStatus("current")


class _HwVoAAAGwAuthorDidH323_Type(Integer32):
    """Custom type hwVoAAAGwAuthorDidH323 based on Integer32"""
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


_HwVoAAAGwAuthorDidH323_Type.__name__ = "Integer32"
_HwVoAAAGwAuthorDidH323_Object = MibScalar
hwVoAAAGwAuthorDidH323 = _HwVoAAAGwAuthorDidH323_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1, 4),
    _HwVoAAAGwAuthorDidH323_Type()
)
hwVoAAAGwAuthorDidH323.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwAuthorDidH323.setStatus("current")


class _HwVoAAAGwAccounting_Type(Integer32):
    """Custom type hwVoAAAGwAccounting based on Integer32"""
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


_HwVoAAAGwAccounting_Type.__name__ = "Integer32"
_HwVoAAAGwAccounting_Object = MibScalar
hwVoAAAGwAccounting = _HwVoAAAGwAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1, 5),
    _HwVoAAAGwAccounting_Type()
)
hwVoAAAGwAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwAccounting.setStatus("current")


class _HwVoAAAGwAccountMethod_Type(Integer32):
    """Custom type hwVoAAAGwAccountMethod based on Integer32"""
    defaultValue = 3

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
        *(("none", 1),
          ("start-ack", 2),
          ("start-no-ack", 3),
          ("stop-only", 4))
    )


_HwVoAAAGwAccountMethod_Type.__name__ = "Integer32"
_HwVoAAAGwAccountMethod_Object = MibScalar
hwVoAAAGwAccountMethod = _HwVoAAAGwAccountMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 1, 6),
    _HwVoAAAGwAccountMethod_Type()
)
hwVoAAAGwAccountMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwAccountMethod.setStatus("current")
_HwVoAAAClientLocalUserTable_Object = MibTable
hwVoAAAClientLocalUserTable = _HwVoAAAClientLocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hwVoAAAClientLocalUserTable.setStatus("current")
_HwVoAAAClientLocalUserEntry_Object = MibTableRow
hwVoAAAClientLocalUserEntry = _HwVoAAAClientLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 2, 1)
)
hwVoAAAClientLocalUserEntry.setIndexNames(
    (0, "HUAWEI-VO-AAA-CLIENT-MIB", "hwVoAAAClientLocalUserName"),
)
if mibBuilder.loadTexts:
    hwVoAAAClientLocalUserEntry.setStatus("current")


class _HwVoAAAClientLocalUserName_Type(OctetString):
    """Custom type hwVoAAAClientLocalUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwVoAAAClientLocalUserName_Type.__name__ = "OctetString"
_HwVoAAAClientLocalUserName_Object = MibTableColumn
hwVoAAAClientLocalUserName = _HwVoAAAClientLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 2, 1, 1),
    _HwVoAAAClientLocalUserName_Type()
)
hwVoAAAClientLocalUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAAAClientLocalUserName.setStatus("current")


class _HwVoAAAClientLocalUserPassword_Type(OctetString):
    """Custom type hwVoAAAClientLocalUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwVoAAAClientLocalUserPassword_Type.__name__ = "OctetString"
_HwVoAAAClientLocalUserPassword_Object = MibTableColumn
hwVoAAAClientLocalUserPassword = _HwVoAAAClientLocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 2, 1, 2),
    _HwVoAAAClientLocalUserPassword_Type()
)
hwVoAAAClientLocalUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAClientLocalUserPassword.setStatus("current")
_HwVoAAAClientLocalRowStatus_Type = EntryStatus
_HwVoAAAClientLocalRowStatus_Object = MibTableColumn
hwVoAAAClientLocalRowStatus = _HwVoAAAClientLocalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 2, 1, 3),
    _HwVoAAAClientLocalRowStatus_Type()
)
hwVoAAAClientLocalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAClientLocalRowStatus.setStatus("current")
_HwVoAAAGwAccessNumberTable_Object = MibTable
hwVoAAAGwAccessNumberTable = _HwVoAAAGwAccessNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hwVoAAAGwAccessNumberTable.setStatus("current")
_HwVoAAAGwAccessNumberEntry_Object = MibTableRow
hwVoAAAGwAccessNumberEntry = _HwVoAAAGwAccessNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1)
)
hwVoAAAGwAccessNumberEntry.setIndexNames(
    (0, "HUAWEI-VO-AAA-CLIENT-MIB", "hwVoAAAGwAccessnumber"),
)
if mibBuilder.loadTexts:
    hwVoAAAGwAccessNumberEntry.setStatus("current")


class _HwVoAAAGwAccessnumber_Type(OctetString):
    """Custom type hwVoAAAGwAccessnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVoAAAGwAccessnumber_Type.__name__ = "OctetString"
_HwVoAAAGwAccessnumber_Object = MibTableColumn
hwVoAAAGwAccessnumber = _HwVoAAAGwAccessnumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 1),
    _HwVoAAAGwAccessnumber_Type()
)
hwVoAAAGwAccessnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAAAGwAccessnumber.setStatus("current")


class _HwVoAAAGwAuthentication_Type(Integer32):
    """Custom type hwVoAAAGwAuthentication based on Integer32"""
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


_HwVoAAAGwAuthentication_Type.__name__ = "Integer32"
_HwVoAAAGwAuthentication_Object = MibTableColumn
hwVoAAAGwAuthentication = _HwVoAAAGwAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 2),
    _HwVoAAAGwAuthentication_Type()
)
hwVoAAAGwAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwAuthentication.setStatus("current")


class _HwVoAAAGwAuthorization_Type(Integer32):
    """Custom type hwVoAAAGwAuthorization based on Integer32"""
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


_HwVoAAAGwAuthorization_Type.__name__ = "Integer32"
_HwVoAAAGwAuthorization_Object = MibTableColumn
hwVoAAAGwAuthorization = _HwVoAAAGwAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 3),
    _HwVoAAAGwAuthorization_Type()
)
hwVoAAAGwAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwAuthorization.setStatus("current")


class _HwVoAAAGwProcessConfig_Type(Integer32):
    """Custom type hwVoAAAGwProcessConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callernumber", 1),
          ("cardnumber", 2))
    )


_HwVoAAAGwProcessConfig_Type.__name__ = "Integer32"
_HwVoAAAGwProcessConfig_Object = MibTableColumn
hwVoAAAGwProcessConfig = _HwVoAAAGwProcessConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 4),
    _HwVoAAAGwProcessConfig_Type()
)
hwVoAAAGwProcessConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwProcessConfig.setStatus("current")


class _HwVoAAAGwCardDigit_Type(Integer32):
    """Custom type hwVoAAAGwCardDigit based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HwVoAAAGwCardDigit_Type.__name__ = "Integer32"
_HwVoAAAGwCardDigit_Object = MibTableColumn
hwVoAAAGwCardDigit = _HwVoAAAGwCardDigit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 5),
    _HwVoAAAGwCardDigit_Type()
)
hwVoAAAGwCardDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwCardDigit.setStatus("current")


class _HwVoAAAGwPasswordDigit_Type(Integer32):
    """Custom type hwVoAAAGwPasswordDigit based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwVoAAAGwPasswordDigit_Type.__name__ = "Integer32"
_HwVoAAAGwPasswordDigit_Object = MibTableColumn
hwVoAAAGwPasswordDigit = _HwVoAAAGwPasswordDigit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 6),
    _HwVoAAAGwPasswordDigit_Type()
)
hwVoAAAGwPasswordDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwPasswordDigit.setStatus("current")


class _HwVoAAAGwRedialtimes_Type(Integer32):
    """Custom type hwVoAAAGwRedialtimes based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwVoAAAGwRedialtimes_Type.__name__ = "Integer32"
_HwVoAAAGwRedialtimes_Object = MibTableColumn
hwVoAAAGwRedialtimes = _HwVoAAAGwRedialtimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 7),
    _HwVoAAAGwRedialtimes_Type()
)
hwVoAAAGwRedialtimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwRedialtimes.setStatus("current")
_HwVoAAAGwRowStatus_Type = EntryStatus
_HwVoAAAGwRowStatus_Object = MibTableColumn
hwVoAAAGwRowStatus = _HwVoAAAGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9, 1, 3, 1, 8),
    _HwVoAAAGwRowStatus_Type()
)
hwVoAAAGwRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAAAGwRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-AAA-CLIENT-MIB",
    **{"EntryStatus": EntryStatus,
       "hwVoiceAAAClientMIB": hwVoiceAAAClientMIB,
       "hwVoAAAClientObjects": hwVoAAAClientObjects,
       "hwVoAAAClientCfgObjects": hwVoAAAClientCfgObjects,
       "hwVoAAAEnable": hwVoAAAEnable,
       "hwVoAAAClienttype": hwVoAAAClienttype,
       "hwVoAAAGwAuthenDidH323": hwVoAAAGwAuthenDidH323,
       "hwVoAAAGwAuthorDidH323": hwVoAAAGwAuthorDidH323,
       "hwVoAAAGwAccounting": hwVoAAAGwAccounting,
       "hwVoAAAGwAccountMethod": hwVoAAAGwAccountMethod,
       "hwVoAAAClientLocalUserTable": hwVoAAAClientLocalUserTable,
       "hwVoAAAClientLocalUserEntry": hwVoAAAClientLocalUserEntry,
       "hwVoAAAClientLocalUserName": hwVoAAAClientLocalUserName,
       "hwVoAAAClientLocalUserPassword": hwVoAAAClientLocalUserPassword,
       "hwVoAAAClientLocalRowStatus": hwVoAAAClientLocalRowStatus,
       "hwVoAAAGwAccessNumberTable": hwVoAAAGwAccessNumberTable,
       "hwVoAAAGwAccessNumberEntry": hwVoAAAGwAccessNumberEntry,
       "hwVoAAAGwAccessnumber": hwVoAAAGwAccessnumber,
       "hwVoAAAGwAuthentication": hwVoAAAGwAuthentication,
       "hwVoAAAGwAuthorization": hwVoAAAGwAuthorization,
       "hwVoAAAGwProcessConfig": hwVoAAAGwProcessConfig,
       "hwVoAAAGwCardDigit": hwVoAAAGwCardDigit,
       "hwVoAAAGwPasswordDigit": hwVoAAAGwPasswordDigit,
       "hwVoAAAGwRedialtimes": hwVoAAAGwRedialtimes,
       "hwVoAAAGwRowStatus": hwVoAAAGwRowStatus}
)
