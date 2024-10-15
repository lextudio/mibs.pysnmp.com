# SNMP MIB module (Nortel-MsCarrier-MscPassport-X25DteMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-X25DteMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:23 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "HexString",
    "Link",
    "NonReplicated",
    "PassportCounter64")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscX25Dte_ObjectIdentity = ObjectIdentity
mscX25Dte = _MscX25Dte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90)
)
_MscX25DteRowStatusTable_Object = MibTable
mscX25DteRowStatusTable = _MscX25DteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 1)
)
if mibBuilder.loadTexts:
    mscX25DteRowStatusTable.setStatus("mandatory")
_MscX25DteRowStatusEntry_Object = MibTableRow
mscX25DteRowStatusEntry = _MscX25DteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 1, 1)
)
mscX25DteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteRowStatusEntry.setStatus("mandatory")
_MscX25DteRowStatus_Type = RowStatus
_MscX25DteRowStatus_Object = MibTableColumn
mscX25DteRowStatus = _MscX25DteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 1, 1, 1),
    _MscX25DteRowStatus_Type()
)
mscX25DteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRowStatus.setStatus("mandatory")
_MscX25DteComponentName_Type = DisplayString
_MscX25DteComponentName_Object = MibTableColumn
mscX25DteComponentName = _MscX25DteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 1, 1, 2),
    _MscX25DteComponentName_Type()
)
mscX25DteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteComponentName.setStatus("mandatory")
_MscX25DteStorageType_Type = StorageType
_MscX25DteStorageType_Object = MibTableColumn
mscX25DteStorageType = _MscX25DteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 1, 1, 4),
    _MscX25DteStorageType_Type()
)
mscX25DteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteStorageType.setStatus("mandatory")


class _MscX25DteIndex_Type(Integer32):
    """Custom type mscX25DteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscX25DteIndex_Type.__name__ = "Integer32"
_MscX25DteIndex_Object = MibTableColumn
mscX25DteIndex = _MscX25DteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 1, 1, 10),
    _MscX25DteIndex_Type()
)
mscX25DteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DteIndex.setStatus("mandatory")
_MscX25DtePeer_ObjectIdentity = ObjectIdentity
mscX25DtePeer = _MscX25DtePeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2)
)
_MscX25DtePeerRowStatusTable_Object = MibTable
mscX25DtePeerRowStatusTable = _MscX25DtePeerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 1)
)
if mibBuilder.loadTexts:
    mscX25DtePeerRowStatusTable.setStatus("mandatory")
_MscX25DtePeerRowStatusEntry_Object = MibTableRow
mscX25DtePeerRowStatusEntry = _MscX25DtePeerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 1, 1)
)
mscX25DtePeerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePeerRowStatusEntry.setStatus("mandatory")
_MscX25DtePeerRowStatus_Type = RowStatus
_MscX25DtePeerRowStatus_Object = MibTableColumn
mscX25DtePeerRowStatus = _MscX25DtePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 1, 1, 1),
    _MscX25DtePeerRowStatus_Type()
)
mscX25DtePeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerRowStatus.setStatus("mandatory")
_MscX25DtePeerComponentName_Type = DisplayString
_MscX25DtePeerComponentName_Object = MibTableColumn
mscX25DtePeerComponentName = _MscX25DtePeerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 1, 1, 2),
    _MscX25DtePeerComponentName_Type()
)
mscX25DtePeerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePeerComponentName.setStatus("mandatory")
_MscX25DtePeerStorageType_Type = StorageType
_MscX25DtePeerStorageType_Object = MibTableColumn
mscX25DtePeerStorageType = _MscX25DtePeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 1, 1, 4),
    _MscX25DtePeerStorageType_Type()
)
mscX25DtePeerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePeerStorageType.setStatus("mandatory")


class _MscX25DtePeerIndex_Type(Integer32):
    """Custom type mscX25DtePeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscX25DtePeerIndex_Type.__name__ = "Integer32"
_MscX25DtePeerIndex_Object = MibTableColumn
mscX25DtePeerIndex = _MscX25DtePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 1, 1, 10),
    _MscX25DtePeerIndex_Type()
)
mscX25DtePeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DtePeerIndex.setStatus("mandatory")
_MscX25DtePeerIfTable_Object = MibTable
mscX25DtePeerIfTable = _MscX25DtePeerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 10)
)
if mibBuilder.loadTexts:
    mscX25DtePeerIfTable.setStatus("mandatory")
_MscX25DtePeerIfEntry_Object = MibTableRow
mscX25DtePeerIfEntry = _MscX25DtePeerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 10, 1)
)
mscX25DtePeerIfEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePeerIfEntry.setStatus("mandatory")


class _MscX25DtePeerEncAddressType_Type(Integer32):
    """Custom type mscX25DtePeerEncAddressType based on Integer32"""
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


_MscX25DtePeerEncAddressType_Type.__name__ = "Integer32"
_MscX25DtePeerEncAddressType_Object = MibTableColumn
mscX25DtePeerEncAddressType = _MscX25DtePeerEncAddressType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 10, 1, 1),
    _MscX25DtePeerEncAddressType_Type()
)
mscX25DtePeerEncAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerEncAddressType.setStatus("mandatory")


class _MscX25DtePeerEncAddress_Type(AsciiString):
    """Custom type mscX25DtePeerEncAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscX25DtePeerEncAddress_Type.__name__ = "AsciiString"
_MscX25DtePeerEncAddress_Object = MibTableColumn
mscX25DtePeerEncAddress = _MscX25DtePeerEncAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 10, 1, 2),
    _MscX25DtePeerEncAddress_Type()
)
mscX25DtePeerEncAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerEncAddress.setStatus("mandatory")


class _MscX25DtePeerX25Address_Type(DigitString):
    """Custom type mscX25DtePeerX25Address based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscX25DtePeerX25Address_Type.__name__ = "DigitString"
_MscX25DtePeerX25Address_Object = MibTableColumn
mscX25DtePeerX25Address = _MscX25DtePeerX25Address_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 10, 1, 3),
    _MscX25DtePeerX25Address_Type()
)
mscX25DtePeerX25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerX25Address.setStatus("mandatory")
_MscX25DtePeerLinkToRemoteGroup_Type = Link
_MscX25DtePeerLinkToRemoteGroup_Object = MibTableColumn
mscX25DtePeerLinkToRemoteGroup = _MscX25DtePeerLinkToRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 10, 1, 4),
    _MscX25DtePeerLinkToRemoteGroup_Type()
)
mscX25DtePeerLinkToRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerLinkToRemoteGroup.setStatus("mandatory")
_MscX25DtePeerCpTable_Object = MibTable
mscX25DtePeerCpTable = _MscX25DtePeerCpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12)
)
if mibBuilder.loadTexts:
    mscX25DtePeerCpTable.setStatus("mandatory")
_MscX25DtePeerCpEntry_Object = MibTableRow
mscX25DtePeerCpEntry = _MscX25DtePeerCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1)
)
mscX25DtePeerCpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePeerCpEntry.setStatus("mandatory")


class _MscX25DtePeerInPacketSize_Type(Unsigned32):
    """Custom type mscX25DtePeerInPacketSize based on Unsigned32"""
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


_MscX25DtePeerInPacketSize_Type.__name__ = "Unsigned32"
_MscX25DtePeerInPacketSize_Object = MibTableColumn
mscX25DtePeerInPacketSize = _MscX25DtePeerInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 1),
    _MscX25DtePeerInPacketSize_Type()
)
mscX25DtePeerInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerInPacketSize.setStatus("mandatory")


class _MscX25DtePeerOutPacketSize_Type(Unsigned32):
    """Custom type mscX25DtePeerOutPacketSize based on Unsigned32"""
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


_MscX25DtePeerOutPacketSize_Type.__name__ = "Unsigned32"
_MscX25DtePeerOutPacketSize_Object = MibTableColumn
mscX25DtePeerOutPacketSize = _MscX25DtePeerOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 2),
    _MscX25DtePeerOutPacketSize_Type()
)
mscX25DtePeerOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerOutPacketSize.setStatus("mandatory")


class _MscX25DtePeerInWindowSize_Type(Unsigned32):
    """Custom type mscX25DtePeerInWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscX25DtePeerInWindowSize_Type.__name__ = "Unsigned32"
_MscX25DtePeerInWindowSize_Object = MibTableColumn
mscX25DtePeerInWindowSize = _MscX25DtePeerInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 3),
    _MscX25DtePeerInWindowSize_Type()
)
mscX25DtePeerInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerInWindowSize.setStatus("mandatory")


class _MscX25DtePeerOutWindowSize_Type(Unsigned32):
    """Custom type mscX25DtePeerOutWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscX25DtePeerOutWindowSize_Type.__name__ = "Unsigned32"
_MscX25DtePeerOutWindowSize_Object = MibTableColumn
mscX25DtePeerOutWindowSize = _MscX25DtePeerOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 4),
    _MscX25DtePeerOutWindowSize_Type()
)
mscX25DtePeerOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerOutWindowSize.setStatus("mandatory")


class _MscX25DtePeerAcceptReverseCharging_Type(Integer32):
    """Custom type mscX25DtePeerAcceptReverseCharging based on Integer32"""
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


_MscX25DtePeerAcceptReverseCharging_Type.__name__ = "Integer32"
_MscX25DtePeerAcceptReverseCharging_Object = MibTableColumn
mscX25DtePeerAcceptReverseCharging = _MscX25DtePeerAcceptReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 5),
    _MscX25DtePeerAcceptReverseCharging_Type()
)
mscX25DtePeerAcceptReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerAcceptReverseCharging.setStatus("mandatory")


class _MscX25DtePeerProposeReverseCharging_Type(Integer32):
    """Custom type mscX25DtePeerProposeReverseCharging based on Integer32"""
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


_MscX25DtePeerProposeReverseCharging_Type.__name__ = "Integer32"
_MscX25DtePeerProposeReverseCharging_Object = MibTableColumn
mscX25DtePeerProposeReverseCharging = _MscX25DtePeerProposeReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 6),
    _MscX25DtePeerProposeReverseCharging_Type()
)
mscX25DtePeerProposeReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerProposeReverseCharging.setStatus("mandatory")


class _MscX25DtePeerOutThroughputClassSize_Type(Integer32):
    """Custom type mscX25DtePeerOutThroughputClassSize based on Integer32"""
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


_MscX25DtePeerOutThroughputClassSize_Type.__name__ = "Integer32"
_MscX25DtePeerOutThroughputClassSize_Object = MibTableColumn
mscX25DtePeerOutThroughputClassSize = _MscX25DtePeerOutThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 8),
    _MscX25DtePeerOutThroughputClassSize_Type()
)
mscX25DtePeerOutThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerOutThroughputClassSize.setStatus("mandatory")


class _MscX25DtePeerInThroughputClassSize_Type(Integer32):
    """Custom type mscX25DtePeerInThroughputClassSize based on Integer32"""
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


_MscX25DtePeerInThroughputClassSize_Type.__name__ = "Integer32"
_MscX25DtePeerInThroughputClassSize_Object = MibTableColumn
mscX25DtePeerInThroughputClassSize = _MscX25DtePeerInThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 9),
    _MscX25DtePeerInThroughputClassSize_Type()
)
mscX25DtePeerInThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerInThroughputClassSize.setStatus("mandatory")


class _MscX25DtePeerCugIndex_Type(AsciiString):
    """Custom type mscX25DtePeerCugIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscX25DtePeerCugIndex_Type.__name__ = "AsciiString"
_MscX25DtePeerCugIndex_Object = MibTableColumn
mscX25DtePeerCugIndex = _MscX25DtePeerCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 10),
    _MscX25DtePeerCugIndex_Type()
)
mscX25DtePeerCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerCugIndex.setStatus("mandatory")


class _MscX25DtePeerCugoaIndex_Type(AsciiString):
    """Custom type mscX25DtePeerCugoaIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscX25DtePeerCugoaIndex_Type.__name__ = "AsciiString"
_MscX25DtePeerCugoaIndex_Object = MibTableColumn
mscX25DtePeerCugoaIndex = _MscX25DtePeerCugoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 11),
    _MscX25DtePeerCugoaIndex_Type()
)
mscX25DtePeerCugoaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerCugoaIndex.setStatus("mandatory")


class _MscX25DtePeerNetworkUserIdentifier_Type(HexString):
    """Custom type mscX25DtePeerNetworkUserIdentifier based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DtePeerNetworkUserIdentifier_Type.__name__ = "HexString"
_MscX25DtePeerNetworkUserIdentifier_Object = MibTableColumn
mscX25DtePeerNetworkUserIdentifier = _MscX25DtePeerNetworkUserIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 12),
    _MscX25DtePeerNetworkUserIdentifier_Type()
)
mscX25DtePeerNetworkUserIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerNetworkUserIdentifier.setStatus("mandatory")


class _MscX25DtePeerChargingInformation_Type(Integer32):
    """Custom type mscX25DtePeerChargingInformation based on Integer32"""
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


_MscX25DtePeerChargingInformation_Type.__name__ = "Integer32"
_MscX25DtePeerChargingInformation_Object = MibTableColumn
mscX25DtePeerChargingInformation = _MscX25DtePeerChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 13),
    _MscX25DtePeerChargingInformation_Type()
)
mscX25DtePeerChargingInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerChargingInformation.setStatus("mandatory")


class _MscX25DtePeerRpoa_Type(AsciiString):
    """Custom type mscX25DtePeerRpoa based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DtePeerRpoa_Type.__name__ = "AsciiString"
_MscX25DtePeerRpoa_Object = MibTableColumn
mscX25DtePeerRpoa = _MscX25DtePeerRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 14),
    _MscX25DtePeerRpoa_Type()
)
mscX25DtePeerRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerRpoa.setStatus("mandatory")


class _MscX25DtePeerTrnstDlySlctnAInd_Type(Unsigned32):
    """Custom type mscX25DtePeerTrnstDlySlctnAInd based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65537),
    )


_MscX25DtePeerTrnstDlySlctnAInd_Type.__name__ = "Unsigned32"
_MscX25DtePeerTrnstDlySlctnAInd_Object = MibTableColumn
mscX25DtePeerTrnstDlySlctnAInd = _MscX25DtePeerTrnstDlySlctnAInd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 15),
    _MscX25DtePeerTrnstDlySlctnAInd_Type()
)
mscX25DtePeerTrnstDlySlctnAInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerTrnstDlySlctnAInd.setStatus("mandatory")


class _MscX25DtePeerCallingNetworkFax_Type(HexString):
    """Custom type mscX25DtePeerCallingNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DtePeerCallingNetworkFax_Type.__name__ = "HexString"
_MscX25DtePeerCallingNetworkFax_Object = MibTableColumn
mscX25DtePeerCallingNetworkFax = _MscX25DtePeerCallingNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 24),
    _MscX25DtePeerCallingNetworkFax_Type()
)
mscX25DtePeerCallingNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerCallingNetworkFax.setStatus("mandatory")


class _MscX25DtePeerCalledNetworkFax_Type(HexString):
    """Custom type mscX25DtePeerCalledNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DtePeerCalledNetworkFax_Type.__name__ = "HexString"
_MscX25DtePeerCalledNetworkFax_Object = MibTableColumn
mscX25DtePeerCalledNetworkFax = _MscX25DtePeerCalledNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 25),
    _MscX25DtePeerCalledNetworkFax_Type()
)
mscX25DtePeerCalledNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerCalledNetworkFax.setStatus("mandatory")


class _MscX25DtePeerCallUserData_Type(HexString):
    """Custom type mscX25DtePeerCallUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscX25DtePeerCallUserData_Type.__name__ = "HexString"
_MscX25DtePeerCallUserData_Object = MibTableColumn
mscX25DtePeerCallUserData = _MscX25DtePeerCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 12, 1, 26),
    _MscX25DtePeerCallUserData_Type()
)
mscX25DtePeerCallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePeerCallUserData.setStatus("mandatory")
_MscX25DtePeerPEncTable_Object = MibTable
mscX25DtePeerPEncTable = _MscX25DtePeerPEncTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 208)
)
if mibBuilder.loadTexts:
    mscX25DtePeerPEncTable.setStatus("mandatory")
_MscX25DtePeerPEncEntry_Object = MibTableRow
mscX25DtePeerPEncEntry = _MscX25DtePeerPEncEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 208, 1)
)
mscX25DtePeerPEncEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerPEncIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePeerPEncEntry.setStatus("mandatory")


class _MscX25DtePeerPEncIndex_Type(Integer32):
    """Custom type mscX25DtePeerPEncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MscX25DtePeerPEncIndex_Type.__name__ = "Integer32"
_MscX25DtePeerPEncIndex_Object = MibTableColumn
mscX25DtePeerPEncIndex = _MscX25DtePeerPEncIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 208, 1, 1),
    _MscX25DtePeerPEncIndex_Type()
)
mscX25DtePeerPEncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DtePeerPEncIndex.setStatus("mandatory")


class _MscX25DtePeerPEncValue_Type(Integer32):
    """Custom type mscX25DtePeerPEncValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            204
        )
    )
    namedValues = NamedValues(
        ("ip", 204)
    )


_MscX25DtePeerPEncValue_Type.__name__ = "Integer32"
_MscX25DtePeerPEncValue_Object = MibTableColumn
mscX25DtePeerPEncValue = _MscX25DtePeerPEncValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 208, 1, 2),
    _MscX25DtePeerPEncValue_Type()
)
mscX25DtePeerPEncValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePeerPEncValue.setStatus("mandatory")
_MscX25DtePeerPEncRowStatus_Type = RowStatus
_MscX25DtePeerPEncRowStatus_Object = MibTableColumn
mscX25DtePeerPEncRowStatus = _MscX25DtePeerPEncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 208, 1, 3),
    _MscX25DtePeerPEncRowStatus_Type()
)
mscX25DtePeerPEncRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscX25DtePeerPEncRowStatus.setStatus("mandatory")
_MscX25DtePeerLcnTable_Object = MibTable
mscX25DtePeerLcnTable = _MscX25DtePeerLcnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 209)
)
if mibBuilder.loadTexts:
    mscX25DtePeerLcnTable.setStatus("mandatory")
_MscX25DtePeerLcnEntry_Object = MibTableRow
mscX25DtePeerLcnEntry = _MscX25DtePeerLcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 209, 1)
)
mscX25DtePeerLcnEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePeerLcnValue"),
)
if mibBuilder.loadTexts:
    mscX25DtePeerLcnEntry.setStatus("mandatory")


