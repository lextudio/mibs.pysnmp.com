# SNMP MIB module (Nortel-Magellan-Passport-X25DteMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-X25DteMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:42 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "HexString",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_X25Dte_ObjectIdentity = ObjectIdentity
x25Dte = _X25Dte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90)
)
_X25DteRowStatusTable_Object = MibTable
x25DteRowStatusTable = _X25DteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 1)
)
if mibBuilder.loadTexts:
    x25DteRowStatusTable.setStatus("mandatory")
_X25DteRowStatusEntry_Object = MibTableRow
x25DteRowStatusEntry = _X25DteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 1, 1)
)
x25DteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteRowStatusEntry.setStatus("mandatory")
_X25DteRowStatus_Type = RowStatus
_X25DteRowStatus_Object = MibTableColumn
x25DteRowStatus = _X25DteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 1, 1, 1),
    _X25DteRowStatus_Type()
)
x25DteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRowStatus.setStatus("mandatory")
_X25DteComponentName_Type = DisplayString
_X25DteComponentName_Object = MibTableColumn
x25DteComponentName = _X25DteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 1, 1, 2),
    _X25DteComponentName_Type()
)
x25DteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteComponentName.setStatus("mandatory")
_X25DteStorageType_Type = StorageType
_X25DteStorageType_Object = MibTableColumn
x25DteStorageType = _X25DteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 1, 1, 4),
    _X25DteStorageType_Type()
)
x25DteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteStorageType.setStatus("mandatory")


class _X25DteIndex_Type(Integer32):
    """Custom type x25DteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_X25DteIndex_Type.__name__ = "Integer32"
_X25DteIndex_Object = MibTableColumn
x25DteIndex = _X25DteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 1, 1, 10),
    _X25DteIndex_Type()
)
x25DteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DteIndex.setStatus("mandatory")
_X25DtePeer_ObjectIdentity = ObjectIdentity
x25DtePeer = _X25DtePeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2)
)
_X25DtePeerRowStatusTable_Object = MibTable
x25DtePeerRowStatusTable = _X25DtePeerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 1)
)
if mibBuilder.loadTexts:
    x25DtePeerRowStatusTable.setStatus("mandatory")
_X25DtePeerRowStatusEntry_Object = MibTableRow
x25DtePeerRowStatusEntry = _X25DtePeerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 1, 1)
)
x25DtePeerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerIndex"),
)
if mibBuilder.loadTexts:
    x25DtePeerRowStatusEntry.setStatus("mandatory")
_X25DtePeerRowStatus_Type = RowStatus
_X25DtePeerRowStatus_Object = MibTableColumn
x25DtePeerRowStatus = _X25DtePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 1, 1, 1),
    _X25DtePeerRowStatus_Type()
)
x25DtePeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerRowStatus.setStatus("mandatory")
_X25DtePeerComponentName_Type = DisplayString
_X25DtePeerComponentName_Object = MibTableColumn
x25DtePeerComponentName = _X25DtePeerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 1, 1, 2),
    _X25DtePeerComponentName_Type()
)
x25DtePeerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePeerComponentName.setStatus("mandatory")
_X25DtePeerStorageType_Type = StorageType
_X25DtePeerStorageType_Object = MibTableColumn
x25DtePeerStorageType = _X25DtePeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 1, 1, 4),
    _X25DtePeerStorageType_Type()
)
x25DtePeerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePeerStorageType.setStatus("mandatory")


class _X25DtePeerIndex_Type(Integer32):
    """Custom type x25DtePeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25DtePeerIndex_Type.__name__ = "Integer32"
_X25DtePeerIndex_Object = MibTableColumn
x25DtePeerIndex = _X25DtePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 1, 1, 10),
    _X25DtePeerIndex_Type()
)
x25DtePeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DtePeerIndex.setStatus("mandatory")
_X25DtePeerIfTable_Object = MibTable
x25DtePeerIfTable = _X25DtePeerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 10)
)
if mibBuilder.loadTexts:
    x25DtePeerIfTable.setStatus("mandatory")
_X25DtePeerIfEntry_Object = MibTableRow
x25DtePeerIfEntry = _X25DtePeerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 10, 1)
)
x25DtePeerIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerIndex"),
)
if mibBuilder.loadTexts:
    x25DtePeerIfEntry.setStatus("mandatory")


class _X25DtePeerEncAddressType_Type(Integer32):
    """Custom type x25DtePeerEncAddressType based on Integer32"""
    defaultValue = 204

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            204
        )
    )
    namedValues = NamedValues(
        ("ip", 204)
    )


_X25DtePeerEncAddressType_Type.__name__ = "Integer32"
_X25DtePeerEncAddressType_Object = MibTableColumn
x25DtePeerEncAddressType = _X25DtePeerEncAddressType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 10, 1, 1),
    _X25DtePeerEncAddressType_Type()
)
x25DtePeerEncAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerEncAddressType.setStatus("mandatory")


class _X25DtePeerEncAddress_Type(AsciiString):
    """Custom type x25DtePeerEncAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_X25DtePeerEncAddress_Type.__name__ = "AsciiString"
_X25DtePeerEncAddress_Object = MibTableColumn
x25DtePeerEncAddress = _X25DtePeerEncAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 10, 1, 2),
    _X25DtePeerEncAddress_Type()
)
x25DtePeerEncAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerEncAddress.setStatus("mandatory")


class _X25DtePeerX25Address_Type(DigitString):
    """Custom type x25DtePeerX25Address based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_X25DtePeerX25Address_Type.__name__ = "DigitString"
_X25DtePeerX25Address_Object = MibTableColumn
x25DtePeerX25Address = _X25DtePeerX25Address_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 10, 1, 3),
    _X25DtePeerX25Address_Type()
)
x25DtePeerX25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerX25Address.setStatus("mandatory")
_X25DtePeerLinkToRemoteGroup_Type = Link
_X25DtePeerLinkToRemoteGroup_Object = MibTableColumn
x25DtePeerLinkToRemoteGroup = _X25DtePeerLinkToRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 10, 1, 4),
    _X25DtePeerLinkToRemoteGroup_Type()
)
x25DtePeerLinkToRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerLinkToRemoteGroup.setStatus("mandatory")
_X25DtePeerCpTable_Object = MibTable
x25DtePeerCpTable = _X25DtePeerCpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12)
)
if mibBuilder.loadTexts:
    x25DtePeerCpTable.setStatus("mandatory")
_X25DtePeerCpEntry_Object = MibTableRow
x25DtePeerCpEntry = _X25DtePeerCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1)
)
x25DtePeerCpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerIndex"),
)
if mibBuilder.loadTexts:
    x25DtePeerCpEntry.setStatus("mandatory")


class _X25DtePeerInPacketSize_Type(Unsigned32):
    """Custom type x25DtePeerInPacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DtePeerInPacketSize_Type.__name__ = "Unsigned32"
_X25DtePeerInPacketSize_Object = MibTableColumn
x25DtePeerInPacketSize = _X25DtePeerInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 1),
    _X25DtePeerInPacketSize_Type()
)
x25DtePeerInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerInPacketSize.setStatus("mandatory")


class _X25DtePeerOutPacketSize_Type(Unsigned32):
    """Custom type x25DtePeerOutPacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DtePeerOutPacketSize_Type.__name__ = "Unsigned32"
_X25DtePeerOutPacketSize_Object = MibTableColumn
x25DtePeerOutPacketSize = _X25DtePeerOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 2),
    _X25DtePeerOutPacketSize_Type()
)
x25DtePeerOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerOutPacketSize.setStatus("mandatory")


class _X25DtePeerInWindowSize_Type(Unsigned32):
    """Custom type x25DtePeerInWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25DtePeerInWindowSize_Type.__name__ = "Unsigned32"
_X25DtePeerInWindowSize_Object = MibTableColumn
x25DtePeerInWindowSize = _X25DtePeerInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 3),
    _X25DtePeerInWindowSize_Type()
)
x25DtePeerInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerInWindowSize.setStatus("mandatory")


class _X25DtePeerOutWindowSize_Type(Unsigned32):
    """Custom type x25DtePeerOutWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25DtePeerOutWindowSize_Type.__name__ = "Unsigned32"
_X25DtePeerOutWindowSize_Object = MibTableColumn
x25DtePeerOutWindowSize = _X25DtePeerOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 4),
    _X25DtePeerOutWindowSize_Type()
)
x25DtePeerOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerOutWindowSize.setStatus("mandatory")


class _X25DtePeerAcceptReverseCharging_Type(Integer32):
    """Custom type x25DtePeerAcceptReverseCharging based on Integer32"""
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
        *(("accept", 2),
          ("default", 1),
          ("refuse", 3))
    )


_X25DtePeerAcceptReverseCharging_Type.__name__ = "Integer32"
_X25DtePeerAcceptReverseCharging_Object = MibTableColumn
x25DtePeerAcceptReverseCharging = _X25DtePeerAcceptReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 5),
    _X25DtePeerAcceptReverseCharging_Type()
)
x25DtePeerAcceptReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerAcceptReverseCharging.setStatus("mandatory")


class _X25DtePeerProposeReverseCharging_Type(Integer32):
    """Custom type x25DtePeerProposeReverseCharging based on Integer32"""
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
        *(("default", 1),
          ("local", 3),
          ("reverse", 2))
    )


_X25DtePeerProposeReverseCharging_Type.__name__ = "Integer32"
_X25DtePeerProposeReverseCharging_Object = MibTableColumn
x25DtePeerProposeReverseCharging = _X25DtePeerProposeReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 6),
    _X25DtePeerProposeReverseCharging_Type()
)
x25DtePeerProposeReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerProposeReverseCharging.setStatus("mandatory")


class _X25DtePeerOutThroughputClassSize_Type(Integer32):
    """Custom type x25DtePeerOutThroughputClassSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("default", 18),
          ("n1200", 7),
          ("n150", 4),
          ("n19200", 11),
          ("n2400", 8),
          ("n300", 5),
          ("n4800", 9),
          ("n48000", 12),
          ("n600", 6),
          ("n64000", 13),
          ("n75", 3),
          ("n9600", 10),
          ("notSpecified", 17))
    )


_X25DtePeerOutThroughputClassSize_Type.__name__ = "Integer32"
_X25DtePeerOutThroughputClassSize_Object = MibTableColumn
x25DtePeerOutThroughputClassSize = _X25DtePeerOutThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 8),
    _X25DtePeerOutThroughputClassSize_Type()
)
x25DtePeerOutThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerOutThroughputClassSize.setStatus("mandatory")


class _X25DtePeerInThroughputClassSize_Type(Integer32):
    """Custom type x25DtePeerInThroughputClassSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("default", 18),
          ("n1200", 7),
          ("n150", 4),
          ("n19200", 11),
          ("n2400", 8),
          ("n300", 5),
          ("n4800", 9),
          ("n48000", 12),
          ("n600", 6),
          ("n64000", 13),
          ("n75", 3),
          ("n9600", 10),
          ("notSpecified", 17))
    )


_X25DtePeerInThroughputClassSize_Type.__name__ = "Integer32"
_X25DtePeerInThroughputClassSize_Object = MibTableColumn
x25DtePeerInThroughputClassSize = _X25DtePeerInThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 9),
    _X25DtePeerInThroughputClassSize_Type()
)
x25DtePeerInThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerInThroughputClassSize.setStatus("mandatory")


class _X25DtePeerCugIndex_Type(AsciiString):
    """Custom type x25DtePeerCugIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25DtePeerCugIndex_Type.__name__ = "AsciiString"
_X25DtePeerCugIndex_Object = MibTableColumn
x25DtePeerCugIndex = _X25DtePeerCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 10),
    _X25DtePeerCugIndex_Type()
)
x25DtePeerCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerCugIndex.setStatus("mandatory")


class _X25DtePeerCugoaIndex_Type(AsciiString):
    """Custom type x25DtePeerCugoaIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25DtePeerCugoaIndex_Type.__name__ = "AsciiString"
_X25DtePeerCugoaIndex_Object = MibTableColumn
x25DtePeerCugoaIndex = _X25DtePeerCugoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 11),
    _X25DtePeerCugoaIndex_Type()
)
x25DtePeerCugoaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerCugoaIndex.setStatus("mandatory")


class _X25DtePeerNetworkUserIdentifier_Type(HexString):
    """Custom type x25DtePeerNetworkUserIdentifier based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DtePeerNetworkUserIdentifier_Type.__name__ = "HexString"
_X25DtePeerNetworkUserIdentifier_Object = MibTableColumn
x25DtePeerNetworkUserIdentifier = _X25DtePeerNetworkUserIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 12),
    _X25DtePeerNetworkUserIdentifier_Type()
)
x25DtePeerNetworkUserIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerNetworkUserIdentifier.setStatus("mandatory")


class _X25DtePeerChargingInformation_Type(Integer32):
    """Custom type x25DtePeerChargingInformation based on Integer32"""
    defaultValue = 2

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
        *(("default", 1),
          ("notRequested", 3),
          ("notSpecified", 2),
          ("requested", 4))
    )


_X25DtePeerChargingInformation_Type.__name__ = "Integer32"
_X25DtePeerChargingInformation_Object = MibTableColumn
x25DtePeerChargingInformation = _X25DtePeerChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 13),
    _X25DtePeerChargingInformation_Type()
)
x25DtePeerChargingInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerChargingInformation.setStatus("mandatory")


class _X25DtePeerRpoa_Type(AsciiString):
    """Custom type x25DtePeerRpoa based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DtePeerRpoa_Type.__name__ = "AsciiString"
_X25DtePeerRpoa_Object = MibTableColumn
x25DtePeerRpoa = _X25DtePeerRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 14),
    _X25DtePeerRpoa_Type()
)
x25DtePeerRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerRpoa.setStatus("mandatory")


class _X25DtePeerTrnstDlySlctnAInd_Type(Unsigned32):
    """Custom type x25DtePeerTrnstDlySlctnAInd based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65537),
    )


_X25DtePeerTrnstDlySlctnAInd_Type.__name__ = "Unsigned32"
_X25DtePeerTrnstDlySlctnAInd_Object = MibTableColumn
x25DtePeerTrnstDlySlctnAInd = _X25DtePeerTrnstDlySlctnAInd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 15),
    _X25DtePeerTrnstDlySlctnAInd_Type()
)
x25DtePeerTrnstDlySlctnAInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerTrnstDlySlctnAInd.setStatus("mandatory")


class _X25DtePeerCallingNetworkFax_Type(HexString):
    """Custom type x25DtePeerCallingNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DtePeerCallingNetworkFax_Type.__name__ = "HexString"
_X25DtePeerCallingNetworkFax_Object = MibTableColumn
x25DtePeerCallingNetworkFax = _X25DtePeerCallingNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 24),
    _X25DtePeerCallingNetworkFax_Type()
)
x25DtePeerCallingNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerCallingNetworkFax.setStatus("mandatory")


class _X25DtePeerCalledNetworkFax_Type(HexString):
    """Custom type x25DtePeerCalledNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DtePeerCalledNetworkFax_Type.__name__ = "HexString"
_X25DtePeerCalledNetworkFax_Object = MibTableColumn
x25DtePeerCalledNetworkFax = _X25DtePeerCalledNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 25),
    _X25DtePeerCalledNetworkFax_Type()
)
x25DtePeerCalledNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerCalledNetworkFax.setStatus("mandatory")


class _X25DtePeerCallUserData_Type(HexString):
    """Custom type x25DtePeerCallUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_X25DtePeerCallUserData_Type.__name__ = "HexString"
_X25DtePeerCallUserData_Object = MibTableColumn
x25DtePeerCallUserData = _X25DtePeerCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 12, 1, 26),
    _X25DtePeerCallUserData_Type()
)
x25DtePeerCallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePeerCallUserData.setStatus("mandatory")
_X25DtePeerPEncTable_Object = MibTable
x25DtePeerPEncTable = _X25DtePeerPEncTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 208)
)
if mibBuilder.loadTexts:
    x25DtePeerPEncTable.setStatus("mandatory")
_X25DtePeerPEncEntry_Object = MibTableRow
x25DtePeerPEncEntry = _X25DtePeerPEncEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 208, 1)
)
x25DtePeerPEncEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerPEncIndex"),
)
if mibBuilder.loadTexts:
    x25DtePeerPEncEntry.setStatus("mandatory")


class _X25DtePeerPEncIndex_Type(Integer32):
    """Custom type x25DtePeerPEncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_X25DtePeerPEncIndex_Type.__name__ = "Integer32"
_X25DtePeerPEncIndex_Object = MibTableColumn
x25DtePeerPEncIndex = _X25DtePeerPEncIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 208, 1, 1),
    _X25DtePeerPEncIndex_Type()
)
x25DtePeerPEncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DtePeerPEncIndex.setStatus("mandatory")


class _X25DtePeerPEncValue_Type(Integer32):
    """Custom type x25DtePeerPEncValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            204
        )
    )
    namedValues = NamedValues(
        ("ip", 204)
    )


_X25DtePeerPEncValue_Type.__name__ = "Integer32"
_X25DtePeerPEncValue_Object = MibTableColumn
x25DtePeerPEncValue = _X25DtePeerPEncValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 208, 1, 2),
    _X25DtePeerPEncValue_Type()
)
x25DtePeerPEncValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePeerPEncValue.setStatus("mandatory")
_X25DtePeerPEncRowStatus_Type = RowStatus
_X25DtePeerPEncRowStatus_Object = MibTableColumn
x25DtePeerPEncRowStatus = _X25DtePeerPEncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 208, 1, 3),
    _X25DtePeerPEncRowStatus_Type()
)
x25DtePeerPEncRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x25DtePeerPEncRowStatus.setStatus("mandatory")
_X25DtePeerLcnTable_Object = MibTable
x25DtePeerLcnTable = _X25DtePeerLcnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 209)
)
if mibBuilder.loadTexts:
    x25DtePeerLcnTable.setStatus("mandatory")
