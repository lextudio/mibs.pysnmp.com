# SNMP MIB module (APPIAN-LPORT-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-LPORT-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:35 2024
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

(AcNodeId,
 acLport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcNodeId",
    "acLport")

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

acPppLinks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcPppEndDiscriminator(Integer32, TextualConvention):
    status = "current"
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
        *(("localAddress", 2),
          ("macAddress", 4),
          ("magicNumber", 5),
          ("networkAddress", 3),
          ("null", 1),
          ("psndn", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AcPppLinkStatusTable_Object = MibTable
acPppLinkStatusTable = _AcPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    acPppLinkStatusTable.setStatus("current")
_AcPppLinkStatusEntry_Object = MibTableRow
acPppLinkStatusEntry = _AcPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1)
)
acPppLinkStatusEntry.setIndexNames(
    (0, "APPIAN-LPORT-PPP-MIB", "acPppLinkStatusNodeId"),
    (0, "APPIAN-LPORT-PPP-MIB", "acPppLinkStatusTimeSlotIndex"),
)
if mibBuilder.loadTexts:
    acPppLinkStatusEntry.setStatus("current")
_AcPppLinkStatusNodeId_Type = AcNodeId
_AcPppLinkStatusNodeId_Object = MibTableColumn
acPppLinkStatusNodeId = _AcPppLinkStatusNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 1),
    _AcPppLinkStatusNodeId_Type()
)
acPppLinkStatusNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acPppLinkStatusNodeId.setStatus("current")


class _AcPppLinkStatusTimeSlotIndex_Type(Integer32):
    """Custom type acPppLinkStatusTimeSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPppLinkStatusTimeSlotIndex_Type.__name__ = "Integer32"
_AcPppLinkStatusTimeSlotIndex_Object = MibTableColumn
acPppLinkStatusTimeSlotIndex = _AcPppLinkStatusTimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 2),
    _AcPppLinkStatusTimeSlotIndex_Type()
)
acPppLinkStatusTimeSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acPppLinkStatusTimeSlotIndex.setStatus("current")
_AcPppLinkStatusLocalMRU_Type = Integer32
_AcPppLinkStatusLocalMRU_Object = MibTableColumn
acPppLinkStatusLocalMRU = _AcPppLinkStatusLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 3),
    _AcPppLinkStatusLocalMRU_Type()
)
acPppLinkStatusLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalMRU.setStatus("current")
_AcPppLinkStatusRemoteMRU_Type = Integer32
_AcPppLinkStatusRemoteMRU_Object = MibTableColumn
acPppLinkStatusRemoteMRU = _AcPppLinkStatusRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 4),
    _AcPppLinkStatusRemoteMRU_Type()
)
acPppLinkStatusRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteMRU.setStatus("current")
_AcPppLinkStatusLocalToPeerACCMap_Type = Integer32
_AcPppLinkStatusLocalToPeerACCMap_Object = MibTableColumn
acPppLinkStatusLocalToPeerACCMap = _AcPppLinkStatusLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 5),
    _AcPppLinkStatusLocalToPeerACCMap_Type()
)
acPppLinkStatusLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalToPeerACCMap.setStatus("current")
_AcPppLinkStatusPeerToLocalACCMap_Type = Integer32
_AcPppLinkStatusPeerToLocalACCMap_Object = MibTableColumn
acPppLinkStatusPeerToLocalACCMap = _AcPppLinkStatusPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 6),
    _AcPppLinkStatusPeerToLocalACCMap_Type()
)
acPppLinkStatusPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusPeerToLocalACCMap.setStatus("current")


class _AcPppLinkStatusLocalToRemoteProtocolCompression_Type(Integer32):
    """Custom type acPppLinkStatusLocalToRemoteProtocolCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AcPppLinkStatusLocalToRemoteProtocolCompression_Type.__name__ = "Integer32"
_AcPppLinkStatusLocalToRemoteProtocolCompression_Object = MibTableColumn
acPppLinkStatusLocalToRemoteProtocolCompression = _AcPppLinkStatusLocalToRemoteProtocolCompression_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 7),
    _AcPppLinkStatusLocalToRemoteProtocolCompression_Type()
)
acPppLinkStatusLocalToRemoteProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalToRemoteProtocolCompression.setStatus("current")