class _MscX25DtePeerLcnValue_Type(Integer32):
    """Custom type mscX25DtePeerLcnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscX25DtePeerLcnValue_Type.__name__ = "Integer32"
_MscX25DtePeerLcnValue_Object = MibTableColumn
mscX25DtePeerLcnValue = _MscX25DtePeerLcnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 2, 209, 1, 1),
    _MscX25DtePeerLcnValue_Type()
)
mscX25DtePeerLcnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePeerLcnValue.setStatus("mandatory")
_MscX25DtePLcn_ObjectIdentity = ObjectIdentity
mscX25DtePLcn = _MscX25DtePLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3)
)
_MscX25DtePLcnRowStatusTable_Object = MibTable
mscX25DtePLcnRowStatusTable = _MscX25DtePLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 1)
)
if mibBuilder.loadTexts:
    mscX25DtePLcnRowStatusTable.setStatus("mandatory")
_MscX25DtePLcnRowStatusEntry_Object = MibTableRow
mscX25DtePLcnRowStatusEntry = _MscX25DtePLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 1, 1)
)
mscX25DtePLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePLcnRowStatusEntry.setStatus("mandatory")
_MscX25DtePLcnRowStatus_Type = RowStatus
_MscX25DtePLcnRowStatus_Object = MibTableColumn
mscX25DtePLcnRowStatus = _MscX25DtePLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 1, 1, 1),
    _MscX25DtePLcnRowStatus_Type()
)
mscX25DtePLcnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnRowStatus.setStatus("mandatory")
_MscX25DtePLcnComponentName_Type = DisplayString
_MscX25DtePLcnComponentName_Object = MibTableColumn
mscX25DtePLcnComponentName = _MscX25DtePLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 1, 1, 2),
    _MscX25DtePLcnComponentName_Type()
)
mscX25DtePLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePLcnComponentName.setStatus("mandatory")
_MscX25DtePLcnStorageType_Type = StorageType
_MscX25DtePLcnStorageType_Object = MibTableColumn
mscX25DtePLcnStorageType = _MscX25DtePLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 1, 1, 4),
    _MscX25DtePLcnStorageType_Type()
)
mscX25DtePLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePLcnStorageType.setStatus("mandatory")


class _MscX25DtePLcnIndex_Type(Integer32):
    """Custom type mscX25DtePLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscX25DtePLcnIndex_Type.__name__ = "Integer32"
_MscX25DtePLcnIndex_Object = MibTableColumn
mscX25DtePLcnIndex = _MscX25DtePLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 1, 1, 10),
    _MscX25DtePLcnIndex_Type()
)
mscX25DtePLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DtePLcnIndex.setStatus("mandatory")
_MscX25DtePLcnProvTable_Object = MibTable
mscX25DtePLcnProvTable = _MscX25DtePLcnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10)
)
if mibBuilder.loadTexts:
    mscX25DtePLcnProvTable.setStatus("mandatory")
_MscX25DtePLcnProvEntry_Object = MibTableRow
mscX25DtePLcnProvEntry = _MscX25DtePLcnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1)
)
mscX25DtePLcnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePLcnProvEntry.setStatus("mandatory")


class _MscX25DtePLcnEncAddressType_Type(Integer32):
    """Custom type mscX25DtePLcnEncAddressType based on Integer32"""
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


_MscX25DtePLcnEncAddressType_Type.__name__ = "Integer32"
_MscX25DtePLcnEncAddressType_Object = MibTableColumn
mscX25DtePLcnEncAddressType = _MscX25DtePLcnEncAddressType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 1),
    _MscX25DtePLcnEncAddressType_Type()
)
mscX25DtePLcnEncAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnEncAddressType.setStatus("mandatory")


class _MscX25DtePLcnEncAddress_Type(AsciiString):
    """Custom type mscX25DtePLcnEncAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscX25DtePLcnEncAddress_Type.__name__ = "AsciiString"
_MscX25DtePLcnEncAddress_Object = MibTableColumn
mscX25DtePLcnEncAddress = _MscX25DtePLcnEncAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 2),
    _MscX25DtePLcnEncAddress_Type()
)
mscX25DtePLcnEncAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnEncAddress.setStatus("mandatory")


class _MscX25DtePLcnProtocolEncType_Type(Integer32):
    """Custom type mscX25DtePLcnProtocolEncType based on Integer32"""
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


_MscX25DtePLcnProtocolEncType_Type.__name__ = "Integer32"
_MscX25DtePLcnProtocolEncType_Object = MibTableColumn
mscX25DtePLcnProtocolEncType = _MscX25DtePLcnProtocolEncType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 3),
    _MscX25DtePLcnProtocolEncType_Type()
)
mscX25DtePLcnProtocolEncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnProtocolEncType.setStatus("mandatory")
_MscX25DtePLcnLinkToRemoteGroup_Type = Link
_MscX25DtePLcnLinkToRemoteGroup_Object = MibTableColumn
mscX25DtePLcnLinkToRemoteGroup = _MscX25DtePLcnLinkToRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 4),
    _MscX25DtePLcnLinkToRemoteGroup_Type()
)
mscX25DtePLcnLinkToRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnLinkToRemoteGroup.setStatus("mandatory")


class _MscX25DtePLcnInPacketSize_Type(Unsigned32):
    """Custom type mscX25DtePLcnInPacketSize based on Unsigned32"""
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


_MscX25DtePLcnInPacketSize_Type.__name__ = "Unsigned32"
_MscX25DtePLcnInPacketSize_Object = MibTableColumn
mscX25DtePLcnInPacketSize = _MscX25DtePLcnInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 5),
    _MscX25DtePLcnInPacketSize_Type()
)
mscX25DtePLcnInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnInPacketSize.setStatus("mandatory")


class _MscX25DtePLcnOutPacketSize_Type(Unsigned32):
    """Custom type mscX25DtePLcnOutPacketSize based on Unsigned32"""
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


_MscX25DtePLcnOutPacketSize_Type.__name__ = "Unsigned32"
_MscX25DtePLcnOutPacketSize_Object = MibTableColumn
mscX25DtePLcnOutPacketSize = _MscX25DtePLcnOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 6),
    _MscX25DtePLcnOutPacketSize_Type()
)
mscX25DtePLcnOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnOutPacketSize.setStatus("mandatory")


class _MscX25DtePLcnInWindowSize_Type(Unsigned32):
    """Custom type mscX25DtePLcnInWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DtePLcnInWindowSize_Type.__name__ = "Unsigned32"
_MscX25DtePLcnInWindowSize_Object = MibTableColumn
mscX25DtePLcnInWindowSize = _MscX25DtePLcnInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 7),
    _MscX25DtePLcnInWindowSize_Type()
)
mscX25DtePLcnInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnInWindowSize.setStatus("mandatory")


class _MscX25DtePLcnOutWindowSize_Type(Unsigned32):
    """Custom type mscX25DtePLcnOutWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DtePLcnOutWindowSize_Type.__name__ = "Unsigned32"
_MscX25DtePLcnOutWindowSize_Object = MibTableColumn
mscX25DtePLcnOutWindowSize = _MscX25DtePLcnOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 3, 10, 1, 8),
    _MscX25DtePLcnOutWindowSize_Type()
)
mscX25DtePLcnOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePLcnOutWindowSize.setStatus("mandatory")
_MscX25DteLcn_ObjectIdentity = ObjectIdentity
mscX25DteLcn = _MscX25DteLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4)
)
_MscX25DteLcnRowStatusTable_Object = MibTable
mscX25DteLcnRowStatusTable = _MscX25DteLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 1)
)
if mibBuilder.loadTexts:
    mscX25DteLcnRowStatusTable.setStatus("mandatory")
_MscX25DteLcnRowStatusEntry_Object = MibTableRow
mscX25DteLcnRowStatusEntry = _MscX25DteLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 1, 1)
)
mscX25DteLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLcnRowStatusEntry.setStatus("mandatory")
_MscX25DteLcnRowStatus_Type = RowStatus
_MscX25DteLcnRowStatus_Object = MibTableColumn
mscX25DteLcnRowStatus = _MscX25DteLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 1, 1, 1),
    _MscX25DteLcnRowStatus_Type()
)
mscX25DteLcnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnRowStatus.setStatus("mandatory")
_MscX25DteLcnComponentName_Type = DisplayString
_MscX25DteLcnComponentName_Object = MibTableColumn
mscX25DteLcnComponentName = _MscX25DteLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 1, 1, 2),
    _MscX25DteLcnComponentName_Type()
)
mscX25DteLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnComponentName.setStatus("mandatory")
_MscX25DteLcnStorageType_Type = StorageType
_MscX25DteLcnStorageType_Object = MibTableColumn
mscX25DteLcnStorageType = _MscX25DteLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 1, 1, 4),
    _MscX25DteLcnStorageType_Type()
)
mscX25DteLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnStorageType.setStatus("mandatory")


class _MscX25DteLcnIndex_Type(Integer32):
    """Custom type mscX25DteLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscX25DteLcnIndex_Type.__name__ = "Integer32"
_MscX25DteLcnIndex_Object = MibTableColumn
mscX25DteLcnIndex = _MscX25DteLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 1, 1, 10),
    _MscX25DteLcnIndex_Type()
)
mscX25DteLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DteLcnIndex.setStatus("mandatory")
_MscX25DteLcnStateTable_Object = MibTable
mscX25DteLcnStateTable = _MscX25DteLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 10)
)
if mibBuilder.loadTexts:
    mscX25DteLcnStateTable.setStatus("mandatory")
_MscX25DteLcnStateEntry_Object = MibTableRow
mscX25DteLcnStateEntry = _MscX25DteLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 10, 1)
)
mscX25DteLcnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLcnStateEntry.setStatus("mandatory")


class _MscX25DteLcnAdminState_Type(Integer32):
    """Custom type mscX25DteLcnAdminState based on Integer32"""
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


_MscX25DteLcnAdminState_Type.__name__ = "Integer32"
_MscX25DteLcnAdminState_Object = MibTableColumn
mscX25DteLcnAdminState = _MscX25DteLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 10, 1, 1),
    _MscX25DteLcnAdminState_Type()
)
mscX25DteLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnAdminState.setStatus("mandatory")


class _MscX25DteLcnOperationalState_Type(Integer32):
    """Custom type mscX25DteLcnOperationalState based on Integer32"""
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


_MscX25DteLcnOperationalState_Type.__name__ = "Integer32"
_MscX25DteLcnOperationalState_Object = MibTableColumn
mscX25DteLcnOperationalState = _MscX25DteLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 10, 1, 2),
    _MscX25DteLcnOperationalState_Type()
)
mscX25DteLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOperationalState.setStatus("mandatory")


class _MscX25DteLcnUsageState_Type(Integer32):
    """Custom type mscX25DteLcnUsageState based on Integer32"""
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


_MscX25DteLcnUsageState_Type.__name__ = "Integer32"
_MscX25DteLcnUsageState_Object = MibTableColumn
mscX25DteLcnUsageState = _MscX25DteLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 10, 1, 3),
    _MscX25DteLcnUsageState_Type()
)
mscX25DteLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnUsageState.setStatus("mandatory")
_MscX25DteLcnCpTable_Object = MibTable
mscX25DteLcnCpTable = _MscX25DteLcnCpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11)
)
if mibBuilder.loadTexts:
    mscX25DteLcnCpTable.setStatus("mandatory")
_MscX25DteLcnCpEntry_Object = MibTableRow
mscX25DteLcnCpEntry = _MscX25DteLcnCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1)
)
mscX25DteLcnCpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLcnCpEntry.setStatus("mandatory")


class _MscX25DteLcnInPacketSize_Type(Unsigned32):
    """Custom type mscX25DteLcnInPacketSize based on Unsigned32"""
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


_MscX25DteLcnInPacketSize_Type.__name__ = "Unsigned32"
_MscX25DteLcnInPacketSize_Object = MibTableColumn
mscX25DteLcnInPacketSize = _MscX25DteLcnInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 1),
    _MscX25DteLcnInPacketSize_Type()
)
mscX25DteLcnInPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInPacketSize.setStatus("mandatory")


class _MscX25DteLcnOutPacketSize_Type(Unsigned32):
    """Custom type mscX25DteLcnOutPacketSize based on Unsigned32"""
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


_MscX25DteLcnOutPacketSize_Type.__name__ = "Unsigned32"
_MscX25DteLcnOutPacketSize_Object = MibTableColumn
mscX25DteLcnOutPacketSize = _MscX25DteLcnOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 2),
    _MscX25DteLcnOutPacketSize_Type()
)
mscX25DteLcnOutPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOutPacketSize.setStatus("mandatory")


class _MscX25DteLcnInWindowSize_Type(Unsigned32):
    """Custom type mscX25DteLcnInWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DteLcnInWindowSize_Type.__name__ = "Unsigned32"
_MscX25DteLcnInWindowSize_Object = MibTableColumn
mscX25DteLcnInWindowSize = _MscX25DteLcnInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 3),
    _MscX25DteLcnInWindowSize_Type()
)
mscX25DteLcnInWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInWindowSize.setStatus("mandatory")


class _MscX25DteLcnOutWindowSize_Type(Unsigned32):
    """Custom type mscX25DteLcnOutWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DteLcnOutWindowSize_Type.__name__ = "Unsigned32"
_MscX25DteLcnOutWindowSize_Object = MibTableColumn
mscX25DteLcnOutWindowSize = _MscX25DteLcnOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 4),
    _MscX25DteLcnOutWindowSize_Type()
)
mscX25DteLcnOutWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOutWindowSize.setStatus("mandatory")


class _MscX25DteLcnProposeReverseCharging_Type(Integer32):
    """Custom type mscX25DteLcnProposeReverseCharging based on Integer32"""
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


_MscX25DteLcnProposeReverseCharging_Type.__name__ = "Integer32"
_MscX25DteLcnProposeReverseCharging_Object = MibTableColumn
mscX25DteLcnProposeReverseCharging = _MscX25DteLcnProposeReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 5),
    _MscX25DteLcnProposeReverseCharging_Type()
)
mscX25DteLcnProposeReverseCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnProposeReverseCharging.setStatus("mandatory")


class _MscX25DteLcnFastSelect_Type(Integer32):
    """Custom type mscX25DteLcnFastSelect based on Integer32"""
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


_MscX25DteLcnFastSelect_Type.__name__ = "Integer32"
_MscX25DteLcnFastSelect_Object = MibTableColumn
mscX25DteLcnFastSelect = _MscX25DteLcnFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 6),
    _MscX25DteLcnFastSelect_Type()
)
mscX25DteLcnFastSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnFastSelect.setStatus("mandatory")


class _MscX25DteLcnOutThroughputClassSize_Type(Integer32):
    """Custom type mscX25DteLcnOutThroughputClassSize based on Integer32"""
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


_MscX25DteLcnOutThroughputClassSize_Type.__name__ = "Integer32"
_MscX25DteLcnOutThroughputClassSize_Object = MibTableColumn
mscX25DteLcnOutThroughputClassSize = _MscX25DteLcnOutThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 7),
    _MscX25DteLcnOutThroughputClassSize_Type()
)
mscX25DteLcnOutThroughputClassSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOutThroughputClassSize.setStatus("mandatory")


class _MscX25DteLcnInThroughputClassSize_Type(Integer32):
    """Custom type mscX25DteLcnInThroughputClassSize based on Integer32"""
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


_MscX25DteLcnInThroughputClassSize_Type.__name__ = "Integer32"
_MscX25DteLcnInThroughputClassSize_Object = MibTableColumn
mscX25DteLcnInThroughputClassSize = _MscX25DteLcnInThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 8),
    _MscX25DteLcnInThroughputClassSize_Type()
)
mscX25DteLcnInThroughputClassSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInThroughputClassSize.setStatus("mandatory")


class _MscX25DteLcnCugIndex_Type(AsciiString):
    """Custom type mscX25DteLcnCugIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscX25DteLcnCugIndex_Type.__name__ = "AsciiString"
_MscX25DteLcnCugIndex_Object = MibTableColumn
mscX25DteLcnCugIndex = _MscX25DteLcnCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 9),
    _MscX25DteLcnCugIndex_Type()
)
mscX25DteLcnCugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCugIndex.setStatus("mandatory")


class _MscX25DteLcnCugoaIndex_Type(AsciiString):
    """Custom type mscX25DteLcnCugoaIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscX25DteLcnCugoaIndex_Type.__name__ = "AsciiString"
_MscX25DteLcnCugoaIndex_Object = MibTableColumn
mscX25DteLcnCugoaIndex = _MscX25DteLcnCugoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 10),
    _MscX25DteLcnCugoaIndex_Type()
)
mscX25DteLcnCugoaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCugoaIndex.setStatus("mandatory")


class _MscX25DteLcnNetworkUserIdentifier_Type(HexString):
    """Custom type mscX25DteLcnNetworkUserIdentifier based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteLcnNetworkUserIdentifier_Type.__name__ = "HexString"
_MscX25DteLcnNetworkUserIdentifier_Object = MibTableColumn
mscX25DteLcnNetworkUserIdentifier = _MscX25DteLcnNetworkUserIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 11),
    _MscX25DteLcnNetworkUserIdentifier_Type()
)
mscX25DteLcnNetworkUserIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnNetworkUserIdentifier.setStatus("mandatory")


class _MscX25DteLcnChargingInformation_Type(Integer32):
    """Custom type mscX25DteLcnChargingInformation based on Integer32"""
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


_MscX25DteLcnChargingInformation_Type.__name__ = "Integer32"
_MscX25DteLcnChargingInformation_Object = MibTableColumn
mscX25DteLcnChargingInformation = _MscX25DteLcnChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 12),
    _MscX25DteLcnChargingInformation_Type()
)
mscX25DteLcnChargingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnChargingInformation.setStatus("mandatory")


class _MscX25DteLcnRpoa_Type(AsciiString):
    """Custom type mscX25DteLcnRpoa based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteLcnRpoa_Type.__name__ = "AsciiString"
_MscX25DteLcnRpoa_Object = MibTableColumn
mscX25DteLcnRpoa = _MscX25DteLcnRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 13),
    _MscX25DteLcnRpoa_Type()
)
mscX25DteLcnRpoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnRpoa.setStatus("mandatory")


class _MscX25DteLcnTrnstDlySlctnAInd_Type(Unsigned32):
    """Custom type mscX25DteLcnTrnstDlySlctnAInd based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_MscX25DteLcnTrnstDlySlctnAInd_Type.__name__ = "Unsigned32"
_MscX25DteLcnTrnstDlySlctnAInd_Object = MibTableColumn
mscX25DteLcnTrnstDlySlctnAInd = _MscX25DteLcnTrnstDlySlctnAInd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 14),
    _MscX25DteLcnTrnstDlySlctnAInd_Type()
)
mscX25DteLcnTrnstDlySlctnAInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnTrnstDlySlctnAInd.setStatus("mandatory")


class _MscX25DteLcnCallingNetworkFax_Type(HexString):
    """Custom type mscX25DteLcnCallingNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteLcnCallingNetworkFax_Type.__name__ = "HexString"
