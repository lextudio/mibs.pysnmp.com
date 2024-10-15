# SNMP MIB module (Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:07 2024
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
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 FixedPoint2,
 Hex,
 IntegerSequence,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "FixedPoint2",
    "Hex",
    "IntegerSequence",
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

_MscAal1Ces_ObjectIdentity = ObjectIdentity
mscAal1Ces = _MscAal1Ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119)
)
_MscAal1CesRowStatusTable_Object = MibTable
mscAal1CesRowStatusTable = _MscAal1CesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 1)
)
if mibBuilder.loadTexts:
    mscAal1CesRowStatusTable.setStatus("mandatory")
_MscAal1CesRowStatusEntry_Object = MibTableRow
mscAal1CesRowStatusEntry = _MscAal1CesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 1, 1)
)
mscAal1CesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesRowStatusEntry.setStatus("mandatory")
_MscAal1CesRowStatus_Type = RowStatus
_MscAal1CesRowStatus_Object = MibTableColumn
mscAal1CesRowStatus = _MscAal1CesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 1, 1, 1),
    _MscAal1CesRowStatus_Type()
)
mscAal1CesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesRowStatus.setStatus("mandatory")
_MscAal1CesComponentName_Type = DisplayString
_MscAal1CesComponentName_Object = MibTableColumn
mscAal1CesComponentName = _MscAal1CesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 1, 1, 2),
    _MscAal1CesComponentName_Type()
)
mscAal1CesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesComponentName.setStatus("mandatory")
_MscAal1CesStorageType_Type = StorageType
_MscAal1CesStorageType_Object = MibTableColumn
mscAal1CesStorageType = _MscAal1CesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 1, 1, 4),
    _MscAal1CesStorageType_Type()
)
mscAal1CesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesStorageType.setStatus("mandatory")


class _MscAal1CesIndex_Type(Integer32):
    """Custom type mscAal1CesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_MscAal1CesIndex_Type.__name__ = "Integer32"
_MscAal1CesIndex_Object = MibTableColumn
mscAal1CesIndex = _MscAal1CesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 1, 1, 10),
    _MscAal1CesIndex_Type()
)
mscAal1CesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAal1CesIndex.setStatus("mandatory")
_MscAal1CesNap_ObjectIdentity = ObjectIdentity
mscAal1CesNap = _MscAal1CesNap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2)
)
_MscAal1CesNapRowStatusTable_Object = MibTable
mscAal1CesNapRowStatusTable = _MscAal1CesNapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 1)
)
if mibBuilder.loadTexts:
    mscAal1CesNapRowStatusTable.setStatus("mandatory")
_MscAal1CesNapRowStatusEntry_Object = MibTableRow
mscAal1CesNapRowStatusEntry = _MscAal1CesNapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 1, 1)
)
mscAal1CesNapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesNapIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesNapRowStatusEntry.setStatus("mandatory")
_MscAal1CesNapRowStatus_Type = RowStatus
_MscAal1CesNapRowStatus_Object = MibTableColumn
mscAal1CesNapRowStatus = _MscAal1CesNapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 1, 1, 1),
    _MscAal1CesNapRowStatus_Type()
)
mscAal1CesNapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesNapRowStatus.setStatus("mandatory")
_MscAal1CesNapComponentName_Type = DisplayString
_MscAal1CesNapComponentName_Object = MibTableColumn
mscAal1CesNapComponentName = _MscAal1CesNapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 1, 1, 2),
    _MscAal1CesNapComponentName_Type()
)
mscAal1CesNapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesNapComponentName.setStatus("mandatory")
_MscAal1CesNapStorageType_Type = StorageType
_MscAal1CesNapStorageType_Object = MibTableColumn
mscAal1CesNapStorageType = _MscAal1CesNapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 1, 1, 4),
    _MscAal1CesNapStorageType_Type()
)
mscAal1CesNapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesNapStorageType.setStatus("mandatory")
_MscAal1CesNapIndex_Type = NonReplicated
_MscAal1CesNapIndex_Object = MibTableColumn
mscAal1CesNapIndex = _MscAal1CesNapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 1, 1, 10),
    _MscAal1CesNapIndex_Type()
)
mscAal1CesNapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAal1CesNapIndex.setStatus("mandatory")
_MscAal1CesNapProvTable_Object = MibTable
mscAal1CesNapProvTable = _MscAal1CesNapProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 10)
)
if mibBuilder.loadTexts:
    mscAal1CesNapProvTable.setStatus("mandatory")
_MscAal1CesNapProvEntry_Object = MibTableRow
mscAal1CesNapProvEntry = _MscAal1CesNapProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 10, 1)
)
mscAal1CesNapProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesNapIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesNapProvEntry.setStatus("mandatory")
_MscAal1CesNapAtmConnection_Type = Link
_MscAal1CesNapAtmConnection_Object = MibTableColumn
mscAal1CesNapAtmConnection = _MscAal1CesNapAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 2, 10, 1, 1),
    _MscAal1CesNapAtmConnection_Type()
)
mscAal1CesNapAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesNapAtmConnection.setStatus("mandatory")
_MscAal1CesAep_ObjectIdentity = ObjectIdentity
mscAal1CesAep = _MscAal1CesAep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3)
)
_MscAal1CesAepRowStatusTable_Object = MibTable
mscAal1CesAepRowStatusTable = _MscAal1CesAepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 1)
)
if mibBuilder.loadTexts:
    mscAal1CesAepRowStatusTable.setStatus("mandatory")
_MscAal1CesAepRowStatusEntry_Object = MibTableRow
mscAal1CesAepRowStatusEntry = _MscAal1CesAepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 1, 1)
)
mscAal1CesAepRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAepRowStatusEntry.setStatus("mandatory")
_MscAal1CesAepRowStatus_Type = RowStatus
_MscAal1CesAepRowStatus_Object = MibTableColumn
mscAal1CesAepRowStatus = _MscAal1CesAepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 1, 1, 1),
    _MscAal1CesAepRowStatus_Type()
)
mscAal1CesAepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepRowStatus.setStatus("mandatory")
_MscAal1CesAepComponentName_Type = DisplayString
_MscAal1CesAepComponentName_Object = MibTableColumn
mscAal1CesAepComponentName = _MscAal1CesAepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 1, 1, 2),
    _MscAal1CesAepComponentName_Type()
)
mscAal1CesAepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepComponentName.setStatus("mandatory")
_MscAal1CesAepStorageType_Type = StorageType
_MscAal1CesAepStorageType_Object = MibTableColumn
mscAal1CesAepStorageType = _MscAal1CesAepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 1, 1, 4),
    _MscAal1CesAepStorageType_Type()
)
mscAal1CesAepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepStorageType.setStatus("mandatory")
_MscAal1CesAepIndex_Type = NonReplicated
_MscAal1CesAepIndex_Object = MibTableColumn
mscAal1CesAepIndex = _MscAal1CesAepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 1, 1, 10),
    _MscAal1CesAepIndex_Type()
)
mscAal1CesAepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAal1CesAepIndex.setStatus("mandatory")
_MscAal1CesAepProvEndPointAddrTable_Object = MibTable
mscAal1CesAepProvEndPointAddrTable = _MscAal1CesAepProvEndPointAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 10)
)
if mibBuilder.loadTexts:
    mscAal1CesAepProvEndPointAddrTable.setStatus("mandatory")
_MscAal1CesAepProvEndPointAddrEntry_Object = MibTableRow
mscAal1CesAepProvEndPointAddrEntry = _MscAal1CesAepProvEndPointAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 10, 1)
)
mscAal1CesAepProvEndPointAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAepProvEndPointAddrEntry.setStatus("mandatory")


class _MscAal1CesAepExpectedRemoteAddress_Type(AsciiString):
    """Custom type mscAal1CesAepExpectedRemoteAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscAal1CesAepExpectedRemoteAddress_Type.__name__ = "AsciiString"
_MscAal1CesAepExpectedRemoteAddress_Object = MibTableColumn
mscAal1CesAepExpectedRemoteAddress = _MscAal1CesAepExpectedRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 10, 1, 1),
    _MscAal1CesAepExpectedRemoteAddress_Type()
)
mscAal1CesAepExpectedRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepExpectedRemoteAddress.setStatus("mandatory")


class _MscAal1CesAepLocalAddress_Type(AsciiString):
    """Custom type mscAal1CesAepLocalAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_MscAal1CesAepLocalAddress_Type.__name__ = "AsciiString"
_MscAal1CesAepLocalAddress_Object = MibTableColumn
mscAal1CesAepLocalAddress = _MscAal1CesAepLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 10, 1, 2),
    _MscAal1CesAepLocalAddress_Type()
)
mscAal1CesAepLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepLocalAddress.setStatus("mandatory")
_MscAal1CesAepProvTable_Object = MibTable
mscAal1CesAepProvTable = _MscAal1CesAepProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11)
)
if mibBuilder.loadTexts:
    mscAal1CesAepProvTable.setStatus("mandatory")
_MscAal1CesAepProvEntry_Object = MibTableRow
mscAal1CesAepProvEntry = _MscAal1CesAepProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1)
)
mscAal1CesAepProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAepProvEntry.setStatus("mandatory")


class _MscAal1CesAepAddressToCall_Type(AsciiString):
    """Custom type mscAal1CesAepAddressToCall based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_MscAal1CesAepAddressToCall_Type.__name__ = "AsciiString"
_MscAal1CesAepAddressToCall_Object = MibTableColumn
mscAal1CesAepAddressToCall = _MscAal1CesAepAddressToCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 1),
    _MscAal1CesAepAddressToCall_Type()
)
mscAal1CesAepAddressToCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepAddressToCall.setStatus("mandatory")


class _MscAal1CesAepRoutingOption_Type(Integer32):
    """Custom type mscAal1CesAepRoutingOption based on Integer32"""
    defaultValue = 0

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
        *(("atmFirst", 3),
          ("atmOnly", 1),
          ("porsFirst", 2),
          ("porsOnly", 0))
    )


_MscAal1CesAepRoutingOption_Type.__name__ = "Integer32"
_MscAal1CesAepRoutingOption_Object = MibTableColumn
mscAal1CesAepRoutingOption = _MscAal1CesAepRoutingOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 2),
    _MscAal1CesAepRoutingOption_Type()
)
mscAal1CesAepRoutingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepRoutingOption.setStatus("mandatory")
_MscAal1CesAepProfile_Type = Link
_MscAal1CesAepProfile_Object = MibTableColumn
mscAal1CesAepProfile = _MscAal1CesAepProfile_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 3),
    _MscAal1CesAepProfile_Type()
)
mscAal1CesAepProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepProfile.setStatus("mandatory")


class _MscAal1CesAepFirstRetryInterval_Type(Unsigned32):
    """Custom type mscAal1CesAepFirstRetryInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscAal1CesAepFirstRetryInterval_Type.__name__ = "Unsigned32"
_MscAal1CesAepFirstRetryInterval_Object = MibTableColumn
mscAal1CesAepFirstRetryInterval = _MscAal1CesAepFirstRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 4),
    _MscAal1CesAepFirstRetryInterval_Type()
)
mscAal1CesAepFirstRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepFirstRetryInterval.setStatus("mandatory")


class _MscAal1CesAepRetryLimit_Type(Unsigned32):
    """Custom type mscAal1CesAepRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAal1CesAepRetryLimit_Type.__name__ = "Unsigned32"
_MscAal1CesAepRetryLimit_Object = MibTableColumn
mscAal1CesAepRetryLimit = _MscAal1CesAepRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 5),
    _MscAal1CesAepRetryLimit_Type()
)
mscAal1CesAepRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepRetryLimit.setStatus("mandatory")


class _MscAal1CesAepActiveEndPointType_Type(Integer32):
    """Custom type mscAal1CesAepActiveEndPointType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("softPVC", 1),
          ("svc", 0))
    )


_MscAal1CesAepActiveEndPointType_Type.__name__ = "Integer32"
_MscAal1CesAepActiveEndPointType_Object = MibTableColumn
mscAal1CesAepActiveEndPointType = _MscAal1CesAepActiveEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 6),
    _MscAal1CesAepActiveEndPointType_Type()
)
mscAal1CesAepActiveEndPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepActiveEndPointType.setStatus("mandatory")


class _MscAal1CesAepCalledVpiVci_Type(IntegerSequence):
    """Custom type mscAal1CesAepCalledVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_MscAal1CesAepCalledVpiVci_Type.__name__ = "IntegerSequence"