_X25DtePeerLcnEntry_Object = MibTableRow
x25DtePeerLcnEntry = _X25DtePeerLcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 209, 1)
)
x25DtePeerLcnEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePeerLcnValue"),
)
if mibBuilder.loadTexts:
    x25DtePeerLcnEntry.setStatus("mandatory")


class _X25DtePeerLcnValue_Type(Integer32):
    """Custom type x25DtePeerLcnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25DtePeerLcnValue_Type.__name__ = "Integer32"
_X25DtePeerLcnValue_Object = MibTableColumn
x25DtePeerLcnValue = _X25DtePeerLcnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 2, 209, 1, 1),
    _X25DtePeerLcnValue_Type()
)
x25DtePeerLcnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePeerLcnValue.setStatus("mandatory")
_X25DtePLcn_ObjectIdentity = ObjectIdentity
x25DtePLcn = _X25DtePLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3)
)
_X25DtePLcnRowStatusTable_Object = MibTable
x25DtePLcnRowStatusTable = _X25DtePLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 1)
)
if mibBuilder.loadTexts:
    x25DtePLcnRowStatusTable.setStatus("mandatory")
_X25DtePLcnRowStatusEntry_Object = MibTableRow
x25DtePLcnRowStatusEntry = _X25DtePLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 1, 1)
)
x25DtePLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DtePLcnRowStatusEntry.setStatus("mandatory")
_X25DtePLcnRowStatus_Type = RowStatus
_X25DtePLcnRowStatus_Object = MibTableColumn
x25DtePLcnRowStatus = _X25DtePLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 1, 1, 1),
    _X25DtePLcnRowStatus_Type()
)
x25DtePLcnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnRowStatus.setStatus("mandatory")
_X25DtePLcnComponentName_Type = DisplayString
_X25DtePLcnComponentName_Object = MibTableColumn
x25DtePLcnComponentName = _X25DtePLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 1, 1, 2),
    _X25DtePLcnComponentName_Type()
)
x25DtePLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePLcnComponentName.setStatus("mandatory")
_X25DtePLcnStorageType_Type = StorageType
_X25DtePLcnStorageType_Object = MibTableColumn
x25DtePLcnStorageType = _X25DtePLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 1, 1, 4),
    _X25DtePLcnStorageType_Type()
)
x25DtePLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePLcnStorageType.setStatus("mandatory")


class _X25DtePLcnIndex_Type(Integer32):
    """Custom type x25DtePLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25DtePLcnIndex_Type.__name__ = "Integer32"
_X25DtePLcnIndex_Object = MibTableColumn
x25DtePLcnIndex = _X25DtePLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 1, 1, 10),
    _X25DtePLcnIndex_Type()
)
x25DtePLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DtePLcnIndex.setStatus("mandatory")
_X25DtePLcnProvTable_Object = MibTable
x25DtePLcnProvTable = _X25DtePLcnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10)
)
if mibBuilder.loadTexts:
    x25DtePLcnProvTable.setStatus("mandatory")
_X25DtePLcnProvEntry_Object = MibTableRow
x25DtePLcnProvEntry = _X25DtePLcnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1)
)
x25DtePLcnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DtePLcnProvEntry.setStatus("mandatory")


class _X25DtePLcnEncAddressType_Type(Integer32):
    """Custom type x25DtePLcnEncAddressType based on Integer32"""
    defaultValue = 204

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              204)
        )
    )
    namedValues = NamedValues(
        *(("ip", 204),
          ("none", 0))
    )


_X25DtePLcnEncAddressType_Type.__name__ = "Integer32"
_X25DtePLcnEncAddressType_Object = MibTableColumn
x25DtePLcnEncAddressType = _X25DtePLcnEncAddressType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 1),
    _X25DtePLcnEncAddressType_Type()
)
x25DtePLcnEncAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnEncAddressType.setStatus("mandatory")


class _X25DtePLcnEncAddress_Type(AsciiString):
    """Custom type x25DtePLcnEncAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_X25DtePLcnEncAddress_Type.__name__ = "AsciiString"
_X25DtePLcnEncAddress_Object = MibTableColumn
x25DtePLcnEncAddress = _X25DtePLcnEncAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 2),
    _X25DtePLcnEncAddress_Type()
)
x25DtePLcnEncAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnEncAddress.setStatus("mandatory")


class _X25DtePLcnProtocolEncType_Type(Integer32):
    """Custom type x25DtePLcnProtocolEncType based on Integer32"""
    defaultValue = 204

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              204,
              257)
        )
    )
    namedValues = NamedValues(
        *(("ip", 204),
          ("nscNull", 257),
          ("null", 0))
    )


_X25DtePLcnProtocolEncType_Type.__name__ = "Integer32"
_X25DtePLcnProtocolEncType_Object = MibTableColumn
x25DtePLcnProtocolEncType = _X25DtePLcnProtocolEncType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 3),
    _X25DtePLcnProtocolEncType_Type()
)
x25DtePLcnProtocolEncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnProtocolEncType.setStatus("mandatory")
_X25DtePLcnLinkToRemoteGroup_Type = Link
_X25DtePLcnLinkToRemoteGroup_Object = MibTableColumn
x25DtePLcnLinkToRemoteGroup = _X25DtePLcnLinkToRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 4),
    _X25DtePLcnLinkToRemoteGroup_Type()
)
x25DtePLcnLinkToRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnLinkToRemoteGroup.setStatus("mandatory")


class _X25DtePLcnInPacketSize_Type(Unsigned32):
    """Custom type x25DtePLcnInPacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DtePLcnInPacketSize_Type.__name__ = "Unsigned32"
_X25DtePLcnInPacketSize_Object = MibTableColumn
x25DtePLcnInPacketSize = _X25DtePLcnInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 5),
    _X25DtePLcnInPacketSize_Type()
)
x25DtePLcnInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnInPacketSize.setStatus("mandatory")


class _X25DtePLcnOutPacketSize_Type(Unsigned32):
    """Custom type x25DtePLcnOutPacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DtePLcnOutPacketSize_Type.__name__ = "Unsigned32"
_X25DtePLcnOutPacketSize_Object = MibTableColumn
x25DtePLcnOutPacketSize = _X25DtePLcnOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 6),
    _X25DtePLcnOutPacketSize_Type()
)
x25DtePLcnOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnOutPacketSize.setStatus("mandatory")


class _X25DtePLcnInWindowSize_Type(Unsigned32):
    """Custom type x25DtePLcnInWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DtePLcnInWindowSize_Type.__name__ = "Unsigned32"
_X25DtePLcnInWindowSize_Object = MibTableColumn
x25DtePLcnInWindowSize = _X25DtePLcnInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 7),
    _X25DtePLcnInWindowSize_Type()
)
x25DtePLcnInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnInWindowSize.setStatus("mandatory")


class _X25DtePLcnOutWindowSize_Type(Unsigned32):
    """Custom type x25DtePLcnOutWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DtePLcnOutWindowSize_Type.__name__ = "Unsigned32"
_X25DtePLcnOutWindowSize_Object = MibTableColumn
x25DtePLcnOutWindowSize = _X25DtePLcnOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 3, 10, 1, 8),
    _X25DtePLcnOutWindowSize_Type()
)
x25DtePLcnOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePLcnOutWindowSize.setStatus("mandatory")
_X25DteLcn_ObjectIdentity = ObjectIdentity
x25DteLcn = _X25DteLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4)
)
_X25DteLcnRowStatusTable_Object = MibTable
x25DteLcnRowStatusTable = _X25DteLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 1)
)
if mibBuilder.loadTexts:
    x25DteLcnRowStatusTable.setStatus("mandatory")
_X25DteLcnRowStatusEntry_Object = MibTableRow
x25DteLcnRowStatusEntry = _X25DteLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 1, 1)
)
x25DteLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DteLcnRowStatusEntry.setStatus("mandatory")
_X25DteLcnRowStatus_Type = RowStatus
_X25DteLcnRowStatus_Object = MibTableColumn
x25DteLcnRowStatus = _X25DteLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 1, 1, 1),
    _X25DteLcnRowStatus_Type()
)
x25DteLcnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnRowStatus.setStatus("mandatory")
_X25DteLcnComponentName_Type = DisplayString
_X25DteLcnComponentName_Object = MibTableColumn
x25DteLcnComponentName = _X25DteLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 1, 1, 2),
    _X25DteLcnComponentName_Type()
)
x25DteLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnComponentName.setStatus("mandatory")
_X25DteLcnStorageType_Type = StorageType
_X25DteLcnStorageType_Object = MibTableColumn
x25DteLcnStorageType = _X25DteLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 1, 1, 4),
    _X25DteLcnStorageType_Type()
)
x25DteLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnStorageType.setStatus("mandatory")


class _X25DteLcnIndex_Type(Integer32):
    """Custom type x25DteLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25DteLcnIndex_Type.__name__ = "Integer32"
_X25DteLcnIndex_Object = MibTableColumn
x25DteLcnIndex = _X25DteLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 1, 1, 10),
    _X25DteLcnIndex_Type()
)
x25DteLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DteLcnIndex.setStatus("mandatory")
_X25DteLcnStateTable_Object = MibTable
x25DteLcnStateTable = _X25DteLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 10)
)
if mibBuilder.loadTexts:
    x25DteLcnStateTable.setStatus("mandatory")
_X25DteLcnStateEntry_Object = MibTableRow
x25DteLcnStateEntry = _X25DteLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 10, 1)
)
x25DteLcnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DteLcnStateEntry.setStatus("mandatory")


class _X25DteLcnAdminState_Type(Integer32):
    """Custom type x25DteLcnAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_X25DteLcnAdminState_Type.__name__ = "Integer32"
_X25DteLcnAdminState_Object = MibTableColumn
x25DteLcnAdminState = _X25DteLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 10, 1, 1),
    _X25DteLcnAdminState_Type()
)
x25DteLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnAdminState.setStatus("mandatory")


class _X25DteLcnOperationalState_Type(Integer32):
    """Custom type x25DteLcnOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X25DteLcnOperationalState_Type.__name__ = "Integer32"
_X25DteLcnOperationalState_Object = MibTableColumn
x25DteLcnOperationalState = _X25DteLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 10, 1, 2),
    _X25DteLcnOperationalState_Type()
)
x25DteLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOperationalState.setStatus("mandatory")


class _X25DteLcnUsageState_Type(Integer32):
    """Custom type x25DteLcnUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_X25DteLcnUsageState_Type.__name__ = "Integer32"
_X25DteLcnUsageState_Object = MibTableColumn
x25DteLcnUsageState = _X25DteLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 10, 1, 3),
    _X25DteLcnUsageState_Type()
)
x25DteLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnUsageState.setStatus("mandatory")
_X25DteLcnCpTable_Object = MibTable
x25DteLcnCpTable = _X25DteLcnCpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11)
)
if mibBuilder.loadTexts:
    x25DteLcnCpTable.setStatus("mandatory")
_X25DteLcnCpEntry_Object = MibTableRow
x25DteLcnCpEntry = _X25DteLcnCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1)
)
x25DteLcnCpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DteLcnCpEntry.setStatus("mandatory")


class _X25DteLcnInPacketSize_Type(Unsigned32):
    """Custom type x25DteLcnInPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DteLcnInPacketSize_Type.__name__ = "Unsigned32"
_X25DteLcnInPacketSize_Object = MibTableColumn
x25DteLcnInPacketSize = _X25DteLcnInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 1),
    _X25DteLcnInPacketSize_Type()
)
x25DteLcnInPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInPacketSize.setStatus("mandatory")


class _X25DteLcnOutPacketSize_Type(Unsigned32):
    """Custom type x25DteLcnOutPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DteLcnOutPacketSize_Type.__name__ = "Unsigned32"
_X25DteLcnOutPacketSize_Object = MibTableColumn
x25DteLcnOutPacketSize = _X25DteLcnOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 2),
    _X25DteLcnOutPacketSize_Type()
)
x25DteLcnOutPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOutPacketSize.setStatus("mandatory")


class _X25DteLcnInWindowSize_Type(Unsigned32):
    """Custom type x25DteLcnInWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DteLcnInWindowSize_Type.__name__ = "Unsigned32"
_X25DteLcnInWindowSize_Object = MibTableColumn
x25DteLcnInWindowSize = _X25DteLcnInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 3),
    _X25DteLcnInWindowSize_Type()
)
x25DteLcnInWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInWindowSize.setStatus("mandatory")


class _X25DteLcnOutWindowSize_Type(Unsigned32):
    """Custom type x25DteLcnOutWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DteLcnOutWindowSize_Type.__name__ = "Unsigned32"
_X25DteLcnOutWindowSize_Object = MibTableColumn
x25DteLcnOutWindowSize = _X25DteLcnOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 4),
    _X25DteLcnOutWindowSize_Type()
)
x25DteLcnOutWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOutWindowSize.setStatus("mandatory")


class _X25DteLcnProposeReverseCharging_Type(Integer32):
    """Custom type x25DteLcnProposeReverseCharging based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("reverse", 2))
    )


_X25DteLcnProposeReverseCharging_Type.__name__ = "Integer32"
_X25DteLcnProposeReverseCharging_Object = MibTableColumn
x25DteLcnProposeReverseCharging = _X25DteLcnProposeReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 5),
    _X25DteLcnProposeReverseCharging_Type()
)
x25DteLcnProposeReverseCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnProposeReverseCharging.setStatus("mandatory")


class _X25DteLcnFastSelect_Type(Integer32):
    """Custom type x25DteLcnFastSelect based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("no", 5),
          ("restricted", 4),
          ("unrestricted", 3))
    )


_X25DteLcnFastSelect_Type.__name__ = "Integer32"
_X25DteLcnFastSelect_Object = MibTableColumn
x25DteLcnFastSelect = _X25DteLcnFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 6),
    _X25DteLcnFastSelect_Type()
)
x25DteLcnFastSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnFastSelect.setStatus("mandatory")


class _X25DteLcnOutThroughputClassSize_Type(Integer32):
    """Custom type x25DteLcnOutThroughputClassSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 7),
          ("n150", 4),
          ("n19200", 11),
          ("n2400", 8),
          ("n300", 5),
          ("n4800", 9),
          ("n48000", 12),
          ("n600", 6),
          ("n64000", 13),
          ("n75", 3),
          ("n9600", 10),
          ("notSpecified", 17))
    )


_X25DteLcnOutThroughputClassSize_Type.__name__ = "Integer32"
_X25DteLcnOutThroughputClassSize_Object = MibTableColumn
x25DteLcnOutThroughputClassSize = _X25DteLcnOutThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 7),
    _X25DteLcnOutThroughputClassSize_Type()
)
x25DteLcnOutThroughputClassSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOutThroughputClassSize.setStatus("mandatory")


class _X25DteLcnInThroughputClassSize_Type(Integer32):
    """Custom type x25DteLcnInThroughputClassSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 7),
          ("n150", 4),
          ("n19200", 11),
          ("n2400", 8),
          ("n300", 5),
          ("n4800", 9),
          ("n48000", 12),
          ("n600", 6),
          ("n64000", 13),
          ("n75", 3),
          ("n9600", 10),
          ("notSpecified", 17))
    )


_X25DteLcnInThroughputClassSize_Type.__name__ = "Integer32"
_X25DteLcnInThroughputClassSize_Object = MibTableColumn
x25DteLcnInThroughputClassSize = _X25DteLcnInThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 8),
    _X25DteLcnInThroughputClassSize_Type()
)
x25DteLcnInThroughputClassSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInThroughputClassSize.setStatus("mandatory")


class _X25DteLcnCugIndex_Type(AsciiString):
    """Custom type x25DteLcnCugIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25DteLcnCugIndex_Type.__name__ = "AsciiString"
_X25DteLcnCugIndex_Object = MibTableColumn
x25DteLcnCugIndex = _X25DteLcnCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 9),
    _X25DteLcnCugIndex_Type()
)
x25DteLcnCugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCugIndex.setStatus("mandatory")


class _X25DteLcnCugoaIndex_Type(AsciiString):
    """Custom type x25DteLcnCugoaIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25DteLcnCugoaIndex_Type.__name__ = "AsciiString"
_X25DteLcnCugoaIndex_Object = MibTableColumn
x25DteLcnCugoaIndex = _X25DteLcnCugoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 10),
    _X25DteLcnCugoaIndex_Type()
)
x25DteLcnCugoaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCugoaIndex.setStatus("mandatory")


class _X25DteLcnNetworkUserIdentifier_Type(HexString):
    """Custom type x25DteLcnNetworkUserIdentifier based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteLcnNetworkUserIdentifier_Type.__name__ = "HexString"
_X25DteLcnNetworkUserIdentifier_Object = MibTableColumn
x25DteLcnNetworkUserIdentifier = _X25DteLcnNetworkUserIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 11),
    _X25DteLcnNetworkUserIdentifier_Type()
)
x25DteLcnNetworkUserIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnNetworkUserIdentifier.setStatus("mandatory")


