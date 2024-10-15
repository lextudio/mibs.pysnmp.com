# SNMP MIB module (Nortel-Magellan-Passport-VoiceNetworkingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VoiceNetworkingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:35 2024
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
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
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

_SigChan_ObjectIdentity = ObjectIdentity
sigChan = _SigChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115)
)
_SigChanRowStatusTable_Object = MibTable
sigChanRowStatusTable = _SigChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 1)
)
if mibBuilder.loadTexts:
    sigChanRowStatusTable.setStatus("mandatory")
_SigChanRowStatusEntry_Object = MibTableRow
sigChanRowStatusEntry = _SigChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 1, 1)
)
sigChanRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
)
if mibBuilder.loadTexts:
    sigChanRowStatusEntry.setStatus("mandatory")
_SigChanRowStatus_Type = RowStatus
_SigChanRowStatus_Object = MibTableColumn
sigChanRowStatus = _SigChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 1, 1, 1),
    _SigChanRowStatus_Type()
)
sigChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanRowStatus.setStatus("mandatory")
_SigChanComponentName_Type = DisplayString
_SigChanComponentName_Object = MibTableColumn
sigChanComponentName = _SigChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 1, 1, 2),
    _SigChanComponentName_Type()
)
sigChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanComponentName.setStatus("mandatory")
_SigChanStorageType_Type = StorageType
_SigChanStorageType_Object = MibTableColumn
sigChanStorageType = _SigChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 1, 1, 4),
    _SigChanStorageType_Type()
)
sigChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanStorageType.setStatus("mandatory")


class _SigChanIndex_Type(Integer32):
    """Custom type sigChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SigChanIndex_Type.__name__ = "Integer32"
_SigChanIndex_Object = MibTableColumn
sigChanIndex = _SigChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 1, 1, 10),
    _SigChanIndex_Type()
)
sigChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanIndex.setStatus("mandatory")
_SigChanBch_ObjectIdentity = ObjectIdentity
sigChanBch = _SigChanBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7)
)
_SigChanBchRowStatusTable_Object = MibTable
sigChanBchRowStatusTable = _SigChanBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 1)
)
if mibBuilder.loadTexts:
    sigChanBchRowStatusTable.setStatus("mandatory")
_SigChanBchRowStatusEntry_Object = MibTableRow
sigChanBchRowStatusEntry = _SigChanBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 1, 1)
)
sigChanBchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanBchIndex"),
)
if mibBuilder.loadTexts:
    sigChanBchRowStatusEntry.setStatus("mandatory")
_SigChanBchRowStatus_Type = RowStatus
_SigChanBchRowStatus_Object = MibTableColumn
sigChanBchRowStatus = _SigChanBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 1, 1, 1),
    _SigChanBchRowStatus_Type()
)
sigChanBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchRowStatus.setStatus("mandatory")
_SigChanBchComponentName_Type = DisplayString
_SigChanBchComponentName_Object = MibTableColumn
sigChanBchComponentName = _SigChanBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 1, 1, 2),
    _SigChanBchComponentName_Type()
)
sigChanBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchComponentName.setStatus("mandatory")
_SigChanBchStorageType_Type = StorageType
_SigChanBchStorageType_Object = MibTableColumn
sigChanBchStorageType = _SigChanBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 1, 1, 4),
    _SigChanBchStorageType_Type()
)
sigChanBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchStorageType.setStatus("mandatory")


class _SigChanBchIndex_Type(Integer32):
    """Custom type sigChanBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 331),
    )


_SigChanBchIndex_Type.__name__ = "Integer32"
_SigChanBchIndex_Object = MibTableColumn
sigChanBchIndex = _SigChanBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 1, 1, 10),
    _SigChanBchIndex_Type()
)
sigChanBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanBchIndex.setStatus("mandatory")
_SigChanBchOperTable_Object = MibTable
sigChanBchOperTable = _SigChanBchOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 4)
)
if mibBuilder.loadTexts:
    sigChanBchOperTable.setStatus("mandatory")
_SigChanBchOperEntry_Object = MibTableRow
sigChanBchOperEntry = _SigChanBchOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 4, 1)
)
sigChanBchOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanBchIndex"),
)
if mibBuilder.loadTexts:
    sigChanBchOperEntry.setStatus("mandatory")


class _SigChanBchStatus_Type(Integer32):
    """Custom type sigChanBchStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("egress", 5),
          ("egressMaintenance", 8),
          ("idle", 2),
          ("idleMaintenance", 6),
          ("ingress", 4),
          ("ingressMaintenance", 7),
          ("maintB", 1),
          ("outOfService", 9),
          ("unknown", 0))
    )


_SigChanBchStatus_Type.__name__ = "Integer32"
_SigChanBchStatus_Object = MibTableColumn
sigChanBchStatus = _SigChanBchStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 4, 1, 1),
    _SigChanBchStatus_Type()
)
sigChanBchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchStatus.setStatus("mandatory")


class _SigChanBchTimeSlot_Type(Unsigned32):
    """Custom type sigChanBchTimeSlot based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SigChanBchTimeSlot_Type.__name__ = "Unsigned32"
_SigChanBchTimeSlot_Object = MibTableColumn
sigChanBchTimeSlot = _SigChanBchTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 4, 1, 2),
    _SigChanBchTimeSlot_Type()
)
sigChanBchTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchTimeSlot.setStatus("mandatory")


class _SigChanBchVsrInstance_Type(Unsigned32):
    """Custom type sigChanBchVsrInstance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SigChanBchVsrInstance_Type.__name__ = "Unsigned32"
_SigChanBchVsrInstance_Object = MibTableColumn
sigChanBchVsrInstance = _SigChanBchVsrInstance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 4, 1, 3),
    _SigChanBchVsrInstance_Type()
)
sigChanBchVsrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchVsrInstance.setStatus("mandatory")


class _SigChanBchCalledDirectoryNumber_Type(DigitString):
    """Custom type sigChanBchCalledDirectoryNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SigChanBchCalledDirectoryNumber_Type.__name__ = "DigitString"
_SigChanBchCalledDirectoryNumber_Object = MibTableColumn
sigChanBchCalledDirectoryNumber = _SigChanBchCalledDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 7, 4, 1, 4),
    _SigChanBchCalledDirectoryNumber_Type()
)
sigChanBchCalledDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanBchCalledDirectoryNumber.setStatus("mandatory")
_SigChanGw_ObjectIdentity = ObjectIdentity
sigChanGw = _SigChanGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15)
)
_SigChanGwRowStatusTable_Object = MibTable
sigChanGwRowStatusTable = _SigChanGwRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 1)
)
if mibBuilder.loadTexts:
    sigChanGwRowStatusTable.setStatus("mandatory")
_SigChanGwRowStatusEntry_Object = MibTableRow
sigChanGwRowStatusEntry = _SigChanGwRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 1, 1)
)
sigChanGwRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanGwIndex"),
)
if mibBuilder.loadTexts:
    sigChanGwRowStatusEntry.setStatus("mandatory")
_SigChanGwRowStatus_Type = RowStatus
_SigChanGwRowStatus_Object = MibTableColumn
sigChanGwRowStatus = _SigChanGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 1, 1, 1),
    _SigChanGwRowStatus_Type()
)
sigChanGwRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwRowStatus.setStatus("mandatory")
_SigChanGwComponentName_Type = DisplayString
_SigChanGwComponentName_Object = MibTableColumn
sigChanGwComponentName = _SigChanGwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 1, 1, 2),
    _SigChanGwComponentName_Type()
)
sigChanGwComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwComponentName.setStatus("mandatory")
_SigChanGwStorageType_Type = StorageType
_SigChanGwStorageType_Object = MibTableColumn
sigChanGwStorageType = _SigChanGwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 1, 1, 4),
    _SigChanGwStorageType_Type()
)
sigChanGwStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwStorageType.setStatus("mandatory")
_SigChanGwIndex_Type = NonReplicated
_SigChanGwIndex_Object = MibTableColumn
sigChanGwIndex = _SigChanGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 1, 1, 10),
    _SigChanGwIndex_Type()
)
sigChanGwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanGwIndex.setStatus("mandatory")
_SigChanGwStatsTable_Object = MibTable
sigChanGwStatsTable = _SigChanGwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 101)
)
if mibBuilder.loadTexts:
    sigChanGwStatsTable.setStatus("mandatory")
_SigChanGwStatsEntry_Object = MibTableRow
sigChanGwStatsEntry = _SigChanGwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 101, 1)
)
sigChanGwStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanGwIndex"),
)
if mibBuilder.loadTexts:
    sigChanGwStatsEntry.setStatus("mandatory")
_SigChanGwRequiredConversions_Type = Counter32
_SigChanGwRequiredConversions_Object = MibTableColumn
sigChanGwRequiredConversions = _SigChanGwRequiredConversions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 101, 1, 1),
    _SigChanGwRequiredConversions_Type()
)
sigChanGwRequiredConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwRequiredConversions.setStatus("mandatory")
_SigChanGwUnsupportedConversions_Type = Counter32
_SigChanGwUnsupportedConversions_Object = MibTableColumn
sigChanGwUnsupportedConversions = _SigChanGwUnsupportedConversions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 101, 1, 2),
    _SigChanGwUnsupportedConversions_Type()
)
sigChanGwUnsupportedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwUnsupportedConversions.setStatus("mandatory")
_SigChanGwGwcTable_Object = MibTable
sigChanGwGwcTable = _SigChanGwGwcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 301)
)
if mibBuilder.loadTexts:
    sigChanGwGwcTable.setStatus("obsolete")
_SigChanGwGwcEntry_Object = MibTableRow
sigChanGwGwcEntry = _SigChanGwGwcEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 301, 1)
)
sigChanGwGwcEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanGwIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanGwGwcIndex"),
)
if mibBuilder.loadTexts:
    sigChanGwGwcEntry.setStatus("obsolete")


class _SigChanGwGwcIndex_Type(Integer32):
    """Custom type sigChanGwGwcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("analogAndCasPG", 2),
          ("etsiQsigPG", 0),
          ("euroIsdnPG", 3),
          ("mcdnPG", 4),
          ("mcdnUniPG", 5),
          ("nisPG", 1))
    )


_SigChanGwGwcIndex_Type.__name__ = "Integer32"
_SigChanGwGwcIndex_Object = MibTableColumn
sigChanGwGwcIndex = _SigChanGwGwcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 301, 1, 1),
    _SigChanGwGwcIndex_Type()
)
sigChanGwGwcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanGwGwcIndex.setStatus("obsolete")


class _SigChanGwGwcValue_Type(Integer32):
    """Custom type sigChanGwGwcValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doubleEndedGw", 2),
          ("nativePG", 4),
          ("noGw", 0),
          ("singleEndedGw", 1),
          ("singleOrDoubleEndedGw", 3))
    )


_SigChanGwGwcValue_Type.__name__ = "Integer32"
_SigChanGwGwcValue_Object = MibTableColumn
sigChanGwGwcValue = _SigChanGwGwcValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 301, 1, 2),
    _SigChanGwGwcValue_Type()
)
sigChanGwGwcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwGwcValue.setStatus("obsolete")
_SigChanGwGatewayCapTable_Object = MibTable
sigChanGwGatewayCapTable = _SigChanGwGatewayCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 302)
)
if mibBuilder.loadTexts:
    sigChanGwGatewayCapTable.setStatus("mandatory")
_SigChanGwGatewayCapEntry_Object = MibTableRow
sigChanGwGatewayCapEntry = _SigChanGwGatewayCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 302, 1)
)
sigChanGwGatewayCapEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanGwIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanGwGatewayCapIndex"),
)
if mibBuilder.loadTexts:
    sigChanGwGatewayCapEntry.setStatus("mandatory")


class _SigChanGwGatewayCapIndex_Type(Integer32):
    """Custom type sigChanGwGatewayCapIndex based on Integer32"""
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
        *(("analogAndCasPG", 2),
          ("etsiQsigPG", 0),
          ("euroIsdnPG", 3),
          ("mcdnPG", 1))
    )


_SigChanGwGatewayCapIndex_Type.__name__ = "Integer32"
_SigChanGwGatewayCapIndex_Object = MibTableColumn
sigChanGwGatewayCapIndex = _SigChanGwGatewayCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 302, 1, 1),
    _SigChanGwGatewayCapIndex_Type()
)
sigChanGwGatewayCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanGwGatewayCapIndex.setStatus("mandatory")


class _SigChanGwGatewayCapValue_Type(Integer32):
    """Custom type sigChanGwGatewayCapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doubleEndedGw", 2),
          ("nativePG", 4),
          ("noGw", 0),
          ("singleEndedGw", 1),
          ("singleOrDoubleEndedGw", 3))
    )


_SigChanGwGatewayCapValue_Type.__name__ = "Integer32"
_SigChanGwGatewayCapValue_Object = MibTableColumn
sigChanGwGatewayCapValue = _SigChanGwGatewayCapValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 15, 302, 1, 2),
    _SigChanGwGatewayCapValue_Type()
)
sigChanGwGatewayCapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanGwGatewayCapValue.setStatus("mandatory")
_SigChanNcas_ObjectIdentity = ObjectIdentity
sigChanNcas = _SigChanNcas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16)
)
_SigChanNcasRowStatusTable_Object = MibTable
sigChanNcasRowStatusTable = _SigChanNcasRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 1)
)
if mibBuilder.loadTexts:
    sigChanNcasRowStatusTable.setStatus("mandatory")
_SigChanNcasRowStatusEntry_Object = MibTableRow
sigChanNcasRowStatusEntry = _SigChanNcasRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 1, 1)
)
sigChanNcasRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanNcasIndex"),
)
if mibBuilder.loadTexts:
    sigChanNcasRowStatusEntry.setStatus("mandatory")
_SigChanNcasRowStatus_Type = RowStatus
_SigChanNcasRowStatus_Object = MibTableColumn
sigChanNcasRowStatus = _SigChanNcasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 1, 1, 1),
    _SigChanNcasRowStatus_Type()
)
sigChanNcasRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasRowStatus.setStatus("mandatory")
_SigChanNcasComponentName_Type = DisplayString
_SigChanNcasComponentName_Object = MibTableColumn
sigChanNcasComponentName = _SigChanNcasComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 1, 1, 2),
    _SigChanNcasComponentName_Type()
)
sigChanNcasComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasComponentName.setStatus("mandatory")
_SigChanNcasStorageType_Type = StorageType
_SigChanNcasStorageType_Object = MibTableColumn
sigChanNcasStorageType = _SigChanNcasStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 1, 1, 4),
    _SigChanNcasStorageType_Type()
)
sigChanNcasStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasStorageType.setStatus("mandatory")


class _SigChanNcasIndex_Type(Integer32):
    """Custom type sigChanNcasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SigChanNcasIndex_Type.__name__ = "Integer32"
_SigChanNcasIndex_Object = MibTableColumn
sigChanNcasIndex = _SigChanNcasIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 1, 1, 10),
    _SigChanNcasIndex_Type()
)
sigChanNcasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanNcasIndex.setStatus("mandatory")
_SigChanNcasOperTable_Object = MibTable
sigChanNcasOperTable = _SigChanNcasOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 100)
)
if mibBuilder.loadTexts:
    sigChanNcasOperTable.setStatus("mandatory")
_SigChanNcasOperEntry_Object = MibTableRow
sigChanNcasOperEntry = _SigChanNcasOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 100, 1)
)
sigChanNcasOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanNcasIndex"),
)
if mibBuilder.loadTexts:
    sigChanNcasOperEntry.setStatus("mandatory")


class _SigChanNcasDirection_Type(Integer32):
    """Custom type sigChanNcasDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_SigChanNcasDirection_Type.__name__ = "Integer32"
_SigChanNcasDirection_Object = MibTableColumn
sigChanNcasDirection = _SigChanNcasDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 100, 1, 1),
    _SigChanNcasDirection_Type()
)
sigChanNcasDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasDirection.setStatus("mandatory")


class _SigChanNcasCallReference_Type(Hex):
    """Custom type sigChanNcasCallReference based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SigChanNcasCallReference_Type.__name__ = "Hex"
_SigChanNcasCallReference_Object = MibTableColumn
sigChanNcasCallReference = _SigChanNcasCallReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 100, 1, 2),
    _SigChanNcasCallReference_Type()
)
sigChanNcasCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasCallReference.setStatus("mandatory")


class _SigChanNcasCalledDirectoryNumber_Type(DigitString):
    """Custom type sigChanNcasCalledDirectoryNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SigChanNcasCalledDirectoryNumber_Type.__name__ = "DigitString"
_SigChanNcasCalledDirectoryNumber_Object = MibTableColumn
sigChanNcasCalledDirectoryNumber = _SigChanNcasCalledDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 100, 1, 3),
    _SigChanNcasCalledDirectoryNumber_Type()
)
sigChanNcasCalledDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasCalledDirectoryNumber.setStatus("mandatory")


class _SigChanNcasDuration_Type(Unsigned32):
    """Custom type sigChanNcasDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNcasDuration_Type.__name__ = "Unsigned32"
_SigChanNcasDuration_Object = MibTableColumn
sigChanNcasDuration = _SigChanNcasDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 16, 100, 1, 4),
    _SigChanNcasDuration_Type()
)
sigChanNcasDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNcasDuration.setStatus("mandatory")
_SigChanICmap_ObjectIdentity = ObjectIdentity
sigChanICmap = _SigChanICmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18)
)
_SigChanICmapRowStatusTable_Object = MibTable
sigChanICmapRowStatusTable = _SigChanICmapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 1)
)
if mibBuilder.loadTexts:
    sigChanICmapRowStatusTable.setStatus("mandatory")
_SigChanICmapRowStatusEntry_Object = MibTableRow
sigChanICmapRowStatusEntry = _SigChanICmapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 1, 1)
)
sigChanICmapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanICmapIndex"),
)
if mibBuilder.loadTexts:
    sigChanICmapRowStatusEntry.setStatus("mandatory")
_SigChanICmapRowStatus_Type = RowStatus
_SigChanICmapRowStatus_Object = MibTableColumn
sigChanICmapRowStatus = _SigChanICmapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 1, 1, 1),
    _SigChanICmapRowStatus_Type()
)
sigChanICmapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapRowStatus.setStatus("mandatory")
_SigChanICmapComponentName_Type = DisplayString
_SigChanICmapComponentName_Object = MibTableColumn
sigChanICmapComponentName = _SigChanICmapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 1, 1, 2),
    _SigChanICmapComponentName_Type()
)
sigChanICmapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanICmapComponentName.setStatus("mandatory")
_SigChanICmapStorageType_Type = StorageType
_SigChanICmapStorageType_Object = MibTableColumn
sigChanICmapStorageType = _SigChanICmapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 1, 1, 4),
    _SigChanICmapStorageType_Type()
)
sigChanICmapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanICmapStorageType.setStatus("mandatory")
_SigChanICmapIndex_Type = NonReplicated
_SigChanICmapIndex_Object = MibTableColumn
sigChanICmapIndex = _SigChanICmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 1, 1, 10),
    _SigChanICmapIndex_Type()
)
sigChanICmapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanICmapIndex.setStatus("mandatory")
_SigChanICmapIntCauseTable_Object = MibTable
sigChanICmapIntCauseTable = _SigChanICmapIntCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100)
)
if mibBuilder.loadTexts:
    sigChanICmapIntCauseTable.setStatus("mandatory")
_SigChanICmapIntCauseEntry_Object = MibTableRow
sigChanICmapIntCauseEntry = _SigChanICmapIntCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1)
)
sigChanICmapIntCauseEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanICmapIndex"),
)
if mibBuilder.loadTexts:
    sigChanICmapIntCauseEntry.setStatus("mandatory")


class _SigChanICmapEgressLinkOutOfServCause_Type(Unsigned32):
    """Custom type sigChanICmapEgressLinkOutOfServCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapEgressLinkOutOfServCause_Type.__name__ = "Unsigned32"
_SigChanICmapEgressLinkOutOfServCause_Object = MibTableColumn
sigChanICmapEgressLinkOutOfServCause = _SigChanICmapEgressLinkOutOfServCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 1),
    _SigChanICmapEgressLinkOutOfServCause_Type()
)
sigChanICmapEgressLinkOutOfServCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapEgressLinkOutOfServCause.setStatus("mandatory")


class _SigChanICmapChanOrCircNotAvailCause_Type(Unsigned32):
    """Custom type sigChanICmapChanOrCircNotAvailCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapChanOrCircNotAvailCause_Type.__name__ = "Unsigned32"
_SigChanICmapChanOrCircNotAvailCause_Object = MibTableColumn
sigChanICmapChanOrCircNotAvailCause = _SigChanICmapChanOrCircNotAvailCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 2),
    _SigChanICmapChanOrCircNotAvailCause_Type()
)
sigChanICmapChanOrCircNotAvailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapChanOrCircNotAvailCause.setStatus("mandatory")


class _SigChanICmapTempFailureCause_Type(Unsigned32):
    """Custom type sigChanICmapTempFailureCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapTempFailureCause_Type.__name__ = "Unsigned32"
_SigChanICmapTempFailureCause_Object = MibTableColumn
sigChanICmapTempFailureCause = _SigChanICmapTempFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 3),
    _SigChanICmapTempFailureCause_Type()
)
sigChanICmapTempFailureCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapTempFailureCause.setStatus("mandatory")


class _SigChanICmapSwitchCongestCause_Type(Unsigned32):
    """Custom type sigChanICmapSwitchCongestCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapSwitchCongestCause_Type.__name__ = "Unsigned32"
_SigChanICmapSwitchCongestCause_Object = MibTableColumn
sigChanICmapSwitchCongestCause = _SigChanICmapSwitchCongestCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 4),
    _SigChanICmapSwitchCongestCause_Type()
)
sigChanICmapSwitchCongestCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapSwitchCongestCause.setStatus("mandatory")


class _SigChanICmapReqChanOrCircNotAvailCause_Type(Unsigned32):
    """Custom type sigChanICmapReqChanOrCircNotAvailCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapReqChanOrCircNotAvailCause_Type.__name__ = "Unsigned32"
_SigChanICmapReqChanOrCircNotAvailCause_Object = MibTableColumn
sigChanICmapReqChanOrCircNotAvailCause = _SigChanICmapReqChanOrCircNotAvailCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 5),
    _SigChanICmapReqChanOrCircNotAvailCause_Type()
)
sigChanICmapReqChanOrCircNotAvailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapReqChanOrCircNotAvailCause.setStatus("mandatory")


class _SigChanICmapResourceUnavailCause_Type(Unsigned32):
    """Custom type sigChanICmapResourceUnavailCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapResourceUnavailCause_Type.__name__ = "Unsigned32"
_SigChanICmapResourceUnavailCause_Object = MibTableColumn
sigChanICmapResourceUnavailCause = _SigChanICmapResourceUnavailCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 6),
    _SigChanICmapResourceUnavailCause_Type()
)
sigChanICmapResourceUnavailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapResourceUnavailCause.setStatus("mandatory")


class _SigChanICmapServNotAllowedCause_Type(Unsigned32):
    """Custom type sigChanICmapServNotAllowedCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapServNotAllowedCause_Type.__name__ = "Unsigned32"
_SigChanICmapServNotAllowedCause_Object = MibTableColumn
sigChanICmapServNotAllowedCause = _SigChanICmapServNotAllowedCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 7),
    _SigChanICmapServNotAllowedCause_Type()
)
sigChanICmapServNotAllowedCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapServNotAllowedCause.setStatus("mandatory")


class _SigChanICmapNoSuchChannelCause_Type(Unsigned32):
    """Custom type sigChanICmapNoSuchChannelCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapNoSuchChannelCause_Type.__name__ = "Unsigned32"
_SigChanICmapNoSuchChannelCause_Object = MibTableColumn
sigChanICmapNoSuchChannelCause = _SigChanICmapNoSuchChannelCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 8),
    _SigChanICmapNoSuchChannelCause_Type()
)
sigChanICmapNoSuchChannelCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapNoSuchChannelCause.setStatus("mandatory")