_MscAal1CesAepCalledVpiVci_Object = MibTableColumn
mscAal1CesAepCalledVpiVci = _MscAal1CesAepCalledVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 11, 1, 7),
    _MscAal1CesAepCalledVpiVci_Type()
)
mscAal1CesAepCalledVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesAepCalledVpiVci.setStatus("mandatory")
_MscAal1CesAepEpOperTable_Object = MibTable
mscAal1CesAepEpOperTable = _MscAal1CesAepEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 12)
)
if mibBuilder.loadTexts:
    mscAal1CesAepEpOperTable.setStatus("mandatory")
_MscAal1CesAepEpOperEntry_Object = MibTableRow
mscAal1CesAepEpOperEntry = _MscAal1CesAepEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 12, 1)
)
mscAal1CesAepEpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAepEpOperEntry.setStatus("mandatory")


class _MscAal1CesAepRemoteAddress_Type(AsciiString):
    """Custom type mscAal1CesAepRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_MscAal1CesAepRemoteAddress_Type.__name__ = "AsciiString"
_MscAal1CesAepRemoteAddress_Object = MibTableColumn
mscAal1CesAepRemoteAddress = _MscAal1CesAepRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 12, 1, 1),
    _MscAal1CesAepRemoteAddress_Type()
)
mscAal1CesAepRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepRemoteAddress.setStatus("mandatory")


class _MscAal1CesAepLastTearDownCause_Type(Unsigned32):
    """Custom type mscAal1CesAepLastTearDownCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAal1CesAepLastTearDownCause_Type.__name__ = "Unsigned32"
_MscAal1CesAepLastTearDownCause_Object = MibTableColumn
mscAal1CesAepLastTearDownCause = _MscAal1CesAepLastTearDownCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 12, 1, 2),
    _MscAal1CesAepLastTearDownCause_Type()
)
mscAal1CesAepLastTearDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepLastTearDownCause.setStatus("mandatory")


class _MscAal1CesAepLastTearDownDiagnostic_Type(AsciiString):
    """Custom type mscAal1CesAepLastTearDownDiagnostic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscAal1CesAepLastTearDownDiagnostic_Type.__name__ = "AsciiString"
_MscAal1CesAepLastTearDownDiagnostic_Object = MibTableColumn
mscAal1CesAepLastTearDownDiagnostic = _MscAal1CesAepLastTearDownDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 12, 1, 3),
    _MscAal1CesAepLastTearDownDiagnostic_Type()
)
mscAal1CesAepLastTearDownDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepLastTearDownDiagnostic.setStatus("mandatory")
_MscAal1CesAepOutTable_Object = MibTable
mscAal1CesAepOutTable = _MscAal1CesAepOutTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13)
)
if mibBuilder.loadTexts:
    mscAal1CesAepOutTable.setStatus("mandatory")
_MscAal1CesAepOutEntry_Object = MibTableRow
mscAal1CesAepOutEntry = _MscAal1CesAepOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13, 1)
)
mscAal1CesAepOutEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAepOutEntry.setStatus("mandatory")


class _MscAal1CesAepSvcStatus_Type(Integer32):
    """Custom type mscAal1CesAepSvcStatus based on Integer32"""
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


_MscAal1CesAepSvcStatus_Type.__name__ = "Integer32"
_MscAal1CesAepSvcStatus_Object = MibTableColumn
mscAal1CesAepSvcStatus = _MscAal1CesAepSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13, 1, 1),
    _MscAal1CesAepSvcStatus_Type()
)
mscAal1CesAepSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepSvcStatus.setStatus("mandatory")


class _MscAal1CesAepLastSetupFailureCause_Type(Unsigned32):
    """Custom type mscAal1CesAepLastSetupFailureCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAal1CesAepLastSetupFailureCause_Type.__name__ = "Unsigned32"
_MscAal1CesAepLastSetupFailureCause_Object = MibTableColumn
mscAal1CesAepLastSetupFailureCause = _MscAal1CesAepLastSetupFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13, 1, 2),
    _MscAal1CesAepLastSetupFailureCause_Type()
)
mscAal1CesAepLastSetupFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepLastSetupFailureCause.setStatus("mandatory")


class _MscAal1CesAepLastSetupFailureDiagnostic_Type(AsciiString):
    """Custom type mscAal1CesAepLastSetupFailureDiagnostic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscAal1CesAepLastSetupFailureDiagnostic_Type.__name__ = "AsciiString"
_MscAal1CesAepLastSetupFailureDiagnostic_Object = MibTableColumn
mscAal1CesAepLastSetupFailureDiagnostic = _MscAal1CesAepLastSetupFailureDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13, 1, 3),
    _MscAal1CesAepLastSetupFailureDiagnostic_Type()
)
mscAal1CesAepLastSetupFailureDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepLastSetupFailureDiagnostic.setStatus("mandatory")
_MscAal1CesAepRetryTimeRemaining_Type = Counter32
_MscAal1CesAepRetryTimeRemaining_Object = MibTableColumn
mscAal1CesAepRetryTimeRemaining = _MscAal1CesAepRetryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13, 1, 4),
    _MscAal1CesAepRetryTimeRemaining_Type()
)
mscAal1CesAepRetryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepRetryTimeRemaining.setStatus("mandatory")
_MscAal1CesAepRetryFailures_Type = Counter32
_MscAal1CesAepRetryFailures_Object = MibTableColumn
mscAal1CesAepRetryFailures = _MscAal1CesAepRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 3, 13, 1, 5),
    _MscAal1CesAepRetryFailures_Type()
)
mscAal1CesAepRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAepRetryFailures.setStatus("mandatory")
_MscAal1CesPep_ObjectIdentity = ObjectIdentity
mscAal1CesPep = _MscAal1CesPep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4)
)
_MscAal1CesPepRowStatusTable_Object = MibTable
mscAal1CesPepRowStatusTable = _MscAal1CesPepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 1)
)
if mibBuilder.loadTexts:
    mscAal1CesPepRowStatusTable.setStatus("mandatory")
_MscAal1CesPepRowStatusEntry_Object = MibTableRow
mscAal1CesPepRowStatusEntry = _MscAal1CesPepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 1, 1)
)
mscAal1CesPepRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesPepRowStatusEntry.setStatus("mandatory")
_MscAal1CesPepRowStatus_Type = RowStatus
_MscAal1CesPepRowStatus_Object = MibTableColumn
mscAal1CesPepRowStatus = _MscAal1CesPepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 1, 1, 1),
    _MscAal1CesPepRowStatus_Type()
)
mscAal1CesPepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesPepRowStatus.setStatus("mandatory")
_MscAal1CesPepComponentName_Type = DisplayString
_MscAal1CesPepComponentName_Object = MibTableColumn
mscAal1CesPepComponentName = _MscAal1CesPepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 1, 1, 2),
    _MscAal1CesPepComponentName_Type()
)
mscAal1CesPepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPepComponentName.setStatus("mandatory")
_MscAal1CesPepStorageType_Type = StorageType
_MscAal1CesPepStorageType_Object = MibTableColumn
mscAal1CesPepStorageType = _MscAal1CesPepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 1, 1, 4),
    _MscAal1CesPepStorageType_Type()
)
mscAal1CesPepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPepStorageType.setStatus("mandatory")
_MscAal1CesPepIndex_Type = NonReplicated
_MscAal1CesPepIndex_Object = MibTableColumn
mscAal1CesPepIndex = _MscAal1CesPepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 1, 1, 10),
    _MscAal1CesPepIndex_Type()
)
mscAal1CesPepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAal1CesPepIndex.setStatus("mandatory")
_MscAal1CesPepProvEndPointAddrTable_Object = MibTable
mscAal1CesPepProvEndPointAddrTable = _MscAal1CesPepProvEndPointAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 10)
)
if mibBuilder.loadTexts:
    mscAal1CesPepProvEndPointAddrTable.setStatus("mandatory")
_MscAal1CesPepProvEndPointAddrEntry_Object = MibTableRow
mscAal1CesPepProvEndPointAddrEntry = _MscAal1CesPepProvEndPointAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 10, 1)
)
mscAal1CesPepProvEndPointAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesPepProvEndPointAddrEntry.setStatus("mandatory")


class _MscAal1CesPepExpectedRemoteAddress_Type(AsciiString):
    """Custom type mscAal1CesPepExpectedRemoteAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscAal1CesPepExpectedRemoteAddress_Type.__name__ = "AsciiString"
_MscAal1CesPepExpectedRemoteAddress_Object = MibTableColumn
mscAal1CesPepExpectedRemoteAddress = _MscAal1CesPepExpectedRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 10, 1, 1),
    _MscAal1CesPepExpectedRemoteAddress_Type()
)
mscAal1CesPepExpectedRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesPepExpectedRemoteAddress.setStatus("mandatory")


class _MscAal1CesPepLocalAddress_Type(AsciiString):
    """Custom type mscAal1CesPepLocalAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_MscAal1CesPepLocalAddress_Type.__name__ = "AsciiString"
_MscAal1CesPepLocalAddress_Object = MibTableColumn
mscAal1CesPepLocalAddress = _MscAal1CesPepLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 10, 1, 2),
    _MscAal1CesPepLocalAddress_Type()
)
mscAal1CesPepLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesPepLocalAddress.setStatus("mandatory")
_MscAal1CesPepEpOperTable_Object = MibTable
mscAal1CesPepEpOperTable = _MscAal1CesPepEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 11)
)
if mibBuilder.loadTexts:
    mscAal1CesPepEpOperTable.setStatus("mandatory")
_MscAal1CesPepEpOperEntry_Object = MibTableRow
mscAal1CesPepEpOperEntry = _MscAal1CesPepEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 11, 1)
)
mscAal1CesPepEpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesPepEpOperEntry.setStatus("mandatory")


class _MscAal1CesPepRemoteAddress_Type(AsciiString):
    """Custom type mscAal1CesPepRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_MscAal1CesPepRemoteAddress_Type.__name__ = "AsciiString"
_MscAal1CesPepRemoteAddress_Object = MibTableColumn
mscAal1CesPepRemoteAddress = _MscAal1CesPepRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 11, 1, 1),
    _MscAal1CesPepRemoteAddress_Type()
)
mscAal1CesPepRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPepRemoteAddress.setStatus("mandatory")


class _MscAal1CesPepLastTearDownCause_Type(Unsigned32):
    """Custom type mscAal1CesPepLastTearDownCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAal1CesPepLastTearDownCause_Type.__name__ = "Unsigned32"
_MscAal1CesPepLastTearDownCause_Object = MibTableColumn
mscAal1CesPepLastTearDownCause = _MscAal1CesPepLastTearDownCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 11, 1, 2),
    _MscAal1CesPepLastTearDownCause_Type()
)
mscAal1CesPepLastTearDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPepLastTearDownCause.setStatus("mandatory")


class _MscAal1CesPepLastTearDownDiagnostic_Type(AsciiString):
    """Custom type mscAal1CesPepLastTearDownDiagnostic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscAal1CesPepLastTearDownDiagnostic_Type.__name__ = "AsciiString"
_MscAal1CesPepLastTearDownDiagnostic_Object = MibTableColumn
mscAal1CesPepLastTearDownDiagnostic = _MscAal1CesPepLastTearDownDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 11, 1, 3),
    _MscAal1CesPepLastTearDownDiagnostic_Type()
)
mscAal1CesPepLastTearDownDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPepLastTearDownDiagnostic.setStatus("mandatory")
_MscAal1CesPepPassiveOperTable_Object = MibTable
mscAal1CesPepPassiveOperTable = _MscAal1CesPepPassiveOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 12)
)
if mibBuilder.loadTexts:
    mscAal1CesPepPassiveOperTable.setStatus("mandatory")
_MscAal1CesPepPassiveOperEntry_Object = MibTableRow
mscAal1CesPepPassiveOperEntry = _MscAal1CesPepPassiveOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 12, 1)
)
mscAal1CesPepPassiveOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesPepIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesPepPassiveOperEntry.setStatus("mandatory")


class _MscAal1CesPepSvcStatus_Type(Integer32):
    """Custom type mscAal1CesPepSvcStatus based on Integer32"""
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