class _X25DteLcnChargingInformation_Type(Integer32):
    """Custom type x25DteLcnChargingInformation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notRequested", 3),
          ("notSpecified", 2),
          ("requested", 4))
    )


_X25DteLcnChargingInformation_Type.__name__ = "Integer32"
_X25DteLcnChargingInformation_Object = MibTableColumn
x25DteLcnChargingInformation = _X25DteLcnChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 12),
    _X25DteLcnChargingInformation_Type()
)
x25DteLcnChargingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnChargingInformation.setStatus("mandatory")


class _X25DteLcnRpoa_Type(AsciiString):
    """Custom type x25DteLcnRpoa based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteLcnRpoa_Type.__name__ = "AsciiString"
_X25DteLcnRpoa_Object = MibTableColumn
x25DteLcnRpoa = _X25DteLcnRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 13),
    _X25DteLcnRpoa_Type()
)
x25DteLcnRpoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnRpoa.setStatus("mandatory")


class _X25DteLcnTrnstDlySlctnAInd_Type(Unsigned32):
    """Custom type x25DteLcnTrnstDlySlctnAInd based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_X25DteLcnTrnstDlySlctnAInd_Type.__name__ = "Unsigned32"
_X25DteLcnTrnstDlySlctnAInd_Object = MibTableColumn
x25DteLcnTrnstDlySlctnAInd = _X25DteLcnTrnstDlySlctnAInd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 14),
    _X25DteLcnTrnstDlySlctnAInd_Type()
)
x25DteLcnTrnstDlySlctnAInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnTrnstDlySlctnAInd.setStatus("mandatory")


class _X25DteLcnCallingNetworkFax_Type(HexString):
    """Custom type x25DteLcnCallingNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteLcnCallingNetworkFax_Type.__name__ = "HexString"
_X25DteLcnCallingNetworkFax_Object = MibTableColumn
x25DteLcnCallingNetworkFax = _X25DteLcnCallingNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 23),
    _X25DteLcnCallingNetworkFax_Type()
)
x25DteLcnCallingNetworkFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCallingNetworkFax.setStatus("mandatory")


class _X25DteLcnCalledNetworkFax_Type(HexString):
    """Custom type x25DteLcnCalledNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteLcnCalledNetworkFax_Type.__name__ = "HexString"
_X25DteLcnCalledNetworkFax_Object = MibTableColumn
x25DteLcnCalledNetworkFax = _X25DteLcnCalledNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 24),
    _X25DteLcnCalledNetworkFax_Type()
)
x25DteLcnCalledNetworkFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCalledNetworkFax.setStatus("mandatory")


class _X25DteLcnCallUserData_Type(HexString):
    """Custom type x25DteLcnCallUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_X25DteLcnCallUserData_Type.__name__ = "HexString"
_X25DteLcnCallUserData_Object = MibTableColumn
x25DteLcnCallUserData = _X25DteLcnCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 11, 1, 25),
    _X25DteLcnCallUserData_Type()
)
x25DteLcnCallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCallUserData.setStatus("mandatory")
_X25DteLcnLcnStatusTable_Object = MibTable
x25DteLcnLcnStatusTable = _X25DteLcnLcnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12)
)
if mibBuilder.loadTexts:
    x25DteLcnLcnStatusTable.setStatus("mandatory")
_X25DteLcnLcnStatusEntry_Object = MibTableRow
x25DteLcnLcnStatusEntry = _X25DteLcnLcnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12, 1)
)
x25DteLcnLcnStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DteLcnLcnStatusEntry.setStatus("mandatory")


class _X25DteLcnStatus_Type(Integer32):
    """Custom type x25DteLcnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("calling", 3),
          ("clearing", 5),
          ("closed", 2),
          ("dataTransfer", 4),
          ("resetting", 7))
    )


_X25DteLcnStatus_Type.__name__ = "Integer32"
_X25DteLcnStatus_Object = MibTableColumn
x25DteLcnStatus = _X25DteLcnStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12, 1, 1),
    _X25DteLcnStatus_Type()
)
x25DteLcnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnStatus.setStatus("mandatory")


class _X25DteLcnCallDirection_Type(Integer32):
    """Custom type x25DteLcnCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("permanentLcn", 3))
    )


_X25DteLcnCallDirection_Type.__name__ = "Integer32"
_X25DteLcnCallDirection_Object = MibTableColumn
x25DteLcnCallDirection = _X25DteLcnCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12, 1, 3),
    _X25DteLcnCallDirection_Type()
)
x25DteLcnCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCallDirection.setStatus("mandatory")


class _X25DteLcnCalledAddress_Type(DigitString):
    """Custom type x25DteLcnCalledAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_X25DteLcnCalledAddress_Type.__name__ = "DigitString"
_X25DteLcnCalledAddress_Object = MibTableColumn
x25DteLcnCalledAddress = _X25DteLcnCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12, 1, 4),
    _X25DteLcnCalledAddress_Type()
)
x25DteLcnCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCalledAddress.setStatus("mandatory")


class _X25DteLcnCallingAddress_Type(DigitString):
    """Custom type x25DteLcnCallingAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_X25DteLcnCallingAddress_Type.__name__ = "DigitString"
_X25DteLcnCallingAddress_Object = MibTableColumn
x25DteLcnCallingAddress = _X25DteLcnCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12, 1, 5),
    _X25DteLcnCallingAddress_Type()
)
x25DteLcnCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnCallingAddress.setStatus("mandatory")


class _X25DteLcnOriginalCalledAddress_Type(DigitString):
    """Custom type x25DteLcnOriginalCalledAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_X25DteLcnOriginalCalledAddress_Type.__name__ = "DigitString"
_X25DteLcnOriginalCalledAddress_Object = MibTableColumn
x25DteLcnOriginalCalledAddress = _X25DteLcnOriginalCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 12, 1, 6),
    _X25DteLcnOriginalCalledAddress_Type()
)
x25DteLcnOriginalCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOriginalCalledAddress.setStatus("mandatory")
_X25DteLcnStatsTable_Object = MibTable
x25DteLcnStatsTable = _X25DteLcnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13)
)
if mibBuilder.loadTexts:
    x25DteLcnStatsTable.setStatus("mandatory")
_X25DteLcnStatsEntry_Object = MibTableRow
x25DteLcnStatsEntry = _X25DteLcnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1)
)
x25DteLcnStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    x25DteLcnStatsEntry.setStatus("mandatory")
_X25DteLcnInUknownProtocols_Type = Counter32
_X25DteLcnInUknownProtocols_Object = MibTableColumn
x25DteLcnInUknownProtocols = _X25DteLcnInUknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 1),
    _X25DteLcnInUknownProtocols_Type()
)
x25DteLcnInUknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInUknownProtocols.setStatus("mandatory")
_X25DteLcnInDataOctets_Type = Counter32
_X25DteLcnInDataOctets_Object = MibTableColumn
x25DteLcnInDataOctets = _X25DteLcnInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 2),
    _X25DteLcnInDataOctets_Type()
)
x25DteLcnInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInDataOctets.setStatus("mandatory")
_X25DteLcnInDataPackets_Type = Counter32
_X25DteLcnInDataPackets_Object = MibTableColumn
x25DteLcnInDataPackets = _X25DteLcnInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 3),
    _X25DteLcnInDataPackets_Type()
)
x25DteLcnInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInDataPackets.setStatus("mandatory")
_X25DteLcnInRmtInitiatedRsts_Type = Counter32
_X25DteLcnInRmtInitiatedRsts_Object = MibTableColumn
x25DteLcnInRmtInitiatedRsts = _X25DteLcnInRmtInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 4),
    _X25DteLcnInRmtInitiatedRsts_Type()
)
x25DteLcnInRmtInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInRmtInitiatedRsts.setStatus("mandatory")
_X25DteLcnInPrvdrInitiatedRsts_Type = Counter32
_X25DteLcnInPrvdrInitiatedRsts_Object = MibTableColumn
x25DteLcnInPrvdrInitiatedRsts = _X25DteLcnInPrvdrInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 5),
    _X25DteLcnInPrvdrInitiatedRsts_Type()
)
x25DteLcnInPrvdrInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInPrvdrInitiatedRsts.setStatus("mandatory")
_X25DteLcnInInterruptPackets_Type = Counter32
_X25DteLcnInInterruptPackets_Object = MibTableColumn
x25DteLcnInInterruptPackets = _X25DteLcnInInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 6),
    _X25DteLcnInInterruptPackets_Type()
)
x25DteLcnInInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnInInterruptPackets.setStatus("mandatory")
_X25DteLcnOutDataOctets_Type = Counter32
_X25DteLcnOutDataOctets_Object = MibTableColumn
x25DteLcnOutDataOctets = _X25DteLcnOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 7),
    _X25DteLcnOutDataOctets_Type()
)
x25DteLcnOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOutDataOctets.setStatus("mandatory")
_X25DteLcnOutDataPackets_Type = Counter32
_X25DteLcnOutDataPackets_Object = MibTableColumn
x25DteLcnOutDataPackets = _X25DteLcnOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 8),
    _X25DteLcnOutDataPackets_Type()
)
x25DteLcnOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOutDataPackets.setStatus("mandatory")
_X25DteLcnOutInterruptPackets_Type = Counter32
_X25DteLcnOutInterruptPackets_Object = MibTableColumn
x25DteLcnOutInterruptPackets = _X25DteLcnOutInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 9),
    _X25DteLcnOutInterruptPackets_Type()
)
x25DteLcnOutInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnOutInterruptPackets.setStatus("mandatory")
_X25DteLcnT22ResetTimeouts_Type = Counter32
_X25DteLcnT22ResetTimeouts_Object = MibTableColumn
x25DteLcnT22ResetTimeouts = _X25DteLcnT22ResetTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 4, 13, 1, 10),
    _X25DteLcnT22ResetTimeouts_Type()
)
x25DteLcnT22ResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLcnT22ResetTimeouts.setStatus("mandatory")
_X25DteLapb_ObjectIdentity = ObjectIdentity
x25DteLapb = _X25DteLapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5)
)
_X25DteLapbRowStatusTable_Object = MibTable
x25DteLapbRowStatusTable = _X25DteLapbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 1)
)
if mibBuilder.loadTexts:
    x25DteLapbRowStatusTable.setStatus("mandatory")
_X25DteLapbRowStatusEntry_Object = MibTableRow
x25DteLapbRowStatusEntry = _X25DteLapbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 1, 1)
)
x25DteLapbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbRowStatusEntry.setStatus("mandatory")
_X25DteLapbRowStatus_Type = RowStatus
_X25DteLapbRowStatus_Object = MibTableColumn
x25DteLapbRowStatus = _X25DteLapbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 1, 1, 1),
    _X25DteLapbRowStatus_Type()
)
x25DteLapbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbRowStatus.setStatus("mandatory")
_X25DteLapbComponentName_Type = DisplayString
_X25DteLapbComponentName_Object = MibTableColumn
x25DteLapbComponentName = _X25DteLapbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 1, 1, 2),
    _X25DteLapbComponentName_Type()
)
x25DteLapbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbComponentName.setStatus("mandatory")
_X25DteLapbStorageType_Type = StorageType
_X25DteLapbStorageType_Object = MibTableColumn
x25DteLapbStorageType = _X25DteLapbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 1, 1, 4),
    _X25DteLapbStorageType_Type()
)
x25DteLapbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbStorageType.setStatus("mandatory")
_X25DteLapbIndex_Type = NonReplicated
_X25DteLapbIndex_Object = MibTableColumn
x25DteLapbIndex = _X25DteLapbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 1, 1, 10),
    _X25DteLapbIndex_Type()
)
x25DteLapbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DteLapbIndex.setStatus("mandatory")
_X25DteLapbFramer_ObjectIdentity = ObjectIdentity
x25DteLapbFramer = _X25DteLapbFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2)
)
_X25DteLapbFramerRowStatusTable_Object = MibTable
x25DteLapbFramerRowStatusTable = _X25DteLapbFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 1)
)
if mibBuilder.loadTexts:
    x25DteLapbFramerRowStatusTable.setStatus("mandatory")
_X25DteLapbFramerRowStatusEntry_Object = MibTableRow
x25DteLapbFramerRowStatusEntry = _X25DteLapbFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 1, 1)
)
x25DteLapbFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbFramerRowStatusEntry.setStatus("mandatory")
_X25DteLapbFramerRowStatus_Type = RowStatus
_X25DteLapbFramerRowStatus_Object = MibTableColumn
x25DteLapbFramerRowStatus = _X25DteLapbFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 1, 1, 1),
    _X25DteLapbFramerRowStatus_Type()
)
x25DteLapbFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerRowStatus.setStatus("mandatory")
_X25DteLapbFramerComponentName_Type = DisplayString
_X25DteLapbFramerComponentName_Object = MibTableColumn
x25DteLapbFramerComponentName = _X25DteLapbFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 1, 1, 2),
    _X25DteLapbFramerComponentName_Type()
)
x25DteLapbFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerComponentName.setStatus("mandatory")
_X25DteLapbFramerStorageType_Type = StorageType
_X25DteLapbFramerStorageType_Object = MibTableColumn
x25DteLapbFramerStorageType = _X25DteLapbFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 1, 1, 4),
    _X25DteLapbFramerStorageType_Type()
)
x25DteLapbFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerStorageType.setStatus("mandatory")
_X25DteLapbFramerIndex_Type = NonReplicated
_X25DteLapbFramerIndex_Object = MibTableColumn
x25DteLapbFramerIndex = _X25DteLapbFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 1, 1, 10),
    _X25DteLapbFramerIndex_Type()
)
x25DteLapbFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DteLapbFramerIndex.setStatus("mandatory")
_X25DteLapbFramerProvTable_Object = MibTable
x25DteLapbFramerProvTable = _X25DteLapbFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 10)
)
if mibBuilder.loadTexts:
    x25DteLapbFramerProvTable.setStatus("mandatory")
_X25DteLapbFramerProvEntry_Object = MibTableRow
x25DteLapbFramerProvEntry = _X25DteLapbFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 10, 1)
)
x25DteLapbFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbFramerProvEntry.setStatus("mandatory")
_X25DteLapbFramerInterfaceName_Type = Link
_X25DteLapbFramerInterfaceName_Object = MibTableColumn
x25DteLapbFramerInterfaceName = _X25DteLapbFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 10, 1, 1),
    _X25DteLapbFramerInterfaceName_Type()
)
x25DteLapbFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbFramerInterfaceName.setStatus("mandatory")
_X25DteLapbFramerLinkTable_Object = MibTable
x25DteLapbFramerLinkTable = _X25DteLapbFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 11)
)
if mibBuilder.loadTexts:
    x25DteLapbFramerLinkTable.setStatus("mandatory")
_X25DteLapbFramerLinkEntry_Object = MibTableRow
x25DteLapbFramerLinkEntry = _X25DteLapbFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 11, 1)
)
x25DteLapbFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbFramerLinkEntry.setStatus("mandatory")


class _X25DteLapbFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type x25DteLapbFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_X25DteLapbFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_X25DteLapbFramerFlagsBetweenFrames_Object = MibTableColumn
x25DteLapbFramerFlagsBetweenFrames = _X25DteLapbFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 11, 1, 4),
    _X25DteLapbFramerFlagsBetweenFrames_Type()
)
x25DteLapbFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbFramerFlagsBetweenFrames.setStatus("mandatory")
_X25DteLapbFramerStateTable_Object = MibTable
x25DteLapbFramerStateTable = _X25DteLapbFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 12)
)
if mibBuilder.loadTexts:
    x25DteLapbFramerStateTable.setStatus("mandatory")
_X25DteLapbFramerStateEntry_Object = MibTableRow
x25DteLapbFramerStateEntry = _X25DteLapbFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 12, 1)
)
x25DteLapbFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbFramerStateEntry.setStatus("mandatory")


class _X25DteLapbFramerAdminState_Type(Integer32):
    """Custom type x25DteLapbFramerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_X25DteLapbFramerAdminState_Type.__name__ = "Integer32"
_X25DteLapbFramerAdminState_Object = MibTableColumn
x25DteLapbFramerAdminState = _X25DteLapbFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 12, 1, 1),
    _X25DteLapbFramerAdminState_Type()
)
x25DteLapbFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerAdminState.setStatus("mandatory")


class _X25DteLapbFramerOperationalState_Type(Integer32):
    """Custom type x25DteLapbFramerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X25DteLapbFramerOperationalState_Type.__name__ = "Integer32"
_X25DteLapbFramerOperationalState_Object = MibTableColumn
x25DteLapbFramerOperationalState = _X25DteLapbFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 12, 1, 2),
    _X25DteLapbFramerOperationalState_Type()
)
x25DteLapbFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerOperationalState.setStatus("mandatory")


class _X25DteLapbFramerUsageState_Type(Integer32):
    """Custom type x25DteLapbFramerUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_X25DteLapbFramerUsageState_Type.__name__ = "Integer32"
_X25DteLapbFramerUsageState_Object = MibTableColumn
x25DteLapbFramerUsageState = _X25DteLapbFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 12, 1, 3),
    _X25DteLapbFramerUsageState_Type()
)
x25DteLapbFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerUsageState.setStatus("mandatory")
_X25DteLapbFramerStatsTable_Object = MibTable
x25DteLapbFramerStatsTable = _X25DteLapbFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13)
)
if mibBuilder.loadTexts:
    x25DteLapbFramerStatsTable.setStatus("mandatory")
