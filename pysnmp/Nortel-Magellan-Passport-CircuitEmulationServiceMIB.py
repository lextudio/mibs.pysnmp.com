# SNMP MIB module (Nortel-Magellan-Passport-CircuitEmulationServiceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-CircuitEmulationServiceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:31 2024
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
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
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

_Aal1Ces_ObjectIdentity = ObjectIdentity
aal1Ces = _Aal1Ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119)
)
_Aal1CesRowStatusTable_Object = MibTable
aal1CesRowStatusTable = _Aal1CesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 1)
)
if mibBuilder.loadTexts:
    aal1CesRowStatusTable.setStatus("mandatory")
_Aal1CesRowStatusEntry_Object = MibTableRow
aal1CesRowStatusEntry = _Aal1CesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 1, 1)
)
aal1CesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
)
if mibBuilder.loadTexts:
    aal1CesRowStatusEntry.setStatus("mandatory")
_Aal1CesRowStatus_Type = RowStatus
_Aal1CesRowStatus_Object = MibTableColumn
aal1CesRowStatus = _Aal1CesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 1, 1, 1),
    _Aal1CesRowStatus_Type()
)
aal1CesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesRowStatus.setStatus("mandatory")
_Aal1CesComponentName_Type = DisplayString
_Aal1CesComponentName_Object = MibTableColumn
aal1CesComponentName = _Aal1CesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 1, 1, 2),
    _Aal1CesComponentName_Type()
)
aal1CesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesComponentName.setStatus("mandatory")
_Aal1CesStorageType_Type = StorageType
_Aal1CesStorageType_Object = MibTableColumn
aal1CesStorageType = _Aal1CesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 1, 1, 4),
    _Aal1CesStorageType_Type()
)
aal1CesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesStorageType.setStatus("mandatory")


class _Aal1CesIndex_Type(Integer32):
    """Custom type aal1CesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_Aal1CesIndex_Type.__name__ = "Integer32"
_Aal1CesIndex_Object = MibTableColumn
aal1CesIndex = _Aal1CesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 1, 1, 10),
    _Aal1CesIndex_Type()
)
aal1CesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal1CesIndex.setStatus("mandatory")
_Aal1CesNap_ObjectIdentity = ObjectIdentity
aal1CesNap = _Aal1CesNap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2)
)
_Aal1CesNapRowStatusTable_Object = MibTable
aal1CesNapRowStatusTable = _Aal1CesNapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 1)
)
if mibBuilder.loadTexts:
    aal1CesNapRowStatusTable.setStatus("mandatory")
_Aal1CesNapRowStatusEntry_Object = MibTableRow
aal1CesNapRowStatusEntry = _Aal1CesNapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 1, 1)
)
aal1CesNapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesNapIndex"),
)
if mibBuilder.loadTexts:
    aal1CesNapRowStatusEntry.setStatus("mandatory")
_Aal1CesNapRowStatus_Type = RowStatus
_Aal1CesNapRowStatus_Object = MibTableColumn
aal1CesNapRowStatus = _Aal1CesNapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 1, 1, 1),
    _Aal1CesNapRowStatus_Type()
)
aal1CesNapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesNapRowStatus.setStatus("mandatory")
_Aal1CesNapComponentName_Type = DisplayString
_Aal1CesNapComponentName_Object = MibTableColumn
aal1CesNapComponentName = _Aal1CesNapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 1, 1, 2),
    _Aal1CesNapComponentName_Type()
)
aal1CesNapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesNapComponentName.setStatus("mandatory")
_Aal1CesNapStorageType_Type = StorageType
_Aal1CesNapStorageType_Object = MibTableColumn
aal1CesNapStorageType = _Aal1CesNapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 1, 1, 4),
    _Aal1CesNapStorageType_Type()
)
aal1CesNapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesNapStorageType.setStatus("mandatory")
_Aal1CesNapIndex_Type = NonReplicated
_Aal1CesNapIndex_Object = MibTableColumn
aal1CesNapIndex = _Aal1CesNapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 1, 1, 10),
    _Aal1CesNapIndex_Type()
)
aal1CesNapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal1CesNapIndex.setStatus("mandatory")
_Aal1CesNapProvTable_Object = MibTable
aal1CesNapProvTable = _Aal1CesNapProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 10)
)
if mibBuilder.loadTexts:
    aal1CesNapProvTable.setStatus("mandatory")
_Aal1CesNapProvEntry_Object = MibTableRow
aal1CesNapProvEntry = _Aal1CesNapProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 10, 1)
)
aal1CesNapProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesNapIndex"),
)
if mibBuilder.loadTexts:
    aal1CesNapProvEntry.setStatus("mandatory")
_Aal1CesNapAtmConnection_Type = Link
_Aal1CesNapAtmConnection_Object = MibTableColumn
aal1CesNapAtmConnection = _Aal1CesNapAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 2, 10, 1, 1),
    _Aal1CesNapAtmConnection_Type()
)
aal1CesNapAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesNapAtmConnection.setStatus("mandatory")
_Aal1CesAep_ObjectIdentity = ObjectIdentity
aal1CesAep = _Aal1CesAep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3)
)
_Aal1CesAepRowStatusTable_Object = MibTable
aal1CesAepRowStatusTable = _Aal1CesAepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 1)
)
if mibBuilder.loadTexts:
    aal1CesAepRowStatusTable.setStatus("mandatory")
_Aal1CesAepRowStatusEntry_Object = MibTableRow
aal1CesAepRowStatusEntry = _Aal1CesAepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 1, 1)
)
aal1CesAepRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesAepRowStatusEntry.setStatus("mandatory")
_Aal1CesAepRowStatus_Type = RowStatus
_Aal1CesAepRowStatus_Object = MibTableColumn
aal1CesAepRowStatus = _Aal1CesAepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 1, 1, 1),
    _Aal1CesAepRowStatus_Type()
)
aal1CesAepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepRowStatus.setStatus("mandatory")
_Aal1CesAepComponentName_Type = DisplayString
_Aal1CesAepComponentName_Object = MibTableColumn
aal1CesAepComponentName = _Aal1CesAepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 1, 1, 2),
    _Aal1CesAepComponentName_Type()
)
aal1CesAepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepComponentName.setStatus("mandatory")
_Aal1CesAepStorageType_Type = StorageType
_Aal1CesAepStorageType_Object = MibTableColumn
aal1CesAepStorageType = _Aal1CesAepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 1, 1, 4),
    _Aal1CesAepStorageType_Type()
)
aal1CesAepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepStorageType.setStatus("mandatory")
_Aal1CesAepIndex_Type = NonReplicated
_Aal1CesAepIndex_Object = MibTableColumn
aal1CesAepIndex = _Aal1CesAepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 1, 1, 10),
    _Aal1CesAepIndex_Type()
)
aal1CesAepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal1CesAepIndex.setStatus("mandatory")
_Aal1CesAepProvEndPointAddrTable_Object = MibTable
aal1CesAepProvEndPointAddrTable = _Aal1CesAepProvEndPointAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 10)
)
if mibBuilder.loadTexts:
    aal1CesAepProvEndPointAddrTable.setStatus("mandatory")
_Aal1CesAepProvEndPointAddrEntry_Object = MibTableRow
aal1CesAepProvEndPointAddrEntry = _Aal1CesAepProvEndPointAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 10, 1)
)
aal1CesAepProvEndPointAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesAepProvEndPointAddrEntry.setStatus("mandatory")


class _Aal1CesAepExpectedRemoteAddress_Type(AsciiString):
    """Custom type aal1CesAepExpectedRemoteAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aal1CesAepExpectedRemoteAddress_Type.__name__ = "AsciiString"
_Aal1CesAepExpectedRemoteAddress_Object = MibTableColumn
aal1CesAepExpectedRemoteAddress = _Aal1CesAepExpectedRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 10, 1, 1),
    _Aal1CesAepExpectedRemoteAddress_Type()
)
aal1CesAepExpectedRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepExpectedRemoteAddress.setStatus("mandatory")


class _Aal1CesAepLocalAddress_Type(AsciiString):
    """Custom type aal1CesAepLocalAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_Aal1CesAepLocalAddress_Type.__name__ = "AsciiString"
_Aal1CesAepLocalAddress_Object = MibTableColumn
aal1CesAepLocalAddress = _Aal1CesAepLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 10, 1, 2),
    _Aal1CesAepLocalAddress_Type()
)
aal1CesAepLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepLocalAddress.setStatus("mandatory")
_Aal1CesAepProvTable_Object = MibTable
aal1CesAepProvTable = _Aal1CesAepProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11)
)
if mibBuilder.loadTexts:
    aal1CesAepProvTable.setStatus("mandatory")
_Aal1CesAepProvEntry_Object = MibTableRow
aal1CesAepProvEntry = _Aal1CesAepProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11, 1)
)
aal1CesAepProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesAepProvEntry.setStatus("mandatory")


class _Aal1CesAepAddressToCall_Type(AsciiString):
    """Custom type aal1CesAepAddressToCall based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_Aal1CesAepAddressToCall_Type.__name__ = "AsciiString"