_MscAal1CesPepSvcStatus_Type.__name__ = "Integer32"
_MscAal1CesPepSvcStatus_Object = MibTableColumn
mscAal1CesPepSvcStatus = _MscAal1CesPepSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 4, 12, 1, 1),
    _MscAal1CesPepSvcStatus_Type()
)
mscAal1CesPepSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPepSvcStatus.setStatus("mandatory")
_MscAal1CesLCo_ObjectIdentity = ObjectIdentity
mscAal1CesLCo = _MscAal1CesLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5)
)
_MscAal1CesLCoRowStatusTable_Object = MibTable
mscAal1CesLCoRowStatusTable = _MscAal1CesLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 1)
)
if mibBuilder.loadTexts:
    mscAal1CesLCoRowStatusTable.setStatus("mandatory")
_MscAal1CesLCoRowStatusEntry_Object = MibTableRow
mscAal1CesLCoRowStatusEntry = _MscAal1CesLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 1, 1)
)
mscAal1CesLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesLCoIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesLCoRowStatusEntry.setStatus("mandatory")
_MscAal1CesLCoRowStatus_Type = RowStatus
_MscAal1CesLCoRowStatus_Object = MibTableColumn
mscAal1CesLCoRowStatus = _MscAal1CesLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 1, 1, 1),
    _MscAal1CesLCoRowStatus_Type()
)
mscAal1CesLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRowStatus.setStatus("mandatory")
_MscAal1CesLCoComponentName_Type = DisplayString
_MscAal1CesLCoComponentName_Object = MibTableColumn
mscAal1CesLCoComponentName = _MscAal1CesLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 1, 1, 2),
    _MscAal1CesLCoComponentName_Type()
)
mscAal1CesLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoComponentName.setStatus("mandatory")
_MscAal1CesLCoStorageType_Type = StorageType
_MscAal1CesLCoStorageType_Object = MibTableColumn
mscAal1CesLCoStorageType = _MscAal1CesLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 1, 1, 4),
    _MscAal1CesLCoStorageType_Type()
)
mscAal1CesLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoStorageType.setStatus("mandatory")
_MscAal1CesLCoIndex_Type = NonReplicated
_MscAal1CesLCoIndex_Object = MibTableColumn
mscAal1CesLCoIndex = _MscAal1CesLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 1, 1, 10),
    _MscAal1CesLCoIndex_Type()
)
mscAal1CesLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAal1CesLCoIndex.setStatus("mandatory")
_MscAal1CesLCoPathDataTable_Object = MibTable
mscAal1CesLCoPathDataTable = _MscAal1CesLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10)
)
if mibBuilder.loadTexts:
    mscAal1CesLCoPathDataTable.setStatus("mandatory")
_MscAal1CesLCoPathDataEntry_Object = MibTableRow
mscAal1CesLCoPathDataEntry = _MscAal1CesLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1)
)
mscAal1CesLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesLCoIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesLCoPathDataEntry.setStatus("mandatory")


class _MscAal1CesLCoState_Type(Integer32):
    """Custom type mscAal1CesLCoState based on Integer32"""
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


_MscAal1CesLCoState_Type.__name__ = "Integer32"
_MscAal1CesLCoState_Object = MibTableColumn
mscAal1CesLCoState = _MscAal1CesLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 1),
    _MscAal1CesLCoState_Type()
)
mscAal1CesLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoState.setStatus("mandatory")


class _MscAal1CesLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscAal1CesLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscAal1CesLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscAal1CesLCoOverrideRemoteName_Object = MibTableColumn
mscAal1CesLCoOverrideRemoteName = _MscAal1CesLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 2),
    _MscAal1CesLCoOverrideRemoteName_Type()
)
mscAal1CesLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesLCoOverrideRemoteName.setStatus("mandatory")


class _MscAal1CesLCoEnd_Type(Integer32):
    """Custom type mscAal1CesLCoEnd based on Integer32"""
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


_MscAal1CesLCoEnd_Type.__name__ = "Integer32"
_MscAal1CesLCoEnd_Object = MibTableColumn
mscAal1CesLCoEnd = _MscAal1CesLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 3),
    _MscAal1CesLCoEnd_Type()
)
mscAal1CesLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoEnd.setStatus("mandatory")


class _MscAal1CesLCoCostMetric_Type(Unsigned32):
    """Custom type mscAal1CesLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAal1CesLCoCostMetric_Type.__name__ = "Unsigned32"
_MscAal1CesLCoCostMetric_Object = MibTableColumn
mscAal1CesLCoCostMetric = _MscAal1CesLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 4),
    _MscAal1CesLCoCostMetric_Type()
)
mscAal1CesLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoCostMetric.setStatus("mandatory")


class _MscAal1CesLCoDelayMetric_Type(Unsigned32):
    """Custom type mscAal1CesLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscAal1CesLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscAal1CesLCoDelayMetric_Object = MibTableColumn
mscAal1CesLCoDelayMetric = _MscAal1CesLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 5),
    _MscAal1CesLCoDelayMetric_Type()
)
mscAal1CesLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoDelayMetric.setStatus("mandatory")


class _MscAal1CesLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscAal1CesLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscAal1CesLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscAal1CesLCoRoundTripDelay_Object = MibTableColumn
mscAal1CesLCoRoundTripDelay = _MscAal1CesLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 6),
    _MscAal1CesLCoRoundTripDelay_Type()
)
mscAal1CesLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRoundTripDelay.setStatus("mandatory")


class _MscAal1CesLCoSetupPriority_Type(Unsigned32):
    """Custom type mscAal1CesLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscAal1CesLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscAal1CesLCoSetupPriority_Object = MibTableColumn
mscAal1CesLCoSetupPriority = _MscAal1CesLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 7),
    _MscAal1CesLCoSetupPriority_Type()
)
mscAal1CesLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoSetupPriority.setStatus("mandatory")


class _MscAal1CesLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscAal1CesLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscAal1CesLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscAal1CesLCoHoldingPriority_Object = MibTableColumn
mscAal1CesLCoHoldingPriority = _MscAal1CesLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 8),
    _MscAal1CesLCoHoldingPriority_Type()
)
mscAal1CesLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoHoldingPriority.setStatus("mandatory")


class _MscAal1CesLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscAal1CesLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAal1CesLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscAal1CesLCoRequiredTxBandwidth_Object = MibTableColumn
mscAal1CesLCoRequiredTxBandwidth = _MscAal1CesLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 9),
    _MscAal1CesLCoRequiredTxBandwidth_Type()
)
mscAal1CesLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscAal1CesLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscAal1CesLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAal1CesLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscAal1CesLCoRequiredRxBandwidth_Object = MibTableColumn
mscAal1CesLCoRequiredRxBandwidth = _MscAal1CesLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 10),
    _MscAal1CesLCoRequiredRxBandwidth_Type()
)
mscAal1CesLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscAal1CesLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscAal1CesLCoRequiredTrafficType based on Integer32"""
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


_MscAal1CesLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscAal1CesLCoRequiredTrafficType_Object = MibTableColumn
mscAal1CesLCoRequiredTrafficType = _MscAal1CesLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 11),
    _MscAal1CesLCoRequiredTrafficType_Type()
)
mscAal1CesLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRequiredTrafficType.setStatus("mandatory")


class _MscAal1CesLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscAal1CesLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAal1CesLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscAal1CesLCoPermittedTrunkTypes_Object = MibTableColumn
mscAal1CesLCoPermittedTrunkTypes = _MscAal1CesLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 12),
    _MscAal1CesLCoPermittedTrunkTypes_Type()
)
mscAal1CesLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscAal1CesLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscAal1CesLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscAal1CesLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscAal1CesLCoRequiredSecurity_Object = MibTableColumn
mscAal1CesLCoRequiredSecurity = _MscAal1CesLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 13),
    _MscAal1CesLCoRequiredSecurity_Type()
)
mscAal1CesLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRequiredSecurity.setStatus("mandatory")


class _MscAal1CesLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscAal1CesLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscAal1CesLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscAal1CesLCoRequiredCustomerParameter_Object = MibTableColumn
mscAal1CesLCoRequiredCustomerParameter = _MscAal1CesLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 14),
    _MscAal1CesLCoRequiredCustomerParameter_Type()
)
mscAal1CesLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscAal1CesLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscAal1CesLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscAal1CesLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscAal1CesLCoEmissionPriority_Object = MibTableColumn
mscAal1CesLCoEmissionPriority = _MscAal1CesLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 15),
    _MscAal1CesLCoEmissionPriority_Type()
)
mscAal1CesLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoEmissionPriority.setStatus("mandatory")


class _MscAal1CesLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscAal1CesLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscAal1CesLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscAal1CesLCoDiscardPriority_Object = MibTableColumn
mscAal1CesLCoDiscardPriority = _MscAal1CesLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 16),
    _MscAal1CesLCoDiscardPriority_Type()
)
mscAal1CesLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoDiscardPriority.setStatus("mandatory")


class _MscAal1CesLCoPathType_Type(Integer32):
    """Custom type mscAal1CesLCoPathType based on Integer32"""
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


_MscAal1CesLCoPathType_Type.__name__ = "Integer32"
_MscAal1CesLCoPathType_Object = MibTableColumn
mscAal1CesLCoPathType = _MscAal1CesLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 17),
    _MscAal1CesLCoPathType_Type()
)
mscAal1CesLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPathType.setStatus("mandatory")


class _MscAal1CesLCoRetryCount_Type(Unsigned32):
    """Custom type mscAal1CesLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAal1CesLCoRetryCount_Type.__name__ = "Unsigned32"
_MscAal1CesLCoRetryCount_Object = MibTableColumn
mscAal1CesLCoRetryCount = _MscAal1CesLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 18),
    _MscAal1CesLCoRetryCount_Type()
)
mscAal1CesLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoRetryCount.setStatus("mandatory")


class _MscAal1CesLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscAal1CesLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAal1CesLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscAal1CesLCoPathFailureCount_Object = MibTableColumn
mscAal1CesLCoPathFailureCount = _MscAal1CesLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 19),
    _MscAal1CesLCoPathFailureCount_Type()
)
mscAal1CesLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPathFailureCount.setStatus("mandatory")


class _MscAal1CesLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscAal1CesLCoReasonForNoRoute based on Integer32"""
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


_MscAal1CesLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscAal1CesLCoReasonForNoRoute_Object = MibTableColumn
mscAal1CesLCoReasonForNoRoute = _MscAal1CesLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 20),
    _MscAal1CesLCoReasonForNoRoute_Type()
)
mscAal1CesLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoReasonForNoRoute.setStatus("mandatory")


class _MscAal1CesLCoLastTearDownReason_Type(Integer32):
    """Custom type mscAal1CesLCoLastTearDownReason based on Integer32"""
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


_MscAal1CesLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscAal1CesLCoLastTearDownReason_Object = MibTableColumn
mscAal1CesLCoLastTearDownReason = _MscAal1CesLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 21),
    _MscAal1CesLCoLastTearDownReason_Type()
)
mscAal1CesLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoLastTearDownReason.setStatus("mandatory")


class _MscAal1CesLCoPathFailureAction_Type(Integer32):
    """Custom type mscAal1CesLCoPathFailureAction based on Integer32"""
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


_MscAal1CesLCoPathFailureAction_Type.__name__ = "Integer32"
_MscAal1CesLCoPathFailureAction_Object = MibTableColumn
mscAal1CesLCoPathFailureAction = _MscAal1CesLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 22),
    _MscAal1CesLCoPathFailureAction_Type()
)
mscAal1CesLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPathFailureAction.setStatus("mandatory")


class _MscAal1CesLCoBumpPreference_Type(Integer32):
    """Custom type mscAal1CesLCoBumpPreference based on Integer32"""
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


_MscAal1CesLCoBumpPreference_Type.__name__ = "Integer32"
_MscAal1CesLCoBumpPreference_Object = MibTableColumn
mscAal1CesLCoBumpPreference = _MscAal1CesLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 23),
    _MscAal1CesLCoBumpPreference_Type()
)
mscAal1CesLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoBumpPreference.setStatus("mandatory")


class _MscAal1CesLCoOptimization_Type(Integer32):
    """Custom type mscAal1CesLCoOptimization based on Integer32"""
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