_X25DteLapbFramerStatsEntry_Object = MibTableRow
x25DteLapbFramerStatsEntry = _X25DteLapbFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1)
)
x25DteLapbFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbFramerStatsEntry.setStatus("mandatory")
_X25DteLapbFramerFrmToIf_Type = Counter32
_X25DteLapbFramerFrmToIf_Object = MibTableColumn
x25DteLapbFramerFrmToIf = _X25DteLapbFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 1),
    _X25DteLapbFramerFrmToIf_Type()
)
x25DteLapbFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerFrmToIf.setStatus("mandatory")
_X25DteLapbFramerFrmFromIf_Type = Counter32
_X25DteLapbFramerFrmFromIf_Object = MibTableColumn
x25DteLapbFramerFrmFromIf = _X25DteLapbFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 2),
    _X25DteLapbFramerFrmFromIf_Type()
)
x25DteLapbFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerFrmFromIf.setStatus("mandatory")
_X25DteLapbFramerOctetFromIf_Type = Counter32
_X25DteLapbFramerOctetFromIf_Object = MibTableColumn
x25DteLapbFramerOctetFromIf = _X25DteLapbFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 3),
    _X25DteLapbFramerOctetFromIf_Type()
)
x25DteLapbFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerOctetFromIf.setStatus("mandatory")
_X25DteLapbFramerAborts_Type = Counter32
_X25DteLapbFramerAborts_Object = MibTableColumn
x25DteLapbFramerAborts = _X25DteLapbFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 4),
    _X25DteLapbFramerAborts_Type()
)
x25DteLapbFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerAborts.setStatus("mandatory")
_X25DteLapbFramerCrcErrors_Type = Counter32
_X25DteLapbFramerCrcErrors_Object = MibTableColumn
x25DteLapbFramerCrcErrors = _X25DteLapbFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 5),
    _X25DteLapbFramerCrcErrors_Type()
)
x25DteLapbFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerCrcErrors.setStatus("mandatory")
_X25DteLapbFramerLrcErrors_Type = Counter32
_X25DteLapbFramerLrcErrors_Object = MibTableColumn
x25DteLapbFramerLrcErrors = _X25DteLapbFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 6),
    _X25DteLapbFramerLrcErrors_Type()
)
x25DteLapbFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerLrcErrors.setStatus("mandatory")
_X25DteLapbFramerNonOctetErrors_Type = Counter32
_X25DteLapbFramerNonOctetErrors_Object = MibTableColumn
x25DteLapbFramerNonOctetErrors = _X25DteLapbFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 7),
    _X25DteLapbFramerNonOctetErrors_Type()
)
x25DteLapbFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerNonOctetErrors.setStatus("mandatory")
_X25DteLapbFramerOverruns_Type = Counter32
_X25DteLapbFramerOverruns_Object = MibTableColumn
x25DteLapbFramerOverruns = _X25DteLapbFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 8),
    _X25DteLapbFramerOverruns_Type()
)
x25DteLapbFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerOverruns.setStatus("mandatory")
_X25DteLapbFramerUnderruns_Type = Counter32
_X25DteLapbFramerUnderruns_Object = MibTableColumn
x25DteLapbFramerUnderruns = _X25DteLapbFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 13, 1, 9),
    _X25DteLapbFramerUnderruns_Type()
)
x25DteLapbFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerUnderruns.setStatus("mandatory")
_X25DteLapbFramerUtilTable_Object = MibTable
x25DteLapbFramerUtilTable = _X25DteLapbFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 14)
)
if mibBuilder.loadTexts:
    x25DteLapbFramerUtilTable.setStatus("mandatory")
_X25DteLapbFramerUtilEntry_Object = MibTableRow
x25DteLapbFramerUtilEntry = _X25DteLapbFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 14, 1)
)
x25DteLapbFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbFramerUtilEntry.setStatus("mandatory")


class _X25DteLapbFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type x25DteLapbFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_X25DteLapbFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_X25DteLapbFramerNormPrioLinkUtilToIf_Object = MibTableColumn
x25DteLapbFramerNormPrioLinkUtilToIf = _X25DteLapbFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 14, 1, 1),
    _X25DteLapbFramerNormPrioLinkUtilToIf_Type()
)
x25DteLapbFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _X25DteLapbFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type x25DteLapbFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_X25DteLapbFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_X25DteLapbFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
x25DteLapbFramerNormPrioLinkUtilFromIf = _X25DteLapbFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 2, 14, 1, 3),
    _X25DteLapbFramerNormPrioLinkUtilFromIf_Type()
)
x25DteLapbFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_X25DteLapbCpTable_Object = MibTable
x25DteLapbCpTable = _X25DteLapbCpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10)
)
if mibBuilder.loadTexts:
    x25DteLapbCpTable.setStatus("mandatory")
_X25DteLapbCpEntry_Object = MibTableRow
x25DteLapbCpEntry = _X25DteLapbCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1)
)
x25DteLapbCpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbCpEntry.setStatus("mandatory")


class _X25DteLapbStationType_Type(Integer32):
    """Custom type x25DteLapbStationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_X25DteLapbStationType_Type.__name__ = "Integer32"
_X25DteLapbStationType_Object = MibTableColumn
x25DteLapbStationType = _X25DteLapbStationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 1),
    _X25DteLapbStationType_Type()
)
x25DteLapbStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbStationType.setStatus("mandatory")


class _X25DteLapbFrameSequencing_Type(Integer32):
    """Custom type x25DteLapbFrameSequencing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_X25DteLapbFrameSequencing_Type.__name__ = "Integer32"
_X25DteLapbFrameSequencing_Object = MibTableColumn
x25DteLapbFrameSequencing = _X25DteLapbFrameSequencing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 2),
    _X25DteLapbFrameSequencing_Type()
)
x25DteLapbFrameSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbFrameSequencing.setStatus("mandatory")


class _X25DteLapbN1FrameSize_Type(Unsigned32):
    """Custom type x25DteLapbN1FrameSize based on Unsigned32"""
    defaultValue = 32856

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 32856),
    )


_X25DteLapbN1FrameSize_Type.__name__ = "Unsigned32"
_X25DteLapbN1FrameSize_Object = MibTableColumn
x25DteLapbN1FrameSize = _X25DteLapbN1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 3),
    _X25DteLapbN1FrameSize_Type()
)
x25DteLapbN1FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbN1FrameSize.setStatus("mandatory")


class _X25DteLapbKWindowSize_Type(Unsigned32):
    """Custom type x25DteLapbKWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DteLapbKWindowSize_Type.__name__ = "Unsigned32"
_X25DteLapbKWindowSize_Object = MibTableColumn
x25DteLapbKWindowSize = _X25DteLapbKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 4),
    _X25DteLapbKWindowSize_Type()
)
x25DteLapbKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbKWindowSize.setStatus("mandatory")


class _X25DteLapbN2TransmitLimit_Type(Unsigned32):
    """Custom type x25DteLapbN2TransmitLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_X25DteLapbN2TransmitLimit_Type.__name__ = "Unsigned32"
_X25DteLapbN2TransmitLimit_Object = MibTableColumn
x25DteLapbN2TransmitLimit = _X25DteLapbN2TransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 5),
    _X25DteLapbN2TransmitLimit_Type()
)
x25DteLapbN2TransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbN2TransmitLimit.setStatus("mandatory")


class _X25DteLapbT1AckTimer_Type(Unsigned32):
    """Custom type x25DteLapbT1AckTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_X25DteLapbT1AckTimer_Type.__name__ = "Unsigned32"
_X25DteLapbT1AckTimer_Object = MibTableColumn
x25DteLapbT1AckTimer = _X25DteLapbT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 6),
    _X25DteLapbT1AckTimer_Type()
)
x25DteLapbT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbT1AckTimer.setStatus("mandatory")


class _X25DteLapbT2AckDelayTimer_Type(Unsigned32):
    """Custom type x25DteLapbT2AckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_X25DteLapbT2AckDelayTimer_Type.__name__ = "Unsigned32"
_X25DteLapbT2AckDelayTimer_Object = MibTableColumn
x25DteLapbT2AckDelayTimer = _X25DteLapbT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 7),
    _X25DteLapbT2AckDelayTimer_Type()
)
x25DteLapbT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbT2AckDelayTimer.setStatus("mandatory")


class _X25DteLapbT4IdleProbeTimer_Type(Unsigned32):
    """Custom type x25DteLapbT4IdleProbeTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_X25DteLapbT4IdleProbeTimer_Type.__name__ = "Unsigned32"
_X25DteLapbT4IdleProbeTimer_Object = MibTableColumn
x25DteLapbT4IdleProbeTimer = _X25DteLapbT4IdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 8),
    _X25DteLapbT4IdleProbeTimer_Type()
)
x25DteLapbT4IdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbT4IdleProbeTimer.setStatus("mandatory")


class _X25DteLapbActionInitiate_Type(Integer32):
    """Custom type x25DteLapbActionInitiate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 4),
          ("sendDM", 3),
          ("sendSABM", 1))
    )


_X25DteLapbActionInitiate_Type.__name__ = "Integer32"
_X25DteLapbActionInitiate_Object = MibTableColumn
x25DteLapbActionInitiate = _X25DteLapbActionInitiate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 9),
    _X25DteLapbActionInitiate_Type()
)
x25DteLapbActionInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbActionInitiate.setStatus("mandatory")


class _X25DteLapbActionRecvDM_Type(Integer32):
    """Custom type x25DteLapbActionRecvDM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sendSABM", 1)
    )


_X25DteLapbActionRecvDM_Type.__name__ = "Integer32"
_X25DteLapbActionRecvDM_Object = MibTableColumn
x25DteLapbActionRecvDM = _X25DteLapbActionRecvDM_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 10),
    _X25DteLapbActionRecvDM_Type()
)
x25DteLapbActionRecvDM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbActionRecvDM.setStatus("mandatory")


class _X25DteLapbTxQDegradeThreshold_Type(Unsigned32):
    """Custom type x25DteLapbTxQDegradeThreshold based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_X25DteLapbTxQDegradeThreshold_Type.__name__ = "Unsigned32"
_X25DteLapbTxQDegradeThreshold_Object = MibTableColumn
x25DteLapbTxQDegradeThreshold = _X25DteLapbTxQDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 11),
    _X25DteLapbTxQDegradeThreshold_Type()
)
x25DteLapbTxQDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbTxQDegradeThreshold.setStatus("mandatory")


class _X25DteLapbTxQResetThreshold_Type(Unsigned32):
    """Custom type x25DteLapbTxQResetThreshold based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_X25DteLapbTxQResetThreshold_Type.__name__ = "Unsigned32"
_X25DteLapbTxQResetThreshold_Object = MibTableColumn
x25DteLapbTxQResetThreshold = _X25DteLapbTxQResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 10, 1, 12),
    _X25DteLapbTxQResetThreshold_Type()
)
x25DteLapbTxQResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLapbTxQResetThreshold.setStatus("mandatory")
_X25DteLapbStateTable_Object = MibTable
x25DteLapbStateTable = _X25DteLapbStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 11)
)
if mibBuilder.loadTexts:
    x25DteLapbStateTable.setStatus("mandatory")
_X25DteLapbStateEntry_Object = MibTableRow
x25DteLapbStateEntry = _X25DteLapbStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 11, 1)
)
x25DteLapbStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbStateEntry.setStatus("mandatory")


class _X25DteLapbAdminState_Type(Integer32):
    """Custom type x25DteLapbAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_X25DteLapbAdminState_Type.__name__ = "Integer32"
_X25DteLapbAdminState_Object = MibTableColumn
x25DteLapbAdminState = _X25DteLapbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 11, 1, 1),
    _X25DteLapbAdminState_Type()
)
x25DteLapbAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbAdminState.setStatus("mandatory")


class _X25DteLapbOperationalState_Type(Integer32):
    """Custom type x25DteLapbOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X25DteLapbOperationalState_Type.__name__ = "Integer32"
_X25DteLapbOperationalState_Object = MibTableColumn
x25DteLapbOperationalState = _X25DteLapbOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 11, 1, 2),
    _X25DteLapbOperationalState_Type()
)
x25DteLapbOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbOperationalState.setStatus("mandatory")


class _X25DteLapbUsageState_Type(Integer32):
    """Custom type x25DteLapbUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_X25DteLapbUsageState_Type.__name__ = "Integer32"
_X25DteLapbUsageState_Object = MibTableColumn
x25DteLapbUsageState = _X25DteLapbUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 11, 1, 3),
    _X25DteLapbUsageState_Type()
)
x25DteLapbUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbUsageState.setStatus("mandatory")
_X25DteLapbStatusTable_Object = MibTable
x25DteLapbStatusTable = _X25DteLapbStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12)
)
if mibBuilder.loadTexts:
    x25DteLapbStatusTable.setStatus("mandatory")
_X25DteLapbStatusEntry_Object = MibTableRow
x25DteLapbStatusEntry = _X25DteLapbStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12, 1)
)
x25DteLapbStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbStatusEntry.setStatus("mandatory")


class _X25DteLapbCurrentState_Type(Integer32):
    """Custom type x25DteLapbCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disconnectRequest", 4),
          ("disconnected", 1),
          ("frameReject", 3),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("waitingAck", 7))
    )


_X25DteLapbCurrentState_Type.__name__ = "Integer32"
_X25DteLapbCurrentState_Object = MibTableColumn
x25DteLapbCurrentState = _X25DteLapbCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12, 1, 1),
    _X25DteLapbCurrentState_Type()
)
x25DteLapbCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbCurrentState.setStatus("mandatory")


class _X25DteLapbLastStateChangeReason_Type(Integer32):
    """Custom type x25DteLapbLastStateChangeReason based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("abmEntered", 2),
          ("abmReset", 4),
          ("abmeEntered", 3),
          ("abmeReset", 5),
          ("discReceived", 8),
          ("discSent", 9),
          ("dmReceived", 6),
          ("dmSent", 7),
          ("frmrReceived", 10),
          ("frmrSent", 11),
          ("n2TimeOut", 12),
          ("notStarted", 1),
          ("other", 13))
    )


_X25DteLapbLastStateChangeReason_Type.__name__ = "Integer32"
_X25DteLapbLastStateChangeReason_Object = MibTableColumn
x25DteLapbLastStateChangeReason = _X25DteLapbLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12, 1, 2),
    _X25DteLapbLastStateChangeReason_Type()
)
x25DteLapbLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbLastStateChangeReason.setStatus("mandatory")


class _X25DteLapbFrmrTransmit_Type(HexString):
    """Custom type x25DteLapbFrmrTransmit based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_X25DteLapbFrmrTransmit_Type.__name__ = "HexString"
_X25DteLapbFrmrTransmit_Object = MibTableColumn
x25DteLapbFrmrTransmit = _X25DteLapbFrmrTransmit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12, 1, 3),
    _X25DteLapbFrmrTransmit_Type()
)
x25DteLapbFrmrTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFrmrTransmit.setStatus("mandatory")


class _X25DteLapbFrmrReceive_Type(HexString):
    """Custom type x25DteLapbFrmrReceive based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_X25DteLapbFrmrReceive_Type.__name__ = "HexString"
_X25DteLapbFrmrReceive_Object = MibTableColumn
x25DteLapbFrmrReceive = _X25DteLapbFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12, 1, 4),
    _X25DteLapbFrmrReceive_Type()
)
x25DteLapbFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbFrmrReceive.setStatus("mandatory")