_MscX25DteLcnCallingNetworkFax_Object = MibTableColumn
mscX25DteLcnCallingNetworkFax = _MscX25DteLcnCallingNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 23),
    _MscX25DteLcnCallingNetworkFax_Type()
)
mscX25DteLcnCallingNetworkFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCallingNetworkFax.setStatus("mandatory")


class _MscX25DteLcnCalledNetworkFax_Type(HexString):
    """Custom type mscX25DteLcnCalledNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteLcnCalledNetworkFax_Type.__name__ = "HexString"
_MscX25DteLcnCalledNetworkFax_Object = MibTableColumn
mscX25DteLcnCalledNetworkFax = _MscX25DteLcnCalledNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 24),
    _MscX25DteLcnCalledNetworkFax_Type()
)
mscX25DteLcnCalledNetworkFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCalledNetworkFax.setStatus("mandatory")


class _MscX25DteLcnCallUserData_Type(HexString):
    """Custom type mscX25DteLcnCallUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscX25DteLcnCallUserData_Type.__name__ = "HexString"
_MscX25DteLcnCallUserData_Object = MibTableColumn
mscX25DteLcnCallUserData = _MscX25DteLcnCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 11, 1, 25),
    _MscX25DteLcnCallUserData_Type()
)
mscX25DteLcnCallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCallUserData.setStatus("mandatory")
_MscX25DteLcnLcnStatusTable_Object = MibTable
mscX25DteLcnLcnStatusTable = _MscX25DteLcnLcnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12)
)
if mibBuilder.loadTexts:
    mscX25DteLcnLcnStatusTable.setStatus("mandatory")
_MscX25DteLcnLcnStatusEntry_Object = MibTableRow
mscX25DteLcnLcnStatusEntry = _MscX25DteLcnLcnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12, 1)
)
mscX25DteLcnLcnStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLcnLcnStatusEntry.setStatus("mandatory")


class _MscX25DteLcnStatus_Type(Integer32):
    """Custom type mscX25DteLcnStatus based on Integer32"""
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


_MscX25DteLcnStatus_Type.__name__ = "Integer32"
_MscX25DteLcnStatus_Object = MibTableColumn
mscX25DteLcnStatus = _MscX25DteLcnStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12, 1, 1),
    _MscX25DteLcnStatus_Type()
)
mscX25DteLcnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnStatus.setStatus("mandatory")


class _MscX25DteLcnCallDirection_Type(Integer32):
    """Custom type mscX25DteLcnCallDirection based on Integer32"""
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


_MscX25DteLcnCallDirection_Type.__name__ = "Integer32"
_MscX25DteLcnCallDirection_Object = MibTableColumn
mscX25DteLcnCallDirection = _MscX25DteLcnCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12, 1, 3),
    _MscX25DteLcnCallDirection_Type()
)
mscX25DteLcnCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCallDirection.setStatus("mandatory")


class _MscX25DteLcnCalledAddress_Type(DigitString):
    """Custom type mscX25DteLcnCalledAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscX25DteLcnCalledAddress_Type.__name__ = "DigitString"
_MscX25DteLcnCalledAddress_Object = MibTableColumn
mscX25DteLcnCalledAddress = _MscX25DteLcnCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12, 1, 4),
    _MscX25DteLcnCalledAddress_Type()
)
mscX25DteLcnCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCalledAddress.setStatus("mandatory")


class _MscX25DteLcnCallingAddress_Type(DigitString):
    """Custom type mscX25DteLcnCallingAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscX25DteLcnCallingAddress_Type.__name__ = "DigitString"
_MscX25DteLcnCallingAddress_Object = MibTableColumn
mscX25DteLcnCallingAddress = _MscX25DteLcnCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12, 1, 5),
    _MscX25DteLcnCallingAddress_Type()
)
mscX25DteLcnCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnCallingAddress.setStatus("mandatory")


class _MscX25DteLcnOriginalCalledAddress_Type(DigitString):
    """Custom type mscX25DteLcnOriginalCalledAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscX25DteLcnOriginalCalledAddress_Type.__name__ = "DigitString"
_MscX25DteLcnOriginalCalledAddress_Object = MibTableColumn
mscX25DteLcnOriginalCalledAddress = _MscX25DteLcnOriginalCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 12, 1, 6),
    _MscX25DteLcnOriginalCalledAddress_Type()
)
mscX25DteLcnOriginalCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOriginalCalledAddress.setStatus("mandatory")
_MscX25DteLcnStatsTable_Object = MibTable
mscX25DteLcnStatsTable = _MscX25DteLcnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13)
)
if mibBuilder.loadTexts:
    mscX25DteLcnStatsTable.setStatus("mandatory")
_MscX25DteLcnStatsEntry_Object = MibTableRow
mscX25DteLcnStatsEntry = _MscX25DteLcnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1)
)
mscX25DteLcnStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLcnIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLcnStatsEntry.setStatus("mandatory")
_MscX25DteLcnInUknownProtocols_Type = Counter32
_MscX25DteLcnInUknownProtocols_Object = MibTableColumn
mscX25DteLcnInUknownProtocols = _MscX25DteLcnInUknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 1),
    _MscX25DteLcnInUknownProtocols_Type()
)
mscX25DteLcnInUknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInUknownProtocols.setStatus("mandatory")
_MscX25DteLcnInDataOctets_Type = Counter32
_MscX25DteLcnInDataOctets_Object = MibTableColumn
mscX25DteLcnInDataOctets = _MscX25DteLcnInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 2),
    _MscX25DteLcnInDataOctets_Type()
)
mscX25DteLcnInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInDataOctets.setStatus("mandatory")
_MscX25DteLcnInDataPackets_Type = Counter32
_MscX25DteLcnInDataPackets_Object = MibTableColumn
mscX25DteLcnInDataPackets = _MscX25DteLcnInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 3),
    _MscX25DteLcnInDataPackets_Type()
)
mscX25DteLcnInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInDataPackets.setStatus("mandatory")
_MscX25DteLcnInRmtInitiatedRsts_Type = Counter32
_MscX25DteLcnInRmtInitiatedRsts_Object = MibTableColumn
mscX25DteLcnInRmtInitiatedRsts = _MscX25DteLcnInRmtInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 4),
    _MscX25DteLcnInRmtInitiatedRsts_Type()
)
mscX25DteLcnInRmtInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInRmtInitiatedRsts.setStatus("mandatory")
_MscX25DteLcnInPrvdrInitiatedRsts_Type = Counter32
_MscX25DteLcnInPrvdrInitiatedRsts_Object = MibTableColumn
mscX25DteLcnInPrvdrInitiatedRsts = _MscX25DteLcnInPrvdrInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 5),
    _MscX25DteLcnInPrvdrInitiatedRsts_Type()
)
mscX25DteLcnInPrvdrInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInPrvdrInitiatedRsts.setStatus("mandatory")
_MscX25DteLcnInInterruptPackets_Type = Counter32
_MscX25DteLcnInInterruptPackets_Object = MibTableColumn
mscX25DteLcnInInterruptPackets = _MscX25DteLcnInInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 6),
    _MscX25DteLcnInInterruptPackets_Type()
)
mscX25DteLcnInInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnInInterruptPackets.setStatus("mandatory")
_MscX25DteLcnOutDataOctets_Type = Counter32
_MscX25DteLcnOutDataOctets_Object = MibTableColumn
mscX25DteLcnOutDataOctets = _MscX25DteLcnOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 7),
    _MscX25DteLcnOutDataOctets_Type()
)
mscX25DteLcnOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOutDataOctets.setStatus("mandatory")
_MscX25DteLcnOutDataPackets_Type = Counter32
_MscX25DteLcnOutDataPackets_Object = MibTableColumn
mscX25DteLcnOutDataPackets = _MscX25DteLcnOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 8),
    _MscX25DteLcnOutDataPackets_Type()
)
mscX25DteLcnOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOutDataPackets.setStatus("mandatory")
_MscX25DteLcnOutInterruptPackets_Type = Counter32
_MscX25DteLcnOutInterruptPackets_Object = MibTableColumn
mscX25DteLcnOutInterruptPackets = _MscX25DteLcnOutInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 9),
    _MscX25DteLcnOutInterruptPackets_Type()
)
mscX25DteLcnOutInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnOutInterruptPackets.setStatus("mandatory")
_MscX25DteLcnT22ResetTimeouts_Type = Counter32
_MscX25DteLcnT22ResetTimeouts_Object = MibTableColumn
mscX25DteLcnT22ResetTimeouts = _MscX25DteLcnT22ResetTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 4, 13, 1, 10),
    _MscX25DteLcnT22ResetTimeouts_Type()
)
mscX25DteLcnT22ResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLcnT22ResetTimeouts.setStatus("mandatory")
_MscX25DteLapb_ObjectIdentity = ObjectIdentity
mscX25DteLapb = _MscX25DteLapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5)
)
_MscX25DteLapbRowStatusTable_Object = MibTable
mscX25DteLapbRowStatusTable = _MscX25DteLapbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 1)
)
if mibBuilder.loadTexts:
    mscX25DteLapbRowStatusTable.setStatus("mandatory")
_MscX25DteLapbRowStatusEntry_Object = MibTableRow
mscX25DteLapbRowStatusEntry = _MscX25DteLapbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 1, 1)
)
mscX25DteLapbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbRowStatusEntry.setStatus("mandatory")
_MscX25DteLapbRowStatus_Type = RowStatus
_MscX25DteLapbRowStatus_Object = MibTableColumn
mscX25DteLapbRowStatus = _MscX25DteLapbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 1, 1, 1),
    _MscX25DteLapbRowStatus_Type()
)
mscX25DteLapbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbRowStatus.setStatus("mandatory")
_MscX25DteLapbComponentName_Type = DisplayString
_MscX25DteLapbComponentName_Object = MibTableColumn
mscX25DteLapbComponentName = _MscX25DteLapbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 1, 1, 2),
    _MscX25DteLapbComponentName_Type()
)
mscX25DteLapbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbComponentName.setStatus("mandatory")
_MscX25DteLapbStorageType_Type = StorageType
_MscX25DteLapbStorageType_Object = MibTableColumn
mscX25DteLapbStorageType = _MscX25DteLapbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 1, 1, 4),
    _MscX25DteLapbStorageType_Type()
)
mscX25DteLapbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbStorageType.setStatus("mandatory")
_MscX25DteLapbIndex_Type = NonReplicated
_MscX25DteLapbIndex_Object = MibTableColumn
mscX25DteLapbIndex = _MscX25DteLapbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 1, 1, 10),
    _MscX25DteLapbIndex_Type()
)
mscX25DteLapbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DteLapbIndex.setStatus("mandatory")
_MscX25DteLapbFramer_ObjectIdentity = ObjectIdentity
mscX25DteLapbFramer = _MscX25DteLapbFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2)
)
_MscX25DteLapbFramerRowStatusTable_Object = MibTable
mscX25DteLapbFramerRowStatusTable = _MscX25DteLapbFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerRowStatusTable.setStatus("mandatory")
_MscX25DteLapbFramerRowStatusEntry_Object = MibTableRow
mscX25DteLapbFramerRowStatusEntry = _MscX25DteLapbFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 1, 1)
)
mscX25DteLapbFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerRowStatusEntry.setStatus("mandatory")
_MscX25DteLapbFramerRowStatus_Type = RowStatus
_MscX25DteLapbFramerRowStatus_Object = MibTableColumn
mscX25DteLapbFramerRowStatus = _MscX25DteLapbFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 1, 1, 1),
    _MscX25DteLapbFramerRowStatus_Type()
)
mscX25DteLapbFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerRowStatus.setStatus("mandatory")
_MscX25DteLapbFramerComponentName_Type = DisplayString
_MscX25DteLapbFramerComponentName_Object = MibTableColumn
mscX25DteLapbFramerComponentName = _MscX25DteLapbFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 1, 1, 2),
    _MscX25DteLapbFramerComponentName_Type()
)
mscX25DteLapbFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerComponentName.setStatus("mandatory")
_MscX25DteLapbFramerStorageType_Type = StorageType
_MscX25DteLapbFramerStorageType_Object = MibTableColumn
mscX25DteLapbFramerStorageType = _MscX25DteLapbFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 1, 1, 4),
    _MscX25DteLapbFramerStorageType_Type()
)
mscX25DteLapbFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerStorageType.setStatus("mandatory")
_MscX25DteLapbFramerIndex_Type = NonReplicated
_MscX25DteLapbFramerIndex_Object = MibTableColumn
mscX25DteLapbFramerIndex = _MscX25DteLapbFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 1, 1, 10),
    _MscX25DteLapbFramerIndex_Type()
)
mscX25DteLapbFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerIndex.setStatus("mandatory")
_MscX25DteLapbFramerProvTable_Object = MibTable
mscX25DteLapbFramerProvTable = _MscX25DteLapbFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerProvTable.setStatus("mandatory")
_MscX25DteLapbFramerProvEntry_Object = MibTableRow
mscX25DteLapbFramerProvEntry = _MscX25DteLapbFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 10, 1)
)
mscX25DteLapbFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerProvEntry.setStatus("mandatory")
_MscX25DteLapbFramerInterfaceName_Type = Link
_MscX25DteLapbFramerInterfaceName_Object = MibTableColumn
mscX25DteLapbFramerInterfaceName = _MscX25DteLapbFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 10, 1, 1),
    _MscX25DteLapbFramerInterfaceName_Type()
)
mscX25DteLapbFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerInterfaceName.setStatus("mandatory")
_MscX25DteLapbFramerLinkTable_Object = MibTable
mscX25DteLapbFramerLinkTable = _MscX25DteLapbFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 11)
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerLinkTable.setStatus("mandatory")
_MscX25DteLapbFramerLinkEntry_Object = MibTableRow
mscX25DteLapbFramerLinkEntry = _MscX25DteLapbFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 11, 1)
)
mscX25DteLapbFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerLinkEntry.setStatus("mandatory")


class _MscX25DteLapbFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscX25DteLapbFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscX25DteLapbFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscX25DteLapbFramerFlagsBetweenFrames_Object = MibTableColumn
mscX25DteLapbFramerFlagsBetweenFrames = _MscX25DteLapbFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 11, 1, 4),
    _MscX25DteLapbFramerFlagsBetweenFrames_Type()
)
mscX25DteLapbFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerFlagsBetweenFrames.setStatus("mandatory")
_MscX25DteLapbFramerStateTable_Object = MibTable
mscX25DteLapbFramerStateTable = _MscX25DteLapbFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 12)
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerStateTable.setStatus("mandatory")
_MscX25DteLapbFramerStateEntry_Object = MibTableRow
mscX25DteLapbFramerStateEntry = _MscX25DteLapbFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 12, 1)
)
mscX25DteLapbFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerStateEntry.setStatus("mandatory")


class _MscX25DteLapbFramerAdminState_Type(Integer32):
    """Custom type mscX25DteLapbFramerAdminState based on Integer32"""
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


_MscX25DteLapbFramerAdminState_Type.__name__ = "Integer32"
_MscX25DteLapbFramerAdminState_Object = MibTableColumn
mscX25DteLapbFramerAdminState = _MscX25DteLapbFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 12, 1, 1),
    _MscX25DteLapbFramerAdminState_Type()
)
mscX25DteLapbFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerAdminState.setStatus("mandatory")


class _MscX25DteLapbFramerOperationalState_Type(Integer32):
    """Custom type mscX25DteLapbFramerOperationalState based on Integer32"""
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


_MscX25DteLapbFramerOperationalState_Type.__name__ = "Integer32"
_MscX25DteLapbFramerOperationalState_Object = MibTableColumn
mscX25DteLapbFramerOperationalState = _MscX25DteLapbFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 12, 1, 2),
    _MscX25DteLapbFramerOperationalState_Type()
)
mscX25DteLapbFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerOperationalState.setStatus("mandatory")


class _MscX25DteLapbFramerUsageState_Type(Integer32):
    """Custom type mscX25DteLapbFramerUsageState based on Integer32"""
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


_MscX25DteLapbFramerUsageState_Type.__name__ = "Integer32"
_MscX25DteLapbFramerUsageState_Object = MibTableColumn
mscX25DteLapbFramerUsageState = _MscX25DteLapbFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 12, 1, 3),
    _MscX25DteLapbFramerUsageState_Type()
)
mscX25DteLapbFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerUsageState.setStatus("mandatory")
_MscX25DteLapbFramerStatsTable_Object = MibTable
mscX25DteLapbFramerStatsTable = _MscX25DteLapbFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13)
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerStatsTable.setStatus("mandatory")
_MscX25DteLapbFramerStatsEntry_Object = MibTableRow
mscX25DteLapbFramerStatsEntry = _MscX25DteLapbFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1)
)
mscX25DteLapbFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerStatsEntry.setStatus("mandatory")
_MscX25DteLapbFramerFrmToIf_Type = Counter32
_MscX25DteLapbFramerFrmToIf_Object = MibTableColumn
mscX25DteLapbFramerFrmToIf = _MscX25DteLapbFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 1),
    _MscX25DteLapbFramerFrmToIf_Type()
)
mscX25DteLapbFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerFrmToIf.setStatus("obsolete")
_MscX25DteLapbFramerFrmFromIf_Type = Counter32
_MscX25DteLapbFramerFrmFromIf_Object = MibTableColumn
mscX25DteLapbFramerFrmFromIf = _MscX25DteLapbFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 2),
    _MscX25DteLapbFramerFrmFromIf_Type()
)
mscX25DteLapbFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerFrmFromIf.setStatus("obsolete")
_MscX25DteLapbFramerOctetFromIf_Type = Counter32
_MscX25DteLapbFramerOctetFromIf_Object = MibTableColumn
mscX25DteLapbFramerOctetFromIf = _MscX25DteLapbFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 3),
    _MscX25DteLapbFramerOctetFromIf_Type()
)
mscX25DteLapbFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerOctetFromIf.setStatus("obsolete")
_MscX25DteLapbFramerAborts_Type = Counter32
_MscX25DteLapbFramerAborts_Object = MibTableColumn
mscX25DteLapbFramerAborts = _MscX25DteLapbFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 4),
    _MscX25DteLapbFramerAborts_Type()
)
mscX25DteLapbFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerAborts.setStatus("mandatory")
_MscX25DteLapbFramerCrcErrors_Type = Counter32
_MscX25DteLapbFramerCrcErrors_Object = MibTableColumn
mscX25DteLapbFramerCrcErrors = _MscX25DteLapbFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 5),
    _MscX25DteLapbFramerCrcErrors_Type()
)
mscX25DteLapbFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerCrcErrors.setStatus("mandatory")
_MscX25DteLapbFramerLrcErrors_Type = Counter32
_MscX25DteLapbFramerLrcErrors_Object = MibTableColumn
mscX25DteLapbFramerLrcErrors = _MscX25DteLapbFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 6),
    _MscX25DteLapbFramerLrcErrors_Type()
)
mscX25DteLapbFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerLrcErrors.setStatus("mandatory")
_MscX25DteLapbFramerNonOctetErrors_Type = Counter32
_MscX25DteLapbFramerNonOctetErrors_Object = MibTableColumn
mscX25DteLapbFramerNonOctetErrors = _MscX25DteLapbFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 7),
    _MscX25DteLapbFramerNonOctetErrors_Type()
)
mscX25DteLapbFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerNonOctetErrors.setStatus("mandatory")
_MscX25DteLapbFramerOverruns_Type = Counter32
_MscX25DteLapbFramerOverruns_Object = MibTableColumn
mscX25DteLapbFramerOverruns = _MscX25DteLapbFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 8),
    _MscX25DteLapbFramerOverruns_Type()
)
mscX25DteLapbFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerOverruns.setStatus("mandatory")
_MscX25DteLapbFramerUnderruns_Type = Counter32
_MscX25DteLapbFramerUnderruns_Object = MibTableColumn
mscX25DteLapbFramerUnderruns = _MscX25DteLapbFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 9),
    _MscX25DteLapbFramerUnderruns_Type()
)
mscX25DteLapbFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerUnderruns.setStatus("mandatory")
_MscX25DteLapbFramerFrmToIf64_Type = PassportCounter64
_MscX25DteLapbFramerFrmToIf64_Object = MibTableColumn
mscX25DteLapbFramerFrmToIf64 = _MscX25DteLapbFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 14),
    _MscX25DteLapbFramerFrmToIf64_Type()
)
mscX25DteLapbFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerFrmToIf64.setStatus("mandatory")
_MscX25DteLapbFramerFrmFromIf64_Type = PassportCounter64
_MscX25DteLapbFramerFrmFromIf64_Object = MibTableColumn
mscX25DteLapbFramerFrmFromIf64 = _MscX25DteLapbFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 15),
    _MscX25DteLapbFramerFrmFromIf64_Type()
)
mscX25DteLapbFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerFrmFromIf64.setStatus("mandatory")
_MscX25DteLapbFramerOctetFromIf64_Type = PassportCounter64
_MscX25DteLapbFramerOctetFromIf64_Object = MibTableColumn
mscX25DteLapbFramerOctetFromIf64 = _MscX25DteLapbFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 13, 1, 16),
    _MscX25DteLapbFramerOctetFromIf64_Type()
)
mscX25DteLapbFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerOctetFromIf64.setStatus("mandatory")
_MscX25DteLapbFramerUtilTable_Object = MibTable
mscX25DteLapbFramerUtilTable = _MscX25DteLapbFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 14)
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerUtilTable.setStatus("mandatory")
_MscX25DteLapbFramerUtilEntry_Object = MibTableRow
mscX25DteLapbFramerUtilEntry = _MscX25DteLapbFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 14, 1)
)
mscX25DteLapbFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbFramerIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbFramerUtilEntry.setStatus("mandatory")


class _MscX25DteLapbFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscX25DteLapbFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscX25DteLapbFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscX25DteLapbFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscX25DteLapbFramerNormPrioLinkUtilToIf = _MscX25DteLapbFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 14, 1, 1),
    _MscX25DteLapbFramerNormPrioLinkUtilToIf_Type()
)
mscX25DteLapbFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscX25DteLapbFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscX25DteLapbFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscX25DteLapbFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscX25DteLapbFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscX25DteLapbFramerNormPrioLinkUtilFromIf = _MscX25DteLapbFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 2, 14, 1, 3),
    _MscX25DteLapbFramerNormPrioLinkUtilFromIf_Type()
)
mscX25DteLapbFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscX25DteLapbCpTable_Object = MibTable
mscX25DteLapbCpTable = _MscX25DteLapbCpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10)
)
if mibBuilder.loadTexts:
    mscX25DteLapbCpTable.setStatus("mandatory")
_MscX25DteLapbCpEntry_Object = MibTableRow
mscX25DteLapbCpEntry = _MscX25DteLapbCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1)
)
mscX25DteLapbCpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbCpEntry.setStatus("mandatory")


class _MscX25DteLapbStationType_Type(Integer32):
    """Custom type mscX25DteLapbStationType based on Integer32"""
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


_MscX25DteLapbStationType_Type.__name__ = "Integer32"
_MscX25DteLapbStationType_Object = MibTableColumn
mscX25DteLapbStationType = _MscX25DteLapbStationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 1),
    _MscX25DteLapbStationType_Type()
)
mscX25DteLapbStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbStationType.setStatus("mandatory")


class _MscX25DteLapbFrameSequencing_Type(Integer32):
    """Custom type mscX25DteLapbFrameSequencing based on Integer32"""
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


_MscX25DteLapbFrameSequencing_Type.__name__ = "Integer32"
_MscX25DteLapbFrameSequencing_Object = MibTableColumn
mscX25DteLapbFrameSequencing = _MscX25DteLapbFrameSequencing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 2),
    _MscX25DteLapbFrameSequencing_Type()
)
mscX25DteLapbFrameSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbFrameSequencing.setStatus("mandatory")


class _MscX25DteLapbN1FrameSize_Type(Unsigned32):
    """Custom type mscX25DteLapbN1FrameSize based on Unsigned32"""
    defaultValue = 32856

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 32856),
    )


_MscX25DteLapbN1FrameSize_Type.__name__ = "Unsigned32"
_MscX25DteLapbN1FrameSize_Object = MibTableColumn
mscX25DteLapbN1FrameSize = _MscX25DteLapbN1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 3),
    _MscX25DteLapbN1FrameSize_Type()
)
mscX25DteLapbN1FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbN1FrameSize.setStatus("mandatory")


class _MscX25DteLapbKWindowSize_Type(Unsigned32):
    """Custom type mscX25DteLapbKWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DteLapbKWindowSize_Type.__name__ = "Unsigned32"