_MscAal1CesLCoOptimization_Type.__name__ = "Integer32"
_MscAal1CesLCoOptimization_Object = MibTableColumn
mscAal1CesLCoOptimization = _MscAal1CesLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 24),
    _MscAal1CesLCoOptimization_Type()
)
mscAal1CesLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoOptimization.setStatus("mandatory")


class _MscAal1CesLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscAal1CesLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscAal1CesLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscAal1CesLCoPathUpDateTime_Object = MibTableColumn
mscAal1CesLCoPathUpDateTime = _MscAal1CesLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 10, 1, 25),
    _MscAal1CesLCoPathUpDateTime_Type()
)
mscAal1CesLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPathUpDateTime.setStatus("mandatory")
_MscAal1CesLCoStatsTable_Object = MibTable
mscAal1CesLCoStatsTable = _MscAal1CesLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 11)
)
if mibBuilder.loadTexts:
    mscAal1CesLCoStatsTable.setStatus("mandatory")
_MscAal1CesLCoStatsEntry_Object = MibTableRow
mscAal1CesLCoStatsEntry = _MscAal1CesLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 11, 1)
)
mscAal1CesLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesLCoIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesLCoStatsEntry.setStatus("mandatory")
_MscAal1CesLCoPktsToNetwork_Type = PassportCounter64
_MscAal1CesLCoPktsToNetwork_Object = MibTableColumn
mscAal1CesLCoPktsToNetwork = _MscAal1CesLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 11, 1, 1),
    _MscAal1CesLCoPktsToNetwork_Type()
)
mscAal1CesLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPktsToNetwork.setStatus("mandatory")
_MscAal1CesLCoBytesToNetwork_Type = PassportCounter64
_MscAal1CesLCoBytesToNetwork_Object = MibTableColumn
mscAal1CesLCoBytesToNetwork = _MscAal1CesLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 11, 1, 2),
    _MscAal1CesLCoBytesToNetwork_Type()
)
mscAal1CesLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoBytesToNetwork.setStatus("mandatory")
_MscAal1CesLCoPktsFromNetwork_Type = PassportCounter64
_MscAal1CesLCoPktsFromNetwork_Object = MibTableColumn
mscAal1CesLCoPktsFromNetwork = _MscAal1CesLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 11, 1, 3),
    _MscAal1CesLCoPktsFromNetwork_Type()
)
mscAal1CesLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPktsFromNetwork.setStatus("mandatory")
_MscAal1CesLCoBytesFromNetwork_Type = PassportCounter64
_MscAal1CesLCoBytesFromNetwork_Object = MibTableColumn
mscAal1CesLCoBytesFromNetwork = _MscAal1CesLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 11, 1, 4),
    _MscAal1CesLCoBytesFromNetwork_Type()
)
mscAal1CesLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoBytesFromNetwork.setStatus("mandatory")
_MscAal1CesLCoPathTable_Object = MibTable
mscAal1CesLCoPathTable = _MscAal1CesLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 264)
)
if mibBuilder.loadTexts:
    mscAal1CesLCoPathTable.setStatus("mandatory")
_MscAal1CesLCoPathEntry_Object = MibTableRow
mscAal1CesLCoPathEntry = _MscAal1CesLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 264, 1)
)
mscAal1CesLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscAal1CesLCoPathEntry.setStatus("mandatory")


class _MscAal1CesLCoPathValue_Type(AsciiString):
    """Custom type mscAal1CesLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscAal1CesLCoPathValue_Type.__name__ = "AsciiString"
_MscAal1CesLCoPathValue_Object = MibTableColumn
mscAal1CesLCoPathValue = _MscAal1CesLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 5, 264, 1, 1),
    _MscAal1CesLCoPathValue_Type()
)
mscAal1CesLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLCoPathValue.setStatus("mandatory")
_MscAal1CesAtmCon_ObjectIdentity = ObjectIdentity
mscAal1CesAtmCon = _MscAal1CesAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6)
)
_MscAal1CesAtmConRowStatusTable_Object = MibTable
mscAal1CesAtmConRowStatusTable = _MscAal1CesAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 1)
)
if mibBuilder.loadTexts:
    mscAal1CesAtmConRowStatusTable.setStatus("mandatory")
_MscAal1CesAtmConRowStatusEntry_Object = MibTableRow
mscAal1CesAtmConRowStatusEntry = _MscAal1CesAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 1, 1)
)
mscAal1CesAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAtmConRowStatusEntry.setStatus("mandatory")
_MscAal1CesAtmConRowStatus_Type = RowStatus
_MscAal1CesAtmConRowStatus_Object = MibTableColumn
mscAal1CesAtmConRowStatus = _MscAal1CesAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 1, 1, 1),
    _MscAal1CesAtmConRowStatus_Type()
)
mscAal1CesAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAtmConRowStatus.setStatus("mandatory")
_MscAal1CesAtmConComponentName_Type = DisplayString
_MscAal1CesAtmConComponentName_Object = MibTableColumn
mscAal1CesAtmConComponentName = _MscAal1CesAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 1, 1, 2),
    _MscAal1CesAtmConComponentName_Type()
)
mscAal1CesAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAtmConComponentName.setStatus("mandatory")
_MscAal1CesAtmConStorageType_Type = StorageType
_MscAal1CesAtmConStorageType_Object = MibTableColumn
mscAal1CesAtmConStorageType = _MscAal1CesAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 1, 1, 4),
    _MscAal1CesAtmConStorageType_Type()
)
mscAal1CesAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAtmConStorageType.setStatus("mandatory")
_MscAal1CesAtmConIndex_Type = NonReplicated
_MscAal1CesAtmConIndex_Object = MibTableColumn
mscAal1CesAtmConIndex = _MscAal1CesAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 1, 1, 10),
    _MscAal1CesAtmConIndex_Type()
)
mscAal1CesAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAal1CesAtmConIndex.setStatus("mandatory")
_MscAal1CesAtmConOperTable_Object = MibTable
mscAal1CesAtmConOperTable = _MscAal1CesAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 10)
)
if mibBuilder.loadTexts:
    mscAal1CesAtmConOperTable.setStatus("mandatory")
_MscAal1CesAtmConOperEntry_Object = MibTableRow
mscAal1CesAtmConOperEntry = _MscAal1CesAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 10, 1)
)
mscAal1CesAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesAtmConOperEntry.setStatus("mandatory")
_MscAal1CesAtmConNextHop_Type = RowPointer
_MscAal1CesAtmConNextHop_Object = MibTableColumn
mscAal1CesAtmConNextHop = _MscAal1CesAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 6, 10, 1, 1),
    _MscAal1CesAtmConNextHop_Type()
)
mscAal1CesAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAtmConNextHop.setStatus("mandatory")
_MscAal1CesCidDataTable_Object = MibTable
mscAal1CesCidDataTable = _MscAal1CesCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 10)
)
if mibBuilder.loadTexts:
    mscAal1CesCidDataTable.setStatus("mandatory")
_MscAal1CesCidDataEntry_Object = MibTableRow
mscAal1CesCidDataEntry = _MscAal1CesCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 10, 1)
)
mscAal1CesCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesCidDataEntry.setStatus("mandatory")


class _MscAal1CesCustomerIdentifier_Type(Unsigned32):
    """Custom type mscAal1CesCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscAal1CesCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscAal1CesCustomerIdentifier_Object = MibTableColumn
mscAal1CesCustomerIdentifier = _MscAal1CesCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 10, 1, 1),
    _MscAal1CesCustomerIdentifier_Type()
)
mscAal1CesCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesCustomerIdentifier.setStatus("mandatory")
_MscAal1CesProvTable_Object = MibTable
mscAal1CesProvTable = _MscAal1CesProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11)
)
if mibBuilder.loadTexts:
    mscAal1CesProvTable.setStatus("mandatory")
_MscAal1CesProvEntry_Object = MibTableRow
mscAal1CesProvEntry = _MscAal1CesProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1)
)
mscAal1CesProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesProvEntry.setStatus("mandatory")


class _MscAal1CesServiceType_Type(Integer32):
    """Custom type mscAal1CesServiceType based on Integer32"""
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


_MscAal1CesServiceType_Type.__name__ = "Integer32"
_MscAal1CesServiceType_Object = MibTableColumn
mscAal1CesServiceType = _MscAal1CesServiceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 1),
    _MscAal1CesServiceType_Type()
)
mscAal1CesServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesServiceType.setStatus("mandatory")


class _MscAal1CesBufferSize_Type(Unsigned32):
    """Custom type mscAal1CesBufferSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(94, 15651),
    )


_MscAal1CesBufferSize_Type.__name__ = "Unsigned32"
_MscAal1CesBufferSize_Object = MibTableColumn
mscAal1CesBufferSize = _MscAal1CesBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 2),
    _MscAal1CesBufferSize_Type()
)
mscAal1CesBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesBufferSize.setStatus("mandatory")


class _MscAal1CesCellLossIntegrationPeriod_Type(Unsigned32):
    """Custom type mscAal1CesCellLossIntegrationPeriod based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_MscAal1CesCellLossIntegrationPeriod_Type.__name__ = "Unsigned32"
_MscAal1CesCellLossIntegrationPeriod_Object = MibTableColumn
mscAal1CesCellLossIntegrationPeriod = _MscAal1CesCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 4),
    _MscAal1CesCellLossIntegrationPeriod_Type()
)
mscAal1CesCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesCellLossIntegrationPeriod.setStatus("mandatory")
_MscAal1CesInterfaceName_Type = Link
_MscAal1CesInterfaceName_Object = MibTableColumn
mscAal1CesInterfaceName = _MscAal1CesInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 5),
    _MscAal1CesInterfaceName_Type()
)
mscAal1CesInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesInterfaceName.setStatus("mandatory")


class _MscAal1CesPartialFill_Type(Unsigned32):
    """Custom type mscAal1CesPartialFill based on Unsigned32"""
    defaultValue = 47

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 47),
    )


_MscAal1CesPartialFill_Type.__name__ = "Unsigned32"
_MscAal1CesPartialFill_Object = MibTableColumn
mscAal1CesPartialFill = _MscAal1CesPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 6),
    _MscAal1CesPartialFill_Type()
)
mscAal1CesPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesPartialFill.setStatus("mandatory")


class _MscAal1CesIdleSuppression_Type(Integer32):
    """Custom type mscAal1CesIdleSuppression based on Integer32"""
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


_MscAal1CesIdleSuppression_Type.__name__ = "Integer32"
_MscAal1CesIdleSuppression_Object = MibTableColumn
mscAal1CesIdleSuppression = _MscAal1CesIdleSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 7),
    _MscAal1CesIdleSuppression_Type()
)
mscAal1CesIdleSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesIdleSuppression.setStatus("mandatory")


class _MscAal1CesIdlePattern_Type(Hex):
    """Custom type mscAal1CesIdlePattern based on Hex"""
    defaultValue = 126

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAal1CesIdlePattern_Type.__name__ = "Hex"
_MscAal1CesIdlePattern_Object = MibTableColumn
mscAal1CesIdlePattern = _MscAal1CesIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 8),
    _MscAal1CesIdlePattern_Type()
)
mscAal1CesIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesIdlePattern.setStatus("mandatory")


class _MscAal1CesCellLossRecoveryPeriod_Type(Unsigned32):
    """Custom type mscAal1CesCellLossRecoveryPeriod based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MscAal1CesCellLossRecoveryPeriod_Type.__name__ = "Unsigned32"
_MscAal1CesCellLossRecoveryPeriod_Object = MibTableColumn
mscAal1CesCellLossRecoveryPeriod = _MscAal1CesCellLossRecoveryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 9),
    _MscAal1CesCellLossRecoveryPeriod_Type()
)
mscAal1CesCellLossRecoveryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesCellLossRecoveryPeriod.setStatus("mandatory")


class _MscAal1CesDummyDataByte_Type(Hex):
    """Custom type mscAal1CesDummyDataByte based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAal1CesDummyDataByte_Type.__name__ = "Hex"
_MscAal1CesDummyDataByte_Object = MibTableColumn
mscAal1CesDummyDataByte = _MscAal1CesDummyDataByte_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 10),
    _MscAal1CesDummyDataByte_Type()
)
mscAal1CesDummyDataByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesDummyDataByte.setStatus("mandatory")


