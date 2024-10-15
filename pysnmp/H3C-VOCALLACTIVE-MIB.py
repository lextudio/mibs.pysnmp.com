# SNMP MIB module (H3C-VOCALLACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOCALLACTIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:41 2024
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

(CodecType,) = mibBuilder.importSymbols(
    "H3C-VO-TYPE-MIB",
    "CodecType")

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

h3cVoiceCallActive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6)
)
h3cVoiceCallActive.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoCallActiveObjects_ObjectIdentity = ObjectIdentity
h3cVoCallActiveObjects = _H3cVoCallActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1)
)
_H3cVoCallActiveTable_Object = MibTable
h3cVoCallActiveTable = _H3cVoCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoCallActiveTable.setStatus("current")
_H3cVoCallActiveEntry_Object = MibTableRow
h3cVoCallActiveEntry = _H3cVoCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1)
)
h3cVoCallActiveEntry.setIndexNames(
    (0, "H3C-VOCALLACTIVE-MIB", "h3cVoCallActiveChannel"),
)
if mibBuilder.loadTexts:
    h3cVoCallActiveEntry.setStatus("current")
_H3cVoCallActiveChannel_Type = Integer32
_H3cVoCallActiveChannel_Object = MibTableColumn
h3cVoCallActiveChannel = _H3cVoCallActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 1),
    _H3cVoCallActiveChannel_Type()
)
h3cVoCallActiveChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoCallActiveChannel.setStatus("current")
_H3cVoCallActiveCallerNumber_Type = OctetString
_H3cVoCallActiveCallerNumber_Object = MibTableColumn
h3cVoCallActiveCallerNumber = _H3cVoCallActiveCallerNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 2),
    _H3cVoCallActiveCallerNumber_Type()
)
h3cVoCallActiveCallerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCallerNumber.setStatus("current")
_H3cVoCallActiveCalledNumber_Type = OctetString
_H3cVoCallActiveCalledNumber_Object = MibTableColumn
h3cVoCallActiveCalledNumber = _H3cVoCallActiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 3),
    _H3cVoCallActiveCalledNumber_Type()
)
h3cVoCallActiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCalledNumber.setStatus("current")
_H3cVoCallActiveEncodeType_Type = CodecType
_H3cVoCallActiveEncodeType_Object = MibTableColumn
h3cVoCallActiveEncodeType = _H3cVoCallActiveEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 4),
    _H3cVoCallActiveEncodeType_Type()
)
h3cVoCallActiveEncodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveEncodeType.setStatus("current")
_H3cVoCallActiveLocalAddressType_Type = InetAddressType
_H3cVoCallActiveLocalAddressType_Object = MibTableColumn
h3cVoCallActiveLocalAddressType = _H3cVoCallActiveLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 5),
    _H3cVoCallActiveLocalAddressType_Type()
)
h3cVoCallActiveLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveLocalAddressType.setStatus("current")
_H3cVoCallActiveLocalAddress_Type = InetAddress
_H3cVoCallActiveLocalAddress_Object = MibTableColumn
h3cVoCallActiveLocalAddress = _H3cVoCallActiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 6),
    _H3cVoCallActiveLocalAddress_Type()
)
h3cVoCallActiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveLocalAddress.setStatus("current")
_H3cVoCallActivePeerAddressType_Type = InetAddressType
_H3cVoCallActivePeerAddressType_Object = MibTableColumn
h3cVoCallActivePeerAddressType = _H3cVoCallActivePeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 7),
    _H3cVoCallActivePeerAddressType_Type()
)
h3cVoCallActivePeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActivePeerAddressType.setStatus("current")
_H3cVoCallActivePeerAddress_Type = InetAddress
_H3cVoCallActivePeerAddress_Object = MibTableColumn
h3cVoCallActivePeerAddress = _H3cVoCallActivePeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 8),
    _H3cVoCallActivePeerAddress_Type()
)
h3cVoCallActivePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActivePeerAddress.setStatus("current")