class _SigChanICmapIncompatDestCause_Type(Unsigned32):
    """Custom type sigChanICmapIncompatDestCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_SigChanICmapIncompatDestCause_Type.__name__ = "Unsigned32"
_SigChanICmapIncompatDestCause_Object = MibTableColumn
sigChanICmapIncompatDestCause = _SigChanICmapIncompatDestCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 18, 100, 1, 9),
    _SigChanICmapIncompatDestCause_Type()
)
sigChanICmapIncompatDestCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanICmapIncompatDestCause.setStatus("mandatory")
_SigChanCidDataTable_Object = MibTable
sigChanCidDataTable = _SigChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 100)
)
if mibBuilder.loadTexts:
    sigChanCidDataTable.setStatus("mandatory")
_SigChanCidDataEntry_Object = MibTableRow
sigChanCidDataEntry = _SigChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 100, 1)
)
sigChanCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
)
if mibBuilder.loadTexts:
    sigChanCidDataEntry.setStatus("mandatory")


class _SigChanCustomerIdentifier_Type(Unsigned32):
    """Custom type sigChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_SigChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_SigChanCustomerIdentifier_Object = MibTableColumn
sigChanCustomerIdentifier = _SigChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 100, 1, 1),
    _SigChanCustomerIdentifier_Type()
)
sigChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanCustomerIdentifier.setStatus("mandatory")
_SigChanIfEntryTable_Object = MibTable
sigChanIfEntryTable = _SigChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 101)
)
if mibBuilder.loadTexts:
    sigChanIfEntryTable.setStatus("mandatory")
_SigChanIfEntryEntry_Object = MibTableRow
sigChanIfEntryEntry = _SigChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 101, 1)
)
sigChanIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
)
if mibBuilder.loadTexts:
    sigChanIfEntryEntry.setStatus("mandatory")


class _SigChanIfAdminStatus_Type(Integer32):
    """Custom type sigChanIfAdminStatus based on Integer32"""
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


_SigChanIfAdminStatus_Type.__name__ = "Integer32"
_SigChanIfAdminStatus_Object = MibTableColumn
sigChanIfAdminStatus = _SigChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 101, 1, 1),
    _SigChanIfAdminStatus_Type()
)
sigChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanIfAdminStatus.setStatus("mandatory")


class _SigChanIfIndex_Type(InterfaceIndex):
    """Custom type sigChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SigChanIfIndex_Type.__name__ = "InterfaceIndex"
_SigChanIfIndex_Object = MibTableColumn
sigChanIfIndex = _SigChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 101, 1, 2),
    _SigChanIfIndex_Type()
)
sigChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanIfIndex.setStatus("mandatory")
_SigChanOperStatusTable_Object = MibTable
sigChanOperStatusTable = _SigChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 102)
)
if mibBuilder.loadTexts:
    sigChanOperStatusTable.setStatus("mandatory")
_SigChanOperStatusEntry_Object = MibTableRow
sigChanOperStatusEntry = _SigChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 102, 1)
)
sigChanOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
)
if mibBuilder.loadTexts:
    sigChanOperStatusEntry.setStatus("mandatory")


class _SigChanSnmpOperStatus_Type(Integer32):
    """Custom type sigChanSnmpOperStatus based on Integer32"""
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


_SigChanSnmpOperStatus_Type.__name__ = "Integer32"
_SigChanSnmpOperStatus_Object = MibTableColumn
sigChanSnmpOperStatus = _SigChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 102, 1, 1),
    _SigChanSnmpOperStatus_Type()
)
sigChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanSnmpOperStatus.setStatus("mandatory")
_SigChanStateTable_Object = MibTable
sigChanStateTable = _SigChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 103)
)
if mibBuilder.loadTexts:
    sigChanStateTable.setStatus("mandatory")
_SigChanStateEntry_Object = MibTableRow
sigChanStateEntry = _SigChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 103, 1)
)
sigChanStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
)
if mibBuilder.loadTexts:
    sigChanStateEntry.setStatus("mandatory")


class _SigChanAdminState_Type(Integer32):
    """Custom type sigChanAdminState based on Integer32"""
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


_SigChanAdminState_Type.__name__ = "Integer32"
_SigChanAdminState_Object = MibTableColumn
sigChanAdminState = _SigChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 103, 1, 1),
    _SigChanAdminState_Type()
)
sigChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanAdminState.setStatus("mandatory")


class _SigChanOperationalState_Type(Integer32):
    """Custom type sigChanOperationalState based on Integer32"""
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


_SigChanOperationalState_Type.__name__ = "Integer32"
_SigChanOperationalState_Object = MibTableColumn
sigChanOperationalState = _SigChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 103, 1, 2),
    _SigChanOperationalState_Type()
)
sigChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanOperationalState.setStatus("mandatory")


class _SigChanUsageState_Type(Integer32):
    """Custom type sigChanUsageState based on Integer32"""
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


_SigChanUsageState_Type.__name__ = "Integer32"
_SigChanUsageState_Object = MibTableColumn
sigChanUsageState = _SigChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 103, 1, 3),
    _SigChanUsageState_Type()
)
sigChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanUsageState.setStatus("mandatory")
_SigChanProvTable_Object = MibTable
sigChanProvTable = _SigChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 104)
)
if mibBuilder.loadTexts:
    sigChanProvTable.setStatus("mandatory")
_SigChanProvEntry_Object = MibTableRow
sigChanProvEntry = _SigChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 104, 1)
)
sigChanProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
)
if mibBuilder.loadTexts:
    sigChanProvEntry.setStatus("mandatory")


class _SigChanCommentText_Type(AsciiString):
    """Custom type sigChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SigChanCommentText_Type.__name__ = "AsciiString"
_SigChanCommentText_Object = MibTableColumn
sigChanCommentText = _SigChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 104, 1, 1),
    _SigChanCommentText_Type()
)
sigChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanCommentText.setStatus("mandatory")


class _SigChanOctothorpeEod_Type(Integer32):
    """Custom type sigChanOctothorpeEod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_SigChanOctothorpeEod_Type.__name__ = "Integer32"
_SigChanOctothorpeEod_Object = MibTableColumn
sigChanOctothorpeEod = _SigChanOctothorpeEod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 104, 1, 2),
    _SigChanOctothorpeEod_Type()
)
sigChanOctothorpeEod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanOctothorpeEod.setStatus("mandatory")


class _SigChanForceNpiTon_Type(Integer32):
    """Custom type sigChanForceNpiTon based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_SigChanForceNpiTon_Type.__name__ = "Integer32"
_SigChanForceNpiTon_Object = MibTableColumn
sigChanForceNpiTon = _SigChanForceNpiTon_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 104, 1, 3),
    _SigChanForceNpiTon_Type()
)
sigChanForceNpiTon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanForceNpiTon.setStatus("mandatory")


class _SigChanDefaultNpiTon_Type(Integer32):
    """Custom type sigChanDefaultNpiTon based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("casUnknown", 12),
          ("international", 1),
          ("national", 2),
          ("p0", 4),
          ("p1", 5),
          ("p2", 6),
          ("p3", 7),
          ("p4", 8),
          ("p5", 9),
          ("p6", 10),
          ("p7", 11),
          ("subscriber", 3),
          ("unknown", 0))
    )


_SigChanDefaultNpiTon_Type.__name__ = "Integer32"
_SigChanDefaultNpiTon_Object = MibTableColumn
sigChanDefaultNpiTon = _SigChanDefaultNpiTon_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 104, 1, 4),
    _SigChanDefaultNpiTon_Type()
)
sigChanDefaultNpiTon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanDefaultNpiTon.setStatus("mandatory")
_SigChanSubroutesTable_Object = MibTable
sigChanSubroutesTable = _SigChanSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 307)
)
if mibBuilder.loadTexts:
    sigChanSubroutesTable.setStatus("mandatory")
_SigChanSubroutesEntry_Object = MibTableRow
sigChanSubroutesEntry = _SigChanSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 307, 1)
)
sigChanSubroutesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanSubroutesValue"),
)
if mibBuilder.loadTexts:
    sigChanSubroutesEntry.setStatus("mandatory")
_SigChanSubroutesValue_Type = Link
_SigChanSubroutesValue_Object = MibTableColumn
sigChanSubroutesValue = _SigChanSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 307, 1, 1),
    _SigChanSubroutesValue_Type()
)
sigChanSubroutesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanSubroutesValue.setStatus("mandatory")
_SigChanSubroutesRowStatus_Type = RowStatus
_SigChanSubroutesRowStatus_Object = MibTableColumn
sigChanSubroutesRowStatus = _SigChanSubroutesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 307, 1, 2),
    _SigChanSubroutesRowStatus_Type()
)
sigChanSubroutesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sigChanSubroutesRowStatus.setStatus("mandatory")
_SigChanDegradedSubroutesTable_Object = MibTable
sigChanDegradedSubroutesTable = _SigChanDegradedSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 308)
)
if mibBuilder.loadTexts:
    sigChanDegradedSubroutesTable.setStatus("mandatory")
_SigChanDegradedSubroutesEntry_Object = MibTableRow
sigChanDegradedSubroutesEntry = _SigChanDegradedSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 308, 1)
)
sigChanDegradedSubroutesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanDegradedSubroutesValue"),
)
if mibBuilder.loadTexts:
    sigChanDegradedSubroutesEntry.setStatus("mandatory")
_SigChanDegradedSubroutesValue_Type = RowPointer
_SigChanDegradedSubroutesValue_Object = MibTableColumn
sigChanDegradedSubroutesValue = _SigChanDegradedSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 308, 1, 1),
    _SigChanDegradedSubroutesValue_Type()
)
sigChanDegradedSubroutesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanDegradedSubroutesValue.setStatus("mandatory")
_VRoute_ObjectIdentity = ObjectIdentity
vRoute = _VRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116)
)
_VRouteRowStatusTable_Object = MibTable
vRouteRowStatusTable = _VRouteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 1)
)
if mibBuilder.loadTexts:
    vRouteRowStatusTable.setStatus("mandatory")
_VRouteRowStatusEntry_Object = MibTableRow
vRouteRowStatusEntry = _VRouteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 1, 1)
)
vRouteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteRowStatusEntry.setStatus("mandatory")
_VRouteRowStatus_Type = RowStatus
_VRouteRowStatus_Object = MibTableColumn
vRouteRowStatus = _VRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 1, 1, 1),
    _VRouteRowStatus_Type()
)
vRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteRowStatus.setStatus("mandatory")
_VRouteComponentName_Type = DisplayString
_VRouteComponentName_Object = MibTableColumn
vRouteComponentName = _VRouteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 1, 1, 2),
    _VRouteComponentName_Type()
)
vRouteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteComponentName.setStatus("mandatory")
_VRouteStorageType_Type = StorageType
_VRouteStorageType_Object = MibTableColumn
vRouteStorageType = _VRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 1, 1, 4),
    _VRouteStorageType_Type()
)
vRouteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteStorageType.setStatus("mandatory")


class _VRouteIndex_Type(Integer32):
    """Custom type vRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VRouteIndex_Type.__name__ = "Integer32"
_VRouteIndex_Object = MibTableColumn
vRouteIndex = _VRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 1, 1, 10),
    _VRouteIndex_Type()
)
vRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteIndex.setStatus("mandatory")
_VRouteDebug_ObjectIdentity = ObjectIdentity
vRouteDebug = _VRouteDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2)
)
_VRouteDebugRowStatusTable_Object = MibTable
vRouteDebugRowStatusTable = _VRouteDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2, 1)
)
if mibBuilder.loadTexts:
    vRouteDebugRowStatusTable.setStatus("mandatory")
_VRouteDebugRowStatusEntry_Object = MibTableRow
vRouteDebugRowStatusEntry = _VRouteDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2, 1, 1)
)
vRouteDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDebugIndex"),
)
if mibBuilder.loadTexts:
    vRouteDebugRowStatusEntry.setStatus("mandatory")
_VRouteDebugRowStatus_Type = RowStatus
_VRouteDebugRowStatus_Object = MibTableColumn
vRouteDebugRowStatus = _VRouteDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2, 1, 1, 1),
    _VRouteDebugRowStatus_Type()
)
vRouteDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDebugRowStatus.setStatus("mandatory")
_VRouteDebugComponentName_Type = DisplayString
_VRouteDebugComponentName_Object = MibTableColumn
vRouteDebugComponentName = _VRouteDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2, 1, 1, 2),
    _VRouteDebugComponentName_Type()
)
vRouteDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDebugComponentName.setStatus("mandatory")
_VRouteDebugStorageType_Type = StorageType
_VRouteDebugStorageType_Object = MibTableColumn
vRouteDebugStorageType = _VRouteDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2, 1, 1, 4),
    _VRouteDebugStorageType_Type()
)
vRouteDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDebugStorageType.setStatus("mandatory")
_VRouteDebugIndex_Type = NonReplicated
_VRouteDebugIndex_Object = MibTableColumn
vRouteDebugIndex = _VRouteDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 2, 1, 1, 10),
    _VRouteDebugIndex_Type()
)
vRouteDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteDebugIndex.setStatus("mandatory")
_VRouteInterface_ObjectIdentity = ObjectIdentity
vRouteInterface = _VRouteInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3)
)
_VRouteInterfaceRowStatusTable_Object = MibTable
vRouteInterfaceRowStatusTable = _VRouteInterfaceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 1)
)
if mibBuilder.loadTexts:
    vRouteInterfaceRowStatusTable.setStatus("mandatory")
_VRouteInterfaceRowStatusEntry_Object = MibTableRow
vRouteInterfaceRowStatusEntry = _VRouteInterfaceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 1, 1)
)
vRouteInterfaceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteInterfaceIndex"),
)
if mibBuilder.loadTexts:
    vRouteInterfaceRowStatusEntry.setStatus("mandatory")
_VRouteInterfaceRowStatus_Type = RowStatus
_VRouteInterfaceRowStatus_Object = MibTableColumn
vRouteInterfaceRowStatus = _VRouteInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 1, 1, 1),
    _VRouteInterfaceRowStatus_Type()
)
vRouteInterfaceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteInterfaceRowStatus.setStatus("mandatory")
_VRouteInterfaceComponentName_Type = DisplayString
_VRouteInterfaceComponentName_Object = MibTableColumn
vRouteInterfaceComponentName = _VRouteInterfaceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 1, 1, 2),
    _VRouteInterfaceComponentName_Type()
)
vRouteInterfaceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteInterfaceComponentName.setStatus("mandatory")
_VRouteInterfaceStorageType_Type = StorageType
_VRouteInterfaceStorageType_Object = MibTableColumn
vRouteInterfaceStorageType = _VRouteInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 1, 1, 4),
    _VRouteInterfaceStorageType_Type()
)
vRouteInterfaceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteInterfaceStorageType.setStatus("mandatory")
_VRouteInterfaceIndex_Type = NonReplicated
_VRouteInterfaceIndex_Object = MibTableColumn
vRouteInterfaceIndex = _VRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 1, 1, 10),
    _VRouteInterfaceIndex_Type()
)
vRouteInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteInterfaceIndex.setStatus("mandatory")
_VRouteInterfaceProvTable_Object = MibTable
vRouteInterfaceProvTable = _VRouteInterfaceProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10)
)
if mibBuilder.loadTexts:
    vRouteInterfaceProvTable.setStatus("mandatory")
_VRouteInterfaceProvEntry_Object = MibTableRow
vRouteInterfaceProvEntry = _VRouteInterfaceProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1)
)
vRouteInterfaceProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteInterfaceIndex"),
)
if mibBuilder.loadTexts:
    vRouteInterfaceProvEntry.setStatus("mandatory")


class _VRouteInterfaceIngressAudioGain_Type(Integer32):
    """Custom type vRouteInterfaceIngressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_VRouteInterfaceIngressAudioGain_Type.__name__ = "Integer32"
_VRouteInterfaceIngressAudioGain_Object = MibTableColumn
vRouteInterfaceIngressAudioGain = _VRouteInterfaceIngressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 1),
    _VRouteInterfaceIngressAudioGain_Type()
)
vRouteInterfaceIngressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceIngressAudioGain.setStatus("mandatory")


class _VRouteInterfaceEgressAudioGain_Type(Integer32):
    """Custom type vRouteInterfaceEgressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_VRouteInterfaceEgressAudioGain_Type.__name__ = "Integer32"
_VRouteInterfaceEgressAudioGain_Object = MibTableColumn
vRouteInterfaceEgressAudioGain = _VRouteInterfaceEgressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 2),
    _VRouteInterfaceEgressAudioGain_Type()
)
vRouteInterfaceEgressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceEgressAudioGain.setStatus("mandatory")


class _VRouteInterfaceTandemPassThrough_Type(Integer32):
    """Custom type vRouteInterfaceTandemPassThrough based on Integer32"""
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


_VRouteInterfaceTandemPassThrough_Type.__name__ = "Integer32"
_VRouteInterfaceTandemPassThrough_Object = MibTableColumn
vRouteInterfaceTandemPassThrough = _VRouteInterfaceTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 3),
    _VRouteInterfaceTandemPassThrough_Type()
)
vRouteInterfaceTandemPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceTandemPassThrough.setStatus("mandatory")


class _VRouteInterfaceEchoCancellation_Type(Integer32):
    """Custom type vRouteInterfaceEchoCancellation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VRouteInterfaceEchoCancellation_Type.__name__ = "Integer32"
_VRouteInterfaceEchoCancellation_Object = MibTableColumn
vRouteInterfaceEchoCancellation = _VRouteInterfaceEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 5),
    _VRouteInterfaceEchoCancellation_Type()
)
vRouteInterfaceEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceEchoCancellation.setStatus("obsolete")


class _VRouteInterfaceComfortNoiseCap_Type(Integer32):
    """Custom type vRouteInterfaceComfortNoiseCap based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-78, -78),
        ValueRangeConstraint(-65, -65),
        ValueRangeConstraint(-60, -60),
        ValueRangeConstraint(-54, -54),
        ValueRangeConstraint(-52, -52),
        ValueRangeConstraint(-50, -50),
        ValueRangeConstraint(-48, -48),
        ValueRangeConstraint(-46, -46),
        ValueRangeConstraint(-44, -44),
        ValueRangeConstraint(-42, -42),
        ValueRangeConstraint(-40, -40),
    )


_VRouteInterfaceComfortNoiseCap_Type.__name__ = "Integer32"
_VRouteInterfaceComfortNoiseCap_Object = MibTableColumn
vRouteInterfaceComfortNoiseCap = _VRouteInterfaceComfortNoiseCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 6),
    _VRouteInterfaceComfortNoiseCap_Type()
)
vRouteInterfaceComfortNoiseCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceComfortNoiseCap.setStatus("mandatory")


class _VRouteInterfaceSpeechHangoverTime_Type(Unsigned32):
    """Custom type vRouteInterfaceSpeechHangoverTime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_VRouteInterfaceSpeechHangoverTime_Type.__name__ = "Unsigned32"
_VRouteInterfaceSpeechHangoverTime_Object = MibTableColumn
vRouteInterfaceSpeechHangoverTime = _VRouteInterfaceSpeechHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 7),
    _VRouteInterfaceSpeechHangoverTime_Type()
)
vRouteInterfaceSpeechHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceSpeechHangoverTime.setStatus("mandatory")


class _VRouteInterfaceFaxHangoverTimeG711G726_Type(Unsigned32):
    """Custom type vRouteInterfaceFaxHangoverTimeG711G726 based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 20000),
    )


_VRouteInterfaceFaxHangoverTimeG711G726_Type.__name__ = "Unsigned32"
_VRouteInterfaceFaxHangoverTimeG711G726_Object = MibTableColumn
vRouteInterfaceFaxHangoverTimeG711G726 = _VRouteInterfaceFaxHangoverTimeG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 8),
    _VRouteInterfaceFaxHangoverTimeG711G726_Type()
)
vRouteInterfaceFaxHangoverTimeG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceFaxHangoverTimeG711G726.setStatus("mandatory")


class _VRouteInterfaceModemFaxSpeechDiscrim_Type(Integer32):
    """Custom type vRouteInterfaceModemFaxSpeechDiscrim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VRouteInterfaceModemFaxSpeechDiscrim_Type.__name__ = "Integer32"
_VRouteInterfaceModemFaxSpeechDiscrim_Object = MibTableColumn
vRouteInterfaceModemFaxSpeechDiscrim = _VRouteInterfaceModemFaxSpeechDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 9),
    _VRouteInterfaceModemFaxSpeechDiscrim_Type()
)
vRouteInterfaceModemFaxSpeechDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceModemFaxSpeechDiscrim.setStatus("mandatory")


class _VRouteInterfaceEchoTailDelay_Type(Unsigned32):
    """Custom type vRouteInterfaceEchoTailDelay based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
    )


_VRouteInterfaceEchoTailDelay_Type.__name__ = "Unsigned32"
_VRouteInterfaceEchoTailDelay_Object = MibTableColumn
vRouteInterfaceEchoTailDelay = _VRouteInterfaceEchoTailDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 10),
    _VRouteInterfaceEchoTailDelay_Type()
)
vRouteInterfaceEchoTailDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceEchoTailDelay.setStatus("mandatory")


class _VRouteInterfaceEchoReturnLoss_Type(Unsigned32):
    """Custom type vRouteInterfaceEchoReturnLoss based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(6, 6),
    )


_VRouteInterfaceEchoReturnLoss_Type.__name__ = "Unsigned32"
_VRouteInterfaceEchoReturnLoss_Object = MibTableColumn
vRouteInterfaceEchoReturnLoss = _VRouteInterfaceEchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 11),
    _VRouteInterfaceEchoReturnLoss_Type()
)
vRouteInterfaceEchoReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceEchoReturnLoss.setStatus("mandatory")


class _VRouteInterfaceEcanBypassMode_Type(Integer32):
    """Custom type vRouteInterfaceEcanBypassMode based on Integer32"""
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
        *(("g164", 0),
          ("g165", 1),
          ("never", 2))
    )


_VRouteInterfaceEcanBypassMode_Type.__name__ = "Integer32"
_VRouteInterfaceEcanBypassMode_Object = MibTableColumn
vRouteInterfaceEcanBypassMode = _VRouteInterfaceEcanBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 10, 1, 15),
    _VRouteInterfaceEcanBypassMode_Type()
)
vRouteInterfaceEcanBypassMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceEcanBypassMode.setStatus("mandatory")
_VRouteInterfaceStructuredEchoCancellationTable_Object = MibTable
vRouteInterfaceStructuredEchoCancellationTable = _VRouteInterfaceStructuredEchoCancellationTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 472)
)
if mibBuilder.loadTexts:
    vRouteInterfaceStructuredEchoCancellationTable.setStatus("mandatory")
_VRouteInterfaceStructuredEchoCancellationEntry_Object = MibTableRow
vRouteInterfaceStructuredEchoCancellationEntry = _VRouteInterfaceStructuredEchoCancellationEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 472, 1)
)
vRouteInterfaceStructuredEchoCancellationEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteInterfaceIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteInterfaceStructuredEchoCancellationIndex"),
)
if mibBuilder.loadTexts:
    vRouteInterfaceStructuredEchoCancellationEntry.setStatus("mandatory")


class _VRouteInterfaceStructuredEchoCancellationIndex_Type(Integer32):
    """Custom type vRouteInterfaceStructuredEchoCancellationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2", 1))
    )


_VRouteInterfaceStructuredEchoCancellationIndex_Type.__name__ = "Integer32"
_VRouteInterfaceStructuredEchoCancellationIndex_Object = MibTableColumn
vRouteInterfaceStructuredEchoCancellationIndex = _VRouteInterfaceStructuredEchoCancellationIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 472, 1, 1),
    _VRouteInterfaceStructuredEchoCancellationIndex_Type()
)
vRouteInterfaceStructuredEchoCancellationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteInterfaceStructuredEchoCancellationIndex.setStatus("mandatory")