class _X25DteLapbCurrentQueueSize_Type(Unsigned32):
    """Custom type x25DteLapbCurrentQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_X25DteLapbCurrentQueueSize_Type.__name__ = "Unsigned32"
_X25DteLapbCurrentQueueSize_Object = MibTableColumn
x25DteLapbCurrentQueueSize = _X25DteLapbCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 12, 1, 5),
    _X25DteLapbCurrentQueueSize_Type()
)
x25DteLapbCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbCurrentQueueSize.setStatus("mandatory")
_X25DteLapbStatsTable_Object = MibTable
x25DteLapbStatsTable = _X25DteLapbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13)
)
if mibBuilder.loadTexts:
    x25DteLapbStatsTable.setStatus("mandatory")
_X25DteLapbStatsEntry_Object = MibTableRow
x25DteLapbStatsEntry = _X25DteLapbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13, 1)
)
x25DteLapbStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    x25DteLapbStatsEntry.setStatus("mandatory")
_X25DteLapbStateChanges_Type = Counter32
_X25DteLapbStateChanges_Object = MibTableColumn
x25DteLapbStateChanges = _X25DteLapbStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13, 1, 1),
    _X25DteLapbStateChanges_Type()
)
x25DteLapbStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbStateChanges.setStatus("mandatory")
_X25DteLapbRemoteBusy_Type = Counter32
_X25DteLapbRemoteBusy_Object = MibTableColumn
x25DteLapbRemoteBusy = _X25DteLapbRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13, 1, 2),
    _X25DteLapbRemoteBusy_Type()
)
x25DteLapbRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbRemoteBusy.setStatus("mandatory")
_X25DteLapbTransmitRejectFrames_Type = Counter32
_X25DteLapbTransmitRejectFrames_Object = MibTableColumn
x25DteLapbTransmitRejectFrames = _X25DteLapbTransmitRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13, 1, 3),
    _X25DteLapbTransmitRejectFrames_Type()
)
x25DteLapbTransmitRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbTransmitRejectFrames.setStatus("mandatory")
_X25DteLapbReceiveRejectFrames_Type = Counter32
_X25DteLapbReceiveRejectFrames_Object = MibTableColumn
x25DteLapbReceiveRejectFrames = _X25DteLapbReceiveRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13, 1, 4),
    _X25DteLapbReceiveRejectFrames_Type()
)
x25DteLapbReceiveRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbReceiveRejectFrames.setStatus("mandatory")
_X25DteLapbT1AckTimeout_Type = Counter32
_X25DteLapbT1AckTimeout_Object = MibTableColumn
x25DteLapbT1AckTimeout = _X25DteLapbT1AckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 5, 13, 1, 5),
    _X25DteLapbT1AckTimeout_Type()
)
x25DteLapbT1AckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteLapbT1AckTimeout.setStatus("mandatory")
_X25DtePle_ObjectIdentity = ObjectIdentity
x25DtePle = _X25DtePle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6)
)
_X25DtePleRowStatusTable_Object = MibTable
x25DtePleRowStatusTable = _X25DtePleRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 1)
)
if mibBuilder.loadTexts:
    x25DtePleRowStatusTable.setStatus("mandatory")
_X25DtePleRowStatusEntry_Object = MibTableRow
x25DtePleRowStatusEntry = _X25DtePleRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 1, 1)
)
x25DtePleRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePleIndex"),
)
if mibBuilder.loadTexts:
    x25DtePleRowStatusEntry.setStatus("mandatory")
_X25DtePleRowStatus_Type = RowStatus
_X25DtePleRowStatus_Object = MibTableColumn
x25DtePleRowStatus = _X25DtePleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 1, 1, 1),
    _X25DtePleRowStatus_Type()
)
x25DtePleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleRowStatus.setStatus("mandatory")
_X25DtePleComponentName_Type = DisplayString
_X25DtePleComponentName_Object = MibTableColumn
x25DtePleComponentName = _X25DtePleComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 1, 1, 2),
    _X25DtePleComponentName_Type()
)
x25DtePleComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleComponentName.setStatus("mandatory")
_X25DtePleStorageType_Type = StorageType
_X25DtePleStorageType_Object = MibTableColumn
x25DtePleStorageType = _X25DtePleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 1, 1, 4),
    _X25DtePleStorageType_Type()
)
x25DtePleStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleStorageType.setStatus("mandatory")
_X25DtePleIndex_Type = NonReplicated
_X25DtePleIndex_Object = MibTableColumn
x25DtePleIndex = _X25DtePleIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 1, 1, 10),
    _X25DtePleIndex_Type()
)
x25DtePleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DtePleIndex.setStatus("mandatory")
_X25DtePleProvTable_Object = MibTable
x25DtePleProvTable = _X25DtePleProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 10)
)
if mibBuilder.loadTexts:
    x25DtePleProvTable.setStatus("mandatory")
_X25DtePleProvEntry_Object = MibTableRow
x25DtePleProvEntry = _X25DtePleProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 10, 1)
)
x25DtePleProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePleIndex"),
)
if mibBuilder.loadTexts:
    x25DtePleProvEntry.setStatus("mandatory")


class _X25DtePleInactivityTimer_Type(Unsigned32):
    """Custom type x25DtePleInactivityTimer based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536000),
    )


_X25DtePleInactivityTimer_Type.__name__ = "Unsigned32"
_X25DtePleInactivityTimer_Object = MibTableColumn
x25DtePleInactivityTimer = _X25DtePleInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 10, 1, 1),
    _X25DtePleInactivityTimer_Type()
)
x25DtePleInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePleInactivityTimer.setStatus("mandatory")
_X25DtePleOpTable_Object = MibTable
x25DtePleOpTable = _X25DtePleOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 11)
)
if mibBuilder.loadTexts:
    x25DtePleOpTable.setStatus("mandatory")
_X25DtePleOpEntry_Object = MibTableRow
x25DtePleOpEntry = _X25DtePleOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 11, 1)
)
x25DtePleOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DtePleIndex"),
)
if mibBuilder.loadTexts:
    x25DtePleOpEntry.setStatus("mandatory")


class _X25DtePleEncAddrToX25LkupFlrs_Type(Unsigned32):
    """Custom type x25DtePleEncAddrToX25LkupFlrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_X25DtePleEncAddrToX25LkupFlrs_Type.__name__ = "Unsigned32"
_X25DtePleEncAddrToX25LkupFlrs_Object = MibTableColumn
x25DtePleEncAddrToX25LkupFlrs = _X25DtePleEncAddrToX25LkupFlrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 11, 1, 1),
    _X25DtePleEncAddrToX25LkupFlrs_Type()
)
x25DtePleEncAddrToX25LkupFlrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleEncAddrToX25LkupFlrs.setStatus("mandatory")


class _X25DtePleLastFailedEncAddr_Type(HexString):
    """Custom type x25DtePleLastFailedEncAddr based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_X25DtePleLastFailedEncAddr_Type.__name__ = "HexString"
_X25DtePleLastFailedEncAddr_Object = MibTableColumn
x25DtePleLastFailedEncAddr = _X25DtePleLastFailedEncAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 11, 1, 2),
    _X25DtePleLastFailedEncAddr_Type()
)
x25DtePleLastFailedEncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleLastFailedEncAddr.setStatus("mandatory")


class _X25DtePleX25AddrToEncLkupFlrs_Type(Unsigned32):
    """Custom type x25DtePleX25AddrToEncLkupFlrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_X25DtePleX25AddrToEncLkupFlrs_Type.__name__ = "Unsigned32"
_X25DtePleX25AddrToEncLkupFlrs_Object = MibTableColumn
x25DtePleX25AddrToEncLkupFlrs = _X25DtePleX25AddrToEncLkupFlrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 11, 1, 4),
    _X25DtePleX25AddrToEncLkupFlrs_Type()
)
x25DtePleX25AddrToEncLkupFlrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleX25AddrToEncLkupFlrs.setStatus("mandatory")


class _X25DtePleLastFailedX25Addr_Type(DigitString):
    """Custom type x25DtePleLastFailedX25Addr based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_X25DtePleLastFailedX25Addr_Type.__name__ = "DigitString"
_X25DtePleLastFailedX25Addr_Object = MibTableColumn
x25DtePleLastFailedX25Addr = _X25DtePleLastFailedX25Addr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 6, 11, 1, 5),
    _X25DtePleLastFailedX25Addr_Type()
)
x25DtePleLastFailedX25Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DtePleLastFailedX25Addr.setStatus("mandatory")
_X25DteRg_ObjectIdentity = ObjectIdentity
x25DteRg = _X25DteRg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7)
)
_X25DteRgRowStatusTable_Object = MibTable
x25DteRgRowStatusTable = _X25DteRgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 1)
)
if mibBuilder.loadTexts:
    x25DteRgRowStatusTable.setStatus("mandatory")
_X25DteRgRowStatusEntry_Object = MibTableRow
x25DteRgRowStatusEntry = _X25DteRgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 1, 1)
)
x25DteRgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
)
if mibBuilder.loadTexts:
    x25DteRgRowStatusEntry.setStatus("mandatory")
_X25DteRgRowStatus_Type = RowStatus
_X25DteRgRowStatus_Object = MibTableColumn
x25DteRgRowStatus = _X25DteRgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 1, 1, 1),
    _X25DteRgRowStatus_Type()
)
x25DteRgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgRowStatus.setStatus("mandatory")
_X25DteRgComponentName_Type = DisplayString
_X25DteRgComponentName_Object = MibTableColumn
x25DteRgComponentName = _X25DteRgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 1, 1, 2),
    _X25DteRgComponentName_Type()
)
x25DteRgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgComponentName.setStatus("mandatory")
_X25DteRgStorageType_Type = StorageType
_X25DteRgStorageType_Object = MibTableColumn
x25DteRgStorageType = _X25DteRgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 1, 1, 4),
    _X25DteRgStorageType_Type()
)
x25DteRgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgStorageType.setStatus("mandatory")


class _X25DteRgIndex_Type(Integer32):
    """Custom type x25DteRgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_X25DteRgIndex_Type.__name__ = "Integer32"
_X25DteRgIndex_Object = MibTableColumn
x25DteRgIndex = _X25DteRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 1, 1, 10),
    _X25DteRgIndex_Type()
)
x25DteRgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x25DteRgIndex.setStatus("mandatory")
_X25DteRgIfEntryTable_Object = MibTable
x25DteRgIfEntryTable = _X25DteRgIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 10)
)
if mibBuilder.loadTexts:
    x25DteRgIfEntryTable.setStatus("mandatory")
_X25DteRgIfEntryEntry_Object = MibTableRow
x25DteRgIfEntryEntry = _X25DteRgIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 10, 1)
)
x25DteRgIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
)
if mibBuilder.loadTexts:
    x25DteRgIfEntryEntry.setStatus("mandatory")


class _X25DteRgIfAdminStatus_Type(Integer32):
    """Custom type x25DteRgIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_X25DteRgIfAdminStatus_Type.__name__ = "Integer32"
_X25DteRgIfAdminStatus_Object = MibTableColumn
x25DteRgIfAdminStatus = _X25DteRgIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 10, 1, 1),
    _X25DteRgIfAdminStatus_Type()
)
x25DteRgIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgIfAdminStatus.setStatus("mandatory")


class _X25DteRgIfIndex_Type(InterfaceIndex):
    """Custom type x25DteRgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_X25DteRgIfIndex_Type.__name__ = "InterfaceIndex"
_X25DteRgIfIndex_Object = MibTableColumn
x25DteRgIfIndex = _X25DteRgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 10, 1, 2),
    _X25DteRgIfIndex_Type()
)
x25DteRgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgIfIndex.setStatus("mandatory")
_X25DteRgProvTable_Object = MibTable
x25DteRgProvTable = _X25DteRgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 11)
)
if mibBuilder.loadTexts:
    x25DteRgProvTable.setStatus("mandatory")
_X25DteRgProvEntry_Object = MibTableRow
x25DteRgProvEntry = _X25DteRgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 11, 1)
)
x25DteRgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
)
if mibBuilder.loadTexts:
    x25DteRgProvEntry.setStatus("mandatory")
_X25DteRgLinkToProtocolPort_Type = Link
_X25DteRgLinkToProtocolPort_Object = MibTableColumn
x25DteRgLinkToProtocolPort = _X25DteRgLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 11, 1, 1),
    _X25DteRgLinkToProtocolPort_Type()
)
x25DteRgLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgLinkToProtocolPort.setStatus("mandatory")


class _X25DteRgLocalAddress_Type(DigitString):
    """Custom type x25DteRgLocalAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_X25DteRgLocalAddress_Type.__name__ = "DigitString"
_X25DteRgLocalAddress_Object = MibTableColumn
x25DteRgLocalAddress = _X25DteRgLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 11, 1, 2),
    _X25DteRgLocalAddress_Type()
)
x25DteRgLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgLocalAddress.setStatus("mandatory")


class _X25DteRgMtuSize_Type(Unsigned32):
    """Custom type x25DteRgMtuSize based on Unsigned32"""
    defaultValue = 1600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 9188),
    )


_X25DteRgMtuSize_Type.__name__ = "Unsigned32"
_X25DteRgMtuSize_Object = MibTableColumn
x25DteRgMtuSize = _X25DteRgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 11, 1, 3),
    _X25DteRgMtuSize_Type()
)
x25DteRgMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgMtuSize.setStatus("mandatory")
_X25DteRgStateTable_Object = MibTable
x25DteRgStateTable = _X25DteRgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 12)
)
if mibBuilder.loadTexts:
    x25DteRgStateTable.setStatus("mandatory")
_X25DteRgStateEntry_Object = MibTableRow
x25DteRgStateEntry = _X25DteRgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 12, 1)
)
x25DteRgStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
)
if mibBuilder.loadTexts:
    x25DteRgStateEntry.setStatus("mandatory")


class _X25DteRgAdminState_Type(Integer32):
    """Custom type x25DteRgAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_X25DteRgAdminState_Type.__name__ = "Integer32"
_X25DteRgAdminState_Object = MibTableColumn
x25DteRgAdminState = _X25DteRgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 12, 1, 1),
    _X25DteRgAdminState_Type()
)
x25DteRgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgAdminState.setStatus("mandatory")


class _X25DteRgOperationalState_Type(Integer32):
    """Custom type x25DteRgOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X25DteRgOperationalState_Type.__name__ = "Integer32"
_X25DteRgOperationalState_Object = MibTableColumn
x25DteRgOperationalState = _X25DteRgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 12, 1, 2),
    _X25DteRgOperationalState_Type()
)
x25DteRgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgOperationalState.setStatus("mandatory")


class _X25DteRgUsageState_Type(Integer32):
    """Custom type x25DteRgUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_X25DteRgUsageState_Type.__name__ = "Integer32"
_X25DteRgUsageState_Object = MibTableColumn
x25DteRgUsageState = _X25DteRgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 12, 1, 3),
    _X25DteRgUsageState_Type()
)
x25DteRgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgUsageState.setStatus("mandatory")
_X25DteRgOperStatusTable_Object = MibTable
x25DteRgOperStatusTable = _X25DteRgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 13)
)
if mibBuilder.loadTexts:
    x25DteRgOperStatusTable.setStatus("mandatory")
_X25DteRgOperStatusEntry_Object = MibTableRow
x25DteRgOperStatusEntry = _X25DteRgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 13, 1)
)
x25DteRgOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
)
if mibBuilder.loadTexts:
    x25DteRgOperStatusEntry.setStatus("mandatory")


class _X25DteRgSnmpOperStatus_Type(Integer32):
    """Custom type x25DteRgSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_X25DteRgSnmpOperStatus_Type.__name__ = "Integer32"
_X25DteRgSnmpOperStatus_Object = MibTableColumn
x25DteRgSnmpOperStatus = _X25DteRgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 13, 1, 1),
    _X25DteRgSnmpOperStatus_Type()
)
x25DteRgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgSnmpOperStatus.setStatus("mandatory")
_X25DteRgLTPlcnTable_Object = MibTable
x25DteRgLTPlcnTable = _X25DteRgLTPlcnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 210)
)
if mibBuilder.loadTexts:
    x25DteRgLTPlcnTable.setStatus("mandatory")
_X25DteRgLTPlcnEntry_Object = MibTableRow
x25DteRgLTPlcnEntry = _X25DteRgLTPlcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 210, 1)
)
x25DteRgLTPlcnEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgLTPlcnValue"),
)
if mibBuilder.loadTexts:
    x25DteRgLTPlcnEntry.setStatus("mandatory")
_X25DteRgLTPlcnValue_Type = Link
_X25DteRgLTPlcnValue_Object = MibTableColumn
x25DteRgLTPlcnValue = _X25DteRgLTPlcnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 210, 1, 1),
    _X25DteRgLTPlcnValue_Type()
)
x25DteRgLTPlcnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgLTPlcnValue.setStatus("mandatory")
_X25DteRgLTPlcnRowStatus_Type = RowStatus
_X25DteRgLTPlcnRowStatus_Object = MibTableColumn
x25DteRgLTPlcnRowStatus = _X25DteRgLTPlcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 210, 1, 2),
    _X25DteRgLTPlcnRowStatus_Type()
)
x25DteRgLTPlcnRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x25DteRgLTPlcnRowStatus.setStatus("mandatory")
_X25DteRgLtPeerTable_Object = MibTable
x25DteRgLtPeerTable = _X25DteRgLtPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 211)
)
if mibBuilder.loadTexts:
    x25DteRgLtPeerTable.setStatus("mandatory")
_X25DteRgLtPeerEntry_Object = MibTableRow
x25DteRgLtPeerEntry = _X25DteRgLtPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 211, 1)
)
x25DteRgLtPeerEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgLtPeerValue"),
)
if mibBuilder.loadTexts:
    x25DteRgLtPeerEntry.setStatus("mandatory")
_X25DteRgLtPeerValue_Type = Link
_X25DteRgLtPeerValue_Object = MibTableColumn
x25DteRgLtPeerValue = _X25DteRgLtPeerValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 211, 1, 1),
    _X25DteRgLtPeerValue_Type()
)
x25DteRgLtPeerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRgLtPeerValue.setStatus("mandatory")
_X25DteRgLtPeerRowStatus_Type = RowStatus
_X25DteRgLtPeerRowStatus_Object = MibTableColumn
x25DteRgLtPeerRowStatus = _X25DteRgLtPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 211, 1, 2),
    _X25DteRgLtPeerRowStatus_Type()
)
x25DteRgLtPeerRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x25DteRgLtPeerRowStatus.setStatus("mandatory")
_X25DteRgLcnTable_Object = MibTable
x25DteRgLcnTable = _X25DteRgLcnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 212)
)
if mibBuilder.loadTexts:
    x25DteRgLcnTable.setStatus("mandatory")
_X25DteRgLcnEntry_Object = MibTableRow
x25DteRgLcnEntry = _X25DteRgLcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 212, 1)
)
x25DteRgLcnEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgIndex"),
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteRgLcnValue"),
)
if mibBuilder.loadTexts:
    x25DteRgLcnEntry.setStatus("mandatory")


class _X25DteRgLcnValue_Type(Integer32):
    """Custom type x25DteRgLcnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25DteRgLcnValue_Type.__name__ = "Integer32"
_X25DteRgLcnValue_Object = MibTableColumn
x25DteRgLcnValue = _X25DteRgLcnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 7, 212, 1, 1),
    _X25DteRgLcnValue_Type()
)
x25DteRgLcnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteRgLcnValue.setStatus("mandatory")
_X25DteCidDataTable_Object = MibTable
x25DteCidDataTable = _X25DteCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 20)
)
if mibBuilder.loadTexts:
    x25DteCidDataTable.setStatus("mandatory")
_X25DteCidDataEntry_Object = MibTableRow
x25DteCidDataEntry = _X25DteCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 20, 1)
)
x25DteCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteCidDataEntry.setStatus("mandatory")


class _X25DteCustomerIdentifier_Type(Unsigned32):
    """Custom type x25DteCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_X25DteCustomerIdentifier_Type.__name__ = "Unsigned32"