_Aal1CesAepAddressToCall_Object = MibTableColumn
aal1CesAepAddressToCall = _Aal1CesAepAddressToCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11, 1, 1),
    _Aal1CesAepAddressToCall_Type()
)
aal1CesAepAddressToCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepAddressToCall.setStatus("mandatory")


class _Aal1CesAepRoutingOption_Type(Integer32):
    """Custom type aal1CesAepRoutingOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("porsOnly", 0)
    )


_Aal1CesAepRoutingOption_Type.__name__ = "Integer32"
_Aal1CesAepRoutingOption_Object = MibTableColumn
aal1CesAepRoutingOption = _Aal1CesAepRoutingOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11, 1, 2),
    _Aal1CesAepRoutingOption_Type()
)
aal1CesAepRoutingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepRoutingOption.setStatus("mandatory")
_Aal1CesAepProfile_Type = Link
_Aal1CesAepProfile_Object = MibTableColumn
aal1CesAepProfile = _Aal1CesAepProfile_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11, 1, 3),
    _Aal1CesAepProfile_Type()
)
aal1CesAepProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepProfile.setStatus("mandatory")


class _Aal1CesAepFirstRetryInterval_Type(Unsigned32):
    """Custom type aal1CesAepFirstRetryInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Aal1CesAepFirstRetryInterval_Type.__name__ = "Unsigned32"
_Aal1CesAepFirstRetryInterval_Object = MibTableColumn
aal1CesAepFirstRetryInterval = _Aal1CesAepFirstRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11, 1, 4),
    _Aal1CesAepFirstRetryInterval_Type()
)
aal1CesAepFirstRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepFirstRetryInterval.setStatus("mandatory")


class _Aal1CesAepRetryLimit_Type(Unsigned32):
    """Custom type aal1CesAepRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aal1CesAepRetryLimit_Type.__name__ = "Unsigned32"
_Aal1CesAepRetryLimit_Object = MibTableColumn
aal1CesAepRetryLimit = _Aal1CesAepRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 11, 1, 5),
    _Aal1CesAepRetryLimit_Type()
)
aal1CesAepRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesAepRetryLimit.setStatus("mandatory")
_Aal1CesAepEpOperTable_Object = MibTable
aal1CesAepEpOperTable = _Aal1CesAepEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 12)
)
if mibBuilder.loadTexts:
    aal1CesAepEpOperTable.setStatus("mandatory")
_Aal1CesAepEpOperEntry_Object = MibTableRow
aal1CesAepEpOperEntry = _Aal1CesAepEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 12, 1)
)
aal1CesAepEpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesAepEpOperEntry.setStatus("mandatory")


class _Aal1CesAepRemoteAddress_Type(AsciiString):
    """Custom type aal1CesAepRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_Aal1CesAepRemoteAddress_Type.__name__ = "AsciiString"
_Aal1CesAepRemoteAddress_Object = MibTableColumn
aal1CesAepRemoteAddress = _Aal1CesAepRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 12, 1, 1),
    _Aal1CesAepRemoteAddress_Type()
)
aal1CesAepRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepRemoteAddress.setStatus("mandatory")


class _Aal1CesAepLastTearDownCause_Type(Unsigned32):
    """Custom type aal1CesAepLastTearDownCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal1CesAepLastTearDownCause_Type.__name__ = "Unsigned32"
_Aal1CesAepLastTearDownCause_Object = MibTableColumn
aal1CesAepLastTearDownCause = _Aal1CesAepLastTearDownCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 12, 1, 2),
    _Aal1CesAepLastTearDownCause_Type()
)
aal1CesAepLastTearDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepLastTearDownCause.setStatus("mandatory")


class _Aal1CesAepLastTearDownDiagnostic_Type(AsciiString):
    """Custom type aal1CesAepLastTearDownDiagnostic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Aal1CesAepLastTearDownDiagnostic_Type.__name__ = "AsciiString"
_Aal1CesAepLastTearDownDiagnostic_Object = MibTableColumn
aal1CesAepLastTearDownDiagnostic = _Aal1CesAepLastTearDownDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 12, 1, 3),
    _Aal1CesAepLastTearDownDiagnostic_Type()
)
aal1CesAepLastTearDownDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepLastTearDownDiagnostic.setStatus("mandatory")
_Aal1CesAepOutTable_Object = MibTable
aal1CesAepOutTable = _Aal1CesAepOutTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13)
)
if mibBuilder.loadTexts:
    aal1CesAepOutTable.setStatus("mandatory")
_Aal1CesAepOutEntry_Object = MibTableRow
aal1CesAepOutEntry = _Aal1CesAepOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13, 1)
)
aal1CesAepOutEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesAepOutEntry.setStatus("mandatory")


class _Aal1CesAepSvcStatus_Type(Integer32):
    """Custom type aal1CesAepSvcStatus based on Integer32"""
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
        *(("connected", 2),
          ("connecting", 1),
          ("failed", 5),
          ("idle", 3),
          ("initialising", 0),
          ("retriesExhausted", 4))
    )


_Aal1CesAepSvcStatus_Type.__name__ = "Integer32"
_Aal1CesAepSvcStatus_Object = MibTableColumn
aal1CesAepSvcStatus = _Aal1CesAepSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13, 1, 1),
    _Aal1CesAepSvcStatus_Type()
)
aal1CesAepSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepSvcStatus.setStatus("mandatory")


class _Aal1CesAepLastSetupFailureCause_Type(Unsigned32):
    """Custom type aal1CesAepLastSetupFailureCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal1CesAepLastSetupFailureCause_Type.__name__ = "Unsigned32"
_Aal1CesAepLastSetupFailureCause_Object = MibTableColumn
aal1CesAepLastSetupFailureCause = _Aal1CesAepLastSetupFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13, 1, 2),
    _Aal1CesAepLastSetupFailureCause_Type()
)
aal1CesAepLastSetupFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepLastSetupFailureCause.setStatus("mandatory")


class _Aal1CesAepLastSetupFailureDiagnostic_Type(AsciiString):
    """Custom type aal1CesAepLastSetupFailureDiagnostic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Aal1CesAepLastSetupFailureDiagnostic_Type.__name__ = "AsciiString"
_Aal1CesAepLastSetupFailureDiagnostic_Object = MibTableColumn
aal1CesAepLastSetupFailureDiagnostic = _Aal1CesAepLastSetupFailureDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13, 1, 3),
    _Aal1CesAepLastSetupFailureDiagnostic_Type()
)
aal1CesAepLastSetupFailureDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepLastSetupFailureDiagnostic.setStatus("mandatory")
_Aal1CesAepRetryTimeRemaining_Type = Counter32
_Aal1CesAepRetryTimeRemaining_Object = MibTableColumn
aal1CesAepRetryTimeRemaining = _Aal1CesAepRetryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13, 1, 4),
    _Aal1CesAepRetryTimeRemaining_Type()
)
aal1CesAepRetryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepRetryTimeRemaining.setStatus("mandatory")
_Aal1CesAepRetryFailures_Type = Counter32
_Aal1CesAepRetryFailures_Object = MibTableColumn
aal1CesAepRetryFailures = _Aal1CesAepRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 3, 13, 1, 5),
    _Aal1CesAepRetryFailures_Type()
)
aal1CesAepRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAepRetryFailures.setStatus("mandatory")
_Aal1CesPep_ObjectIdentity = ObjectIdentity
aal1CesPep = _Aal1CesPep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4)
)
_Aal1CesPepRowStatusTable_Object = MibTable
aal1CesPepRowStatusTable = _Aal1CesPepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 1)
)
if mibBuilder.loadTexts:
    aal1CesPepRowStatusTable.setStatus("mandatory")