class _VRouteInterfaceStructuredEchoCancellationValue_Type(Integer32):
    """Custom type vRouteInterfaceStructuredEchoCancellationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VRouteInterfaceStructuredEchoCancellationValue_Type.__name__ = "Integer32"
_VRouteInterfaceStructuredEchoCancellationValue_Object = MibTableColumn
vRouteInterfaceStructuredEchoCancellationValue = _VRouteInterfaceStructuredEchoCancellationValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 3, 472, 1, 2),
    _VRouteInterfaceStructuredEchoCancellationValue_Type()
)
vRouteInterfaceStructuredEchoCancellationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteInterfaceStructuredEchoCancellationValue.setStatus("mandatory")
_VRouteDna_ObjectIdentity = ObjectIdentity
vRouteDna = _VRouteDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4)
)
_VRouteDnaRowStatusTable_Object = MibTable
vRouteDnaRowStatusTable = _VRouteDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 1)
)
if mibBuilder.loadTexts:
    vRouteDnaRowStatusTable.setStatus("mandatory")
_VRouteDnaRowStatusEntry_Object = MibTableRow
vRouteDnaRowStatusEntry = _VRouteDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 1, 1)
)
vRouteDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaRowStatusEntry.setStatus("mandatory")
_VRouteDnaRowStatus_Type = RowStatus
_VRouteDnaRowStatus_Object = MibTableColumn
vRouteDnaRowStatus = _VRouteDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 1, 1, 1),
    _VRouteDnaRowStatus_Type()
)
vRouteDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaRowStatus.setStatus("mandatory")
_VRouteDnaComponentName_Type = DisplayString
_VRouteDnaComponentName_Object = MibTableColumn
vRouteDnaComponentName = _VRouteDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 1, 1, 2),
    _VRouteDnaComponentName_Type()
)
vRouteDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaComponentName.setStatus("mandatory")
_VRouteDnaStorageType_Type = StorageType
_VRouteDnaStorageType_Object = MibTableColumn
vRouteDnaStorageType = _VRouteDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 1, 1, 4),
    _VRouteDnaStorageType_Type()
)
vRouteDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaStorageType.setStatus("mandatory")
_VRouteDnaIndex_Type = NonReplicated
_VRouteDnaIndex_Object = MibTableColumn
vRouteDnaIndex = _VRouteDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 1, 1, 10),
    _VRouteDnaIndex_Type()
)
vRouteDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteDnaIndex.setStatus("mandatory")
_VRouteDnaHgm_ObjectIdentity = ObjectIdentity
vRouteDnaHgm = _VRouteDnaHgm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3)
)
_VRouteDnaHgmRowStatusTable_Object = MibTable
vRouteDnaHgmRowStatusTable = _VRouteDnaHgmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 1)
)
if mibBuilder.loadTexts:
    vRouteDnaHgmRowStatusTable.setStatus("mandatory")
_VRouteDnaHgmRowStatusEntry_Object = MibTableRow
vRouteDnaHgmRowStatusEntry = _VRouteDnaHgmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 1, 1)
)
vRouteDnaHgmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaHgmRowStatusEntry.setStatus("mandatory")
_VRouteDnaHgmRowStatus_Type = RowStatus
_VRouteDnaHgmRowStatus_Object = MibTableColumn
vRouteDnaHgmRowStatus = _VRouteDnaHgmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 1, 1, 1),
    _VRouteDnaHgmRowStatus_Type()
)
vRouteDnaHgmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaHgmRowStatus.setStatus("mandatory")
_VRouteDnaHgmComponentName_Type = DisplayString
_VRouteDnaHgmComponentName_Object = MibTableColumn
vRouteDnaHgmComponentName = _VRouteDnaHgmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 1, 1, 2),
    _VRouteDnaHgmComponentName_Type()
)
vRouteDnaHgmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmComponentName.setStatus("mandatory")
_VRouteDnaHgmStorageType_Type = StorageType
_VRouteDnaHgmStorageType_Object = MibTableColumn
vRouteDnaHgmStorageType = _VRouteDnaHgmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 1, 1, 4),
    _VRouteDnaHgmStorageType_Type()
)
vRouteDnaHgmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmStorageType.setStatus("mandatory")
_VRouteDnaHgmIndex_Type = NonReplicated
_VRouteDnaHgmIndex_Object = MibTableColumn
vRouteDnaHgmIndex = _VRouteDnaHgmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 1, 1, 10),
    _VRouteDnaHgmIndex_Type()
)
vRouteDnaHgmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteDnaHgmIndex.setStatus("mandatory")
_VRouteDnaHgmHgAddr_ObjectIdentity = ObjectIdentity
vRouteDnaHgmHgAddr = _VRouteDnaHgmHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2)
)
_VRouteDnaHgmHgAddrRowStatusTable_Object = MibTable
vRouteDnaHgmHgAddrRowStatusTable = _VRouteDnaHgmHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrRowStatusTable.setStatus("mandatory")
_VRouteDnaHgmHgAddrRowStatusEntry_Object = MibTableRow
vRouteDnaHgmHgAddrRowStatusEntry = _VRouteDnaHgmHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 1, 1)
)
vRouteDnaHgmHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmHgAddrIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrRowStatusEntry.setStatus("mandatory")
_VRouteDnaHgmHgAddrRowStatus_Type = RowStatus
_VRouteDnaHgmHgAddrRowStatus_Object = MibTableColumn
vRouteDnaHgmHgAddrRowStatus = _VRouteDnaHgmHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 1, 1, 1),
    _VRouteDnaHgmHgAddrRowStatus_Type()
)
vRouteDnaHgmHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrRowStatus.setStatus("mandatory")
_VRouteDnaHgmHgAddrComponentName_Type = DisplayString
_VRouteDnaHgmHgAddrComponentName_Object = MibTableColumn
vRouteDnaHgmHgAddrComponentName = _VRouteDnaHgmHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 1, 1, 2),
    _VRouteDnaHgmHgAddrComponentName_Type()
)
vRouteDnaHgmHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrComponentName.setStatus("mandatory")
_VRouteDnaHgmHgAddrStorageType_Type = StorageType
_VRouteDnaHgmHgAddrStorageType_Object = MibTableColumn
vRouteDnaHgmHgAddrStorageType = _VRouteDnaHgmHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 1, 1, 4),
    _VRouteDnaHgmHgAddrStorageType_Type()
)
vRouteDnaHgmHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrStorageType.setStatus("mandatory")


class _VRouteDnaHgmHgAddrIndex_Type(Integer32):
    """Custom type vRouteDnaHgmHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VRouteDnaHgmHgAddrIndex_Type.__name__ = "Integer32"
_VRouteDnaHgmHgAddrIndex_Object = MibTableColumn
vRouteDnaHgmHgAddrIndex = _VRouteDnaHgmHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 1, 1, 10),
    _VRouteDnaHgmHgAddrIndex_Type()
)
vRouteDnaHgmHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrIndex.setStatus("mandatory")
_VRouteDnaHgmHgAddrAddrTable_Object = MibTable
vRouteDnaHgmHgAddrAddrTable = _VRouteDnaHgmHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrAddrTable.setStatus("mandatory")
_VRouteDnaHgmHgAddrAddrEntry_Object = MibTableRow
vRouteDnaHgmHgAddrAddrEntry = _VRouteDnaHgmHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 10, 1)
)
vRouteDnaHgmHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmHgAddrIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrAddrEntry.setStatus("mandatory")


class _VRouteDnaHgmHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type vRouteDnaHgmHgAddrNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VRouteDnaHgmHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_VRouteDnaHgmHgAddrNumberingPlanIndicator_Object = MibTableColumn
vRouteDnaHgmHgAddrNumberingPlanIndicator = _VRouteDnaHgmHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 10, 1, 1),
    _VRouteDnaHgmHgAddrNumberingPlanIndicator_Type()
)
vRouteDnaHgmHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _VRouteDnaHgmHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type vRouteDnaHgmHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VRouteDnaHgmHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_VRouteDnaHgmHgAddrDataNetworkAddress_Object = MibTableColumn
vRouteDnaHgmHgAddrDataNetworkAddress = _VRouteDnaHgmHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 2, 10, 1, 2),
    _VRouteDnaHgmHgAddrDataNetworkAddress_Type()
)
vRouteDnaHgmHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaHgmHgAddrDataNetworkAddress.setStatus("mandatory")
_VRouteDnaHgmIfTable_Object = MibTable
vRouteDnaHgmIfTable = _VRouteDnaHgmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 10)
)
if mibBuilder.loadTexts:
    vRouteDnaHgmIfTable.setStatus("mandatory")
_VRouteDnaHgmIfEntry_Object = MibTableRow
vRouteDnaHgmIfEntry = _VRouteDnaHgmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 10, 1)
)
vRouteDnaHgmIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaHgmIfEntry.setStatus("mandatory")


class _VRouteDnaHgmUsageDeltaUpdateThreshold_Type(Unsigned32):
    """Custom type vRouteDnaHgmUsageDeltaUpdateThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VRouteDnaHgmUsageDeltaUpdateThreshold_Type.__name__ = "Unsigned32"
_VRouteDnaHgmUsageDeltaUpdateThreshold_Object = MibTableColumn
vRouteDnaHgmUsageDeltaUpdateThreshold = _VRouteDnaHgmUsageDeltaUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 10, 1, 1),
    _VRouteDnaHgmUsageDeltaUpdateThreshold_Type()
)
vRouteDnaHgmUsageDeltaUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaHgmUsageDeltaUpdateThreshold.setStatus("mandatory")
_VRouteDnaHgmOpTable_Object = MibTable
vRouteDnaHgmOpTable = _VRouteDnaHgmOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 11)
)
if mibBuilder.loadTexts:
    vRouteDnaHgmOpTable.setStatus("mandatory")
_VRouteDnaHgmOpEntry_Object = MibTableRow
vRouteDnaHgmOpEntry = _VRouteDnaHgmOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 11, 1)
)
vRouteDnaHgmOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaHgmIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaHgmOpEntry.setStatus("mandatory")


class _VRouteDnaHgmMaxAvailableChannels_Type(Unsigned32):
    """Custom type vRouteDnaHgmMaxAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VRouteDnaHgmMaxAvailableChannels_Type.__name__ = "Unsigned32"
_VRouteDnaHgmMaxAvailableChannels_Object = MibTableColumn
vRouteDnaHgmMaxAvailableChannels = _VRouteDnaHgmMaxAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 11, 1, 1),
    _VRouteDnaHgmMaxAvailableChannels_Type()
)
vRouteDnaHgmMaxAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmMaxAvailableChannels.setStatus("mandatory")


class _VRouteDnaHgmAvailableChannels_Type(Unsigned32):
    """Custom type vRouteDnaHgmAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VRouteDnaHgmAvailableChannels_Type.__name__ = "Unsigned32"
_VRouteDnaHgmAvailableChannels_Object = MibTableColumn
vRouteDnaHgmAvailableChannels = _VRouteDnaHgmAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 11, 1, 2),
    _VRouteDnaHgmAvailableChannels_Type()
)
vRouteDnaHgmAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmAvailableChannels.setStatus("mandatory")


class _VRouteDnaHgmAvailabilityDelta_Type(Integer32):
    """Custom type vRouteDnaHgmAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4096, 4096),
    )


_VRouteDnaHgmAvailabilityDelta_Type.__name__ = "Integer32"
_VRouteDnaHgmAvailabilityDelta_Object = MibTableColumn
vRouteDnaHgmAvailabilityDelta = _VRouteDnaHgmAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 3, 11, 1, 3),
    _VRouteDnaHgmAvailabilityDelta_Type()
)
vRouteDnaHgmAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDnaHgmAvailabilityDelta.setStatus("mandatory")
_VRouteDnaAddressTable_Object = MibTable
vRouteDnaAddressTable = _VRouteDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 10)
)
if mibBuilder.loadTexts:
    vRouteDnaAddressTable.setStatus("mandatory")
_VRouteDnaAddressEntry_Object = MibTableRow
vRouteDnaAddressEntry = _VRouteDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 10, 1)
)
vRouteDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDnaIndex"),
)
if mibBuilder.loadTexts:
    vRouteDnaAddressEntry.setStatus("mandatory")


class _VRouteDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type vRouteDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VRouteDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_VRouteDnaNumberingPlanIndicator_Object = MibTableColumn
vRouteDnaNumberingPlanIndicator = _VRouteDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 10, 1, 1),
    _VRouteDnaNumberingPlanIndicator_Type()
)
vRouteDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaNumberingPlanIndicator.setStatus("mandatory")


class _VRouteDnaDataNetworkAddress_Type(DigitString):
    """Custom type vRouteDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VRouteDnaDataNetworkAddress_Type.__name__ = "DigitString"
_VRouteDnaDataNetworkAddress_Object = MibTableColumn
vRouteDnaDataNetworkAddress = _VRouteDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 4, 10, 1, 2),
    _VRouteDnaDataNetworkAddress_Type()
)
vRouteDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDnaDataNetworkAddress.setStatus("mandatory")
_VRouteAcct_ObjectIdentity = ObjectIdentity
vRouteAcct = _VRouteAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5)
)
_VRouteAcctRowStatusTable_Object = MibTable
vRouteAcctRowStatusTable = _VRouteAcctRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 1)
)
if mibBuilder.loadTexts:
    vRouteAcctRowStatusTable.setStatus("mandatory")
_VRouteAcctRowStatusEntry_Object = MibTableRow
vRouteAcctRowStatusEntry = _VRouteAcctRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 1, 1)
)
vRouteAcctRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteAcctIndex"),
)
if mibBuilder.loadTexts:
    vRouteAcctRowStatusEntry.setStatus("mandatory")
_VRouteAcctRowStatus_Type = RowStatus
_VRouteAcctRowStatus_Object = MibTableColumn
vRouteAcctRowStatus = _VRouteAcctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 1, 1, 1),
    _VRouteAcctRowStatus_Type()
)
vRouteAcctRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteAcctRowStatus.setStatus("mandatory")
_VRouteAcctComponentName_Type = DisplayString
_VRouteAcctComponentName_Object = MibTableColumn
vRouteAcctComponentName = _VRouteAcctComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 1, 1, 2),
    _VRouteAcctComponentName_Type()
)
vRouteAcctComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteAcctComponentName.setStatus("mandatory")
_VRouteAcctStorageType_Type = StorageType
_VRouteAcctStorageType_Object = MibTableColumn
vRouteAcctStorageType = _VRouteAcctStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 1, 1, 4),
    _VRouteAcctStorageType_Type()
)
vRouteAcctStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteAcctStorageType.setStatus("mandatory")
_VRouteAcctIndex_Type = NonReplicated
_VRouteAcctIndex_Object = MibTableColumn
vRouteAcctIndex = _VRouteAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 1, 1, 10),
    _VRouteAcctIndex_Type()
)
vRouteAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRouteAcctIndex.setStatus("mandatory")
_VRouteAcctProvTable_Object = MibTable
vRouteAcctProvTable = _VRouteAcctProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2)
)
if mibBuilder.loadTexts:
    vRouteAcctProvTable.setStatus("mandatory")
_VRouteAcctProvEntry_Object = MibTableRow
vRouteAcctProvEntry = _VRouteAcctProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2, 1)
)
vRouteAcctProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteAcctIndex"),
)
if mibBuilder.loadTexts:
    vRouteAcctProvEntry.setStatus("mandatory")


class _VRouteAcctAccountCollection_Type(OctetString):
    """Custom type vRouteAcctAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VRouteAcctAccountCollection_Type.__name__ = "OctetString"
_VRouteAcctAccountCollection_Object = MibTableColumn
vRouteAcctAccountCollection = _VRouteAcctAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2, 1, 2),
    _VRouteAcctAccountCollection_Type()
)
vRouteAcctAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteAcctAccountCollection.setStatus("mandatory")


class _VRouteAcctAccountClass_Type(Unsigned32):
    """Custom type vRouteAcctAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRouteAcctAccountClass_Type.__name__ = "Unsigned32"
_VRouteAcctAccountClass_Object = MibTableColumn
vRouteAcctAccountClass = _VRouteAcctAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2, 1, 3),
    _VRouteAcctAccountClass_Type()
)
vRouteAcctAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteAcctAccountClass.setStatus("mandatory")


class _VRouteAcctServiceExchange_Type(Unsigned32):
    """Custom type vRouteAcctServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRouteAcctServiceExchange_Type.__name__ = "Unsigned32"
_VRouteAcctServiceExchange_Object = MibTableColumn
vRouteAcctServiceExchange = _VRouteAcctServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2, 1, 4),
    _VRouteAcctServiceExchange_Type()
)
vRouteAcctServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteAcctServiceExchange.setStatus("mandatory")


class _VRouteAcctDigitsSuppressed_Type(Unsigned32):
    """Custom type vRouteAcctDigitsSuppressed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VRouteAcctDigitsSuppressed_Type.__name__ = "Unsigned32"
_VRouteAcctDigitsSuppressed_Object = MibTableColumn
vRouteAcctDigitsSuppressed = _VRouteAcctDigitsSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2, 1, 5),
    _VRouteAcctDigitsSuppressed_Type()
)
vRouteAcctDigitsSuppressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteAcctDigitsSuppressed.setStatus("mandatory")


class _VRouteAcctAccountingOptions_Type(OctetString):
    """Custom type vRouteAcctAccountingOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VRouteAcctAccountingOptions_Type.__name__ = "OctetString"
_VRouteAcctAccountingOptions_Object = MibTableColumn
vRouteAcctAccountingOptions = _VRouteAcctAccountingOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 5, 2, 1, 6),
    _VRouteAcctAccountingOptions_Type()
)
vRouteAcctAccountingOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteAcctAccountingOptions.setStatus("mandatory")
_VRouteProvTable_Object = MibTable
vRouteProvTable = _VRouteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10)
)
if mibBuilder.loadTexts:
    vRouteProvTable.setStatus("mandatory")
_VRouteProvEntry_Object = MibTableRow
vRouteProvEntry = _VRouteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1)
)
vRouteProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteProvEntry.setStatus("mandatory")


class _VRouteCommentText_Type(AsciiString):
    """Custom type vRouteCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VRouteCommentText_Type.__name__ = "AsciiString"
_VRouteCommentText_Object = MibTableColumn
vRouteCommentText = _VRouteCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 1),
    _VRouteCommentText_Type()
)
vRouteCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteCommentText.setStatus("mandatory")


class _VRouteTypeOfRoute_Type(Integer32):
    """Custom type vRouteTypeOfRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 0),
          ("voiceData", 2))
    )


_VRouteTypeOfRoute_Type.__name__ = "Integer32"
_VRouteTypeOfRoute_Object = MibTableColumn
vRouteTypeOfRoute = _VRouteTypeOfRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 2),
    _VRouteTypeOfRoute_Type()
)
vRouteTypeOfRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteTypeOfRoute.setStatus("mandatory")


class _VRouteDiallingPlan0_Type(OctetString):
    """Custom type vRouteDiallingPlan0 based on OctetString"""
    defaultHexValue = "fff8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VRouteDiallingPlan0_Type.__name__ = "OctetString"
_VRouteDiallingPlan0_Object = MibTableColumn
vRouteDiallingPlan0 = _VRouteDiallingPlan0_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 6),
    _VRouteDiallingPlan0_Type()
)
vRouteDiallingPlan0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDiallingPlan0.setStatus("mandatory")


class _VRouteDiallingPlan1_Type(OctetString):
    """Custom type vRouteDiallingPlan1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VRouteDiallingPlan1_Type.__name__ = "OctetString"
_VRouteDiallingPlan1_Object = MibTableColumn
vRouteDiallingPlan1 = _VRouteDiallingPlan1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 7),
    _VRouteDiallingPlan1_Type()
)
vRouteDiallingPlan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDiallingPlan1.setStatus("mandatory")


class _VRouteDiallingPlan2_Type(OctetString):
    """Custom type vRouteDiallingPlan2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VRouteDiallingPlan2_Type.__name__ = "OctetString"
_VRouteDiallingPlan2_Object = MibTableColumn
vRouteDiallingPlan2 = _VRouteDiallingPlan2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 8),
    _VRouteDiallingPlan2_Type()
)
vRouteDiallingPlan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteDiallingPlan2.setStatus("mandatory")


class _VRouteHuntingAlgorithm_Type(Integer32):
    """Custom type vRouteHuntingAlgorithm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bottomUpLinear", 0),
          ("topDownLinear", 1))
    )


_VRouteHuntingAlgorithm_Type.__name__ = "Integer32"
_VRouteHuntingAlgorithm_Object = MibTableColumn
vRouteHuntingAlgorithm = _VRouteHuntingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 9),
    _VRouteHuntingAlgorithm_Type()
)
vRouteHuntingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteHuntingAlgorithm.setStatus("mandatory")


class _VRouteMinimumDigitsToRoute_Type(Unsigned32):
    """Custom type vRouteMinimumDigitsToRoute based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VRouteMinimumDigitsToRoute_Type.__name__ = "Unsigned32"
_VRouteMinimumDigitsToRoute_Object = MibTableColumn
vRouteMinimumDigitsToRoute = _VRouteMinimumDigitsToRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 10),
    _VRouteMinimumDigitsToRoute_Type()
)
vRouteMinimumDigitsToRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteMinimumDigitsToRoute.setStatus("mandatory")
_VRouteVoiceNetworkingCallServer_Type = Link
_VRouteVoiceNetworkingCallServer_Object = MibTableColumn
vRouteVoiceNetworkingCallServer = _VRouteVoiceNetworkingCallServer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 11),
    _VRouteVoiceNetworkingCallServer_Type()
)
vRouteVoiceNetworkingCallServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteVoiceNetworkingCallServer.setStatus("mandatory")


class _VRouteOverrideDirectoryNumber_Type(DigitString):
    """Custom type vRouteOverrideDirectoryNumber based on DigitString"""
    defaultHexValue = ""

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_VRouteOverrideDirectoryNumber_Type.__name__ = "DigitString"
_VRouteOverrideDirectoryNumber_Object = MibTableColumn
vRouteOverrideDirectoryNumber = _VRouteOverrideDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 12),
    _VRouteOverrideDirectoryNumber_Type()
)
vRouteOverrideDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteOverrideDirectoryNumber.setStatus("mandatory")


class _VRoutePrivateNetworkIdentifer_Type(Unsigned32):
    """Custom type vRoutePrivateNetworkIdentifer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32700),
    )


_VRoutePrivateNetworkIdentifer_Type.__name__ = "Unsigned32"
_VRoutePrivateNetworkIdentifer_Object = MibTableColumn
vRoutePrivateNetworkIdentifer = _VRoutePrivateNetworkIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 10, 1, 13),
    _VRoutePrivateNetworkIdentifer_Type()
)
vRoutePrivateNetworkIdentifer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRoutePrivateNetworkIdentifer.setStatus("mandatory")
_VRouteCidDataTable_Object = MibTable
vRouteCidDataTable = _VRouteCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 11)
)
if mibBuilder.loadTexts:
    vRouteCidDataTable.setStatus("mandatory")
_VRouteCidDataEntry_Object = MibTableRow
vRouteCidDataEntry = _VRouteCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 11, 1)
)
vRouteCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteCidDataEntry.setStatus("mandatory")


class _VRouteCustomerIdentifier_Type(Unsigned32):
    """Custom type vRouteCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_VRouteCustomerIdentifier_Type.__name__ = "Unsigned32"
_VRouteCustomerIdentifier_Object = MibTableColumn
vRouteCustomerIdentifier = _VRouteCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 11, 1, 1),
    _VRouteCustomerIdentifier_Type()
)
vRouteCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteCustomerIdentifier.setStatus("mandatory")
_VRouteIfEntryTable_Object = MibTable
vRouteIfEntryTable = _VRouteIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 12)
)
if mibBuilder.loadTexts:
    vRouteIfEntryTable.setStatus("mandatory")
_VRouteIfEntryEntry_Object = MibTableRow
vRouteIfEntryEntry = _VRouteIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 12, 1)
)
vRouteIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteIfEntryEntry.setStatus("mandatory")


class _VRouteIfAdminStatus_Type(Integer32):
    """Custom type vRouteIfAdminStatus based on Integer32"""
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


_VRouteIfAdminStatus_Type.__name__ = "Integer32"
_VRouteIfAdminStatus_Object = MibTableColumn
vRouteIfAdminStatus = _VRouteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 12, 1, 1),
    _VRouteIfAdminStatus_Type()
)
vRouteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteIfAdminStatus.setStatus("mandatory")