_MscX25DteLapbKWindowSize_Object = MibTableColumn
mscX25DteLapbKWindowSize = _MscX25DteLapbKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 4),
    _MscX25DteLapbKWindowSize_Type()
)
mscX25DteLapbKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbKWindowSize.setStatus("mandatory")


class _MscX25DteLapbN2TransmitLimit_Type(Unsigned32):
    """Custom type mscX25DteLapbN2TransmitLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscX25DteLapbN2TransmitLimit_Type.__name__ = "Unsigned32"
_MscX25DteLapbN2TransmitLimit_Object = MibTableColumn
mscX25DteLapbN2TransmitLimit = _MscX25DteLapbN2TransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 5),
    _MscX25DteLapbN2TransmitLimit_Type()
)
mscX25DteLapbN2TransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbN2TransmitLimit.setStatus("mandatory")


class _MscX25DteLapbT1AckTimer_Type(Unsigned32):
    """Custom type mscX25DteLapbT1AckTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_MscX25DteLapbT1AckTimer_Type.__name__ = "Unsigned32"
_MscX25DteLapbT1AckTimer_Object = MibTableColumn
mscX25DteLapbT1AckTimer = _MscX25DteLapbT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 6),
    _MscX25DteLapbT1AckTimer_Type()
)
mscX25DteLapbT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbT1AckTimer.setStatus("mandatory")


class _MscX25DteLapbT2AckDelayTimer_Type(Unsigned32):
    """Custom type mscX25DteLapbT2AckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscX25DteLapbT2AckDelayTimer_Type.__name__ = "Unsigned32"
_MscX25DteLapbT2AckDelayTimer_Object = MibTableColumn
mscX25DteLapbT2AckDelayTimer = _MscX25DteLapbT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 7),
    _MscX25DteLapbT2AckDelayTimer_Type()
)
mscX25DteLapbT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbT2AckDelayTimer.setStatus("mandatory")


class _MscX25DteLapbT4IdleProbeTimer_Type(Unsigned32):
    """Custom type mscX25DteLapbT4IdleProbeTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_MscX25DteLapbT4IdleProbeTimer_Type.__name__ = "Unsigned32"
_MscX25DteLapbT4IdleProbeTimer_Object = MibTableColumn
mscX25DteLapbT4IdleProbeTimer = _MscX25DteLapbT4IdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 8),
    _MscX25DteLapbT4IdleProbeTimer_Type()
)
mscX25DteLapbT4IdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbT4IdleProbeTimer.setStatus("mandatory")


class _MscX25DteLapbActionInitiate_Type(Integer32):
    """Custom type mscX25DteLapbActionInitiate based on Integer32"""
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


_MscX25DteLapbActionInitiate_Type.__name__ = "Integer32"
_MscX25DteLapbActionInitiate_Object = MibTableColumn
mscX25DteLapbActionInitiate = _MscX25DteLapbActionInitiate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 9),
    _MscX25DteLapbActionInitiate_Type()
)
mscX25DteLapbActionInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbActionInitiate.setStatus("mandatory")


class _MscX25DteLapbActionRecvDM_Type(Integer32):
    """Custom type mscX25DteLapbActionRecvDM based on Integer32"""
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


_MscX25DteLapbActionRecvDM_Type.__name__ = "Integer32"
_MscX25DteLapbActionRecvDM_Object = MibTableColumn
mscX25DteLapbActionRecvDM = _MscX25DteLapbActionRecvDM_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 10),
    _MscX25DteLapbActionRecvDM_Type()
)
mscX25DteLapbActionRecvDM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbActionRecvDM.setStatus("mandatory")


class _MscX25DteLapbTxQDegradeThreshold_Type(Unsigned32):
    """Custom type mscX25DteLapbTxQDegradeThreshold based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MscX25DteLapbTxQDegradeThreshold_Type.__name__ = "Unsigned32"
_MscX25DteLapbTxQDegradeThreshold_Object = MibTableColumn
mscX25DteLapbTxQDegradeThreshold = _MscX25DteLapbTxQDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 11),
    _MscX25DteLapbTxQDegradeThreshold_Type()
)
mscX25DteLapbTxQDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbTxQDegradeThreshold.setStatus("mandatory")


class _MscX25DteLapbTxQResetThreshold_Type(Unsigned32):
    """Custom type mscX25DteLapbTxQResetThreshold based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MscX25DteLapbTxQResetThreshold_Type.__name__ = "Unsigned32"
_MscX25DteLapbTxQResetThreshold_Object = MibTableColumn
mscX25DteLapbTxQResetThreshold = _MscX25DteLapbTxQResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 10, 1, 12),
    _MscX25DteLapbTxQResetThreshold_Type()
)
mscX25DteLapbTxQResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLapbTxQResetThreshold.setStatus("mandatory")
_MscX25DteLapbStateTable_Object = MibTable
mscX25DteLapbStateTable = _MscX25DteLapbStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 11)
)
if mibBuilder.loadTexts:
    mscX25DteLapbStateTable.setStatus("mandatory")
_MscX25DteLapbStateEntry_Object = MibTableRow
mscX25DteLapbStateEntry = _MscX25DteLapbStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 11, 1)
)
mscX25DteLapbStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbStateEntry.setStatus("mandatory")


class _MscX25DteLapbAdminState_Type(Integer32):
    """Custom type mscX25DteLapbAdminState based on Integer32"""
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


_MscX25DteLapbAdminState_Type.__name__ = "Integer32"
_MscX25DteLapbAdminState_Object = MibTableColumn
mscX25DteLapbAdminState = _MscX25DteLapbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 11, 1, 1),
    _MscX25DteLapbAdminState_Type()
)
mscX25DteLapbAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbAdminState.setStatus("mandatory")


class _MscX25DteLapbOperationalState_Type(Integer32):
    """Custom type mscX25DteLapbOperationalState based on Integer32"""
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


_MscX25DteLapbOperationalState_Type.__name__ = "Integer32"
_MscX25DteLapbOperationalState_Object = MibTableColumn
mscX25DteLapbOperationalState = _MscX25DteLapbOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 11, 1, 2),
    _MscX25DteLapbOperationalState_Type()
)
mscX25DteLapbOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbOperationalState.setStatus("mandatory")


class _MscX25DteLapbUsageState_Type(Integer32):
    """Custom type mscX25DteLapbUsageState based on Integer32"""
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


_MscX25DteLapbUsageState_Type.__name__ = "Integer32"
_MscX25DteLapbUsageState_Object = MibTableColumn
mscX25DteLapbUsageState = _MscX25DteLapbUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 11, 1, 3),
    _MscX25DteLapbUsageState_Type()
)
mscX25DteLapbUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbUsageState.setStatus("mandatory")
_MscX25DteLapbStatusTable_Object = MibTable
mscX25DteLapbStatusTable = _MscX25DteLapbStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12)
)
if mibBuilder.loadTexts:
    mscX25DteLapbStatusTable.setStatus("mandatory")
_MscX25DteLapbStatusEntry_Object = MibTableRow
mscX25DteLapbStatusEntry = _MscX25DteLapbStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12, 1)
)
mscX25DteLapbStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbStatusEntry.setStatus("mandatory")


class _MscX25DteLapbCurrentState_Type(Integer32):
    """Custom type mscX25DteLapbCurrentState based on Integer32"""
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


_MscX25DteLapbCurrentState_Type.__name__ = "Integer32"
_MscX25DteLapbCurrentState_Object = MibTableColumn
mscX25DteLapbCurrentState = _MscX25DteLapbCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12, 1, 1),
    _MscX25DteLapbCurrentState_Type()
)
mscX25DteLapbCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbCurrentState.setStatus("mandatory")


class _MscX25DteLapbLastStateChangeReason_Type(Integer32):
    """Custom type mscX25DteLapbLastStateChangeReason based on Integer32"""
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


_MscX25DteLapbLastStateChangeReason_Type.__name__ = "Integer32"
_MscX25DteLapbLastStateChangeReason_Object = MibTableColumn
mscX25DteLapbLastStateChangeReason = _MscX25DteLapbLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12, 1, 2),
    _MscX25DteLapbLastStateChangeReason_Type()
)
mscX25DteLapbLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbLastStateChangeReason.setStatus("mandatory")


class _MscX25DteLapbFrmrTransmit_Type(HexString):
    """Custom type mscX25DteLapbFrmrTransmit based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MscX25DteLapbFrmrTransmit_Type.__name__ = "HexString"
_MscX25DteLapbFrmrTransmit_Object = MibTableColumn
mscX25DteLapbFrmrTransmit = _MscX25DteLapbFrmrTransmit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12, 1, 3),
    _MscX25DteLapbFrmrTransmit_Type()
)
mscX25DteLapbFrmrTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFrmrTransmit.setStatus("mandatory")


class _MscX25DteLapbFrmrReceive_Type(HexString):
    """Custom type mscX25DteLapbFrmrReceive based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MscX25DteLapbFrmrReceive_Type.__name__ = "HexString"
_MscX25DteLapbFrmrReceive_Object = MibTableColumn
mscX25DteLapbFrmrReceive = _MscX25DteLapbFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12, 1, 4),
    _MscX25DteLapbFrmrReceive_Type()
)
mscX25DteLapbFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbFrmrReceive.setStatus("mandatory")


class _MscX25DteLapbCurrentQueueSize_Type(Unsigned32):
    """Custom type mscX25DteLapbCurrentQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscX25DteLapbCurrentQueueSize_Type.__name__ = "Unsigned32"
_MscX25DteLapbCurrentQueueSize_Object = MibTableColumn
mscX25DteLapbCurrentQueueSize = _MscX25DteLapbCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 12, 1, 5),
    _MscX25DteLapbCurrentQueueSize_Type()
)
mscX25DteLapbCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbCurrentQueueSize.setStatus("mandatory")
_MscX25DteLapbStatsTable_Object = MibTable
mscX25DteLapbStatsTable = _MscX25DteLapbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13)
)
if mibBuilder.loadTexts:
    mscX25DteLapbStatsTable.setStatus("mandatory")
_MscX25DteLapbStatsEntry_Object = MibTableRow
mscX25DteLapbStatsEntry = _MscX25DteLapbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13, 1)
)
mscX25DteLapbStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteLapbIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLapbStatsEntry.setStatus("mandatory")
_MscX25DteLapbStateChanges_Type = Counter32
_MscX25DteLapbStateChanges_Object = MibTableColumn
mscX25DteLapbStateChanges = _MscX25DteLapbStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13, 1, 1),
    _MscX25DteLapbStateChanges_Type()
)
mscX25DteLapbStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbStateChanges.setStatus("mandatory")
_MscX25DteLapbRemoteBusy_Type = Counter32
_MscX25DteLapbRemoteBusy_Object = MibTableColumn
mscX25DteLapbRemoteBusy = _MscX25DteLapbRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13, 1, 2),
    _MscX25DteLapbRemoteBusy_Type()
)
mscX25DteLapbRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbRemoteBusy.setStatus("mandatory")
_MscX25DteLapbTransmitRejectFrames_Type = Counter32
_MscX25DteLapbTransmitRejectFrames_Object = MibTableColumn
mscX25DteLapbTransmitRejectFrames = _MscX25DteLapbTransmitRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13, 1, 3),
    _MscX25DteLapbTransmitRejectFrames_Type()
)
mscX25DteLapbTransmitRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbTransmitRejectFrames.setStatus("mandatory")
_MscX25DteLapbReceiveRejectFrames_Type = Counter32
_MscX25DteLapbReceiveRejectFrames_Object = MibTableColumn
mscX25DteLapbReceiveRejectFrames = _MscX25DteLapbReceiveRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13, 1, 4),
    _MscX25DteLapbReceiveRejectFrames_Type()
)
mscX25DteLapbReceiveRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbReceiveRejectFrames.setStatus("mandatory")
_MscX25DteLapbT1AckTimeout_Type = Counter32
_MscX25DteLapbT1AckTimeout_Object = MibTableColumn
mscX25DteLapbT1AckTimeout = _MscX25DteLapbT1AckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 5, 13, 1, 5),
    _MscX25DteLapbT1AckTimeout_Type()
)
mscX25DteLapbT1AckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteLapbT1AckTimeout.setStatus("mandatory")
_MscX25DtePle_ObjectIdentity = ObjectIdentity
mscX25DtePle = _MscX25DtePle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6)
)
_MscX25DtePleRowStatusTable_Object = MibTable
mscX25DtePleRowStatusTable = _MscX25DtePleRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 1)
)
if mibBuilder.loadTexts:
    mscX25DtePleRowStatusTable.setStatus("mandatory")
_MscX25DtePleRowStatusEntry_Object = MibTableRow
mscX25DtePleRowStatusEntry = _MscX25DtePleRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 1, 1)
)
mscX25DtePleRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePleIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePleRowStatusEntry.setStatus("mandatory")
_MscX25DtePleRowStatus_Type = RowStatus
_MscX25DtePleRowStatus_Object = MibTableColumn
mscX25DtePleRowStatus = _MscX25DtePleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 1, 1, 1),
    _MscX25DtePleRowStatus_Type()
)
mscX25DtePleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleRowStatus.setStatus("mandatory")
_MscX25DtePleComponentName_Type = DisplayString
_MscX25DtePleComponentName_Object = MibTableColumn
mscX25DtePleComponentName = _MscX25DtePleComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 1, 1, 2),
    _MscX25DtePleComponentName_Type()
)
mscX25DtePleComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleComponentName.setStatus("mandatory")
_MscX25DtePleStorageType_Type = StorageType
_MscX25DtePleStorageType_Object = MibTableColumn
mscX25DtePleStorageType = _MscX25DtePleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 1, 1, 4),
    _MscX25DtePleStorageType_Type()
)
mscX25DtePleStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleStorageType.setStatus("mandatory")
_MscX25DtePleIndex_Type = NonReplicated
_MscX25DtePleIndex_Object = MibTableColumn
mscX25DtePleIndex = _MscX25DtePleIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 1, 1, 10),
    _MscX25DtePleIndex_Type()
)
mscX25DtePleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DtePleIndex.setStatus("mandatory")
_MscX25DtePleProvTable_Object = MibTable
mscX25DtePleProvTable = _MscX25DtePleProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 10)
)
if mibBuilder.loadTexts:
    mscX25DtePleProvTable.setStatus("mandatory")
_MscX25DtePleProvEntry_Object = MibTableRow
mscX25DtePleProvEntry = _MscX25DtePleProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 10, 1)
)
mscX25DtePleProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePleIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePleProvEntry.setStatus("mandatory")


class _MscX25DtePleInactivityTimer_Type(Unsigned32):
    """Custom type mscX25DtePleInactivityTimer based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536000),
    )