_Aal1CesPepRowStatusEntry_Object = MibTableRow
aal1CesPepRowStatusEntry = _Aal1CesPepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 1, 1)
)
aal1CesPepRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesPepRowStatusEntry.setStatus("mandatory")
_Aal1CesPepRowStatus_Type = RowStatus
_Aal1CesPepRowStatus_Object = MibTableColumn
aal1CesPepRowStatus = _Aal1CesPepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 1, 1, 1),
    _Aal1CesPepRowStatus_Type()
)
aal1CesPepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesPepRowStatus.setStatus("mandatory")
_Aal1CesPepComponentName_Type = DisplayString
_Aal1CesPepComponentName_Object = MibTableColumn
aal1CesPepComponentName = _Aal1CesPepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 1, 1, 2),
    _Aal1CesPepComponentName_Type()
)
aal1CesPepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPepComponentName.setStatus("mandatory")
_Aal1CesPepStorageType_Type = StorageType
_Aal1CesPepStorageType_Object = MibTableColumn
aal1CesPepStorageType = _Aal1CesPepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 1, 1, 4),
    _Aal1CesPepStorageType_Type()
)
aal1CesPepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPepStorageType.setStatus("mandatory")
_Aal1CesPepIndex_Type = NonReplicated
_Aal1CesPepIndex_Object = MibTableColumn
aal1CesPepIndex = _Aal1CesPepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 1, 1, 10),
    _Aal1CesPepIndex_Type()
)
aal1CesPepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal1CesPepIndex.setStatus("mandatory")
_Aal1CesPepProvEndPointAddrTable_Object = MibTable
aal1CesPepProvEndPointAddrTable = _Aal1CesPepProvEndPointAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 10)
)
if mibBuilder.loadTexts:
    aal1CesPepProvEndPointAddrTable.setStatus("mandatory")
_Aal1CesPepProvEndPointAddrEntry_Object = MibTableRow
aal1CesPepProvEndPointAddrEntry = _Aal1CesPepProvEndPointAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 10, 1)
)
aal1CesPepProvEndPointAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesPepProvEndPointAddrEntry.setStatus("mandatory")


class _Aal1CesPepExpectedRemoteAddress_Type(AsciiString):
    """Custom type aal1CesPepExpectedRemoteAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aal1CesPepExpectedRemoteAddress_Type.__name__ = "AsciiString"
_Aal1CesPepExpectedRemoteAddress_Object = MibTableColumn
aal1CesPepExpectedRemoteAddress = _Aal1CesPepExpectedRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 10, 1, 1),
    _Aal1CesPepExpectedRemoteAddress_Type()
)
aal1CesPepExpectedRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesPepExpectedRemoteAddress.setStatus("mandatory")


class _Aal1CesPepLocalAddress_Type(AsciiString):
    """Custom type aal1CesPepLocalAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_Aal1CesPepLocalAddress_Type.__name__ = "AsciiString"
_Aal1CesPepLocalAddress_Object = MibTableColumn
aal1CesPepLocalAddress = _Aal1CesPepLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 10, 1, 2),
    _Aal1CesPepLocalAddress_Type()
)
aal1CesPepLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesPepLocalAddress.setStatus("mandatory")
_Aal1CesPepEpOperTable_Object = MibTable
aal1CesPepEpOperTable = _Aal1CesPepEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 11)
)
if mibBuilder.loadTexts:
    aal1CesPepEpOperTable.setStatus("mandatory")
_Aal1CesPepEpOperEntry_Object = MibTableRow
aal1CesPepEpOperEntry = _Aal1CesPepEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 11, 1)
)
aal1CesPepEpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesPepEpOperEntry.setStatus("mandatory")


class _Aal1CesPepRemoteAddress_Type(AsciiString):
    """Custom type aal1CesPepRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_Aal1CesPepRemoteAddress_Type.__name__ = "AsciiString"
_Aal1CesPepRemoteAddress_Object = MibTableColumn
aal1CesPepRemoteAddress = _Aal1CesPepRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 11, 1, 1),
    _Aal1CesPepRemoteAddress_Type()
)
aal1CesPepRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPepRemoteAddress.setStatus("mandatory")


class _Aal1CesPepLastTearDownCause_Type(Unsigned32):
    """Custom type aal1CesPepLastTearDownCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal1CesPepLastTearDownCause_Type.__name__ = "Unsigned32"
_Aal1CesPepLastTearDownCause_Object = MibTableColumn
aal1CesPepLastTearDownCause = _Aal1CesPepLastTearDownCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 11, 1, 2),
    _Aal1CesPepLastTearDownCause_Type()
)
aal1CesPepLastTearDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPepLastTearDownCause.setStatus("mandatory")


class _Aal1CesPepLastTearDownDiagnostic_Type(AsciiString):
    """Custom type aal1CesPepLastTearDownDiagnostic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Aal1CesPepLastTearDownDiagnostic_Type.__name__ = "AsciiString"
_Aal1CesPepLastTearDownDiagnostic_Object = MibTableColumn
aal1CesPepLastTearDownDiagnostic = _Aal1CesPepLastTearDownDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 11, 1, 3),
    _Aal1CesPepLastTearDownDiagnostic_Type()
)
aal1CesPepLastTearDownDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPepLastTearDownDiagnostic.setStatus("mandatory")
_Aal1CesPepPassiveOperTable_Object = MibTable
aal1CesPepPassiveOperTable = _Aal1CesPepPassiveOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 12)
)
if mibBuilder.loadTexts:
    aal1CesPepPassiveOperTable.setStatus("mandatory")
_Aal1CesPepPassiveOperEntry_Object = MibTableRow
aal1CesPepPassiveOperEntry = _Aal1CesPepPassiveOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 12, 1)
)
aal1CesPepPassiveOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    aal1CesPepPassiveOperEntry.setStatus("mandatory")


class _Aal1CesPepSvcStatus_Type(Integer32):
    """Custom type aal1CesPepSvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 1),
          ("failed", 5),
          ("idle", 3),
          ("initialising", 0))
    )


_Aal1CesPepSvcStatus_Type.__name__ = "Integer32"
_Aal1CesPepSvcStatus_Object = MibTableColumn
aal1CesPepSvcStatus = _Aal1CesPepSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 4, 12, 1, 1),
    _Aal1CesPepSvcStatus_Type()
)
aal1CesPepSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPepSvcStatus.setStatus("mandatory")
_Aal1CesLCo_ObjectIdentity = ObjectIdentity
aal1CesLCo = _Aal1CesLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5)
)
_Aal1CesLCoRowStatusTable_Object = MibTable
aal1CesLCoRowStatusTable = _Aal1CesLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 1)
)
if mibBuilder.loadTexts:
    aal1CesLCoRowStatusTable.setStatus("mandatory")
_Aal1CesLCoRowStatusEntry_Object = MibTableRow
aal1CesLCoRowStatusEntry = _Aal1CesLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 1, 1)
)
aal1CesLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesLCoIndex"),
)
if mibBuilder.loadTexts:
    aal1CesLCoRowStatusEntry.setStatus("mandatory")
_Aal1CesLCoRowStatus_Type = RowStatus
_Aal1CesLCoRowStatus_Object = MibTableColumn
aal1CesLCoRowStatus = _Aal1CesLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 1, 1, 1),
    _Aal1CesLCoRowStatus_Type()
)
aal1CesLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRowStatus.setStatus("mandatory")
_Aal1CesLCoComponentName_Type = DisplayString
_Aal1CesLCoComponentName_Object = MibTableColumn
aal1CesLCoComponentName = _Aal1CesLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 1, 1, 2),
    _Aal1CesLCoComponentName_Type()
)
aal1CesLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoComponentName.setStatus("mandatory")
_Aal1CesLCoStorageType_Type = StorageType
_Aal1CesLCoStorageType_Object = MibTableColumn
aal1CesLCoStorageType = _Aal1CesLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 1, 1, 4),
    _Aal1CesLCoStorageType_Type()
)
aal1CesLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoStorageType.setStatus("mandatory")
_Aal1CesLCoIndex_Type = NonReplicated
_Aal1CesLCoIndex_Object = MibTableColumn
aal1CesLCoIndex = _Aal1CesLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 1, 1, 10),
    _Aal1CesLCoIndex_Type()
)
aal1CesLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal1CesLCoIndex.setStatus("mandatory")
_Aal1CesLCoPathDataTable_Object = MibTable
aal1CesLCoPathDataTable = _Aal1CesLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10)
)
if mibBuilder.loadTexts:
    aal1CesLCoPathDataTable.setStatus("mandatory")
_Aal1CesLCoPathDataEntry_Object = MibTableRow
aal1CesLCoPathDataEntry = _Aal1CesLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1)
)
aal1CesLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesLCoIndex"),
)
if mibBuilder.loadTexts:
    aal1CesLCoPathDataEntry.setStatus("mandatory")


class _Aal1CesLCoState_Type(Integer32):
    """Custom type aal1CesLCoState based on Integer32"""
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


_Aal1CesLCoState_Type.__name__ = "Integer32"
_Aal1CesLCoState_Object = MibTableColumn
aal1CesLCoState = _Aal1CesLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 1),
    _Aal1CesLCoState_Type()
)
aal1CesLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoState.setStatus("mandatory")