class _AcPppLinkStatusRemoteToLocalProtocolCompression_Type(Integer32):
    """Custom type acPppLinkStatusRemoteToLocalProtocolCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AcPppLinkStatusRemoteToLocalProtocolCompression_Type.__name__ = "Integer32"
_AcPppLinkStatusRemoteToLocalProtocolCompression_Object = MibTableColumn
acPppLinkStatusRemoteToLocalProtocolCompression = _AcPppLinkStatusRemoteToLocalProtocolCompression_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 8),
    _AcPppLinkStatusRemoteToLocalProtocolCompression_Type()
)
acPppLinkStatusRemoteToLocalProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteToLocalProtocolCompression.setStatus("current")


class _AcPppLinkStatusLocalToRemoteACCompression_Type(Integer32):
    """Custom type acPppLinkStatusLocalToRemoteACCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AcPppLinkStatusLocalToRemoteACCompression_Type.__name__ = "Integer32"
_AcPppLinkStatusLocalToRemoteACCompression_Object = MibTableColumn
acPppLinkStatusLocalToRemoteACCompression = _AcPppLinkStatusLocalToRemoteACCompression_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 9),
    _AcPppLinkStatusLocalToRemoteACCompression_Type()
)
acPppLinkStatusLocalToRemoteACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalToRemoteACCompression.setStatus("current")


class _AcPppLinkStatusRemoteToLocalACCompression_Type(Integer32):
    """Custom type acPppLinkStatusRemoteToLocalACCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AcPppLinkStatusRemoteToLocalACCompression_Type.__name__ = "Integer32"
_AcPppLinkStatusRemoteToLocalACCompression_Object = MibTableColumn
acPppLinkStatusRemoteToLocalACCompression = _AcPppLinkStatusRemoteToLocalACCompression_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 10),
    _AcPppLinkStatusRemoteToLocalACCompression_Type()
)
acPppLinkStatusRemoteToLocalACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteToLocalACCompression.setStatus("current")


class _AcPppLinkStatusTransmitFcsSize_Type(Integer32):
    """Custom type acPppLinkStatusTransmitFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcPppLinkStatusTransmitFcsSize_Type.__name__ = "Integer32"
_AcPppLinkStatusTransmitFcsSize_Object = MibTableColumn
acPppLinkStatusTransmitFcsSize = _AcPppLinkStatusTransmitFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 11),
    _AcPppLinkStatusTransmitFcsSize_Type()
)
acPppLinkStatusTransmitFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusTransmitFcsSize.setStatus("current")


class _AcPppLinkStatusReceiveFcsSize_Type(Integer32):
    """Custom type acPppLinkStatusReceiveFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcPppLinkStatusReceiveFcsSize_Type.__name__ = "Integer32"
_AcPppLinkStatusReceiveFcsSize_Object = MibTableColumn
acPppLinkStatusReceiveFcsSize = _AcPppLinkStatusReceiveFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 12),
    _AcPppLinkStatusReceiveFcsSize_Type()
)
acPppLinkStatusReceiveFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusReceiveFcsSize.setStatus("current")
_AcPppLinkStatusLocalMRRU_Type = Integer32
_AcPppLinkStatusLocalMRRU_Object = MibTableColumn
acPppLinkStatusLocalMRRU = _AcPppLinkStatusLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 13),
    _AcPppLinkStatusLocalMRRU_Type()
)
acPppLinkStatusLocalMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalMRRU.setStatus("current")
_AcPppLinkStatusRemoteMRRU_Type = Integer32
_AcPppLinkStatusRemoteMRRU_Object = MibTableColumn
acPppLinkStatusRemoteMRRU = _AcPppLinkStatusRemoteMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 14),
    _AcPppLinkStatusRemoteMRRU_Type()
)
acPppLinkStatusRemoteMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteMRRU.setStatus("current")
_AcPppLinkStatusLocalEPDClass_Type = AcPppEndDiscriminator
_AcPppLinkStatusLocalEPDClass_Object = MibTableColumn
acPppLinkStatusLocalEPDClass = _AcPppLinkStatusLocalEPDClass_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 15),
    _AcPppLinkStatusLocalEPDClass_Type()
)
acPppLinkStatusLocalEPDClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalEPDClass.setStatus("current")


class _AcPppLinkStatusLocalEPDLength_Type(Integer32):
    """Custom type acPppLinkStatusLocalEPDLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AcPppLinkStatusLocalEPDLength_Type.__name__ = "Integer32"
_AcPppLinkStatusLocalEPDLength_Object = MibTableColumn
acPppLinkStatusLocalEPDLength = _AcPppLinkStatusLocalEPDLength_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 16),
    _AcPppLinkStatusLocalEPDLength_Type()
)
acPppLinkStatusLocalEPDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalEPDLength.setStatus("current")