class _VRouteIfIndex_Type(InterfaceIndex):
    """Custom type vRouteIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRouteIfIndex_Type.__name__ = "InterfaceIndex"
_VRouteIfIndex_Object = MibTableColumn
vRouteIfIndex = _VRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 12, 1, 2),
    _VRouteIfIndex_Type()
)
vRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteIfIndex.setStatus("mandatory")
_VRouteStateTable_Object = MibTable
vRouteStateTable = _VRouteStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 13)
)
if mibBuilder.loadTexts:
    vRouteStateTable.setStatus("mandatory")
_VRouteStateEntry_Object = MibTableRow
vRouteStateEntry = _VRouteStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 13, 1)
)
vRouteStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteStateEntry.setStatus("mandatory")


class _VRouteAdminState_Type(Integer32):
    """Custom type vRouteAdminState based on Integer32"""
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


_VRouteAdminState_Type.__name__ = "Integer32"
_VRouteAdminState_Object = MibTableColumn
vRouteAdminState = _VRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 13, 1, 1),
    _VRouteAdminState_Type()
)
vRouteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteAdminState.setStatus("mandatory")


class _VRouteOperationalState_Type(Integer32):
    """Custom type vRouteOperationalState based on Integer32"""
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


_VRouteOperationalState_Type.__name__ = "Integer32"
_VRouteOperationalState_Object = MibTableColumn
vRouteOperationalState = _VRouteOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 13, 1, 2),
    _VRouteOperationalState_Type()
)
vRouteOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteOperationalState.setStatus("mandatory")


class _VRouteUsageState_Type(Integer32):
    """Custom type vRouteUsageState based on Integer32"""
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


_VRouteUsageState_Type.__name__ = "Integer32"
_VRouteUsageState_Object = MibTableColumn
vRouteUsageState = _VRouteUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 13, 1, 3),
    _VRouteUsageState_Type()
)
vRouteUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteUsageState.setStatus("mandatory")
_VRouteOperStatusTable_Object = MibTable
vRouteOperStatusTable = _VRouteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 14)
)
if mibBuilder.loadTexts:
    vRouteOperStatusTable.setStatus("mandatory")
_VRouteOperStatusEntry_Object = MibTableRow
vRouteOperStatusEntry = _VRouteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 14, 1)
)
vRouteOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteOperStatusEntry.setStatus("mandatory")


class _VRouteSnmpOperStatus_Type(Integer32):
    """Custom type vRouteSnmpOperStatus based on Integer32"""
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


_VRouteSnmpOperStatus_Type.__name__ = "Integer32"
_VRouteSnmpOperStatus_Object = MibTableColumn
vRouteSnmpOperStatus = _VRouteSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 14, 1, 1),
    _VRouteSnmpOperStatus_Type()
)
vRouteSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteSnmpOperStatus.setStatus("mandatory")
_VRouteStatsTable_Object = MibTable
vRouteStatsTable = _VRouteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 15)
)
if mibBuilder.loadTexts:
    vRouteStatsTable.setStatus("mandatory")
_VRouteStatsEntry_Object = MibTableRow
vRouteStatsEntry = _VRouteStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 15, 1)
)
vRouteStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
)
if mibBuilder.loadTexts:
    vRouteStatsEntry.setStatus("mandatory")
_VRouteTotalCallsFromSubnet_Type = Counter32
_VRouteTotalCallsFromSubnet_Object = MibTableColumn
vRouteTotalCallsFromSubnet = _VRouteTotalCallsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 15, 1, 1),
    _VRouteTotalCallsFromSubnet_Type()
)
vRouteTotalCallsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteTotalCallsFromSubnet.setStatus("mandatory")
_VRouteCallsClearedNoChannel_Type = Counter32
_VRouteCallsClearedNoChannel_Object = MibTableColumn
vRouteCallsClearedNoChannel = _VRouteCallsClearedNoChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 15, 1, 2),
    _VRouteCallsClearedNoChannel_Type()
)
vRouteCallsClearedNoChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteCallsClearedNoChannel.setStatus("mandatory")
_VRouteCallsClearedOutOfService_Type = Counter32
_VRouteCallsClearedOutOfService_Object = MibTableColumn
vRouteCallsClearedOutOfService = _VRouteCallsClearedOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 15, 1, 3),
    _VRouteCallsClearedOutOfService_Type()
)
vRouteCallsClearedOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteCallsClearedOutOfService.setStatus("mandatory")
_VRouteCallsRejected_Type = Counter32
_VRouteCallsRejected_Object = MibTableColumn
vRouteCallsRejected = _VRouteCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 15, 1, 4),
    _VRouteCallsRejected_Type()
)
vRouteCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteCallsRejected.setStatus("mandatory")
_VRouteSubroutesTable_Object = MibTable
vRouteSubroutesTable = _VRouteSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 309)
)
if mibBuilder.loadTexts:
    vRouteSubroutesTable.setStatus("mandatory")
_VRouteSubroutesEntry_Object = MibTableRow
vRouteSubroutesEntry = _VRouteSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 309, 1)
)
vRouteSubroutesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteSubroutesValue"),
)
if mibBuilder.loadTexts:
    vRouteSubroutesEntry.setStatus("mandatory")
_VRouteSubroutesValue_Type = Link
_VRouteSubroutesValue_Object = MibTableColumn
vRouteSubroutesValue = _VRouteSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 309, 1, 1),
    _VRouteSubroutesValue_Type()
)
vRouteSubroutesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouteSubroutesValue.setStatus("mandatory")
_VRouteSubroutesRowStatus_Type = RowStatus
_VRouteSubroutesRowStatus_Object = MibTableColumn
vRouteSubroutesRowStatus = _VRouteSubroutesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 309, 1, 2),
    _VRouteSubroutesRowStatus_Type()
)
vRouteSubroutesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vRouteSubroutesRowStatus.setStatus("mandatory")
_VRouteDegradedSubroutesTable_Object = MibTable
vRouteDegradedSubroutesTable = _VRouteDegradedSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 310)
)
if mibBuilder.loadTexts:
    vRouteDegradedSubroutesTable.setStatus("mandatory")
_VRouteDegradedSubroutesEntry_Object = MibTableRow
vRouteDegradedSubroutesEntry = _VRouteDegradedSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 310, 1)
)
vRouteDegradedSubroutesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vRouteDegradedSubroutesValue"),
)
if mibBuilder.loadTexts:
    vRouteDegradedSubroutesEntry.setStatus("mandatory")
_VRouteDegradedSubroutesValue_Type = RowPointer
_VRouteDegradedSubroutesValue_Object = MibTableColumn
vRouteDegradedSubroutesValue = _VRouteDegradedSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 116, 310, 1, 1),
    _VRouteDegradedSubroutesValue_Type()
)
vRouteDegradedSubroutesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouteDegradedSubroutesValue.setStatus("mandatory")
_Vsr_ObjectIdentity = ObjectIdentity
vsr = _Vsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117)
)
_VsrRowStatusTable_Object = MibTable
vsrRowStatusTable = _VsrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 1)
)
if mibBuilder.loadTexts:
    vsrRowStatusTable.setStatus("mandatory")
_VsrRowStatusEntry_Object = MibTableRow
vsrRowStatusEntry = _VsrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 1, 1)
)
vsrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrRowStatusEntry.setStatus("mandatory")
_VsrRowStatus_Type = RowStatus
_VsrRowStatus_Object = MibTableColumn
vsrRowStatus = _VsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 1, 1, 1),
    _VsrRowStatus_Type()
)
vsrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrRowStatus.setStatus("mandatory")
_VsrComponentName_Type = DisplayString
_VsrComponentName_Object = MibTableColumn
vsrComponentName = _VsrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 1, 1, 2),
    _VsrComponentName_Type()
)
vsrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrComponentName.setStatus("mandatory")
_VsrStorageType_Type = StorageType
_VsrStorageType_Object = MibTableColumn
vsrStorageType = _VsrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 1, 1, 4),
    _VsrStorageType_Type()
)
vsrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrStorageType.setStatus("mandatory")


class _VsrIndex_Type(Integer32):
    """Custom type vsrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VsrIndex_Type.__name__ = "Integer32"
_VsrIndex_Object = MibTableColumn
vsrIndex = _VsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 1, 1, 10),
    _VsrIndex_Type()
)
vsrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrIndex.setStatus("mandatory")
_VsrSvs_ObjectIdentity = ObjectIdentity
vsrSvs = _VsrSvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2)
)
_VsrSvsRowStatusTable_Object = MibTable
vsrSvsRowStatusTable = _VsrSvsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 1)
)
if mibBuilder.loadTexts:
    vsrSvsRowStatusTable.setStatus("mandatory")
_VsrSvsRowStatusEntry_Object = MibTableRow
vsrSvsRowStatusEntry = _VsrSvsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 1, 1)
)
vsrSvsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsRowStatusEntry.setStatus("mandatory")
_VsrSvsRowStatus_Type = RowStatus
_VsrSvsRowStatus_Object = MibTableColumn
vsrSvsRowStatus = _VsrSvsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 1, 1, 1),
    _VsrSvsRowStatus_Type()
)
vsrSvsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsRowStatus.setStatus("mandatory")
_VsrSvsComponentName_Type = DisplayString
_VsrSvsComponentName_Object = MibTableColumn
vsrSvsComponentName = _VsrSvsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 1, 1, 2),
    _VsrSvsComponentName_Type()
)
vsrSvsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsComponentName.setStatus("mandatory")
_VsrSvsStorageType_Type = StorageType
_VsrSvsStorageType_Object = MibTableColumn
vsrSvsStorageType = _VsrSvsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 1, 1, 4),
    _VsrSvsStorageType_Type()
)
vsrSvsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsStorageType.setStatus("mandatory")


class _VsrSvsIndex_Type(Integer32):
    """Custom type vsrSvsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VsrSvsIndex_Type.__name__ = "Integer32"
_VsrSvsIndex_Object = MibTableColumn
vsrSvsIndex = _VsrSvsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 1, 1, 10),
    _VsrSvsIndex_Type()
)
vsrSvsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsIndex.setStatus("mandatory")
_VsrSvsFramer_ObjectIdentity = ObjectIdentity
vsrSvsFramer = _VsrSvsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2)
)
_VsrSvsFramerRowStatusTable_Object = MibTable
vsrSvsFramerRowStatusTable = _VsrSvsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vsrSvsFramerRowStatusTable.setStatus("mandatory")
_VsrSvsFramerRowStatusEntry_Object = MibTableRow
vsrSvsFramerRowStatusEntry = _VsrSvsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 1, 1)
)
vsrSvsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerRowStatusEntry.setStatus("mandatory")
_VsrSvsFramerRowStatus_Type = RowStatus
_VsrSvsFramerRowStatus_Object = MibTableColumn
vsrSvsFramerRowStatus = _VsrSvsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 1, 1, 1),
    _VsrSvsFramerRowStatus_Type()
)
vsrSvsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerRowStatus.setStatus("mandatory")
_VsrSvsFramerComponentName_Type = DisplayString
_VsrSvsFramerComponentName_Object = MibTableColumn
vsrSvsFramerComponentName = _VsrSvsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 1, 1, 2),
    _VsrSvsFramerComponentName_Type()
)
vsrSvsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerComponentName.setStatus("mandatory")
_VsrSvsFramerStorageType_Type = StorageType
_VsrSvsFramerStorageType_Object = MibTableColumn
vsrSvsFramerStorageType = _VsrSvsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 1, 1, 4),
    _VsrSvsFramerStorageType_Type()
)
vsrSvsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerStorageType.setStatus("mandatory")
_VsrSvsFramerIndex_Type = NonReplicated
_VsrSvsFramerIndex_Object = MibTableColumn
vsrSvsFramerIndex = _VsrSvsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 1, 1, 10),
    _VsrSvsFramerIndex_Type()
)
vsrSvsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerIndex.setStatus("mandatory")
_VsrSvsFramerVfpDebug_ObjectIdentity = ObjectIdentity
vsrSvsFramerVfpDebug = _VsrSvsFramerVfpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5)
)
_VsrSvsFramerVfpDebugRowStatusTable_Object = MibTable
vsrSvsFramerVfpDebugRowStatusTable = _VsrSvsFramerVfpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vsrSvsFramerVfpDebugRowStatusTable.setStatus("mandatory")
_VsrSvsFramerVfpDebugRowStatusEntry_Object = MibTableRow
vsrSvsFramerVfpDebugRowStatusEntry = _VsrSvsFramerVfpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5, 1, 1)
)
vsrSvsFramerVfpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerVfpDebugIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerVfpDebugRowStatusEntry.setStatus("mandatory")
_VsrSvsFramerVfpDebugRowStatus_Type = RowStatus
_VsrSvsFramerVfpDebugRowStatus_Object = MibTableColumn
vsrSvsFramerVfpDebugRowStatus = _VsrSvsFramerVfpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5, 1, 1, 1),
    _VsrSvsFramerVfpDebugRowStatus_Type()
)
vsrSvsFramerVfpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerVfpDebugRowStatus.setStatus("mandatory")
_VsrSvsFramerVfpDebugComponentName_Type = DisplayString
_VsrSvsFramerVfpDebugComponentName_Object = MibTableColumn
vsrSvsFramerVfpDebugComponentName = _VsrSvsFramerVfpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5, 1, 1, 2),
    _VsrSvsFramerVfpDebugComponentName_Type()
)
vsrSvsFramerVfpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerVfpDebugComponentName.setStatus("mandatory")
_VsrSvsFramerVfpDebugStorageType_Type = StorageType
_VsrSvsFramerVfpDebugStorageType_Object = MibTableColumn
vsrSvsFramerVfpDebugStorageType = _VsrSvsFramerVfpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5, 1, 1, 4),
    _VsrSvsFramerVfpDebugStorageType_Type()
)
vsrSvsFramerVfpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerVfpDebugStorageType.setStatus("mandatory")
_VsrSvsFramerVfpDebugIndex_Type = NonReplicated
_VsrSvsFramerVfpDebugIndex_Object = MibTableColumn
vsrSvsFramerVfpDebugIndex = _VsrSvsFramerVfpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 5, 1, 1, 10),
    _VsrSvsFramerVfpDebugIndex_Type()
)
vsrSvsFramerVfpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerVfpDebugIndex.setStatus("mandatory")
_VsrSvsFramerMvpDebug_ObjectIdentity = ObjectIdentity
vsrSvsFramerMvpDebug = _VsrSvsFramerMvpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6)
)
_VsrSvsFramerMvpDebugRowStatusTable_Object = MibTable
vsrSvsFramerMvpDebugRowStatusTable = _VsrSvsFramerMvpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vsrSvsFramerMvpDebugRowStatusTable.setStatus("mandatory")
_VsrSvsFramerMvpDebugRowStatusEntry_Object = MibTableRow
vsrSvsFramerMvpDebugRowStatusEntry = _VsrSvsFramerMvpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6, 1, 1)
)
vsrSvsFramerMvpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerMvpDebugIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerMvpDebugRowStatusEntry.setStatus("mandatory")
_VsrSvsFramerMvpDebugRowStatus_Type = RowStatus
_VsrSvsFramerMvpDebugRowStatus_Object = MibTableColumn
vsrSvsFramerMvpDebugRowStatus = _VsrSvsFramerMvpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6, 1, 1, 1),
    _VsrSvsFramerMvpDebugRowStatus_Type()
)
vsrSvsFramerMvpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerMvpDebugRowStatus.setStatus("mandatory")
_VsrSvsFramerMvpDebugComponentName_Type = DisplayString
_VsrSvsFramerMvpDebugComponentName_Object = MibTableColumn
vsrSvsFramerMvpDebugComponentName = _VsrSvsFramerMvpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6, 1, 1, 2),
    _VsrSvsFramerMvpDebugComponentName_Type()
)
vsrSvsFramerMvpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerMvpDebugComponentName.setStatus("mandatory")
_VsrSvsFramerMvpDebugStorageType_Type = StorageType
_VsrSvsFramerMvpDebugStorageType_Object = MibTableColumn
vsrSvsFramerMvpDebugStorageType = _VsrSvsFramerMvpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6, 1, 1, 4),
    _VsrSvsFramerMvpDebugStorageType_Type()
)
vsrSvsFramerMvpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerMvpDebugStorageType.setStatus("mandatory")
_VsrSvsFramerMvpDebugIndex_Type = NonReplicated
_VsrSvsFramerMvpDebugIndex_Object = MibTableColumn
vsrSvsFramerMvpDebugIndex = _VsrSvsFramerMvpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 6, 1, 1, 10),
    _VsrSvsFramerMvpDebugIndex_Type()
)
vsrSvsFramerMvpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerMvpDebugIndex.setStatus("mandatory")
_VsrSvsFramerPcmCapture_ObjectIdentity = ObjectIdentity
vsrSvsFramerPcmCapture = _VsrSvsFramerPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7)
)
_VsrSvsFramerPcmCaptureRowStatusTable_Object = MibTable
vsrSvsFramerPcmCaptureRowStatusTable = _VsrSvsFramerPcmCaptureRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vsrSvsFramerPcmCaptureRowStatusTable.setStatus("mandatory")
_VsrSvsFramerPcmCaptureRowStatusEntry_Object = MibTableRow
vsrSvsFramerPcmCaptureRowStatusEntry = _VsrSvsFramerPcmCaptureRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7, 1, 1)
)
vsrSvsFramerPcmCaptureRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerPcmCaptureIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerPcmCaptureRowStatusEntry.setStatus("mandatory")
_VsrSvsFramerPcmCaptureRowStatus_Type = RowStatus
_VsrSvsFramerPcmCaptureRowStatus_Object = MibTableColumn
vsrSvsFramerPcmCaptureRowStatus = _VsrSvsFramerPcmCaptureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7, 1, 1, 1),
    _VsrSvsFramerPcmCaptureRowStatus_Type()
)
vsrSvsFramerPcmCaptureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerPcmCaptureRowStatus.setStatus("mandatory")
_VsrSvsFramerPcmCaptureComponentName_Type = DisplayString
_VsrSvsFramerPcmCaptureComponentName_Object = MibTableColumn
vsrSvsFramerPcmCaptureComponentName = _VsrSvsFramerPcmCaptureComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7, 1, 1, 2),
    _VsrSvsFramerPcmCaptureComponentName_Type()
)
vsrSvsFramerPcmCaptureComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerPcmCaptureComponentName.setStatus("mandatory")
_VsrSvsFramerPcmCaptureStorageType_Type = StorageType
_VsrSvsFramerPcmCaptureStorageType_Object = MibTableColumn
vsrSvsFramerPcmCaptureStorageType = _VsrSvsFramerPcmCaptureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7, 1, 1, 4),
    _VsrSvsFramerPcmCaptureStorageType_Type()
)
vsrSvsFramerPcmCaptureStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerPcmCaptureStorageType.setStatus("mandatory")
_VsrSvsFramerPcmCaptureIndex_Type = NonReplicated
_VsrSvsFramerPcmCaptureIndex_Object = MibTableColumn
vsrSvsFramerPcmCaptureIndex = _VsrSvsFramerPcmCaptureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 7, 1, 1, 10),
    _VsrSvsFramerPcmCaptureIndex_Type()
)
vsrSvsFramerPcmCaptureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerPcmCaptureIndex.setStatus("mandatory")
_VsrSvsFramerProvTable_Object = MibTable
vsrSvsFramerProvTable = _VsrSvsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vsrSvsFramerProvTable.setStatus("mandatory")
_VsrSvsFramerProvEntry_Object = MibTableRow
vsrSvsFramerProvEntry = _VsrSvsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 10, 1)
)
vsrSvsFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerProvEntry.setStatus("mandatory")
_VsrSvsFramerInterfaceName_Type = Link
_VsrSvsFramerInterfaceName_Object = MibTableColumn
vsrSvsFramerInterfaceName = _VsrSvsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 10, 1, 1),
    _VsrSvsFramerInterfaceName_Type()
)
vsrSvsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsFramerInterfaceName.setStatus("mandatory")
_VsrSvsFramerStateTable_Object = MibTable
vsrSvsFramerStateTable = _VsrSvsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 14)
)
if mibBuilder.loadTexts:
    vsrSvsFramerStateTable.setStatus("mandatory")
_VsrSvsFramerStateEntry_Object = MibTableRow
vsrSvsFramerStateEntry = _VsrSvsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 14, 1)
)
vsrSvsFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerStateEntry.setStatus("mandatory")


class _VsrSvsFramerAdminState_Type(Integer32):
    """Custom type vsrSvsFramerAdminState based on Integer32"""
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


_VsrSvsFramerAdminState_Type.__name__ = "Integer32"
_VsrSvsFramerAdminState_Object = MibTableColumn
vsrSvsFramerAdminState = _VsrSvsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 14, 1, 1),
    _VsrSvsFramerAdminState_Type()
)
vsrSvsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerAdminState.setStatus("mandatory")


class _VsrSvsFramerOperationalState_Type(Integer32):
    """Custom type vsrSvsFramerOperationalState based on Integer32"""
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


_VsrSvsFramerOperationalState_Type.__name__ = "Integer32"
_VsrSvsFramerOperationalState_Object = MibTableColumn
vsrSvsFramerOperationalState = _VsrSvsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 14, 1, 2),
    _VsrSvsFramerOperationalState_Type()
)
vsrSvsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerOperationalState.setStatus("mandatory")


class _VsrSvsFramerUsageState_Type(Integer32):
    """Custom type vsrSvsFramerUsageState based on Integer32"""
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


_VsrSvsFramerUsageState_Type.__name__ = "Integer32"
_VsrSvsFramerUsageState_Object = MibTableColumn
vsrSvsFramerUsageState = _VsrSvsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 14, 1, 3),
    _VsrSvsFramerUsageState_Type()
)
vsrSvsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerUsageState.setStatus("mandatory")
_VsrSvsFramerStatsTable_Object = MibTable
vsrSvsFramerStatsTable = _VsrSvsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15)
)
if mibBuilder.loadTexts:
    vsrSvsFramerStatsTable.setStatus("mandatory")
_VsrSvsFramerStatsEntry_Object = MibTableRow
vsrSvsFramerStatsEntry = _VsrSvsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1)
)
vsrSvsFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerStatsEntry.setStatus("mandatory")


class _VsrSvsFramerTotalCells_Type(Unsigned32):
    """Custom type vsrSvsFramerTotalCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerTotalCells_Type.__name__ = "Unsigned32"
_VsrSvsFramerTotalCells_Object = MibTableColumn
vsrSvsFramerTotalCells = _VsrSvsFramerTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 1),
    _VsrSvsFramerTotalCells_Type()
)
vsrSvsFramerTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerTotalCells.setStatus("mandatory")


class _VsrSvsFramerAudioCells_Type(Unsigned32):
    """Custom type vsrSvsFramerAudioCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerAudioCells_Type.__name__ = "Unsigned32"
_VsrSvsFramerAudioCells_Object = MibTableColumn
vsrSvsFramerAudioCells = _VsrSvsFramerAudioCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 2),
    _VsrSvsFramerAudioCells_Type()
)
vsrSvsFramerAudioCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerAudioCells.setStatus("mandatory")


class _VsrSvsFramerSilenceCells_Type(Unsigned32):
    """Custom type vsrSvsFramerSilenceCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerSilenceCells_Type.__name__ = "Unsigned32"
_VsrSvsFramerSilenceCells_Object = MibTableColumn
vsrSvsFramerSilenceCells = _VsrSvsFramerSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 4),
    _VsrSvsFramerSilenceCells_Type()
)
vsrSvsFramerSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerSilenceCells.setStatus("mandatory")


class _VsrSvsFramerModemCells_Type(Unsigned32):
    """Custom type vsrSvsFramerModemCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerModemCells_Type.__name__ = "Unsigned32"
_VsrSvsFramerModemCells_Object = MibTableColumn
vsrSvsFramerModemCells = _VsrSvsFramerModemCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 5),
    _VsrSvsFramerModemCells_Type()
)
vsrSvsFramerModemCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerModemCells.setStatus("obsolete")


class _VsrSvsFramerCurrentEncodingRate_Type(Integer32):
    """Custom type vsrSvsFramerCurrentEncodingRate based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n03", 15),
          ("n12", 14),
          ("n120", 7),
          ("n144", 6),
          ("n160", 4),
          ("n24", 13),
          ("n240", 3),
          ("n320", 2),
          ("n48", 12),
          ("n53", 11),
          ("n63", 10),
          ("n640", 1),
          ("n72", 9),
          ("n80", 5),
          ("n96", 8))
    )


_VsrSvsFramerCurrentEncodingRate_Type.__name__ = "Integer32"
_VsrSvsFramerCurrentEncodingRate_Object = MibTableColumn
vsrSvsFramerCurrentEncodingRate = _VsrSvsFramerCurrentEncodingRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 6),
    _VsrSvsFramerCurrentEncodingRate_Type()
)
vsrSvsFramerCurrentEncodingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerCurrentEncodingRate.setStatus("obsolete")


class _VsrSvsFramerLrcErrors_Type(Unsigned32):
    """Custom type vsrSvsFramerLrcErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerLrcErrors_Type.__name__ = "Unsigned32"
_VsrSvsFramerLrcErrors_Object = MibTableColumn
vsrSvsFramerLrcErrors = _VsrSvsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 7),
    _VsrSvsFramerLrcErrors_Type()
)
vsrSvsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerLrcErrors.setStatus("mandatory")


class _VsrSvsFramerFrmLostInNetwork_Type(Unsigned32):
    """Custom type vsrSvsFramerFrmLostInNetwork based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerFrmLostInNetwork_Type.__name__ = "Unsigned32"