class _Aal1CesLCoOverrideRemoteName_Type(AsciiString):
    """Custom type aal1CesLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aal1CesLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_Aal1CesLCoOverrideRemoteName_Object = MibTableColumn
aal1CesLCoOverrideRemoteName = _Aal1CesLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 2),
    _Aal1CesLCoOverrideRemoteName_Type()
)
aal1CesLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesLCoOverrideRemoteName.setStatus("mandatory")


class _Aal1CesLCoEnd_Type(Integer32):
    """Custom type aal1CesLCoEnd based on Integer32"""
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


_Aal1CesLCoEnd_Type.__name__ = "Integer32"
_Aal1CesLCoEnd_Object = MibTableColumn
aal1CesLCoEnd = _Aal1CesLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 3),
    _Aal1CesLCoEnd_Type()
)
aal1CesLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoEnd.setStatus("mandatory")


class _Aal1CesLCoCostMetric_Type(Unsigned32):
    """Custom type aal1CesLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aal1CesLCoCostMetric_Type.__name__ = "Unsigned32"
_Aal1CesLCoCostMetric_Object = MibTableColumn
aal1CesLCoCostMetric = _Aal1CesLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 4),
    _Aal1CesLCoCostMetric_Type()
)
aal1CesLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoCostMetric.setStatus("mandatory")


class _Aal1CesLCoDelayMetric_Type(Unsigned32):
    """Custom type aal1CesLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Aal1CesLCoDelayMetric_Type.__name__ = "Unsigned32"
_Aal1CesLCoDelayMetric_Object = MibTableColumn
aal1CesLCoDelayMetric = _Aal1CesLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 5),
    _Aal1CesLCoDelayMetric_Type()
)
aal1CesLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoDelayMetric.setStatus("mandatory")


class _Aal1CesLCoRoundTripDelay_Type(Unsigned32):
    """Custom type aal1CesLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_Aal1CesLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_Aal1CesLCoRoundTripDelay_Object = MibTableColumn
aal1CesLCoRoundTripDelay = _Aal1CesLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 6),
    _Aal1CesLCoRoundTripDelay_Type()
)
aal1CesLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRoundTripDelay.setStatus("mandatory")


class _Aal1CesLCoSetupPriority_Type(Unsigned32):
    """Custom type aal1CesLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Aal1CesLCoSetupPriority_Type.__name__ = "Unsigned32"
_Aal1CesLCoSetupPriority_Object = MibTableColumn
aal1CesLCoSetupPriority = _Aal1CesLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 7),
    _Aal1CesLCoSetupPriority_Type()
)
aal1CesLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoSetupPriority.setStatus("mandatory")


class _Aal1CesLCoHoldingPriority_Type(Unsigned32):
    """Custom type aal1CesLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Aal1CesLCoHoldingPriority_Type.__name__ = "Unsigned32"
_Aal1CesLCoHoldingPriority_Object = MibTableColumn
aal1CesLCoHoldingPriority = _Aal1CesLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 8),
    _Aal1CesLCoHoldingPriority_Type()
)
aal1CesLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoHoldingPriority.setStatus("mandatory")


class _Aal1CesLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type aal1CesLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Aal1CesLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_Aal1CesLCoRequiredTxBandwidth_Object = MibTableColumn
aal1CesLCoRequiredTxBandwidth = _Aal1CesLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 9),
    _Aal1CesLCoRequiredTxBandwidth_Type()
)
aal1CesLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRequiredTxBandwidth.setStatus("mandatory")


class _Aal1CesLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type aal1CesLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Aal1CesLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_Aal1CesLCoRequiredRxBandwidth_Object = MibTableColumn
aal1CesLCoRequiredRxBandwidth = _Aal1CesLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 10),
    _Aal1CesLCoRequiredRxBandwidth_Type()
)
aal1CesLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRequiredRxBandwidth.setStatus("mandatory")


class _Aal1CesLCoRequiredTrafficType_Type(Integer32):
    """Custom type aal1CesLCoRequiredTrafficType based on Integer32"""
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


_Aal1CesLCoRequiredTrafficType_Type.__name__ = "Integer32"
_Aal1CesLCoRequiredTrafficType_Object = MibTableColumn
aal1CesLCoRequiredTrafficType = _Aal1CesLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 11),
    _Aal1CesLCoRequiredTrafficType_Type()
)
aal1CesLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRequiredTrafficType.setStatus("mandatory")


class _Aal1CesLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type aal1CesLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Aal1CesLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_Aal1CesLCoPermittedTrunkTypes_Object = MibTableColumn
aal1CesLCoPermittedTrunkTypes = _Aal1CesLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 12),
    _Aal1CesLCoPermittedTrunkTypes_Type()
)
aal1CesLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPermittedTrunkTypes.setStatus("mandatory")


class _Aal1CesLCoRequiredSecurity_Type(Unsigned32):
    """Custom type aal1CesLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Aal1CesLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_Aal1CesLCoRequiredSecurity_Object = MibTableColumn
aal1CesLCoRequiredSecurity = _Aal1CesLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 13),
    _Aal1CesLCoRequiredSecurity_Type()
)
aal1CesLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRequiredSecurity.setStatus("mandatory")


class _Aal1CesLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type aal1CesLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Aal1CesLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_Aal1CesLCoRequiredCustomerParameter_Object = MibTableColumn
aal1CesLCoRequiredCustomerParameter = _Aal1CesLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 14),
    _Aal1CesLCoRequiredCustomerParameter_Type()
)
aal1CesLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRequiredCustomerParameter.setStatus("mandatory")


class _Aal1CesLCoEmissionPriority_Type(Unsigned32):
    """Custom type aal1CesLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Aal1CesLCoEmissionPriority_Type.__name__ = "Unsigned32"
_Aal1CesLCoEmissionPriority_Object = MibTableColumn
aal1CesLCoEmissionPriority = _Aal1CesLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 15),
    _Aal1CesLCoEmissionPriority_Type()
)
aal1CesLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoEmissionPriority.setStatus("mandatory")


class _Aal1CesLCoDiscardPriority_Type(Unsigned32):
    """Custom type aal1CesLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Aal1CesLCoDiscardPriority_Type.__name__ = "Unsigned32"
_Aal1CesLCoDiscardPriority_Object = MibTableColumn
aal1CesLCoDiscardPriority = _Aal1CesLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 16),
    _Aal1CesLCoDiscardPriority_Type()
)
aal1CesLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoDiscardPriority.setStatus("mandatory")


class _Aal1CesLCoPathType_Type(Integer32):
    """Custom type aal1CesLCoPathType based on Integer32"""
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


_Aal1CesLCoPathType_Type.__name__ = "Integer32"
_Aal1CesLCoPathType_Object = MibTableColumn
aal1CesLCoPathType = _Aal1CesLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 17),
    _Aal1CesLCoPathType_Type()
)
aal1CesLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPathType.setStatus("mandatory")


class _Aal1CesLCoRetryCount_Type(Unsigned32):
    """Custom type aal1CesLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal1CesLCoRetryCount_Type.__name__ = "Unsigned32"
_Aal1CesLCoRetryCount_Object = MibTableColumn
aal1CesLCoRetryCount = _Aal1CesLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 18),
    _Aal1CesLCoRetryCount_Type()
)
aal1CesLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoRetryCount.setStatus("mandatory")