class _AcPppLinkStatusLocalEPDArray_Type(DisplayString):
    """Custom type acPppLinkStatusLocalEPDArray based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 55),
    )


_AcPppLinkStatusLocalEPDArray_Type.__name__ = "DisplayString"
_AcPppLinkStatusLocalEPDArray_Object = MibTableColumn
acPppLinkStatusLocalEPDArray = _AcPppLinkStatusLocalEPDArray_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 17),
    _AcPppLinkStatusLocalEPDArray_Type()
)
acPppLinkStatusLocalEPDArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusLocalEPDArray.setStatus("current")
_AcPppLinkStatusRemoteEPDClass_Type = AcPppEndDiscriminator
_AcPppLinkStatusRemoteEPDClass_Object = MibTableColumn
acPppLinkStatusRemoteEPDClass = _AcPppLinkStatusRemoteEPDClass_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 18),
    _AcPppLinkStatusRemoteEPDClass_Type()
)
acPppLinkStatusRemoteEPDClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteEPDClass.setStatus("current")


class _AcPppLinkStatusRemoteEPDLength_Type(Integer32):
    """Custom type acPppLinkStatusRemoteEPDLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AcPppLinkStatusRemoteEPDLength_Type.__name__ = "Integer32"
_AcPppLinkStatusRemoteEPDLength_Object = MibTableColumn
acPppLinkStatusRemoteEPDLength = _AcPppLinkStatusRemoteEPDLength_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 19),
    _AcPppLinkStatusRemoteEPDLength_Type()
)
acPppLinkStatusRemoteEPDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteEPDLength.setStatus("current")


class _AcPppLinkStatusRemoteEPDArray_Type(DisplayString):
    """Custom type acPppLinkStatusRemoteEPDArray based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 55),
    )


_AcPppLinkStatusRemoteEPDArray_Type.__name__ = "DisplayString"
_AcPppLinkStatusRemoteEPDArray_Object = MibTableColumn
acPppLinkStatusRemoteEPDArray = _AcPppLinkStatusRemoteEPDArray_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 5, 1, 1, 20),
    _AcPppLinkStatusRemoteEPDArray_Type()
)
acPppLinkStatusRemoteEPDArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPppLinkStatusRemoteEPDArray.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-LPORT-PPP-MIB",
    **{"AcPppEndDiscriminator": AcPppEndDiscriminator,
       "acPppLinks": acPppLinks,
       "acPppLinkStatusTable": acPppLinkStatusTable,
       "acPppLinkStatusEntry": acPppLinkStatusEntry,
       "acPppLinkStatusNodeId": acPppLinkStatusNodeId,
       "acPppLinkStatusTimeSlotIndex": acPppLinkStatusTimeSlotIndex,
       "acPppLinkStatusLocalMRU": acPppLinkStatusLocalMRU,
       "acPppLinkStatusRemoteMRU": acPppLinkStatusRemoteMRU,
       "acPppLinkStatusLocalToPeerACCMap": acPppLinkStatusLocalToPeerACCMap,
       "acPppLinkStatusPeerToLocalACCMap": acPppLinkStatusPeerToLocalACCMap,
       "acPppLinkStatusLocalToRemoteProtocolCompression": acPppLinkStatusLocalToRemoteProtocolCompression,
       "acPppLinkStatusRemoteToLocalProtocolCompression": acPppLinkStatusRemoteToLocalProtocolCompression,
       "acPppLinkStatusLocalToRemoteACCompression": acPppLinkStatusLocalToRemoteACCompression,
       "acPppLinkStatusRemoteToLocalACCompression": acPppLinkStatusRemoteToLocalACCompression,
       "acPppLinkStatusTransmitFcsSize": acPppLinkStatusTransmitFcsSize,
       "acPppLinkStatusReceiveFcsSize": acPppLinkStatusReceiveFcsSize,
       "acPppLinkStatusLocalMRRU": acPppLinkStatusLocalMRRU,
       "acPppLinkStatusRemoteMRRU": acPppLinkStatusRemoteMRRU,
       "acPppLinkStatusLocalEPDClass": acPppLinkStatusLocalEPDClass,
       "acPppLinkStatusLocalEPDLength": acPppLinkStatusLocalEPDLength,
       "acPppLinkStatusLocalEPDArray": acPppLinkStatusLocalEPDArray,
       "acPppLinkStatusRemoteEPDClass": acPppLinkStatusRemoteEPDClass,
       "acPppLinkStatusRemoteEPDLength": acPppLinkStatusRemoteEPDLength,
       "acPppLinkStatusRemoteEPDArray": acPppLinkStatusRemoteEPDArray}
)