_X25DteCustomerIdentifier_Object = MibTableColumn
x25DteCustomerIdentifier = _X25DteCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 20, 1, 1),
    _X25DteCustomerIdentifier_Type()
)
x25DteCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteCustomerIdentifier.setStatus("mandatory")
_X25DteIfTable_Object = MibTable
x25DteIfTable = _X25DteIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21)
)
if mibBuilder.loadTexts:
    x25DteIfTable.setStatus("mandatory")
_X25DteIfEntry_Object = MibTableRow
x25DteIfEntry = _X25DteIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1)
)
x25DteIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteIfEntry.setStatus("mandatory")


class _X25DteInterfaceMode_Type(Integer32):
    """Custom type x25DteInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_X25DteInterfaceMode_Type.__name__ = "Integer32"
_X25DteInterfaceMode_Object = MibTableColumn
x25DteInterfaceMode = _X25DteInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 1),
    _X25DteInterfaceMode_Type()
)
x25DteInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInterfaceMode.setStatus("mandatory")


class _X25DteMaxActiveChannels_Type(Unsigned32):
    """Custom type x25DteMaxActiveChannels based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteMaxActiveChannels_Type.__name__ = "Unsigned32"
_X25DteMaxActiveChannels_Object = MibTableColumn
x25DteMaxActiveChannels = _X25DteMaxActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 2),
    _X25DteMaxActiveChannels_Type()
)
x25DteMaxActiveChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteMaxActiveChannels.setStatus("mandatory")


class _X25DteNumberOfPLcn_Type(Unsigned32):
    """Custom type x25DteNumberOfPLcn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteNumberOfPLcn_Type.__name__ = "Unsigned32"
_X25DteNumberOfPLcn_Object = MibTableColumn
x25DteNumberOfPLcn = _X25DteNumberOfPLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 3),
    _X25DteNumberOfPLcn_Type()
)
x25DteNumberOfPLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteNumberOfPLcn.setStatus("mandatory")


class _X25DtePacketSequencing_Type(Integer32):
    """Custom type x25DtePacketSequencing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_X25DtePacketSequencing_Type.__name__ = "Integer32"
_X25DtePacketSequencing_Object = MibTableColumn
x25DtePacketSequencing = _X25DtePacketSequencing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 4),
    _X25DtePacketSequencing_Type()
)
x25DtePacketSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DtePacketSequencing.setStatus("mandatory")


class _X25DteT20RestartTimer_Type(Unsigned32):
    """Custom type x25DteT20RestartTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_X25DteT20RestartTimer_Type.__name__ = "Unsigned32"
_X25DteT20RestartTimer_Object = MibTableColumn
x25DteT20RestartTimer = _X25DteT20RestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 5),
    _X25DteT20RestartTimer_Type()
)
x25DteT20RestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteT20RestartTimer.setStatus("mandatory")


class _X25DteT21CallTimer_Type(Unsigned32):
    """Custom type x25DteT21CallTimer based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_X25DteT21CallTimer_Type.__name__ = "Unsigned32"
_X25DteT21CallTimer_Object = MibTableColumn
x25DteT21CallTimer = _X25DteT21CallTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 6),
    _X25DteT21CallTimer_Type()
)
x25DteT21CallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteT21CallTimer.setStatus("mandatory")


class _X25DteT22ResetTimer_Type(Unsigned32):
    """Custom type x25DteT22ResetTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_X25DteT22ResetTimer_Type.__name__ = "Unsigned32"
_X25DteT22ResetTimer_Object = MibTableColumn
x25DteT22ResetTimer = _X25DteT22ResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 7),
    _X25DteT22ResetTimer_Type()
)
x25DteT22ResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteT22ResetTimer.setStatus("mandatory")


class _X25DteT23ClearTimer_Type(Unsigned32):
    """Custom type x25DteT23ClearTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_X25DteT23ClearTimer_Type.__name__ = "Unsigned32"
_X25DteT23ClearTimer_Object = MibTableColumn
x25DteT23ClearTimer = _X25DteT23ClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 21, 1, 8),
    _X25DteT23ClearTimer_Type()
)
x25DteT23ClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteT23ClearTimer.setStatus("mandatory")
_X25DteLcnCTable_Object = MibTable
x25DteLcnCTable = _X25DteLcnCTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22)
)
if mibBuilder.loadTexts:
    x25DteLcnCTable.setStatus("mandatory")
_X25DteLcnCEntry_Object = MibTableRow
x25DteLcnCEntry = _X25DteLcnCEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1)
)
x25DteLcnCEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteLcnCEntry.setStatus("mandatory")


class _X25DteLowestILChannelNumber_Type(Unsigned32):
    """Custom type x25DteLowestILChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteLowestILChannelNumber_Type.__name__ = "Unsigned32"
_X25DteLowestILChannelNumber_Object = MibTableColumn
x25DteLowestILChannelNumber = _X25DteLowestILChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1, 1),
    _X25DteLowestILChannelNumber_Type()
)
x25DteLowestILChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLowestILChannelNumber.setStatus("mandatory")


class _X25DteHighestILChannelNumber_Type(Unsigned32):
    """Custom type x25DteHighestILChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteHighestILChannelNumber_Type.__name__ = "Unsigned32"
_X25DteHighestILChannelNumber_Object = MibTableColumn
x25DteHighestILChannelNumber = _X25DteHighestILChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1, 2),
    _X25DteHighestILChannelNumber_Type()
)
x25DteHighestILChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteHighestILChannelNumber.setStatus("mandatory")


class _X25DteLowestTLChannelNumber_Type(Unsigned32):
    """Custom type x25DteLowestTLChannelNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteLowestTLChannelNumber_Type.__name__ = "Unsigned32"
_X25DteLowestTLChannelNumber_Object = MibTableColumn
x25DteLowestTLChannelNumber = _X25DteLowestTLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1, 3),
    _X25DteLowestTLChannelNumber_Type()
)
x25DteLowestTLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLowestTLChannelNumber.setStatus("mandatory")


class _X25DteHighestTLChannelNumber_Type(Unsigned32):
    """Custom type x25DteHighestTLChannelNumber based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteHighestTLChannelNumber_Type.__name__ = "Unsigned32"
_X25DteHighestTLChannelNumber_Object = MibTableColumn
x25DteHighestTLChannelNumber = _X25DteHighestTLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1, 4),
    _X25DteHighestTLChannelNumber_Type()
)
x25DteHighestTLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteHighestTLChannelNumber.setStatus("mandatory")


class _X25DteLowestOLChannelNumber_Type(Unsigned32):
    """Custom type x25DteLowestOLChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteLowestOLChannelNumber_Type.__name__ = "Unsigned32"
_X25DteLowestOLChannelNumber_Object = MibTableColumn
x25DteLowestOLChannelNumber = _X25DteLowestOLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1, 5),
    _X25DteLowestOLChannelNumber_Type()
)
x25DteLowestOLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteLowestOLChannelNumber.setStatus("mandatory")


class _X25DteHighestOLChannelNumber_Type(Unsigned32):
    """Custom type x25DteHighestOLChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25DteHighestOLChannelNumber_Type.__name__ = "Unsigned32"
_X25DteHighestOLChannelNumber_Object = MibTableColumn
x25DteHighestOLChannelNumber = _X25DteHighestOLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 22, 1, 6),
    _X25DteHighestOLChannelNumber_Type()
)
x25DteHighestOLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteHighestOLChannelNumber.setStatus("mandatory")
_X25DteDcpTable_Object = MibTable
x25DteDcpTable = _X25DteDcpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23)
)
if mibBuilder.loadTexts:
    x25DteDcpTable.setStatus("mandatory")
_X25DteDcpEntry_Object = MibTableRow
x25DteDcpEntry = _X25DteDcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1)
)
x25DteDcpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteDcpEntry.setStatus("mandatory")


class _X25DteInPacketSize_Type(Unsigned32):
    """Custom type x25DteInPacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DteInPacketSize_Type.__name__ = "Unsigned32"
_X25DteInPacketSize_Object = MibTableColumn
x25DteInPacketSize = _X25DteInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 1),
    _X25DteInPacketSize_Type()
)
x25DteInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteInPacketSize.setStatus("mandatory")


class _X25DteOutPacketSize_Type(Unsigned32):
    """Custom type x25DteOutPacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_X25DteOutPacketSize_Type.__name__ = "Unsigned32"
_X25DteOutPacketSize_Object = MibTableColumn
x25DteOutPacketSize = _X25DteOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 2),
    _X25DteOutPacketSize_Type()
)
x25DteOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteOutPacketSize.setStatus("mandatory")


class _X25DteInWindowSize_Type(Unsigned32):
    """Custom type x25DteInWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DteInWindowSize_Type.__name__ = "Unsigned32"
_X25DteInWindowSize_Object = MibTableColumn
x25DteInWindowSize = _X25DteInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 3),
    _X25DteInWindowSize_Type()
)
x25DteInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteInWindowSize.setStatus("mandatory")


class _X25DteOutWindowSize_Type(Unsigned32):
    """Custom type x25DteOutWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25DteOutWindowSize_Type.__name__ = "Unsigned32"
_X25DteOutWindowSize_Object = MibTableColumn
x25DteOutWindowSize = _X25DteOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 4),
    _X25DteOutWindowSize_Type()
)
x25DteOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteOutWindowSize.setStatus("mandatory")


class _X25DteAcceptReverseCharging_Type(Integer32):
    """Custom type x25DteAcceptReverseCharging based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("neverAccept", 4),
          ("refuse", 3))
    )


_X25DteAcceptReverseCharging_Type.__name__ = "Integer32"
_X25DteAcceptReverseCharging_Object = MibTableColumn
x25DteAcceptReverseCharging = _X25DteAcceptReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 5),
    _X25DteAcceptReverseCharging_Type()
)
x25DteAcceptReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteAcceptReverseCharging.setStatus("mandatory")


class _X25DteProposeReverseCharging_Type(Integer32):
    """Custom type x25DteProposeReverseCharging based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("reverse", 2))
    )


_X25DteProposeReverseCharging_Type.__name__ = "Integer32"
_X25DteProposeReverseCharging_Object = MibTableColumn
x25DteProposeReverseCharging = _X25DteProposeReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 6),
    _X25DteProposeReverseCharging_Type()
)
x25DteProposeReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteProposeReverseCharging.setStatus("mandatory")


class _X25DteOutThroughputClassSize_Type(Integer32):
    """Custom type x25DteOutThroughputClassSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 7),
          ("n150", 4),
          ("n19200", 11),
          ("n2400", 8),
          ("n300", 5),
          ("n4800", 9),
          ("n48000", 12),
          ("n600", 6),
          ("n64000", 13),
          ("n75", 3),
          ("n9600", 10),
          ("notSpecified", 17))
    )


_X25DteOutThroughputClassSize_Type.__name__ = "Integer32"
_X25DteOutThroughputClassSize_Object = MibTableColumn
x25DteOutThroughputClassSize = _X25DteOutThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 8),
    _X25DteOutThroughputClassSize_Type()
)
x25DteOutThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteOutThroughputClassSize.setStatus("mandatory")


class _X25DteInThroughputClassSize_Type(Integer32):
    """Custom type x25DteInThroughputClassSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 7),
          ("n150", 4),
          ("n19200", 11),
          ("n2400", 8),
          ("n300", 5),
          ("n4800", 9),
          ("n48000", 12),
          ("n600", 6),
          ("n64000", 13),
          ("n75", 3),
          ("n9600", 10),
          ("notSpecified", 17))
    )


_X25DteInThroughputClassSize_Type.__name__ = "Integer32"
_X25DteInThroughputClassSize_Object = MibTableColumn
x25DteInThroughputClassSize = _X25DteInThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 9),
    _X25DteInThroughputClassSize_Type()
)
x25DteInThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteInThroughputClassSize.setStatus("mandatory")


class _X25DteCugIndex_Type(AsciiString):
    """Custom type x25DteCugIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25DteCugIndex_Type.__name__ = "AsciiString"
_X25DteCugIndex_Object = MibTableColumn
x25DteCugIndex = _X25DteCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 10),
    _X25DteCugIndex_Type()
)
x25DteCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteCugIndex.setStatus("mandatory")


class _X25DteCugoaIndex_Type(AsciiString):
    """Custom type x25DteCugoaIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25DteCugoaIndex_Type.__name__ = "AsciiString"
_X25DteCugoaIndex_Object = MibTableColumn
x25DteCugoaIndex = _X25DteCugoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 11),
    _X25DteCugoaIndex_Type()
)
x25DteCugoaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteCugoaIndex.setStatus("mandatory")


class _X25DteChargingInformation_Type(Integer32):
    """Custom type x25DteChargingInformation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notRequested", 3),
          ("notSpecified", 2),
          ("requested", 4))
    )


_X25DteChargingInformation_Type.__name__ = "Integer32"
_X25DteChargingInformation_Object = MibTableColumn
x25DteChargingInformation = _X25DteChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 13),
    _X25DteChargingInformation_Type()
)
x25DteChargingInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteChargingInformation.setStatus("mandatory")


class _X25DteRpoa_Type(AsciiString):
    """Custom type x25DteRpoa based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteRpoa_Type.__name__ = "AsciiString"
_X25DteRpoa_Object = MibTableColumn
x25DteRpoa = _X25DteRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 14),
    _X25DteRpoa_Type()
)
x25DteRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteRpoa.setStatus("mandatory")


class _X25DteTrnstDlySlctnAInd_Type(Unsigned32):
    """Custom type x25DteTrnstDlySlctnAInd based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_X25DteTrnstDlySlctnAInd_Type.__name__ = "Unsigned32"
_X25DteTrnstDlySlctnAInd_Object = MibTableColumn
x25DteTrnstDlySlctnAInd = _X25DteTrnstDlySlctnAInd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 15),
    _X25DteTrnstDlySlctnAInd_Type()
)
x25DteTrnstDlySlctnAInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteTrnstDlySlctnAInd.setStatus("mandatory")


class _X25DteCallingNetworkFax_Type(HexString):
    """Custom type x25DteCallingNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteCallingNetworkFax_Type.__name__ = "HexString"
_X25DteCallingNetworkFax_Object = MibTableColumn
x25DteCallingNetworkFax = _X25DteCallingNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 24),
    _X25DteCallingNetworkFax_Type()
)
x25DteCallingNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteCallingNetworkFax.setStatus("mandatory")


class _X25DteCalledNetworkFax_Type(HexString):
    """Custom type x25DteCalledNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25DteCalledNetworkFax_Type.__name__ = "HexString"
_X25DteCalledNetworkFax_Object = MibTableColumn
x25DteCalledNetworkFax = _X25DteCalledNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 25),
    _X25DteCalledNetworkFax_Type()
)
x25DteCalledNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteCalledNetworkFax.setStatus("mandatory")


class _X25DteCallUserData_Type(HexString):
    """Custom type x25DteCallUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_X25DteCallUserData_Type.__name__ = "HexString"
_X25DteCallUserData_Object = MibTableColumn
x25DteCallUserData = _X25DteCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 23, 1, 26),
    _X25DteCallUserData_Type()
)
x25DteCallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteCallUserData.setStatus("mandatory")
_X25DteIfEntryTable_Object = MibTable
x25DteIfEntryTable = _X25DteIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 24)
)
if mibBuilder.loadTexts:
    x25DteIfEntryTable.setStatus("mandatory")
_X25DteIfEntryEntry_Object = MibTableRow
x25DteIfEntryEntry = _X25DteIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 24, 1)
)
x25DteIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteIfEntryEntry.setStatus("mandatory")


class _X25DteIfAdminStatus_Type(Integer32):
    """Custom type x25DteIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_X25DteIfAdminStatus_Type.__name__ = "Integer32"
_X25DteIfAdminStatus_Object = MibTableColumn
x25DteIfAdminStatus = _X25DteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 24, 1, 1),
    _X25DteIfAdminStatus_Type()
)
x25DteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25DteIfAdminStatus.setStatus("mandatory")


class _X25DteIfIndex_Type(InterfaceIndex):
    """Custom type x25DteIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_X25DteIfIndex_Type.__name__ = "InterfaceIndex"
_X25DteIfIndex_Object = MibTableColumn
x25DteIfIndex = _X25DteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 24, 1, 2),
    _X25DteIfIndex_Type()
)
x25DteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteIfIndex.setStatus("mandatory")
_X25DteStateTable_Object = MibTable
x25DteStateTable = _X25DteStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 25)
)
if mibBuilder.loadTexts:
    x25DteStateTable.setStatus("mandatory")
_X25DteStateEntry_Object = MibTableRow
x25DteStateEntry = _X25DteStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 25, 1)
)
x25DteStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteStateEntry.setStatus("mandatory")


class _X25DteAdminState_Type(Integer32):
    """Custom type x25DteAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_X25DteAdminState_Type.__name__ = "Integer32"
_X25DteAdminState_Object = MibTableColumn
x25DteAdminState = _X25DteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 25, 1, 1),
    _X25DteAdminState_Type()
)
x25DteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteAdminState.setStatus("mandatory")


class _X25DteOperationalState_Type(Integer32):
    """Custom type x25DteOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X25DteOperationalState_Type.__name__ = "Integer32"