class _Aal1CesLCoPathFailureCount_Type(Unsigned32):
    """Custom type aal1CesLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aal1CesLCoPathFailureCount_Type.__name__ = "Unsigned32"
_Aal1CesLCoPathFailureCount_Object = MibTableColumn
aal1CesLCoPathFailureCount = _Aal1CesLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 19),
    _Aal1CesLCoPathFailureCount_Type()
)
aal1CesLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPathFailureCount.setStatus("mandatory")


class _Aal1CesLCoReasonForNoRoute_Type(Integer32):
    """Custom type aal1CesLCoReasonForNoRoute based on Integer32"""
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


_Aal1CesLCoReasonForNoRoute_Type.__name__ = "Integer32"
_Aal1CesLCoReasonForNoRoute_Object = MibTableColumn
aal1CesLCoReasonForNoRoute = _Aal1CesLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 20),
    _Aal1CesLCoReasonForNoRoute_Type()
)
aal1CesLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoReasonForNoRoute.setStatus("mandatory")


class _Aal1CesLCoLastTearDownReason_Type(Integer32):
    """Custom type aal1CesLCoLastTearDownReason based on Integer32"""
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


_Aal1CesLCoLastTearDownReason_Type.__name__ = "Integer32"
_Aal1CesLCoLastTearDownReason_Object = MibTableColumn
aal1CesLCoLastTearDownReason = _Aal1CesLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 21),
    _Aal1CesLCoLastTearDownReason_Type()
)
aal1CesLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoLastTearDownReason.setStatus("mandatory")


class _Aal1CesLCoPathFailureAction_Type(Integer32):
    """Custom type aal1CesLCoPathFailureAction based on Integer32"""
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


_Aal1CesLCoPathFailureAction_Type.__name__ = "Integer32"
_Aal1CesLCoPathFailureAction_Object = MibTableColumn
aal1CesLCoPathFailureAction = _Aal1CesLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 22),
    _Aal1CesLCoPathFailureAction_Type()
)
aal1CesLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPathFailureAction.setStatus("mandatory")


class _Aal1CesLCoBumpPreference_Type(Integer32):
    """Custom type aal1CesLCoBumpPreference based on Integer32"""
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


_Aal1CesLCoBumpPreference_Type.__name__ = "Integer32"
_Aal1CesLCoBumpPreference_Object = MibTableColumn
aal1CesLCoBumpPreference = _Aal1CesLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 23),
    _Aal1CesLCoBumpPreference_Type()
)
aal1CesLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoBumpPreference.setStatus("mandatory")


class _Aal1CesLCoOptimization_Type(Integer32):
    """Custom type aal1CesLCoOptimization based on Integer32"""
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


_Aal1CesLCoOptimization_Type.__name__ = "Integer32"
_Aal1CesLCoOptimization_Object = MibTableColumn
aal1CesLCoOptimization = _Aal1CesLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 24),
    _Aal1CesLCoOptimization_Type()
)
aal1CesLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoOptimization.setStatus("mandatory")


class _Aal1CesLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type aal1CesLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_Aal1CesLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_Aal1CesLCoPathUpDateTime_Object = MibTableColumn
aal1CesLCoPathUpDateTime = _Aal1CesLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 10, 1, 25),
    _Aal1CesLCoPathUpDateTime_Type()
)
aal1CesLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPathUpDateTime.setStatus("mandatory")
_Aal1CesLCoStatsTable_Object = MibTable
aal1CesLCoStatsTable = _Aal1CesLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 11)
)
if mibBuilder.loadTexts:
    aal1CesLCoStatsTable.setStatus("mandatory")
_Aal1CesLCoStatsEntry_Object = MibTableRow
aal1CesLCoStatsEntry = _Aal1CesLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 11, 1)
)
aal1CesLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesLCoIndex"),
)
if mibBuilder.loadTexts:
    aal1CesLCoStatsEntry.setStatus("mandatory")
_Aal1CesLCoPktsToNetwork_Type = PassportCounter64
_Aal1CesLCoPktsToNetwork_Object = MibTableColumn
aal1CesLCoPktsToNetwork = _Aal1CesLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 11, 1, 1),
    _Aal1CesLCoPktsToNetwork_Type()
)
aal1CesLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPktsToNetwork.setStatus("mandatory")
_Aal1CesLCoBytesToNetwork_Type = PassportCounter64
_Aal1CesLCoBytesToNetwork_Object = MibTableColumn
aal1CesLCoBytesToNetwork = _Aal1CesLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 11, 1, 2),
    _Aal1CesLCoBytesToNetwork_Type()
)
aal1CesLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoBytesToNetwork.setStatus("mandatory")
_Aal1CesLCoPktsFromNetwork_Type = PassportCounter64
_Aal1CesLCoPktsFromNetwork_Object = MibTableColumn
aal1CesLCoPktsFromNetwork = _Aal1CesLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 11, 1, 3),
    _Aal1CesLCoPktsFromNetwork_Type()
)
aal1CesLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPktsFromNetwork.setStatus("mandatory")
_Aal1CesLCoBytesFromNetwork_Type = PassportCounter64
_Aal1CesLCoBytesFromNetwork_Object = MibTableColumn
aal1CesLCoBytesFromNetwork = _Aal1CesLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 11, 1, 4),
    _Aal1CesLCoBytesFromNetwork_Type()
)
aal1CesLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoBytesFromNetwork.setStatus("mandatory")
_Aal1CesLCoPathTable_Object = MibTable
aal1CesLCoPathTable = _Aal1CesLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 264)
)
if mibBuilder.loadTexts:
    aal1CesLCoPathTable.setStatus("mandatory")
_Aal1CesLCoPathEntry_Object = MibTableRow
aal1CesLCoPathEntry = _Aal1CesLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 264, 1)
)
aal1CesLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesLCoIndex"),
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesLCoPathValue"),
)
if mibBuilder.loadTexts:
    aal1CesLCoPathEntry.setStatus("mandatory")


class _Aal1CesLCoPathValue_Type(AsciiString):
    """Custom type aal1CesLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aal1CesLCoPathValue_Type.__name__ = "AsciiString"
_Aal1CesLCoPathValue_Object = MibTableColumn
aal1CesLCoPathValue = _Aal1CesLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 5, 264, 1, 1),
    _Aal1CesLCoPathValue_Type()
)
aal1CesLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLCoPathValue.setStatus("mandatory")
_Aal1CesCidDataTable_Object = MibTable
aal1CesCidDataTable = _Aal1CesCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 10)
)
if mibBuilder.loadTexts:
    aal1CesCidDataTable.setStatus("mandatory")
_Aal1CesCidDataEntry_Object = MibTableRow
aal1CesCidDataEntry = _Aal1CesCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 10, 1)
)
aal1CesCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
)
if mibBuilder.loadTexts:
    aal1CesCidDataEntry.setStatus("mandatory")


class _Aal1CesCustomerIdentifier_Type(Unsigned32):
    """Custom type aal1CesCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_Aal1CesCustomerIdentifier_Type.__name__ = "Unsigned32"
_Aal1CesCustomerIdentifier_Object = MibTableColumn
aal1CesCustomerIdentifier = _Aal1CesCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 10, 1, 1),
    _Aal1CesCustomerIdentifier_Type()
)
aal1CesCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesCustomerIdentifier.setStatus("mandatory")
_Aal1CesProvTable_Object = MibTable
aal1CesProvTable = _Aal1CesProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11)
)
if mibBuilder.loadTexts:
    aal1CesProvTable.setStatus("mandatory")
_Aal1CesProvEntry_Object = MibTableRow
aal1CesProvEntry = _Aal1CesProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1)
)
aal1CesProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
)
if mibBuilder.loadTexts:
    aal1CesProvEntry.setStatus("mandatory")


class _Aal1CesServiceType_Type(Integer32):
    """Custom type aal1CesServiceType based on Integer32"""
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
        *(("basicStructured", 1),
          ("casStructured", 2),
          ("unstructured", 0))
    )


_Aal1CesServiceType_Type.__name__ = "Integer32"
_Aal1CesServiceType_Object = MibTableColumn
aal1CesServiceType = _Aal1CesServiceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 1),
    _Aal1CesServiceType_Type()
)
aal1CesServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesServiceType.setStatus("mandatory")


class _Aal1CesBufferSize_Type(Unsigned32):
    """Custom type aal1CesBufferSize based on Unsigned32"""
    defaultValue = 282

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(94, 15651),
    )


_Aal1CesBufferSize_Type.__name__ = "Unsigned32"
_Aal1CesBufferSize_Object = MibTableColumn
aal1CesBufferSize = _Aal1CesBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 2),
    _Aal1CesBufferSize_Type()
)
aal1CesBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesBufferSize.setStatus("mandatory")


class _Aal1CesCellDelayVariationTolerance_Type(Unsigned32):
    """Custom type aal1CesCellDelayVariationTolerance based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_Aal1CesCellDelayVariationTolerance_Type.__name__ = "Unsigned32"
_Aal1CesCellDelayVariationTolerance_Object = MibTableColumn
aal1CesCellDelayVariationTolerance = _Aal1CesCellDelayVariationTolerance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 3),
    _Aal1CesCellDelayVariationTolerance_Type()
)
aal1CesCellDelayVariationTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesCellDelayVariationTolerance.setStatus("mandatory")


class _Aal1CesCellLossIntegrationPeriod_Type(Unsigned32):
    """Custom type aal1CesCellLossIntegrationPeriod based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_Aal1CesCellLossIntegrationPeriod_Type.__name__ = "Unsigned32"
_Aal1CesCellLossIntegrationPeriod_Object = MibTableColumn
aal1CesCellLossIntegrationPeriod = _Aal1CesCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 4),
    _Aal1CesCellLossIntegrationPeriod_Type()
)
aal1CesCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesCellLossIntegrationPeriod.setStatus("mandatory")
_Aal1CesInterfaceName_Type = Link
_Aal1CesInterfaceName_Object = MibTableColumn
aal1CesInterfaceName = _Aal1CesInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 5),
    _Aal1CesInterfaceName_Type()
)
aal1CesInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesInterfaceName.setStatus("mandatory")


class _Aal1CesPartialFill_Type(Unsigned32):
    """Custom type aal1CesPartialFill based on Unsigned32"""
    defaultValue = 47

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 47),
    )


_Aal1CesPartialFill_Type.__name__ = "Unsigned32"
_Aal1CesPartialFill_Object = MibTableColumn
aal1CesPartialFill = _Aal1CesPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 6),
    _Aal1CesPartialFill_Type()
)
aal1CesPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesPartialFill.setStatus("mandatory")


class _Aal1CesIdleSuppression_Type(Integer32):
    """Custom type aal1CesIdleSuppression based on Integer32"""
    defaultValue = 0

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


_Aal1CesIdleSuppression_Type.__name__ = "Integer32"
_Aal1CesIdleSuppression_Object = MibTableColumn
aal1CesIdleSuppression = _Aal1CesIdleSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 7),
    _Aal1CesIdleSuppression_Type()
)
aal1CesIdleSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesIdleSuppression.setStatus("mandatory")


class _Aal1CesIdlePattern_Type(Hex):
    """Custom type aal1CesIdlePattern based on Hex"""
    defaultValue = 126

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal1CesIdlePattern_Type.__name__ = "Hex"
_Aal1CesIdlePattern_Object = MibTableColumn
aal1CesIdlePattern = _Aal1CesIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 8),
    _Aal1CesIdlePattern_Type()
)
aal1CesIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesIdlePattern.setStatus("mandatory")


class _Aal1CesCellLossRecoveryPeriod_Type(Unsigned32):
    """Custom type aal1CesCellLossRecoveryPeriod based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Aal1CesCellLossRecoveryPeriod_Type.__name__ = "Unsigned32"