class _MscAal1CesMaximumBufferDelay_Type(FixedPoint2):
    """Custom type mscAal1CesMaximumBufferDelay based on FixedPoint2"""
    defaultValue = 0

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65500),
    )


_MscAal1CesMaximumBufferDelay_Type.__name__ = "FixedPoint2"
_MscAal1CesMaximumBufferDelay_Object = MibTableColumn
mscAal1CesMaximumBufferDelay = _MscAal1CesMaximumBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 11),
    _MscAal1CesMaximumBufferDelay_Type()
)
mscAal1CesMaximumBufferDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesMaximumBufferDelay.setStatus("mandatory")


class _MscAal1CesDp2CellDelayVariationTolerance_Type(FixedPoint2):
    """Custom type mscAal1CesDp2CellDelayVariationTolerance based on FixedPoint2"""
    defaultValue = 100

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_MscAal1CesDp2CellDelayVariationTolerance_Type.__name__ = "FixedPoint2"
_MscAal1CesDp2CellDelayVariationTolerance_Object = MibTableColumn
mscAal1CesDp2CellDelayVariationTolerance = _MscAal1CesDp2CellDelayVariationTolerance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 11, 1, 12),
    _MscAal1CesDp2CellDelayVariationTolerance_Type()
)
mscAal1CesDp2CellDelayVariationTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAal1CesDp2CellDelayVariationTolerance.setStatus("mandatory")
_MscAal1CesStateTable_Object = MibTable
mscAal1CesStateTable = _MscAal1CesStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12)
)
if mibBuilder.loadTexts:
    mscAal1CesStateTable.setStatus("mandatory")
_MscAal1CesStateEntry_Object = MibTableRow
mscAal1CesStateEntry = _MscAal1CesStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1)
)
mscAal1CesStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesStateEntry.setStatus("mandatory")


class _MscAal1CesAdminState_Type(Integer32):
    """Custom type mscAal1CesAdminState based on Integer32"""
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


_MscAal1CesAdminState_Type.__name__ = "Integer32"
_MscAal1CesAdminState_Object = MibTableColumn
mscAal1CesAdminState = _MscAal1CesAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 1),
    _MscAal1CesAdminState_Type()
)
mscAal1CesAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAdminState.setStatus("mandatory")


class _MscAal1CesOperationalState_Type(Integer32):
    """Custom type mscAal1CesOperationalState based on Integer32"""
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


_MscAal1CesOperationalState_Type.__name__ = "Integer32"
_MscAal1CesOperationalState_Object = MibTableColumn
mscAal1CesOperationalState = _MscAal1CesOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 2),
    _MscAal1CesOperationalState_Type()
)
mscAal1CesOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesOperationalState.setStatus("mandatory")


class _MscAal1CesUsageState_Type(Integer32):
    """Custom type mscAal1CesUsageState based on Integer32"""
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


_MscAal1CesUsageState_Type.__name__ = "Integer32"
_MscAal1CesUsageState_Object = MibTableColumn
mscAal1CesUsageState = _MscAal1CesUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 3),
    _MscAal1CesUsageState_Type()
)
mscAal1CesUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesUsageState.setStatus("mandatory")


class _MscAal1CesAvailabilityStatus_Type(OctetString):
    """Custom type mscAal1CesAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscAal1CesAvailabilityStatus_Type.__name__ = "OctetString"
_MscAal1CesAvailabilityStatus_Object = MibTableColumn
mscAal1CesAvailabilityStatus = _MscAal1CesAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 4),
    _MscAal1CesAvailabilityStatus_Type()
)
mscAal1CesAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAvailabilityStatus.setStatus("mandatory")


class _MscAal1CesProceduralStatus_Type(OctetString):
    """Custom type mscAal1CesProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAal1CesProceduralStatus_Type.__name__ = "OctetString"
_MscAal1CesProceduralStatus_Object = MibTableColumn
mscAal1CesProceduralStatus = _MscAal1CesProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 5),
    _MscAal1CesProceduralStatus_Type()
)
mscAal1CesProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesProceduralStatus.setStatus("mandatory")


class _MscAal1CesControlStatus_Type(OctetString):
    """Custom type mscAal1CesControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAal1CesControlStatus_Type.__name__ = "OctetString"
_MscAal1CesControlStatus_Object = MibTableColumn
mscAal1CesControlStatus = _MscAal1CesControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 6),
    _MscAal1CesControlStatus_Type()
)
mscAal1CesControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesControlStatus.setStatus("mandatory")


class _MscAal1CesAlarmStatus_Type(OctetString):
    """Custom type mscAal1CesAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAal1CesAlarmStatus_Type.__name__ = "OctetString"
_MscAal1CesAlarmStatus_Object = MibTableColumn
mscAal1CesAlarmStatus = _MscAal1CesAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 7),
    _MscAal1CesAlarmStatus_Type()
)
mscAal1CesAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAlarmStatus.setStatus("mandatory")


class _MscAal1CesStandbyStatus_Type(Integer32):
    """Custom type mscAal1CesStandbyStatus based on Integer32"""
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


_MscAal1CesStandbyStatus_Type.__name__ = "Integer32"
_MscAal1CesStandbyStatus_Object = MibTableColumn
mscAal1CesStandbyStatus = _MscAal1CesStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 8),
    _MscAal1CesStandbyStatus_Type()
)
mscAal1CesStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesStandbyStatus.setStatus("mandatory")


class _MscAal1CesUnknownStatus_Type(Integer32):
    """Custom type mscAal1CesUnknownStatus based on Integer32"""
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


_MscAal1CesUnknownStatus_Type.__name__ = "Integer32"
_MscAal1CesUnknownStatus_Object = MibTableColumn
mscAal1CesUnknownStatus = _MscAal1CesUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 12, 1, 9),
    _MscAal1CesUnknownStatus_Type()
)
mscAal1CesUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesUnknownStatus.setStatus("mandatory")
_MscAal1CesOperTable_Object = MibTable
mscAal1CesOperTable = _MscAal1CesOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 13)
)
if mibBuilder.loadTexts:
    mscAal1CesOperTable.setStatus("mandatory")
_MscAal1CesOperEntry_Object = MibTableRow
mscAal1CesOperEntry = _MscAal1CesOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 13, 1)
)
mscAal1CesOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesOperEntry.setStatus("mandatory")


class _MscAal1CesCellLossStatus_Type(Integer32):
    """Custom type mscAal1CesCellLossStatus based on Integer32"""
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


_MscAal1CesCellLossStatus_Type.__name__ = "Integer32"
_MscAal1CesCellLossStatus_Object = MibTableColumn
mscAal1CesCellLossStatus = _MscAal1CesCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 13, 1, 1),
    _MscAal1CesCellLossStatus_Type()
)
mscAal1CesCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesCellLossStatus.setStatus("mandatory")


class _MscAal1CesAal1LayerLossStatus_Type(Integer32):
    """Custom type mscAal1CesAal1LayerLossStatus based on Integer32"""
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


_MscAal1CesAal1LayerLossStatus_Type.__name__ = "Integer32"
_MscAal1CesAal1LayerLossStatus_Object = MibTableColumn
mscAal1CesAal1LayerLossStatus = _MscAal1CesAal1LayerLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 13, 1, 2),
    _MscAal1CesAal1LayerLossStatus_Type()
)
mscAal1CesAal1LayerLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAal1LayerLossStatus.setStatus("mandatory")


class _MscAal1CesConnectionStatus_Type(Integer32):
    """Custom type mscAal1CesConnectionStatus based on Integer32"""
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


_MscAal1CesConnectionStatus_Type.__name__ = "Integer32"
_MscAal1CesConnectionStatus_Object = MibTableColumn
mscAal1CesConnectionStatus = _MscAal1CesConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 13, 1, 3),
    _MscAal1CesConnectionStatus_Type()
)
mscAal1CesConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesConnectionStatus.setStatus("mandatory")
_MscAal1CesStatsTable_Object = MibTable
mscAal1CesStatsTable = _MscAal1CesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14)
)
if mibBuilder.loadTexts:
    mscAal1CesStatsTable.setStatus("mandatory")
_MscAal1CesStatsEntry_Object = MibTableRow
mscAal1CesStatsEntry = _MscAal1CesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1)
)
mscAal1CesStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscAal1CesIndex"),
)
if mibBuilder.loadTexts:
    mscAal1CesStatsEntry.setStatus("mandatory")
_MscAal1CesCellsTransmitted_Type = PassportCounter64
_MscAal1CesCellsTransmitted_Object = MibTableColumn
mscAal1CesCellsTransmitted = _MscAal1CesCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 1),
    _MscAal1CesCellsTransmitted_Type()
)
mscAal1CesCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesCellsTransmitted.setStatus("mandatory")
_MscAal1CesCellsReceived_Type = PassportCounter64
_MscAal1CesCellsReceived_Object = MibTableColumn
mscAal1CesCellsReceived = _MscAal1CesCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 2),
    _MscAal1CesCellsReceived_Type()
)
mscAal1CesCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesCellsReceived.setStatus("mandatory")
_MscAal1CesLostCells_Type = Counter32
_MscAal1CesLostCells_Object = MibTableColumn
mscAal1CesLostCells = _MscAal1CesLostCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 3),
    _MscAal1CesLostCells_Type()
)
mscAal1CesLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesLostCells.setStatus("mandatory")
_MscAal1CesBufferUnderflows_Type = Counter32
_MscAal1CesBufferUnderflows_Object = MibTableColumn
mscAal1CesBufferUnderflows = _MscAal1CesBufferUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 4),
    _MscAal1CesBufferUnderflows_Type()
)
mscAal1CesBufferUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesBufferUnderflows.setStatus("mandatory")
_MscAal1CesBufferOverflows_Type = Counter32
_MscAal1CesBufferOverflows_Object = MibTableColumn
mscAal1CesBufferOverflows = _MscAal1CesBufferOverflows_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 5),
    _MscAal1CesBufferOverflows_Type()
)
mscAal1CesBufferOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesBufferOverflows.setStatus("mandatory")
_MscAal1CesReassembledCells_Type = PassportCounter64
_MscAal1CesReassembledCells_Object = MibTableColumn
mscAal1CesReassembledCells = _MscAal1CesReassembledCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 6),
    _MscAal1CesReassembledCells_Type()
)
mscAal1CesReassembledCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesReassembledCells.setStatus("mandatory")
_MscAal1CesHeaderErrors_Type = Counter32
_MscAal1CesHeaderErrors_Object = MibTableColumn
mscAal1CesHeaderErrors = _MscAal1CesHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 7),
    _MscAal1CesHeaderErrors_Type()
)
mscAal1CesHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesHeaderErrors.setStatus("mandatory")
_MscAal1CesPointerReframes_Type = Counter32
_MscAal1CesPointerReframes_Object = MibTableColumn
mscAal1CesPointerReframes = _MscAal1CesPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 8),
    _MscAal1CesPointerReframes_Type()
)
mscAal1CesPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPointerReframes.setStatus("mandatory")
_MscAal1CesPointerParityErrors_Type = Counter32
_MscAal1CesPointerParityErrors_Object = MibTableColumn
mscAal1CesPointerParityErrors = _MscAal1CesPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 9),
    _MscAal1CesPointerParityErrors_Type()
)
mscAal1CesPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesPointerParityErrors.setStatus("mandatory")
_MscAal1CesAal1SequenceErrors_Type = Counter32
_MscAal1CesAal1SequenceErrors_Object = MibTableColumn
mscAal1CesAal1SequenceErrors = _MscAal1CesAal1SequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 10),
    _MscAal1CesAal1SequenceErrors_Type()
)
mscAal1CesAal1SequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesAal1SequenceErrors.setStatus("mandatory")
_MscAal1CesMisinsertedCells_Type = Counter32
_MscAal1CesMisinsertedCells_Object = MibTableColumn
mscAal1CesMisinsertedCells = _MscAal1CesMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 119, 14, 1, 11),
    _MscAal1CesMisinsertedCells_Type()
)
mscAal1CesMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAal1CesMisinsertedCells.setStatus("mandatory")
_MscMmTx_ObjectIdentity = ObjectIdentity
mscMmTx = _MscMmTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151)
)
_MscMmTxRowStatusTable_Object = MibTable
mscMmTxRowStatusTable = _MscMmTxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 1)
)
if mibBuilder.loadTexts:
    mscMmTxRowStatusTable.setStatus("mandatory")