_MscX25DtePleInactivityTimer_Type.__name__ = "Unsigned32"
_MscX25DtePleInactivityTimer_Object = MibTableColumn
mscX25DtePleInactivityTimer = _MscX25DtePleInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 10, 1, 1),
    _MscX25DtePleInactivityTimer_Type()
)
mscX25DtePleInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePleInactivityTimer.setStatus("mandatory")
_MscX25DtePleOpTable_Object = MibTable
mscX25DtePleOpTable = _MscX25DtePleOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 11)
)
if mibBuilder.loadTexts:
    mscX25DtePleOpTable.setStatus("mandatory")
_MscX25DtePleOpEntry_Object = MibTableRow
mscX25DtePleOpEntry = _MscX25DtePleOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 11, 1)
)
mscX25DtePleOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DtePleIndex"),
)
if mibBuilder.loadTexts:
    mscX25DtePleOpEntry.setStatus("mandatory")


class _MscX25DtePleEncAddrToX25LkupFlrs_Type(Unsigned32):
    """Custom type mscX25DtePleEncAddrToX25LkupFlrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscX25DtePleEncAddrToX25LkupFlrs_Type.__name__ = "Unsigned32"
_MscX25DtePleEncAddrToX25LkupFlrs_Object = MibTableColumn
mscX25DtePleEncAddrToX25LkupFlrs = _MscX25DtePleEncAddrToX25LkupFlrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 11, 1, 1),
    _MscX25DtePleEncAddrToX25LkupFlrs_Type()
)
mscX25DtePleEncAddrToX25LkupFlrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleEncAddrToX25LkupFlrs.setStatus("mandatory")


class _MscX25DtePleLastFailedEncAddr_Type(HexString):
    """Custom type mscX25DtePleLastFailedEncAddr based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_MscX25DtePleLastFailedEncAddr_Type.__name__ = "HexString"
_MscX25DtePleLastFailedEncAddr_Object = MibTableColumn
mscX25DtePleLastFailedEncAddr = _MscX25DtePleLastFailedEncAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 11, 1, 2),
    _MscX25DtePleLastFailedEncAddr_Type()
)
mscX25DtePleLastFailedEncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleLastFailedEncAddr.setStatus("mandatory")


class _MscX25DtePleX25AddrToEncLkupFlrs_Type(Unsigned32):
    """Custom type mscX25DtePleX25AddrToEncLkupFlrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscX25DtePleX25AddrToEncLkupFlrs_Type.__name__ = "Unsigned32"
_MscX25DtePleX25AddrToEncLkupFlrs_Object = MibTableColumn
mscX25DtePleX25AddrToEncLkupFlrs = _MscX25DtePleX25AddrToEncLkupFlrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 11, 1, 4),
    _MscX25DtePleX25AddrToEncLkupFlrs_Type()
)
mscX25DtePleX25AddrToEncLkupFlrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleX25AddrToEncLkupFlrs.setStatus("mandatory")


class _MscX25DtePleLastFailedX25Addr_Type(DigitString):
    """Custom type mscX25DtePleLastFailedX25Addr based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscX25DtePleLastFailedX25Addr_Type.__name__ = "DigitString"
_MscX25DtePleLastFailedX25Addr_Object = MibTableColumn
mscX25DtePleLastFailedX25Addr = _MscX25DtePleLastFailedX25Addr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 6, 11, 1, 5),
    _MscX25DtePleLastFailedX25Addr_Type()
)
mscX25DtePleLastFailedX25Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DtePleLastFailedX25Addr.setStatus("mandatory")
_MscX25DteRg_ObjectIdentity = ObjectIdentity
mscX25DteRg = _MscX25DteRg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7)
)
_MscX25DteRgRowStatusTable_Object = MibTable
mscX25DteRgRowStatusTable = _MscX25DteRgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 1)
)
if mibBuilder.loadTexts:
    mscX25DteRgRowStatusTable.setStatus("mandatory")
_MscX25DteRgRowStatusEntry_Object = MibTableRow
mscX25DteRgRowStatusEntry = _MscX25DteRgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 1, 1)
)
mscX25DteRgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteRgRowStatusEntry.setStatus("mandatory")
_MscX25DteRgRowStatus_Type = RowStatus
_MscX25DteRgRowStatus_Object = MibTableColumn
mscX25DteRgRowStatus = _MscX25DteRgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 1, 1, 1),
    _MscX25DteRgRowStatus_Type()
)
mscX25DteRgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgRowStatus.setStatus("mandatory")
_MscX25DteRgComponentName_Type = DisplayString
_MscX25DteRgComponentName_Object = MibTableColumn
mscX25DteRgComponentName = _MscX25DteRgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 1, 1, 2),
    _MscX25DteRgComponentName_Type()
)
mscX25DteRgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgComponentName.setStatus("mandatory")
_MscX25DteRgStorageType_Type = StorageType
_MscX25DteRgStorageType_Object = MibTableColumn
mscX25DteRgStorageType = _MscX25DteRgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 1, 1, 4),
    _MscX25DteRgStorageType_Type()
)
mscX25DteRgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgStorageType.setStatus("mandatory")


class _MscX25DteRgIndex_Type(Integer32):
    """Custom type mscX25DteRgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_MscX25DteRgIndex_Type.__name__ = "Integer32"
_MscX25DteRgIndex_Object = MibTableColumn
mscX25DteRgIndex = _MscX25DteRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 1, 1, 10),
    _MscX25DteRgIndex_Type()
)
mscX25DteRgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscX25DteRgIndex.setStatus("mandatory")
_MscX25DteRgIfEntryTable_Object = MibTable
mscX25DteRgIfEntryTable = _MscX25DteRgIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 10)
)
if mibBuilder.loadTexts:
    mscX25DteRgIfEntryTable.setStatus("mandatory")
_MscX25DteRgIfEntryEntry_Object = MibTableRow
mscX25DteRgIfEntryEntry = _MscX25DteRgIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 10, 1)
)
mscX25DteRgIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteRgIfEntryEntry.setStatus("mandatory")


class _MscX25DteRgIfAdminStatus_Type(Integer32):
    """Custom type mscX25DteRgIfAdminStatus based on Integer32"""
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


_MscX25DteRgIfAdminStatus_Type.__name__ = "Integer32"
_MscX25DteRgIfAdminStatus_Object = MibTableColumn
mscX25DteRgIfAdminStatus = _MscX25DteRgIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 10, 1, 1),
    _MscX25DteRgIfAdminStatus_Type()
)
mscX25DteRgIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgIfAdminStatus.setStatus("mandatory")


class _MscX25DteRgIfIndex_Type(InterfaceIndex):
    """Custom type mscX25DteRgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscX25DteRgIfIndex_Type.__name__ = "InterfaceIndex"
_MscX25DteRgIfIndex_Object = MibTableColumn
mscX25DteRgIfIndex = _MscX25DteRgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 10, 1, 2),
    _MscX25DteRgIfIndex_Type()
)
mscX25DteRgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgIfIndex.setStatus("mandatory")
_MscX25DteRgProvTable_Object = MibTable
mscX25DteRgProvTable = _MscX25DteRgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 11)
)
if mibBuilder.loadTexts:
    mscX25DteRgProvTable.setStatus("mandatory")
_MscX25DteRgProvEntry_Object = MibTableRow
mscX25DteRgProvEntry = _MscX25DteRgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 11, 1)
)
mscX25DteRgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteRgProvEntry.setStatus("mandatory")
_MscX25DteRgLinkToProtocolPort_Type = Link
_MscX25DteRgLinkToProtocolPort_Object = MibTableColumn
mscX25DteRgLinkToProtocolPort = _MscX25DteRgLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 11, 1, 1),
    _MscX25DteRgLinkToProtocolPort_Type()
)
mscX25DteRgLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgLinkToProtocolPort.setStatus("mandatory")


class _MscX25DteRgLocalAddress_Type(DigitString):
    """Custom type mscX25DteRgLocalAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscX25DteRgLocalAddress_Type.__name__ = "DigitString"
_MscX25DteRgLocalAddress_Object = MibTableColumn
mscX25DteRgLocalAddress = _MscX25DteRgLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 11, 1, 2),
    _MscX25DteRgLocalAddress_Type()
)
mscX25DteRgLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgLocalAddress.setStatus("mandatory")


class _MscX25DteRgMtuSize_Type(Unsigned32):
    """Custom type mscX25DteRgMtuSize based on Unsigned32"""
    defaultValue = 1600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 9188),
    )


_MscX25DteRgMtuSize_Type.__name__ = "Unsigned32"
_MscX25DteRgMtuSize_Object = MibTableColumn
mscX25DteRgMtuSize = _MscX25DteRgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 11, 1, 3),
    _MscX25DteRgMtuSize_Type()
)
mscX25DteRgMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgMtuSize.setStatus("mandatory")
_MscX25DteRgStateTable_Object = MibTable
mscX25DteRgStateTable = _MscX25DteRgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 12)
)
if mibBuilder.loadTexts:
    mscX25DteRgStateTable.setStatus("mandatory")
_MscX25DteRgStateEntry_Object = MibTableRow
mscX25DteRgStateEntry = _MscX25DteRgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 12, 1)
)
mscX25DteRgStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteRgStateEntry.setStatus("mandatory")


class _MscX25DteRgAdminState_Type(Integer32):
    """Custom type mscX25DteRgAdminState based on Integer32"""
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


_MscX25DteRgAdminState_Type.__name__ = "Integer32"
_MscX25DteRgAdminState_Object = MibTableColumn
mscX25DteRgAdminState = _MscX25DteRgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 12, 1, 1),
    _MscX25DteRgAdminState_Type()
)
mscX25DteRgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgAdminState.setStatus("mandatory")


class _MscX25DteRgOperationalState_Type(Integer32):
    """Custom type mscX25DteRgOperationalState based on Integer32"""
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


_MscX25DteRgOperationalState_Type.__name__ = "Integer32"
_MscX25DteRgOperationalState_Object = MibTableColumn
mscX25DteRgOperationalState = _MscX25DteRgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 12, 1, 2),
    _MscX25DteRgOperationalState_Type()
)
mscX25DteRgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgOperationalState.setStatus("mandatory")


class _MscX25DteRgUsageState_Type(Integer32):
    """Custom type mscX25DteRgUsageState based on Integer32"""
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


_MscX25DteRgUsageState_Type.__name__ = "Integer32"
_MscX25DteRgUsageState_Object = MibTableColumn
mscX25DteRgUsageState = _MscX25DteRgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 12, 1, 3),
    _MscX25DteRgUsageState_Type()
)
mscX25DteRgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgUsageState.setStatus("mandatory")
_MscX25DteRgOperStatusTable_Object = MibTable
mscX25DteRgOperStatusTable = _MscX25DteRgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 13)
)
if mibBuilder.loadTexts:
    mscX25DteRgOperStatusTable.setStatus("mandatory")
_MscX25DteRgOperStatusEntry_Object = MibTableRow
mscX25DteRgOperStatusEntry = _MscX25DteRgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 13, 1)
)
mscX25DteRgOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteRgOperStatusEntry.setStatus("mandatory")


class _MscX25DteRgSnmpOperStatus_Type(Integer32):
    """Custom type mscX25DteRgSnmpOperStatus based on Integer32"""
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


_MscX25DteRgSnmpOperStatus_Type.__name__ = "Integer32"
_MscX25DteRgSnmpOperStatus_Object = MibTableColumn
mscX25DteRgSnmpOperStatus = _MscX25DteRgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 13, 1, 1),
    _MscX25DteRgSnmpOperStatus_Type()
)
mscX25DteRgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgSnmpOperStatus.setStatus("mandatory")
_MscX25DteRgLTPlcnTable_Object = MibTable
mscX25DteRgLTPlcnTable = _MscX25DteRgLTPlcnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 210)
)
if mibBuilder.loadTexts:
    mscX25DteRgLTPlcnTable.setStatus("mandatory")
_MscX25DteRgLTPlcnEntry_Object = MibTableRow
mscX25DteRgLTPlcnEntry = _MscX25DteRgLTPlcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 210, 1)
)
mscX25DteRgLTPlcnEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgLTPlcnValue"),
)
if mibBuilder.loadTexts:
    mscX25DteRgLTPlcnEntry.setStatus("mandatory")
_MscX25DteRgLTPlcnValue_Type = Link
_MscX25DteRgLTPlcnValue_Object = MibTableColumn
mscX25DteRgLTPlcnValue = _MscX25DteRgLTPlcnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 210, 1, 1),
    _MscX25DteRgLTPlcnValue_Type()
)
mscX25DteRgLTPlcnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgLTPlcnValue.setStatus("mandatory")
_MscX25DteRgLTPlcnRowStatus_Type = RowStatus
_MscX25DteRgLTPlcnRowStatus_Object = MibTableColumn
mscX25DteRgLTPlcnRowStatus = _MscX25DteRgLTPlcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 210, 1, 2),
    _MscX25DteRgLTPlcnRowStatus_Type()
)
mscX25DteRgLTPlcnRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscX25DteRgLTPlcnRowStatus.setStatus("mandatory")
_MscX25DteRgLtPeerTable_Object = MibTable
mscX25DteRgLtPeerTable = _MscX25DteRgLtPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 211)
)
if mibBuilder.loadTexts:
    mscX25DteRgLtPeerTable.setStatus("mandatory")
_MscX25DteRgLtPeerEntry_Object = MibTableRow
mscX25DteRgLtPeerEntry = _MscX25DteRgLtPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 211, 1)
)
mscX25DteRgLtPeerEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgLtPeerValue"),
)
if mibBuilder.loadTexts:
    mscX25DteRgLtPeerEntry.setStatus("mandatory")
_MscX25DteRgLtPeerValue_Type = Link
_MscX25DteRgLtPeerValue_Object = MibTableColumn
mscX25DteRgLtPeerValue = _MscX25DteRgLtPeerValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 211, 1, 1),
    _MscX25DteRgLtPeerValue_Type()
)
mscX25DteRgLtPeerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRgLtPeerValue.setStatus("mandatory")
_MscX25DteRgLtPeerRowStatus_Type = RowStatus
_MscX25DteRgLtPeerRowStatus_Object = MibTableColumn
mscX25DteRgLtPeerRowStatus = _MscX25DteRgLtPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 211, 1, 2),
    _MscX25DteRgLtPeerRowStatus_Type()
)
mscX25DteRgLtPeerRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscX25DteRgLtPeerRowStatus.setStatus("mandatory")
_MscX25DteRgLcnTable_Object = MibTable
mscX25DteRgLcnTable = _MscX25DteRgLcnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 212)
)
if mibBuilder.loadTexts:
    mscX25DteRgLcnTable.setStatus("mandatory")
_MscX25DteRgLcnEntry_Object = MibTableRow
mscX25DteRgLcnEntry = _MscX25DteRgLcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 212, 1)
)
mscX25DteRgLcnEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteRgLcnValue"),
)
if mibBuilder.loadTexts:
    mscX25DteRgLcnEntry.setStatus("mandatory")


class _MscX25DteRgLcnValue_Type(Integer32):
    """Custom type mscX25DteRgLcnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscX25DteRgLcnValue_Type.__name__ = "Integer32"
_MscX25DteRgLcnValue_Object = MibTableColumn
mscX25DteRgLcnValue = _MscX25DteRgLcnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 7, 212, 1, 1),
    _MscX25DteRgLcnValue_Type()
)
mscX25DteRgLcnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteRgLcnValue.setStatus("mandatory")
_MscX25DteCidDataTable_Object = MibTable
mscX25DteCidDataTable = _MscX25DteCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 20)
)
if mibBuilder.loadTexts:
    mscX25DteCidDataTable.setStatus("mandatory")
_MscX25DteCidDataEntry_Object = MibTableRow
mscX25DteCidDataEntry = _MscX25DteCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 20, 1)
)
mscX25DteCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteCidDataEntry.setStatus("mandatory")


class _MscX25DteCustomerIdentifier_Type(Unsigned32):
    """Custom type mscX25DteCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscX25DteCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscX25DteCustomerIdentifier_Object = MibTableColumn
mscX25DteCustomerIdentifier = _MscX25DteCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 20, 1, 1),
    _MscX25DteCustomerIdentifier_Type()
)
mscX25DteCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteCustomerIdentifier.setStatus("mandatory")
_MscX25DteIfTable_Object = MibTable
mscX25DteIfTable = _MscX25DteIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21)
)
if mibBuilder.loadTexts:
    mscX25DteIfTable.setStatus("mandatory")
_MscX25DteIfEntry_Object = MibTableRow
mscX25DteIfEntry = _MscX25DteIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1)
)
mscX25DteIfEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteIfEntry.setStatus("mandatory")


class _MscX25DteInterfaceMode_Type(Integer32):
    """Custom type mscX25DteInterfaceMode based on Integer32"""
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


_MscX25DteInterfaceMode_Type.__name__ = "Integer32"
_MscX25DteInterfaceMode_Object = MibTableColumn
mscX25DteInterfaceMode = _MscX25DteInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 1),
    _MscX25DteInterfaceMode_Type()
)
mscX25DteInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInterfaceMode.setStatus("mandatory")


class _MscX25DteMaxActiveChannels_Type(Unsigned32):
    """Custom type mscX25DteMaxActiveChannels based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteMaxActiveChannels_Type.__name__ = "Unsigned32"