_Aal1CesCellLossRecoveryPeriod_Object = MibTableColumn
aal1CesCellLossRecoveryPeriod = _Aal1CesCellLossRecoveryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 9),
    _Aal1CesCellLossRecoveryPeriod_Type()
)
aal1CesCellLossRecoveryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesCellLossRecoveryPeriod.setStatus("mandatory")


class _Aal1CesDummyDataByte_Type(Hex):
    """Custom type aal1CesDummyDataByte based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal1CesDummyDataByte_Type.__name__ = "Hex"
_Aal1CesDummyDataByte_Object = MibTableColumn
aal1CesDummyDataByte = _Aal1CesDummyDataByte_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 11, 1, 10),
    _Aal1CesDummyDataByte_Type()
)
aal1CesDummyDataByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal1CesDummyDataByte.setStatus("mandatory")
_Aal1CesStateTable_Object = MibTable
aal1CesStateTable = _Aal1CesStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12)
)
if mibBuilder.loadTexts:
    aal1CesStateTable.setStatus("mandatory")
_Aal1CesStateEntry_Object = MibTableRow
aal1CesStateEntry = _Aal1CesStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1)
)
aal1CesStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
)
if mibBuilder.loadTexts:
    aal1CesStateEntry.setStatus("mandatory")


class _Aal1CesAdminState_Type(Integer32):
    """Custom type aal1CesAdminState based on Integer32"""
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


_Aal1CesAdminState_Type.__name__ = "Integer32"
_Aal1CesAdminState_Object = MibTableColumn
aal1CesAdminState = _Aal1CesAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 1),
    _Aal1CesAdminState_Type()
)
aal1CesAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAdminState.setStatus("mandatory")


class _Aal1CesOperationalState_Type(Integer32):
    """Custom type aal1CesOperationalState based on Integer32"""
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


_Aal1CesOperationalState_Type.__name__ = "Integer32"
_Aal1CesOperationalState_Object = MibTableColumn
aal1CesOperationalState = _Aal1CesOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 2),
    _Aal1CesOperationalState_Type()
)
aal1CesOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesOperationalState.setStatus("mandatory")


class _Aal1CesUsageState_Type(Integer32):
    """Custom type aal1CesUsageState based on Integer32"""
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


_Aal1CesUsageState_Type.__name__ = "Integer32"
_Aal1CesUsageState_Object = MibTableColumn
aal1CesUsageState = _Aal1CesUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 3),
    _Aal1CesUsageState_Type()
)
aal1CesUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesUsageState.setStatus("mandatory")


class _Aal1CesAvailabilityStatus_Type(OctetString):
    """Custom type aal1CesAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Aal1CesAvailabilityStatus_Type.__name__ = "OctetString"
_Aal1CesAvailabilityStatus_Object = MibTableColumn
aal1CesAvailabilityStatus = _Aal1CesAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 4),
    _Aal1CesAvailabilityStatus_Type()
)
aal1CesAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAvailabilityStatus.setStatus("mandatory")


class _Aal1CesProceduralStatus_Type(OctetString):
    """Custom type aal1CesProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Aal1CesProceduralStatus_Type.__name__ = "OctetString"
_Aal1CesProceduralStatus_Object = MibTableColumn
aal1CesProceduralStatus = _Aal1CesProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 5),
    _Aal1CesProceduralStatus_Type()
)
aal1CesProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesProceduralStatus.setStatus("mandatory")


class _Aal1CesControlStatus_Type(OctetString):
    """Custom type aal1CesControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Aal1CesControlStatus_Type.__name__ = "OctetString"
_Aal1CesControlStatus_Object = MibTableColumn
aal1CesControlStatus = _Aal1CesControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 6),
    _Aal1CesControlStatus_Type()
)
aal1CesControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesControlStatus.setStatus("mandatory")


class _Aal1CesAlarmStatus_Type(OctetString):
    """Custom type aal1CesAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Aal1CesAlarmStatus_Type.__name__ = "OctetString"
_Aal1CesAlarmStatus_Object = MibTableColumn
aal1CesAlarmStatus = _Aal1CesAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 7),
    _Aal1CesAlarmStatus_Type()
)
aal1CesAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAlarmStatus.setStatus("mandatory")


class _Aal1CesStandbyStatus_Type(Integer32):
    """Custom type aal1CesStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_Aal1CesStandbyStatus_Type.__name__ = "Integer32"
_Aal1CesStandbyStatus_Object = MibTableColumn
aal1CesStandbyStatus = _Aal1CesStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 8),
    _Aal1CesStandbyStatus_Type()
)
aal1CesStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesStandbyStatus.setStatus("mandatory")


class _Aal1CesUnknownStatus_Type(Integer32):
    """Custom type aal1CesUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Aal1CesUnknownStatus_Type.__name__ = "Integer32"
_Aal1CesUnknownStatus_Object = MibTableColumn
aal1CesUnknownStatus = _Aal1CesUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 12, 1, 9),
    _Aal1CesUnknownStatus_Type()
)
aal1CesUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesUnknownStatus.setStatus("mandatory")
_Aal1CesOperTable_Object = MibTable
aal1CesOperTable = _Aal1CesOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 13)
)
if mibBuilder.loadTexts:
    aal1CesOperTable.setStatus("mandatory")
_Aal1CesOperEntry_Object = MibTableRow
aal1CesOperEntry = _Aal1CesOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 13, 1)
)
aal1CesOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
)
if mibBuilder.loadTexts:
    aal1CesOperEntry.setStatus("mandatory")


class _Aal1CesCellLossStatus_Type(Integer32):
    """Custom type aal1CesCellLossStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("noLoss", 0))
    )


_Aal1CesCellLossStatus_Type.__name__ = "Integer32"
_Aal1CesCellLossStatus_Object = MibTableColumn
aal1CesCellLossStatus = _Aal1CesCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 13, 1, 1),
    _Aal1CesCellLossStatus_Type()
)
aal1CesCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesCellLossStatus.setStatus("mandatory")