_VsrSvsFramerFrmLostInNetwork_Object = MibTableColumn
vsrSvsFramerFrmLostInNetwork = _VsrSvsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 8),
    _VsrSvsFramerFrmLostInNetwork_Type()
)
vsrSvsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmLostInNetwork.setStatus("mandatory")


class _VsrSvsFramerFrmUnderRuns_Type(Unsigned32):
    """Custom type vsrSvsFramerFrmUnderRuns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerFrmUnderRuns_Type.__name__ = "Unsigned32"
_VsrSvsFramerFrmUnderRuns_Object = MibTableColumn
vsrSvsFramerFrmUnderRuns = _VsrSvsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 9),
    _VsrSvsFramerFrmUnderRuns_Type()
)
vsrSvsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmUnderRuns.setStatus("mandatory")


class _VsrSvsFramerFrmDumped_Type(Unsigned32):
    """Custom type vsrSvsFramerFrmDumped based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerFrmDumped_Type.__name__ = "Unsigned32"
_VsrSvsFramerFrmDumped_Object = MibTableColumn
vsrSvsFramerFrmDumped = _VsrSvsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 10),
    _VsrSvsFramerFrmDumped_Type()
)
vsrSvsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmDumped.setStatus("mandatory")
_VsrSvsFramerModemSilenceCells_Type = Counter32
_VsrSvsFramerModemSilenceCells_Object = MibTableColumn
vsrSvsFramerModemSilenceCells = _VsrSvsFramerModemSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 26),
    _VsrSvsFramerModemSilenceCells_Type()
)
vsrSvsFramerModemSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerModemSilenceCells.setStatus("obsolete")


class _VsrSvsFramerCurrentEncoding_Type(Integer32):
    """Custom type vsrSvsFramerCurrentEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              64,
              65,
              66,
              67,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faxRelay", 64),
          ("g711", 5),
          ("g723", 3),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17", 67),
          ("v22", 32),
          ("v22bis", 33),
          ("v27", 65),
          ("v29", 66))
    )


_VsrSvsFramerCurrentEncoding_Type.__name__ = "Integer32"
_VsrSvsFramerCurrentEncoding_Object = MibTableColumn
vsrSvsFramerCurrentEncoding = _VsrSvsFramerCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 27),
    _VsrSvsFramerCurrentEncoding_Type()
)
vsrSvsFramerCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerCurrentEncoding.setStatus("obsolete")


class _VsrSvsFramerTptStatus_Type(Integer32):
    """Custom type vsrSvsFramerTptStatus based on Integer32"""
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
        *(("disabled", 3),
          ("monitoring", 2),
          ("operating", 0),
          ("rejected", 1))
    )


_VsrSvsFramerTptStatus_Type.__name__ = "Integer32"
_VsrSvsFramerTptStatus_Object = MibTableColumn
vsrSvsFramerTptStatus = _VsrSvsFramerTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 28),
    _VsrSvsFramerTptStatus_Type()
)
vsrSvsFramerTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerTptStatus.setStatus("obsolete")
_VsrSvsFramerFaxRelayCells_Type = Counter32
_VsrSvsFramerFaxRelayCells_Object = MibTableColumn
vsrSvsFramerFaxRelayCells = _VsrSvsFramerFaxRelayCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 35),
    _VsrSvsFramerFaxRelayCells_Type()
)
vsrSvsFramerFaxRelayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFaxRelayCells.setStatus("mandatory")


class _VsrSvsFramerModemFaxCells_Type(Unsigned32):
    """Custom type vsrSvsFramerModemFaxCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerModemFaxCells_Type.__name__ = "Unsigned32"
_VsrSvsFramerModemFaxCells_Object = MibTableColumn
vsrSvsFramerModemFaxCells = _VsrSvsFramerModemFaxCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 36),
    _VsrSvsFramerModemFaxCells_Type()
)
vsrSvsFramerModemFaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerModemFaxCells.setStatus("mandatory")
_VsrSvsFramerFaxIdleCells_Type = Counter32
_VsrSvsFramerFaxIdleCells_Object = MibTableColumn
vsrSvsFramerFaxIdleCells = _VsrSvsFramerFaxIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 15, 1, 37),
    _VsrSvsFramerFaxIdleCells_Type()
)
vsrSvsFramerFaxIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFaxIdleCells.setStatus("mandatory")
_VsrSvsFramerOperTable_Object = MibTable
vsrSvsFramerOperTable = _VsrSvsFramerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 16)
)
if mibBuilder.loadTexts:
    vsrSvsFramerOperTable.setStatus("mandatory")
_VsrSvsFramerOperEntry_Object = MibTableRow
vsrSvsFramerOperEntry = _VsrSvsFramerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 16, 1)
)
vsrSvsFramerOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerOperEntry.setStatus("mandatory")


class _VsrSvsFramerOpCurrentEncoding_Type(Integer32):
    """Custom type vsrSvsFramerOpCurrentEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              64,
              65,
              66,
              67,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faxRelay", 64),
          ("g711", 5),
          ("g723", 3),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17", 67),
          ("v22", 32),
          ("v22bis", 33),
          ("v27", 65),
          ("v29", 66))
    )


_VsrSvsFramerOpCurrentEncoding_Type.__name__ = "Integer32"
_VsrSvsFramerOpCurrentEncoding_Object = MibTableColumn
vsrSvsFramerOpCurrentEncoding = _VsrSvsFramerOpCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 16, 1, 1),
    _VsrSvsFramerOpCurrentEncoding_Type()
)
vsrSvsFramerOpCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerOpCurrentEncoding.setStatus("mandatory")


class _VsrSvsFramerCurrentRate_Type(Integer32):
    """Custom type vsrSvsFramerCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n03", 15),
          ("n12", 14),
          ("n120", 7),
          ("n144", 6),
          ("n160", 4),
          ("n24", 13),
          ("n240", 3),
          ("n320", 2),
          ("n48", 12),
          ("n53", 11),
          ("n63", 10),
          ("n640", 1),
          ("n72", 9),
          ("n80", 5),
          ("n96", 8))
    )


_VsrSvsFramerCurrentRate_Type.__name__ = "Integer32"
_VsrSvsFramerCurrentRate_Object = MibTableColumn
vsrSvsFramerCurrentRate = _VsrSvsFramerCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 16, 1, 2),
    _VsrSvsFramerCurrentRate_Type()
)
vsrSvsFramerCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerCurrentRate.setStatus("mandatory")


class _VsrSvsFramerOpTptStatus_Type(Integer32):
    """Custom type vsrSvsFramerOpTptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("monitoring", 2),
          ("operating", 0))
    )


_VsrSvsFramerOpTptStatus_Type.__name__ = "Integer32"
_VsrSvsFramerOpTptStatus_Object = MibTableColumn
vsrSvsFramerOpTptStatus = _VsrSvsFramerOpTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 16, 1, 3),
    _VsrSvsFramerOpTptStatus_Type()
)
vsrSvsFramerOpTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerOpTptStatus.setStatus("mandatory")
_VsrSvsFramerNegTable_Object = MibTable
vsrSvsFramerNegTable = _VsrSvsFramerNegTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17)
)
if mibBuilder.loadTexts:
    vsrSvsFramerNegTable.setStatus("mandatory")
_VsrSvsFramerNegEntry_Object = MibTableRow
vsrSvsFramerNegEntry = _VsrSvsFramerNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17, 1)
)
vsrSvsFramerNegEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerNegEntry.setStatus("mandatory")


class _VsrSvsFramerNegotiatedSilenceSuppression_Type(Integer32):
    """Custom type vsrSvsFramerNegotiatedSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_VsrSvsFramerNegotiatedSilenceSuppression_Type.__name__ = "Integer32"
_VsrSvsFramerNegotiatedSilenceSuppression_Object = MibTableColumn
vsrSvsFramerNegotiatedSilenceSuppression = _VsrSvsFramerNegotiatedSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17, 1, 1),
    _VsrSvsFramerNegotiatedSilenceSuppression_Type()
)
vsrSvsFramerNegotiatedSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsFramerNegotiatedSilenceSuppression.setStatus("mandatory")


class _VsrSvsFramerNegotiatedFisG711G726_Type(Integer32):
    """Custom type vsrSvsFramerNegotiatedFisG711G726 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VsrSvsFramerNegotiatedFisG711G726_Type.__name__ = "Integer32"
_VsrSvsFramerNegotiatedFisG711G726_Object = MibTableColumn
vsrSvsFramerNegotiatedFisG711G726 = _VsrSvsFramerNegotiatedFisG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17, 1, 2),
    _VsrSvsFramerNegotiatedFisG711G726_Type()
)
vsrSvsFramerNegotiatedFisG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsFramerNegotiatedFisG711G726.setStatus("mandatory")


class _VsrSvsFramerNegotiatedDtmfRegeneration_Type(Integer32):
    """Custom type vsrSvsFramerNegotiatedDtmfRegeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VsrSvsFramerNegotiatedDtmfRegeneration_Type.__name__ = "Integer32"
_VsrSvsFramerNegotiatedDtmfRegeneration_Object = MibTableColumn
vsrSvsFramerNegotiatedDtmfRegeneration = _VsrSvsFramerNegotiatedDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17, 1, 3),
    _VsrSvsFramerNegotiatedDtmfRegeneration_Type()
)
vsrSvsFramerNegotiatedDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsFramerNegotiatedDtmfRegeneration.setStatus("mandatory")


class _VsrSvsFramerNegotiatedV17AsG711G726_Type(Integer32):
    """Custom type vsrSvsFramerNegotiatedV17AsG711G726 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VsrSvsFramerNegotiatedV17AsG711G726_Type.__name__ = "Integer32"
_VsrSvsFramerNegotiatedV17AsG711G726_Object = MibTableColumn
vsrSvsFramerNegotiatedV17AsG711G726 = _VsrSvsFramerNegotiatedV17AsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17, 1, 4),
    _VsrSvsFramerNegotiatedV17AsG711G726_Type()
)
vsrSvsFramerNegotiatedV17AsG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerNegotiatedV17AsG711G726.setStatus("mandatory")


class _VsrSvsFramerNegotiatedTandemPassThrough_Type(Integer32):
    """Custom type vsrSvsFramerNegotiatedTandemPassThrough based on Integer32"""
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


_VsrSvsFramerNegotiatedTandemPassThrough_Type.__name__ = "Integer32"
_VsrSvsFramerNegotiatedTandemPassThrough_Object = MibTableColumn
vsrSvsFramerNegotiatedTandemPassThrough = _VsrSvsFramerNegotiatedTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 17, 1, 5),
    _VsrSvsFramerNegotiatedTandemPassThrough_Type()
)
vsrSvsFramerNegotiatedTandemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerNegotiatedTandemPassThrough.setStatus("mandatory")
_VsrSvsFramerFrmToNetworkTable_Object = MibTable
vsrSvsFramerFrmToNetworkTable = _VsrSvsFramerFrmToNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 315)
)
if mibBuilder.loadTexts:
    vsrSvsFramerFrmToNetworkTable.setStatus("mandatory")
_VsrSvsFramerFrmToNetworkEntry_Object = MibTableRow
vsrSvsFramerFrmToNetworkEntry = _VsrSvsFramerFrmToNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 315, 1)
)
vsrSvsFramerFrmToNetworkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerFrmToNetworkIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerFrmToNetworkEntry.setStatus("mandatory")


class _VsrSvsFramerFrmToNetworkIndex_Type(Integer32):
    """Custom type vsrSvsFramerFrmToNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n16KbitS", 3),
          ("n24KbitS", 2),
          ("n32KbitS", 1),
          ("n64KbitS", 0),
          ("n8KbitS", 4))
    )


_VsrSvsFramerFrmToNetworkIndex_Type.__name__ = "Integer32"
_VsrSvsFramerFrmToNetworkIndex_Object = MibTableColumn
vsrSvsFramerFrmToNetworkIndex = _VsrSvsFramerFrmToNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 315, 1, 1),
    _VsrSvsFramerFrmToNetworkIndex_Type()
)
vsrSvsFramerFrmToNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmToNetworkIndex.setStatus("mandatory")


class _VsrSvsFramerFrmToNetworkValue_Type(Unsigned32):
    """Custom type vsrSvsFramerFrmToNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerFrmToNetworkValue_Type.__name__ = "Unsigned32"
_VsrSvsFramerFrmToNetworkValue_Object = MibTableColumn
vsrSvsFramerFrmToNetworkValue = _VsrSvsFramerFrmToNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 315, 1, 2),
    _VsrSvsFramerFrmToNetworkValue_Type()
)
vsrSvsFramerFrmToNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmToNetworkValue.setStatus("mandatory")
_VsrSvsFramerFrmFromNetworkTable_Object = MibTable
vsrSvsFramerFrmFromNetworkTable = _VsrSvsFramerFrmFromNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 316)
)
if mibBuilder.loadTexts:
    vsrSvsFramerFrmFromNetworkTable.setStatus("mandatory")
_VsrSvsFramerFrmFromNetworkEntry_Object = MibTableRow
vsrSvsFramerFrmFromNetworkEntry = _VsrSvsFramerFrmFromNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 316, 1)
)
vsrSvsFramerFrmFromNetworkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerFrmFromNetworkIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerFrmFromNetworkEntry.setStatus("mandatory")


class _VsrSvsFramerFrmFromNetworkIndex_Type(Integer32):
    """Custom type vsrSvsFramerFrmFromNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n16KbitS", 3),
          ("n24KbitS", 2),
          ("n32KbitS", 1),
          ("n64KbitS", 0),
          ("n8KbitS", 4))
    )


_VsrSvsFramerFrmFromNetworkIndex_Type.__name__ = "Integer32"
_VsrSvsFramerFrmFromNetworkIndex_Object = MibTableColumn
vsrSvsFramerFrmFromNetworkIndex = _VsrSvsFramerFrmFromNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 316, 1, 1),
    _VsrSvsFramerFrmFromNetworkIndex_Type()
)
vsrSvsFramerFrmFromNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmFromNetworkIndex.setStatus("mandatory")


class _VsrSvsFramerFrmFromNetworkValue_Type(Unsigned32):
    """Custom type vsrSvsFramerFrmFromNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsFramerFrmFromNetworkValue_Type.__name__ = "Unsigned32"
_VsrSvsFramerFrmFromNetworkValue_Object = MibTableColumn
vsrSvsFramerFrmFromNetworkValue = _VsrSvsFramerFrmFromNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 316, 1, 2),
    _VsrSvsFramerFrmFromNetworkValue_Type()
)
vsrSvsFramerFrmFromNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsFramerFrmFromNetworkValue.setStatus("mandatory")
_VsrSvsFramerNEncodingTable_Object = MibTable
vsrSvsFramerNEncodingTable = _VsrSvsFramerNEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 467)
)
if mibBuilder.loadTexts:
    vsrSvsFramerNEncodingTable.setStatus("mandatory")
_VsrSvsFramerNEncodingEntry_Object = MibTableRow
vsrSvsFramerNEncodingEntry = _VsrSvsFramerNEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 467, 1)
)
vsrSvsFramerNEncodingEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerNEncodingIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerNEncodingEntry.setStatus("mandatory")


class _VsrSvsFramerNEncodingIndex_Type(Integer32):
    """Custom type vsrSvsFramerNEncodingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("modemFax", 1),
          ("voice", 0))
    )


_VsrSvsFramerNEncodingIndex_Type.__name__ = "Integer32"
_VsrSvsFramerNEncodingIndex_Object = MibTableColumn
vsrSvsFramerNEncodingIndex = _VsrSvsFramerNEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 467, 1, 1),
    _VsrSvsFramerNEncodingIndex_Type()
)
vsrSvsFramerNEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerNEncodingIndex.setStatus("mandatory")


class _VsrSvsFramerNEncodingValue_Type(Integer32):
    """Custom type vsrSvsFramerNEncodingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              31,
              64,
              68,
              255)
        )
    )
    namedValues = NamedValues(
        *(("g711", 5),
          ("g711G726", 31),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17V29V27Relay", 68),
          ("v29V27Relay", 64))
    )


_VsrSvsFramerNEncodingValue_Type.__name__ = "Integer32"
_VsrSvsFramerNEncodingValue_Object = MibTableColumn
vsrSvsFramerNEncodingValue = _VsrSvsFramerNEncodingValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 467, 1, 2),
    _VsrSvsFramerNEncodingValue_Type()
)
vsrSvsFramerNEncodingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsFramerNEncodingValue.setStatus("mandatory")
_VsrSvsFramerNRatesTable_Object = MibTable
vsrSvsFramerNRatesTable = _VsrSvsFramerNRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 479)
)
if mibBuilder.loadTexts:
    vsrSvsFramerNRatesTable.setStatus("mandatory")
_VsrSvsFramerNRatesEntry_Object = MibTableRow
vsrSvsFramerNRatesEntry = _VsrSvsFramerNRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 479, 1)
)
vsrSvsFramerNRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerNRatesTrafficIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsFramerNRatesRateIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsFramerNRatesEntry.setStatus("mandatory")


class _VsrSvsFramerNRatesTrafficIndex_Type(Integer32):
    """Custom type vsrSvsFramerNRatesTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("modemFax", 1),
          ("voice", 0))
    )


_VsrSvsFramerNRatesTrafficIndex_Type.__name__ = "Integer32"
_VsrSvsFramerNRatesTrafficIndex_Object = MibTableColumn
vsrSvsFramerNRatesTrafficIndex = _VsrSvsFramerNRatesTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 479, 1, 1),
    _VsrSvsFramerNRatesTrafficIndex_Type()
)
vsrSvsFramerNRatesTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerNRatesTrafficIndex.setStatus("mandatory")


class _VsrSvsFramerNRatesRateIndex_Type(Integer32):
    """Custom type vsrSvsFramerNRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_VsrSvsFramerNRatesRateIndex_Type.__name__ = "Integer32"
_VsrSvsFramerNRatesRateIndex_Object = MibTableColumn
vsrSvsFramerNRatesRateIndex = _VsrSvsFramerNRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 479, 1, 2),
    _VsrSvsFramerNRatesRateIndex_Type()
)
vsrSvsFramerNRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsFramerNRatesRateIndex.setStatus("mandatory")


class _VsrSvsFramerNRatesValue_Type(Integer32):
    """Custom type vsrSvsFramerNRatesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              66,
              67,
              68,
              69,
              70)
        )
    )
    namedValues = NamedValues(
        *(("n00", 0),
          ("n03", 1),
          ("n12", 2),
          ("n120", 7),
          ("n144", 8),
          ("n160", 67),
          ("n24", 3),
          ("n240", 68),
          ("n320", 69),
          ("n48", 4),
          ("n640", 70),
          ("n72", 5),
          ("n80", 66),
          ("n96", 6))
    )


_VsrSvsFramerNRatesValue_Type.__name__ = "Integer32"
_VsrSvsFramerNRatesValue_Object = MibTableColumn
vsrSvsFramerNRatesValue = _VsrSvsFramerNRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 2, 479, 1, 3),
    _VsrSvsFramerNRatesValue_Type()
)
vsrSvsFramerNRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsFramerNRatesValue.setStatus("mandatory")
_VsrSvsLCo_ObjectIdentity = ObjectIdentity
vsrSvsLCo = _VsrSvsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3)
)
_VsrSvsLCoRowStatusTable_Object = MibTable
vsrSvsLCoRowStatusTable = _VsrSvsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vsrSvsLCoRowStatusTable.setStatus("mandatory")
_VsrSvsLCoRowStatusEntry_Object = MibTableRow
vsrSvsLCoRowStatusEntry = _VsrSvsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 1, 1)
)
vsrSvsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsLCoIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsLCoRowStatusEntry.setStatus("mandatory")
_VsrSvsLCoRowStatus_Type = RowStatus
_VsrSvsLCoRowStatus_Object = MibTableColumn
vsrSvsLCoRowStatus = _VsrSvsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 1, 1, 1),
    _VsrSvsLCoRowStatus_Type()
)
vsrSvsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRowStatus.setStatus("mandatory")
_VsrSvsLCoComponentName_Type = DisplayString
_VsrSvsLCoComponentName_Object = MibTableColumn
vsrSvsLCoComponentName = _VsrSvsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 1, 1, 2),
    _VsrSvsLCoComponentName_Type()
)
vsrSvsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoComponentName.setStatus("mandatory")
_VsrSvsLCoStorageType_Type = StorageType
_VsrSvsLCoStorageType_Object = MibTableColumn
vsrSvsLCoStorageType = _VsrSvsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 1, 1, 4),
    _VsrSvsLCoStorageType_Type()
)
vsrSvsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoStorageType.setStatus("mandatory")
_VsrSvsLCoIndex_Type = NonReplicated
_VsrSvsLCoIndex_Object = MibTableColumn
vsrSvsLCoIndex = _VsrSvsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 1, 1, 10),
    _VsrSvsLCoIndex_Type()
)
vsrSvsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsLCoIndex.setStatus("mandatory")
_VsrSvsLCoPathDataTable_Object = MibTable
vsrSvsLCoPathDataTable = _VsrSvsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vsrSvsLCoPathDataTable.setStatus("mandatory")
_VsrSvsLCoPathDataEntry_Object = MibTableRow
vsrSvsLCoPathDataEntry = _VsrSvsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1)
)
vsrSvsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsLCoIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsLCoPathDataEntry.setStatus("mandatory")


class _VsrSvsLCoState_Type(Integer32):
    """Custom type vsrSvsLCoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("pathDown", 0),
          ("pathDownRetrying", 4),
          ("pathUp", 3),
          ("selectingRoute", 1))
    )


_VsrSvsLCoState_Type.__name__ = "Integer32"
_VsrSvsLCoState_Object = MibTableColumn
vsrSvsLCoState = _VsrSvsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 1),
    _VsrSvsLCoState_Type()
)
vsrSvsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoState.setStatus("mandatory")


class _VsrSvsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type vsrSvsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsrSvsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_VsrSvsLCoOverrideRemoteName_Object = MibTableColumn
vsrSvsLCoOverrideRemoteName = _VsrSvsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 2),
    _VsrSvsLCoOverrideRemoteName_Type()
)
vsrSvsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsLCoOverrideRemoteName.setStatus("mandatory")


class _VsrSvsLCoEnd_Type(Integer32):
    """Custom type vsrSvsLCoEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 0))
    )


_VsrSvsLCoEnd_Type.__name__ = "Integer32"
_VsrSvsLCoEnd_Object = MibTableColumn
vsrSvsLCoEnd = _VsrSvsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 3),
    _VsrSvsLCoEnd_Type()
)
vsrSvsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoEnd.setStatus("mandatory")


class _VsrSvsLCoCostMetric_Type(Unsigned32):
    """Custom type vsrSvsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsrSvsLCoCostMetric_Type.__name__ = "Unsigned32"
_VsrSvsLCoCostMetric_Object = MibTableColumn
vsrSvsLCoCostMetric = _VsrSvsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 4),
    _VsrSvsLCoCostMetric_Type()
)
vsrSvsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoCostMetric.setStatus("mandatory")


class _VsrSvsLCoDelayMetric_Type(Unsigned32):
    """Custom type vsrSvsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VsrSvsLCoDelayMetric_Type.__name__ = "Unsigned32"
_VsrSvsLCoDelayMetric_Object = MibTableColumn
vsrSvsLCoDelayMetric = _VsrSvsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 5),
    _VsrSvsLCoDelayMetric_Type()
)
vsrSvsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoDelayMetric.setStatus("mandatory")


class _VsrSvsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type vsrSvsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_VsrSvsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_VsrSvsLCoRoundTripDelay_Object = MibTableColumn
vsrSvsLCoRoundTripDelay = _VsrSvsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 6),
    _VsrSvsLCoRoundTripDelay_Type()
)
vsrSvsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRoundTripDelay.setStatus("mandatory")


class _VsrSvsLCoSetupPriority_Type(Unsigned32):
    """Custom type vsrSvsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsrSvsLCoSetupPriority_Type.__name__ = "Unsigned32"
_VsrSvsLCoSetupPriority_Object = MibTableColumn
vsrSvsLCoSetupPriority = _VsrSvsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 7),
    _VsrSvsLCoSetupPriority_Type()
)
vsrSvsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoSetupPriority.setStatus("mandatory")


class _VsrSvsLCoHoldingPriority_Type(Unsigned32):
    """Custom type vsrSvsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsrSvsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_VsrSvsLCoHoldingPriority_Object = MibTableColumn