_MscMmTxRowStatusEntry_Object = MibTableRow
mscMmTxRowStatusEntry = _MscMmTxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 1, 1)
)
mscMmTxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxRowStatusEntry.setStatus("mandatory")
_MscMmTxRowStatus_Type = RowStatus
_MscMmTxRowStatus_Object = MibTableColumn
mscMmTxRowStatus = _MscMmTxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 1, 1, 1),
    _MscMmTxRowStatus_Type()
)
mscMmTxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxRowStatus.setStatus("mandatory")
_MscMmTxComponentName_Type = DisplayString
_MscMmTxComponentName_Object = MibTableColumn
mscMmTxComponentName = _MscMmTxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 1, 1, 2),
    _MscMmTxComponentName_Type()
)
mscMmTxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxComponentName.setStatus("mandatory")
_MscMmTxStorageType_Type = StorageType
_MscMmTxStorageType_Object = MibTableColumn
mscMmTxStorageType = _MscMmTxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 1, 1, 4),
    _MscMmTxStorageType_Type()
)
mscMmTxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxStorageType.setStatus("mandatory")


class _MscMmTxIndex_Type(Integer32):
    """Custom type mscMmTxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscMmTxIndex_Type.__name__ = "Integer32"
_MscMmTxIndex_Object = MibTableColumn
mscMmTxIndex = _MscMmTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 1, 1, 10),
    _MscMmTxIndex_Type()
)
mscMmTxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMmTxIndex.setStatus("mandatory")
_MscMmTxNap_ObjectIdentity = ObjectIdentity
mscMmTxNap = _MscMmTxNap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2)
)
_MscMmTxNapRowStatusTable_Object = MibTable
mscMmTxNapRowStatusTable = _MscMmTxNapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 1)
)
if mibBuilder.loadTexts:
    mscMmTxNapRowStatusTable.setStatus("mandatory")
_MscMmTxNapRowStatusEntry_Object = MibTableRow
mscMmTxNapRowStatusEntry = _MscMmTxNapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 1, 1)
)
mscMmTxNapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxNapIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxNapRowStatusEntry.setStatus("mandatory")
_MscMmTxNapRowStatus_Type = RowStatus
_MscMmTxNapRowStatus_Object = MibTableColumn
mscMmTxNapRowStatus = _MscMmTxNapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 1, 1, 1),
    _MscMmTxNapRowStatus_Type()
)
mscMmTxNapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxNapRowStatus.setStatus("mandatory")
_MscMmTxNapComponentName_Type = DisplayString
_MscMmTxNapComponentName_Object = MibTableColumn
mscMmTxNapComponentName = _MscMmTxNapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 1, 1, 2),
    _MscMmTxNapComponentName_Type()
)
mscMmTxNapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxNapComponentName.setStatus("mandatory")
_MscMmTxNapStorageType_Type = StorageType
_MscMmTxNapStorageType_Object = MibTableColumn
mscMmTxNapStorageType = _MscMmTxNapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 1, 1, 4),
    _MscMmTxNapStorageType_Type()
)
mscMmTxNapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxNapStorageType.setStatus("mandatory")
_MscMmTxNapIndex_Type = NonReplicated
_MscMmTxNapIndex_Object = MibTableColumn
mscMmTxNapIndex = _MscMmTxNapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 1, 1, 10),
    _MscMmTxNapIndex_Type()
)
mscMmTxNapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMmTxNapIndex.setStatus("mandatory")
_MscMmTxNapProvTable_Object = MibTable
mscMmTxNapProvTable = _MscMmTxNapProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 10)
)
if mibBuilder.loadTexts:
    mscMmTxNapProvTable.setStatus("mandatory")
_MscMmTxNapProvEntry_Object = MibTableRow
mscMmTxNapProvEntry = _MscMmTxNapProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 10, 1)
)
mscMmTxNapProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxNapIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxNapProvEntry.setStatus("mandatory")
_MscMmTxNapAtmConnection_Type = Link
_MscMmTxNapAtmConnection_Object = MibTableColumn
mscMmTxNapAtmConnection = _MscMmTxNapAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 2, 10, 1, 1),
    _MscMmTxNapAtmConnection_Type()
)
mscMmTxNapAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxNapAtmConnection.setStatus("mandatory")
_MscMmTxAtmCon_ObjectIdentity = ObjectIdentity
mscMmTxAtmCon = _MscMmTxAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6)
)
_MscMmTxAtmConRowStatusTable_Object = MibTable
mscMmTxAtmConRowStatusTable = _MscMmTxAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 1)
)
if mibBuilder.loadTexts:
    mscMmTxAtmConRowStatusTable.setStatus("mandatory")
_MscMmTxAtmConRowStatusEntry_Object = MibTableRow
mscMmTxAtmConRowStatusEntry = _MscMmTxAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 1, 1)
)
mscMmTxAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxAtmConRowStatusEntry.setStatus("mandatory")
_MscMmTxAtmConRowStatus_Type = RowStatus
_MscMmTxAtmConRowStatus_Object = MibTableColumn
mscMmTxAtmConRowStatus = _MscMmTxAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 1, 1, 1),
    _MscMmTxAtmConRowStatus_Type()
)
mscMmTxAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAtmConRowStatus.setStatus("mandatory")
_MscMmTxAtmConComponentName_Type = DisplayString
_MscMmTxAtmConComponentName_Object = MibTableColumn
mscMmTxAtmConComponentName = _MscMmTxAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 1, 1, 2),
    _MscMmTxAtmConComponentName_Type()
)
mscMmTxAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAtmConComponentName.setStatus("mandatory")
_MscMmTxAtmConStorageType_Type = StorageType
_MscMmTxAtmConStorageType_Object = MibTableColumn
mscMmTxAtmConStorageType = _MscMmTxAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 1, 1, 4),
    _MscMmTxAtmConStorageType_Type()
)
mscMmTxAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAtmConStorageType.setStatus("mandatory")
_MscMmTxAtmConIndex_Type = NonReplicated
_MscMmTxAtmConIndex_Object = MibTableColumn
mscMmTxAtmConIndex = _MscMmTxAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 1, 1, 10),
    _MscMmTxAtmConIndex_Type()
)
mscMmTxAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMmTxAtmConIndex.setStatus("mandatory")
_MscMmTxAtmConOperTable_Object = MibTable
mscMmTxAtmConOperTable = _MscMmTxAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 10)
)
if mibBuilder.loadTexts:
    mscMmTxAtmConOperTable.setStatus("mandatory")
_MscMmTxAtmConOperEntry_Object = MibTableRow
mscMmTxAtmConOperEntry = _MscMmTxAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 10, 1)
)
mscMmTxAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxAtmConOperEntry.setStatus("mandatory")
_MscMmTxAtmConNextHop_Type = RowPointer
_MscMmTxAtmConNextHop_Object = MibTableColumn
mscMmTxAtmConNextHop = _MscMmTxAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 6, 10, 1, 1),
    _MscMmTxAtmConNextHop_Type()
)
mscMmTxAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAtmConNextHop.setStatus("mandatory")
_MscMmTxCidDataTable_Object = MibTable
mscMmTxCidDataTable = _MscMmTxCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 10)
)
if mibBuilder.loadTexts:
    mscMmTxCidDataTable.setStatus("mandatory")
_MscMmTxCidDataEntry_Object = MibTableRow
mscMmTxCidDataEntry = _MscMmTxCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 10, 1)
)
mscMmTxCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxCidDataEntry.setStatus("mandatory")


class _MscMmTxCustomerIdentifier_Type(Unsigned32):
    """Custom type mscMmTxCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscMmTxCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscMmTxCustomerIdentifier_Object = MibTableColumn
mscMmTxCustomerIdentifier = _MscMmTxCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 10, 1, 1),
    _MscMmTxCustomerIdentifier_Type()
)
mscMmTxCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxCustomerIdentifier.setStatus("mandatory")
_MscMmTxProvTable_Object = MibTable
mscMmTxProvTable = _MscMmTxProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11)
)
if mibBuilder.loadTexts:
    mscMmTxProvTable.setStatus("mandatory")
_MscMmTxProvEntry_Object = MibTableRow
mscMmTxProvEntry = _MscMmTxProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11, 1)
)
mscMmTxProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxProvEntry.setStatus("mandatory")
_MscMmTxLinkToLogicalProcessor_Type = Link
_MscMmTxLinkToLogicalProcessor_Object = MibTableColumn
mscMmTxLinkToLogicalProcessor = _MscMmTxLinkToLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11, 1, 3),
    _MscMmTxLinkToLogicalProcessor_Type()
)
mscMmTxLinkToLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxLinkToLogicalProcessor.setStatus("mandatory")


class _MscMmTxMonitoredDirection_Type(Integer32):
    """Custom type mscMmTxMonitoredDirection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ingress", 0)
    )


_MscMmTxMonitoredDirection_Type.__name__ = "Integer32"
_MscMmTxMonitoredDirection_Object = MibTableColumn
mscMmTxMonitoredDirection = _MscMmTxMonitoredDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11, 1, 4),
    _MscMmTxMonitoredDirection_Type()
)
mscMmTxMonitoredDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxMonitoredDirection.setStatus("mandatory")


class _MscMmTxServiceType_Type(Integer32):
    """Custom type mscMmTxServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("basicStructured", 1)
    )


_MscMmTxServiceType_Type.__name__ = "Integer32"
_MscMmTxServiceType_Object = MibTableColumn
mscMmTxServiceType = _MscMmTxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11, 1, 5),
    _MscMmTxServiceType_Type()
)
mscMmTxServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxServiceType.setStatus("mandatory")


class _MscMmTxPartialFill_Type(Unsigned32):
    """Custom type mscMmTxPartialFill based on Unsigned32"""
    defaultValue = 47

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(47, 47),
    )


_MscMmTxPartialFill_Type.__name__ = "Unsigned32"
_MscMmTxPartialFill_Object = MibTableColumn
mscMmTxPartialFill = _MscMmTxPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11, 1, 6),
    _MscMmTxPartialFill_Type()
)
mscMmTxPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxPartialFill.setStatus("mandatory")


class _MscMmTxIdleSuppression_Type(Integer32):
    """Custom type mscMmTxIdleSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("off", 0)
    )


_MscMmTxIdleSuppression_Type.__name__ = "Integer32"
_MscMmTxIdleSuppression_Object = MibTableColumn
mscMmTxIdleSuppression = _MscMmTxIdleSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 11, 1, 7),
    _MscMmTxIdleSuppression_Type()
)
mscMmTxIdleSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxIdleSuppression.setStatus("mandatory")
_MscMmTxStateTable_Object = MibTable
mscMmTxStateTable = _MscMmTxStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12)
)
if mibBuilder.loadTexts:
    mscMmTxStateTable.setStatus("mandatory")
_MscMmTxStateEntry_Object = MibTableRow
mscMmTxStateEntry = _MscMmTxStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1)
)
mscMmTxStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxStateEntry.setStatus("mandatory")


class _MscMmTxAdminState_Type(Integer32):
    """Custom type mscMmTxAdminState based on Integer32"""
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


_MscMmTxAdminState_Type.__name__ = "Integer32"
_MscMmTxAdminState_Object = MibTableColumn
mscMmTxAdminState = _MscMmTxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 1),
    _MscMmTxAdminState_Type()
)
mscMmTxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAdminState.setStatus("mandatory")


class _MscMmTxOperationalState_Type(Integer32):
    """Custom type mscMmTxOperationalState based on Integer32"""
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


_MscMmTxOperationalState_Type.__name__ = "Integer32"
_MscMmTxOperationalState_Object = MibTableColumn
mscMmTxOperationalState = _MscMmTxOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 2),
    _MscMmTxOperationalState_Type()
)
mscMmTxOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxOperationalState.setStatus("mandatory")


class _MscMmTxUsageState_Type(Integer32):
    """Custom type mscMmTxUsageState based on Integer32"""
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


_MscMmTxUsageState_Type.__name__ = "Integer32"
_MscMmTxUsageState_Object = MibTableColumn
mscMmTxUsageState = _MscMmTxUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 3),
    _MscMmTxUsageState_Type()
)
mscMmTxUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxUsageState.setStatus("mandatory")


class _MscMmTxAvailabilityStatus_Type(OctetString):
    """Custom type mscMmTxAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMmTxAvailabilityStatus_Type.__name__ = "OctetString"