_MscX25DteMaxActiveChannels_Object = MibTableColumn
mscX25DteMaxActiveChannels = _MscX25DteMaxActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 2),
    _MscX25DteMaxActiveChannels_Type()
)
mscX25DteMaxActiveChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteMaxActiveChannels.setStatus("mandatory")


class _MscX25DteNumberOfPLcn_Type(Unsigned32):
    """Custom type mscX25DteNumberOfPLcn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteNumberOfPLcn_Type.__name__ = "Unsigned32"
_MscX25DteNumberOfPLcn_Object = MibTableColumn
mscX25DteNumberOfPLcn = _MscX25DteNumberOfPLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 3),
    _MscX25DteNumberOfPLcn_Type()
)
mscX25DteNumberOfPLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteNumberOfPLcn.setStatus("mandatory")


class _MscX25DtePacketSequencing_Type(Integer32):
    """Custom type mscX25DtePacketSequencing based on Integer32"""
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


_MscX25DtePacketSequencing_Type.__name__ = "Integer32"
_MscX25DtePacketSequencing_Object = MibTableColumn
mscX25DtePacketSequencing = _MscX25DtePacketSequencing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 4),
    _MscX25DtePacketSequencing_Type()
)
mscX25DtePacketSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DtePacketSequencing.setStatus("mandatory")


class _MscX25DteT20RestartTimer_Type(Unsigned32):
    """Custom type mscX25DteT20RestartTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_MscX25DteT20RestartTimer_Type.__name__ = "Unsigned32"
_MscX25DteT20RestartTimer_Object = MibTableColumn
mscX25DteT20RestartTimer = _MscX25DteT20RestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 5),
    _MscX25DteT20RestartTimer_Type()
)
mscX25DteT20RestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteT20RestartTimer.setStatus("mandatory")


class _MscX25DteT21CallTimer_Type(Unsigned32):
    """Custom type mscX25DteT21CallTimer based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_MscX25DteT21CallTimer_Type.__name__ = "Unsigned32"
_MscX25DteT21CallTimer_Object = MibTableColumn
mscX25DteT21CallTimer = _MscX25DteT21CallTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 6),
    _MscX25DteT21CallTimer_Type()
)
mscX25DteT21CallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteT21CallTimer.setStatus("mandatory")


class _MscX25DteT22ResetTimer_Type(Unsigned32):
    """Custom type mscX25DteT22ResetTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_MscX25DteT22ResetTimer_Type.__name__ = "Unsigned32"
_MscX25DteT22ResetTimer_Object = MibTableColumn
mscX25DteT22ResetTimer = _MscX25DteT22ResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 7),
    _MscX25DteT22ResetTimer_Type()
)
mscX25DteT22ResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteT22ResetTimer.setStatus("mandatory")


class _MscX25DteT23ClearTimer_Type(Unsigned32):
    """Custom type mscX25DteT23ClearTimer based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65536000),
    )


_MscX25DteT23ClearTimer_Type.__name__ = "Unsigned32"
_MscX25DteT23ClearTimer_Object = MibTableColumn
mscX25DteT23ClearTimer = _MscX25DteT23ClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 21, 1, 8),
    _MscX25DteT23ClearTimer_Type()
)
mscX25DteT23ClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteT23ClearTimer.setStatus("mandatory")
_MscX25DteLcnCTable_Object = MibTable
mscX25DteLcnCTable = _MscX25DteLcnCTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22)
)
if mibBuilder.loadTexts:
    mscX25DteLcnCTable.setStatus("mandatory")
_MscX25DteLcnCEntry_Object = MibTableRow
mscX25DteLcnCEntry = _MscX25DteLcnCEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1)
)
mscX25DteLcnCEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteLcnCEntry.setStatus("mandatory")


class _MscX25DteLowestILChannelNumber_Type(Unsigned32):
    """Custom type mscX25DteLowestILChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteLowestILChannelNumber_Type.__name__ = "Unsigned32"
_MscX25DteLowestILChannelNumber_Object = MibTableColumn
mscX25DteLowestILChannelNumber = _MscX25DteLowestILChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1, 1),
    _MscX25DteLowestILChannelNumber_Type()
)
mscX25DteLowestILChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLowestILChannelNumber.setStatus("mandatory")


class _MscX25DteHighestILChannelNumber_Type(Unsigned32):
    """Custom type mscX25DteHighestILChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteHighestILChannelNumber_Type.__name__ = "Unsigned32"
_MscX25DteHighestILChannelNumber_Object = MibTableColumn
mscX25DteHighestILChannelNumber = _MscX25DteHighestILChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1, 2),
    _MscX25DteHighestILChannelNumber_Type()
)
mscX25DteHighestILChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteHighestILChannelNumber.setStatus("mandatory")


class _MscX25DteLowestTLChannelNumber_Type(Unsigned32):
    """Custom type mscX25DteLowestTLChannelNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteLowestTLChannelNumber_Type.__name__ = "Unsigned32"
_MscX25DteLowestTLChannelNumber_Object = MibTableColumn
mscX25DteLowestTLChannelNumber = _MscX25DteLowestTLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1, 3),
    _MscX25DteLowestTLChannelNumber_Type()
)
mscX25DteLowestTLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLowestTLChannelNumber.setStatus("mandatory")


class _MscX25DteHighestTLChannelNumber_Type(Unsigned32):
    """Custom type mscX25DteHighestTLChannelNumber based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteHighestTLChannelNumber_Type.__name__ = "Unsigned32"
_MscX25DteHighestTLChannelNumber_Object = MibTableColumn
mscX25DteHighestTLChannelNumber = _MscX25DteHighestTLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1, 4),
    _MscX25DteHighestTLChannelNumber_Type()
)
mscX25DteHighestTLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteHighestTLChannelNumber.setStatus("mandatory")


class _MscX25DteLowestOLChannelNumber_Type(Unsigned32):
    """Custom type mscX25DteLowestOLChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteLowestOLChannelNumber_Type.__name__ = "Unsigned32"
_MscX25DteLowestOLChannelNumber_Object = MibTableColumn
mscX25DteLowestOLChannelNumber = _MscX25DteLowestOLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1, 5),
    _MscX25DteLowestOLChannelNumber_Type()
)
mscX25DteLowestOLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteLowestOLChannelNumber.setStatus("mandatory")


class _MscX25DteHighestOLChannelNumber_Type(Unsigned32):
    """Custom type mscX25DteHighestOLChannelNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscX25DteHighestOLChannelNumber_Type.__name__ = "Unsigned32"
_MscX25DteHighestOLChannelNumber_Object = MibTableColumn
mscX25DteHighestOLChannelNumber = _MscX25DteHighestOLChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 22, 1, 6),
    _MscX25DteHighestOLChannelNumber_Type()
)
mscX25DteHighestOLChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteHighestOLChannelNumber.setStatus("mandatory")
_MscX25DteDcpTable_Object = MibTable
mscX25DteDcpTable = _MscX25DteDcpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23)
)
if mibBuilder.loadTexts:
    mscX25DteDcpTable.setStatus("mandatory")
_MscX25DteDcpEntry_Object = MibTableRow
mscX25DteDcpEntry = _MscX25DteDcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1)
)
mscX25DteDcpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteDcpEntry.setStatus("mandatory")


class _MscX25DteInPacketSize_Type(Unsigned32):
    """Custom type mscX25DteInPacketSize based on Unsigned32"""
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


_MscX25DteInPacketSize_Type.__name__ = "Unsigned32"
_MscX25DteInPacketSize_Object = MibTableColumn
mscX25DteInPacketSize = _MscX25DteInPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 1),
    _MscX25DteInPacketSize_Type()
)
mscX25DteInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteInPacketSize.setStatus("mandatory")


class _MscX25DteOutPacketSize_Type(Unsigned32):
    """Custom type mscX25DteOutPacketSize based on Unsigned32"""
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


_MscX25DteOutPacketSize_Type.__name__ = "Unsigned32"
_MscX25DteOutPacketSize_Object = MibTableColumn
mscX25DteOutPacketSize = _MscX25DteOutPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 2),
    _MscX25DteOutPacketSize_Type()
)
mscX25DteOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteOutPacketSize.setStatus("mandatory")


class _MscX25DteInWindowSize_Type(Unsigned32):
    """Custom type mscX25DteInWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DteInWindowSize_Type.__name__ = "Unsigned32"
_MscX25DteInWindowSize_Object = MibTableColumn
mscX25DteInWindowSize = _MscX25DteInWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 3),
    _MscX25DteInWindowSize_Type()
)
mscX25DteInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteInWindowSize.setStatus("mandatory")


class _MscX25DteOutWindowSize_Type(Unsigned32):
    """Custom type mscX25DteOutWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscX25DteOutWindowSize_Type.__name__ = "Unsigned32"
_MscX25DteOutWindowSize_Object = MibTableColumn
mscX25DteOutWindowSize = _MscX25DteOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 4),
    _MscX25DteOutWindowSize_Type()
)
mscX25DteOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteOutWindowSize.setStatus("mandatory")


class _MscX25DteAcceptReverseCharging_Type(Integer32):
    """Custom type mscX25DteAcceptReverseCharging based on Integer32"""
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


_MscX25DteAcceptReverseCharging_Type.__name__ = "Integer32"
_MscX25DteAcceptReverseCharging_Object = MibTableColumn
mscX25DteAcceptReverseCharging = _MscX25DteAcceptReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 5),
    _MscX25DteAcceptReverseCharging_Type()
)
mscX25DteAcceptReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteAcceptReverseCharging.setStatus("mandatory")


class _MscX25DteProposeReverseCharging_Type(Integer32):
    """Custom type mscX25DteProposeReverseCharging based on Integer32"""
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


_MscX25DteProposeReverseCharging_Type.__name__ = "Integer32"
_MscX25DteProposeReverseCharging_Object = MibTableColumn
mscX25DteProposeReverseCharging = _MscX25DteProposeReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 6),
    _MscX25DteProposeReverseCharging_Type()
)
mscX25DteProposeReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteProposeReverseCharging.setStatus("mandatory")


class _MscX25DteOutThroughputClassSize_Type(Integer32):
    """Custom type mscX25DteOutThroughputClassSize based on Integer32"""
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


_MscX25DteOutThroughputClassSize_Type.__name__ = "Integer32"
_MscX25DteOutThroughputClassSize_Object = MibTableColumn
mscX25DteOutThroughputClassSize = _MscX25DteOutThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 8),
    _MscX25DteOutThroughputClassSize_Type()
)
mscX25DteOutThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteOutThroughputClassSize.setStatus("mandatory")


class _MscX25DteInThroughputClassSize_Type(Integer32):
    """Custom type mscX25DteInThroughputClassSize based on Integer32"""
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


_MscX25DteInThroughputClassSize_Type.__name__ = "Integer32"
_MscX25DteInThroughputClassSize_Object = MibTableColumn
mscX25DteInThroughputClassSize = _MscX25DteInThroughputClassSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 9),
    _MscX25DteInThroughputClassSize_Type()
)
mscX25DteInThroughputClassSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteInThroughputClassSize.setStatus("mandatory")


class _MscX25DteCugIndex_Type(AsciiString):
    """Custom type mscX25DteCugIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscX25DteCugIndex_Type.__name__ = "AsciiString"
_MscX25DteCugIndex_Object = MibTableColumn
mscX25DteCugIndex = _MscX25DteCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 10),
    _MscX25DteCugIndex_Type()
)
mscX25DteCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteCugIndex.setStatus("mandatory")


class _MscX25DteCugoaIndex_Type(AsciiString):
    """Custom type mscX25DteCugoaIndex based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscX25DteCugoaIndex_Type.__name__ = "AsciiString"
_MscX25DteCugoaIndex_Object = MibTableColumn
mscX25DteCugoaIndex = _MscX25DteCugoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 11),
    _MscX25DteCugoaIndex_Type()
)
mscX25DteCugoaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteCugoaIndex.setStatus("mandatory")


class _MscX25DteChargingInformation_Type(Integer32):
    """Custom type mscX25DteChargingInformation based on Integer32"""
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


_MscX25DteChargingInformation_Type.__name__ = "Integer32"
_MscX25DteChargingInformation_Object = MibTableColumn
mscX25DteChargingInformation = _MscX25DteChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 13),
    _MscX25DteChargingInformation_Type()
)
mscX25DteChargingInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteChargingInformation.setStatus("mandatory")


class _MscX25DteRpoa_Type(AsciiString):
    """Custom type mscX25DteRpoa based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteRpoa_Type.__name__ = "AsciiString"
_MscX25DteRpoa_Object = MibTableColumn
mscX25DteRpoa = _MscX25DteRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 14),
    _MscX25DteRpoa_Type()
)
mscX25DteRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteRpoa.setStatus("mandatory")


class _MscX25DteTrnstDlySlctnAInd_Type(Unsigned32):
    """Custom type mscX25DteTrnstDlySlctnAInd based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_MscX25DteTrnstDlySlctnAInd_Type.__name__ = "Unsigned32"
_MscX25DteTrnstDlySlctnAInd_Object = MibTableColumn
mscX25DteTrnstDlySlctnAInd = _MscX25DteTrnstDlySlctnAInd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 15),
    _MscX25DteTrnstDlySlctnAInd_Type()
)
mscX25DteTrnstDlySlctnAInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteTrnstDlySlctnAInd.setStatus("mandatory")


class _MscX25DteCallingNetworkFax_Type(HexString):
    """Custom type mscX25DteCallingNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteCallingNetworkFax_Type.__name__ = "HexString"
_MscX25DteCallingNetworkFax_Object = MibTableColumn
mscX25DteCallingNetworkFax = _MscX25DteCallingNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 24),
    _MscX25DteCallingNetworkFax_Type()
)
mscX25DteCallingNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteCallingNetworkFax.setStatus("mandatory")


class _MscX25DteCalledNetworkFax_Type(HexString):
    """Custom type mscX25DteCalledNetworkFax based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_MscX25DteCalledNetworkFax_Type.__name__ = "HexString"
_MscX25DteCalledNetworkFax_Object = MibTableColumn
mscX25DteCalledNetworkFax = _MscX25DteCalledNetworkFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 25),
    _MscX25DteCalledNetworkFax_Type()
)
mscX25DteCalledNetworkFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteCalledNetworkFax.setStatus("mandatory")


class _MscX25DteCallUserData_Type(HexString):
    """Custom type mscX25DteCallUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscX25DteCallUserData_Type.__name__ = "HexString"
_MscX25DteCallUserData_Object = MibTableColumn
mscX25DteCallUserData = _MscX25DteCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 23, 1, 26),
    _MscX25DteCallUserData_Type()
)
mscX25DteCallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteCallUserData.setStatus("mandatory")
_MscX25DteIfEntryTable_Object = MibTable
mscX25DteIfEntryTable = _MscX25DteIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 24)
)
if mibBuilder.loadTexts:
    mscX25DteIfEntryTable.setStatus("mandatory")
_MscX25DteIfEntryEntry_Object = MibTableRow
mscX25DteIfEntryEntry = _MscX25DteIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 24, 1)
)
mscX25DteIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteIfEntryEntry.setStatus("mandatory")


class _MscX25DteIfAdminStatus_Type(Integer32):
    """Custom type mscX25DteIfAdminStatus based on Integer32"""
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


_MscX25DteIfAdminStatus_Type.__name__ = "Integer32"
_MscX25DteIfAdminStatus_Object = MibTableColumn
mscX25DteIfAdminStatus = _MscX25DteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 24, 1, 1),
    _MscX25DteIfAdminStatus_Type()
)
mscX25DteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscX25DteIfAdminStatus.setStatus("mandatory")