vsrSvsLCoHoldingPriority = _VsrSvsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 8),
    _VsrSvsLCoHoldingPriority_Type()
)
vsrSvsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoHoldingPriority.setStatus("mandatory")


class _VsrSvsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type vsrSvsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_VsrSvsLCoRequiredTxBandwidth_Object = MibTableColumn
vsrSvsLCoRequiredTxBandwidth = _VsrSvsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 9),
    _VsrSvsLCoRequiredTxBandwidth_Type()
)
vsrSvsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRequiredTxBandwidth.setStatus("mandatory")


class _VsrSvsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type vsrSvsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsrSvsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_VsrSvsLCoRequiredRxBandwidth_Object = MibTableColumn
vsrSvsLCoRequiredRxBandwidth = _VsrSvsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 10),
    _VsrSvsLCoRequiredRxBandwidth_Type()
)
vsrSvsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRequiredRxBandwidth.setStatus("mandatory")


class _VsrSvsLCoRequiredTrafficType_Type(Integer32):
    """Custom type vsrSvsLCoRequiredTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_VsrSvsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_VsrSvsLCoRequiredTrafficType_Object = MibTableColumn
vsrSvsLCoRequiredTrafficType = _VsrSvsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 11),
    _VsrSvsLCoRequiredTrafficType_Type()
)
vsrSvsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRequiredTrafficType.setStatus("mandatory")


class _VsrSvsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type vsrSvsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VsrSvsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_VsrSvsLCoPermittedTrunkTypes_Object = MibTableColumn
vsrSvsLCoPermittedTrunkTypes = _VsrSvsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 12),
    _VsrSvsLCoPermittedTrunkTypes_Type()
)
vsrSvsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPermittedTrunkTypes.setStatus("mandatory")


class _VsrSvsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type vsrSvsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VsrSvsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_VsrSvsLCoRequiredSecurity_Object = MibTableColumn
vsrSvsLCoRequiredSecurity = _VsrSvsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 13),
    _VsrSvsLCoRequiredSecurity_Type()
)
vsrSvsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRequiredSecurity.setStatus("mandatory")


class _VsrSvsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type vsrSvsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VsrSvsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_VsrSvsLCoRequiredCustomerParameter_Object = MibTableColumn
vsrSvsLCoRequiredCustomerParameter = _VsrSvsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 14),
    _VsrSvsLCoRequiredCustomerParameter_Type()
)
vsrSvsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRequiredCustomerParameter.setStatus("mandatory")


class _VsrSvsLCoEmissionPriority_Type(Unsigned32):
    """Custom type vsrSvsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VsrSvsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_VsrSvsLCoEmissionPriority_Object = MibTableColumn
vsrSvsLCoEmissionPriority = _VsrSvsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 15),
    _VsrSvsLCoEmissionPriority_Type()
)
vsrSvsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoEmissionPriority.setStatus("mandatory")


class _VsrSvsLCoDiscardPriority_Type(Unsigned32):
    """Custom type vsrSvsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VsrSvsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_VsrSvsLCoDiscardPriority_Object = MibTableColumn
vsrSvsLCoDiscardPriority = _VsrSvsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 16),
    _VsrSvsLCoDiscardPriority_Type()
)
vsrSvsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoDiscardPriority.setStatus("mandatory")


class _VsrSvsLCoPathType_Type(Integer32):
    """Custom type vsrSvsLCoPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_VsrSvsLCoPathType_Type.__name__ = "Integer32"
_VsrSvsLCoPathType_Object = MibTableColumn
vsrSvsLCoPathType = _VsrSvsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 17),
    _VsrSvsLCoPathType_Type()
)
vsrSvsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPathType.setStatus("mandatory")


class _VsrSvsLCoRetryCount_Type(Unsigned32):
    """Custom type vsrSvsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VsrSvsLCoRetryCount_Type.__name__ = "Unsigned32"
_VsrSvsLCoRetryCount_Object = MibTableColumn
vsrSvsLCoRetryCount = _VsrSvsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 18),
    _VsrSvsLCoRetryCount_Type()
)
vsrSvsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoRetryCount.setStatus("mandatory")


class _VsrSvsLCoPathFailureCount_Type(Unsigned32):
    """Custom type vsrSvsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsrSvsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_VsrSvsLCoPathFailureCount_Object = MibTableColumn
vsrSvsLCoPathFailureCount = _VsrSvsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 19),
    _VsrSvsLCoPathFailureCount_Type()
)
vsrSvsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPathFailureCount.setStatus("mandatory")


class _VsrSvsLCoReasonForNoRoute_Type(Integer32):
    """Custom type vsrSvsLCoReasonForNoRoute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("anError", 12),
          ("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routesDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_VsrSvsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_VsrSvsLCoReasonForNoRoute_Object = MibTableColumn
vsrSvsLCoReasonForNoRoute = _VsrSvsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 20),
    _VsrSvsLCoReasonForNoRoute_Type()
)
vsrSvsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoReasonForNoRoute.setStatus("mandatory")


class _VsrSvsLCoLastTearDownReason_Type(Integer32):
    """Custom type vsrSvsLCoLastTearDownReason based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("callLoopedBack", 13),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("normalShutDown", 1),
          ("operatorForced", 6),
          ("optimized", 21),
          ("overrideRemoteName", 22),
          ("reconnectFromFarEnd", 18),
          ("remoteNameMismatch", 16),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("trunkOrFarEndDidNotSupportMode", 23),
          ("unknownReason", 14),
          ("wrongModuleReached", 11))
    )


_VsrSvsLCoLastTearDownReason_Type.__name__ = "Integer32"
_VsrSvsLCoLastTearDownReason_Object = MibTableColumn
vsrSvsLCoLastTearDownReason = _VsrSvsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 21),
    _VsrSvsLCoLastTearDownReason_Type()
)
vsrSvsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoLastTearDownReason.setStatus("mandatory")


class _VsrSvsLCoPathFailureAction_Type(Integer32):
    """Custom type vsrSvsLCoPathFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_VsrSvsLCoPathFailureAction_Type.__name__ = "Integer32"
_VsrSvsLCoPathFailureAction_Object = MibTableColumn
vsrSvsLCoPathFailureAction = _VsrSvsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 22),
    _VsrSvsLCoPathFailureAction_Type()
)
vsrSvsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPathFailureAction.setStatus("mandatory")


class _VsrSvsLCoBumpPreference_Type(Integer32):
    """Custom type vsrSvsLCoBumpPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_VsrSvsLCoBumpPreference_Type.__name__ = "Integer32"
_VsrSvsLCoBumpPreference_Object = MibTableColumn
vsrSvsLCoBumpPreference = _VsrSvsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 23),
    _VsrSvsLCoBumpPreference_Type()
)
vsrSvsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoBumpPreference.setStatus("mandatory")


class _VsrSvsLCoOptimization_Type(Integer32):
    """Custom type vsrSvsLCoOptimization based on Integer32"""
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


_VsrSvsLCoOptimization_Type.__name__ = "Integer32"
_VsrSvsLCoOptimization_Object = MibTableColumn
vsrSvsLCoOptimization = _VsrSvsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 24),
    _VsrSvsLCoOptimization_Type()
)
vsrSvsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoOptimization.setStatus("mandatory")


class _VsrSvsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type vsrSvsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_VsrSvsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_VsrSvsLCoPathUpDateTime_Object = MibTableColumn
vsrSvsLCoPathUpDateTime = _VsrSvsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 10, 1, 25),
    _VsrSvsLCoPathUpDateTime_Type()
)
vsrSvsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPathUpDateTime.setStatus("mandatory")
_VsrSvsLCoStatsTable_Object = MibTable
vsrSvsLCoStatsTable = _VsrSvsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vsrSvsLCoStatsTable.setStatus("mandatory")
_VsrSvsLCoStatsEntry_Object = MibTableRow
vsrSvsLCoStatsEntry = _VsrSvsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 11, 1)
)
vsrSvsLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsLCoIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsLCoStatsEntry.setStatus("mandatory")
_VsrSvsLCoPktsToNetwork_Type = PassportCounter64
_VsrSvsLCoPktsToNetwork_Object = MibTableColumn
vsrSvsLCoPktsToNetwork = _VsrSvsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 11, 1, 1),
    _VsrSvsLCoPktsToNetwork_Type()
)
vsrSvsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPktsToNetwork.setStatus("mandatory")
_VsrSvsLCoBytesToNetwork_Type = PassportCounter64
_VsrSvsLCoBytesToNetwork_Object = MibTableColumn
vsrSvsLCoBytesToNetwork = _VsrSvsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 11, 1, 2),
    _VsrSvsLCoBytesToNetwork_Type()
)
vsrSvsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoBytesToNetwork.setStatus("mandatory")
_VsrSvsLCoPktsFromNetwork_Type = PassportCounter64
_VsrSvsLCoPktsFromNetwork_Object = MibTableColumn
vsrSvsLCoPktsFromNetwork = _VsrSvsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 11, 1, 3),
    _VsrSvsLCoPktsFromNetwork_Type()
)
vsrSvsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPktsFromNetwork.setStatus("mandatory")
_VsrSvsLCoBytesFromNetwork_Type = PassportCounter64
_VsrSvsLCoBytesFromNetwork_Object = MibTableColumn
vsrSvsLCoBytesFromNetwork = _VsrSvsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 11, 1, 4),
    _VsrSvsLCoBytesFromNetwork_Type()
)
vsrSvsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoBytesFromNetwork.setStatus("mandatory")
_VsrSvsLCoPathTable_Object = MibTable
vsrSvsLCoPathTable = _VsrSvsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 264)
)
if mibBuilder.loadTexts:
    vsrSvsLCoPathTable.setStatus("mandatory")
_VsrSvsLCoPathEntry_Object = MibTableRow
vsrSvsLCoPathEntry = _VsrSvsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 264, 1)
)
vsrSvsLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsLCoIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsLCoPathValue"),
)
if mibBuilder.loadTexts:
    vsrSvsLCoPathEntry.setStatus("mandatory")


class _VsrSvsLCoPathValue_Type(AsciiString):
    """Custom type vsrSvsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsrSvsLCoPathValue_Type.__name__ = "AsciiString"
_VsrSvsLCoPathValue_Object = MibTableColumn
vsrSvsLCoPathValue = _VsrSvsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 3, 264, 1, 1),
    _VsrSvsLCoPathValue_Type()
)
vsrSvsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsLCoPathValue.setStatus("mandatory")
_VsrSvsDebug_ObjectIdentity = ObjectIdentity
vsrSvsDebug = _VsrSvsDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4)
)
_VsrSvsDebugRowStatusTable_Object = MibTable
vsrSvsDebugRowStatusTable = _VsrSvsDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vsrSvsDebugRowStatusTable.setStatus("mandatory")
_VsrSvsDebugRowStatusEntry_Object = MibTableRow
vsrSvsDebugRowStatusEntry = _VsrSvsDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4, 1, 1)
)
vsrSvsDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsDebugIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsDebugRowStatusEntry.setStatus("mandatory")
_VsrSvsDebugRowStatus_Type = RowStatus
_VsrSvsDebugRowStatus_Object = MibTableColumn
vsrSvsDebugRowStatus = _VsrSvsDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4, 1, 1, 1),
    _VsrSvsDebugRowStatus_Type()
)
vsrSvsDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsDebugRowStatus.setStatus("mandatory")
_VsrSvsDebugComponentName_Type = DisplayString
_VsrSvsDebugComponentName_Object = MibTableColumn
vsrSvsDebugComponentName = _VsrSvsDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4, 1, 1, 2),
    _VsrSvsDebugComponentName_Type()
)
vsrSvsDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsDebugComponentName.setStatus("mandatory")
_VsrSvsDebugStorageType_Type = StorageType
_VsrSvsDebugStorageType_Object = MibTableColumn
vsrSvsDebugStorageType = _VsrSvsDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4, 1, 1, 4),
    _VsrSvsDebugStorageType_Type()
)
vsrSvsDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsDebugStorageType.setStatus("mandatory")
_VsrSvsDebugIndex_Type = NonReplicated
_VsrSvsDebugIndex_Object = MibTableColumn
vsrSvsDebugIndex = _VsrSvsDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 4, 1, 1, 10),
    _VsrSvsDebugIndex_Type()
)
vsrSvsDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrSvsDebugIndex.setStatus("mandatory")
_VsrSvsIfEntryTable_Object = MibTable
vsrSvsIfEntryTable = _VsrSvsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 11)
)
if mibBuilder.loadTexts:
    vsrSvsIfEntryTable.setStatus("mandatory")
_VsrSvsIfEntryEntry_Object = MibTableRow
vsrSvsIfEntryEntry = _VsrSvsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 11, 1)
)
vsrSvsIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsIfEntryEntry.setStatus("mandatory")


class _VsrSvsIfAdminStatus_Type(Integer32):
    """Custom type vsrSvsIfAdminStatus based on Integer32"""
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


_VsrSvsIfAdminStatus_Type.__name__ = "Integer32"
_VsrSvsIfAdminStatus_Object = MibTableColumn
vsrSvsIfAdminStatus = _VsrSvsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 11, 1, 1),
    _VsrSvsIfAdminStatus_Type()
)
vsrSvsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSvsIfAdminStatus.setStatus("mandatory")


class _VsrSvsIfIndex_Type(InterfaceIndex):
    """Custom type vsrSvsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsrSvsIfIndex_Type.__name__ = "InterfaceIndex"
_VsrSvsIfIndex_Object = MibTableColumn
vsrSvsIfIndex = _VsrSvsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 11, 1, 2),
    _VsrSvsIfIndex_Type()
)
vsrSvsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsIfIndex.setStatus("mandatory")
_VsrSvsOperTable_Object = MibTable
vsrSvsOperTable = _VsrSvsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12)
)
if mibBuilder.loadTexts:
    vsrSvsOperTable.setStatus("mandatory")
_VsrSvsOperEntry_Object = MibTableRow
vsrSvsOperEntry = _VsrSvsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1)
)
vsrSvsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsOperEntry.setStatus("mandatory")


class _VsrSvsStatus_Type(Integer32):
    """Custom type vsrSvsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("answered", 2),
          ("clearing", 3),
          ("idle", 0),
          ("idleMaintenance", 5),
          ("lockout", 4),
          ("seized", 1))
    )


_VsrSvsStatus_Type.__name__ = "Integer32"
_VsrSvsStatus_Object = MibTableColumn
vsrSvsStatus = _VsrSvsStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1, 1),
    _VsrSvsStatus_Type()
)
vsrSvsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsStatus.setStatus("mandatory")
_VsrSvsProfileNumber_Type = Counter32
_VsrSvsProfileNumber_Object = MibTableColumn
vsrSvsProfileNumber = _VsrSvsProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1, 2),
    _VsrSvsProfileNumber_Type()
)
vsrSvsProfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsProfileNumber.setStatus("mandatory")


class _VsrSvsCallType_Type(Integer32):
    """Custom type vsrSvsCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("modem", 2),
          ("voice", 0))
    )


_VsrSvsCallType_Type.__name__ = "Integer32"
_VsrSvsCallType_Object = MibTableColumn
vsrSvsCallType = _VsrSvsCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1, 3),
    _VsrSvsCallType_Type()
)
vsrSvsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsCallType.setStatus("mandatory")


class _VsrSvsCalledNumber_Type(DigitString):
    """Custom type vsrSvsCalledNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VsrSvsCalledNumber_Type.__name__ = "DigitString"
_VsrSvsCalledNumber_Object = MibTableColumn
vsrSvsCalledNumber = _VsrSvsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1, 4),
    _VsrSvsCalledNumber_Type()
)
vsrSvsCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsCalledNumber.setStatus("mandatory")


class _VsrSvsCallingNumber_Type(DigitString):
    """Custom type vsrSvsCallingNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VsrSvsCallingNumber_Type.__name__ = "DigitString"
_VsrSvsCallingNumber_Object = MibTableColumn
vsrSvsCallingNumber = _VsrSvsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1, 5),
    _VsrSvsCallingNumber_Type()
)
vsrSvsCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsCallingNumber.setStatus("mandatory")


class _VsrSvsClearCauseCode_Type(Hex):
    """Custom type vsrSvsClearCauseCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VsrSvsClearCauseCode_Type.__name__ = "Hex"
_VsrSvsClearCauseCode_Object = MibTableColumn
vsrSvsClearCauseCode = _VsrSvsClearCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 12, 1, 6),
    _VsrSvsClearCauseCode_Type()
)
vsrSvsClearCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsClearCauseCode.setStatus("mandatory")
_VsrSvsStatsTable_Object = MibTable
vsrSvsStatsTable = _VsrSvsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 13)
)
if mibBuilder.loadTexts:
    vsrSvsStatsTable.setStatus("mandatory")
_VsrSvsStatsEntry_Object = MibTableRow
vsrSvsStatsEntry = _VsrSvsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 13, 1)
)
vsrSvsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsStatsEntry.setStatus("mandatory")
_VsrSvsTotalCalls_Type = Counter32
_VsrSvsTotalCalls_Object = MibTableColumn
vsrSvsTotalCalls = _VsrSvsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 13, 1, 1),
    _VsrSvsTotalCalls_Type()
)
vsrSvsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsTotalCalls.setStatus("mandatory")
_VsrSvsTotalCallSeconds_Type = Counter32
_VsrSvsTotalCallSeconds_Object = MibTableColumn
vsrSvsTotalCallSeconds = _VsrSvsTotalCallSeconds_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 13, 1, 2),
    _VsrSvsTotalCallSeconds_Type()
)
vsrSvsTotalCallSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsTotalCallSeconds.setStatus("mandatory")
_VsrSvsStateTable_Object = MibTable
vsrSvsStateTable = _VsrSvsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 14)
)
if mibBuilder.loadTexts:
    vsrSvsStateTable.setStatus("mandatory")
_VsrSvsStateEntry_Object = MibTableRow
vsrSvsStateEntry = _VsrSvsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 14, 1)
)
vsrSvsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsStateEntry.setStatus("mandatory")


class _VsrSvsAdminState_Type(Integer32):
    """Custom type vsrSvsAdminState based on Integer32"""
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


_VsrSvsAdminState_Type.__name__ = "Integer32"
_VsrSvsAdminState_Object = MibTableColumn
vsrSvsAdminState = _VsrSvsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 14, 1, 1),
    _VsrSvsAdminState_Type()
)
vsrSvsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsAdminState.setStatus("mandatory")


class _VsrSvsOperationalState_Type(Integer32):
    """Custom type vsrSvsOperationalState based on Integer32"""
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


_VsrSvsOperationalState_Type.__name__ = "Integer32"
_VsrSvsOperationalState_Object = MibTableColumn
vsrSvsOperationalState = _VsrSvsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 14, 1, 2),
    _VsrSvsOperationalState_Type()
)
vsrSvsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsOperationalState.setStatus("mandatory")


class _VsrSvsUsageState_Type(Integer32):
    """Custom type vsrSvsUsageState based on Integer32"""
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


_VsrSvsUsageState_Type.__name__ = "Integer32"
_VsrSvsUsageState_Object = MibTableColumn
vsrSvsUsageState = _VsrSvsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 14, 1, 3),
    _VsrSvsUsageState_Type()
)
vsrSvsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsUsageState.setStatus("mandatory")
_VsrSvsOperStatusTable_Object = MibTable
vsrSvsOperStatusTable = _VsrSvsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 15)
)
if mibBuilder.loadTexts:
    vsrSvsOperStatusTable.setStatus("mandatory")
_VsrSvsOperStatusEntry_Object = MibTableRow
vsrSvsOperStatusEntry = _VsrSvsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 15, 1)
)
vsrSvsOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrSvsIndex"),
)
if mibBuilder.loadTexts:
    vsrSvsOperStatusEntry.setStatus("mandatory")


class _VsrSvsSnmpOperStatus_Type(Integer32):
    """Custom type vsrSvsSnmpOperStatus based on Integer32"""
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


_VsrSvsSnmpOperStatus_Type.__name__ = "Integer32"
_VsrSvsSnmpOperStatus_Object = MibTableColumn
vsrSvsSnmpOperStatus = _VsrSvsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 2, 15, 1, 1),
    _VsrSvsSnmpOperStatus_Type()
)
vsrSvsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSvsSnmpOperStatus.setStatus("mandatory")
_VsrDebug_ObjectIdentity = ObjectIdentity
vsrDebug = _VsrDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3)
)
_VsrDebugRowStatusTable_Object = MibTable
vsrDebugRowStatusTable = _VsrDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3, 1)
)
if mibBuilder.loadTexts:
    vsrDebugRowStatusTable.setStatus("mandatory")
_VsrDebugRowStatusEntry_Object = MibTableRow
vsrDebugRowStatusEntry = _VsrDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3, 1, 1)
)
vsrDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrDebugIndex"),
)
if mibBuilder.loadTexts:
    vsrDebugRowStatusEntry.setStatus("mandatory")
_VsrDebugRowStatus_Type = RowStatus
_VsrDebugRowStatus_Object = MibTableColumn
vsrDebugRowStatus = _VsrDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3, 1, 1, 1),
    _VsrDebugRowStatus_Type()
)
vsrDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrDebugRowStatus.setStatus("mandatory")
_VsrDebugComponentName_Type = DisplayString
_VsrDebugComponentName_Object = MibTableColumn
vsrDebugComponentName = _VsrDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3, 1, 1, 2),
    _VsrDebugComponentName_Type()
)
vsrDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrDebugComponentName.setStatus("mandatory")
_VsrDebugStorageType_Type = StorageType
_VsrDebugStorageType_Object = MibTableColumn
vsrDebugStorageType = _VsrDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3, 1, 1, 4),
    _VsrDebugStorageType_Type()
)
vsrDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrDebugStorageType.setStatus("mandatory")
_VsrDebugIndex_Type = NonReplicated
_VsrDebugIndex_Object = MibTableColumn
vsrDebugIndex = _VsrDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 3, 1, 1, 10),
    _VsrDebugIndex_Type()
)
vsrDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsrDebugIndex.setStatus("mandatory")
_VsrCidDataTable_Object = MibTable
vsrCidDataTable = _VsrCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 10)
)
if mibBuilder.loadTexts:
    vsrCidDataTable.setStatus("mandatory")
_VsrCidDataEntry_Object = MibTableRow
vsrCidDataEntry = _VsrCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 10, 1)
)
vsrCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrCidDataEntry.setStatus("mandatory")


class _VsrCustomerIdentifier_Type(Unsigned32):
    """Custom type vsrCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_VsrCustomerIdentifier_Type.__name__ = "Unsigned32"
_VsrCustomerIdentifier_Object = MibTableColumn
vsrCustomerIdentifier = _VsrCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 10, 1, 1),
    _VsrCustomerIdentifier_Type()
)
vsrCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrCustomerIdentifier.setStatus("mandatory")
_VsrIfEntryTable_Object = MibTable
vsrIfEntryTable = _VsrIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 11)
)
if mibBuilder.loadTexts:
    vsrIfEntryTable.setStatus("mandatory")
_VsrIfEntryEntry_Object = MibTableRow
vsrIfEntryEntry = _VsrIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 11, 1)
)
vsrIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrIfEntryEntry.setStatus("mandatory")


class _VsrIfAdminStatus_Type(Integer32):
    """Custom type vsrIfAdminStatus based on Integer32"""
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


_VsrIfAdminStatus_Type.__name__ = "Integer32"
_VsrIfAdminStatus_Object = MibTableColumn
vsrIfAdminStatus = _VsrIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 11, 1, 1),
    _VsrIfAdminStatus_Type()
)
vsrIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrIfAdminStatus.setStatus("mandatory")


class _VsrIfIndex_Type(InterfaceIndex):
    """Custom type vsrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsrIfIndex_Type.__name__ = "InterfaceIndex"
_VsrIfIndex_Object = MibTableColumn
vsrIfIndex = _VsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 11, 1, 2),
    _VsrIfIndex_Type()
)
vsrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrIfIndex.setStatus("mandatory")
_VsrProvTable_Object = MibTable
vsrProvTable = _VsrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 12)
)
if mibBuilder.loadTexts:
    vsrProvTable.setStatus("mandatory")
_VsrProvEntry_Object = MibTableRow
vsrProvEntry = _VsrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 12, 1)
)
vsrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrProvEntry.setStatus("mandatory")


class _VsrCommentText_Type(AsciiString):
    """Custom type vsrCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsrCommentText_Type.__name__ = "AsciiString"