_X25DteOperationalState_Object = MibTableColumn
x25DteOperationalState = _X25DteOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 25, 1, 2),
    _X25DteOperationalState_Type()
)
x25DteOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteOperationalState.setStatus("mandatory")


class _X25DteUsageState_Type(Integer32):
    """Custom type x25DteUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_X25DteUsageState_Type.__name__ = "Integer32"
_X25DteUsageState_Object = MibTableColumn
x25DteUsageState = _X25DteUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 25, 1, 3),
    _X25DteUsageState_Type()
)
x25DteUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteUsageState.setStatus("mandatory")
_X25DteOperStatusTable_Object = MibTable
x25DteOperStatusTable = _X25DteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 26)
)
if mibBuilder.loadTexts:
    x25DteOperStatusTable.setStatus("mandatory")
_X25DteOperStatusEntry_Object = MibTableRow
x25DteOperStatusEntry = _X25DteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 26, 1)
)
x25DteOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteOperStatusEntry.setStatus("mandatory")


class _X25DteSnmpOperStatus_Type(Integer32):
    """Custom type x25DteSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_X25DteSnmpOperStatus_Type.__name__ = "Integer32"
_X25DteSnmpOperStatus_Object = MibTableColumn
x25DteSnmpOperStatus = _X25DteSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 26, 1, 1),
    _X25DteSnmpOperStatus_Type()
)
x25DteSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteSnmpOperStatus.setStatus("mandatory")
_X25DteOpTable_Object = MibTable
x25DteOpTable = _X25DteOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 27)
)
if mibBuilder.loadTexts:
    x25DteOpTable.setStatus("mandatory")
_X25DteOpEntry_Object = MibTableRow
x25DteOpEntry = _X25DteOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 27, 1)
)
x25DteOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteOpEntry.setStatus("mandatory")


class _X25DteInterfaceState_Type(Integer32):
    """Custom type x25DteInterfaceState based on Integer32"""
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
        *(("localRestarting", 1),
          ("notReady", 0),
          ("ready", 3),
          ("remoteRestarting", 2))
    )


_X25DteInterfaceState_Type.__name__ = "Integer32"
_X25DteInterfaceState_Object = MibTableColumn
x25DteInterfaceState = _X25DteInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 27, 1, 1),
    _X25DteInterfaceState_Type()
)
x25DteInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInterfaceState.setStatus("mandatory")
_X25DteStatsTable_Object = MibTable
x25DteStatsTable = _X25DteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28)
)
if mibBuilder.loadTexts:
    x25DteStatsTable.setStatus("mandatory")
_X25DteStatsEntry_Object = MibTableRow
x25DteStatsEntry = _X25DteStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1)
)
x25DteStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-X25DteMIB", "x25DteIndex"),
)
if mibBuilder.loadTexts:
    x25DteStatsEntry.setStatus("mandatory")