class _MscX25DteIfIndex_Type(InterfaceIndex):
    """Custom type mscX25DteIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscX25DteIfIndex_Type.__name__ = "InterfaceIndex"
_MscX25DteIfIndex_Object = MibTableColumn
mscX25DteIfIndex = _MscX25DteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 24, 1, 2),
    _MscX25DteIfIndex_Type()
)
mscX25DteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteIfIndex.setStatus("mandatory")
_MscX25DteStateTable_Object = MibTable
mscX25DteStateTable = _MscX25DteStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 25)
)
if mibBuilder.loadTexts:
    mscX25DteStateTable.setStatus("mandatory")
_MscX25DteStateEntry_Object = MibTableRow
mscX25DteStateEntry = _MscX25DteStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 25, 1)
)
mscX25DteStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteStateEntry.setStatus("mandatory")


class _MscX25DteAdminState_Type(Integer32):
    """Custom type mscX25DteAdminState based on Integer32"""
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


_MscX25DteAdminState_Type.__name__ = "Integer32"
_MscX25DteAdminState_Object = MibTableColumn
mscX25DteAdminState = _MscX25DteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 25, 1, 1),
    _MscX25DteAdminState_Type()
)
mscX25DteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteAdminState.setStatus("mandatory")


class _MscX25DteOperationalState_Type(Integer32):
    """Custom type mscX25DteOperationalState based on Integer32"""
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


_MscX25DteOperationalState_Type.__name__ = "Integer32"
_MscX25DteOperationalState_Object = MibTableColumn
mscX25DteOperationalState = _MscX25DteOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 25, 1, 2),
    _MscX25DteOperationalState_Type()
)
mscX25DteOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteOperationalState.setStatus("mandatory")


class _MscX25DteUsageState_Type(Integer32):
    """Custom type mscX25DteUsageState based on Integer32"""
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


_MscX25DteUsageState_Type.__name__ = "Integer32"
_MscX25DteUsageState_Object = MibTableColumn
mscX25DteUsageState = _MscX25DteUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 25, 1, 3),
    _MscX25DteUsageState_Type()
)
mscX25DteUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteUsageState.setStatus("mandatory")
_MscX25DteOperStatusTable_Object = MibTable
mscX25DteOperStatusTable = _MscX25DteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 26)
)
if mibBuilder.loadTexts:
    mscX25DteOperStatusTable.setStatus("mandatory")
_MscX25DteOperStatusEntry_Object = MibTableRow
mscX25DteOperStatusEntry = _MscX25DteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 26, 1)
)
mscX25DteOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteOperStatusEntry.setStatus("mandatory")


class _MscX25DteSnmpOperStatus_Type(Integer32):
    """Custom type mscX25DteSnmpOperStatus based on Integer32"""
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


_MscX25DteSnmpOperStatus_Type.__name__ = "Integer32"
_MscX25DteSnmpOperStatus_Object = MibTableColumn
mscX25DteSnmpOperStatus = _MscX25DteSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 26, 1, 1),
    _MscX25DteSnmpOperStatus_Type()
)
mscX25DteSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteSnmpOperStatus.setStatus("mandatory")
_MscX25DteOpTable_Object = MibTable
mscX25DteOpTable = _MscX25DteOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 27)
)
if mibBuilder.loadTexts:
    mscX25DteOpTable.setStatus("mandatory")
_MscX25DteOpEntry_Object = MibTableRow
mscX25DteOpEntry = _MscX25DteOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 27, 1)
)
mscX25DteOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteOpEntry.setStatus("mandatory")


class _MscX25DteInterfaceState_Type(Integer32):
    """Custom type mscX25DteInterfaceState based on Integer32"""
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


_MscX25DteInterfaceState_Type.__name__ = "Integer32"
_MscX25DteInterfaceState_Object = MibTableColumn
mscX25DteInterfaceState = _MscX25DteInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 27, 1, 1),
    _MscX25DteInterfaceState_Type()
)
mscX25DteInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInterfaceState.setStatus("mandatory")
_MscX25DteStatsTable_Object = MibTable
mscX25DteStatsTable = _MscX25DteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28)
)
if mibBuilder.loadTexts:
    mscX25DteStatsTable.setStatus("mandatory")
_MscX25DteStatsEntry_Object = MibTableRow
mscX25DteStatsEntry = _MscX25DteStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1)
)
mscX25DteStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-X25DteMIB", "mscX25DteIndex"),
)
if mibBuilder.loadTexts:
    mscX25DteStatsEntry.setStatus("mandatory")
_MscX25DteInCalls_Type = Counter32
_MscX25DteInCalls_Object = MibTableColumn
mscX25DteInCalls = _MscX25DteInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 1),
    _MscX25DteInCalls_Type()
)
mscX25DteInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInCalls.setStatus("mandatory")
_MscX25DteInCallRefusals_Type = Counter32
_MscX25DteInCallRefusals_Object = MibTableColumn
mscX25DteInCallRefusals = _MscX25DteInCallRefusals_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 2),
    _MscX25DteInCallRefusals_Type()
)
mscX25DteInCallRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInCallRefusals.setStatus("mandatory")
_MscX25DteInPrvdrInitiatedClrs_Type = Counter32
_MscX25DteInPrvdrInitiatedClrs_Object = MibTableColumn
mscX25DteInPrvdrInitiatedClrs = _MscX25DteInPrvdrInitiatedClrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 3),
    _MscX25DteInPrvdrInitiatedClrs_Type()
)
mscX25DteInPrvdrInitiatedClrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInPrvdrInitiatedClrs.setStatus("mandatory")
_MscX25DteInRmtInitiatedRsts_Type = Counter32
_MscX25DteInRmtInitiatedRsts_Object = MibTableColumn
mscX25DteInRmtInitiatedRsts = _MscX25DteInRmtInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 4),
    _MscX25DteInRmtInitiatedRsts_Type()
)
mscX25DteInRmtInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInRmtInitiatedRsts.setStatus("mandatory")
_MscX25DteInPrvdrInitiatedRsts_Type = Counter32
_MscX25DteInPrvdrInitiatedRsts_Object = MibTableColumn
mscX25DteInPrvdrInitiatedRsts = _MscX25DteInPrvdrInitiatedRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 5),
    _MscX25DteInPrvdrInitiatedRsts_Type()
)
mscX25DteInPrvdrInitiatedRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInPrvdrInitiatedRsts.setStatus("mandatory")
_MscX25DteInRestarts_Type = Counter32
_MscX25DteInRestarts_Object = MibTableColumn
mscX25DteInRestarts = _MscX25DteInRestarts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 6),
    _MscX25DteInRestarts_Type()
)
mscX25DteInRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInRestarts.setStatus("mandatory")
_MscX25DteInDataPackets_Type = Counter32
_MscX25DteInDataPackets_Object = MibTableColumn
mscX25DteInDataPackets = _MscX25DteInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 7),
    _MscX25DteInDataPackets_Type()
)
mscX25DteInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInDataPackets.setStatus("mandatory")
_MscX25DteInPktsAcusdOfPrtclErr_Type = Counter32
_MscX25DteInPktsAcusdOfPrtclErr_Object = MibTableColumn
mscX25DteInPktsAcusdOfPrtclErr = _MscX25DteInPktsAcusdOfPrtclErr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 8),
    _MscX25DteInPktsAcusdOfPrtclErr_Type()
)
mscX25DteInPktsAcusdOfPrtclErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInPktsAcusdOfPrtclErr.setStatus("mandatory")
_MscX25DteInInterruptPackets_Type = Counter32
_MscX25DteInInterruptPackets_Object = MibTableColumn
mscX25DteInInterruptPackets = _MscX25DteInInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 9),
    _MscX25DteInInterruptPackets_Type()
)
mscX25DteInInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInInterruptPackets.setStatus("mandatory")
_MscX25DteOutCallAttempts_Type = Counter32
_MscX25DteOutCallAttempts_Object = MibTableColumn
mscX25DteOutCallAttempts = _MscX25DteOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 10),
    _MscX25DteOutCallAttempts_Type()
)
mscX25DteOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteOutCallAttempts.setStatus("mandatory")
_MscX25DteOutCallFailures_Type = Counter32
_MscX25DteOutCallFailures_Object = MibTableColumn
mscX25DteOutCallFailures = _MscX25DteOutCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 11),
    _MscX25DteOutCallFailures_Type()
)
mscX25DteOutCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteOutCallFailures.setStatus("mandatory")
_MscX25DteOutInterruptPackets_Type = Counter32
_MscX25DteOutInterruptPackets_Object = MibTableColumn
mscX25DteOutInterruptPackets = _MscX25DteOutInterruptPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 12),
    _MscX25DteOutInterruptPackets_Type()
)
mscX25DteOutInterruptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteOutInterruptPackets.setStatus("mandatory")
_MscX25DteOutDataPackets_Type = Counter32
_MscX25DteOutDataPackets_Object = MibTableColumn
mscX25DteOutDataPackets = _MscX25DteOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 13),
    _MscX25DteOutDataPackets_Type()
)
mscX25DteOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteOutDataPackets.setStatus("mandatory")
_MscX25DteOutActiveChannels_Type = Counter32
_MscX25DteOutActiveChannels_Object = MibTableColumn
mscX25DteOutActiveChannels = _MscX25DteOutActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 14),
    _MscX25DteOutActiveChannels_Type()
)
mscX25DteOutActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteOutActiveChannels.setStatus("mandatory")
_MscX25DteInActiveChannels_Type = Counter32
_MscX25DteInActiveChannels_Object = MibTableColumn
mscX25DteInActiveChannels = _MscX25DteInActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 15),
    _MscX25DteInActiveChannels_Type()
)
mscX25DteInActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteInActiveChannels.setStatus("mandatory")
_MscX25DteTwowayActiveChannels_Type = Counter32
_MscX25DteTwowayActiveChannels_Object = MibTableColumn
mscX25DteTwowayActiveChannels = _MscX25DteTwowayActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 16),
    _MscX25DteTwowayActiveChannels_Type()
)
mscX25DteTwowayActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteTwowayActiveChannels.setStatus("mandatory")
_MscX25DteT20RestartTimeouts_Type = Counter32
_MscX25DteT20RestartTimeouts_Object = MibTableColumn
mscX25DteT20RestartTimeouts = _MscX25DteT20RestartTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 17),
    _MscX25DteT20RestartTimeouts_Type()
)
mscX25DteT20RestartTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteT20RestartTimeouts.setStatus("mandatory")
_MscX25DteT21CallTimeouts_Type = Counter32
_MscX25DteT21CallTimeouts_Object = MibTableColumn
mscX25DteT21CallTimeouts = _MscX25DteT21CallTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 18),
    _MscX25DteT21CallTimeouts_Type()
)
mscX25DteT21CallTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteT21CallTimeouts.setStatus("mandatory")
_MscX25DteT22ResetTimeouts_Type = Counter32
_MscX25DteT22ResetTimeouts_Object = MibTableColumn
mscX25DteT22ResetTimeouts = _MscX25DteT22ResetTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 19),
    _MscX25DteT22ResetTimeouts_Type()
)
mscX25DteT22ResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteT22ResetTimeouts.setStatus("mandatory")
_MscX25DteT23ClearTimeouts_Type = Counter32
_MscX25DteT23ClearTimeouts_Object = MibTableColumn
mscX25DteT23ClearTimeouts = _MscX25DteT23ClearTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 90, 28, 1, 20),
    _MscX25DteT23ClearTimeouts_Type()
)
mscX25DteT23ClearTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscX25DteT23ClearTimeouts.setStatus("mandatory")
_X25DteMIB_ObjectIdentity = ObjectIdentity
x25DteMIB = _X25DteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48)
)
_X25DteGroup_ObjectIdentity = ObjectIdentity
x25DteGroup = _X25DteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 1)
)
_X25DteGroupCA_ObjectIdentity = ObjectIdentity
x25DteGroupCA = _X25DteGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 1, 1)
)
_X25DteGroupCA02_ObjectIdentity = ObjectIdentity
x25DteGroupCA02 = _X25DteGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 1, 1, 3)
)
_X25DteGroupCA02A_ObjectIdentity = ObjectIdentity
x25DteGroupCA02A = _X25DteGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 1, 1, 3, 2)
)
_X25DteCapabilities_ObjectIdentity = ObjectIdentity
x25DteCapabilities = _X25DteCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 3)
)
_X25DteCapabilitiesCA_ObjectIdentity = ObjectIdentity
x25DteCapabilitiesCA = _X25DteCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 3, 1)
)
_X25DteCapabilitiesCA02_ObjectIdentity = ObjectIdentity
x25DteCapabilitiesCA02 = _X25DteCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 3, 1, 3)
)
_X25DteCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
x25DteCapabilitiesCA02A = _X25DteCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 48, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-X25DteMIB",
    **{"mscX25Dte": mscX25Dte,
       "mscX25DteRowStatusTable": mscX25DteRowStatusTable,
       "mscX25DteRowStatusEntry": mscX25DteRowStatusEntry,
       "mscX25DteRowStatus": mscX25DteRowStatus,
       "mscX25DteComponentName": mscX25DteComponentName,
       "mscX25DteStorageType": mscX25DteStorageType,
       "mscX25DteIndex": mscX25DteIndex,
       "mscX25DtePeer": mscX25DtePeer,
       "mscX25DtePeerRowStatusTable": mscX25DtePeerRowStatusTable,
       "mscX25DtePeerRowStatusEntry": mscX25DtePeerRowStatusEntry,
       "mscX25DtePeerRowStatus": mscX25DtePeerRowStatus,
       "mscX25DtePeerComponentName": mscX25DtePeerComponentName,
       "mscX25DtePeerStorageType": mscX25DtePeerStorageType,
       "mscX25DtePeerIndex": mscX25DtePeerIndex,
       "mscX25DtePeerIfTable": mscX25DtePeerIfTable,
       "mscX25DtePeerIfEntry": mscX25DtePeerIfEntry,
       "mscX25DtePeerEncAddressType": mscX25DtePeerEncAddressType,
       "mscX25DtePeerEncAddress": mscX25DtePeerEncAddress,
       "mscX25DtePeerX25Address": mscX25DtePeerX25Address,
       "mscX25DtePeerLinkToRemoteGroup": mscX25DtePeerLinkToRemoteGroup,
       "mscX25DtePeerCpTable": mscX25DtePeerCpTable,
       "mscX25DtePeerCpEntry": mscX25DtePeerCpEntry,
       "mscX25DtePeerInPacketSize": mscX25DtePeerInPacketSize,
       "mscX25DtePeerOutPacketSize": mscX25DtePeerOutPacketSize,
       "mscX25DtePeerInWindowSize": mscX25DtePeerInWindowSize,
       "mscX25DtePeerOutWindowSize": mscX25DtePeerOutWindowSize,
       "mscX25DtePeerAcceptReverseCharging": mscX25DtePeerAcceptReverseCharging,
       "mscX25DtePeerProposeReverseCharging": mscX25DtePeerProposeReverseCharging,
       "mscX25DtePeerOutThroughputClassSize": mscX25DtePeerOutThroughputClassSize,
       "mscX25DtePeerInThroughputClassSize": mscX25DtePeerInThroughputClassSize,
       "mscX25DtePeerCugIndex": mscX25DtePeerCugIndex,
       "mscX25DtePeerCugoaIndex": mscX25DtePeerCugoaIndex,
       "mscX25DtePeerNetworkUserIdentifier": mscX25DtePeerNetworkUserIdentifier,
       "mscX25DtePeerChargingInformation": mscX25DtePeerChargingInformation,
       "mscX25DtePeerRpoa": mscX25DtePeerRpoa,
       "mscX25DtePeerTrnstDlySlctnAInd": mscX25DtePeerTrnstDlySlctnAInd,
       "mscX25DtePeerCallingNetworkFax": mscX25DtePeerCallingNetworkFax,
       "mscX25DtePeerCalledNetworkFax": mscX25DtePeerCalledNetworkFax,
       "mscX25DtePeerCallUserData": mscX25DtePeerCallUserData,
       "mscX25DtePeerPEncTable": mscX25DtePeerPEncTable,
       "mscX25DtePeerPEncEntry": mscX25DtePeerPEncEntry,
       "mscX25DtePeerPEncIndex": mscX25DtePeerPEncIndex,
       "mscX25DtePeerPEncValue": mscX25DtePeerPEncValue,
       "mscX25DtePeerPEncRowStatus": mscX25DtePeerPEncRowStatus,
       "mscX25DtePeerLcnTable": mscX25DtePeerLcnTable,
       "mscX25DtePeerLcnEntry": mscX25DtePeerLcnEntry,
       "mscX25DtePeerLcnValue": mscX25DtePeerLcnValue,
       "mscX25DtePLcn": mscX25DtePLcn,
       "mscX25DtePLcnRowStatusTable": mscX25DtePLcnRowStatusTable,
       "mscX25DtePLcnRowStatusEntry": mscX25DtePLcnRowStatusEntry,
       "mscX25DtePLcnRowStatus": mscX25DtePLcnRowStatus,
       "mscX25DtePLcnComponentName": mscX25DtePLcnComponentName,
       "mscX25DtePLcnStorageType": mscX25DtePLcnStorageType,
       "mscX25DtePLcnIndex": mscX25DtePLcnIndex,
       "mscX25DtePLcnProvTable": mscX25DtePLcnProvTable,
       "mscX25DtePLcnProvEntry": mscX25DtePLcnProvEntry,
       "mscX25DtePLcnEncAddressType": mscX25DtePLcnEncAddressType,
       "mscX25DtePLcnEncAddress": mscX25DtePLcnEncAddress,
       "mscX25DtePLcnProtocolEncType": mscX25DtePLcnProtocolEncType,
       "mscX25DtePLcnLinkToRemoteGroup": mscX25DtePLcnLinkToRemoteGroup,
       "mscX25DtePLcnInPacketSize": mscX25DtePLcnInPacketSize,
       "mscX25DtePLcnOutPacketSize": mscX25DtePLcnOutPacketSize,
       "mscX25DtePLcnInWindowSize": mscX25DtePLcnInWindowSize,
       "mscX25DtePLcnOutWindowSize": mscX25DtePLcnOutWindowSize,
       "mscX25DteLcn": mscX25DteLcn,
       "mscX25DteLcnRowStatusTable": mscX25DteLcnRowStatusTable,
       "mscX25DteLcnRowStatusEntry": mscX25DteLcnRowStatusEntry,
       "mscX25DteLcnRowStatus": mscX25DteLcnRowStatus,
       "mscX25DteLcnComponentName": mscX25DteLcnComponentName,
       "mscX25DteLcnStorageType": mscX25DteLcnStorageType,
       "mscX25DteLcnIndex": mscX25DteLcnIndex,
       "mscX25DteLcnStateTable": mscX25DteLcnStateTable,
       "mscX25DteLcnStateEntry": mscX25DteLcnStateEntry,
       "mscX25DteLcnAdminState": mscX25DteLcnAdminState,
       "mscX25DteLcnOperationalState": mscX25DteLcnOperationalState,
       "mscX25DteLcnUsageState": mscX25DteLcnUsageState,
       "mscX25DteLcnCpTable": mscX25DteLcnCpTable,
       "mscX25DteLcnCpEntry": mscX25DteLcnCpEntry,
       "mscX25DteLcnInPacketSize": mscX25DteLcnInPacketSize,
       "mscX25DteLcnOutPacketSize": mscX25DteLcnOutPacketSize,
       "mscX25DteLcnInWindowSize": mscX25DteLcnInWindowSize,
       "mscX25DteLcnOutWindowSize": mscX25DteLcnOutWindowSize,
       "mscX25DteLcnProposeReverseCharging": mscX25DteLcnProposeReverseCharging,
       "mscX25DteLcnFastSelect": mscX25DteLcnFastSelect,
       "mscX25DteLcnOutThroughputClassSize": mscX25DteLcnOutThroughputClassSize,
       "mscX25DteLcnInThroughputClassSize": mscX25DteLcnInThroughputClassSize,
       "mscX25DteLcnCugIndex": mscX25DteLcnCugIndex,
       "mscX25DteLcnCugoaIndex": mscX25DteLcnCugoaIndex,
       "mscX25DteLcnNetworkUserIdentifier": mscX25DteLcnNetworkUserIdentifier,
       "mscX25DteLcnChargingInformation": mscX25DteLcnChargingInformation,
       "mscX25DteLcnRpoa": mscX25DteLcnRpoa,
       "mscX25DteLcnTrnstDlySlctnAInd": mscX25DteLcnTrnstDlySlctnAInd,
       "mscX25DteLcnCallingNetworkFax": mscX25DteLcnCallingNetworkFax,
       "mscX25DteLcnCalledNetworkFax": mscX25DteLcnCalledNetworkFax,
       "mscX25DteLcnCallUserData": mscX25DteLcnCallUserData,
       "mscX25DteLcnLcnStatusTable": mscX25DteLcnLcnStatusTable,
       "mscX25DteLcnLcnStatusEntry": mscX25DteLcnLcnStatusEntry,
       "mscX25DteLcnStatus": mscX25DteLcnStatus,
       "mscX25DteLcnCallDirection": mscX25DteLcnCallDirection,
       "mscX25DteLcnCalledAddress": mscX25DteLcnCalledAddress,
       "mscX25DteLcnCallingAddress": mscX25DteLcnCallingAddress,
       "mscX25DteLcnOriginalCalledAddress": mscX25DteLcnOriginalCalledAddress,
       "mscX25DteLcnStatsTable": mscX25DteLcnStatsTable,
       "mscX25DteLcnStatsEntry": mscX25DteLcnStatsEntry,
       "mscX25DteLcnInUknownProtocols": mscX25DteLcnInUknownProtocols,
       "mscX25DteLcnInDataOctets": mscX25DteLcnInDataOctets,
       "mscX25DteLcnInDataPackets": mscX25DteLcnInDataPackets,
       "mscX25DteLcnInRmtInitiatedRsts": mscX25DteLcnInRmtInitiatedRsts,
       "mscX25DteLcnInPrvdrInitiatedRsts": mscX25DteLcnInPrvdrInitiatedRsts,
       "mscX25DteLcnInInterruptPackets": mscX25DteLcnInInterruptPackets,
       "mscX25DteLcnOutDataOctets": mscX25DteLcnOutDataOctets,
       "mscX25DteLcnOutDataPackets": mscX25DteLcnOutDataPackets,
       "mscX25DteLcnOutInterruptPackets": mscX25DteLcnOutInterruptPackets,
       "mscX25DteLcnT22ResetTimeouts": mscX25DteLcnT22ResetTimeouts,
       "mscX25DteLapb": mscX25DteLapb,
       "mscX25DteLapbRowStatusTable": mscX25DteLapbRowStatusTable,
       "mscX25DteLapbRowStatusEntry": mscX25DteLapbRowStatusEntry,
       "mscX25DteLapbRowStatus": mscX25DteLapbRowStatus,
       "mscX25DteLapbComponentName": mscX25DteLapbComponentName,
       "mscX25DteLapbStorageType": mscX25DteLapbStorageType,
       "mscX25DteLapbIndex": mscX25DteLapbIndex,
       "mscX25DteLapbFramer": mscX25DteLapbFramer,
       "mscX25DteLapbFramerRowStatusTable": mscX25DteLapbFramerRowStatusTable,
       "mscX25DteLapbFramerRowStatusEntry": mscX25DteLapbFramerRowStatusEntry,
       "mscX25DteLapbFramerRowStatus": mscX25DteLapbFramerRowStatus,
       "mscX25DteLapbFramerComponentName": mscX25DteLapbFramerComponentName,
       "mscX25DteLapbFramerStorageType": mscX25DteLapbFramerStorageType,
       "mscX25DteLapbFramerIndex": mscX25DteLapbFramerIndex,
       "mscX25DteLapbFramerProvTable": mscX25DteLapbFramerProvTable,
       "mscX25DteLapbFramerProvEntry": mscX25DteLapbFramerProvEntry,
       "mscX25DteLapbFramerInterfaceName": mscX25DteLapbFramerInterfaceName,
       "mscX25DteLapbFramerLinkTable": mscX25DteLapbFramerLinkTable,
       "mscX25DteLapbFramerLinkEntry": mscX25DteLapbFramerLinkEntry,
       "mscX25DteLapbFramerFlagsBetweenFrames": mscX25DteLapbFramerFlagsBetweenFrames,
       "mscX25DteLapbFramerStateTable": mscX25DteLapbFramerStateTable,
       "mscX25DteLapbFramerStateEntry": mscX25DteLapbFramerStateEntry,
       "mscX25DteLapbFramerAdminState": mscX25DteLapbFramerAdminState,
       "mscX25DteLapbFramerOperationalState": mscX25DteLapbFramerOperationalState,
       "mscX25DteLapbFramerUsageState": mscX25DteLapbFramerUsageState,
       "mscX25DteLapbFramerStatsTable": mscX25DteLapbFramerStatsTable,
       "mscX25DteLapbFramerStatsEntry": mscX25DteLapbFramerStatsEntry,
       "mscX25DteLapbFramerFrmToIf": mscX25DteLapbFramerFrmToIf,
       "mscX25DteLapbFramerFrmFromIf": mscX25DteLapbFramerFrmFromIf,
       "mscX25DteLapbFramerOctetFromIf": mscX25DteLapbFramerOctetFromIf,
       "mscX25DteLapbFramerAborts": mscX25DteLapbFramerAborts,
       "mscX25DteLapbFramerCrcErrors": mscX25DteLapbFramerCrcErrors,
       "mscX25DteLapbFramerLrcErrors": mscX25DteLapbFramerLrcErrors,
       "mscX25DteLapbFramerNonOctetErrors": mscX25DteLapbFramerNonOctetErrors,
       "mscX25DteLapbFramerOverruns": mscX25DteLapbFramerOverruns,
       "mscX25DteLapbFramerUnderruns": mscX25DteLapbFramerUnderruns,
       "mscX25DteLapbFramerFrmToIf64": mscX25DteLapbFramerFrmToIf64,
       "mscX25DteLapbFramerFrmFromIf64": mscX25DteLapbFramerFrmFromIf64,
       "mscX25DteLapbFramerOctetFromIf64": mscX25DteLapbFramerOctetFromIf64,
       "mscX25DteLapbFramerUtilTable": mscX25DteLapbFramerUtilTable,
       "mscX25DteLapbFramerUtilEntry": mscX25DteLapbFramerUtilEntry,
       "mscX25DteLapbFramerNormPrioLinkUtilToIf": mscX25DteLapbFramerNormPrioLinkUtilToIf,
       "mscX25DteLapbFramerNormPrioLinkUtilFromIf": mscX25DteLapbFramerNormPrioLinkUtilFromIf,
       "mscX25DteLapbCpTable": mscX25DteLapbCpTable,
       "mscX25DteLapbCpEntry": mscX25DteLapbCpEntry,
       "mscX25DteLapbStationType": mscX25DteLapbStationType,
       "mscX25DteLapbFrameSequencing": mscX25DteLapbFrameSequencing,
       "mscX25DteLapbN1FrameSize": mscX25DteLapbN1FrameSize,
       "mscX25DteLapbKWindowSize": mscX25DteLapbKWindowSize,
       "mscX25DteLapbN2TransmitLimit": mscX25DteLapbN2TransmitLimit,
       "mscX25DteLapbT1AckTimer": mscX25DteLapbT1AckTimer,
       "mscX25DteLapbT2AckDelayTimer": mscX25DteLapbT2AckDelayTimer,
       "mscX25DteLapbT4IdleProbeTimer": mscX25DteLapbT4IdleProbeTimer,
       "mscX25DteLapbActionInitiate": mscX25DteLapbActionInitiate,
       "mscX25DteLapbActionRecvDM": mscX25DteLapbActionRecvDM,
       "mscX25DteLapbTxQDegradeThreshold": mscX25DteLapbTxQDegradeThreshold,
       "mscX25DteLapbTxQResetThreshold": mscX25DteLapbTxQResetThreshold,
       "mscX25DteLapbStateTable": mscX25DteLapbStateTable,
       "mscX25DteLapbStateEntry": mscX25DteLapbStateEntry,
       "mscX25DteLapbAdminState": mscX25DteLapbAdminState,
       "mscX25DteLapbOperationalState": mscX25DteLapbOperationalState,
       "mscX25DteLapbUsageState": mscX25DteLapbUsageState,
       "mscX25DteLapbStatusTable": mscX25DteLapbStatusTable,
       "mscX25DteLapbStatusEntry": mscX25DteLapbStatusEntry,
       "mscX25DteLapbCurrentState": mscX25DteLapbCurrentState,
       "mscX25DteLapbLastStateChangeReason": mscX25DteLapbLastStateChangeReason,
       "mscX25DteLapbFrmrTransmit": mscX25DteLapbFrmrTransmit,
       "mscX25DteLapbFrmrReceive": mscX25DteLapbFrmrReceive,
       "mscX25DteLapbCurrentQueueSize": mscX25DteLapbCurrentQueueSize,
       "mscX25DteLapbStatsTable": mscX25DteLapbStatsTable,
       "mscX25DteLapbStatsEntry": mscX25DteLapbStatsEntry,
       "mscX25DteLapbStateChanges": mscX25DteLapbStateChanges,
       "mscX25DteLapbRemoteBusy": mscX25DteLapbRemoteBusy,
       "mscX25DteLapbTransmitRejectFrames": mscX25DteLapbTransmitRejectFrames,
       "mscX25DteLapbReceiveRejectFrames": mscX25DteLapbReceiveRejectFrames,
       "mscX25DteLapbT1AckTimeout": mscX25DteLapbT1AckTimeout,
       "mscX25DtePle": mscX25DtePle,
       "mscX25DtePleRowStatusTable": mscX25DtePleRowStatusTable,
       "mscX25DtePleRowStatusEntry": mscX25DtePleRowStatusEntry,
       "mscX25DtePleRowStatus": mscX25DtePleRowStatus,
       "mscX25DtePleComponentName": mscX25DtePleComponentName,
       "mscX25DtePleStorageType": mscX25DtePleStorageType,
       "mscX25DtePleIndex": mscX25DtePleIndex,
       "mscX25DtePleProvTable": mscX25DtePleProvTable,
       "mscX25DtePleProvEntry": mscX25DtePleProvEntry,
       "mscX25DtePleInactivityTimer": mscX25DtePleInactivityTimer,
       "mscX25DtePleOpTable": mscX25DtePleOpTable,
       "mscX25DtePleOpEntry": mscX25DtePleOpEntry,
       "mscX25DtePleEncAddrToX25LkupFlrs": mscX25DtePleEncAddrToX25LkupFlrs,
       "mscX25DtePleLastFailedEncAddr": mscX25DtePleLastFailedEncAddr,
       "mscX25DtePleX25AddrToEncLkupFlrs": mscX25DtePleX25AddrToEncLkupFlrs,
       "mscX25DtePleLastFailedX25Addr": mscX25DtePleLastFailedX25Addr,
       "mscX25DteRg": mscX25DteRg,
       "mscX25DteRgRowStatusTable": mscX25DteRgRowStatusTable,
       "mscX25DteRgRowStatusEntry": mscX25DteRgRowStatusEntry,
       "mscX25DteRgRowStatus": mscX25DteRgRowStatus,
       "mscX25DteRgComponentName": mscX25DteRgComponentName,
       "mscX25DteRgStorageType": mscX25DteRgStorageType,
       "mscX25DteRgIndex": mscX25DteRgIndex,
       "mscX25DteRgIfEntryTable": mscX25DteRgIfEntryTable,
       "mscX25DteRgIfEntryEntry": mscX25DteRgIfEntryEntry,
       "mscX25DteRgIfAdminStatus": mscX25DteRgIfAdminStatus,
       "mscX25DteRgIfIndex": mscX25DteRgIfIndex,
       "mscX25DteRgProvTable": mscX25DteRgProvTable,
       "mscX25DteRgProvEntry": mscX25DteRgProvEntry,
       "mscX25DteRgLinkToProtocolPort": mscX25DteRgLinkToProtocolPort,
       "mscX25DteRgLocalAddress": mscX25DteRgLocalAddress,
       "mscX25DteRgMtuSize": mscX25DteRgMtuSize,
       "mscX25DteRgStateTable": mscX25DteRgStateTable,
       "mscX25DteRgStateEntry": mscX25DteRgStateEntry,
       "mscX25DteRgAdminState": mscX25DteRgAdminState,
       "mscX25DteRgOperationalState": mscX25DteRgOperationalState,
       "mscX25DteRgUsageState": mscX25DteRgUsageState,
       "mscX25DteRgOperStatusTable": mscX25DteRgOperStatusTable,
       "mscX25DteRgOperStatusEntry": mscX25DteRgOperStatusEntry,
       "mscX25DteRgSnmpOperStatus": mscX25DteRgSnmpOperStatus,
       "mscX25DteRgLTPlcnTable": mscX25DteRgLTPlcnTable,
       "mscX25DteRgLTPlcnEntry": mscX25DteRgLTPlcnEntry,
       "mscX25DteRgLTPlcnValue": mscX25DteRgLTPlcnValue,
       "mscX25DteRgLTPlcnRowStatus": mscX25DteRgLTPlcnRowStatus,
       "mscX25DteRgLtPeerTable": mscX25DteRgLtPeerTable,
       "mscX25DteRgLtPeerEntry": mscX25DteRgLtPeerEntry,
       "mscX25DteRgLtPeerValue": mscX25DteRgLtPeerValue,
       "mscX25DteRgLtPeerRowStatus": mscX25DteRgLtPeerRowStatus,
       "mscX25DteRgLcnTable": mscX25DteRgLcnTable,
       "mscX25DteRgLcnEntry": mscX25DteRgLcnEntry,
       "mscX25DteRgLcnValue": mscX25DteRgLcnValue,
       "mscX25DteCidDataTable": mscX25DteCidDataTable,
       "mscX25DteCidDataEntry": mscX25DteCidDataEntry,
       "mscX25DteCustomerIdentifier": mscX25DteCustomerIdentifier,
       "mscX25DteIfTable": mscX25DteIfTable,
       "mscX25DteIfEntry": mscX25DteIfEntry,
       "mscX25DteInterfaceMode": mscX25DteInterfaceMode,
       "mscX25DteMaxActiveChannels": mscX25DteMaxActiveChannels,
       "mscX25DteNumberOfPLcn": mscX25DteNumberOfPLcn,
       "mscX25DtePacketSequencing": mscX25DtePacketSequencing,
       "mscX25DteT20RestartTimer": mscX25DteT20RestartTimer,
       "mscX25DteT21CallTimer": mscX25DteT21CallTimer,
       "mscX25DteT22ResetTimer": mscX25DteT22ResetTimer,
       "mscX25DteT23ClearTimer": mscX25DteT23ClearTimer,
       "mscX25DteLcnCTable": mscX25DteLcnCTable,
       "mscX25DteLcnCEntry": mscX25DteLcnCEntry,
       "mscX25DteLowestILChannelNumber": mscX25DteLowestILChannelNumber,
       "mscX25DteHighestILChannelNumber": mscX25DteHighestILChannelNumber,
       "mscX25DteLowestTLChannelNumber": mscX25DteLowestTLChannelNumber,
       "mscX25DteHighestTLChannelNumber": mscX25DteHighestTLChannelNumber,
       "mscX25DteLowestOLChannelNumber": mscX25DteLowestOLChannelNumber,
       "mscX25DteHighestOLChannelNumber": mscX25DteHighestOLChannelNumber,
       "mscX25DteDcpTable": mscX25DteDcpTable,
       "mscX25DteDcpEntry": mscX25DteDcpEntry,
       "mscX25DteInPacketSize": mscX25DteInPacketSize,
       "mscX25DteOutPacketSize": mscX25DteOutPacketSize,
       "mscX25DteInWindowSize": mscX25DteInWindowSize,
       "mscX25DteOutWindowSize": mscX25DteOutWindowSize,
       "mscX25DteAcceptReverseCharging": mscX25DteAcceptReverseCharging,
       "mscX25DteProposeReverseCharging": mscX25DteProposeReverseCharging,
       "mscX25DteOutThroughputClassSize": mscX25DteOutThroughputClassSize,
       "mscX25DteInThroughputClassSize": mscX25DteInThroughputClassSize,
       "mscX25DteCugIndex": mscX25DteCugIndex,
       "mscX25DteCugoaIndex": mscX25DteCugoaIndex,
       "mscX25DteChargingInformation": mscX25DteChargingInformation,
       "mscX25DteRpoa": mscX25DteRpoa,
       "mscX25DteTrnstDlySlctnAInd": mscX25DteTrnstDlySlctnAInd,
       "mscX25DteCallingNetworkFax": mscX25DteCallingNetworkFax,
       "mscX25DteCalledNetworkFax": mscX25DteCalledNetworkFax,
       "mscX25DteCallUserData": mscX25DteCallUserData,
       "mscX25DteIfEntryTable": mscX25DteIfEntryTable,
       "mscX25DteIfEntryEntry": mscX25DteIfEntryEntry,
       "mscX25DteIfAdminStatus": mscX25DteIfAdminStatus,
       "mscX25DteIfIndex": mscX25DteIfIndex,
       "mscX25DteStateTable": mscX25DteStateTable,
       "mscX25DteStateEntry": mscX25DteStateEntry,
       "mscX25DteAdminState": mscX25DteAdminState,
       "mscX25DteOperationalState": mscX25DteOperationalState,
       "mscX25DteUsageState": mscX25DteUsageState,
       "mscX25DteOperStatusTable": mscX25DteOperStatusTable,
       "mscX25DteOperStatusEntry": mscX25DteOperStatusEntry,
       "mscX25DteSnmpOperStatus": mscX25DteSnmpOperStatus,
       "mscX25DteOpTable": mscX25DteOpTable,
       "mscX25DteOpEntry": mscX25DteOpEntry,
       "mscX25DteInterfaceState": mscX25DteInterfaceState,
       "mscX25DteStatsTable": mscX25DteStatsTable,
       "mscX25DteStatsEntry": mscX25DteStatsEntry,
       "mscX25DteInCalls": mscX25DteInCalls,
       "mscX25DteInCallRefusals": mscX25DteInCallRefusals,
       "mscX25DteInPrvdrInitiatedClrs": mscX25DteInPrvdrInitiatedClrs,
       "mscX25DteInRmtInitiatedRsts": mscX25DteInRmtInitiatedRsts,
       "mscX25DteInPrvdrInitiatedRsts": mscX25DteInPrvdrInitiatedRsts,
       "mscX25DteInRestarts": mscX25DteInRestarts,
       "mscX25DteInDataPackets": mscX25DteInDataPackets,
       "mscX25DteInPktsAcusdOfPrtclErr": mscX25DteInPktsAcusdOfPrtclErr,
       "mscX25DteInInterruptPackets": mscX25DteInInterruptPackets,
       "mscX25DteOutCallAttempts": mscX25DteOutCallAttempts,
       "mscX25DteOutCallFailures": mscX25DteOutCallFailures,
       "mscX25DteOutInterruptPackets": mscX25DteOutInterruptPackets,
       "mscX25DteOutDataPackets": mscX25DteOutDataPackets,
       "mscX25DteOutActiveChannels": mscX25DteOutActiveChannels,
       "mscX25DteInActiveChannels": mscX25DteInActiveChannels,
       "mscX25DteTwowayActiveChannels": mscX25DteTwowayActiveChannels,
       "mscX25DteT20RestartTimeouts": mscX25DteT20RestartTimeouts,
       "mscX25DteT21CallTimeouts": mscX25DteT21CallTimeouts,
       "mscX25DteT22ResetTimeouts": mscX25DteT22ResetTimeouts,
       "mscX25DteT23ClearTimeouts": mscX25DteT23ClearTimeouts,
       "x25DteMIB": x25DteMIB,
       "x25DteGroup": x25DteGroup,
       "x25DteGroupCA": x25DteGroupCA,
       "x25DteGroupCA02": x25DteGroupCA02,
       "x25DteGroupCA02A": x25DteGroupCA02A,
       "x25DteCapabilities": x25DteCapabilities,
       "x25DteCapabilitiesCA": x25DteCapabilitiesCA,
       "x25DteCapabilitiesCA02": x25DteCapabilitiesCA02,
       "x25DteCapabilitiesCA02A": x25DteCapabilitiesCA02A}
)