_VsrCommentText_Object = MibTableColumn
vsrCommentText = _VsrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 12, 1, 1),
    _VsrCommentText_Type()
)
vsrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrCommentText.setStatus("mandatory")
_VsrVoiceRoute_Type = Link
_VsrVoiceRoute_Object = MibTableColumn
vsrVoiceRoute = _VsrVoiceRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 12, 1, 3),
    _VsrVoiceRoute_Type()
)
vsrVoiceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrVoiceRoute.setStatus("mandatory")
_VsrSignallingChannel_Type = Link
_VsrSignallingChannel_Object = MibTableColumn
vsrSignallingChannel = _VsrSignallingChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 12, 1, 311),
    _VsrSignallingChannel_Type()
)
vsrSignallingChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsrSignallingChannel.setStatus("mandatory")
_VsrStateTable_Object = MibTable
vsrStateTable = _VsrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 13)
)
if mibBuilder.loadTexts:
    vsrStateTable.setStatus("mandatory")
_VsrStateEntry_Object = MibTableRow
vsrStateEntry = _VsrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 13, 1)
)
vsrStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrStateEntry.setStatus("mandatory")


class _VsrAdminState_Type(Integer32):
    """Custom type vsrAdminState based on Integer32"""
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


_VsrAdminState_Type.__name__ = "Integer32"
_VsrAdminState_Object = MibTableColumn
vsrAdminState = _VsrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 13, 1, 1),
    _VsrAdminState_Type()
)
vsrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrAdminState.setStatus("mandatory")


class _VsrOperationalState_Type(Integer32):
    """Custom type vsrOperationalState based on Integer32"""
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


_VsrOperationalState_Type.__name__ = "Integer32"
_VsrOperationalState_Object = MibTableColumn
vsrOperationalState = _VsrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 13, 1, 2),
    _VsrOperationalState_Type()
)
vsrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrOperationalState.setStatus("mandatory")


class _VsrUsageState_Type(Integer32):
    """Custom type vsrUsageState based on Integer32"""
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


_VsrUsageState_Type.__name__ = "Integer32"
_VsrUsageState_Object = MibTableColumn
vsrUsageState = _VsrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 13, 1, 3),
    _VsrUsageState_Type()
)
vsrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrUsageState.setStatus("mandatory")
_VsrOperStatusTable_Object = MibTable
vsrOperStatusTable = _VsrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 14)
)
if mibBuilder.loadTexts:
    vsrOperStatusTable.setStatus("mandatory")
_VsrOperStatusEntry_Object = MibTableRow
vsrOperStatusEntry = _VsrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 14, 1)
)
vsrOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrOperStatusEntry.setStatus("mandatory")


class _VsrSnmpOperStatus_Type(Integer32):
    """Custom type vsrSnmpOperStatus based on Integer32"""
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


_VsrSnmpOperStatus_Type.__name__ = "Integer32"
_VsrSnmpOperStatus_Object = MibTableColumn
vsrSnmpOperStatus = _VsrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 14, 1, 1),
    _VsrSnmpOperStatus_Type()
)
vsrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrSnmpOperStatus.setStatus("mandatory")
_VsrStatsTable_Object = MibTable
vsrStatsTable = _VsrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15)
)
if mibBuilder.loadTexts:
    vsrStatsTable.setStatus("mandatory")
_VsrStatsEntry_Object = MibTableRow
vsrStatsEntry = _VsrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1)
)
vsrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrStatsEntry.setStatus("mandatory")
_VsrTotalCallsFromIf_Type = Counter32
_VsrTotalCallsFromIf_Object = MibTableColumn
vsrTotalCallsFromIf = _VsrTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 1),
    _VsrTotalCallsFromIf_Type()
)
vsrTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrTotalCallsFromIf.setStatus("mandatory")
_VsrTotalFailedCallsFromIf_Type = Counter32
_VsrTotalFailedCallsFromIf_Object = MibTableColumn
vsrTotalFailedCallsFromIf = _VsrTotalFailedCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 2),
    _VsrTotalFailedCallsFromIf_Type()
)
vsrTotalFailedCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrTotalFailedCallsFromIf.setStatus("mandatory")
_VsrInvalidNumberingPlanCalls_Type = Counter32
_VsrInvalidNumberingPlanCalls_Object = MibTableColumn
vsrInvalidNumberingPlanCalls = _VsrInvalidNumberingPlanCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 3),
    _VsrInvalidNumberingPlanCalls_Type()
)
vsrInvalidNumberingPlanCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrInvalidNumberingPlanCalls.setStatus("mandatory")
_VsrAddressResolutionFailedCalls_Type = Counter32
_VsrAddressResolutionFailedCalls_Object = MibTableColumn
vsrAddressResolutionFailedCalls = _VsrAddressResolutionFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 4),
    _VsrAddressResolutionFailedCalls_Type()
)
vsrAddressResolutionFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrAddressResolutionFailedCalls.setStatus("mandatory")
_VsrAddressIncompleteCalls_Type = Counter32
_VsrAddressIncompleteCalls_Object = MibTableColumn
vsrAddressIncompleteCalls = _VsrAddressIncompleteCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 5),
    _VsrAddressIncompleteCalls_Type()
)
vsrAddressIncompleteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrAddressIncompleteCalls.setStatus("mandatory")
_VsrPathAttributesNotMetCalls_Type = Counter32
_VsrPathAttributesNotMetCalls_Object = MibTableColumn
vsrPathAttributesNotMetCalls = _VsrPathAttributesNotMetCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 6),
    _VsrPathAttributesNotMetCalls_Type()
)
vsrPathAttributesNotMetCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPathAttributesNotMetCalls.setStatus("mandatory")
_VsrPathSetupTimeOutCalls_Type = Counter32
_VsrPathSetupTimeOutCalls_Object = MibTableColumn
vsrPathSetupTimeOutCalls = _VsrPathSetupTimeOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 7),
    _VsrPathSetupTimeOutCalls_Type()
)
vsrPathSetupTimeOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPathSetupTimeOutCalls.setStatus("mandatory")
_VsrCallsRejectedLocally_Type = Counter32
_VsrCallsRejectedLocally_Object = MibTableColumn
vsrCallsRejectedLocally = _VsrCallsRejectedLocally_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 8),
    _VsrCallsRejectedLocally_Type()
)
vsrCallsRejectedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrCallsRejectedLocally.setStatus("mandatory")
_VsrCallsRejectedByFarEnd_Type = Counter32
_VsrCallsRejectedByFarEnd_Object = MibTableColumn
vsrCallsRejectedByFarEnd = _VsrCallsRejectedByFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 15, 1, 9),
    _VsrCallsRejectedByFarEnd_Type()
)
vsrCallsRejectedByFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrCallsRejectedByFarEnd.setStatus("mandatory")
_VsrOperTable_Object = MibTable
vsrOperTable = _VsrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16)
)
if mibBuilder.loadTexts:
    vsrOperTable.setStatus("mandatory")
_VsrOperEntry_Object = MibTableRow
vsrOperEntry = _VsrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1)
)
vsrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "vsrIndex"),
)
if mibBuilder.loadTexts:
    vsrOperEntry.setStatus("mandatory")
_VsrActiveChannels_Type = Counter32
_VsrActiveChannels_Object = MibTableColumn
vsrActiveChannels = _VsrActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 2),
    _VsrActiveChannels_Type()
)
vsrActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrActiveChannels.setStatus("mandatory")
_VsrPeakActiveChannels_Type = Counter32
_VsrPeakActiveChannels_Object = MibTableColumn
vsrPeakActiveChannels = _VsrPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 3),
    _VsrPeakActiveChannels_Type()
)
vsrPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPeakActiveChannels.setStatus("mandatory")
_VsrActiveVoiceChannels_Type = Counter32
_VsrActiveVoiceChannels_Object = MibTableColumn
vsrActiveVoiceChannels = _VsrActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 4),
    _VsrActiveVoiceChannels_Type()
)
vsrActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrActiveVoiceChannels.setStatus("mandatory")
_VsrActiveModemChannels_Type = Counter32
_VsrActiveModemChannels_Object = MibTableColumn
vsrActiveModemChannels = _VsrActiveModemChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 5),
    _VsrActiveModemChannels_Type()
)
vsrActiveModemChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrActiveModemChannels.setStatus("mandatory")
_VsrActiveDataChannels_Type = Counter32
_VsrActiveDataChannels_Object = MibTableColumn
vsrActiveDataChannels = _VsrActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 6),
    _VsrActiveDataChannels_Type()
)
vsrActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrActiveDataChannels.setStatus("mandatory")
_VsrPeakActiveVoiceChannels_Type = Counter32
_VsrPeakActiveVoiceChannels_Object = MibTableColumn
vsrPeakActiveVoiceChannels = _VsrPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 7),
    _VsrPeakActiveVoiceChannels_Type()
)
vsrPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPeakActiveVoiceChannels.setStatus("mandatory")
_VsrPeakActiveModemChannels_Type = Counter32
_VsrPeakActiveModemChannels_Object = MibTableColumn
vsrPeakActiveModemChannels = _VsrPeakActiveModemChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 8),
    _VsrPeakActiveModemChannels_Type()
)
vsrPeakActiveModemChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPeakActiveModemChannels.setStatus("mandatory")
_VsrPeakActiveDataChannels_Type = Counter32
_VsrPeakActiveDataChannels_Object = MibTableColumn
vsrPeakActiveDataChannels = _VsrPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 9),
    _VsrPeakActiveDataChannels_Type()
)
vsrPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPeakActiveDataChannels.setStatus("mandatory")


class _VsrActiveFaxRelayChannels_Type(Gauge32):
    """Custom type vsrActiveFaxRelayChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VsrActiveFaxRelayChannels_Type.__name__ = "Gauge32"
_VsrActiveFaxRelayChannels_Object = MibTableColumn
vsrActiveFaxRelayChannels = _VsrActiveFaxRelayChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 10),
    _VsrActiveFaxRelayChannels_Type()
)
vsrActiveFaxRelayChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrActiveFaxRelayChannels.setStatus("mandatory")


class _VsrActiveTptChannels_Type(Gauge32):
    """Custom type vsrActiveTptChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VsrActiveTptChannels_Type.__name__ = "Gauge32"
_VsrActiveTptChannels_Object = MibTableColumn
vsrActiveTptChannels = _VsrActiveTptChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 11),
    _VsrActiveTptChannels_Type()
)
vsrActiveTptChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrActiveTptChannels.setStatus("mandatory")


class _VsrPeakActiveFaxRelayChannels_Type(Gauge32):
    """Custom type vsrPeakActiveFaxRelayChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VsrPeakActiveFaxRelayChannels_Type.__name__ = "Gauge32"
_VsrPeakActiveFaxRelayChannels_Object = MibTableColumn
vsrPeakActiveFaxRelayChannels = _VsrPeakActiveFaxRelayChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 12),
    _VsrPeakActiveFaxRelayChannels_Type()
)
vsrPeakActiveFaxRelayChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPeakActiveFaxRelayChannels.setStatus("mandatory")


class _VsrPeakActiveTptChannels_Type(Gauge32):
    """Custom type vsrPeakActiveTptChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VsrPeakActiveTptChannels_Type.__name__ = "Gauge32"