_X25DteInCalls_Type = Counter32
_X25DteInCalls_Object = MibTableColumn
x25DteInCalls = _X25DteInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 1),
    _X25DteInCalls_Type()
)
x25DteInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInCalls.setStatus("mandatory")
_X25DteInCallRefusals_Type = Counter32
_X25DteInCallRefusals_Object = MibTableColumn
x25DteInCallRefusals = _X25DteInCallRefusals_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 2),
    _X25DteInCallRefusals_Type()
)
x25DteInCallRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInCallRefusals.setStatus("mandatory")
_X25DteInPrvdrInitiatedClrs_Type = Counter32
_X25DteInPrvdrInitiatedClrs_Object = MibTableColumn
x25DteInPrvdrInitiatedClrs = _X25DteInPrvdrInitiatedClrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 3),
    _X25DteInPrvdrInitiatedClrs_Type()
)
x25DteInPrvdrInitiatedClrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInPrvdrInitiatedClrs.setStatus("mandatory")
_X25DteInRmtInitiatedRsts_Type = Counter32
_X25DteInRmtInitiatedRsts_Object = MibTableColumn
x25DteInRmtInitiatedRsts = _X25DteInRmtInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 4),
    _X25DteInRmtInitiatedRsts_Type()
)
x25DteInRmtInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInRmtInitiatedRsts.setStatus("mandatory")
_X25DteInPrvdrInitiatedRsts_Type = Counter32
_X25DteInPrvdrInitiatedRsts_Object = MibTableColumn
x25DteInPrvdrInitiatedRsts = _X25DteInPrvdrInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 5),
    _X25DteInPrvdrInitiatedRsts_Type()
)
x25DteInPrvdrInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInPrvdrInitiatedRsts.setStatus("mandatory")
_X25DteInRestarts_Type = Counter32
_X25DteInRestarts_Object = MibTableColumn
x25DteInRestarts = _X25DteInRestarts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 6),
    _X25DteInRestarts_Type()
)
x25DteInRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInRestarts.setStatus("mandatory")
_X25DteInDataPackets_Type = Counter32
_X25DteInDataPackets_Object = MibTableColumn
x25DteInDataPackets = _X25DteInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 7),
    _X25DteInDataPackets_Type()
)
x25DteInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInDataPackets.setStatus("mandatory")
_X25DteInPktsAcusdOfPrtclErr_Type = Counter32
_X25DteInPktsAcusdOfPrtclErr_Object = MibTableColumn
x25DteInPktsAcusdOfPrtclErr = _X25DteInPktsAcusdOfPrtclErr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 8),
    _X25DteInPktsAcusdOfPrtclErr_Type()
)
x25DteInPktsAcusdOfPrtclErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInPktsAcusdOfPrtclErr.setStatus("mandatory")
_X25DteInInterruptPackets_Type = Counter32
_X25DteInInterruptPackets_Object = MibTableColumn
x25DteInInterruptPackets = _X25DteInInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 9),
    _X25DteInInterruptPackets_Type()
)
x25DteInInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInInterruptPackets.setStatus("mandatory")
_X25DteOutCallAttempts_Type = Counter32
_X25DteOutCallAttempts_Object = MibTableColumn
x25DteOutCallAttempts = _X25DteOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 10),
    _X25DteOutCallAttempts_Type()
)
x25DteOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteOutCallAttempts.setStatus("mandatory")
_X25DteOutCallFailures_Type = Counter32
_X25DteOutCallFailures_Object = MibTableColumn
x25DteOutCallFailures = _X25DteOutCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 11),
    _X25DteOutCallFailures_Type()
)
x25DteOutCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteOutCallFailures.setStatus("mandatory")
_X25DteOutInterruptPackets_Type = Counter32
_X25DteOutInterruptPackets_Object = MibTableColumn
x25DteOutInterruptPackets = _X25DteOutInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 12),
    _X25DteOutInterruptPackets_Type()
)
x25DteOutInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteOutInterruptPackets.setStatus("mandatory")
_X25DteOutDataPackets_Type = Counter32
_X25DteOutDataPackets_Object = MibTableColumn
x25DteOutDataPackets = _X25DteOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 13),
    _X25DteOutDataPackets_Type()
)
x25DteOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteOutDataPackets.setStatus("mandatory")
_X25DteOutActiveChannels_Type = Counter32
_X25DteOutActiveChannels_Object = MibTableColumn
x25DteOutActiveChannels = _X25DteOutActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 14),
    _X25DteOutActiveChannels_Type()
)
x25DteOutActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteOutActiveChannels.setStatus("mandatory")
_X25DteInActiveChannels_Type = Counter32
_X25DteInActiveChannels_Object = MibTableColumn
x25DteInActiveChannels = _X25DteInActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 15),
    _X25DteInActiveChannels_Type()
)
x25DteInActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteInActiveChannels.setStatus("mandatory")
_X25DteTwowayActiveChannels_Type = Counter32
_X25DteTwowayActiveChannels_Object = MibTableColumn
x25DteTwowayActiveChannels = _X25DteTwowayActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 16),
    _X25DteTwowayActiveChannels_Type()
)
x25DteTwowayActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteTwowayActiveChannels.setStatus("mandatory")
_X25DteT20RestartTimeouts_Type = Counter32
_X25DteT20RestartTimeouts_Object = MibTableColumn
x25DteT20RestartTimeouts = _X25DteT20RestartTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 17),
    _X25DteT20RestartTimeouts_Type()
)
x25DteT20RestartTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteT20RestartTimeouts.setStatus("mandatory")
_X25DteT21CallTimeouts_Type = Counter32
_X25DteT21CallTimeouts_Object = MibTableColumn
x25DteT21CallTimeouts = _X25DteT21CallTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 18),
    _X25DteT21CallTimeouts_Type()
)
x25DteT21CallTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteT21CallTimeouts.setStatus("mandatory")
_X25DteT22ResetTimeouts_Type = Counter32
_X25DteT22ResetTimeouts_Object = MibTableColumn
x25DteT22ResetTimeouts = _X25DteT22ResetTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 19),
    _X25DteT22ResetTimeouts_Type()
)
x25DteT22ResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteT22ResetTimeouts.setStatus("mandatory")
_X25DteT23ClearTimeouts_Type = Counter32
_X25DteT23ClearTimeouts_Object = MibTableColumn
x25DteT23ClearTimeouts = _X25DteT23ClearTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 90, 28, 1, 20),
    _X25DteT23ClearTimeouts_Type()
)
x25DteT23ClearTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DteT23ClearTimeouts.setStatus("mandatory")
_X25DteMIB_ObjectIdentity = ObjectIdentity
x25DteMIB = _X25DteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48)
)
_X25DteGroup_ObjectIdentity = ObjectIdentity
x25DteGroup = _X25DteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 1)
)
_X25DteGroupBE_ObjectIdentity = ObjectIdentity
x25DteGroupBE = _X25DteGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 1, 5)
)
_X25DteGroupBE00_ObjectIdentity = ObjectIdentity
x25DteGroupBE00 = _X25DteGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 1, 5, 1)
)
_X25DteGroupBE00A_ObjectIdentity = ObjectIdentity
x25DteGroupBE00A = _X25DteGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 1, 5, 1, 2)
)
_X25DteCapabilities_ObjectIdentity = ObjectIdentity
x25DteCapabilities = _X25DteCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 3)
)
_X25DteCapabilitiesBE_ObjectIdentity = ObjectIdentity
x25DteCapabilitiesBE = _X25DteCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 3, 5)
)
_X25DteCapabilitiesBE00_ObjectIdentity = ObjectIdentity
x25DteCapabilitiesBE00 = _X25DteCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 3, 5, 1)
)
_X25DteCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
x25DteCapabilitiesBE00A = _X25DteCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 48, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-X25DteMIB",
    **{"x25Dte": x25Dte,
       "x25DteRowStatusTable": x25DteRowStatusTable,
       "x25DteRowStatusEntry": x25DteRowStatusEntry,
       "x25DteRowStatus": x25DteRowStatus,
       "x25DteComponentName": x25DteComponentName,
       "x25DteStorageType": x25DteStorageType,
       "x25DteIndex": x25DteIndex,
       "x25DtePeer": x25DtePeer,
       "x25DtePeerRowStatusTable": x25DtePeerRowStatusTable,
       "x25DtePeerRowStatusEntry": x25DtePeerRowStatusEntry,
       "x25DtePeerRowStatus": x25DtePeerRowStatus,
       "x25DtePeerComponentName": x25DtePeerComponentName,
       "x25DtePeerStorageType": x25DtePeerStorageType,
       "x25DtePeerIndex": x25DtePeerIndex,
       "x25DtePeerIfTable": x25DtePeerIfTable,
       "x25DtePeerIfEntry": x25DtePeerIfEntry,
       "x25DtePeerEncAddressType": x25DtePeerEncAddressType,
       "x25DtePeerEncAddress": x25DtePeerEncAddress,
       "x25DtePeerX25Address": x25DtePeerX25Address,
       "x25DtePeerLinkToRemoteGroup": x25DtePeerLinkToRemoteGroup,
       "x25DtePeerCpTable": x25DtePeerCpTable,
       "x25DtePeerCpEntry": x25DtePeerCpEntry,
       "x25DtePeerInPacketSize": x25DtePeerInPacketSize,
       "x25DtePeerOutPacketSize": x25DtePeerOutPacketSize,
       "x25DtePeerInWindowSize": x25DtePeerInWindowSize,
       "x25DtePeerOutWindowSize": x25DtePeerOutWindowSize,
       "x25DtePeerAcceptReverseCharging": x25DtePeerAcceptReverseCharging,
       "x25DtePeerProposeReverseCharging": x25DtePeerProposeReverseCharging,
       "x25DtePeerOutThroughputClassSize": x25DtePeerOutThroughputClassSize,
       "x25DtePeerInThroughputClassSize": x25DtePeerInThroughputClassSize,
       "x25DtePeerCugIndex": x25DtePeerCugIndex,
       "x25DtePeerCugoaIndex": x25DtePeerCugoaIndex,
       "x25DtePeerNetworkUserIdentifier": x25DtePeerNetworkUserIdentifier,
       "x25DtePeerChargingInformation": x25DtePeerChargingInformation,
       "x25DtePeerRpoa": x25DtePeerRpoa,
       "x25DtePeerTrnstDlySlctnAInd": x25DtePeerTrnstDlySlctnAInd,
       "x25DtePeerCallingNetworkFax": x25DtePeerCallingNetworkFax,
       "x25DtePeerCalledNetworkFax": x25DtePeerCalledNetworkFax,
       "x25DtePeerCallUserData": x25DtePeerCallUserData,
       "x25DtePeerPEncTable": x25DtePeerPEncTable,
       "x25DtePeerPEncEntry": x25DtePeerPEncEntry,
       "x25DtePeerPEncIndex": x25DtePeerPEncIndex,
       "x25DtePeerPEncValue": x25DtePeerPEncValue,
       "x25DtePeerPEncRowStatus": x25DtePeerPEncRowStatus,
       "x25DtePeerLcnTable": x25DtePeerLcnTable,
       "x25DtePeerLcnEntry": x25DtePeerLcnEntry,
       "x25DtePeerLcnValue": x25DtePeerLcnValue,
       "x25DtePLcn": x25DtePLcn,
       "x25DtePLcnRowStatusTable": x25DtePLcnRowStatusTable,
       "x25DtePLcnRowStatusEntry": x25DtePLcnRowStatusEntry,
       "x25DtePLcnRowStatus": x25DtePLcnRowStatus,
       "x25DtePLcnComponentName": x25DtePLcnComponentName,
       "x25DtePLcnStorageType": x25DtePLcnStorageType,
       "x25DtePLcnIndex": x25DtePLcnIndex,
       "x25DtePLcnProvTable": x25DtePLcnProvTable,
       "x25DtePLcnProvEntry": x25DtePLcnProvEntry,
       "x25DtePLcnEncAddressType": x25DtePLcnEncAddressType,
       "x25DtePLcnEncAddress": x25DtePLcnEncAddress,
       "x25DtePLcnProtocolEncType": x25DtePLcnProtocolEncType,
       "x25DtePLcnLinkToRemoteGroup": x25DtePLcnLinkToRemoteGroup,
       "x25DtePLcnInPacketSize": x25DtePLcnInPacketSize,
       "x25DtePLcnOutPacketSize": x25DtePLcnOutPacketSize,
       "x25DtePLcnInWindowSize": x25DtePLcnInWindowSize,
       "x25DtePLcnOutWindowSize": x25DtePLcnOutWindowSize,
       "x25DteLcn": x25DteLcn,
       "x25DteLcnRowStatusTable": x25DteLcnRowStatusTable,
       "x25DteLcnRowStatusEntry": x25DteLcnRowStatusEntry,
       "x25DteLcnRowStatus": x25DteLcnRowStatus,
       "x25DteLcnComponentName": x25DteLcnComponentName,
       "x25DteLcnStorageType": x25DteLcnStorageType,
       "x25DteLcnIndex": x25DteLcnIndex,
       "x25DteLcnStateTable": x25DteLcnStateTable,
       "x25DteLcnStateEntry": x25DteLcnStateEntry,
       "x25DteLcnAdminState": x25DteLcnAdminState,
       "x25DteLcnOperationalState": x25DteLcnOperationalState,
       "x25DteLcnUsageState": x25DteLcnUsageState,
       "x25DteLcnCpTable": x25DteLcnCpTable,
       "x25DteLcnCpEntry": x25DteLcnCpEntry,
       "x25DteLcnInPacketSize": x25DteLcnInPacketSize,
       "x25DteLcnOutPacketSize": x25DteLcnOutPacketSize,
       "x25DteLcnInWindowSize": x25DteLcnInWindowSize,
       "x25DteLcnOutWindowSize": x25DteLcnOutWindowSize,
       "x25DteLcnProposeReverseCharging": x25DteLcnProposeReverseCharging,
       "x25DteLcnFastSelect": x25DteLcnFastSelect,
       "x25DteLcnOutThroughputClassSize": x25DteLcnOutThroughputClassSize,
       "x25DteLcnInThroughputClassSize": x25DteLcnInThroughputClassSize,
       "x25DteLcnCugIndex": x25DteLcnCugIndex,
       "x25DteLcnCugoaIndex": x25DteLcnCugoaIndex,
       "x25DteLcnNetworkUserIdentifier": x25DteLcnNetworkUserIdentifier,
       "x25DteLcnChargingInformation": x25DteLcnChargingInformation,
       "x25DteLcnRpoa": x25DteLcnRpoa,
       "x25DteLcnTrnstDlySlctnAInd": x25DteLcnTrnstDlySlctnAInd,
       "x25DteLcnCallingNetworkFax": x25DteLcnCallingNetworkFax,
       "x25DteLcnCalledNetworkFax": x25DteLcnCalledNetworkFax,
       "x25DteLcnCallUserData": x25DteLcnCallUserData,
       "x25DteLcnLcnStatusTable": x25DteLcnLcnStatusTable,
       "x25DteLcnLcnStatusEntry": x25DteLcnLcnStatusEntry,
       "x25DteLcnStatus": x25DteLcnStatus,
       "x25DteLcnCallDirection": x25DteLcnCallDirection,
       "x25DteLcnCalledAddress": x25DteLcnCalledAddress,
       "x25DteLcnCallingAddress": x25DteLcnCallingAddress,
       "x25DteLcnOriginalCalledAddress": x25DteLcnOriginalCalledAddress,
       "x25DteLcnStatsTable": x25DteLcnStatsTable,
       "x25DteLcnStatsEntry": x25DteLcnStatsEntry,
       "x25DteLcnInUknownProtocols": x25DteLcnInUknownProtocols,
       "x25DteLcnInDataOctets": x25DteLcnInDataOctets,
       "x25DteLcnInDataPackets": x25DteLcnInDataPackets,
       "x25DteLcnInRmtInitiatedRsts": x25DteLcnInRmtInitiatedRsts,
       "x25DteLcnInPrvdrInitiatedRsts": x25DteLcnInPrvdrInitiatedRsts,
       "x25DteLcnInInterruptPackets": x25DteLcnInInterruptPackets,
       "x25DteLcnOutDataOctets": x25DteLcnOutDataOctets,
       "x25DteLcnOutDataPackets": x25DteLcnOutDataPackets,
       "x25DteLcnOutInterruptPackets": x25DteLcnOutInterruptPackets,
       "x25DteLcnT22ResetTimeouts": x25DteLcnT22ResetTimeouts,
       "x25DteLapb": x25DteLapb,
       "x25DteLapbRowStatusTable": x25DteLapbRowStatusTable,
       "x25DteLapbRowStatusEntry": x25DteLapbRowStatusEntry,
       "x25DteLapbRowStatus": x25DteLapbRowStatus,
       "x25DteLapbComponentName": x25DteLapbComponentName,
       "x25DteLapbStorageType": x25DteLapbStorageType,
       "x25DteLapbIndex": x25DteLapbIndex,
       "x25DteLapbFramer": x25DteLapbFramer,
       "x25DteLapbFramerRowStatusTable": x25DteLapbFramerRowStatusTable,
       "x25DteLapbFramerRowStatusEntry": x25DteLapbFramerRowStatusEntry,
       "x25DteLapbFramerRowStatus": x25DteLapbFramerRowStatus,
       "x25DteLapbFramerComponentName": x25DteLapbFramerComponentName,
       "x25DteLapbFramerStorageType": x25DteLapbFramerStorageType,
       "x25DteLapbFramerIndex": x25DteLapbFramerIndex,
       "x25DteLapbFramerProvTable": x25DteLapbFramerProvTable,
       "x25DteLapbFramerProvEntry": x25DteLapbFramerProvEntry,
       "x25DteLapbFramerInterfaceName": x25DteLapbFramerInterfaceName,
       "x25DteLapbFramerLinkTable": x25DteLapbFramerLinkTable,
       "x25DteLapbFramerLinkEntry": x25DteLapbFramerLinkEntry,
       "x25DteLapbFramerFlagsBetweenFrames": x25DteLapbFramerFlagsBetweenFrames,
       "x25DteLapbFramerStateTable": x25DteLapbFramerStateTable,
       "x25DteLapbFramerStateEntry": x25DteLapbFramerStateEntry,
       "x25DteLapbFramerAdminState": x25DteLapbFramerAdminState,
       "x25DteLapbFramerOperationalState": x25DteLapbFramerOperationalState,
       "x25DteLapbFramerUsageState": x25DteLapbFramerUsageState,
       "x25DteLapbFramerStatsTable": x25DteLapbFramerStatsTable,
       "x25DteLapbFramerStatsEntry": x25DteLapbFramerStatsEntry,
       "x25DteLapbFramerFrmToIf": x25DteLapbFramerFrmToIf,
       "x25DteLapbFramerFrmFromIf": x25DteLapbFramerFrmFromIf,
       "x25DteLapbFramerOctetFromIf": x25DteLapbFramerOctetFromIf,
       "x25DteLapbFramerAborts": x25DteLapbFramerAborts,
       "x25DteLapbFramerCrcErrors": x25DteLapbFramerCrcErrors,
       "x25DteLapbFramerLrcErrors": x25DteLapbFramerLrcErrors,
       "x25DteLapbFramerNonOctetErrors": x25DteLapbFramerNonOctetErrors,
       "x25DteLapbFramerOverruns": x25DteLapbFramerOverruns,
       "x25DteLapbFramerUnderruns": x25DteLapbFramerUnderruns,
       "x25DteLapbFramerUtilTable": x25DteLapbFramerUtilTable,
       "x25DteLapbFramerUtilEntry": x25DteLapbFramerUtilEntry,
       "x25DteLapbFramerNormPrioLinkUtilToIf": x25DteLapbFramerNormPrioLinkUtilToIf,
       "x25DteLapbFramerNormPrioLinkUtilFromIf": x25DteLapbFramerNormPrioLinkUtilFromIf,
       "x25DteLapbCpTable": x25DteLapbCpTable,
       "x25DteLapbCpEntry": x25DteLapbCpEntry,
       "x25DteLapbStationType": x25DteLapbStationType,
       "x25DteLapbFrameSequencing": x25DteLapbFrameSequencing,
       "x25DteLapbN1FrameSize": x25DteLapbN1FrameSize,
       "x25DteLapbKWindowSize": x25DteLapbKWindowSize,
       "x25DteLapbN2TransmitLimit": x25DteLapbN2TransmitLimit,
       "x25DteLapbT1AckTimer": x25DteLapbT1AckTimer,
       "x25DteLapbT2AckDelayTimer": x25DteLapbT2AckDelayTimer,
       "x25DteLapbT4IdleProbeTimer": x25DteLapbT4IdleProbeTimer,
       "x25DteLapbActionInitiate": x25DteLapbActionInitiate,
       "x25DteLapbActionRecvDM": x25DteLapbActionRecvDM,
       "x25DteLapbTxQDegradeThreshold": x25DteLapbTxQDegradeThreshold,
       "x25DteLapbTxQResetThreshold": x25DteLapbTxQResetThreshold,
       "x25DteLapbStateTable": x25DteLapbStateTable,
       "x25DteLapbStateEntry": x25DteLapbStateEntry,
       "x25DteLapbAdminState": x25DteLapbAdminState,
       "x25DteLapbOperationalState": x25DteLapbOperationalState,
       "x25DteLapbUsageState": x25DteLapbUsageState,
       "x25DteLapbStatusTable": x25DteLapbStatusTable,
       "x25DteLapbStatusEntry": x25DteLapbStatusEntry,
       "x25DteLapbCurrentState": x25DteLapbCurrentState,
       "x25DteLapbLastStateChangeReason": x25DteLapbLastStateChangeReason,
       "x25DteLapbFrmrTransmit": x25DteLapbFrmrTransmit,
       "x25DteLapbFrmrReceive": x25DteLapbFrmrReceive,
       "x25DteLapbCurrentQueueSize": x25DteLapbCurrentQueueSize,
       "x25DteLapbStatsTable": x25DteLapbStatsTable,
       "x25DteLapbStatsEntry": x25DteLapbStatsEntry,
       "x25DteLapbStateChanges": x25DteLapbStateChanges,
       "x25DteLapbRemoteBusy": x25DteLapbRemoteBusy,
       "x25DteLapbTransmitRejectFrames": x25DteLapbTransmitRejectFrames,
       "x25DteLapbReceiveRejectFrames": x25DteLapbReceiveRejectFrames,
       "x25DteLapbT1AckTimeout": x25DteLapbT1AckTimeout,
       "x25DtePle": x25DtePle,
       "x25DtePleRowStatusTable": x25DtePleRowStatusTable,
       "x25DtePleRowStatusEntry": x25DtePleRowStatusEntry,
       "x25DtePleRowStatus": x25DtePleRowStatus,
       "x25DtePleComponentName": x25DtePleComponentName,
       "x25DtePleStorageType": x25DtePleStorageType,
       "x25DtePleIndex": x25DtePleIndex,
       "x25DtePleProvTable": x25DtePleProvTable,
       "x25DtePleProvEntry": x25DtePleProvEntry,
       "x25DtePleInactivityTimer": x25DtePleInactivityTimer,
       "x25DtePleOpTable": x25DtePleOpTable,
       "x25DtePleOpEntry": x25DtePleOpEntry,
       "x25DtePleEncAddrToX25LkupFlrs": x25DtePleEncAddrToX25LkupFlrs,
       "x25DtePleLastFailedEncAddr": x25DtePleLastFailedEncAddr,
       "x25DtePleX25AddrToEncLkupFlrs": x25DtePleX25AddrToEncLkupFlrs,
       "x25DtePleLastFailedX25Addr": x25DtePleLastFailedX25Addr,
       "x25DteRg": x25DteRg,
       "x25DteRgRowStatusTable": x25DteRgRowStatusTable,
       "x25DteRgRowStatusEntry": x25DteRgRowStatusEntry,
       "x25DteRgRowStatus": x25DteRgRowStatus,
       "x25DteRgComponentName": x25DteRgComponentName,
       "x25DteRgStorageType": x25DteRgStorageType,
       "x25DteRgIndex": x25DteRgIndex,
       "x25DteRgIfEntryTable": x25DteRgIfEntryTable,
       "x25DteRgIfEntryEntry": x25DteRgIfEntryEntry,
       "x25DteRgIfAdminStatus": x25DteRgIfAdminStatus,
       "x25DteRgIfIndex": x25DteRgIfIndex,
       "x25DteRgProvTable": x25DteRgProvTable,
       "x25DteRgProvEntry": x25DteRgProvEntry,
       "x25DteRgLinkToProtocolPort": x25DteRgLinkToProtocolPort,
       "x25DteRgLocalAddress": x25DteRgLocalAddress,
       "x25DteRgMtuSize": x25DteRgMtuSize,
       "x25DteRgStateTable": x25DteRgStateTable,
       "x25DteRgStateEntry": x25DteRgStateEntry,
       "x25DteRgAdminState": x25DteRgAdminState,
       "x25DteRgOperationalState": x25DteRgOperationalState,
       "x25DteRgUsageState": x25DteRgUsageState,
       "x25DteRgOperStatusTable": x25DteRgOperStatusTable,
       "x25DteRgOperStatusEntry": x25DteRgOperStatusEntry,
       "x25DteRgSnmpOperStatus": x25DteRgSnmpOperStatus,
       "x25DteRgLTPlcnTable": x25DteRgLTPlcnTable,
       "x25DteRgLTPlcnEntry": x25DteRgLTPlcnEntry,
       "x25DteRgLTPlcnValue": x25DteRgLTPlcnValue,
       "x25DteRgLTPlcnRowStatus": x25DteRgLTPlcnRowStatus,
       "x25DteRgLtPeerTable": x25DteRgLtPeerTable,
       "x25DteRgLtPeerEntry": x25DteRgLtPeerEntry,
       "x25DteRgLtPeerValue": x25DteRgLtPeerValue,
       "x25DteRgLtPeerRowStatus": x25DteRgLtPeerRowStatus,
       "x25DteRgLcnTable": x25DteRgLcnTable,
       "x25DteRgLcnEntry": x25DteRgLcnEntry,
       "x25DteRgLcnValue": x25DteRgLcnValue,
       "x25DteCidDataTable": x25DteCidDataTable,
       "x25DteCidDataEntry": x25DteCidDataEntry,
       "x25DteCustomerIdentifier": x25DteCustomerIdentifier,
       "x25DteIfTable": x25DteIfTable,
       "x25DteIfEntry": x25DteIfEntry,
       "x25DteInterfaceMode": x25DteInterfaceMode,
       "x25DteMaxActiveChannels": x25DteMaxActiveChannels,
       "x25DteNumberOfPLcn": x25DteNumberOfPLcn,
       "x25DtePacketSequencing": x25DtePacketSequencing,
       "x25DteT20RestartTimer": x25DteT20RestartTimer,
       "x25DteT21CallTimer": x25DteT21CallTimer,
       "x25DteT22ResetTimer": x25DteT22ResetTimer,
       "x25DteT23ClearTimer": x25DteT23ClearTimer,
       "x25DteLcnCTable": x25DteLcnCTable,
       "x25DteLcnCEntry": x25DteLcnCEntry,
       "x25DteLowestILChannelNumber": x25DteLowestILChannelNumber,
       "x25DteHighestILChannelNumber": x25DteHighestILChannelNumber,
       "x25DteLowestTLChannelNumber": x25DteLowestTLChannelNumber,
       "x25DteHighestTLChannelNumber": x25DteHighestTLChannelNumber,
       "x25DteLowestOLChannelNumber": x25DteLowestOLChannelNumber,
       "x25DteHighestOLChannelNumber": x25DteHighestOLChannelNumber,
       "x25DteDcpTable": x25DteDcpTable,
       "x25DteDcpEntry": x25DteDcpEntry,
       "x25DteInPacketSize": x25DteInPacketSize,
       "x25DteOutPacketSize": x25DteOutPacketSize,
       "x25DteInWindowSize": x25DteInWindowSize,
       "x25DteOutWindowSize": x25DteOutWindowSize,
       "x25DteAcceptReverseCharging": x25DteAcceptReverseCharging,
       "x25DteProposeReverseCharging": x25DteProposeReverseCharging,
       "x25DteOutThroughputClassSize": x25DteOutThroughputClassSize,
       "x25DteInThroughputClassSize": x25DteInThroughputClassSize,
       "x25DteCugIndex": x25DteCugIndex,
       "x25DteCugoaIndex": x25DteCugoaIndex,
       "x25DteChargingInformation": x25DteChargingInformation,
       "x25DteRpoa": x25DteRpoa,
       "x25DteTrnstDlySlctnAInd": x25DteTrnstDlySlctnAInd,
       "x25DteCallingNetworkFax": x25DteCallingNetworkFax,
       "x25DteCalledNetworkFax": x25DteCalledNetworkFax,
       "x25DteCallUserData": x25DteCallUserData,
       "x25DteIfEntryTable": x25DteIfEntryTable,
       "x25DteIfEntryEntry": x25DteIfEntryEntry,
       "x25DteIfAdminStatus": x25DteIfAdminStatus,
       "x25DteIfIndex": x25DteIfIndex,
       "x25DteStateTable": x25DteStateTable,
       "x25DteStateEntry": x25DteStateEntry,
       "x25DteAdminState": x25DteAdminState,
       "x25DteOperationalState": x25DteOperationalState,
       "x25DteUsageState": x25DteUsageState,
       "x25DteOperStatusTable": x25DteOperStatusTable,
       "x25DteOperStatusEntry": x25DteOperStatusEntry,
       "x25DteSnmpOperStatus": x25DteSnmpOperStatus,
       "x25DteOpTable": x25DteOpTable,
       "x25DteOpEntry": x25DteOpEntry,
       "x25DteInterfaceState": x25DteInterfaceState,
       "x25DteStatsTable": x25DteStatsTable,
       "x25DteStatsEntry": x25DteStatsEntry,
       "x25DteInCalls": x25DteInCalls,
       "x25DteInCallRefusals": x25DteInCallRefusals,
       "x25DteInPrvdrInitiatedClrs": x25DteInPrvdrInitiatedClrs,
       "x25DteInRmtInitiatedRsts": x25DteInRmtInitiatedRsts,
       "x25DteInPrvdrInitiatedRsts": x25DteInPrvdrInitiatedRsts,
       "x25DteInRestarts": x25DteInRestarts,
       "x25DteInDataPackets": x25DteInDataPackets,
       "x25DteInPktsAcusdOfPrtclErr": x25DteInPktsAcusdOfPrtclErr,
       "x25DteInInterruptPackets": x25DteInInterruptPackets,
       "x25DteOutCallAttempts": x25DteOutCallAttempts,
       "x25DteOutCallFailures": x25DteOutCallFailures,
       "x25DteOutInterruptPackets": x25DteOutInterruptPackets,
       "x25DteOutDataPackets": x25DteOutDataPackets,
       "x25DteOutActiveChannels": x25DteOutActiveChannels,
       "x25DteInActiveChannels": x25DteInActiveChannels,
       "x25DteTwowayActiveChannels": x25DteTwowayActiveChannels,
       "x25DteT20RestartTimeouts": x25DteT20RestartTimeouts,
       "x25DteT21CallTimeouts": x25DteT21CallTimeouts,
       "x25DteT22ResetTimeouts": x25DteT22ResetTimeouts,
       "x25DteT23ClearTimeouts": x25DteT23ClearTimeouts,
       "x25DteMIB": x25DteMIB,
       "x25DteGroup": x25DteGroup,
       "x25DteGroupBE": x25DteGroupBE,
       "x25DteGroupBE00": x25DteGroupBE00,
       "x25DteGroupBE00A": x25DteGroupBE00A,
       "x25DteCapabilities": x25DteCapabilities,
       "x25DteCapabilitiesBE": x25DteCapabilitiesBE,
       "x25DteCapabilitiesBE00": x25DteCapabilitiesBE00,
       "x25DteCapabilitiesBE00A": x25DteCapabilitiesBE00A}
)