class _H3cVoCallActiveCallOrigin_Type(Integer32):
    """Custom type h3cVoCallActiveCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 2),
          ("caller", 1))
    )


_H3cVoCallActiveCallOrigin_Type.__name__ = "Integer32"
_H3cVoCallActiveCallOrigin_Object = MibTableColumn
h3cVoCallActiveCallOrigin = _H3cVoCallActiveCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 9),
    _H3cVoCallActiveCallOrigin_Type()
)
h3cVoCallActiveCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCallOrigin.setStatus("current")


class _H3cVoCallActiveIPSigType_Type(Integer32):
    """Custom type h3cVoCallActiveIPSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("sip", 3),
          ("unknown", 1))
    )


_H3cVoCallActiveIPSigType_Type.__name__ = "Integer32"
_H3cVoCallActiveIPSigType_Object = MibTableColumn
h3cVoCallActiveIPSigType = _H3cVoCallActiveIPSigType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 10),
    _H3cVoCallActiveIPSigType_Type()
)
h3cVoCallActiveIPSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveIPSigType.setStatus("current")


class _H3cVoCallActivePSTNSigType_Type(Integer32):
    """Custom type h3cVoCallActivePSTNSigType based on Integer32"""
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
        *(("dem", 7),
          ("dss1", 6),
          ("em", 4),
          ("fxo", 3),
          ("fxs", 2),
          ("r2", 5),
          ("unknown", 1))
    )


_H3cVoCallActivePSTNSigType_Type.__name__ = "Integer32"
_H3cVoCallActivePSTNSigType_Object = MibTableColumn
h3cVoCallActivePSTNSigType = _H3cVoCallActivePSTNSigType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 11),
    _H3cVoCallActivePSTNSigType_Type()
)
h3cVoCallActivePSTNSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActivePSTNSigType.setStatus("current")


class _H3cVoCallActiveStatus_Type(Integer32):
    """Custom type h3cVoCallActiveStatus based on Integer32"""
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
        *(("alerting", 3),
          ("calling", 2),
          ("idle", 1),
          ("release", 5),
          ("talking", 4))
    )


_H3cVoCallActiveStatus_Type.__name__ = "Integer32"
_H3cVoCallActiveStatus_Object = MibTableColumn
h3cVoCallActiveStatus = _H3cVoCallActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 12),
    _H3cVoCallActiveStatus_Type()
)
h3cVoCallActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOCALLACTIVE-MIB",
    **{"h3cVoiceCallActive": h3cVoiceCallActive,
       "h3cVoCallActiveObjects": h3cVoCallActiveObjects,
       "h3cVoCallActiveTable": h3cVoCallActiveTable,
       "h3cVoCallActiveEntry": h3cVoCallActiveEntry,
       "h3cVoCallActiveChannel": h3cVoCallActiveChannel,
       "h3cVoCallActiveCallerNumber": h3cVoCallActiveCallerNumber,
       "h3cVoCallActiveCalledNumber": h3cVoCallActiveCalledNumber,
       "h3cVoCallActiveEncodeType": h3cVoCallActiveEncodeType,
       "h3cVoCallActiveLocalAddressType": h3cVoCallActiveLocalAddressType,
       "h3cVoCallActiveLocalAddress": h3cVoCallActiveLocalAddress,
       "h3cVoCallActivePeerAddressType": h3cVoCallActivePeerAddressType,
       "h3cVoCallActivePeerAddress": h3cVoCallActivePeerAddress,
       "h3cVoCallActiveCallOrigin": h3cVoCallActiveCallOrigin,
       "h3cVoCallActiveIPSigType": h3cVoCallActiveIPSigType,
       "h3cVoCallActivePSTNSigType": h3cVoCallActivePSTNSigType,
       "h3cVoCallActiveStatus": h3cVoCallActiveStatus}
)
