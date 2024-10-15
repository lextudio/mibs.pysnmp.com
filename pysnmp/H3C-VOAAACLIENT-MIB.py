# SNMP MIB module (H3C-VOAAACLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOAAACLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:40 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cVoiceAAAClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9)
)
h3cVoiceAAAClient.setRevisions(
        ("2006-03-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoAAAClientObjects_ObjectIdentity = ObjectIdentity
h3cVoAAAClientObjects = _H3cVoAAAClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1)
)
_H3cVoAAAClientCfgObjects_ObjectIdentity = ObjectIdentity
h3cVoAAAClientCfgObjects = _H3cVoAAAClientCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1)
)


class _H3cVoAAAGwAuthenDid_Type(TruthValue):
    """Custom type h3cVoAAAGwAuthenDid based on TruthValue"""


_H3cVoAAAGwAuthenDid_Object = MibScalar
h3cVoAAAGwAuthenDid = _H3cVoAAAGwAuthenDid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 1),
    _H3cVoAAAGwAuthenDid_Type()
)
h3cVoAAAGwAuthenDid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAAAGwAuthenDid.setStatus("current")


class _H3cVoAAAGwAuthorDid_Type(TruthValue):
    """Custom type h3cVoAAAGwAuthorDid based on TruthValue"""


_H3cVoAAAGwAuthorDid_Object = MibScalar
h3cVoAAAGwAuthorDid = _H3cVoAAAGwAuthorDid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 2),
    _H3cVoAAAGwAuthorDid_Type()
)
h3cVoAAAGwAuthorDid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAAAGwAuthorDid.setStatus("current")


class _H3cVoAAAGwAccountingDid_Type(TruthValue):
    """Custom type h3cVoAAAGwAccountingDid based on TruthValue"""


_H3cVoAAAGwAccountingDid_Object = MibScalar
h3cVoAAAGwAccountingDid = _H3cVoAAAGwAccountingDid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 3),
    _H3cVoAAAGwAccountingDid_Type()
)
h3cVoAAAGwAccountingDid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAAAGwAccountingDid.setStatus("current")


class _H3cVoAAAGwAccountMethod_Type(Integer32):
    """Custom type h3cVoAAAGwAccountMethod based on Integer32"""
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
        *(("startAck", 1),
          ("startNoAck", 2),
          ("stopOnly", 3))
    )


_H3cVoAAAGwAccountMethod_Type.__name__ = "Integer32"
_H3cVoAAAGwAccountMethod_Object = MibScalar
h3cVoAAAGwAccountMethod = _H3cVoAAAGwAccountMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 4),
    _H3cVoAAAGwAccountMethod_Type()
)
h3cVoAAAGwAccountMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAAAGwAccountMethod.setStatus("current")
_H3cVoAAAGwAccessNumberTable_Object = MibTable
h3cVoAAAGwAccessNumberTable = _H3cVoAAAGwAccessNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVoAAAGwAccessNumberTable.setStatus("current")
_H3cVoAAAGwAccessNumberEntry_Object = MibTableRow
h3cVoAAAGwAccessNumberEntry = _H3cVoAAAGwAccessNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1)
)
h3cVoAAAGwAccessNumberEntry.setIndexNames(
    (0, "H3C-VOAAACLIENT-MIB", "h3cVoAAAGwAccessNumber"),
)
if mibBuilder.loadTexts:
    h3cVoAAAGwAccessNumberEntry.setStatus("current")