class _Aal1CesAal1LayerLossStatus_Type(Integer32):
    """Custom type aal1CesAal1LayerLossStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("noLoss", 0))
    )


_Aal1CesAal1LayerLossStatus_Type.__name__ = "Integer32"
_Aal1CesAal1LayerLossStatus_Object = MibTableColumn
aal1CesAal1LayerLossStatus = _Aal1CesAal1LayerLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 13, 1, 2),
    _Aal1CesAal1LayerLossStatus_Type()
)
aal1CesAal1LayerLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAal1LayerLossStatus.setStatus("mandatory")


class _Aal1CesConnectionStatus_Type(Integer32):
    """Custom type aal1CesConnectionStatus based on Integer32"""
    defaultValue = 1

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
        *(("atmNotConfigured", 3),
          ("atmNotReady", 2),
          ("channelNotReady", 1),
          ("connected", 0))
    )


_Aal1CesConnectionStatus_Type.__name__ = "Integer32"
_Aal1CesConnectionStatus_Object = MibTableColumn
aal1CesConnectionStatus = _Aal1CesConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 13, 1, 3),
    _Aal1CesConnectionStatus_Type()
)
aal1CesConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesConnectionStatus.setStatus("mandatory")
_Aal1CesStatsTable_Object = MibTable
aal1CesStatsTable = _Aal1CesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14)
)
if mibBuilder.loadTexts:
    aal1CesStatsTable.setStatus("mandatory")
_Aal1CesStatsEntry_Object = MibTableRow
aal1CesStatsEntry = _Aal1CesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1)
)
aal1CesStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CircuitEmulationServiceMIB", "aal1CesIndex"),
)
if mibBuilder.loadTexts:
    aal1CesStatsEntry.setStatus("mandatory")
_Aal1CesCellsTransmitted_Type = PassportCounter64
_Aal1CesCellsTransmitted_Object = MibTableColumn
aal1CesCellsTransmitted = _Aal1CesCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 1),
    _Aal1CesCellsTransmitted_Type()
)
aal1CesCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesCellsTransmitted.setStatus("mandatory")
_Aal1CesCellsReceived_Type = PassportCounter64
_Aal1CesCellsReceived_Object = MibTableColumn
aal1CesCellsReceived = _Aal1CesCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 2),
    _Aal1CesCellsReceived_Type()
)
aal1CesCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesCellsReceived.setStatus("mandatory")
_Aal1CesLostCells_Type = Counter32
_Aal1CesLostCells_Object = MibTableColumn
aal1CesLostCells = _Aal1CesLostCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 3),
    _Aal1CesLostCells_Type()
)
aal1CesLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesLostCells.setStatus("mandatory")
_Aal1CesBufferUnderflows_Type = Counter32
_Aal1CesBufferUnderflows_Object = MibTableColumn
aal1CesBufferUnderflows = _Aal1CesBufferUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 4),
    _Aal1CesBufferUnderflows_Type()
)
aal1CesBufferUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesBufferUnderflows.setStatus("mandatory")
_Aal1CesBufferOverflows_Type = Counter32
_Aal1CesBufferOverflows_Object = MibTableColumn
aal1CesBufferOverflows = _Aal1CesBufferOverflows_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 5),
    _Aal1CesBufferOverflows_Type()
)
aal1CesBufferOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesBufferOverflows.setStatus("mandatory")
_Aal1CesReassembledCells_Type = PassportCounter64
_Aal1CesReassembledCells_Object = MibTableColumn
aal1CesReassembledCells = _Aal1CesReassembledCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 6),
    _Aal1CesReassembledCells_Type()
)
aal1CesReassembledCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesReassembledCells.setStatus("mandatory")
_Aal1CesHeaderErrors_Type = Counter32
_Aal1CesHeaderErrors_Object = MibTableColumn
aal1CesHeaderErrors = _Aal1CesHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 7),
    _Aal1CesHeaderErrors_Type()
)
aal1CesHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesHeaderErrors.setStatus("mandatory")
_Aal1CesPointerReframes_Type = Counter32
_Aal1CesPointerReframes_Object = MibTableColumn
aal1CesPointerReframes = _Aal1CesPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 8),
    _Aal1CesPointerReframes_Type()
)
aal1CesPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPointerReframes.setStatus("mandatory")
_Aal1CesPointerParityErrors_Type = Counter32
_Aal1CesPointerParityErrors_Object = MibTableColumn
aal1CesPointerParityErrors = _Aal1CesPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 9),
    _Aal1CesPointerParityErrors_Type()
)
aal1CesPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesPointerParityErrors.setStatus("mandatory")
_Aal1CesAal1SequenceErrors_Type = Counter32
_Aal1CesAal1SequenceErrors_Object = MibTableColumn
aal1CesAal1SequenceErrors = _Aal1CesAal1SequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 10),
    _Aal1CesAal1SequenceErrors_Type()
)
aal1CesAal1SequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesAal1SequenceErrors.setStatus("mandatory")
_Aal1CesMisinsertedCells_Type = Counter32
_Aal1CesMisinsertedCells_Object = MibTableColumn
aal1CesMisinsertedCells = _Aal1CesMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 119, 14, 1, 11),
    _Aal1CesMisinsertedCells_Type()
)
aal1CesMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal1CesMisinsertedCells.setStatus("mandatory")
_CircuitEmulationServiceMIB_ObjectIdentity = ObjectIdentity
circuitEmulationServiceMIB = _CircuitEmulationServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55)
)
_CircuitEmulationServiceGroup_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroup = _CircuitEmulationServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 1)
)
_CircuitEmulationServiceGroupBD_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroupBD = _CircuitEmulationServiceGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 1, 4)
)
_CircuitEmulationServiceGroupBD00_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroupBD00 = _CircuitEmulationServiceGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 1, 4, 1)
)
_CircuitEmulationServiceGroupBD00A_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroupBD00A = _CircuitEmulationServiceGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 1, 4, 1, 2)
)
_CircuitEmulationServiceCapabilities_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilities = _CircuitEmulationServiceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 3)
)
_CircuitEmulationServiceCapabilitiesBD_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilitiesBD = _CircuitEmulationServiceCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 3, 4)
)
_CircuitEmulationServiceCapabilitiesBD00_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilitiesBD00 = _CircuitEmulationServiceCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 3, 4, 1)
)
_CircuitEmulationServiceCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilitiesBD00A = _CircuitEmulationServiceCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 55, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-CircuitEmulationServiceMIB",
    **{"aal1Ces": aal1Ces,
       "aal1CesRowStatusTable": aal1CesRowStatusTable,
       "aal1CesRowStatusEntry": aal1CesRowStatusEntry,
       "aal1CesRowStatus": aal1CesRowStatus,
       "aal1CesComponentName": aal1CesComponentName,
       "aal1CesStorageType": aal1CesStorageType,
       "aal1CesIndex": aal1CesIndex,
       "aal1CesNap": aal1CesNap,
       "aal1CesNapRowStatusTable": aal1CesNapRowStatusTable,
       "aal1CesNapRowStatusEntry": aal1CesNapRowStatusEntry,
       "aal1CesNapRowStatus": aal1CesNapRowStatus,
       "aal1CesNapComponentName": aal1CesNapComponentName,
       "aal1CesNapStorageType": aal1CesNapStorageType,
       "aal1CesNapIndex": aal1CesNapIndex,
       "aal1CesNapProvTable": aal1CesNapProvTable,
       "aal1CesNapProvEntry": aal1CesNapProvEntry,
       "aal1CesNapAtmConnection": aal1CesNapAtmConnection,
       "aal1CesAep": aal1CesAep,
       "aal1CesAepRowStatusTable": aal1CesAepRowStatusTable,
       "aal1CesAepRowStatusEntry": aal1CesAepRowStatusEntry,
       "aal1CesAepRowStatus": aal1CesAepRowStatus,
       "aal1CesAepComponentName": aal1CesAepComponentName,
       "aal1CesAepStorageType": aal1CesAepStorageType,
       "aal1CesAepIndex": aal1CesAepIndex,
       "aal1CesAepProvEndPointAddrTable": aal1CesAepProvEndPointAddrTable,
       "aal1CesAepProvEndPointAddrEntry": aal1CesAepProvEndPointAddrEntry,
       "aal1CesAepExpectedRemoteAddress": aal1CesAepExpectedRemoteAddress,
       "aal1CesAepLocalAddress": aal1CesAepLocalAddress,
       "aal1CesAepProvTable": aal1CesAepProvTable,
       "aal1CesAepProvEntry": aal1CesAepProvEntry,
       "aal1CesAepAddressToCall": aal1CesAepAddressToCall,
       "aal1CesAepRoutingOption": aal1CesAepRoutingOption,
       "aal1CesAepProfile": aal1CesAepProfile,
       "aal1CesAepFirstRetryInterval": aal1CesAepFirstRetryInterval,
       "aal1CesAepRetryLimit": aal1CesAepRetryLimit,
       "aal1CesAepEpOperTable": aal1CesAepEpOperTable,
       "aal1CesAepEpOperEntry": aal1CesAepEpOperEntry,
       "aal1CesAepRemoteAddress": aal1CesAepRemoteAddress,
       "aal1CesAepLastTearDownCause": aal1CesAepLastTearDownCause,
       "aal1CesAepLastTearDownDiagnostic": aal1CesAepLastTearDownDiagnostic,
       "aal1CesAepOutTable": aal1CesAepOutTable,
       "aal1CesAepOutEntry": aal1CesAepOutEntry,
       "aal1CesAepSvcStatus": aal1CesAepSvcStatus,
       "aal1CesAepLastSetupFailureCause": aal1CesAepLastSetupFailureCause,
       "aal1CesAepLastSetupFailureDiagnostic": aal1CesAepLastSetupFailureDiagnostic,
       "aal1CesAepRetryTimeRemaining": aal1CesAepRetryTimeRemaining,
       "aal1CesAepRetryFailures": aal1CesAepRetryFailures,
       "aal1CesPep": aal1CesPep,
       "aal1CesPepRowStatusTable": aal1CesPepRowStatusTable,
       "aal1CesPepRowStatusEntry": aal1CesPepRowStatusEntry,
       "aal1CesPepRowStatus": aal1CesPepRowStatus,
       "aal1CesPepComponentName": aal1CesPepComponentName,
       "aal1CesPepStorageType": aal1CesPepStorageType,
       "aal1CesPepIndex": aal1CesPepIndex,
       "aal1CesPepProvEndPointAddrTable": aal1CesPepProvEndPointAddrTable,
       "aal1CesPepProvEndPointAddrEntry": aal1CesPepProvEndPointAddrEntry,
       "aal1CesPepExpectedRemoteAddress": aal1CesPepExpectedRemoteAddress,
       "aal1CesPepLocalAddress": aal1CesPepLocalAddress,
       "aal1CesPepEpOperTable": aal1CesPepEpOperTable,
       "aal1CesPepEpOperEntry": aal1CesPepEpOperEntry,
       "aal1CesPepRemoteAddress": aal1CesPepRemoteAddress,
       "aal1CesPepLastTearDownCause": aal1CesPepLastTearDownCause,
       "aal1CesPepLastTearDownDiagnostic": aal1CesPepLastTearDownDiagnostic,
       "aal1CesPepPassiveOperTable": aal1CesPepPassiveOperTable,
       "aal1CesPepPassiveOperEntry": aal1CesPepPassiveOperEntry,
       "aal1CesPepSvcStatus": aal1CesPepSvcStatus,
       "aal1CesLCo": aal1CesLCo,
       "aal1CesLCoRowStatusTable": aal1CesLCoRowStatusTable,
       "aal1CesLCoRowStatusEntry": aal1CesLCoRowStatusEntry,
       "aal1CesLCoRowStatus": aal1CesLCoRowStatus,
       "aal1CesLCoComponentName": aal1CesLCoComponentName,
       "aal1CesLCoStorageType": aal1CesLCoStorageType,
       "aal1CesLCoIndex": aal1CesLCoIndex,
       "aal1CesLCoPathDataTable": aal1CesLCoPathDataTable,
       "aal1CesLCoPathDataEntry": aal1CesLCoPathDataEntry,
       "aal1CesLCoState": aal1CesLCoState,
       "aal1CesLCoOverrideRemoteName": aal1CesLCoOverrideRemoteName,
       "aal1CesLCoEnd": aal1CesLCoEnd,
       "aal1CesLCoCostMetric": aal1CesLCoCostMetric,
       "aal1CesLCoDelayMetric": aal1CesLCoDelayMetric,
       "aal1CesLCoRoundTripDelay": aal1CesLCoRoundTripDelay,
       "aal1CesLCoSetupPriority": aal1CesLCoSetupPriority,
       "aal1CesLCoHoldingPriority": aal1CesLCoHoldingPriority,
       "aal1CesLCoRequiredTxBandwidth": aal1CesLCoRequiredTxBandwidth,
       "aal1CesLCoRequiredRxBandwidth": aal1CesLCoRequiredRxBandwidth,
       "aal1CesLCoRequiredTrafficType": aal1CesLCoRequiredTrafficType,
       "aal1CesLCoPermittedTrunkTypes": aal1CesLCoPermittedTrunkTypes,
       "aal1CesLCoRequiredSecurity": aal1CesLCoRequiredSecurity,
       "aal1CesLCoRequiredCustomerParameter": aal1CesLCoRequiredCustomerParameter,
       "aal1CesLCoEmissionPriority": aal1CesLCoEmissionPriority,
       "aal1CesLCoDiscardPriority": aal1CesLCoDiscardPriority,
       "aal1CesLCoPathType": aal1CesLCoPathType,
       "aal1CesLCoRetryCount": aal1CesLCoRetryCount,
       "aal1CesLCoPathFailureCount": aal1CesLCoPathFailureCount,
       "aal1CesLCoReasonForNoRoute": aal1CesLCoReasonForNoRoute,
       "aal1CesLCoLastTearDownReason": aal1CesLCoLastTearDownReason,
       "aal1CesLCoPathFailureAction": aal1CesLCoPathFailureAction,
       "aal1CesLCoBumpPreference": aal1CesLCoBumpPreference,
       "aal1CesLCoOptimization": aal1CesLCoOptimization,
       "aal1CesLCoPathUpDateTime": aal1CesLCoPathUpDateTime,
       "aal1CesLCoStatsTable": aal1CesLCoStatsTable,
       "aal1CesLCoStatsEntry": aal1CesLCoStatsEntry,
       "aal1CesLCoPktsToNetwork": aal1CesLCoPktsToNetwork,
       "aal1CesLCoBytesToNetwork": aal1CesLCoBytesToNetwork,
       "aal1CesLCoPktsFromNetwork": aal1CesLCoPktsFromNetwork,
       "aal1CesLCoBytesFromNetwork": aal1CesLCoBytesFromNetwork,
       "aal1CesLCoPathTable": aal1CesLCoPathTable,
       "aal1CesLCoPathEntry": aal1CesLCoPathEntry,
       "aal1CesLCoPathValue": aal1CesLCoPathValue,
       "aal1CesCidDataTable": aal1CesCidDataTable,
       "aal1CesCidDataEntry": aal1CesCidDataEntry,
       "aal1CesCustomerIdentifier": aal1CesCustomerIdentifier,
       "aal1CesProvTable": aal1CesProvTable,
       "aal1CesProvEntry": aal1CesProvEntry,
       "aal1CesServiceType": aal1CesServiceType,
       "aal1CesBufferSize": aal1CesBufferSize,
       "aal1CesCellDelayVariationTolerance": aal1CesCellDelayVariationTolerance,
       "aal1CesCellLossIntegrationPeriod": aal1CesCellLossIntegrationPeriod,
       "aal1CesInterfaceName": aal1CesInterfaceName,
       "aal1CesPartialFill": aal1CesPartialFill,
       "aal1CesIdleSuppression": aal1CesIdleSuppression,
       "aal1CesIdlePattern": aal1CesIdlePattern,
       "aal1CesCellLossRecoveryPeriod": aal1CesCellLossRecoveryPeriod,
       "aal1CesDummyDataByte": aal1CesDummyDataByte,
       "aal1CesStateTable": aal1CesStateTable,
       "aal1CesStateEntry": aal1CesStateEntry,
       "aal1CesAdminState": aal1CesAdminState,
       "aal1CesOperationalState": aal1CesOperationalState,
       "aal1CesUsageState": aal1CesUsageState,
       "aal1CesAvailabilityStatus": aal1CesAvailabilityStatus,
       "aal1CesProceduralStatus": aal1CesProceduralStatus,
       "aal1CesControlStatus": aal1CesControlStatus,
       "aal1CesAlarmStatus": aal1CesAlarmStatus,
       "aal1CesStandbyStatus": aal1CesStandbyStatus,
       "aal1CesUnknownStatus": aal1CesUnknownStatus,
       "aal1CesOperTable": aal1CesOperTable,
       "aal1CesOperEntry": aal1CesOperEntry,
       "aal1CesCellLossStatus": aal1CesCellLossStatus,
       "aal1CesAal1LayerLossStatus": aal1CesAal1LayerLossStatus,
       "aal1CesConnectionStatus": aal1CesConnectionStatus,
       "aal1CesStatsTable": aal1CesStatsTable,
       "aal1CesStatsEntry": aal1CesStatsEntry,
       "aal1CesCellsTransmitted": aal1CesCellsTransmitted,
       "aal1CesCellsReceived": aal1CesCellsReceived,
       "aal1CesLostCells": aal1CesLostCells,
       "aal1CesBufferUnderflows": aal1CesBufferUnderflows,
       "aal1CesBufferOverflows": aal1CesBufferOverflows,
       "aal1CesReassembledCells": aal1CesReassembledCells,
       "aal1CesHeaderErrors": aal1CesHeaderErrors,
       "aal1CesPointerReframes": aal1CesPointerReframes,
       "aal1CesPointerParityErrors": aal1CesPointerParityErrors,
       "aal1CesAal1SequenceErrors": aal1CesAal1SequenceErrors,
       "aal1CesMisinsertedCells": aal1CesMisinsertedCells,
       "circuitEmulationServiceMIB": circuitEmulationServiceMIB,
       "circuitEmulationServiceGroup": circuitEmulationServiceGroup,
       "circuitEmulationServiceGroupBD": circuitEmulationServiceGroupBD,
       "circuitEmulationServiceGroupBD00": circuitEmulationServiceGroupBD00,
       "circuitEmulationServiceGroupBD00A": circuitEmulationServiceGroupBD00A,
       "circuitEmulationServiceCapabilities": circuitEmulationServiceCapabilities,
       "circuitEmulationServiceCapabilitiesBD": circuitEmulationServiceCapabilitiesBD,
       "circuitEmulationServiceCapabilitiesBD00": circuitEmulationServiceCapabilitiesBD00,
       "circuitEmulationServiceCapabilitiesBD00A": circuitEmulationServiceCapabilitiesBD00A}
)