_VsrPeakActiveTptChannels_Object = MibTableColumn
vsrPeakActiveTptChannels = _VsrPeakActiveTptChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 117, 16, 1, 13),
    _VsrPeakActiveTptChannels_Type()
)
vsrPeakActiveTptChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsrPeakActiveTptChannels.setStatus("mandatory")
_VoiceNetworkingMIB_ObjectIdentity = ObjectIdentity
voiceNetworkingMIB = _VoiceNetworkingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109)
)
_VoiceNetworkingGroup_ObjectIdentity = ObjectIdentity
voiceNetworkingGroup = _VoiceNetworkingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 1)
)
_VoiceNetworkingGroupBE_ObjectIdentity = ObjectIdentity
voiceNetworkingGroupBE = _VoiceNetworkingGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 1, 5)
)
_VoiceNetworkingGroupBE01_ObjectIdentity = ObjectIdentity
voiceNetworkingGroupBE01 = _VoiceNetworkingGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 1, 5, 2)
)
_VoiceNetworkingGroupBE01A_ObjectIdentity = ObjectIdentity
voiceNetworkingGroupBE01A = _VoiceNetworkingGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 1, 5, 2, 2)
)
_VoiceNetworkingCapabilities_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilities = _VoiceNetworkingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 3)
)
_VoiceNetworkingCapabilitiesBE_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilitiesBE = _VoiceNetworkingCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 3, 5)
)
_VoiceNetworkingCapabilitiesBE01_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilitiesBE01 = _VoiceNetworkingCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 3, 5, 2)
)
_VoiceNetworkingCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilitiesBE01A = _VoiceNetworkingCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 109, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VoiceNetworkingMIB",
    **{"sigChan": sigChan,
       "sigChanRowStatusTable": sigChanRowStatusTable,
       "sigChanRowStatusEntry": sigChanRowStatusEntry,
       "sigChanRowStatus": sigChanRowStatus,
       "sigChanComponentName": sigChanComponentName,
       "sigChanStorageType": sigChanStorageType,
       "sigChanIndex": sigChanIndex,
       "sigChanBch": sigChanBch,
       "sigChanBchRowStatusTable": sigChanBchRowStatusTable,
       "sigChanBchRowStatusEntry": sigChanBchRowStatusEntry,
       "sigChanBchRowStatus": sigChanBchRowStatus,
       "sigChanBchComponentName": sigChanBchComponentName,
       "sigChanBchStorageType": sigChanBchStorageType,
       "sigChanBchIndex": sigChanBchIndex,
       "sigChanBchOperTable": sigChanBchOperTable,
       "sigChanBchOperEntry": sigChanBchOperEntry,
       "sigChanBchStatus": sigChanBchStatus,
       "sigChanBchTimeSlot": sigChanBchTimeSlot,
       "sigChanBchVsrInstance": sigChanBchVsrInstance,
       "sigChanBchCalledDirectoryNumber": sigChanBchCalledDirectoryNumber,
       "sigChanGw": sigChanGw,
       "sigChanGwRowStatusTable": sigChanGwRowStatusTable,
       "sigChanGwRowStatusEntry": sigChanGwRowStatusEntry,
       "sigChanGwRowStatus": sigChanGwRowStatus,
       "sigChanGwComponentName": sigChanGwComponentName,
       "sigChanGwStorageType": sigChanGwStorageType,
       "sigChanGwIndex": sigChanGwIndex,
       "sigChanGwStatsTable": sigChanGwStatsTable,
       "sigChanGwStatsEntry": sigChanGwStatsEntry,
       "sigChanGwRequiredConversions": sigChanGwRequiredConversions,
       "sigChanGwUnsupportedConversions": sigChanGwUnsupportedConversions,
       "sigChanGwGwcTable": sigChanGwGwcTable,
       "sigChanGwGwcEntry": sigChanGwGwcEntry,
       "sigChanGwGwcIndex": sigChanGwGwcIndex,
       "sigChanGwGwcValue": sigChanGwGwcValue,
       "sigChanGwGatewayCapTable": sigChanGwGatewayCapTable,
       "sigChanGwGatewayCapEntry": sigChanGwGatewayCapEntry,
       "sigChanGwGatewayCapIndex": sigChanGwGatewayCapIndex,
       "sigChanGwGatewayCapValue": sigChanGwGatewayCapValue,
       "sigChanNcas": sigChanNcas,
       "sigChanNcasRowStatusTable": sigChanNcasRowStatusTable,
       "sigChanNcasRowStatusEntry": sigChanNcasRowStatusEntry,
       "sigChanNcasRowStatus": sigChanNcasRowStatus,
       "sigChanNcasComponentName": sigChanNcasComponentName,
       "sigChanNcasStorageType": sigChanNcasStorageType,
       "sigChanNcasIndex": sigChanNcasIndex,
       "sigChanNcasOperTable": sigChanNcasOperTable,
       "sigChanNcasOperEntry": sigChanNcasOperEntry,
       "sigChanNcasDirection": sigChanNcasDirection,
       "sigChanNcasCallReference": sigChanNcasCallReference,
       "sigChanNcasCalledDirectoryNumber": sigChanNcasCalledDirectoryNumber,
       "sigChanNcasDuration": sigChanNcasDuration,
       "sigChanICmap": sigChanICmap,
       "sigChanICmapRowStatusTable": sigChanICmapRowStatusTable,
       "sigChanICmapRowStatusEntry": sigChanICmapRowStatusEntry,
       "sigChanICmapRowStatus": sigChanICmapRowStatus,
       "sigChanICmapComponentName": sigChanICmapComponentName,
       "sigChanICmapStorageType": sigChanICmapStorageType,
       "sigChanICmapIndex": sigChanICmapIndex,
       "sigChanICmapIntCauseTable": sigChanICmapIntCauseTable,
       "sigChanICmapIntCauseEntry": sigChanICmapIntCauseEntry,
       "sigChanICmapEgressLinkOutOfServCause": sigChanICmapEgressLinkOutOfServCause,
       "sigChanICmapChanOrCircNotAvailCause": sigChanICmapChanOrCircNotAvailCause,
       "sigChanICmapTempFailureCause": sigChanICmapTempFailureCause,
       "sigChanICmapSwitchCongestCause": sigChanICmapSwitchCongestCause,
       "sigChanICmapReqChanOrCircNotAvailCause": sigChanICmapReqChanOrCircNotAvailCause,
       "sigChanICmapResourceUnavailCause": sigChanICmapResourceUnavailCause,
       "sigChanICmapServNotAllowedCause": sigChanICmapServNotAllowedCause,
       "sigChanICmapNoSuchChannelCause": sigChanICmapNoSuchChannelCause,
       "sigChanICmapIncompatDestCause": sigChanICmapIncompatDestCause,
       "sigChanCidDataTable": sigChanCidDataTable,
       "sigChanCidDataEntry": sigChanCidDataEntry,
       "sigChanCustomerIdentifier": sigChanCustomerIdentifier,
       "sigChanIfEntryTable": sigChanIfEntryTable,
       "sigChanIfEntryEntry": sigChanIfEntryEntry,
       "sigChanIfAdminStatus": sigChanIfAdminStatus,
       "sigChanIfIndex": sigChanIfIndex,
       "sigChanOperStatusTable": sigChanOperStatusTable,
       "sigChanOperStatusEntry": sigChanOperStatusEntry,
       "sigChanSnmpOperStatus": sigChanSnmpOperStatus,
       "sigChanStateTable": sigChanStateTable,
       "sigChanStateEntry": sigChanStateEntry,
       "sigChanAdminState": sigChanAdminState,
       "sigChanOperationalState": sigChanOperationalState,
       "sigChanUsageState": sigChanUsageState,
       "sigChanProvTable": sigChanProvTable,
       "sigChanProvEntry": sigChanProvEntry,
       "sigChanCommentText": sigChanCommentText,
       "sigChanOctothorpeEod": sigChanOctothorpeEod,
       "sigChanForceNpiTon": sigChanForceNpiTon,
       "sigChanDefaultNpiTon": sigChanDefaultNpiTon,
       "sigChanSubroutesTable": sigChanSubroutesTable,
       "sigChanSubroutesEntry": sigChanSubroutesEntry,
       "sigChanSubroutesValue": sigChanSubroutesValue,
       "sigChanSubroutesRowStatus": sigChanSubroutesRowStatus,
       "sigChanDegradedSubroutesTable": sigChanDegradedSubroutesTable,
       "sigChanDegradedSubroutesEntry": sigChanDegradedSubroutesEntry,
       "sigChanDegradedSubroutesValue": sigChanDegradedSubroutesValue,
       "vRoute": vRoute,
       "vRouteRowStatusTable": vRouteRowStatusTable,
       "vRouteRowStatusEntry": vRouteRowStatusEntry,
       "vRouteRowStatus": vRouteRowStatus,
       "vRouteComponentName": vRouteComponentName,
       "vRouteStorageType": vRouteStorageType,
       "vRouteIndex": vRouteIndex,
       "vRouteDebug": vRouteDebug,
       "vRouteDebugRowStatusTable": vRouteDebugRowStatusTable,
       "vRouteDebugRowStatusEntry": vRouteDebugRowStatusEntry,
       "vRouteDebugRowStatus": vRouteDebugRowStatus,
       "vRouteDebugComponentName": vRouteDebugComponentName,
       "vRouteDebugStorageType": vRouteDebugStorageType,
       "vRouteDebugIndex": vRouteDebugIndex,
       "vRouteInterface": vRouteInterface,
       "vRouteInterfaceRowStatusTable": vRouteInterfaceRowStatusTable,
       "vRouteInterfaceRowStatusEntry": vRouteInterfaceRowStatusEntry,
       "vRouteInterfaceRowStatus": vRouteInterfaceRowStatus,
       "vRouteInterfaceComponentName": vRouteInterfaceComponentName,
       "vRouteInterfaceStorageType": vRouteInterfaceStorageType,
       "vRouteInterfaceIndex": vRouteInterfaceIndex,
       "vRouteInterfaceProvTable": vRouteInterfaceProvTable,
       "vRouteInterfaceProvEntry": vRouteInterfaceProvEntry,
       "vRouteInterfaceIngressAudioGain": vRouteInterfaceIngressAudioGain,
       "vRouteInterfaceEgressAudioGain": vRouteInterfaceEgressAudioGain,
       "vRouteInterfaceTandemPassThrough": vRouteInterfaceTandemPassThrough,
       "vRouteInterfaceEchoCancellation": vRouteInterfaceEchoCancellation,
       "vRouteInterfaceComfortNoiseCap": vRouteInterfaceComfortNoiseCap,
       "vRouteInterfaceSpeechHangoverTime": vRouteInterfaceSpeechHangoverTime,
       "vRouteInterfaceFaxHangoverTimeG711G726": vRouteInterfaceFaxHangoverTimeG711G726,
       "vRouteInterfaceModemFaxSpeechDiscrim": vRouteInterfaceModemFaxSpeechDiscrim,
       "vRouteInterfaceEchoTailDelay": vRouteInterfaceEchoTailDelay,
       "vRouteInterfaceEchoReturnLoss": vRouteInterfaceEchoReturnLoss,
       "vRouteInterfaceEcanBypassMode": vRouteInterfaceEcanBypassMode,
       "vRouteInterfaceStructuredEchoCancellationTable": vRouteInterfaceStructuredEchoCancellationTable,
       "vRouteInterfaceStructuredEchoCancellationEntry": vRouteInterfaceStructuredEchoCancellationEntry,
       "vRouteInterfaceStructuredEchoCancellationIndex": vRouteInterfaceStructuredEchoCancellationIndex,
       "vRouteInterfaceStructuredEchoCancellationValue": vRouteInterfaceStructuredEchoCancellationValue,
       "vRouteDna": vRouteDna,
       "vRouteDnaRowStatusTable": vRouteDnaRowStatusTable,
       "vRouteDnaRowStatusEntry": vRouteDnaRowStatusEntry,
       "vRouteDnaRowStatus": vRouteDnaRowStatus,
       "vRouteDnaComponentName": vRouteDnaComponentName,
       "vRouteDnaStorageType": vRouteDnaStorageType,
       "vRouteDnaIndex": vRouteDnaIndex,
       "vRouteDnaHgm": vRouteDnaHgm,
       "vRouteDnaHgmRowStatusTable": vRouteDnaHgmRowStatusTable,
       "vRouteDnaHgmRowStatusEntry": vRouteDnaHgmRowStatusEntry,
       "vRouteDnaHgmRowStatus": vRouteDnaHgmRowStatus,
       "vRouteDnaHgmComponentName": vRouteDnaHgmComponentName,
       "vRouteDnaHgmStorageType": vRouteDnaHgmStorageType,
       "vRouteDnaHgmIndex": vRouteDnaHgmIndex,
       "vRouteDnaHgmHgAddr": vRouteDnaHgmHgAddr,
       "vRouteDnaHgmHgAddrRowStatusTable": vRouteDnaHgmHgAddrRowStatusTable,
       "vRouteDnaHgmHgAddrRowStatusEntry": vRouteDnaHgmHgAddrRowStatusEntry,
       "vRouteDnaHgmHgAddrRowStatus": vRouteDnaHgmHgAddrRowStatus,
       "vRouteDnaHgmHgAddrComponentName": vRouteDnaHgmHgAddrComponentName,
       "vRouteDnaHgmHgAddrStorageType": vRouteDnaHgmHgAddrStorageType,
       "vRouteDnaHgmHgAddrIndex": vRouteDnaHgmHgAddrIndex,
       "vRouteDnaHgmHgAddrAddrTable": vRouteDnaHgmHgAddrAddrTable,
       "vRouteDnaHgmHgAddrAddrEntry": vRouteDnaHgmHgAddrAddrEntry,
       "vRouteDnaHgmHgAddrNumberingPlanIndicator": vRouteDnaHgmHgAddrNumberingPlanIndicator,
       "vRouteDnaHgmHgAddrDataNetworkAddress": vRouteDnaHgmHgAddrDataNetworkAddress,
       "vRouteDnaHgmIfTable": vRouteDnaHgmIfTable,
       "vRouteDnaHgmIfEntry": vRouteDnaHgmIfEntry,
       "vRouteDnaHgmUsageDeltaUpdateThreshold": vRouteDnaHgmUsageDeltaUpdateThreshold,
       "vRouteDnaHgmOpTable": vRouteDnaHgmOpTable,
       "vRouteDnaHgmOpEntry": vRouteDnaHgmOpEntry,
       "vRouteDnaHgmMaxAvailableChannels": vRouteDnaHgmMaxAvailableChannels,
       "vRouteDnaHgmAvailableChannels": vRouteDnaHgmAvailableChannels,
       "vRouteDnaHgmAvailabilityDelta": vRouteDnaHgmAvailabilityDelta,
       "vRouteDnaAddressTable": vRouteDnaAddressTable,
       "vRouteDnaAddressEntry": vRouteDnaAddressEntry,
       "vRouteDnaNumberingPlanIndicator": vRouteDnaNumberingPlanIndicator,
       "vRouteDnaDataNetworkAddress": vRouteDnaDataNetworkAddress,
       "vRouteAcct": vRouteAcct,
       "vRouteAcctRowStatusTable": vRouteAcctRowStatusTable,
       "vRouteAcctRowStatusEntry": vRouteAcctRowStatusEntry,
       "vRouteAcctRowStatus": vRouteAcctRowStatus,
       "vRouteAcctComponentName": vRouteAcctComponentName,
       "vRouteAcctStorageType": vRouteAcctStorageType,
       "vRouteAcctIndex": vRouteAcctIndex,
       "vRouteAcctProvTable": vRouteAcctProvTable,
       "vRouteAcctProvEntry": vRouteAcctProvEntry,
       "vRouteAcctAccountCollection": vRouteAcctAccountCollection,
       "vRouteAcctAccountClass": vRouteAcctAccountClass,
       "vRouteAcctServiceExchange": vRouteAcctServiceExchange,
       "vRouteAcctDigitsSuppressed": vRouteAcctDigitsSuppressed,
       "vRouteAcctAccountingOptions": vRouteAcctAccountingOptions,
       "vRouteProvTable": vRouteProvTable,
       "vRouteProvEntry": vRouteProvEntry,
       "vRouteCommentText": vRouteCommentText,
       "vRouteTypeOfRoute": vRouteTypeOfRoute,
       "vRouteDiallingPlan0": vRouteDiallingPlan0,
       "vRouteDiallingPlan1": vRouteDiallingPlan1,
       "vRouteDiallingPlan2": vRouteDiallingPlan2,
       "vRouteHuntingAlgorithm": vRouteHuntingAlgorithm,
       "vRouteMinimumDigitsToRoute": vRouteMinimumDigitsToRoute,
       "vRouteVoiceNetworkingCallServer": vRouteVoiceNetworkingCallServer,
       "vRouteOverrideDirectoryNumber": vRouteOverrideDirectoryNumber,
       "vRoutePrivateNetworkIdentifer": vRoutePrivateNetworkIdentifer,
       "vRouteCidDataTable": vRouteCidDataTable,
       "vRouteCidDataEntry": vRouteCidDataEntry,
       "vRouteCustomerIdentifier": vRouteCustomerIdentifier,
       "vRouteIfEntryTable": vRouteIfEntryTable,
       "vRouteIfEntryEntry": vRouteIfEntryEntry,
       "vRouteIfAdminStatus": vRouteIfAdminStatus,
       "vRouteIfIndex": vRouteIfIndex,
       "vRouteStateTable": vRouteStateTable,
       "vRouteStateEntry": vRouteStateEntry,
       "vRouteAdminState": vRouteAdminState,
       "vRouteOperationalState": vRouteOperationalState,
       "vRouteUsageState": vRouteUsageState,
       "vRouteOperStatusTable": vRouteOperStatusTable,
       "vRouteOperStatusEntry": vRouteOperStatusEntry,
       "vRouteSnmpOperStatus": vRouteSnmpOperStatus,
       "vRouteStatsTable": vRouteStatsTable,
       "vRouteStatsEntry": vRouteStatsEntry,
       "vRouteTotalCallsFromSubnet": vRouteTotalCallsFromSubnet,
       "vRouteCallsClearedNoChannel": vRouteCallsClearedNoChannel,
       "vRouteCallsClearedOutOfService": vRouteCallsClearedOutOfService,
       "vRouteCallsRejected": vRouteCallsRejected,
       "vRouteSubroutesTable": vRouteSubroutesTable,
       "vRouteSubroutesEntry": vRouteSubroutesEntry,
       "vRouteSubroutesValue": vRouteSubroutesValue,
       "vRouteSubroutesRowStatus": vRouteSubroutesRowStatus,
       "vRouteDegradedSubroutesTable": vRouteDegradedSubroutesTable,
       "vRouteDegradedSubroutesEntry": vRouteDegradedSubroutesEntry,
       "vRouteDegradedSubroutesValue": vRouteDegradedSubroutesValue,
       "vsr": vsr,
       "vsrRowStatusTable": vsrRowStatusTable,
       "vsrRowStatusEntry": vsrRowStatusEntry,
       "vsrRowStatus": vsrRowStatus,
       "vsrComponentName": vsrComponentName,
       "vsrStorageType": vsrStorageType,
       "vsrIndex": vsrIndex,
       "vsrSvs": vsrSvs,
       "vsrSvsRowStatusTable": vsrSvsRowStatusTable,
       "vsrSvsRowStatusEntry": vsrSvsRowStatusEntry,
       "vsrSvsRowStatus": vsrSvsRowStatus,
       "vsrSvsComponentName": vsrSvsComponentName,
       "vsrSvsStorageType": vsrSvsStorageType,
       "vsrSvsIndex": vsrSvsIndex,
       "vsrSvsFramer": vsrSvsFramer,
       "vsrSvsFramerRowStatusTable": vsrSvsFramerRowStatusTable,
       "vsrSvsFramerRowStatusEntry": vsrSvsFramerRowStatusEntry,
       "vsrSvsFramerRowStatus": vsrSvsFramerRowStatus,
       "vsrSvsFramerComponentName": vsrSvsFramerComponentName,
       "vsrSvsFramerStorageType": vsrSvsFramerStorageType,
       "vsrSvsFramerIndex": vsrSvsFramerIndex,
       "vsrSvsFramerVfpDebug": vsrSvsFramerVfpDebug,
       "vsrSvsFramerVfpDebugRowStatusTable": vsrSvsFramerVfpDebugRowStatusTable,
       "vsrSvsFramerVfpDebugRowStatusEntry": vsrSvsFramerVfpDebugRowStatusEntry,
       "vsrSvsFramerVfpDebugRowStatus": vsrSvsFramerVfpDebugRowStatus,
       "vsrSvsFramerVfpDebugComponentName": vsrSvsFramerVfpDebugComponentName,
       "vsrSvsFramerVfpDebugStorageType": vsrSvsFramerVfpDebugStorageType,
       "vsrSvsFramerVfpDebugIndex": vsrSvsFramerVfpDebugIndex,
       "vsrSvsFramerMvpDebug": vsrSvsFramerMvpDebug,
       "vsrSvsFramerMvpDebugRowStatusTable": vsrSvsFramerMvpDebugRowStatusTable,
       "vsrSvsFramerMvpDebugRowStatusEntry": vsrSvsFramerMvpDebugRowStatusEntry,
       "vsrSvsFramerMvpDebugRowStatus": vsrSvsFramerMvpDebugRowStatus,
       "vsrSvsFramerMvpDebugComponentName": vsrSvsFramerMvpDebugComponentName,
       "vsrSvsFramerMvpDebugStorageType": vsrSvsFramerMvpDebugStorageType,
       "vsrSvsFramerMvpDebugIndex": vsrSvsFramerMvpDebugIndex,
       "vsrSvsFramerPcmCapture": vsrSvsFramerPcmCapture,
       "vsrSvsFramerPcmCaptureRowStatusTable": vsrSvsFramerPcmCaptureRowStatusTable,
       "vsrSvsFramerPcmCaptureRowStatusEntry": vsrSvsFramerPcmCaptureRowStatusEntry,
       "vsrSvsFramerPcmCaptureRowStatus": vsrSvsFramerPcmCaptureRowStatus,
       "vsrSvsFramerPcmCaptureComponentName": vsrSvsFramerPcmCaptureComponentName,
       "vsrSvsFramerPcmCaptureStorageType": vsrSvsFramerPcmCaptureStorageType,
       "vsrSvsFramerPcmCaptureIndex": vsrSvsFramerPcmCaptureIndex,
       "vsrSvsFramerProvTable": vsrSvsFramerProvTable,
       "vsrSvsFramerProvEntry": vsrSvsFramerProvEntry,
       "vsrSvsFramerInterfaceName": vsrSvsFramerInterfaceName,
       "vsrSvsFramerStateTable": vsrSvsFramerStateTable,
       "vsrSvsFramerStateEntry": vsrSvsFramerStateEntry,
       "vsrSvsFramerAdminState": vsrSvsFramerAdminState,
       "vsrSvsFramerOperationalState": vsrSvsFramerOperationalState,
       "vsrSvsFramerUsageState": vsrSvsFramerUsageState,
       "vsrSvsFramerStatsTable": vsrSvsFramerStatsTable,
       "vsrSvsFramerStatsEntry": vsrSvsFramerStatsEntry,
       "vsrSvsFramerTotalCells": vsrSvsFramerTotalCells,
       "vsrSvsFramerAudioCells": vsrSvsFramerAudioCells,
       "vsrSvsFramerSilenceCells": vsrSvsFramerSilenceCells,
       "vsrSvsFramerModemCells": vsrSvsFramerModemCells,
       "vsrSvsFramerCurrentEncodingRate": vsrSvsFramerCurrentEncodingRate,
       "vsrSvsFramerLrcErrors": vsrSvsFramerLrcErrors,
       "vsrSvsFramerFrmLostInNetwork": vsrSvsFramerFrmLostInNetwork,
       "vsrSvsFramerFrmUnderRuns": vsrSvsFramerFrmUnderRuns,
       "vsrSvsFramerFrmDumped": vsrSvsFramerFrmDumped,
       "vsrSvsFramerModemSilenceCells": vsrSvsFramerModemSilenceCells,
       "vsrSvsFramerCurrentEncoding": vsrSvsFramerCurrentEncoding,
       "vsrSvsFramerTptStatus": vsrSvsFramerTptStatus,
       "vsrSvsFramerFaxRelayCells": vsrSvsFramerFaxRelayCells,
       "vsrSvsFramerModemFaxCells": vsrSvsFramerModemFaxCells,
       "vsrSvsFramerFaxIdleCells": vsrSvsFramerFaxIdleCells,
       "vsrSvsFramerOperTable": vsrSvsFramerOperTable,
       "vsrSvsFramerOperEntry": vsrSvsFramerOperEntry,
       "vsrSvsFramerOpCurrentEncoding": vsrSvsFramerOpCurrentEncoding,
       "vsrSvsFramerCurrentRate": vsrSvsFramerCurrentRate,
       "vsrSvsFramerOpTptStatus": vsrSvsFramerOpTptStatus,
       "vsrSvsFramerNegTable": vsrSvsFramerNegTable,
       "vsrSvsFramerNegEntry": vsrSvsFramerNegEntry,
       "vsrSvsFramerNegotiatedSilenceSuppression": vsrSvsFramerNegotiatedSilenceSuppression,
       "vsrSvsFramerNegotiatedFisG711G726": vsrSvsFramerNegotiatedFisG711G726,
       "vsrSvsFramerNegotiatedDtmfRegeneration": vsrSvsFramerNegotiatedDtmfRegeneration,
       "vsrSvsFramerNegotiatedV17AsG711G726": vsrSvsFramerNegotiatedV17AsG711G726,
       "vsrSvsFramerNegotiatedTandemPassThrough": vsrSvsFramerNegotiatedTandemPassThrough,
       "vsrSvsFramerFrmToNetworkTable": vsrSvsFramerFrmToNetworkTable,
       "vsrSvsFramerFrmToNetworkEntry": vsrSvsFramerFrmToNetworkEntry,
       "vsrSvsFramerFrmToNetworkIndex": vsrSvsFramerFrmToNetworkIndex,
       "vsrSvsFramerFrmToNetworkValue": vsrSvsFramerFrmToNetworkValue,
       "vsrSvsFramerFrmFromNetworkTable": vsrSvsFramerFrmFromNetworkTable,
       "vsrSvsFramerFrmFromNetworkEntry": vsrSvsFramerFrmFromNetworkEntry,
       "vsrSvsFramerFrmFromNetworkIndex": vsrSvsFramerFrmFromNetworkIndex,
       "vsrSvsFramerFrmFromNetworkValue": vsrSvsFramerFrmFromNetworkValue,
       "vsrSvsFramerNEncodingTable": vsrSvsFramerNEncodingTable,
       "vsrSvsFramerNEncodingEntry": vsrSvsFramerNEncodingEntry,
       "vsrSvsFramerNEncodingIndex": vsrSvsFramerNEncodingIndex,
       "vsrSvsFramerNEncodingValue": vsrSvsFramerNEncodingValue,
       "vsrSvsFramerNRatesTable": vsrSvsFramerNRatesTable,
       "vsrSvsFramerNRatesEntry": vsrSvsFramerNRatesEntry,
       "vsrSvsFramerNRatesTrafficIndex": vsrSvsFramerNRatesTrafficIndex,
       "vsrSvsFramerNRatesRateIndex": vsrSvsFramerNRatesRateIndex,
       "vsrSvsFramerNRatesValue": vsrSvsFramerNRatesValue,
       "vsrSvsLCo": vsrSvsLCo,
       "vsrSvsLCoRowStatusTable": vsrSvsLCoRowStatusTable,
       "vsrSvsLCoRowStatusEntry": vsrSvsLCoRowStatusEntry,
       "vsrSvsLCoRowStatus": vsrSvsLCoRowStatus,
       "vsrSvsLCoComponentName": vsrSvsLCoComponentName,
       "vsrSvsLCoStorageType": vsrSvsLCoStorageType,
       "vsrSvsLCoIndex": vsrSvsLCoIndex,
       "vsrSvsLCoPathDataTable": vsrSvsLCoPathDataTable,
       "vsrSvsLCoPathDataEntry": vsrSvsLCoPathDataEntry,
       "vsrSvsLCoState": vsrSvsLCoState,
       "vsrSvsLCoOverrideRemoteName": vsrSvsLCoOverrideRemoteName,
       "vsrSvsLCoEnd": vsrSvsLCoEnd,
       "vsrSvsLCoCostMetric": vsrSvsLCoCostMetric,
       "vsrSvsLCoDelayMetric": vsrSvsLCoDelayMetric,
       "vsrSvsLCoRoundTripDelay": vsrSvsLCoRoundTripDelay,
       "vsrSvsLCoSetupPriority": vsrSvsLCoSetupPriority,
       "vsrSvsLCoHoldingPriority": vsrSvsLCoHoldingPriority,
       "vsrSvsLCoRequiredTxBandwidth": vsrSvsLCoRequiredTxBandwidth,
       "vsrSvsLCoRequiredRxBandwidth": vsrSvsLCoRequiredRxBandwidth,
       "vsrSvsLCoRequiredTrafficType": vsrSvsLCoRequiredTrafficType,
       "vsrSvsLCoPermittedTrunkTypes": vsrSvsLCoPermittedTrunkTypes,
       "vsrSvsLCoRequiredSecurity": vsrSvsLCoRequiredSecurity,
       "vsrSvsLCoRequiredCustomerParameter": vsrSvsLCoRequiredCustomerParameter,
       "vsrSvsLCoEmissionPriority": vsrSvsLCoEmissionPriority,
       "vsrSvsLCoDiscardPriority": vsrSvsLCoDiscardPriority,
       "vsrSvsLCoPathType": vsrSvsLCoPathType,
       "vsrSvsLCoRetryCount": vsrSvsLCoRetryCount,
       "vsrSvsLCoPathFailureCount": vsrSvsLCoPathFailureCount,
       "vsrSvsLCoReasonForNoRoute": vsrSvsLCoReasonForNoRoute,
       "vsrSvsLCoLastTearDownReason": vsrSvsLCoLastTearDownReason,
       "vsrSvsLCoPathFailureAction": vsrSvsLCoPathFailureAction,
       "vsrSvsLCoBumpPreference": vsrSvsLCoBumpPreference,
       "vsrSvsLCoOptimization": vsrSvsLCoOptimization,
       "vsrSvsLCoPathUpDateTime": vsrSvsLCoPathUpDateTime,
       "vsrSvsLCoStatsTable": vsrSvsLCoStatsTable,
       "vsrSvsLCoStatsEntry": vsrSvsLCoStatsEntry,
       "vsrSvsLCoPktsToNetwork": vsrSvsLCoPktsToNetwork,
       "vsrSvsLCoBytesToNetwork": vsrSvsLCoBytesToNetwork,
       "vsrSvsLCoPktsFromNetwork": vsrSvsLCoPktsFromNetwork,
       "vsrSvsLCoBytesFromNetwork": vsrSvsLCoBytesFromNetwork,
       "vsrSvsLCoPathTable": vsrSvsLCoPathTable,
       "vsrSvsLCoPathEntry": vsrSvsLCoPathEntry,
       "vsrSvsLCoPathValue": vsrSvsLCoPathValue,
       "vsrSvsDebug": vsrSvsDebug,
       "vsrSvsDebugRowStatusTable": vsrSvsDebugRowStatusTable,
       "vsrSvsDebugRowStatusEntry": vsrSvsDebugRowStatusEntry,
       "vsrSvsDebugRowStatus": vsrSvsDebugRowStatus,
       "vsrSvsDebugComponentName": vsrSvsDebugComponentName,
       "vsrSvsDebugStorageType": vsrSvsDebugStorageType,
       "vsrSvsDebugIndex": vsrSvsDebugIndex,
       "vsrSvsIfEntryTable": vsrSvsIfEntryTable,
       "vsrSvsIfEntryEntry": vsrSvsIfEntryEntry,
       "vsrSvsIfAdminStatus": vsrSvsIfAdminStatus,
       "vsrSvsIfIndex": vsrSvsIfIndex,
       "vsrSvsOperTable": vsrSvsOperTable,
       "vsrSvsOperEntry": vsrSvsOperEntry,
       "vsrSvsStatus": vsrSvsStatus,
       "vsrSvsProfileNumber": vsrSvsProfileNumber,
       "vsrSvsCallType": vsrSvsCallType,
       "vsrSvsCalledNumber": vsrSvsCalledNumber,
       "vsrSvsCallingNumber": vsrSvsCallingNumber,
       "vsrSvsClearCauseCode": vsrSvsClearCauseCode,
       "vsrSvsStatsTable": vsrSvsStatsTable,
       "vsrSvsStatsEntry": vsrSvsStatsEntry,
       "vsrSvsTotalCalls": vsrSvsTotalCalls,
       "vsrSvsTotalCallSeconds": vsrSvsTotalCallSeconds,
       "vsrSvsStateTable": vsrSvsStateTable,
       "vsrSvsStateEntry": vsrSvsStateEntry,
       "vsrSvsAdminState": vsrSvsAdminState,
       "vsrSvsOperationalState": vsrSvsOperationalState,
       "vsrSvsUsageState": vsrSvsUsageState,
       "vsrSvsOperStatusTable": vsrSvsOperStatusTable,
       "vsrSvsOperStatusEntry": vsrSvsOperStatusEntry,
       "vsrSvsSnmpOperStatus": vsrSvsSnmpOperStatus,
       "vsrDebug": vsrDebug,
       "vsrDebugRowStatusTable": vsrDebugRowStatusTable,
       "vsrDebugRowStatusEntry": vsrDebugRowStatusEntry,
       "vsrDebugRowStatus": vsrDebugRowStatus,
       "vsrDebugComponentName": vsrDebugComponentName,
       "vsrDebugStorageType": vsrDebugStorageType,
       "vsrDebugIndex": vsrDebugIndex,
       "vsrCidDataTable": vsrCidDataTable,
       "vsrCidDataEntry": vsrCidDataEntry,
       "vsrCustomerIdentifier": vsrCustomerIdentifier,
       "vsrIfEntryTable": vsrIfEntryTable,
       "vsrIfEntryEntry": vsrIfEntryEntry,
       "vsrIfAdminStatus": vsrIfAdminStatus,
       "vsrIfIndex": vsrIfIndex,
       "vsrProvTable": vsrProvTable,
       "vsrProvEntry": vsrProvEntry,
       "vsrCommentText": vsrCommentText,
       "vsrVoiceRoute": vsrVoiceRoute,
       "vsrSignallingChannel": vsrSignallingChannel,
       "vsrStateTable": vsrStateTable,
       "vsrStateEntry": vsrStateEntry,
       "vsrAdminState": vsrAdminState,
       "vsrOperationalState": vsrOperationalState,
       "vsrUsageState": vsrUsageState,
       "vsrOperStatusTable": vsrOperStatusTable,
       "vsrOperStatusEntry": vsrOperStatusEntry,
       "vsrSnmpOperStatus": vsrSnmpOperStatus,
       "vsrStatsTable": vsrStatsTable,
       "vsrStatsEntry": vsrStatsEntry,
       "vsrTotalCallsFromIf": vsrTotalCallsFromIf,
       "vsrTotalFailedCallsFromIf": vsrTotalFailedCallsFromIf,
       "vsrInvalidNumberingPlanCalls": vsrInvalidNumberingPlanCalls,
       "vsrAddressResolutionFailedCalls": vsrAddressResolutionFailedCalls,
       "vsrAddressIncompleteCalls": vsrAddressIncompleteCalls,
       "vsrPathAttributesNotMetCalls": vsrPathAttributesNotMetCalls,
       "vsrPathSetupTimeOutCalls": vsrPathSetupTimeOutCalls,
       "vsrCallsRejectedLocally": vsrCallsRejectedLocally,
       "vsrCallsRejectedByFarEnd": vsrCallsRejectedByFarEnd,
       "vsrOperTable": vsrOperTable,
       "vsrOperEntry": vsrOperEntry,
       "vsrActiveChannels": vsrActiveChannels,
       "vsrPeakActiveChannels": vsrPeakActiveChannels,
       "vsrActiveVoiceChannels": vsrActiveVoiceChannels,
       "vsrActiveModemChannels": vsrActiveModemChannels,
       "vsrActiveDataChannels": vsrActiveDataChannels,
       "vsrPeakActiveVoiceChannels": vsrPeakActiveVoiceChannels,
       "vsrPeakActiveModemChannels": vsrPeakActiveModemChannels,
       "vsrPeakActiveDataChannels": vsrPeakActiveDataChannels,
       "vsrActiveFaxRelayChannels": vsrActiveFaxRelayChannels,
       "vsrActiveTptChannels": vsrActiveTptChannels,
       "vsrPeakActiveFaxRelayChannels": vsrPeakActiveFaxRelayChannels,
       "vsrPeakActiveTptChannels": vsrPeakActiveTptChannels,
       "voiceNetworkingMIB": voiceNetworkingMIB,
       "voiceNetworkingGroup": voiceNetworkingGroup,
       "voiceNetworkingGroupBE": voiceNetworkingGroupBE,
       "voiceNetworkingGroupBE01": voiceNetworkingGroupBE01,
       "voiceNetworkingGroupBE01A": voiceNetworkingGroupBE01A,
       "voiceNetworkingCapabilities": voiceNetworkingCapabilities,
       "voiceNetworkingCapabilitiesBE": voiceNetworkingCapabilitiesBE,
       "voiceNetworkingCapabilitiesBE01": voiceNetworkingCapabilitiesBE01,
       "voiceNetworkingCapabilitiesBE01A": voiceNetworkingCapabilitiesBE01A}
)