_MscMmTxAvailabilityStatus_Object = MibTableColumn
mscMmTxAvailabilityStatus = _MscMmTxAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 4),
    _MscMmTxAvailabilityStatus_Type()
)
mscMmTxAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAvailabilityStatus.setStatus("mandatory")


class _MscMmTxProceduralStatus_Type(OctetString):
    """Custom type mscMmTxProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMmTxProceduralStatus_Type.__name__ = "OctetString"
_MscMmTxProceduralStatus_Object = MibTableColumn
mscMmTxProceduralStatus = _MscMmTxProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 5),
    _MscMmTxProceduralStatus_Type()
)
mscMmTxProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxProceduralStatus.setStatus("mandatory")


class _MscMmTxControlStatus_Type(OctetString):
    """Custom type mscMmTxControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMmTxControlStatus_Type.__name__ = "OctetString"
_MscMmTxControlStatus_Object = MibTableColumn
mscMmTxControlStatus = _MscMmTxControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 6),
    _MscMmTxControlStatus_Type()
)
mscMmTxControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxControlStatus.setStatus("mandatory")


class _MscMmTxAlarmStatus_Type(OctetString):
    """Custom type mscMmTxAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMmTxAlarmStatus_Type.__name__ = "OctetString"
_MscMmTxAlarmStatus_Object = MibTableColumn
mscMmTxAlarmStatus = _MscMmTxAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 7),
    _MscMmTxAlarmStatus_Type()
)
mscMmTxAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxAlarmStatus.setStatus("mandatory")


class _MscMmTxStandbyStatus_Type(Integer32):
    """Custom type mscMmTxStandbyStatus based on Integer32"""
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


_MscMmTxStandbyStatus_Type.__name__ = "Integer32"
_MscMmTxStandbyStatus_Object = MibTableColumn
mscMmTxStandbyStatus = _MscMmTxStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 8),
    _MscMmTxStandbyStatus_Type()
)
mscMmTxStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxStandbyStatus.setStatus("mandatory")


class _MscMmTxUnknownStatus_Type(Integer32):
    """Custom type mscMmTxUnknownStatus based on Integer32"""
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


_MscMmTxUnknownStatus_Type.__name__ = "Integer32"
_MscMmTxUnknownStatus_Object = MibTableColumn
mscMmTxUnknownStatus = _MscMmTxUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 12, 1, 9),
    _MscMmTxUnknownStatus_Type()
)
mscMmTxUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxUnknownStatus.setStatus("mandatory")
_MscMmTxOperTable_Object = MibTable
mscMmTxOperTable = _MscMmTxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 13)
)
if mibBuilder.loadTexts:
    mscMmTxOperTable.setStatus("mandatory")
_MscMmTxOperEntry_Object = MibTableRow
mscMmTxOperEntry = _MscMmTxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 13, 1)
)
mscMmTxOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB", "mscMmTxIndex"),
)
if mibBuilder.loadTexts:
    mscMmTxOperEntry.setStatus("mandatory")


class _MscMmTxConnectionStatus_Type(Integer32):
    """Custom type mscMmTxConnectionStatus based on Integer32"""
    defaultValue = 1

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
        *(("atmNotConfigured", 3),
          ("atmNotReady", 2),
          ("channelNotReady", 1),
          ("channelNotSpecified", 4),
          ("connected", 0))
    )


_MscMmTxConnectionStatus_Type.__name__ = "Integer32"
_MscMmTxConnectionStatus_Object = MibTableColumn
mscMmTxConnectionStatus = _MscMmTxConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 13, 1, 3),
    _MscMmTxConnectionStatus_Type()
)
mscMmTxConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMmTxConnectionStatus.setStatus("mandatory")
_MscMmTxChanToMonitor_Type = RowPointer
_MscMmTxChanToMonitor_Object = MibTableColumn
mscMmTxChanToMonitor = _MscMmTxChanToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 151, 13, 1, 4),
    _MscMmTxChanToMonitor_Type()
)
mscMmTxChanToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMmTxChanToMonitor.setStatus("mandatory")
_CircuitEmulationServiceMIB_ObjectIdentity = ObjectIdentity
circuitEmulationServiceMIB = _CircuitEmulationServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55)
)
_CircuitEmulationServiceGroup_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroup = _CircuitEmulationServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 1)
)
_CircuitEmulationServiceGroupCA_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroupCA = _CircuitEmulationServiceGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 1, 1)
)
_CircuitEmulationServiceGroupCA02_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroupCA02 = _CircuitEmulationServiceGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 1, 1, 3)
)
_CircuitEmulationServiceGroupCA02A_ObjectIdentity = ObjectIdentity
circuitEmulationServiceGroupCA02A = _CircuitEmulationServiceGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 1, 1, 3, 2)
)
_CircuitEmulationServiceCapabilities_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilities = _CircuitEmulationServiceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 3)
)
_CircuitEmulationServiceCapabilitiesCA_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilitiesCA = _CircuitEmulationServiceCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 3, 1)
)
_CircuitEmulationServiceCapabilitiesCA02_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilitiesCA02 = _CircuitEmulationServiceCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 3, 1, 3)
)
_CircuitEmulationServiceCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
circuitEmulationServiceCapabilitiesCA02A = _CircuitEmulationServiceCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 55, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-CircuitEmulationServiceMIB",
    **{"mscAal1Ces": mscAal1Ces,
       "mscAal1CesRowStatusTable": mscAal1CesRowStatusTable,
       "mscAal1CesRowStatusEntry": mscAal1CesRowStatusEntry,
       "mscAal1CesRowStatus": mscAal1CesRowStatus,
       "mscAal1CesComponentName": mscAal1CesComponentName,
       "mscAal1CesStorageType": mscAal1CesStorageType,
       "mscAal1CesIndex": mscAal1CesIndex,
       "mscAal1CesNap": mscAal1CesNap,
       "mscAal1CesNapRowStatusTable": mscAal1CesNapRowStatusTable,
       "mscAal1CesNapRowStatusEntry": mscAal1CesNapRowStatusEntry,
       "mscAal1CesNapRowStatus": mscAal1CesNapRowStatus,
       "mscAal1CesNapComponentName": mscAal1CesNapComponentName,
       "mscAal1CesNapStorageType": mscAal1CesNapStorageType,
       "mscAal1CesNapIndex": mscAal1CesNapIndex,
       "mscAal1CesNapProvTable": mscAal1CesNapProvTable,
       "mscAal1CesNapProvEntry": mscAal1CesNapProvEntry,
       "mscAal1CesNapAtmConnection": mscAal1CesNapAtmConnection,
       "mscAal1CesAep": mscAal1CesAep,
       "mscAal1CesAepRowStatusTable": mscAal1CesAepRowStatusTable,
       "mscAal1CesAepRowStatusEntry": mscAal1CesAepRowStatusEntry,
       "mscAal1CesAepRowStatus": mscAal1CesAepRowStatus,
       "mscAal1CesAepComponentName": mscAal1CesAepComponentName,
       "mscAal1CesAepStorageType": mscAal1CesAepStorageType,
       "mscAal1CesAepIndex": mscAal1CesAepIndex,
       "mscAal1CesAepProvEndPointAddrTable": mscAal1CesAepProvEndPointAddrTable,
       "mscAal1CesAepProvEndPointAddrEntry": mscAal1CesAepProvEndPointAddrEntry,
       "mscAal1CesAepExpectedRemoteAddress": mscAal1CesAepExpectedRemoteAddress,
       "mscAal1CesAepLocalAddress": mscAal1CesAepLocalAddress,
       "mscAal1CesAepProvTable": mscAal1CesAepProvTable,
       "mscAal1CesAepProvEntry": mscAal1CesAepProvEntry,
       "mscAal1CesAepAddressToCall": mscAal1CesAepAddressToCall,
       "mscAal1CesAepRoutingOption": mscAal1CesAepRoutingOption,
       "mscAal1CesAepProfile": mscAal1CesAepProfile,
       "mscAal1CesAepFirstRetryInterval": mscAal1CesAepFirstRetryInterval,
       "mscAal1CesAepRetryLimit": mscAal1CesAepRetryLimit,
       "mscAal1CesAepActiveEndPointType": mscAal1CesAepActiveEndPointType,
       "mscAal1CesAepCalledVpiVci": mscAal1CesAepCalledVpiVci,
       "mscAal1CesAepEpOperTable": mscAal1CesAepEpOperTable,
       "mscAal1CesAepEpOperEntry": mscAal1CesAepEpOperEntry,
       "mscAal1CesAepRemoteAddress": mscAal1CesAepRemoteAddress,
       "mscAal1CesAepLastTearDownCause": mscAal1CesAepLastTearDownCause,
       "mscAal1CesAepLastTearDownDiagnostic": mscAal1CesAepLastTearDownDiagnostic,
       "mscAal1CesAepOutTable": mscAal1CesAepOutTable,
       "mscAal1CesAepOutEntry": mscAal1CesAepOutEntry,
       "mscAal1CesAepSvcStatus": mscAal1CesAepSvcStatus,
       "mscAal1CesAepLastSetupFailureCause": mscAal1CesAepLastSetupFailureCause,
       "mscAal1CesAepLastSetupFailureDiagnostic": mscAal1CesAepLastSetupFailureDiagnostic,
       "mscAal1CesAepRetryTimeRemaining": mscAal1CesAepRetryTimeRemaining,
       "mscAal1CesAepRetryFailures": mscAal1CesAepRetryFailures,
       "mscAal1CesPep": mscAal1CesPep,
       "mscAal1CesPepRowStatusTable": mscAal1CesPepRowStatusTable,
       "mscAal1CesPepRowStatusEntry": mscAal1CesPepRowStatusEntry,
       "mscAal1CesPepRowStatus": mscAal1CesPepRowStatus,
       "mscAal1CesPepComponentName": mscAal1CesPepComponentName,
       "mscAal1CesPepStorageType": mscAal1CesPepStorageType,
       "mscAal1CesPepIndex": mscAal1CesPepIndex,
       "mscAal1CesPepProvEndPointAddrTable": mscAal1CesPepProvEndPointAddrTable,
       "mscAal1CesPepProvEndPointAddrEntry": mscAal1CesPepProvEndPointAddrEntry,
       "mscAal1CesPepExpectedRemoteAddress": mscAal1CesPepExpectedRemoteAddress,
       "mscAal1CesPepLocalAddress": mscAal1CesPepLocalAddress,
       "mscAal1CesPepEpOperTable": mscAal1CesPepEpOperTable,
       "mscAal1CesPepEpOperEntry": mscAal1CesPepEpOperEntry,
       "mscAal1CesPepRemoteAddress": mscAal1CesPepRemoteAddress,
       "mscAal1CesPepLastTearDownCause": mscAal1CesPepLastTearDownCause,
       "mscAal1CesPepLastTearDownDiagnostic": mscAal1CesPepLastTearDownDiagnostic,
       "mscAal1CesPepPassiveOperTable": mscAal1CesPepPassiveOperTable,
       "mscAal1CesPepPassiveOperEntry": mscAal1CesPepPassiveOperEntry,
       "mscAal1CesPepSvcStatus": mscAal1CesPepSvcStatus,
       "mscAal1CesLCo": mscAal1CesLCo,
       "mscAal1CesLCoRowStatusTable": mscAal1CesLCoRowStatusTable,
       "mscAal1CesLCoRowStatusEntry": mscAal1CesLCoRowStatusEntry,
       "mscAal1CesLCoRowStatus": mscAal1CesLCoRowStatus,
       "mscAal1CesLCoComponentName": mscAal1CesLCoComponentName,
       "mscAal1CesLCoStorageType": mscAal1CesLCoStorageType,
       "mscAal1CesLCoIndex": mscAal1CesLCoIndex,
       "mscAal1CesLCoPathDataTable": mscAal1CesLCoPathDataTable,
       "mscAal1CesLCoPathDataEntry": mscAal1CesLCoPathDataEntry,
       "mscAal1CesLCoState": mscAal1CesLCoState,
       "mscAal1CesLCoOverrideRemoteName": mscAal1CesLCoOverrideRemoteName,
       "mscAal1CesLCoEnd": mscAal1CesLCoEnd,
       "mscAal1CesLCoCostMetric": mscAal1CesLCoCostMetric,
       "mscAal1CesLCoDelayMetric": mscAal1CesLCoDelayMetric,
       "mscAal1CesLCoRoundTripDelay": mscAal1CesLCoRoundTripDelay,
       "mscAal1CesLCoSetupPriority": mscAal1CesLCoSetupPriority,
       "mscAal1CesLCoHoldingPriority": mscAal1CesLCoHoldingPriority,
       "mscAal1CesLCoRequiredTxBandwidth": mscAal1CesLCoRequiredTxBandwidth,
       "mscAal1CesLCoRequiredRxBandwidth": mscAal1CesLCoRequiredRxBandwidth,
       "mscAal1CesLCoRequiredTrafficType": mscAal1CesLCoRequiredTrafficType,
       "mscAal1CesLCoPermittedTrunkTypes": mscAal1CesLCoPermittedTrunkTypes,
       "mscAal1CesLCoRequiredSecurity": mscAal1CesLCoRequiredSecurity,
       "mscAal1CesLCoRequiredCustomerParameter": mscAal1CesLCoRequiredCustomerParameter,
       "mscAal1CesLCoEmissionPriority": mscAal1CesLCoEmissionPriority,
       "mscAal1CesLCoDiscardPriority": mscAal1CesLCoDiscardPriority,
       "mscAal1CesLCoPathType": mscAal1CesLCoPathType,
       "mscAal1CesLCoRetryCount": mscAal1CesLCoRetryCount,
       "mscAal1CesLCoPathFailureCount": mscAal1CesLCoPathFailureCount,
       "mscAal1CesLCoReasonForNoRoute": mscAal1CesLCoReasonForNoRoute,
       "mscAal1CesLCoLastTearDownReason": mscAal1CesLCoLastTearDownReason,
       "mscAal1CesLCoPathFailureAction": mscAal1CesLCoPathFailureAction,
       "mscAal1CesLCoBumpPreference": mscAal1CesLCoBumpPreference,
       "mscAal1CesLCoOptimization": mscAal1CesLCoOptimization,
       "mscAal1CesLCoPathUpDateTime": mscAal1CesLCoPathUpDateTime,
       "mscAal1CesLCoStatsTable": mscAal1CesLCoStatsTable,
       "mscAal1CesLCoStatsEntry": mscAal1CesLCoStatsEntry,
       "mscAal1CesLCoPktsToNetwork": mscAal1CesLCoPktsToNetwork,
       "mscAal1CesLCoBytesToNetwork": mscAal1CesLCoBytesToNetwork,
       "mscAal1CesLCoPktsFromNetwork": mscAal1CesLCoPktsFromNetwork,
       "mscAal1CesLCoBytesFromNetwork": mscAal1CesLCoBytesFromNetwork,
       "mscAal1CesLCoPathTable": mscAal1CesLCoPathTable,
       "mscAal1CesLCoPathEntry": mscAal1CesLCoPathEntry,
       "mscAal1CesLCoPathValue": mscAal1CesLCoPathValue,
       "mscAal1CesAtmCon": mscAal1CesAtmCon,
       "mscAal1CesAtmConRowStatusTable": mscAal1CesAtmConRowStatusTable,
       "mscAal1CesAtmConRowStatusEntry": mscAal1CesAtmConRowStatusEntry,
       "mscAal1CesAtmConRowStatus": mscAal1CesAtmConRowStatus,
       "mscAal1CesAtmConComponentName": mscAal1CesAtmConComponentName,
       "mscAal1CesAtmConStorageType": mscAal1CesAtmConStorageType,
       "mscAal1CesAtmConIndex": mscAal1CesAtmConIndex,
       "mscAal1CesAtmConOperTable": mscAal1CesAtmConOperTable,
       "mscAal1CesAtmConOperEntry": mscAal1CesAtmConOperEntry,
       "mscAal1CesAtmConNextHop": mscAal1CesAtmConNextHop,
       "mscAal1CesCidDataTable": mscAal1CesCidDataTable,
       "mscAal1CesCidDataEntry": mscAal1CesCidDataEntry,
       "mscAal1CesCustomerIdentifier": mscAal1CesCustomerIdentifier,
       "mscAal1CesProvTable": mscAal1CesProvTable,
       "mscAal1CesProvEntry": mscAal1CesProvEntry,
       "mscAal1CesServiceType": mscAal1CesServiceType,
       "mscAal1CesBufferSize": mscAal1CesBufferSize,
       "mscAal1CesCellLossIntegrationPeriod": mscAal1CesCellLossIntegrationPeriod,
       "mscAal1CesInterfaceName": mscAal1CesInterfaceName,
       "mscAal1CesPartialFill": mscAal1CesPartialFill,
       "mscAal1CesIdleSuppression": mscAal1CesIdleSuppression,
       "mscAal1CesIdlePattern": mscAal1CesIdlePattern,
       "mscAal1CesCellLossRecoveryPeriod": mscAal1CesCellLossRecoveryPeriod,
       "mscAal1CesDummyDataByte": mscAal1CesDummyDataByte,
       "mscAal1CesMaximumBufferDelay": mscAal1CesMaximumBufferDelay,
       "mscAal1CesDp2CellDelayVariationTolerance": mscAal1CesDp2CellDelayVariationTolerance,
       "mscAal1CesStateTable": mscAal1CesStateTable,
       "mscAal1CesStateEntry": mscAal1CesStateEntry,
       "mscAal1CesAdminState": mscAal1CesAdminState,
       "mscAal1CesOperationalState": mscAal1CesOperationalState,
       "mscAal1CesUsageState": mscAal1CesUsageState,
       "mscAal1CesAvailabilityStatus": mscAal1CesAvailabilityStatus,
       "mscAal1CesProceduralStatus": mscAal1CesProceduralStatus,
       "mscAal1CesControlStatus": mscAal1CesControlStatus,
       "mscAal1CesAlarmStatus": mscAal1CesAlarmStatus,
       "mscAal1CesStandbyStatus": mscAal1CesStandbyStatus,
       "mscAal1CesUnknownStatus": mscAal1CesUnknownStatus,
       "mscAal1CesOperTable": mscAal1CesOperTable,
       "mscAal1CesOperEntry": mscAal1CesOperEntry,
       "mscAal1CesCellLossStatus": mscAal1CesCellLossStatus,
       "mscAal1CesAal1LayerLossStatus": mscAal1CesAal1LayerLossStatus,
       "mscAal1CesConnectionStatus": mscAal1CesConnectionStatus,
       "mscAal1CesStatsTable": mscAal1CesStatsTable,
       "mscAal1CesStatsEntry": mscAal1CesStatsEntry,
       "mscAal1CesCellsTransmitted": mscAal1CesCellsTransmitted,
       "mscAal1CesCellsReceived": mscAal1CesCellsReceived,
       "mscAal1CesLostCells": mscAal1CesLostCells,
       "mscAal1CesBufferUnderflows": mscAal1CesBufferUnderflows,
       "mscAal1CesBufferOverflows": mscAal1CesBufferOverflows,
       "mscAal1CesReassembledCells": mscAal1CesReassembledCells,
       "mscAal1CesHeaderErrors": mscAal1CesHeaderErrors,
       "mscAal1CesPointerReframes": mscAal1CesPointerReframes,
       "mscAal1CesPointerParityErrors": mscAal1CesPointerParityErrors,
       "mscAal1CesAal1SequenceErrors": mscAal1CesAal1SequenceErrors,
       "mscAal1CesMisinsertedCells": mscAal1CesMisinsertedCells,
       "mscMmTx": mscMmTx,
       "mscMmTxRowStatusTable": mscMmTxRowStatusTable,
       "mscMmTxRowStatusEntry": mscMmTxRowStatusEntry,
       "mscMmTxRowStatus": mscMmTxRowStatus,
       "mscMmTxComponentName": mscMmTxComponentName,
       "mscMmTxStorageType": mscMmTxStorageType,
       "mscMmTxIndex": mscMmTxIndex,
       "mscMmTxNap": mscMmTxNap,
       "mscMmTxNapRowStatusTable": mscMmTxNapRowStatusTable,
       "mscMmTxNapRowStatusEntry": mscMmTxNapRowStatusEntry,
       "mscMmTxNapRowStatus": mscMmTxNapRowStatus,
       "mscMmTxNapComponentName": mscMmTxNapComponentName,
       "mscMmTxNapStorageType": mscMmTxNapStorageType,
       "mscMmTxNapIndex": mscMmTxNapIndex,
       "mscMmTxNapProvTable": mscMmTxNapProvTable,
       "mscMmTxNapProvEntry": mscMmTxNapProvEntry,
       "mscMmTxNapAtmConnection": mscMmTxNapAtmConnection,
       "mscMmTxAtmCon": mscMmTxAtmCon,
       "mscMmTxAtmConRowStatusTable": mscMmTxAtmConRowStatusTable,
       "mscMmTxAtmConRowStatusEntry": mscMmTxAtmConRowStatusEntry,
       "mscMmTxAtmConRowStatus": mscMmTxAtmConRowStatus,
       "mscMmTxAtmConComponentName": mscMmTxAtmConComponentName,
       "mscMmTxAtmConStorageType": mscMmTxAtmConStorageType,
       "mscMmTxAtmConIndex": mscMmTxAtmConIndex,
       "mscMmTxAtmConOperTable": mscMmTxAtmConOperTable,
       "mscMmTxAtmConOperEntry": mscMmTxAtmConOperEntry,
       "mscMmTxAtmConNextHop": mscMmTxAtmConNextHop,
       "mscMmTxCidDataTable": mscMmTxCidDataTable,
       "mscMmTxCidDataEntry": mscMmTxCidDataEntry,
       "mscMmTxCustomerIdentifier": mscMmTxCustomerIdentifier,
       "mscMmTxProvTable": mscMmTxProvTable,
       "mscMmTxProvEntry": mscMmTxProvEntry,
       "mscMmTxLinkToLogicalProcessor": mscMmTxLinkToLogicalProcessor,
       "mscMmTxMonitoredDirection": mscMmTxMonitoredDirection,
       "mscMmTxServiceType": mscMmTxServiceType,
       "mscMmTxPartialFill": mscMmTxPartialFill,
       "mscMmTxIdleSuppression": mscMmTxIdleSuppression,
       "mscMmTxStateTable": mscMmTxStateTable,
       "mscMmTxStateEntry": mscMmTxStateEntry,
       "mscMmTxAdminState": mscMmTxAdminState,
       "mscMmTxOperationalState": mscMmTxOperationalState,
       "mscMmTxUsageState": mscMmTxUsageState,
       "mscMmTxAvailabilityStatus": mscMmTxAvailabilityStatus,
       "mscMmTxProceduralStatus": mscMmTxProceduralStatus,
       "mscMmTxControlStatus": mscMmTxControlStatus,
       "mscMmTxAlarmStatus": mscMmTxAlarmStatus,
       "mscMmTxStandbyStatus": mscMmTxStandbyStatus,
       "mscMmTxUnknownStatus": mscMmTxUnknownStatus,
       "mscMmTxOperTable": mscMmTxOperTable,
       "mscMmTxOperEntry": mscMmTxOperEntry,
       "mscMmTxConnectionStatus": mscMmTxConnectionStatus,
       "mscMmTxChanToMonitor": mscMmTxChanToMonitor,
       "circuitEmulationServiceMIB": circuitEmulationServiceMIB,
       "circuitEmulationServiceGroup": circuitEmulationServiceGroup,
       "circuitEmulationServiceGroupCA": circuitEmulationServiceGroupCA,
       "circuitEmulationServiceGroupCA02": circuitEmulationServiceGroupCA02,
       "circuitEmulationServiceGroupCA02A": circuitEmulationServiceGroupCA02A,
       "circuitEmulationServiceCapabilities": circuitEmulationServiceCapabilities,
       "circuitEmulationServiceCapabilitiesCA": circuitEmulationServiceCapabilitiesCA,
       "circuitEmulationServiceCapabilitiesCA02": circuitEmulationServiceCapabilitiesCA02,
       "circuitEmulationServiceCapabilitiesCA02A": circuitEmulationServiceCapabilitiesCA02A}
)