class _H3cVoAAAGwAccessNumber_Type(OctetString):
    """Custom type h3cVoAAAGwAccessNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cVoAAAGwAccessNumber_Type.__name__ = "OctetString"
_H3cVoAAAGwAccessNumber_Object = MibTableColumn
h3cVoAAAGwAccessNumber = _H3cVoAAAGwAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 1),
    _H3cVoAAAGwAccessNumber_Type()
)
h3cVoAAAGwAccessNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoAAAGwAccessNumber.setStatus("current")


class _H3cVoAAAGwAuthentication_Type(TruthValue):
    """Custom type h3cVoAAAGwAuthentication based on TruthValue"""


_H3cVoAAAGwAuthentication_Object = MibTableColumn
h3cVoAAAGwAuthentication = _H3cVoAAAGwAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 2),
    _H3cVoAAAGwAuthentication_Type()
)
h3cVoAAAGwAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwAuthentication.setStatus("current")


class _H3cVoAAAGwAuthorization_Type(TruthValue):
    """Custom type h3cVoAAAGwAuthorization based on TruthValue"""


_H3cVoAAAGwAuthorization_Object = MibTableColumn
h3cVoAAAGwAuthorization = _H3cVoAAAGwAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 3),
    _H3cVoAAAGwAuthorization_Type()
)
h3cVoAAAGwAuthorization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwAuthorization.setStatus("current")


class _H3cVoAAAGwAccounting_Type(TruthValue):
    """Custom type h3cVoAAAGwAccounting based on TruthValue"""


_H3cVoAAAGwAccounting_Object = MibTableColumn
h3cVoAAAGwAccounting = _H3cVoAAAGwAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 4),
    _H3cVoAAAGwAccounting_Type()
)
h3cVoAAAGwAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwAccounting.setStatus("current")


class _H3cVoAAAGwProcessConfig_Type(Integer32):
    """Custom type h3cVoAAAGwProcessConfig based on Integer32"""
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
        *(("callerNumIvr", 3),
          ("callerNumber", 1),
          ("cardNumber", 2))
    )


_H3cVoAAAGwProcessConfig_Type.__name__ = "Integer32"
_H3cVoAAAGwProcessConfig_Object = MibTableColumn
h3cVoAAAGwProcessConfig = _H3cVoAAAGwProcessConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 5),
    _H3cVoAAAGwProcessConfig_Type()
)
h3cVoAAAGwProcessConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwProcessConfig.setStatus("current")


class _H3cVoAAAGwCardDigit_Type(Integer32):
    """Custom type h3cVoAAAGwCardDigit based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_H3cVoAAAGwCardDigit_Type.__name__ = "Integer32"
_H3cVoAAAGwCardDigit_Object = MibTableColumn
h3cVoAAAGwCardDigit = _H3cVoAAAGwCardDigit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 6),
    _H3cVoAAAGwCardDigit_Type()
)
h3cVoAAAGwCardDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwCardDigit.setStatus("current")


class _H3cVoAAAGwPasswordDigit_Type(Integer32):
    """Custom type h3cVoAAAGwPasswordDigit based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cVoAAAGwPasswordDigit_Type.__name__ = "Integer32"
_H3cVoAAAGwPasswordDigit_Object = MibTableColumn
h3cVoAAAGwPasswordDigit = _H3cVoAAAGwPasswordDigit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 7),
    _H3cVoAAAGwPasswordDigit_Type()
)
h3cVoAAAGwPasswordDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwPasswordDigit.setStatus("current")


class _H3cVoAAAGwRedialTimes_Type(Integer32):
    """Custom type h3cVoAAAGwRedialTimes based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_H3cVoAAAGwRedialTimes_Type.__name__ = "Integer32"
_H3cVoAAAGwRedialTimes_Object = MibTableColumn
h3cVoAAAGwRedialTimes = _H3cVoAAAGwRedialTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 8),
    _H3cVoAAAGwRedialTimes_Type()
)
h3cVoAAAGwRedialTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwRedialTimes.setStatus("current")
_H3cVoAAAGwRowStatus_Type = RowStatus
_H3cVoAAAGwRowStatus_Object = MibTableColumn
h3cVoAAAGwRowStatus = _H3cVoAAAGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 9),
    _H3cVoAAAGwRowStatus_Type()
)
h3cVoAAAGwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoAAAGwRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOAAACLIENT-MIB",
    **{"h3cVoiceAAAClient": h3cVoiceAAAClient,
       "h3cVoAAAClientObjects": h3cVoAAAClientObjects,
       "h3cVoAAAClientCfgObjects": h3cVoAAAClientCfgObjects,
       "h3cVoAAAGwAuthenDid": h3cVoAAAGwAuthenDid,
       "h3cVoAAAGwAuthorDid": h3cVoAAAGwAuthorDid,
       "h3cVoAAAGwAccountingDid": h3cVoAAAGwAccountingDid,
       "h3cVoAAAGwAccountMethod": h3cVoAAAGwAccountMethod,
       "h3cVoAAAGwAccessNumberTable": h3cVoAAAGwAccessNumberTable,
       "h3cVoAAAGwAccessNumberEntry": h3cVoAAAGwAccessNumberEntry,
       "h3cVoAAAGwAccessNumber": h3cVoAAAGwAccessNumber,
       "h3cVoAAAGwAuthentication": h3cVoAAAGwAuthentication,
       "h3cVoAAAGwAuthorization": h3cVoAAAGwAuthorization,
       "h3cVoAAAGwAccounting": h3cVoAAAGwAccounting,
       "h3cVoAAAGwProcessConfig": h3cVoAAAGwProcessConfig,
       "h3cVoAAAGwCardDigit": h3cVoAAAGwCardDigit,
       "h3cVoAAAGwPasswordDigit": h3cVoAAAGwPasswordDigit,
       "h3cVoAAAGwRedialTimes": h3cVoAAAGwRedialTimes,
       "h3cVoAAAGwRowStatus": h3cVoAAAGwRowStatus}
)
