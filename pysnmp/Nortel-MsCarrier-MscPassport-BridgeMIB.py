# SNMP MIB module (Nortel-MsCarrier-MscPassport-BridgeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BridgeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:02 2024
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

(BridgeId,
 Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 MacAddress,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "BridgeId",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DashedHexString,
 Hex,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex,
 mscVrPp,
 mscVrPpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
    "mscVrIndex",
    "mscVrPp",
    "mscVrPpIndex")

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

_MscVrPpTbcl_ObjectIdentity = ObjectIdentity
mscVrPpTbcl = _MscVrPpTbcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2)
)
_MscVrPpTbclRowStatusTable_Object = MibTable
mscVrPpTbclRowStatusTable = _MscVrPpTbclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpTbclRowStatusTable.setStatus("mandatory")
_MscVrPpTbclRowStatusEntry_Object = MibTableRow
mscVrPpTbclRowStatusEntry = _MscVrPpTbclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 1, 1)
)
mscVrPpTbclRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclRowStatusEntry.setStatus("mandatory")
_MscVrPpTbclRowStatus_Type = RowStatus
_MscVrPpTbclRowStatus_Object = MibTableColumn
mscVrPpTbclRowStatus = _MscVrPpTbclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 1, 1, 1),
    _MscVrPpTbclRowStatus_Type()
)
mscVrPpTbclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclRowStatus.setStatus("mandatory")
_MscVrPpTbclComponentName_Type = DisplayString
_MscVrPpTbclComponentName_Object = MibTableColumn
mscVrPpTbclComponentName = _MscVrPpTbclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 1, 1, 2),
    _MscVrPpTbclComponentName_Type()
)
mscVrPpTbclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclComponentName.setStatus("mandatory")
_MscVrPpTbclStorageType_Type = StorageType
_MscVrPpTbclStorageType_Object = MibTableColumn
mscVrPpTbclStorageType = _MscVrPpTbclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 1, 1, 4),
    _MscVrPpTbclStorageType_Type()
)
mscVrPpTbclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclStorageType.setStatus("mandatory")
_MscVrPpTbclIndex_Type = NonReplicated
_MscVrPpTbclIndex_Object = MibTableColumn
mscVrPpTbclIndex = _MscVrPpTbclIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 1, 1, 10),
    _MscVrPpTbclIndex_Type()
)
mscVrPpTbclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpTbclIndex.setStatus("mandatory")
_MscVrPpTbclNs_ObjectIdentity = ObjectIdentity
mscVrPpTbclNs = _MscVrPpTbclNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2)
)
_MscVrPpTbclNsRowStatusTable_Object = MibTable
mscVrPpTbclNsRowStatusTable = _MscVrPpTbclNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpTbclNsRowStatusTable.setStatus("mandatory")
_MscVrPpTbclNsRowStatusEntry_Object = MibTableRow
mscVrPpTbclNsRowStatusEntry = _MscVrPpTbclNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 1, 1)
)
mscVrPpTbclNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclNsRowStatusEntry.setStatus("mandatory")
_MscVrPpTbclNsRowStatus_Type = RowStatus
_MscVrPpTbclNsRowStatus_Object = MibTableColumn
mscVrPpTbclNsRowStatus = _MscVrPpTbclNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 1, 1, 1),
    _MscVrPpTbclNsRowStatus_Type()
)
mscVrPpTbclNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclNsRowStatus.setStatus("mandatory")
_MscVrPpTbclNsComponentName_Type = DisplayString
_MscVrPpTbclNsComponentName_Object = MibTableColumn
mscVrPpTbclNsComponentName = _MscVrPpTbclNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 1, 1, 2),
    _MscVrPpTbclNsComponentName_Type()
)
mscVrPpTbclNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclNsComponentName.setStatus("mandatory")
_MscVrPpTbclNsStorageType_Type = StorageType
_MscVrPpTbclNsStorageType_Object = MibTableColumn
mscVrPpTbclNsStorageType = _MscVrPpTbclNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 1, 1, 4),
    _MscVrPpTbclNsStorageType_Type()
)
mscVrPpTbclNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclNsStorageType.setStatus("mandatory")
_MscVrPpTbclNsIndex_Type = NonReplicated
_MscVrPpTbclNsIndex_Object = MibTableColumn
mscVrPpTbclNsIndex = _MscVrPpTbclNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 1, 1, 10),
    _MscVrPpTbclNsIndex_Type()
)
mscVrPpTbclNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpTbclNsIndex.setStatus("mandatory")
_MscVrPpTbclNsProvTable_Object = MibTable
mscVrPpTbclNsProvTable = _MscVrPpTbclNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpTbclNsProvTable.setStatus("mandatory")
_MscVrPpTbclNsProvEntry_Object = MibTableRow
mscVrPpTbclNsProvEntry = _MscVrPpTbclNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 10, 1)
)
mscVrPpTbclNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclNsProvEntry.setStatus("mandatory")


class _MscVrPpTbclNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpTbclNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpTbclNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpTbclNsIncomingFilter_Object = MibTableColumn
mscVrPpTbclNsIncomingFilter = _MscVrPpTbclNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 10, 1, 2),
    _MscVrPpTbclNsIncomingFilter_Type()
)
mscVrPpTbclNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclNsIncomingFilter.setStatus("mandatory")


class _MscVrPpTbclNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpTbclNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpTbclNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpTbclNsOutgoingFilter_Object = MibTableColumn
mscVrPpTbclNsOutgoingFilter = _MscVrPpTbclNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 2, 10, 1, 3),
    _MscVrPpTbclNsOutgoingFilter_Type()
)
mscVrPpTbclNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclNsOutgoingFilter.setStatus("mandatory")
_MscVrPpTbclProvTable_Object = MibTable
mscVrPpTbclProvTable = _MscVrPpTbclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpTbclProvTable.setStatus("mandatory")
_MscVrPpTbclProvEntry_Object = MibTableRow
mscVrPpTbclProvEntry = _MscVrPpTbclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10, 1)
)
mscVrPpTbclProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclProvEntry.setStatus("mandatory")


class _MscVrPpTbclTranslateIpx_Type(Integer32):
    """Custom type mscVrPpTbclTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpTbclTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpTbclTranslateIpx_Object = MibTableColumn
mscVrPpTbclTranslateIpx = _MscVrPpTbclTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10, 1, 1),
    _MscVrPpTbclTranslateIpx_Type()
)
mscVrPpTbclTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclTranslateIpx.setStatus("mandatory")


class _MscVrPpTbclFragmentIp_Type(Integer32):
    """Custom type mscVrPpTbclFragmentIp based on Integer32"""
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


_MscVrPpTbclFragmentIp_Type.__name__ = "Integer32"
_MscVrPpTbclFragmentIp_Object = MibTableColumn
mscVrPpTbclFragmentIp = _MscVrPpTbclFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10, 1, 2),
    _MscVrPpTbclFragmentIp_Type()
)
mscVrPpTbclFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclFragmentIp.setStatus("mandatory")


class _MscVrPpTbclServiceClass_Type(Integer32):
    """Custom type mscVrPpTbclServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpTbclServiceClass_Type.__name__ = "Integer32"
_MscVrPpTbclServiceClass_Object = MibTableColumn
mscVrPpTbclServiceClass = _MscVrPpTbclServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10, 1, 3),
    _MscVrPpTbclServiceClass_Type()
)
mscVrPpTbclServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclServiceClass.setStatus("mandatory")


class _MscVrPpTbclConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpTbclConvertArpMacAddress based on Integer32"""
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


_MscVrPpTbclConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpTbclConvertArpMacAddress_Object = MibTableColumn
mscVrPpTbclConvertArpMacAddress = _MscVrPpTbclConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10, 1, 4),
    _MscVrPpTbclConvertArpMacAddress_Type()
)
mscVrPpTbclConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpTbclPortNum_Type(Unsigned32):
    """Custom type mscVrPpTbclPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpTbclPortNum_Type.__name__ = "Unsigned32"
_MscVrPpTbclPortNum_Object = MibTableColumn
mscVrPpTbclPortNum = _MscVrPpTbclPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 10, 1, 5),
    _MscVrPpTbclPortNum_Type()
)
mscVrPpTbclPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclPortNum.setStatus("mandatory")
_MscVrPpTbclTbProvTable_Object = MibTable
mscVrPpTbclTbProvTable = _MscVrPpTbclTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrPpTbclTbProvTable.setStatus("mandatory")
_MscVrPpTbclTbProvEntry_Object = MibTableRow
mscVrPpTbclTbProvEntry = _MscVrPpTbclTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 11, 1)
)
mscVrPpTbclTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclTbProvEntry.setStatus("mandatory")


class _MscVrPpTbclSecureOption_Type(Integer32):
    """Custom type mscVrPpTbclSecureOption based on Integer32"""
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


_MscVrPpTbclSecureOption_Type.__name__ = "Integer32"
_MscVrPpTbclSecureOption_Object = MibTableColumn
mscVrPpTbclSecureOption = _MscVrPpTbclSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 11, 1, 1),
    _MscVrPpTbclSecureOption_Type()
)
mscVrPpTbclSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclSecureOption.setStatus("mandatory")
_MscVrPpTbclStpProvTable_Object = MibTable
mscVrPpTbclStpProvTable = _MscVrPpTbclStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12)
)
if mibBuilder.loadTexts:
    mscVrPpTbclStpProvTable.setStatus("mandatory")
_MscVrPpTbclStpProvEntry_Object = MibTableRow
mscVrPpTbclStpProvEntry = _MscVrPpTbclStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1)
)
mscVrPpTbclStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclStpProvEntry.setStatus("mandatory")


class _MscVrPpTbclAdminStatus_Type(Integer32):
    """Custom type mscVrPpTbclAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpTbclAdminStatus_Type.__name__ = "Integer32"
_MscVrPpTbclAdminStatus_Object = MibTableColumn
mscVrPpTbclAdminStatus = _MscVrPpTbclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1, 1),
    _MscVrPpTbclAdminStatus_Type()
)
mscVrPpTbclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclAdminStatus.setStatus("mandatory")


class _MscVrPpTbclPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpTbclPortStateStpControl based on Integer32"""
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


_MscVrPpTbclPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpTbclPortStateStpControl_Object = MibTableColumn
mscVrPpTbclPortStateStpControl = _MscVrPpTbclPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1, 2),
    _MscVrPpTbclPortStateStpControl_Type()
)
mscVrPpTbclPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclPortStateStpControl.setStatus("mandatory")


class _MscVrPpTbclStpTypeProv_Type(Integer32):
    """Custom type mscVrPpTbclStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpTbclStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpTbclStpTypeProv_Object = MibTableColumn
mscVrPpTbclStpTypeProv = _MscVrPpTbclStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1, 3),
    _MscVrPpTbclStpTypeProv_Type()
)
mscVrPpTbclStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclStpTypeProv.setStatus("mandatory")


class _MscVrPpTbclPortPriority_Type(Unsigned32):
    """Custom type mscVrPpTbclPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbclPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpTbclPortPriority_Object = MibTableColumn
mscVrPpTbclPortPriority = _MscVrPpTbclPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1, 4),
    _MscVrPpTbclPortPriority_Type()
)
mscVrPpTbclPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclPortPriority.setStatus("mandatory")


class _MscVrPpTbclPathCost_Type(Unsigned32):
    """Custom type mscVrPpTbclPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbclPathCost_Type.__name__ = "Unsigned32"
_MscVrPpTbclPathCost_Object = MibTableColumn
mscVrPpTbclPathCost = _MscVrPpTbclPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1, 5),
    _MscVrPpTbclPathCost_Type()
)
mscVrPpTbclPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclPathCost.setStatus("mandatory")


class _MscVrPpTbclPathCostMethod_Type(Integer32):
    """Custom type mscVrPpTbclPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpTbclPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpTbclPathCostMethod_Object = MibTableColumn
mscVrPpTbclPathCostMethod = _MscVrPpTbclPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 12, 1, 6),
    _MscVrPpTbclPathCostMethod_Type()
)
mscVrPpTbclPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclPathCostMethod.setStatus("mandatory")
_MscVrPpTbclDIProvTable_Object = MibTable
mscVrPpTbclDIProvTable = _MscVrPpTbclDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 13)
)
if mibBuilder.loadTexts:
    mscVrPpTbclDIProvTable.setStatus("mandatory")
_MscVrPpTbclDIProvEntry_Object = MibTableRow
mscVrPpTbclDIProvEntry = _MscVrPpTbclDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 13, 1)
)
mscVrPpTbclDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclDIProvEntry.setStatus("mandatory")


class _MscVrPpTbclDomainNum_Type(Unsigned32):
    """Custom type mscVrPpTbclDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpTbclDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpTbclDomainNum_Object = MibTableColumn
mscVrPpTbclDomainNum = _MscVrPpTbclDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 13, 1, 1),
    _MscVrPpTbclDomainNum_Type()
)
mscVrPpTbclDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclDomainNum.setStatus("mandatory")


class _MscVrPpTbclPreserveDomain_Type(Integer32):
    """Custom type mscVrPpTbclPreserveDomain based on Integer32"""
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


_MscVrPpTbclPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpTbclPreserveDomain_Object = MibTableColumn
mscVrPpTbclPreserveDomain = _MscVrPpTbclPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 13, 1, 2),
    _MscVrPpTbclPreserveDomain_Type()
)
mscVrPpTbclPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbclPreserveDomain.setStatus("mandatory")
_MscVrPpTbclStateTable_Object = MibTable
mscVrPpTbclStateTable = _MscVrPpTbclStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 14)
)
if mibBuilder.loadTexts:
    mscVrPpTbclStateTable.setStatus("mandatory")
_MscVrPpTbclStateEntry_Object = MibTableRow
mscVrPpTbclStateEntry = _MscVrPpTbclStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 14, 1)
)
mscVrPpTbclStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclStateEntry.setStatus("mandatory")


class _MscVrPpTbclAdminState_Type(Integer32):
    """Custom type mscVrPpTbclAdminState based on Integer32"""
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


_MscVrPpTbclAdminState_Type.__name__ = "Integer32"
_MscVrPpTbclAdminState_Object = MibTableColumn
mscVrPpTbclAdminState = _MscVrPpTbclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 14, 1, 1),
    _MscVrPpTbclAdminState_Type()
)
mscVrPpTbclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclAdminState.setStatus("mandatory")


class _MscVrPpTbclOperationalState_Type(Integer32):
    """Custom type mscVrPpTbclOperationalState based on Integer32"""
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


_MscVrPpTbclOperationalState_Type.__name__ = "Integer32"
_MscVrPpTbclOperationalState_Object = MibTableColumn
mscVrPpTbclOperationalState = _MscVrPpTbclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 14, 1, 2),
    _MscVrPpTbclOperationalState_Type()
)
mscVrPpTbclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclOperationalState.setStatus("mandatory")


class _MscVrPpTbclUsageState_Type(Integer32):
    """Custom type mscVrPpTbclUsageState based on Integer32"""
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


_MscVrPpTbclUsageState_Type.__name__ = "Integer32"
_MscVrPpTbclUsageState_Object = MibTableColumn
mscVrPpTbclUsageState = _MscVrPpTbclUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 14, 1, 3),
    _MscVrPpTbclUsageState_Type()
)
mscVrPpTbclUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclUsageState.setStatus("mandatory")
_MscVrPpTbclOperStatusTable_Object = MibTable
mscVrPpTbclOperStatusTable = _MscVrPpTbclOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 15)
)
if mibBuilder.loadTexts:
    mscVrPpTbclOperStatusTable.setStatus("mandatory")
_MscVrPpTbclOperStatusEntry_Object = MibTableRow
mscVrPpTbclOperStatusEntry = _MscVrPpTbclOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 15, 1)
)
mscVrPpTbclOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclOperStatusEntry.setStatus("mandatory")


class _MscVrPpTbclSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpTbclSnmpOperStatus based on Integer32"""
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


_MscVrPpTbclSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpTbclSnmpOperStatus_Object = MibTableColumn
mscVrPpTbclSnmpOperStatus = _MscVrPpTbclSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 15, 1, 1),
    _MscVrPpTbclSnmpOperStatus_Type()
)
mscVrPpTbclSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclSnmpOperStatus.setStatus("mandatory")
_MscVrPpTbclOperTable_Object = MibTable
mscVrPpTbclOperTable = _MscVrPpTbclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16)
)
if mibBuilder.loadTexts:
    mscVrPpTbclOperTable.setStatus("mandatory")
_MscVrPpTbclOperEntry_Object = MibTableRow
mscVrPpTbclOperEntry = _MscVrPpTbclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1)
)
mscVrPpTbclOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclOperEntry.setStatus("mandatory")


class _MscVrPpTbclPortName_Type(AsciiString):
    """Custom type mscVrPpTbclPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpTbclPortName_Type.__name__ = "AsciiString"
_MscVrPpTbclPortName_Object = MibTableColumn
mscVrPpTbclPortName = _MscVrPpTbclPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 1),
    _MscVrPpTbclPortName_Type()
)
mscVrPpTbclPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclPortName.setStatus("mandatory")


class _MscVrPpTbclUpTime_Type(Unsigned32):
    """Custom type mscVrPpTbclUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbclUpTime_Type.__name__ = "Unsigned32"
_MscVrPpTbclUpTime_Object = MibTableColumn
mscVrPpTbclUpTime = _MscVrPpTbclUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 3),
    _MscVrPpTbclUpTime_Type()
)
mscVrPpTbclUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclUpTime.setStatus("mandatory")


class _MscVrPpTbclDownTime_Type(Unsigned32):
    """Custom type mscVrPpTbclDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbclDownTime_Type.__name__ = "Unsigned32"
_MscVrPpTbclDownTime_Object = MibTableColumn
mscVrPpTbclDownTime = _MscVrPpTbclDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 4),
    _MscVrPpTbclDownTime_Type()
)
mscVrPpTbclDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDownTime.setStatus("mandatory")


class _MscVrPpTbclBridgingMode_Type(Integer32):
    """Custom type mscVrPpTbclBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpTbclBridgingMode_Type.__name__ = "Integer32"
_MscVrPpTbclBridgingMode_Object = MibTableColumn
mscVrPpTbclBridgingMode = _MscVrPpTbclBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 5),
    _MscVrPpTbclBridgingMode_Type()
)
mscVrPpTbclBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclBridgingMode.setStatus("mandatory")


class _MscVrPpTbclBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpTbclBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpTbclBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpTbclBridgePortConfig_Object = MibTableColumn
mscVrPpTbclBridgePortConfig = _MscVrPpTbclBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 6),
    _MscVrPpTbclBridgePortConfig_Type()
)
mscVrPpTbclBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclBridgePortConfig.setStatus("mandatory")


class _MscVrPpTbclBridgePortType_Type(Integer32):
    """Custom type mscVrPpTbclBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpTbclBridgePortType_Type.__name__ = "Integer32"
_MscVrPpTbclBridgePortType_Object = MibTableColumn
mscVrPpTbclBridgePortType = _MscVrPpTbclBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 7),
    _MscVrPpTbclBridgePortType_Type()
)
mscVrPpTbclBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclBridgePortType.setStatus("mandatory")


class _MscVrPpTbclIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpTbclIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbclIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpTbclIfIndex_Object = MibTableColumn
mscVrPpTbclIfIndex = _MscVrPpTbclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 8),
    _MscVrPpTbclIfIndex_Type()
)
mscVrPpTbclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclIfIndex.setStatus("mandatory")
_MscVrPpTbclDelayExceededDiscards_Type = Counter32
_MscVrPpTbclDelayExceededDiscards_Object = MibTableColumn
mscVrPpTbclDelayExceededDiscards = _MscVrPpTbclDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 10),
    _MscVrPpTbclDelayExceededDiscards_Type()
)
mscVrPpTbclDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDelayExceededDiscards.setStatus("mandatory")
_MscVrPpTbclMtuExceededDiscards_Type = Counter32
_MscVrPpTbclMtuExceededDiscards_Object = MibTableColumn
mscVrPpTbclMtuExceededDiscards = _MscVrPpTbclMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 16, 1, 11),
    _MscVrPpTbclMtuExceededDiscards_Type()
)
mscVrPpTbclMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclMtuExceededDiscards.setStatus("mandatory")
_MscVrPpTbclTbOperTable_Object = MibTable
mscVrPpTbclTbOperTable = _MscVrPpTbclTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17)
)
if mibBuilder.loadTexts:
    mscVrPpTbclTbOperTable.setStatus("mandatory")
_MscVrPpTbclTbOperEntry_Object = MibTableRow
mscVrPpTbclTbOperEntry = _MscVrPpTbclTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1)
)
mscVrPpTbclTbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclTbOperEntry.setStatus("mandatory")


class _MscVrPpTbclMaxInfo_Type(Unsigned32):
    """Custom type mscVrPpTbclMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbclMaxInfo_Type.__name__ = "Unsigned32"
_MscVrPpTbclMaxInfo_Object = MibTableColumn
mscVrPpTbclMaxInfo = _MscVrPpTbclMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 2),
    _MscVrPpTbclMaxInfo_Type()
)
mscVrPpTbclMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclMaxInfo.setStatus("mandatory")
_MscVrPpTbclBadVerifyDiscards_Type = Counter32
_MscVrPpTbclBadVerifyDiscards_Object = MibTableColumn
mscVrPpTbclBadVerifyDiscards = _MscVrPpTbclBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 3),
    _MscVrPpTbclBadVerifyDiscards_Type()
)
mscVrPpTbclBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclBadVerifyDiscards.setStatus("mandatory")
_MscVrPpTbclUnicastNoMatches_Type = Counter32
_MscVrPpTbclUnicastNoMatches_Object = MibTableColumn
mscVrPpTbclUnicastNoMatches = _MscVrPpTbclUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 4),
    _MscVrPpTbclUnicastNoMatches_Type()
)
mscVrPpTbclUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclUnicastNoMatches.setStatus("mandatory")
_MscVrPpTbclStaticEntryDiscards_Type = Counter32
_MscVrPpTbclStaticEntryDiscards_Object = MibTableColumn
mscVrPpTbclStaticEntryDiscards = _MscVrPpTbclStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 5),
    _MscVrPpTbclStaticEntryDiscards_Type()
)
mscVrPpTbclStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclStaticEntryDiscards.setStatus("mandatory")
_MscVrPpTbclDynamicEntryDiscards_Type = Counter32
_MscVrPpTbclDynamicEntryDiscards_Object = MibTableColumn
mscVrPpTbclDynamicEntryDiscards = _MscVrPpTbclDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 6),
    _MscVrPpTbclDynamicEntryDiscards_Type()
)
mscVrPpTbclDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDynamicEntryDiscards.setStatus("mandatory")
_MscVrPpTbclLearningDiscards_Type = Counter32
_MscVrPpTbclLearningDiscards_Object = MibTableColumn
mscVrPpTbclLearningDiscards = _MscVrPpTbclLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 7),
    _MscVrPpTbclLearningDiscards_Type()
)
mscVrPpTbclLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclLearningDiscards.setStatus("mandatory")
_MscVrPpTbclInDiscards_Type = Counter32
_MscVrPpTbclInDiscards_Object = MibTableColumn
mscVrPpTbclInDiscards = _MscVrPpTbclInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 8),
    _MscVrPpTbclInDiscards_Type()
)
mscVrPpTbclInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclInDiscards.setStatus("mandatory")
_MscVrPpTbclInFrames_Type = Counter32
_MscVrPpTbclInFrames_Object = MibTableColumn
mscVrPpTbclInFrames = _MscVrPpTbclInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 9),
    _MscVrPpTbclInFrames_Type()
)
mscVrPpTbclInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclInFrames.setStatus("mandatory")
_MscVrPpTbclOutFrames_Type = Counter32
_MscVrPpTbclOutFrames_Object = MibTableColumn
mscVrPpTbclOutFrames = _MscVrPpTbclOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 17, 1, 10),
    _MscVrPpTbclOutFrames_Type()
)
mscVrPpTbclOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclOutFrames.setStatus("mandatory")
_MscVrPpTbclStpOperTable_Object = MibTable
mscVrPpTbclStpOperTable = _MscVrPpTbclStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18)
)
if mibBuilder.loadTexts:
    mscVrPpTbclStpOperTable.setStatus("mandatory")
_MscVrPpTbclStpOperEntry_Object = MibTableRow
mscVrPpTbclStpOperEntry = _MscVrPpTbclStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1)
)
mscVrPpTbclStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclStpOperEntry.setStatus("mandatory")


class _MscVrPpTbclStpPortState_Type(Integer32):
    """Custom type mscVrPpTbclStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpTbclStpPortState_Type.__name__ = "Integer32"
_MscVrPpTbclStpPortState_Object = MibTableColumn
mscVrPpTbclStpPortState = _MscVrPpTbclStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 2),
    _MscVrPpTbclStpPortState_Type()
)
mscVrPpTbclStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclStpPortState.setStatus("mandatory")


class _MscVrPpTbclStpTypeOper_Type(Integer32):
    """Custom type mscVrPpTbclStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpTbclStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpTbclStpTypeOper_Object = MibTableColumn
mscVrPpTbclStpTypeOper = _MscVrPpTbclStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 3),
    _MscVrPpTbclStpTypeOper_Type()
)
mscVrPpTbclStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclStpTypeOper.setStatus("mandatory")


class _MscVrPpTbclDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpTbclDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbclDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpTbclDesignatedCost_Object = MibTableColumn
mscVrPpTbclDesignatedCost = _MscVrPpTbclDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 4),
    _MscVrPpTbclDesignatedCost_Type()
)
mscVrPpTbclDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDesignatedCost.setStatus("mandatory")


class _MscVrPpTbclPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpTbclPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbclPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpTbclPathCostOper_Object = MibTableColumn
mscVrPpTbclPathCostOper = _MscVrPpTbclPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 5),
    _MscVrPpTbclPathCostOper_Type()
)
mscVrPpTbclPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclPathCostOper.setStatus("mandatory")


class _MscVrPpTbclDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpTbclDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbclDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpTbclDesignatedBridge_Object = MibTableColumn
mscVrPpTbclDesignatedBridge = _MscVrPpTbclDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 6),
    _MscVrPpTbclDesignatedBridge_Type()
)
mscVrPpTbclDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDesignatedBridge.setStatus("mandatory")


class _MscVrPpTbclDesignatedPort_Type(Hex):
    """Custom type mscVrPpTbclDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbclDesignatedPort_Type.__name__ = "Hex"
_MscVrPpTbclDesignatedPort_Object = MibTableColumn
mscVrPpTbclDesignatedPort = _MscVrPpTbclDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 7),
    _MscVrPpTbclDesignatedPort_Type()
)
mscVrPpTbclDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDesignatedPort.setStatus("mandatory")
_MscVrPpTbclForwardTransitions_Type = Counter32
_MscVrPpTbclForwardTransitions_Object = MibTableColumn
mscVrPpTbclForwardTransitions = _MscVrPpTbclForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 8),
    _MscVrPpTbclForwardTransitions_Type()
)
mscVrPpTbclForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclForwardTransitions.setStatus("mandatory")
_MscVrPpTbclBlockingDiscards_Type = Counter32
_MscVrPpTbclBlockingDiscards_Object = MibTableColumn
mscVrPpTbclBlockingDiscards = _MscVrPpTbclBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 9),
    _MscVrPpTbclBlockingDiscards_Type()
)
mscVrPpTbclBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclBlockingDiscards.setStatus("mandatory")


class _MscVrPpTbclDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpTbclDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbclDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpTbclDesignatedRoot_Object = MibTableColumn
mscVrPpTbclDesignatedRoot = _MscVrPpTbclDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 18, 1, 10),
    _MscVrPpTbclDesignatedRoot_Type()
)
mscVrPpTbclDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclDesignatedRoot.setStatus("mandatory")
_MscVrPpTbclStatsTable_Object = MibTable
mscVrPpTbclStatsTable = _MscVrPpTbclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19)
)
if mibBuilder.loadTexts:
    mscVrPpTbclStatsTable.setStatus("mandatory")
_MscVrPpTbclStatsEntry_Object = MibTableRow
mscVrPpTbclStatsEntry = _MscVrPpTbclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19, 1)
)
mscVrPpTbclStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbclStatsEntry.setStatus("mandatory")
_MscVrPpTbclBadAbstractDiscards_Type = Counter32
_MscVrPpTbclBadAbstractDiscards_Object = MibTableColumn
mscVrPpTbclBadAbstractDiscards = _MscVrPpTbclBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19, 1, 1),
    _MscVrPpTbclBadAbstractDiscards_Type()
)
mscVrPpTbclBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclBadAbstractDiscards.setStatus("mandatory")
_MscVrPpTbclTinygramFramesIn_Type = Counter32
_MscVrPpTbclTinygramFramesIn_Object = MibTableColumn
mscVrPpTbclTinygramFramesIn = _MscVrPpTbclTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19, 1, 2),
    _MscVrPpTbclTinygramFramesIn_Type()
)
mscVrPpTbclTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclTinygramFramesIn.setStatus("mandatory")
_MscVrPpTbclTinygramFramesOut_Type = Counter32
_MscVrPpTbclTinygramFramesOut_Object = MibTableColumn
mscVrPpTbclTinygramFramesOut = _MscVrPpTbclTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19, 1, 3),
    _MscVrPpTbclTinygramFramesOut_Type()
)
mscVrPpTbclTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclTinygramFramesOut.setStatus("mandatory")
_MscVrPpTbclInFilterDiscards_Type = Counter32
_MscVrPpTbclInFilterDiscards_Object = MibTableColumn
mscVrPpTbclInFilterDiscards = _MscVrPpTbclInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19, 1, 4),
    _MscVrPpTbclInFilterDiscards_Type()
)
mscVrPpTbclInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclInFilterDiscards.setStatus("mandatory")
_MscVrPpTbclOutFilterDiscards_Type = Counter32
_MscVrPpTbclOutFilterDiscards_Object = MibTableColumn
mscVrPpTbclOutFilterDiscards = _MscVrPpTbclOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 2, 19, 1, 5),
    _MscVrPpTbclOutFilterDiscards_Type()
)
mscVrPpTbclOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbclOutFilterDiscards.setStatus("mandatory")
_MscVrPpFddiETB_ObjectIdentity = ObjectIdentity
mscVrPpFddiETB = _MscVrPpFddiETB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3)
)
_MscVrPpFddiETBRowStatusTable_Object = MibTable
mscVrPpFddiETBRowStatusTable = _MscVrPpFddiETBRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBRowStatusTable.setStatus("mandatory")
_MscVrPpFddiETBRowStatusEntry_Object = MibTableRow
mscVrPpFddiETBRowStatusEntry = _MscVrPpFddiETBRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 1, 1)
)
mscVrPpFddiETBRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBRowStatusEntry.setStatus("mandatory")
_MscVrPpFddiETBRowStatus_Type = RowStatus
_MscVrPpFddiETBRowStatus_Object = MibTableColumn
mscVrPpFddiETBRowStatus = _MscVrPpFddiETBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 1, 1, 1),
    _MscVrPpFddiETBRowStatus_Type()
)
mscVrPpFddiETBRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBRowStatus.setStatus("mandatory")
_MscVrPpFddiETBComponentName_Type = DisplayString
_MscVrPpFddiETBComponentName_Object = MibTableColumn
mscVrPpFddiETBComponentName = _MscVrPpFddiETBComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 1, 1, 2),
    _MscVrPpFddiETBComponentName_Type()
)
mscVrPpFddiETBComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBComponentName.setStatus("mandatory")
_MscVrPpFddiETBStorageType_Type = StorageType
_MscVrPpFddiETBStorageType_Object = MibTableColumn
mscVrPpFddiETBStorageType = _MscVrPpFddiETBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 1, 1, 4),
    _MscVrPpFddiETBStorageType_Type()
)
mscVrPpFddiETBStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBStorageType.setStatus("mandatory")
_MscVrPpFddiETBIndex_Type = NonReplicated
_MscVrPpFddiETBIndex_Object = MibTableColumn
mscVrPpFddiETBIndex = _MscVrPpFddiETBIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 1, 1, 10),
    _MscVrPpFddiETBIndex_Type()
)
mscVrPpFddiETBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpFddiETBIndex.setStatus("mandatory")
_MscVrPpFddiETBNs_ObjectIdentity = ObjectIdentity
mscVrPpFddiETBNs = _MscVrPpFddiETBNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2)
)
_MscVrPpFddiETBNsRowStatusTable_Object = MibTable
mscVrPpFddiETBNsRowStatusTable = _MscVrPpFddiETBNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsRowStatusTable.setStatus("mandatory")
_MscVrPpFddiETBNsRowStatusEntry_Object = MibTableRow
mscVrPpFddiETBNsRowStatusEntry = _MscVrPpFddiETBNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 1, 1)
)
mscVrPpFddiETBNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsRowStatusEntry.setStatus("mandatory")
_MscVrPpFddiETBNsRowStatus_Type = RowStatus
_MscVrPpFddiETBNsRowStatus_Object = MibTableColumn
mscVrPpFddiETBNsRowStatus = _MscVrPpFddiETBNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 1, 1, 1),
    _MscVrPpFddiETBNsRowStatus_Type()
)
mscVrPpFddiETBNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsRowStatus.setStatus("mandatory")
_MscVrPpFddiETBNsComponentName_Type = DisplayString
_MscVrPpFddiETBNsComponentName_Object = MibTableColumn
mscVrPpFddiETBNsComponentName = _MscVrPpFddiETBNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 1, 1, 2),
    _MscVrPpFddiETBNsComponentName_Type()
)
mscVrPpFddiETBNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsComponentName.setStatus("mandatory")
_MscVrPpFddiETBNsStorageType_Type = StorageType
_MscVrPpFddiETBNsStorageType_Object = MibTableColumn
mscVrPpFddiETBNsStorageType = _MscVrPpFddiETBNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 1, 1, 4),
    _MscVrPpFddiETBNsStorageType_Type()
)
mscVrPpFddiETBNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsStorageType.setStatus("mandatory")
_MscVrPpFddiETBNsIndex_Type = NonReplicated
_MscVrPpFddiETBNsIndex_Object = MibTableColumn
mscVrPpFddiETBNsIndex = _MscVrPpFddiETBNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 1, 1, 10),
    _MscVrPpFddiETBNsIndex_Type()
)
mscVrPpFddiETBNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsIndex.setStatus("mandatory")
_MscVrPpFddiETBNsProvTable_Object = MibTable
mscVrPpFddiETBNsProvTable = _MscVrPpFddiETBNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsProvTable.setStatus("mandatory")
_MscVrPpFddiETBNsProvEntry_Object = MibTableRow
mscVrPpFddiETBNsProvEntry = _MscVrPpFddiETBNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 10, 1)
)
mscVrPpFddiETBNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsProvEntry.setStatus("mandatory")


class _MscVrPpFddiETBNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpFddiETBNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpFddiETBNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpFddiETBNsIncomingFilter_Object = MibTableColumn
mscVrPpFddiETBNsIncomingFilter = _MscVrPpFddiETBNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 10, 1, 2),
    _MscVrPpFddiETBNsIncomingFilter_Type()
)
mscVrPpFddiETBNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsIncomingFilter.setStatus("mandatory")


class _MscVrPpFddiETBNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpFddiETBNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpFddiETBNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpFddiETBNsOutgoingFilter_Object = MibTableColumn
mscVrPpFddiETBNsOutgoingFilter = _MscVrPpFddiETBNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 2, 10, 1, 3),
    _MscVrPpFddiETBNsOutgoingFilter_Type()
)
mscVrPpFddiETBNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBNsOutgoingFilter.setStatus("mandatory")
_MscVrPpFddiETBProvTable_Object = MibTable
mscVrPpFddiETBProvTable = _MscVrPpFddiETBProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBProvTable.setStatus("mandatory")
_MscVrPpFddiETBProvEntry_Object = MibTableRow
mscVrPpFddiETBProvEntry = _MscVrPpFddiETBProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10, 1)
)
mscVrPpFddiETBProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBProvEntry.setStatus("mandatory")


class _MscVrPpFddiETBTranslateIpx_Type(Integer32):
    """Custom type mscVrPpFddiETBTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpFddiETBTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpFddiETBTranslateIpx_Object = MibTableColumn
mscVrPpFddiETBTranslateIpx = _MscVrPpFddiETBTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10, 1, 1),
    _MscVrPpFddiETBTranslateIpx_Type()
)
mscVrPpFddiETBTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBTranslateIpx.setStatus("mandatory")


class _MscVrPpFddiETBFragmentIp_Type(Integer32):
    """Custom type mscVrPpFddiETBFragmentIp based on Integer32"""
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


_MscVrPpFddiETBFragmentIp_Type.__name__ = "Integer32"
_MscVrPpFddiETBFragmentIp_Object = MibTableColumn
mscVrPpFddiETBFragmentIp = _MscVrPpFddiETBFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10, 1, 2),
    _MscVrPpFddiETBFragmentIp_Type()
)
mscVrPpFddiETBFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBFragmentIp.setStatus("mandatory")


class _MscVrPpFddiETBServiceClass_Type(Integer32):
    """Custom type mscVrPpFddiETBServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpFddiETBServiceClass_Type.__name__ = "Integer32"
_MscVrPpFddiETBServiceClass_Object = MibTableColumn
mscVrPpFddiETBServiceClass = _MscVrPpFddiETBServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10, 1, 3),
    _MscVrPpFddiETBServiceClass_Type()
)
mscVrPpFddiETBServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBServiceClass.setStatus("mandatory")


class _MscVrPpFddiETBConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpFddiETBConvertArpMacAddress based on Integer32"""
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


_MscVrPpFddiETBConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpFddiETBConvertArpMacAddress_Object = MibTableColumn
mscVrPpFddiETBConvertArpMacAddress = _MscVrPpFddiETBConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10, 1, 4),
    _MscVrPpFddiETBConvertArpMacAddress_Type()
)
mscVrPpFddiETBConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpFddiETBPortNum_Type(Unsigned32):
    """Custom type mscVrPpFddiETBPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpFddiETBPortNum_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBPortNum_Object = MibTableColumn
mscVrPpFddiETBPortNum = _MscVrPpFddiETBPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 10, 1, 5),
    _MscVrPpFddiETBPortNum_Type()
)
mscVrPpFddiETBPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPortNum.setStatus("mandatory")
_MscVrPpFddiETBTbProvTable_Object = MibTable
mscVrPpFddiETBTbProvTable = _MscVrPpFddiETBTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBTbProvTable.setStatus("mandatory")
_MscVrPpFddiETBTbProvEntry_Object = MibTableRow
mscVrPpFddiETBTbProvEntry = _MscVrPpFddiETBTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 11, 1)
)
mscVrPpFddiETBTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBTbProvEntry.setStatus("mandatory")


class _MscVrPpFddiETBSecureOption_Type(Integer32):
    """Custom type mscVrPpFddiETBSecureOption based on Integer32"""
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


_MscVrPpFddiETBSecureOption_Type.__name__ = "Integer32"
_MscVrPpFddiETBSecureOption_Object = MibTableColumn
mscVrPpFddiETBSecureOption = _MscVrPpFddiETBSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 11, 1, 1),
    _MscVrPpFddiETBSecureOption_Type()
)
mscVrPpFddiETBSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBSecureOption.setStatus("mandatory")
_MscVrPpFddiETBStpProvTable_Object = MibTable
mscVrPpFddiETBStpProvTable = _MscVrPpFddiETBStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpProvTable.setStatus("mandatory")
_MscVrPpFddiETBStpProvEntry_Object = MibTableRow
mscVrPpFddiETBStpProvEntry = _MscVrPpFddiETBStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1)
)
mscVrPpFddiETBStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpProvEntry.setStatus("mandatory")


class _MscVrPpFddiETBAdminStatus_Type(Integer32):
    """Custom type mscVrPpFddiETBAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpFddiETBAdminStatus_Type.__name__ = "Integer32"
_MscVrPpFddiETBAdminStatus_Object = MibTableColumn
mscVrPpFddiETBAdminStatus = _MscVrPpFddiETBAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1, 1),
    _MscVrPpFddiETBAdminStatus_Type()
)
mscVrPpFddiETBAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBAdminStatus.setStatus("mandatory")


class _MscVrPpFddiETBPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpFddiETBPortStateStpControl based on Integer32"""
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


_MscVrPpFddiETBPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpFddiETBPortStateStpControl_Object = MibTableColumn
mscVrPpFddiETBPortStateStpControl = _MscVrPpFddiETBPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1, 2),
    _MscVrPpFddiETBPortStateStpControl_Type()
)
mscVrPpFddiETBPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPortStateStpControl.setStatus("mandatory")


class _MscVrPpFddiETBStpTypeProv_Type(Integer32):
    """Custom type mscVrPpFddiETBStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpFddiETBStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpFddiETBStpTypeProv_Object = MibTableColumn
mscVrPpFddiETBStpTypeProv = _MscVrPpFddiETBStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1, 3),
    _MscVrPpFddiETBStpTypeProv_Type()
)
mscVrPpFddiETBStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpTypeProv.setStatus("mandatory")


class _MscVrPpFddiETBPortPriority_Type(Unsigned32):
    """Custom type mscVrPpFddiETBPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpFddiETBPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBPortPriority_Object = MibTableColumn
mscVrPpFddiETBPortPriority = _MscVrPpFddiETBPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1, 4),
    _MscVrPpFddiETBPortPriority_Type()
)
mscVrPpFddiETBPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPortPriority.setStatus("mandatory")


class _MscVrPpFddiETBPathCost_Type(Unsigned32):
    """Custom type mscVrPpFddiETBPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpFddiETBPathCost_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBPathCost_Object = MibTableColumn
mscVrPpFddiETBPathCost = _MscVrPpFddiETBPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1, 5),
    _MscVrPpFddiETBPathCost_Type()
)
mscVrPpFddiETBPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPathCost.setStatus("mandatory")


class _MscVrPpFddiETBPathCostMethod_Type(Integer32):
    """Custom type mscVrPpFddiETBPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpFddiETBPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpFddiETBPathCostMethod_Object = MibTableColumn
mscVrPpFddiETBPathCostMethod = _MscVrPpFddiETBPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 12, 1, 6),
    _MscVrPpFddiETBPathCostMethod_Type()
)
mscVrPpFddiETBPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPathCostMethod.setStatus("mandatory")
_MscVrPpFddiETBDIProvTable_Object = MibTable
mscVrPpFddiETBDIProvTable = _MscVrPpFddiETBDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 13)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBDIProvTable.setStatus("mandatory")
_MscVrPpFddiETBDIProvEntry_Object = MibTableRow
mscVrPpFddiETBDIProvEntry = _MscVrPpFddiETBDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 13, 1)
)
mscVrPpFddiETBDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBDIProvEntry.setStatus("mandatory")


class _MscVrPpFddiETBDomainNum_Type(Unsigned32):
    """Custom type mscVrPpFddiETBDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpFddiETBDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBDomainNum_Object = MibTableColumn
mscVrPpFddiETBDomainNum = _MscVrPpFddiETBDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 13, 1, 1),
    _MscVrPpFddiETBDomainNum_Type()
)
mscVrPpFddiETBDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDomainNum.setStatus("mandatory")


class _MscVrPpFddiETBPreserveDomain_Type(Integer32):
    """Custom type mscVrPpFddiETBPreserveDomain based on Integer32"""
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


_MscVrPpFddiETBPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpFddiETBPreserveDomain_Object = MibTableColumn
mscVrPpFddiETBPreserveDomain = _MscVrPpFddiETBPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 13, 1, 2),
    _MscVrPpFddiETBPreserveDomain_Type()
)
mscVrPpFddiETBPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPreserveDomain.setStatus("mandatory")
_MscVrPpFddiETBStateTable_Object = MibTable
mscVrPpFddiETBStateTable = _MscVrPpFddiETBStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 14)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStateTable.setStatus("mandatory")
_MscVrPpFddiETBStateEntry_Object = MibTableRow
mscVrPpFddiETBStateEntry = _MscVrPpFddiETBStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 14, 1)
)
mscVrPpFddiETBStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStateEntry.setStatus("mandatory")


class _MscVrPpFddiETBAdminState_Type(Integer32):
    """Custom type mscVrPpFddiETBAdminState based on Integer32"""
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


_MscVrPpFddiETBAdminState_Type.__name__ = "Integer32"
_MscVrPpFddiETBAdminState_Object = MibTableColumn
mscVrPpFddiETBAdminState = _MscVrPpFddiETBAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 14, 1, 1),
    _MscVrPpFddiETBAdminState_Type()
)
mscVrPpFddiETBAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBAdminState.setStatus("mandatory")


class _MscVrPpFddiETBOperationalState_Type(Integer32):
    """Custom type mscVrPpFddiETBOperationalState based on Integer32"""
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


_MscVrPpFddiETBOperationalState_Type.__name__ = "Integer32"
_MscVrPpFddiETBOperationalState_Object = MibTableColumn
mscVrPpFddiETBOperationalState = _MscVrPpFddiETBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 14, 1, 2),
    _MscVrPpFddiETBOperationalState_Type()
)
mscVrPpFddiETBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBOperationalState.setStatus("mandatory")


class _MscVrPpFddiETBUsageState_Type(Integer32):
    """Custom type mscVrPpFddiETBUsageState based on Integer32"""
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


_MscVrPpFddiETBUsageState_Type.__name__ = "Integer32"
_MscVrPpFddiETBUsageState_Object = MibTableColumn
mscVrPpFddiETBUsageState = _MscVrPpFddiETBUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 14, 1, 3),
    _MscVrPpFddiETBUsageState_Type()
)
mscVrPpFddiETBUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBUsageState.setStatus("mandatory")
_MscVrPpFddiETBOperStatusTable_Object = MibTable
mscVrPpFddiETBOperStatusTable = _MscVrPpFddiETBOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 15)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBOperStatusTable.setStatus("mandatory")
_MscVrPpFddiETBOperStatusEntry_Object = MibTableRow
mscVrPpFddiETBOperStatusEntry = _MscVrPpFddiETBOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 15, 1)
)
mscVrPpFddiETBOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBOperStatusEntry.setStatus("mandatory")


class _MscVrPpFddiETBSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpFddiETBSnmpOperStatus based on Integer32"""
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


_MscVrPpFddiETBSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpFddiETBSnmpOperStatus_Object = MibTableColumn
mscVrPpFddiETBSnmpOperStatus = _MscVrPpFddiETBSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 15, 1, 1),
    _MscVrPpFddiETBSnmpOperStatus_Type()
)
mscVrPpFddiETBSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBSnmpOperStatus.setStatus("mandatory")
_MscVrPpFddiETBOperTable_Object = MibTable
mscVrPpFddiETBOperTable = _MscVrPpFddiETBOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBOperTable.setStatus("mandatory")
_MscVrPpFddiETBOperEntry_Object = MibTableRow
mscVrPpFddiETBOperEntry = _MscVrPpFddiETBOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1)
)
mscVrPpFddiETBOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBOperEntry.setStatus("mandatory")


class _MscVrPpFddiETBPortName_Type(AsciiString):
    """Custom type mscVrPpFddiETBPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpFddiETBPortName_Type.__name__ = "AsciiString"
_MscVrPpFddiETBPortName_Object = MibTableColumn
mscVrPpFddiETBPortName = _MscVrPpFddiETBPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 1),
    _MscVrPpFddiETBPortName_Type()
)
mscVrPpFddiETBPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPortName.setStatus("mandatory")


class _MscVrPpFddiETBUpTime_Type(Unsigned32):
    """Custom type mscVrPpFddiETBUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpFddiETBUpTime_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBUpTime_Object = MibTableColumn
mscVrPpFddiETBUpTime = _MscVrPpFddiETBUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 3),
    _MscVrPpFddiETBUpTime_Type()
)
mscVrPpFddiETBUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBUpTime.setStatus("mandatory")


class _MscVrPpFddiETBDownTime_Type(Unsigned32):
    """Custom type mscVrPpFddiETBDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpFddiETBDownTime_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBDownTime_Object = MibTableColumn
mscVrPpFddiETBDownTime = _MscVrPpFddiETBDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 4),
    _MscVrPpFddiETBDownTime_Type()
)
mscVrPpFddiETBDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDownTime.setStatus("mandatory")


class _MscVrPpFddiETBBridgingMode_Type(Integer32):
    """Custom type mscVrPpFddiETBBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpFddiETBBridgingMode_Type.__name__ = "Integer32"
_MscVrPpFddiETBBridgingMode_Object = MibTableColumn
mscVrPpFddiETBBridgingMode = _MscVrPpFddiETBBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 5),
    _MscVrPpFddiETBBridgingMode_Type()
)
mscVrPpFddiETBBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBBridgingMode.setStatus("mandatory")


class _MscVrPpFddiETBBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpFddiETBBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpFddiETBBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpFddiETBBridgePortConfig_Object = MibTableColumn
mscVrPpFddiETBBridgePortConfig = _MscVrPpFddiETBBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 6),
    _MscVrPpFddiETBBridgePortConfig_Type()
)
mscVrPpFddiETBBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBBridgePortConfig.setStatus("mandatory")


class _MscVrPpFddiETBBridgePortType_Type(Integer32):
    """Custom type mscVrPpFddiETBBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpFddiETBBridgePortType_Type.__name__ = "Integer32"
_MscVrPpFddiETBBridgePortType_Object = MibTableColumn
mscVrPpFddiETBBridgePortType = _MscVrPpFddiETBBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 7),
    _MscVrPpFddiETBBridgePortType_Type()
)
mscVrPpFddiETBBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBBridgePortType.setStatus("mandatory")


class _MscVrPpFddiETBIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpFddiETBIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpFddiETBIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpFddiETBIfIndex_Object = MibTableColumn
mscVrPpFddiETBIfIndex = _MscVrPpFddiETBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 8),
    _MscVrPpFddiETBIfIndex_Type()
)
mscVrPpFddiETBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBIfIndex.setStatus("mandatory")
_MscVrPpFddiETBDelayExceededDiscards_Type = Counter32
_MscVrPpFddiETBDelayExceededDiscards_Object = MibTableColumn
mscVrPpFddiETBDelayExceededDiscards = _MscVrPpFddiETBDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 10),
    _MscVrPpFddiETBDelayExceededDiscards_Type()
)
mscVrPpFddiETBDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDelayExceededDiscards.setStatus("mandatory")
_MscVrPpFddiETBMtuExceededDiscards_Type = Counter32
_MscVrPpFddiETBMtuExceededDiscards_Object = MibTableColumn
mscVrPpFddiETBMtuExceededDiscards = _MscVrPpFddiETBMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 16, 1, 11),
    _MscVrPpFddiETBMtuExceededDiscards_Type()
)
mscVrPpFddiETBMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBMtuExceededDiscards.setStatus("mandatory")
_MscVrPpFddiETBTbOperTable_Object = MibTable
mscVrPpFddiETBTbOperTable = _MscVrPpFddiETBTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBTbOperTable.setStatus("mandatory")
_MscVrPpFddiETBTbOperEntry_Object = MibTableRow
mscVrPpFddiETBTbOperEntry = _MscVrPpFddiETBTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1)
)
mscVrPpFddiETBTbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBTbOperEntry.setStatus("mandatory")


class _MscVrPpFddiETBMaxInfo_Type(Unsigned32):
    """Custom type mscVrPpFddiETBMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpFddiETBMaxInfo_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBMaxInfo_Object = MibTableColumn
mscVrPpFddiETBMaxInfo = _MscVrPpFddiETBMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 2),
    _MscVrPpFddiETBMaxInfo_Type()
)
mscVrPpFddiETBMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBMaxInfo.setStatus("mandatory")
_MscVrPpFddiETBBadVerifyDiscards_Type = Counter32
_MscVrPpFddiETBBadVerifyDiscards_Object = MibTableColumn
mscVrPpFddiETBBadVerifyDiscards = _MscVrPpFddiETBBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 3),
    _MscVrPpFddiETBBadVerifyDiscards_Type()
)
mscVrPpFddiETBBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBBadVerifyDiscards.setStatus("mandatory")
_MscVrPpFddiETBUnicastNoMatches_Type = Counter32
_MscVrPpFddiETBUnicastNoMatches_Object = MibTableColumn
mscVrPpFddiETBUnicastNoMatches = _MscVrPpFddiETBUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 4),
    _MscVrPpFddiETBUnicastNoMatches_Type()
)
mscVrPpFddiETBUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBUnicastNoMatches.setStatus("mandatory")
_MscVrPpFddiETBStaticEntryDiscards_Type = Counter32
_MscVrPpFddiETBStaticEntryDiscards_Object = MibTableColumn
mscVrPpFddiETBStaticEntryDiscards = _MscVrPpFddiETBStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 5),
    _MscVrPpFddiETBStaticEntryDiscards_Type()
)
mscVrPpFddiETBStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBStaticEntryDiscards.setStatus("mandatory")
_MscVrPpFddiETBDynamicEntryDiscards_Type = Counter32
_MscVrPpFddiETBDynamicEntryDiscards_Object = MibTableColumn
mscVrPpFddiETBDynamicEntryDiscards = _MscVrPpFddiETBDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 6),
    _MscVrPpFddiETBDynamicEntryDiscards_Type()
)
mscVrPpFddiETBDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDynamicEntryDiscards.setStatus("mandatory")
_MscVrPpFddiETBLearningDiscards_Type = Counter32
_MscVrPpFddiETBLearningDiscards_Object = MibTableColumn
mscVrPpFddiETBLearningDiscards = _MscVrPpFddiETBLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 7),
    _MscVrPpFddiETBLearningDiscards_Type()
)
mscVrPpFddiETBLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBLearningDiscards.setStatus("mandatory")
_MscVrPpFddiETBInDiscards_Type = Counter32
_MscVrPpFddiETBInDiscards_Object = MibTableColumn
mscVrPpFddiETBInDiscards = _MscVrPpFddiETBInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 8),
    _MscVrPpFddiETBInDiscards_Type()
)
mscVrPpFddiETBInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBInDiscards.setStatus("mandatory")
_MscVrPpFddiETBInFrames_Type = Counter32
_MscVrPpFddiETBInFrames_Object = MibTableColumn
mscVrPpFddiETBInFrames = _MscVrPpFddiETBInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 9),
    _MscVrPpFddiETBInFrames_Type()
)
mscVrPpFddiETBInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBInFrames.setStatus("mandatory")
_MscVrPpFddiETBOutFrames_Type = Counter32
_MscVrPpFddiETBOutFrames_Object = MibTableColumn
mscVrPpFddiETBOutFrames = _MscVrPpFddiETBOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 17, 1, 10),
    _MscVrPpFddiETBOutFrames_Type()
)
mscVrPpFddiETBOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBOutFrames.setStatus("mandatory")
_MscVrPpFddiETBStpOperTable_Object = MibTable
mscVrPpFddiETBStpOperTable = _MscVrPpFddiETBStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpOperTable.setStatus("mandatory")
_MscVrPpFddiETBStpOperEntry_Object = MibTableRow
mscVrPpFddiETBStpOperEntry = _MscVrPpFddiETBStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1)
)
mscVrPpFddiETBStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpOperEntry.setStatus("mandatory")


class _MscVrPpFddiETBStpPortState_Type(Integer32):
    """Custom type mscVrPpFddiETBStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpFddiETBStpPortState_Type.__name__ = "Integer32"
_MscVrPpFddiETBStpPortState_Object = MibTableColumn
mscVrPpFddiETBStpPortState = _MscVrPpFddiETBStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 2),
    _MscVrPpFddiETBStpPortState_Type()
)
mscVrPpFddiETBStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpPortState.setStatus("mandatory")


class _MscVrPpFddiETBStpTypeOper_Type(Integer32):
    """Custom type mscVrPpFddiETBStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpFddiETBStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpFddiETBStpTypeOper_Object = MibTableColumn
mscVrPpFddiETBStpTypeOper = _MscVrPpFddiETBStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 3),
    _MscVrPpFddiETBStpTypeOper_Type()
)
mscVrPpFddiETBStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBStpTypeOper.setStatus("mandatory")


class _MscVrPpFddiETBDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpFddiETBDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpFddiETBDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBDesignatedCost_Object = MibTableColumn
mscVrPpFddiETBDesignatedCost = _MscVrPpFddiETBDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 4),
    _MscVrPpFddiETBDesignatedCost_Type()
)
mscVrPpFddiETBDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDesignatedCost.setStatus("mandatory")


class _MscVrPpFddiETBPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpFddiETBPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpFddiETBPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpFddiETBPathCostOper_Object = MibTableColumn
mscVrPpFddiETBPathCostOper = _MscVrPpFddiETBPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 5),
    _MscVrPpFddiETBPathCostOper_Type()
)
mscVrPpFddiETBPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBPathCostOper.setStatus("mandatory")


class _MscVrPpFddiETBDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpFddiETBDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpFddiETBDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpFddiETBDesignatedBridge_Object = MibTableColumn
mscVrPpFddiETBDesignatedBridge = _MscVrPpFddiETBDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 6),
    _MscVrPpFddiETBDesignatedBridge_Type()
)
mscVrPpFddiETBDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDesignatedBridge.setStatus("mandatory")


class _MscVrPpFddiETBDesignatedPort_Type(Hex):
    """Custom type mscVrPpFddiETBDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpFddiETBDesignatedPort_Type.__name__ = "Hex"
_MscVrPpFddiETBDesignatedPort_Object = MibTableColumn
mscVrPpFddiETBDesignatedPort = _MscVrPpFddiETBDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 7),
    _MscVrPpFddiETBDesignatedPort_Type()
)
mscVrPpFddiETBDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDesignatedPort.setStatus("mandatory")
_MscVrPpFddiETBForwardTransitions_Type = Counter32
_MscVrPpFddiETBForwardTransitions_Object = MibTableColumn
mscVrPpFddiETBForwardTransitions = _MscVrPpFddiETBForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 8),
    _MscVrPpFddiETBForwardTransitions_Type()
)
mscVrPpFddiETBForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBForwardTransitions.setStatus("mandatory")
_MscVrPpFddiETBBlockingDiscards_Type = Counter32
_MscVrPpFddiETBBlockingDiscards_Object = MibTableColumn
mscVrPpFddiETBBlockingDiscards = _MscVrPpFddiETBBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 9),
    _MscVrPpFddiETBBlockingDiscards_Type()
)
mscVrPpFddiETBBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBBlockingDiscards.setStatus("mandatory")


class _MscVrPpFddiETBDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpFddiETBDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpFddiETBDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpFddiETBDesignatedRoot_Object = MibTableColumn
mscVrPpFddiETBDesignatedRoot = _MscVrPpFddiETBDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 18, 1, 10),
    _MscVrPpFddiETBDesignatedRoot_Type()
)
mscVrPpFddiETBDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBDesignatedRoot.setStatus("mandatory")
_MscVrPpFddiETBStatsTable_Object = MibTable
mscVrPpFddiETBStatsTable = _MscVrPpFddiETBStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19)
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStatsTable.setStatus("mandatory")
_MscVrPpFddiETBStatsEntry_Object = MibTableRow
mscVrPpFddiETBStatsEntry = _MscVrPpFddiETBStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19, 1)
)
mscVrPpFddiETBStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpFddiETBStatsEntry.setStatus("mandatory")
_MscVrPpFddiETBBadAbstractDiscards_Type = Counter32
_MscVrPpFddiETBBadAbstractDiscards_Object = MibTableColumn
mscVrPpFddiETBBadAbstractDiscards = _MscVrPpFddiETBBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19, 1, 1),
    _MscVrPpFddiETBBadAbstractDiscards_Type()
)
mscVrPpFddiETBBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBBadAbstractDiscards.setStatus("mandatory")
_MscVrPpFddiETBTinygramFramesIn_Type = Counter32
_MscVrPpFddiETBTinygramFramesIn_Object = MibTableColumn
mscVrPpFddiETBTinygramFramesIn = _MscVrPpFddiETBTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19, 1, 2),
    _MscVrPpFddiETBTinygramFramesIn_Type()
)
mscVrPpFddiETBTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBTinygramFramesIn.setStatus("mandatory")
_MscVrPpFddiETBTinygramFramesOut_Type = Counter32
_MscVrPpFddiETBTinygramFramesOut_Object = MibTableColumn
mscVrPpFddiETBTinygramFramesOut = _MscVrPpFddiETBTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19, 1, 3),
    _MscVrPpFddiETBTinygramFramesOut_Type()
)
mscVrPpFddiETBTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBTinygramFramesOut.setStatus("mandatory")
_MscVrPpFddiETBInFilterDiscards_Type = Counter32
_MscVrPpFddiETBInFilterDiscards_Object = MibTableColumn
mscVrPpFddiETBInFilterDiscards = _MscVrPpFddiETBInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19, 1, 4),
    _MscVrPpFddiETBInFilterDiscards_Type()
)
mscVrPpFddiETBInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBInFilterDiscards.setStatus("mandatory")
_MscVrPpFddiETBOutFilterDiscards_Type = Counter32
_MscVrPpFddiETBOutFilterDiscards_Object = MibTableColumn
mscVrPpFddiETBOutFilterDiscards = _MscVrPpFddiETBOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 3, 19, 1, 5),
    _MscVrPpFddiETBOutFilterDiscards_Type()
)
mscVrPpFddiETBOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpFddiETBOutFilterDiscards.setStatus("mandatory")
_MscVrPpTbp_ObjectIdentity = ObjectIdentity
mscVrPpTbp = _MscVrPpTbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4)
)
_MscVrPpTbpRowStatusTable_Object = MibTable
mscVrPpTbpRowStatusTable = _MscVrPpTbpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrPpTbpRowStatusTable.setStatus("mandatory")
_MscVrPpTbpRowStatusEntry_Object = MibTableRow
mscVrPpTbpRowStatusEntry = _MscVrPpTbpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 1, 1)
)
mscVrPpTbpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpRowStatusEntry.setStatus("mandatory")
_MscVrPpTbpRowStatus_Type = RowStatus
_MscVrPpTbpRowStatus_Object = MibTableColumn
mscVrPpTbpRowStatus = _MscVrPpTbpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 1, 1, 1),
    _MscVrPpTbpRowStatus_Type()
)
mscVrPpTbpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpRowStatus.setStatus("mandatory")
_MscVrPpTbpComponentName_Type = DisplayString
_MscVrPpTbpComponentName_Object = MibTableColumn
mscVrPpTbpComponentName = _MscVrPpTbpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 1, 1, 2),
    _MscVrPpTbpComponentName_Type()
)
mscVrPpTbpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpComponentName.setStatus("mandatory")
_MscVrPpTbpStorageType_Type = StorageType
_MscVrPpTbpStorageType_Object = MibTableColumn
mscVrPpTbpStorageType = _MscVrPpTbpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 1, 1, 4),
    _MscVrPpTbpStorageType_Type()
)
mscVrPpTbpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpStorageType.setStatus("mandatory")
_MscVrPpTbpIndex_Type = NonReplicated
_MscVrPpTbpIndex_Object = MibTableColumn
mscVrPpTbpIndex = _MscVrPpTbpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 1, 1, 10),
    _MscVrPpTbpIndex_Type()
)
mscVrPpTbpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpTbpIndex.setStatus("mandatory")
_MscVrPpTbpNs_ObjectIdentity = ObjectIdentity
mscVrPpTbpNs = _MscVrPpTbpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2)
)
_MscVrPpTbpNsRowStatusTable_Object = MibTable
mscVrPpTbpNsRowStatusTable = _MscVrPpTbpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpTbpNsRowStatusTable.setStatus("mandatory")
_MscVrPpTbpNsRowStatusEntry_Object = MibTableRow
mscVrPpTbpNsRowStatusEntry = _MscVrPpTbpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 1, 1)
)
mscVrPpTbpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpNsRowStatusEntry.setStatus("mandatory")
_MscVrPpTbpNsRowStatus_Type = RowStatus
_MscVrPpTbpNsRowStatus_Object = MibTableColumn
mscVrPpTbpNsRowStatus = _MscVrPpTbpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 1, 1, 1),
    _MscVrPpTbpNsRowStatus_Type()
)
mscVrPpTbpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpNsRowStatus.setStatus("mandatory")
_MscVrPpTbpNsComponentName_Type = DisplayString
_MscVrPpTbpNsComponentName_Object = MibTableColumn
mscVrPpTbpNsComponentName = _MscVrPpTbpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 1, 1, 2),
    _MscVrPpTbpNsComponentName_Type()
)
mscVrPpTbpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpNsComponentName.setStatus("mandatory")
_MscVrPpTbpNsStorageType_Type = StorageType
_MscVrPpTbpNsStorageType_Object = MibTableColumn
mscVrPpTbpNsStorageType = _MscVrPpTbpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 1, 1, 4),
    _MscVrPpTbpNsStorageType_Type()
)
mscVrPpTbpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpNsStorageType.setStatus("mandatory")
_MscVrPpTbpNsIndex_Type = NonReplicated
_MscVrPpTbpNsIndex_Object = MibTableColumn
mscVrPpTbpNsIndex = _MscVrPpTbpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 1, 1, 10),
    _MscVrPpTbpNsIndex_Type()
)
mscVrPpTbpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpTbpNsIndex.setStatus("mandatory")
_MscVrPpTbpNsProvTable_Object = MibTable
mscVrPpTbpNsProvTable = _MscVrPpTbpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpTbpNsProvTable.setStatus("mandatory")
_MscVrPpTbpNsProvEntry_Object = MibTableRow
mscVrPpTbpNsProvEntry = _MscVrPpTbpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 10, 1)
)
mscVrPpTbpNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpNsProvEntry.setStatus("mandatory")


class _MscVrPpTbpNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpTbpNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpTbpNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpTbpNsIncomingFilter_Object = MibTableColumn
mscVrPpTbpNsIncomingFilter = _MscVrPpTbpNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 10, 1, 2),
    _MscVrPpTbpNsIncomingFilter_Type()
)
mscVrPpTbpNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpNsIncomingFilter.setStatus("mandatory")


class _MscVrPpTbpNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpTbpNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpTbpNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpTbpNsOutgoingFilter_Object = MibTableColumn
mscVrPpTbpNsOutgoingFilter = _MscVrPpTbpNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 2, 10, 1, 3),
    _MscVrPpTbpNsOutgoingFilter_Type()
)
mscVrPpTbpNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpNsOutgoingFilter.setStatus("mandatory")
_MscVrPpTbpProvTable_Object = MibTable
mscVrPpTbpProvTable = _MscVrPpTbpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrPpTbpProvTable.setStatus("mandatory")
_MscVrPpTbpProvEntry_Object = MibTableRow
mscVrPpTbpProvEntry = _MscVrPpTbpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10, 1)
)
mscVrPpTbpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpProvEntry.setStatus("mandatory")


class _MscVrPpTbpTranslateIpx_Type(Integer32):
    """Custom type mscVrPpTbpTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpTbpTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpTbpTranslateIpx_Object = MibTableColumn
mscVrPpTbpTranslateIpx = _MscVrPpTbpTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10, 1, 1),
    _MscVrPpTbpTranslateIpx_Type()
)
mscVrPpTbpTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpTranslateIpx.setStatus("mandatory")


class _MscVrPpTbpFragmentIp_Type(Integer32):
    """Custom type mscVrPpTbpFragmentIp based on Integer32"""
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


_MscVrPpTbpFragmentIp_Type.__name__ = "Integer32"
_MscVrPpTbpFragmentIp_Object = MibTableColumn
mscVrPpTbpFragmentIp = _MscVrPpTbpFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10, 1, 2),
    _MscVrPpTbpFragmentIp_Type()
)
mscVrPpTbpFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpFragmentIp.setStatus("mandatory")


class _MscVrPpTbpServiceClass_Type(Integer32):
    """Custom type mscVrPpTbpServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpTbpServiceClass_Type.__name__ = "Integer32"
_MscVrPpTbpServiceClass_Object = MibTableColumn
mscVrPpTbpServiceClass = _MscVrPpTbpServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10, 1, 3),
    _MscVrPpTbpServiceClass_Type()
)
mscVrPpTbpServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpServiceClass.setStatus("mandatory")


class _MscVrPpTbpConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpTbpConvertArpMacAddress based on Integer32"""
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


_MscVrPpTbpConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpTbpConvertArpMacAddress_Object = MibTableColumn
mscVrPpTbpConvertArpMacAddress = _MscVrPpTbpConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10, 1, 4),
    _MscVrPpTbpConvertArpMacAddress_Type()
)
mscVrPpTbpConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpTbpPortNum_Type(Unsigned32):
    """Custom type mscVrPpTbpPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpTbpPortNum_Type.__name__ = "Unsigned32"
_MscVrPpTbpPortNum_Object = MibTableColumn
mscVrPpTbpPortNum = _MscVrPpTbpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 10, 1, 5),
    _MscVrPpTbpPortNum_Type()
)
mscVrPpTbpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpPortNum.setStatus("mandatory")
_MscVrPpTbpTbProvTable_Object = MibTable
mscVrPpTbpTbProvTable = _MscVrPpTbpTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 11)
)
if mibBuilder.loadTexts:
    mscVrPpTbpTbProvTable.setStatus("mandatory")
_MscVrPpTbpTbProvEntry_Object = MibTableRow
mscVrPpTbpTbProvEntry = _MscVrPpTbpTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 11, 1)
)
mscVrPpTbpTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpTbProvEntry.setStatus("mandatory")


class _MscVrPpTbpSecureOption_Type(Integer32):
    """Custom type mscVrPpTbpSecureOption based on Integer32"""
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


_MscVrPpTbpSecureOption_Type.__name__ = "Integer32"
_MscVrPpTbpSecureOption_Object = MibTableColumn
mscVrPpTbpSecureOption = _MscVrPpTbpSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 11, 1, 1),
    _MscVrPpTbpSecureOption_Type()
)
mscVrPpTbpSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpSecureOption.setStatus("mandatory")
_MscVrPpTbpStpProvTable_Object = MibTable
mscVrPpTbpStpProvTable = _MscVrPpTbpStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12)
)
if mibBuilder.loadTexts:
    mscVrPpTbpStpProvTable.setStatus("mandatory")
_MscVrPpTbpStpProvEntry_Object = MibTableRow
mscVrPpTbpStpProvEntry = _MscVrPpTbpStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1)
)
mscVrPpTbpStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpStpProvEntry.setStatus("mandatory")


class _MscVrPpTbpAdminStatus_Type(Integer32):
    """Custom type mscVrPpTbpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpTbpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpTbpAdminStatus_Object = MibTableColumn
mscVrPpTbpAdminStatus = _MscVrPpTbpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1, 1),
    _MscVrPpTbpAdminStatus_Type()
)
mscVrPpTbpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpAdminStatus.setStatus("mandatory")


class _MscVrPpTbpPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpTbpPortStateStpControl based on Integer32"""
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


_MscVrPpTbpPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpTbpPortStateStpControl_Object = MibTableColumn
mscVrPpTbpPortStateStpControl = _MscVrPpTbpPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1, 2),
    _MscVrPpTbpPortStateStpControl_Type()
)
mscVrPpTbpPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpPortStateStpControl.setStatus("mandatory")


class _MscVrPpTbpStpTypeProv_Type(Integer32):
    """Custom type mscVrPpTbpStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpTbpStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpTbpStpTypeProv_Object = MibTableColumn
mscVrPpTbpStpTypeProv = _MscVrPpTbpStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1, 3),
    _MscVrPpTbpStpTypeProv_Type()
)
mscVrPpTbpStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpStpTypeProv.setStatus("mandatory")


class _MscVrPpTbpPortPriority_Type(Unsigned32):
    """Custom type mscVrPpTbpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbpPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpTbpPortPriority_Object = MibTableColumn
mscVrPpTbpPortPriority = _MscVrPpTbpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1, 4),
    _MscVrPpTbpPortPriority_Type()
)
mscVrPpTbpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpPortPriority.setStatus("mandatory")


class _MscVrPpTbpPathCost_Type(Unsigned32):
    """Custom type mscVrPpTbpPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbpPathCost_Type.__name__ = "Unsigned32"
_MscVrPpTbpPathCost_Object = MibTableColumn
mscVrPpTbpPathCost = _MscVrPpTbpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1, 5),
    _MscVrPpTbpPathCost_Type()
)
mscVrPpTbpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpPathCost.setStatus("mandatory")


class _MscVrPpTbpPathCostMethod_Type(Integer32):
    """Custom type mscVrPpTbpPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpTbpPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpTbpPathCostMethod_Object = MibTableColumn
mscVrPpTbpPathCostMethod = _MscVrPpTbpPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 12, 1, 6),
    _MscVrPpTbpPathCostMethod_Type()
)
mscVrPpTbpPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpPathCostMethod.setStatus("mandatory")
_MscVrPpTbpDIProvTable_Object = MibTable
mscVrPpTbpDIProvTable = _MscVrPpTbpDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 13)
)
if mibBuilder.loadTexts:
    mscVrPpTbpDIProvTable.setStatus("mandatory")
_MscVrPpTbpDIProvEntry_Object = MibTableRow
mscVrPpTbpDIProvEntry = _MscVrPpTbpDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 13, 1)
)
mscVrPpTbpDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpDIProvEntry.setStatus("mandatory")


class _MscVrPpTbpDomainNum_Type(Unsigned32):
    """Custom type mscVrPpTbpDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpTbpDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpTbpDomainNum_Object = MibTableColumn
mscVrPpTbpDomainNum = _MscVrPpTbpDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 13, 1, 1),
    _MscVrPpTbpDomainNum_Type()
)
mscVrPpTbpDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpDomainNum.setStatus("mandatory")


class _MscVrPpTbpPreserveDomain_Type(Integer32):
    """Custom type mscVrPpTbpPreserveDomain based on Integer32"""
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


_MscVrPpTbpPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpTbpPreserveDomain_Object = MibTableColumn
mscVrPpTbpPreserveDomain = _MscVrPpTbpPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 13, 1, 2),
    _MscVrPpTbpPreserveDomain_Type()
)
mscVrPpTbpPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbpPreserveDomain.setStatus("mandatory")
_MscVrPpTbpStateTable_Object = MibTable
mscVrPpTbpStateTable = _MscVrPpTbpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 14)
)
if mibBuilder.loadTexts:
    mscVrPpTbpStateTable.setStatus("mandatory")
_MscVrPpTbpStateEntry_Object = MibTableRow
mscVrPpTbpStateEntry = _MscVrPpTbpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 14, 1)
)
mscVrPpTbpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpStateEntry.setStatus("mandatory")


class _MscVrPpTbpAdminState_Type(Integer32):
    """Custom type mscVrPpTbpAdminState based on Integer32"""
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


_MscVrPpTbpAdminState_Type.__name__ = "Integer32"
_MscVrPpTbpAdminState_Object = MibTableColumn
mscVrPpTbpAdminState = _MscVrPpTbpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 14, 1, 1),
    _MscVrPpTbpAdminState_Type()
)
mscVrPpTbpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpAdminState.setStatus("mandatory")


class _MscVrPpTbpOperationalState_Type(Integer32):
    """Custom type mscVrPpTbpOperationalState based on Integer32"""
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


_MscVrPpTbpOperationalState_Type.__name__ = "Integer32"
_MscVrPpTbpOperationalState_Object = MibTableColumn
mscVrPpTbpOperationalState = _MscVrPpTbpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 14, 1, 2),
    _MscVrPpTbpOperationalState_Type()
)
mscVrPpTbpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpOperationalState.setStatus("mandatory")


class _MscVrPpTbpUsageState_Type(Integer32):
    """Custom type mscVrPpTbpUsageState based on Integer32"""
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


_MscVrPpTbpUsageState_Type.__name__ = "Integer32"
_MscVrPpTbpUsageState_Object = MibTableColumn
mscVrPpTbpUsageState = _MscVrPpTbpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 14, 1, 3),
    _MscVrPpTbpUsageState_Type()
)
mscVrPpTbpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpUsageState.setStatus("mandatory")
_MscVrPpTbpOperStatusTable_Object = MibTable
mscVrPpTbpOperStatusTable = _MscVrPpTbpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 15)
)
if mibBuilder.loadTexts:
    mscVrPpTbpOperStatusTable.setStatus("mandatory")
_MscVrPpTbpOperStatusEntry_Object = MibTableRow
mscVrPpTbpOperStatusEntry = _MscVrPpTbpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 15, 1)
)
mscVrPpTbpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpOperStatusEntry.setStatus("mandatory")


class _MscVrPpTbpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpTbpSnmpOperStatus based on Integer32"""
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


_MscVrPpTbpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpTbpSnmpOperStatus_Object = MibTableColumn
mscVrPpTbpSnmpOperStatus = _MscVrPpTbpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 15, 1, 1),
    _MscVrPpTbpSnmpOperStatus_Type()
)
mscVrPpTbpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpSnmpOperStatus.setStatus("mandatory")
_MscVrPpTbpOperTable_Object = MibTable
mscVrPpTbpOperTable = _MscVrPpTbpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16)
)
if mibBuilder.loadTexts:
    mscVrPpTbpOperTable.setStatus("mandatory")
_MscVrPpTbpOperEntry_Object = MibTableRow
mscVrPpTbpOperEntry = _MscVrPpTbpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1)
)
mscVrPpTbpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpOperEntry.setStatus("mandatory")


class _MscVrPpTbpPortName_Type(AsciiString):
    """Custom type mscVrPpTbpPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpTbpPortName_Type.__name__ = "AsciiString"
_MscVrPpTbpPortName_Object = MibTableColumn
mscVrPpTbpPortName = _MscVrPpTbpPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 1),
    _MscVrPpTbpPortName_Type()
)
mscVrPpTbpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpPortName.setStatus("mandatory")


class _MscVrPpTbpUpTime_Type(Unsigned32):
    """Custom type mscVrPpTbpUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbpUpTime_Type.__name__ = "Unsigned32"
_MscVrPpTbpUpTime_Object = MibTableColumn
mscVrPpTbpUpTime = _MscVrPpTbpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 3),
    _MscVrPpTbpUpTime_Type()
)
mscVrPpTbpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpUpTime.setStatus("mandatory")


class _MscVrPpTbpDownTime_Type(Unsigned32):
    """Custom type mscVrPpTbpDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbpDownTime_Type.__name__ = "Unsigned32"
_MscVrPpTbpDownTime_Object = MibTableColumn
mscVrPpTbpDownTime = _MscVrPpTbpDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 4),
    _MscVrPpTbpDownTime_Type()
)
mscVrPpTbpDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDownTime.setStatus("mandatory")


class _MscVrPpTbpBridgingMode_Type(Integer32):
    """Custom type mscVrPpTbpBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpTbpBridgingMode_Type.__name__ = "Integer32"
_MscVrPpTbpBridgingMode_Object = MibTableColumn
mscVrPpTbpBridgingMode = _MscVrPpTbpBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 5),
    _MscVrPpTbpBridgingMode_Type()
)
mscVrPpTbpBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpBridgingMode.setStatus("mandatory")


class _MscVrPpTbpBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpTbpBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpTbpBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpTbpBridgePortConfig_Object = MibTableColumn
mscVrPpTbpBridgePortConfig = _MscVrPpTbpBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 6),
    _MscVrPpTbpBridgePortConfig_Type()
)
mscVrPpTbpBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpBridgePortConfig.setStatus("mandatory")


class _MscVrPpTbpBridgePortType_Type(Integer32):
    """Custom type mscVrPpTbpBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpTbpBridgePortType_Type.__name__ = "Integer32"
_MscVrPpTbpBridgePortType_Object = MibTableColumn
mscVrPpTbpBridgePortType = _MscVrPpTbpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 7),
    _MscVrPpTbpBridgePortType_Type()
)
mscVrPpTbpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpBridgePortType.setStatus("mandatory")


class _MscVrPpTbpIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpTbpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbpIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpTbpIfIndex_Object = MibTableColumn
mscVrPpTbpIfIndex = _MscVrPpTbpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 8),
    _MscVrPpTbpIfIndex_Type()
)
mscVrPpTbpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpIfIndex.setStatus("mandatory")
_MscVrPpTbpDelayExceededDiscards_Type = Counter32
_MscVrPpTbpDelayExceededDiscards_Object = MibTableColumn
mscVrPpTbpDelayExceededDiscards = _MscVrPpTbpDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 10),
    _MscVrPpTbpDelayExceededDiscards_Type()
)
mscVrPpTbpDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDelayExceededDiscards.setStatus("mandatory")
_MscVrPpTbpMtuExceededDiscards_Type = Counter32
_MscVrPpTbpMtuExceededDiscards_Object = MibTableColumn
mscVrPpTbpMtuExceededDiscards = _MscVrPpTbpMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 16, 1, 11),
    _MscVrPpTbpMtuExceededDiscards_Type()
)
mscVrPpTbpMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpMtuExceededDiscards.setStatus("mandatory")
_MscVrPpTbpTbOperTable_Object = MibTable
mscVrPpTbpTbOperTable = _MscVrPpTbpTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17)
)
if mibBuilder.loadTexts:
    mscVrPpTbpTbOperTable.setStatus("mandatory")
_MscVrPpTbpTbOperEntry_Object = MibTableRow
mscVrPpTbpTbOperEntry = _MscVrPpTbpTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1)
)
mscVrPpTbpTbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpTbOperEntry.setStatus("mandatory")


class _MscVrPpTbpMaxInfo_Type(Unsigned32):
    """Custom type mscVrPpTbpMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbpMaxInfo_Type.__name__ = "Unsigned32"
_MscVrPpTbpMaxInfo_Object = MibTableColumn
mscVrPpTbpMaxInfo = _MscVrPpTbpMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 2),
    _MscVrPpTbpMaxInfo_Type()
)
mscVrPpTbpMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpMaxInfo.setStatus("mandatory")
_MscVrPpTbpBadVerifyDiscards_Type = Counter32
_MscVrPpTbpBadVerifyDiscards_Object = MibTableColumn
mscVrPpTbpBadVerifyDiscards = _MscVrPpTbpBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 3),
    _MscVrPpTbpBadVerifyDiscards_Type()
)
mscVrPpTbpBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpBadVerifyDiscards.setStatus("mandatory")
_MscVrPpTbpUnicastNoMatches_Type = Counter32
_MscVrPpTbpUnicastNoMatches_Object = MibTableColumn
mscVrPpTbpUnicastNoMatches = _MscVrPpTbpUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 4),
    _MscVrPpTbpUnicastNoMatches_Type()
)
mscVrPpTbpUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpUnicastNoMatches.setStatus("mandatory")
_MscVrPpTbpStaticEntryDiscards_Type = Counter32
_MscVrPpTbpStaticEntryDiscards_Object = MibTableColumn
mscVrPpTbpStaticEntryDiscards = _MscVrPpTbpStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 5),
    _MscVrPpTbpStaticEntryDiscards_Type()
)
mscVrPpTbpStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpStaticEntryDiscards.setStatus("mandatory")
_MscVrPpTbpDynamicEntryDiscards_Type = Counter32
_MscVrPpTbpDynamicEntryDiscards_Object = MibTableColumn
mscVrPpTbpDynamicEntryDiscards = _MscVrPpTbpDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 6),
    _MscVrPpTbpDynamicEntryDiscards_Type()
)
mscVrPpTbpDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDynamicEntryDiscards.setStatus("mandatory")
_MscVrPpTbpLearningDiscards_Type = Counter32
_MscVrPpTbpLearningDiscards_Object = MibTableColumn
mscVrPpTbpLearningDiscards = _MscVrPpTbpLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 7),
    _MscVrPpTbpLearningDiscards_Type()
)
mscVrPpTbpLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpLearningDiscards.setStatus("mandatory")
_MscVrPpTbpInDiscards_Type = Counter32
_MscVrPpTbpInDiscards_Object = MibTableColumn
mscVrPpTbpInDiscards = _MscVrPpTbpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 8),
    _MscVrPpTbpInDiscards_Type()
)
mscVrPpTbpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpInDiscards.setStatus("mandatory")
_MscVrPpTbpInFrames_Type = Counter32
_MscVrPpTbpInFrames_Object = MibTableColumn
mscVrPpTbpInFrames = _MscVrPpTbpInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 9),
    _MscVrPpTbpInFrames_Type()
)
mscVrPpTbpInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpInFrames.setStatus("mandatory")
_MscVrPpTbpOutFrames_Type = Counter32
_MscVrPpTbpOutFrames_Object = MibTableColumn
mscVrPpTbpOutFrames = _MscVrPpTbpOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 17, 1, 10),
    _MscVrPpTbpOutFrames_Type()
)
mscVrPpTbpOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpOutFrames.setStatus("mandatory")
_MscVrPpTbpStpOperTable_Object = MibTable
mscVrPpTbpStpOperTable = _MscVrPpTbpStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18)
)
if mibBuilder.loadTexts:
    mscVrPpTbpStpOperTable.setStatus("mandatory")
_MscVrPpTbpStpOperEntry_Object = MibTableRow
mscVrPpTbpStpOperEntry = _MscVrPpTbpStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1)
)
mscVrPpTbpStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpStpOperEntry.setStatus("mandatory")


class _MscVrPpTbpStpPortState_Type(Integer32):
    """Custom type mscVrPpTbpStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpTbpStpPortState_Type.__name__ = "Integer32"
_MscVrPpTbpStpPortState_Object = MibTableColumn
mscVrPpTbpStpPortState = _MscVrPpTbpStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 2),
    _MscVrPpTbpStpPortState_Type()
)
mscVrPpTbpStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpStpPortState.setStatus("mandatory")


class _MscVrPpTbpStpTypeOper_Type(Integer32):
    """Custom type mscVrPpTbpStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpTbpStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpTbpStpTypeOper_Object = MibTableColumn
mscVrPpTbpStpTypeOper = _MscVrPpTbpStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 3),
    _MscVrPpTbpStpTypeOper_Type()
)
mscVrPpTbpStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpStpTypeOper.setStatus("mandatory")


class _MscVrPpTbpDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpTbpDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbpDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpTbpDesignatedCost_Object = MibTableColumn
mscVrPpTbpDesignatedCost = _MscVrPpTbpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 4),
    _MscVrPpTbpDesignatedCost_Type()
)
mscVrPpTbpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDesignatedCost.setStatus("mandatory")


class _MscVrPpTbpPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpTbpPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbpPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpTbpPathCostOper_Object = MibTableColumn
mscVrPpTbpPathCostOper = _MscVrPpTbpPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 5),
    _MscVrPpTbpPathCostOper_Type()
)
mscVrPpTbpPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpPathCostOper.setStatus("mandatory")


class _MscVrPpTbpDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpTbpDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbpDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpTbpDesignatedBridge_Object = MibTableColumn
mscVrPpTbpDesignatedBridge = _MscVrPpTbpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 6),
    _MscVrPpTbpDesignatedBridge_Type()
)
mscVrPpTbpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDesignatedBridge.setStatus("mandatory")


class _MscVrPpTbpDesignatedPort_Type(Hex):
    """Custom type mscVrPpTbpDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbpDesignatedPort_Type.__name__ = "Hex"
_MscVrPpTbpDesignatedPort_Object = MibTableColumn
mscVrPpTbpDesignatedPort = _MscVrPpTbpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 7),
    _MscVrPpTbpDesignatedPort_Type()
)
mscVrPpTbpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDesignatedPort.setStatus("mandatory")
_MscVrPpTbpForwardTransitions_Type = Counter32
_MscVrPpTbpForwardTransitions_Object = MibTableColumn
mscVrPpTbpForwardTransitions = _MscVrPpTbpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 8),
    _MscVrPpTbpForwardTransitions_Type()
)
mscVrPpTbpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpForwardTransitions.setStatus("mandatory")
_MscVrPpTbpBlockingDiscards_Type = Counter32
_MscVrPpTbpBlockingDiscards_Object = MibTableColumn
mscVrPpTbpBlockingDiscards = _MscVrPpTbpBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 9),
    _MscVrPpTbpBlockingDiscards_Type()
)
mscVrPpTbpBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpBlockingDiscards.setStatus("mandatory")


class _MscVrPpTbpDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpTbpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbpDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpTbpDesignatedRoot_Object = MibTableColumn
mscVrPpTbpDesignatedRoot = _MscVrPpTbpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 18, 1, 10),
    _MscVrPpTbpDesignatedRoot_Type()
)
mscVrPpTbpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpDesignatedRoot.setStatus("mandatory")
_MscVrPpTbpStatsTable_Object = MibTable
mscVrPpTbpStatsTable = _MscVrPpTbpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19)
)
if mibBuilder.loadTexts:
    mscVrPpTbpStatsTable.setStatus("mandatory")
_MscVrPpTbpStatsEntry_Object = MibTableRow
mscVrPpTbpStatsEntry = _MscVrPpTbpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19, 1)
)
mscVrPpTbpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbpStatsEntry.setStatus("mandatory")
_MscVrPpTbpBadAbstractDiscards_Type = Counter32
_MscVrPpTbpBadAbstractDiscards_Object = MibTableColumn
mscVrPpTbpBadAbstractDiscards = _MscVrPpTbpBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19, 1, 1),
    _MscVrPpTbpBadAbstractDiscards_Type()
)
mscVrPpTbpBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpBadAbstractDiscards.setStatus("mandatory")
_MscVrPpTbpTinygramFramesIn_Type = Counter32
_MscVrPpTbpTinygramFramesIn_Object = MibTableColumn
mscVrPpTbpTinygramFramesIn = _MscVrPpTbpTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19, 1, 2),
    _MscVrPpTbpTinygramFramesIn_Type()
)
mscVrPpTbpTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpTinygramFramesIn.setStatus("mandatory")
_MscVrPpTbpTinygramFramesOut_Type = Counter32
_MscVrPpTbpTinygramFramesOut_Object = MibTableColumn
mscVrPpTbpTinygramFramesOut = _MscVrPpTbpTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19, 1, 3),
    _MscVrPpTbpTinygramFramesOut_Type()
)
mscVrPpTbpTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpTinygramFramesOut.setStatus("mandatory")
_MscVrPpTbpInFilterDiscards_Type = Counter32
_MscVrPpTbpInFilterDiscards_Object = MibTableColumn
mscVrPpTbpInFilterDiscards = _MscVrPpTbpInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19, 1, 4),
    _MscVrPpTbpInFilterDiscards_Type()
)
mscVrPpTbpInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpInFilterDiscards.setStatus("mandatory")
_MscVrPpTbpOutFilterDiscards_Type = Counter32
_MscVrPpTbpOutFilterDiscards_Object = MibTableColumn
mscVrPpTbpOutFilterDiscards = _MscVrPpTbpOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 4, 19, 1, 5),
    _MscVrPpTbpOutFilterDiscards_Type()
)
mscVrPpTbpOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbpOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrBp_ObjectIdentity = ObjectIdentity
mscVrPpSrBp = _MscVrPpSrBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8)
)
_MscVrPpSrBpRowStatusTable_Object = MibTable
mscVrPpSrBpRowStatusTable = _MscVrPpSrBpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpRowStatusTable.setStatus("mandatory")
_MscVrPpSrBpRowStatusEntry_Object = MibTableRow
mscVrPpSrBpRowStatusEntry = _MscVrPpSrBpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 1, 1)
)
mscVrPpSrBpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpRowStatusEntry.setStatus("mandatory")
_MscVrPpSrBpRowStatus_Type = RowStatus
_MscVrPpSrBpRowStatus_Object = MibTableColumn
mscVrPpSrBpRowStatus = _MscVrPpSrBpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 1, 1, 1),
    _MscVrPpSrBpRowStatus_Type()
)
mscVrPpSrBpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpRowStatus.setStatus("mandatory")
_MscVrPpSrBpComponentName_Type = DisplayString
_MscVrPpSrBpComponentName_Object = MibTableColumn
mscVrPpSrBpComponentName = _MscVrPpSrBpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 1, 1, 2),
    _MscVrPpSrBpComponentName_Type()
)
mscVrPpSrBpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpComponentName.setStatus("mandatory")
_MscVrPpSrBpStorageType_Type = StorageType
_MscVrPpSrBpStorageType_Object = MibTableColumn
mscVrPpSrBpStorageType = _MscVrPpSrBpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 1, 1, 4),
    _MscVrPpSrBpStorageType_Type()
)
mscVrPpSrBpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpStorageType.setStatus("mandatory")
_MscVrPpSrBpIndex_Type = NonReplicated
_MscVrPpSrBpIndex_Object = MibTableColumn
mscVrPpSrBpIndex = _MscVrPpSrBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 1, 1, 10),
    _MscVrPpSrBpIndex_Type()
)
mscVrPpSrBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrBpIndex.setStatus("mandatory")
_MscVrPpSrBpNs_ObjectIdentity = ObjectIdentity
mscVrPpSrBpNs = _MscVrPpSrBpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2)
)
_MscVrPpSrBpNsRowStatusTable_Object = MibTable
mscVrPpSrBpNsRowStatusTable = _MscVrPpSrBpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpNsRowStatusTable.setStatus("mandatory")
_MscVrPpSrBpNsRowStatusEntry_Object = MibTableRow
mscVrPpSrBpNsRowStatusEntry = _MscVrPpSrBpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 1, 1)
)
mscVrPpSrBpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpNsRowStatusEntry.setStatus("mandatory")
_MscVrPpSrBpNsRowStatus_Type = RowStatus
_MscVrPpSrBpNsRowStatus_Object = MibTableColumn
mscVrPpSrBpNsRowStatus = _MscVrPpSrBpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 1, 1, 1),
    _MscVrPpSrBpNsRowStatus_Type()
)
mscVrPpSrBpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpNsRowStatus.setStatus("mandatory")
_MscVrPpSrBpNsComponentName_Type = DisplayString
_MscVrPpSrBpNsComponentName_Object = MibTableColumn
mscVrPpSrBpNsComponentName = _MscVrPpSrBpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 1, 1, 2),
    _MscVrPpSrBpNsComponentName_Type()
)
mscVrPpSrBpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpNsComponentName.setStatus("mandatory")
_MscVrPpSrBpNsStorageType_Type = StorageType
_MscVrPpSrBpNsStorageType_Object = MibTableColumn
mscVrPpSrBpNsStorageType = _MscVrPpSrBpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 1, 1, 4),
    _MscVrPpSrBpNsStorageType_Type()
)
mscVrPpSrBpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpNsStorageType.setStatus("mandatory")
_MscVrPpSrBpNsIndex_Type = NonReplicated
_MscVrPpSrBpNsIndex_Object = MibTableColumn
mscVrPpSrBpNsIndex = _MscVrPpSrBpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 1, 1, 10),
    _MscVrPpSrBpNsIndex_Type()
)
mscVrPpSrBpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrBpNsIndex.setStatus("mandatory")
_MscVrPpSrBpNsProvTable_Object = MibTable
mscVrPpSrBpNsProvTable = _MscVrPpSrBpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpNsProvTable.setStatus("mandatory")
_MscVrPpSrBpNsProvEntry_Object = MibTableRow
mscVrPpSrBpNsProvEntry = _MscVrPpSrBpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 10, 1)
)
mscVrPpSrBpNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpNsProvEntry.setStatus("mandatory")


class _MscVrPpSrBpNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpSrBpNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpSrBpNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpSrBpNsIncomingFilter_Object = MibTableColumn
mscVrPpSrBpNsIncomingFilter = _MscVrPpSrBpNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 10, 1, 2),
    _MscVrPpSrBpNsIncomingFilter_Type()
)
mscVrPpSrBpNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpNsIncomingFilter.setStatus("mandatory")


class _MscVrPpSrBpNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpSrBpNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpSrBpNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpSrBpNsOutgoingFilter_Object = MibTableColumn
mscVrPpSrBpNsOutgoingFilter = _MscVrPpSrBpNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 2, 10, 1, 3),
    _MscVrPpSrBpNsOutgoingFilter_Type()
)
mscVrPpSrBpNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpNsOutgoingFilter.setStatus("mandatory")
_MscVrPpSrBpProvTable_Object = MibTable
mscVrPpSrBpProvTable = _MscVrPpSrBpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpProvTable.setStatus("mandatory")
_MscVrPpSrBpProvEntry_Object = MibTableRow
mscVrPpSrBpProvEntry = _MscVrPpSrBpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10, 1)
)
mscVrPpSrBpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpProvEntry.setStatus("mandatory")


class _MscVrPpSrBpTranslateIpx_Type(Integer32):
    """Custom type mscVrPpSrBpTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpSrBpTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpSrBpTranslateIpx_Object = MibTableColumn
mscVrPpSrBpTranslateIpx = _MscVrPpSrBpTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10, 1, 1),
    _MscVrPpSrBpTranslateIpx_Type()
)
mscVrPpSrBpTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpTranslateIpx.setStatus("mandatory")


class _MscVrPpSrBpFragmentIp_Type(Integer32):
    """Custom type mscVrPpSrBpFragmentIp based on Integer32"""
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


_MscVrPpSrBpFragmentIp_Type.__name__ = "Integer32"
_MscVrPpSrBpFragmentIp_Object = MibTableColumn
mscVrPpSrBpFragmentIp = _MscVrPpSrBpFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10, 1, 2),
    _MscVrPpSrBpFragmentIp_Type()
)
mscVrPpSrBpFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpFragmentIp.setStatus("mandatory")


class _MscVrPpSrBpServiceClass_Type(Integer32):
    """Custom type mscVrPpSrBpServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpSrBpServiceClass_Type.__name__ = "Integer32"
_MscVrPpSrBpServiceClass_Object = MibTableColumn
mscVrPpSrBpServiceClass = _MscVrPpSrBpServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10, 1, 3),
    _MscVrPpSrBpServiceClass_Type()
)
mscVrPpSrBpServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpServiceClass.setStatus("mandatory")


class _MscVrPpSrBpConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpSrBpConvertArpMacAddress based on Integer32"""
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


_MscVrPpSrBpConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpSrBpConvertArpMacAddress_Object = MibTableColumn
mscVrPpSrBpConvertArpMacAddress = _MscVrPpSrBpConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10, 1, 4),
    _MscVrPpSrBpConvertArpMacAddress_Type()
)
mscVrPpSrBpConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpSrBpPortNum_Type(Unsigned32):
    """Custom type mscVrPpSrBpPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpSrBpPortNum_Type.__name__ = "Unsigned32"
_MscVrPpSrBpPortNum_Object = MibTableColumn
mscVrPpSrBpPortNum = _MscVrPpSrBpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 10, 1, 5),
    _MscVrPpSrBpPortNum_Type()
)
mscVrPpSrBpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpPortNum.setStatus("mandatory")
_MscVrPpSrBpStpProvTable_Object = MibTable
mscVrPpSrBpStpProvTable = _MscVrPpSrBpStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStpProvTable.setStatus("mandatory")
_MscVrPpSrBpStpProvEntry_Object = MibTableRow
mscVrPpSrBpStpProvEntry = _MscVrPpSrBpStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1)
)
mscVrPpSrBpStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStpProvEntry.setStatus("mandatory")


class _MscVrPpSrBpAdminStatus_Type(Integer32):
    """Custom type mscVrPpSrBpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpSrBpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSrBpAdminStatus_Object = MibTableColumn
mscVrPpSrBpAdminStatus = _MscVrPpSrBpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1, 1),
    _MscVrPpSrBpAdminStatus_Type()
)
mscVrPpSrBpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpAdminStatus.setStatus("mandatory")


class _MscVrPpSrBpPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpSrBpPortStateStpControl based on Integer32"""
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


_MscVrPpSrBpPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpSrBpPortStateStpControl_Object = MibTableColumn
mscVrPpSrBpPortStateStpControl = _MscVrPpSrBpPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1, 2),
    _MscVrPpSrBpPortStateStpControl_Type()
)
mscVrPpSrBpPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpPortStateStpControl.setStatus("mandatory")


class _MscVrPpSrBpStpTypeProv_Type(Integer32):
    """Custom type mscVrPpSrBpStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpSrBpStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpSrBpStpTypeProv_Object = MibTableColumn
mscVrPpSrBpStpTypeProv = _MscVrPpSrBpStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1, 3),
    _MscVrPpSrBpStpTypeProv_Type()
)
mscVrPpSrBpStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpStpTypeProv.setStatus("mandatory")


class _MscVrPpSrBpPortPriority_Type(Unsigned32):
    """Custom type mscVrPpSrBpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrBpPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpSrBpPortPriority_Object = MibTableColumn
mscVrPpSrBpPortPriority = _MscVrPpSrBpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1, 4),
    _MscVrPpSrBpPortPriority_Type()
)
mscVrPpSrBpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpPortPriority.setStatus("mandatory")


class _MscVrPpSrBpPathCost_Type(Unsigned32):
    """Custom type mscVrPpSrBpPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrBpPathCost_Type.__name__ = "Unsigned32"
_MscVrPpSrBpPathCost_Object = MibTableColumn
mscVrPpSrBpPathCost = _MscVrPpSrBpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1, 5),
    _MscVrPpSrBpPathCost_Type()
)
mscVrPpSrBpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpPathCost.setStatus("mandatory")


class _MscVrPpSrBpPathCostMethod_Type(Integer32):
    """Custom type mscVrPpSrBpPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpSrBpPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpSrBpPathCostMethod_Object = MibTableColumn
mscVrPpSrBpPathCostMethod = _MscVrPpSrBpPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 12, 1, 6),
    _MscVrPpSrBpPathCostMethod_Type()
)
mscVrPpSrBpPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpPathCostMethod.setStatus("mandatory")
_MscVrPpSrBpDIProvTable_Object = MibTable
mscVrPpSrBpDIProvTable = _MscVrPpSrBpDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 13)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpDIProvTable.setStatus("mandatory")
_MscVrPpSrBpDIProvEntry_Object = MibTableRow
mscVrPpSrBpDIProvEntry = _MscVrPpSrBpDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 13, 1)
)
mscVrPpSrBpDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpDIProvEntry.setStatus("mandatory")


class _MscVrPpSrBpDomainNum_Type(Unsigned32):
    """Custom type mscVrPpSrBpDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpSrBpDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpSrBpDomainNum_Object = MibTableColumn
mscVrPpSrBpDomainNum = _MscVrPpSrBpDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 13, 1, 1),
    _MscVrPpSrBpDomainNum_Type()
)
mscVrPpSrBpDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpDomainNum.setStatus("mandatory")


class _MscVrPpSrBpPreserveDomain_Type(Integer32):
    """Custom type mscVrPpSrBpPreserveDomain based on Integer32"""
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


_MscVrPpSrBpPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpSrBpPreserveDomain_Object = MibTableColumn
mscVrPpSrBpPreserveDomain = _MscVrPpSrBpPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 13, 1, 2),
    _MscVrPpSrBpPreserveDomain_Type()
)
mscVrPpSrBpPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpPreserveDomain.setStatus("mandatory")
_MscVrPpSrBpStateTable_Object = MibTable
mscVrPpSrBpStateTable = _MscVrPpSrBpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 14)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStateTable.setStatus("mandatory")
_MscVrPpSrBpStateEntry_Object = MibTableRow
mscVrPpSrBpStateEntry = _MscVrPpSrBpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 14, 1)
)
mscVrPpSrBpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStateEntry.setStatus("mandatory")


class _MscVrPpSrBpAdminState_Type(Integer32):
    """Custom type mscVrPpSrBpAdminState based on Integer32"""
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


_MscVrPpSrBpAdminState_Type.__name__ = "Integer32"
_MscVrPpSrBpAdminState_Object = MibTableColumn
mscVrPpSrBpAdminState = _MscVrPpSrBpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 14, 1, 1),
    _MscVrPpSrBpAdminState_Type()
)
mscVrPpSrBpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpAdminState.setStatus("mandatory")


class _MscVrPpSrBpOperationalState_Type(Integer32):
    """Custom type mscVrPpSrBpOperationalState based on Integer32"""
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


_MscVrPpSrBpOperationalState_Type.__name__ = "Integer32"
_MscVrPpSrBpOperationalState_Object = MibTableColumn
mscVrPpSrBpOperationalState = _MscVrPpSrBpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 14, 1, 2),
    _MscVrPpSrBpOperationalState_Type()
)
mscVrPpSrBpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpOperationalState.setStatus("mandatory")


class _MscVrPpSrBpUsageState_Type(Integer32):
    """Custom type mscVrPpSrBpUsageState based on Integer32"""
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


_MscVrPpSrBpUsageState_Type.__name__ = "Integer32"
_MscVrPpSrBpUsageState_Object = MibTableColumn
mscVrPpSrBpUsageState = _MscVrPpSrBpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 14, 1, 3),
    _MscVrPpSrBpUsageState_Type()
)
mscVrPpSrBpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpUsageState.setStatus("mandatory")
_MscVrPpSrBpOperStatusTable_Object = MibTable
mscVrPpSrBpOperStatusTable = _MscVrPpSrBpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 15)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpOperStatusTable.setStatus("mandatory")
_MscVrPpSrBpOperStatusEntry_Object = MibTableRow
mscVrPpSrBpOperStatusEntry = _MscVrPpSrBpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 15, 1)
)
mscVrPpSrBpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpOperStatusEntry.setStatus("mandatory")


class _MscVrPpSrBpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSrBpSnmpOperStatus based on Integer32"""
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


_MscVrPpSrBpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSrBpSnmpOperStatus_Object = MibTableColumn
mscVrPpSrBpSnmpOperStatus = _MscVrPpSrBpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 15, 1, 1),
    _MscVrPpSrBpSnmpOperStatus_Type()
)
mscVrPpSrBpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpSnmpOperStatus.setStatus("mandatory")
_MscVrPpSrBpOperTable_Object = MibTable
mscVrPpSrBpOperTable = _MscVrPpSrBpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpOperTable.setStatus("mandatory")
_MscVrPpSrBpOperEntry_Object = MibTableRow
mscVrPpSrBpOperEntry = _MscVrPpSrBpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1)
)
mscVrPpSrBpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpOperEntry.setStatus("mandatory")


class _MscVrPpSrBpPortName_Type(AsciiString):
    """Custom type mscVrPpSrBpPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpSrBpPortName_Type.__name__ = "AsciiString"
_MscVrPpSrBpPortName_Object = MibTableColumn
mscVrPpSrBpPortName = _MscVrPpSrBpPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 1),
    _MscVrPpSrBpPortName_Type()
)
mscVrPpSrBpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpPortName.setStatus("mandatory")


class _MscVrPpSrBpUpTime_Type(Unsigned32):
    """Custom type mscVrPpSrBpUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrBpUpTime_Type.__name__ = "Unsigned32"
_MscVrPpSrBpUpTime_Object = MibTableColumn
mscVrPpSrBpUpTime = _MscVrPpSrBpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 3),
    _MscVrPpSrBpUpTime_Type()
)
mscVrPpSrBpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpUpTime.setStatus("mandatory")


class _MscVrPpSrBpDownTime_Type(Unsigned32):
    """Custom type mscVrPpSrBpDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrBpDownTime_Type.__name__ = "Unsigned32"
_MscVrPpSrBpDownTime_Object = MibTableColumn
mscVrPpSrBpDownTime = _MscVrPpSrBpDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 4),
    _MscVrPpSrBpDownTime_Type()
)
mscVrPpSrBpDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDownTime.setStatus("mandatory")


class _MscVrPpSrBpBridgingMode_Type(Integer32):
    """Custom type mscVrPpSrBpBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpSrBpBridgingMode_Type.__name__ = "Integer32"
_MscVrPpSrBpBridgingMode_Object = MibTableColumn
mscVrPpSrBpBridgingMode = _MscVrPpSrBpBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 5),
    _MscVrPpSrBpBridgingMode_Type()
)
mscVrPpSrBpBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpBridgingMode.setStatus("mandatory")


class _MscVrPpSrBpBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpSrBpBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpSrBpBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpSrBpBridgePortConfig_Object = MibTableColumn
mscVrPpSrBpBridgePortConfig = _MscVrPpSrBpBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 6),
    _MscVrPpSrBpBridgePortConfig_Type()
)
mscVrPpSrBpBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpBridgePortConfig.setStatus("mandatory")


class _MscVrPpSrBpBridgePortType_Type(Integer32):
    """Custom type mscVrPpSrBpBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpSrBpBridgePortType_Type.__name__ = "Integer32"
_MscVrPpSrBpBridgePortType_Object = MibTableColumn
mscVrPpSrBpBridgePortType = _MscVrPpSrBpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 7),
    _MscVrPpSrBpBridgePortType_Type()
)
mscVrPpSrBpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpBridgePortType.setStatus("mandatory")


class _MscVrPpSrBpIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpSrBpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrBpIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpSrBpIfIndex_Object = MibTableColumn
mscVrPpSrBpIfIndex = _MscVrPpSrBpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 8),
    _MscVrPpSrBpIfIndex_Type()
)
mscVrPpSrBpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpIfIndex.setStatus("mandatory")
_MscVrPpSrBpDelayExceededDiscards_Type = Counter32
_MscVrPpSrBpDelayExceededDiscards_Object = MibTableColumn
mscVrPpSrBpDelayExceededDiscards = _MscVrPpSrBpDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 10),
    _MscVrPpSrBpDelayExceededDiscards_Type()
)
mscVrPpSrBpDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDelayExceededDiscards.setStatus("mandatory")
_MscVrPpSrBpMtuExceededDiscards_Type = Counter32
_MscVrPpSrBpMtuExceededDiscards_Object = MibTableColumn
mscVrPpSrBpMtuExceededDiscards = _MscVrPpSrBpMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 16, 1, 11),
    _MscVrPpSrBpMtuExceededDiscards_Type()
)
mscVrPpSrBpMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpMtuExceededDiscards.setStatus("mandatory")
_MscVrPpSrBpStpOperTable_Object = MibTable
mscVrPpSrBpStpOperTable = _MscVrPpSrBpStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStpOperTable.setStatus("mandatory")
_MscVrPpSrBpStpOperEntry_Object = MibTableRow
mscVrPpSrBpStpOperEntry = _MscVrPpSrBpStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1)
)
mscVrPpSrBpStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStpOperEntry.setStatus("mandatory")


class _MscVrPpSrBpStpPortState_Type(Integer32):
    """Custom type mscVrPpSrBpStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpSrBpStpPortState_Type.__name__ = "Integer32"
_MscVrPpSrBpStpPortState_Object = MibTableColumn
mscVrPpSrBpStpPortState = _MscVrPpSrBpStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 2),
    _MscVrPpSrBpStpPortState_Type()
)
mscVrPpSrBpStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpStpPortState.setStatus("mandatory")


class _MscVrPpSrBpStpTypeOper_Type(Integer32):
    """Custom type mscVrPpSrBpStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpSrBpStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpSrBpStpTypeOper_Object = MibTableColumn
mscVrPpSrBpStpTypeOper = _MscVrPpSrBpStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 3),
    _MscVrPpSrBpStpTypeOper_Type()
)
mscVrPpSrBpStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpStpTypeOper.setStatus("mandatory")


class _MscVrPpSrBpDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpSrBpDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrBpDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpSrBpDesignatedCost_Object = MibTableColumn
mscVrPpSrBpDesignatedCost = _MscVrPpSrBpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 4),
    _MscVrPpSrBpDesignatedCost_Type()
)
mscVrPpSrBpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDesignatedCost.setStatus("mandatory")


class _MscVrPpSrBpPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpSrBpPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrBpPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpSrBpPathCostOper_Object = MibTableColumn
mscVrPpSrBpPathCostOper = _MscVrPpSrBpPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 5),
    _MscVrPpSrBpPathCostOper_Type()
)
mscVrPpSrBpPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpPathCostOper.setStatus("mandatory")


class _MscVrPpSrBpDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpSrBpDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrBpDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpSrBpDesignatedBridge_Object = MibTableColumn
mscVrPpSrBpDesignatedBridge = _MscVrPpSrBpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 6),
    _MscVrPpSrBpDesignatedBridge_Type()
)
mscVrPpSrBpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDesignatedBridge.setStatus("mandatory")


class _MscVrPpSrBpDesignatedPort_Type(Hex):
    """Custom type mscVrPpSrBpDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrBpDesignatedPort_Type.__name__ = "Hex"
_MscVrPpSrBpDesignatedPort_Object = MibTableColumn
mscVrPpSrBpDesignatedPort = _MscVrPpSrBpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 7),
    _MscVrPpSrBpDesignatedPort_Type()
)
mscVrPpSrBpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDesignatedPort.setStatus("mandatory")
_MscVrPpSrBpForwardTransitions_Type = Counter32
_MscVrPpSrBpForwardTransitions_Object = MibTableColumn
mscVrPpSrBpForwardTransitions = _MscVrPpSrBpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 8),
    _MscVrPpSrBpForwardTransitions_Type()
)
mscVrPpSrBpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpForwardTransitions.setStatus("mandatory")
_MscVrPpSrBpBlockingDiscards_Type = Counter32
_MscVrPpSrBpBlockingDiscards_Object = MibTableColumn
mscVrPpSrBpBlockingDiscards = _MscVrPpSrBpBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 9),
    _MscVrPpSrBpBlockingDiscards_Type()
)
mscVrPpSrBpBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpBlockingDiscards.setStatus("mandatory")


class _MscVrPpSrBpDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpSrBpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrBpDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpSrBpDesignatedRoot_Object = MibTableColumn
mscVrPpSrBpDesignatedRoot = _MscVrPpSrBpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 18, 1, 10),
    _MscVrPpSrBpDesignatedRoot_Type()
)
mscVrPpSrBpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDesignatedRoot.setStatus("mandatory")
_MscVrPpSrBpStatsTable_Object = MibTable
mscVrPpSrBpStatsTable = _MscVrPpSrBpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStatsTable.setStatus("mandatory")
_MscVrPpSrBpStatsEntry_Object = MibTableRow
mscVrPpSrBpStatsEntry = _MscVrPpSrBpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19, 1)
)
mscVrPpSrBpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpStatsEntry.setStatus("mandatory")
_MscVrPpSrBpBadAbstractDiscards_Type = Counter32
_MscVrPpSrBpBadAbstractDiscards_Object = MibTableColumn
mscVrPpSrBpBadAbstractDiscards = _MscVrPpSrBpBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19, 1, 1),
    _MscVrPpSrBpBadAbstractDiscards_Type()
)
mscVrPpSrBpBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpBadAbstractDiscards.setStatus("mandatory")
_MscVrPpSrBpTinygramFramesIn_Type = Counter32
_MscVrPpSrBpTinygramFramesIn_Object = MibTableColumn
mscVrPpSrBpTinygramFramesIn = _MscVrPpSrBpTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19, 1, 2),
    _MscVrPpSrBpTinygramFramesIn_Type()
)
mscVrPpSrBpTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpTinygramFramesIn.setStatus("mandatory")
_MscVrPpSrBpTinygramFramesOut_Type = Counter32
_MscVrPpSrBpTinygramFramesOut_Object = MibTableColumn
mscVrPpSrBpTinygramFramesOut = _MscVrPpSrBpTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19, 1, 3),
    _MscVrPpSrBpTinygramFramesOut_Type()
)
mscVrPpSrBpTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpTinygramFramesOut.setStatus("mandatory")
_MscVrPpSrBpInFilterDiscards_Type = Counter32
_MscVrPpSrBpInFilterDiscards_Object = MibTableColumn
mscVrPpSrBpInFilterDiscards = _MscVrPpSrBpInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19, 1, 4),
    _MscVrPpSrBpInFilterDiscards_Type()
)
mscVrPpSrBpInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpInFilterDiscards.setStatus("mandatory")
_MscVrPpSrBpOutFilterDiscards_Type = Counter32
_MscVrPpSrBpOutFilterDiscards_Object = MibTableColumn
mscVrPpSrBpOutFilterDiscards = _MscVrPpSrBpOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 19, 1, 5),
    _MscVrPpSrBpOutFilterDiscards_Type()
)
mscVrPpSrBpOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrBpSrProvTable_Object = MibTable
mscVrPpSrBpSrProvTable = _MscVrPpSrBpSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpSrProvTable.setStatus("mandatory")
_MscVrPpSrBpSrProvEntry_Object = MibTableRow
mscVrPpSrBpSrProvEntry = _MscVrPpSrBpSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1)
)
mscVrPpSrBpSrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpSrProvEntry.setStatus("mandatory")


class _MscVrPpSrBpHopCount_Type(Unsigned32):
    """Custom type mscVrPpSrBpHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrPpSrBpHopCount_Type.__name__ = "Unsigned32"
_MscVrPpSrBpHopCount_Object = MibTableColumn
mscVrPpSrBpHopCount = _MscVrPpSrBpHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 1),
    _MscVrPpSrBpHopCount_Type()
)
mscVrPpSrBpHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpHopCount.setStatus("mandatory")


class _MscVrPpSrBpExploreFrameTreatment_Type(Integer32):
    """Custom type mscVrPpSrBpExploreFrameTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encap", 0),
          ("xlate", 1))
    )


_MscVrPpSrBpExploreFrameTreatment_Type.__name__ = "Integer32"
_MscVrPpSrBpExploreFrameTreatment_Object = MibTableColumn
mscVrPpSrBpExploreFrameTreatment = _MscVrPpSrBpExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 2),
    _MscVrPpSrBpExploreFrameTreatment_Type()
)
mscVrPpSrBpExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpExploreFrameTreatment.setStatus("mandatory")


class _MscVrPpSrBpLanId_Type(Unsigned32):
    """Custom type mscVrPpSrBpLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrBpLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrBpLanId_Object = MibTableColumn
mscVrPpSrBpLanId = _MscVrPpSrBpLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 3),
    _MscVrPpSrBpLanId_Type()
)
mscVrPpSrBpLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpLanId.setStatus("mandatory")


class _MscVrPpSrBpInternalLanId_Type(Unsigned32):
    """Custom type mscVrPpSrBpInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrBpInternalLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrBpInternalLanId_Object = MibTableColumn
mscVrPpSrBpInternalLanId = _MscVrPpSrBpInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 4),
    _MscVrPpSrBpInternalLanId_Type()
)
mscVrPpSrBpInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpInternalLanId.setStatus("mandatory")


class _MscVrPpSrBpBridgeNum_Type(Unsigned32):
    """Custom type mscVrPpSrBpBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrPpSrBpBridgeNum_Type.__name__ = "Unsigned32"
_MscVrPpSrBpBridgeNum_Object = MibTableColumn
mscVrPpSrBpBridgeNum = _MscVrPpSrBpBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 5),
    _MscVrPpSrBpBridgeNum_Type()
)
mscVrPpSrBpBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpBridgeNum.setStatus("mandatory")


class _MscVrPpSrBpLargestFrame_Type(Unsigned32):
    """Custom type mscVrPpSrBpLargestFrame based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 516),
        ValueRangeConstraint(1470, 1470),
        ValueRangeConstraint(2052, 2052),
        ValueRangeConstraint(4399, 4399),
        ValueRangeConstraint(8130, 8130),
        ValueRangeConstraint(11407, 11407),
        ValueRangeConstraint(17749, 17749),
    )


_MscVrPpSrBpLargestFrame_Type.__name__ = "Unsigned32"
_MscVrPpSrBpLargestFrame_Object = MibTableColumn
mscVrPpSrBpLargestFrame = _MscVrPpSrBpLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 6),
    _MscVrPpSrBpLargestFrame_Type()
)
mscVrPpSrBpLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpLargestFrame.setStatus("mandatory")


class _MscVrPpSrBpSteSpanMode_Type(Integer32):
    """Custom type mscVrPpSrBpSteSpanMode based on Integer32"""
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
        *(("autoSpan", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_MscVrPpSrBpSteSpanMode_Type.__name__ = "Integer32"
_MscVrPpSrBpSteSpanMode_Object = MibTableColumn
mscVrPpSrBpSteSpanMode = _MscVrPpSrBpSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 7),
    _MscVrPpSrBpSteSpanMode_Type()
)
mscVrPpSrBpSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpSteSpanMode.setStatus("mandatory")


class _MscVrPpSrBpAreRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrBpAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrBpAreRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrBpAreRdLimit_Object = MibTableColumn
mscVrPpSrBpAreRdLimit = _MscVrPpSrBpAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 8),
    _MscVrPpSrBpAreRdLimit_Type()
)
mscVrPpSrBpAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpAreRdLimit.setStatus("mandatory")


class _MscVrPpSrBpSteRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrBpSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrBpSteRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrBpSteRdLimit_Object = MibTableColumn
mscVrPpSrBpSteRdLimit = _MscVrPpSrBpSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 20, 1, 9),
    _MscVrPpSrBpSteRdLimit_Type()
)
mscVrPpSrBpSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrBpSteRdLimit.setStatus("mandatory")
_MscVrPpSrBpSrStatsTable_Object = MibTable
mscVrPpSrBpSrStatsTable = _MscVrPpSrBpSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21)
)
if mibBuilder.loadTexts:
    mscVrPpSrBpSrStatsTable.setStatus("mandatory")
_MscVrPpSrBpSrStatsEntry_Object = MibTableRow
mscVrPpSrBpSrStatsEntry = _MscVrPpSrBpSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1)
)
mscVrPpSrBpSrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrBpSrStatsEntry.setStatus("mandatory")
_MscVrPpSrBpSpecInFrames_Type = Counter32
_MscVrPpSrBpSpecInFrames_Object = MibTableColumn
mscVrPpSrBpSpecInFrames = _MscVrPpSrBpSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 1),
    _MscVrPpSrBpSpecInFrames_Type()
)
mscVrPpSrBpSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpSpecInFrames.setStatus("mandatory")
_MscVrPpSrBpSpecOutFrames_Type = Counter32
_MscVrPpSrBpSpecOutFrames_Object = MibTableColumn
mscVrPpSrBpSpecOutFrames = _MscVrPpSrBpSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 2),
    _MscVrPpSrBpSpecOutFrames_Type()
)
mscVrPpSrBpSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpSpecOutFrames.setStatus("mandatory")
_MscVrPpSrBpApeInFrames_Type = Counter32
_MscVrPpSrBpApeInFrames_Object = MibTableColumn
mscVrPpSrBpApeInFrames = _MscVrPpSrBpApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 3),
    _MscVrPpSrBpApeInFrames_Type()
)
mscVrPpSrBpApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpApeInFrames.setStatus("mandatory")
_MscVrPpSrBpApeOutFrames_Type = Counter32
_MscVrPpSrBpApeOutFrames_Object = MibTableColumn
mscVrPpSrBpApeOutFrames = _MscVrPpSrBpApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 4),
    _MscVrPpSrBpApeOutFrames_Type()
)
mscVrPpSrBpApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpApeOutFrames.setStatus("mandatory")
_MscVrPpSrBpSteInFrames_Type = Counter32
_MscVrPpSrBpSteInFrames_Object = MibTableColumn
mscVrPpSrBpSteInFrames = _MscVrPpSrBpSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 5),
    _MscVrPpSrBpSteInFrames_Type()
)
mscVrPpSrBpSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpSteInFrames.setStatus("mandatory")
_MscVrPpSrBpSteOutFrames_Type = Counter32
_MscVrPpSrBpSteOutFrames_Object = MibTableColumn
mscVrPpSrBpSteOutFrames = _MscVrPpSrBpSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 6),
    _MscVrPpSrBpSteOutFrames_Type()
)
mscVrPpSrBpSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpSteOutFrames.setStatus("mandatory")
_MscVrPpSrBpSegmentMismatchDiscards_Type = Counter32
_MscVrPpSrBpSegmentMismatchDiscards_Object = MibTableColumn
mscVrPpSrBpSegmentMismatchDiscards = _MscVrPpSrBpSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 7),
    _MscVrPpSrBpSegmentMismatchDiscards_Type()
)
mscVrPpSrBpSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpSegmentMismatchDiscards.setStatus("mandatory")
_MscVrPpSrBpDupSegmentDiscards_Type = Counter32
_MscVrPpSrBpDupSegmentDiscards_Object = MibTableColumn
mscVrPpSrBpDupSegmentDiscards = _MscVrPpSrBpDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 8),
    _MscVrPpSrBpDupSegmentDiscards_Type()
)
mscVrPpSrBpDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDupSegmentDiscards.setStatus("mandatory")
_MscVrPpSrBpHopCountExceededDiscards_Type = Counter32
_MscVrPpSrBpHopCountExceededDiscards_Object = MibTableColumn
mscVrPpSrBpHopCountExceededDiscards = _MscVrPpSrBpHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 9),
    _MscVrPpSrBpHopCountExceededDiscards_Type()
)
mscVrPpSrBpHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpHopCountExceededDiscards.setStatus("mandatory")
_MscVrPpSrBpDupLanIdOrTreeErrors_Type = Counter32
_MscVrPpSrBpDupLanIdOrTreeErrors_Object = MibTableColumn
mscVrPpSrBpDupLanIdOrTreeErrors = _MscVrPpSrBpDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 10),
    _MscVrPpSrBpDupLanIdOrTreeErrors_Type()
)
mscVrPpSrBpDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDupLanIdOrTreeErrors.setStatus("mandatory")
_MscVrPpSrBpLanIdMismatches_Type = Counter32
_MscVrPpSrBpLanIdMismatches_Object = MibTableColumn
mscVrPpSrBpLanIdMismatches = _MscVrPpSrBpLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 11),
    _MscVrPpSrBpLanIdMismatches_Type()
)
mscVrPpSrBpLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpLanIdMismatches.setStatus("mandatory")
_MscVrPpSrBpStaticDiscards_Type = Counter32
_MscVrPpSrBpStaticDiscards_Object = MibTableColumn
mscVrPpSrBpStaticDiscards = _MscVrPpSrBpStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 12),
    _MscVrPpSrBpStaticDiscards_Type()
)
mscVrPpSrBpStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpStaticDiscards.setStatus("mandatory")
_MscVrPpSrBpDynamicDiscards_Type = Counter32
_MscVrPpSrBpDynamicDiscards_Object = MibTableColumn
mscVrPpSrBpDynamicDiscards = _MscVrPpSrBpDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 8, 21, 1, 13),
    _MscVrPpSrBpDynamicDiscards_Type()
)
mscVrPpSrBpDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrBpDynamicDiscards.setStatus("mandatory")
_MscVrPpSrtBp_ObjectIdentity = ObjectIdentity
mscVrPpSrtBp = _MscVrPpSrtBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9)
)
_MscVrPpSrtBpRowStatusTable_Object = MibTable
mscVrPpSrtBpRowStatusTable = _MscVrPpSrtBpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpRowStatusTable.setStatus("mandatory")
_MscVrPpSrtBpRowStatusEntry_Object = MibTableRow
mscVrPpSrtBpRowStatusEntry = _MscVrPpSrtBpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 1, 1)
)
mscVrPpSrtBpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpRowStatusEntry.setStatus("mandatory")
_MscVrPpSrtBpRowStatus_Type = RowStatus
_MscVrPpSrtBpRowStatus_Object = MibTableColumn
mscVrPpSrtBpRowStatus = _MscVrPpSrtBpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 1, 1, 1),
    _MscVrPpSrtBpRowStatus_Type()
)
mscVrPpSrtBpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpRowStatus.setStatus("mandatory")
_MscVrPpSrtBpComponentName_Type = DisplayString
_MscVrPpSrtBpComponentName_Object = MibTableColumn
mscVrPpSrtBpComponentName = _MscVrPpSrtBpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 1, 1, 2),
    _MscVrPpSrtBpComponentName_Type()
)
mscVrPpSrtBpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpComponentName.setStatus("mandatory")
_MscVrPpSrtBpStorageType_Type = StorageType
_MscVrPpSrtBpStorageType_Object = MibTableColumn
mscVrPpSrtBpStorageType = _MscVrPpSrtBpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 1, 1, 4),
    _MscVrPpSrtBpStorageType_Type()
)
mscVrPpSrtBpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpStorageType.setStatus("mandatory")
_MscVrPpSrtBpIndex_Type = NonReplicated
_MscVrPpSrtBpIndex_Object = MibTableColumn
mscVrPpSrtBpIndex = _MscVrPpSrtBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 1, 1, 10),
    _MscVrPpSrtBpIndex_Type()
)
mscVrPpSrtBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrtBpIndex.setStatus("mandatory")
_MscVrPpSrtBpNs_ObjectIdentity = ObjectIdentity
mscVrPpSrtBpNs = _MscVrPpSrtBpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2)
)
_MscVrPpSrtBpNsRowStatusTable_Object = MibTable
mscVrPpSrtBpNsRowStatusTable = _MscVrPpSrtBpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsRowStatusTable.setStatus("mandatory")
_MscVrPpSrtBpNsRowStatusEntry_Object = MibTableRow
mscVrPpSrtBpNsRowStatusEntry = _MscVrPpSrtBpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 1, 1)
)
mscVrPpSrtBpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsRowStatusEntry.setStatus("mandatory")
_MscVrPpSrtBpNsRowStatus_Type = RowStatus
_MscVrPpSrtBpNsRowStatus_Object = MibTableColumn
mscVrPpSrtBpNsRowStatus = _MscVrPpSrtBpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 1, 1, 1),
    _MscVrPpSrtBpNsRowStatus_Type()
)
mscVrPpSrtBpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsRowStatus.setStatus("mandatory")
_MscVrPpSrtBpNsComponentName_Type = DisplayString
_MscVrPpSrtBpNsComponentName_Object = MibTableColumn
mscVrPpSrtBpNsComponentName = _MscVrPpSrtBpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 1, 1, 2),
    _MscVrPpSrtBpNsComponentName_Type()
)
mscVrPpSrtBpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsComponentName.setStatus("mandatory")
_MscVrPpSrtBpNsStorageType_Type = StorageType
_MscVrPpSrtBpNsStorageType_Object = MibTableColumn
mscVrPpSrtBpNsStorageType = _MscVrPpSrtBpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 1, 1, 4),
    _MscVrPpSrtBpNsStorageType_Type()
)
mscVrPpSrtBpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsStorageType.setStatus("mandatory")
_MscVrPpSrtBpNsIndex_Type = NonReplicated
_MscVrPpSrtBpNsIndex_Object = MibTableColumn
mscVrPpSrtBpNsIndex = _MscVrPpSrtBpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 1, 1, 10),
    _MscVrPpSrtBpNsIndex_Type()
)
mscVrPpSrtBpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsIndex.setStatus("mandatory")
_MscVrPpSrtBpNsProvTable_Object = MibTable
mscVrPpSrtBpNsProvTable = _MscVrPpSrtBpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsProvTable.setStatus("mandatory")
_MscVrPpSrtBpNsProvEntry_Object = MibTableRow
mscVrPpSrtBpNsProvEntry = _MscVrPpSrtBpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 10, 1)
)
mscVrPpSrtBpNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsProvEntry.setStatus("mandatory")


class _MscVrPpSrtBpNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpSrtBpNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpSrtBpNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpSrtBpNsIncomingFilter_Object = MibTableColumn
mscVrPpSrtBpNsIncomingFilter = _MscVrPpSrtBpNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 10, 1, 2),
    _MscVrPpSrtBpNsIncomingFilter_Type()
)
mscVrPpSrtBpNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsIncomingFilter.setStatus("mandatory")


class _MscVrPpSrtBpNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpSrtBpNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpSrtBpNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpSrtBpNsOutgoingFilter_Object = MibTableColumn
mscVrPpSrtBpNsOutgoingFilter = _MscVrPpSrtBpNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 2, 10, 1, 3),
    _MscVrPpSrtBpNsOutgoingFilter_Type()
)
mscVrPpSrtBpNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpNsOutgoingFilter.setStatus("mandatory")
_MscVrPpSrtBpProvTable_Object = MibTable
mscVrPpSrtBpProvTable = _MscVrPpSrtBpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpProvTable.setStatus("mandatory")
_MscVrPpSrtBpProvEntry_Object = MibTableRow
mscVrPpSrtBpProvEntry = _MscVrPpSrtBpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10, 1)
)
mscVrPpSrtBpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpProvEntry.setStatus("mandatory")


class _MscVrPpSrtBpTranslateIpx_Type(Integer32):
    """Custom type mscVrPpSrtBpTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpSrtBpTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpSrtBpTranslateIpx_Object = MibTableColumn
mscVrPpSrtBpTranslateIpx = _MscVrPpSrtBpTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10, 1, 1),
    _MscVrPpSrtBpTranslateIpx_Type()
)
mscVrPpSrtBpTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpTranslateIpx.setStatus("mandatory")


class _MscVrPpSrtBpFragmentIp_Type(Integer32):
    """Custom type mscVrPpSrtBpFragmentIp based on Integer32"""
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


_MscVrPpSrtBpFragmentIp_Type.__name__ = "Integer32"
_MscVrPpSrtBpFragmentIp_Object = MibTableColumn
mscVrPpSrtBpFragmentIp = _MscVrPpSrtBpFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10, 1, 2),
    _MscVrPpSrtBpFragmentIp_Type()
)
mscVrPpSrtBpFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpFragmentIp.setStatus("mandatory")


class _MscVrPpSrtBpServiceClass_Type(Integer32):
    """Custom type mscVrPpSrtBpServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpSrtBpServiceClass_Type.__name__ = "Integer32"
_MscVrPpSrtBpServiceClass_Object = MibTableColumn
mscVrPpSrtBpServiceClass = _MscVrPpSrtBpServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10, 1, 3),
    _MscVrPpSrtBpServiceClass_Type()
)
mscVrPpSrtBpServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpServiceClass.setStatus("mandatory")


class _MscVrPpSrtBpConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpSrtBpConvertArpMacAddress based on Integer32"""
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


_MscVrPpSrtBpConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpSrtBpConvertArpMacAddress_Object = MibTableColumn
mscVrPpSrtBpConvertArpMacAddress = _MscVrPpSrtBpConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10, 1, 4),
    _MscVrPpSrtBpConvertArpMacAddress_Type()
)
mscVrPpSrtBpConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpSrtBpPortNum_Type(Unsigned32):
    """Custom type mscVrPpSrtBpPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpSrtBpPortNum_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpPortNum_Object = MibTableColumn
mscVrPpSrtBpPortNum = _MscVrPpSrtBpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 10, 1, 5),
    _MscVrPpSrtBpPortNum_Type()
)
mscVrPpSrtBpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPortNum.setStatus("mandatory")
_MscVrPpSrtBpTbProvTable_Object = MibTable
mscVrPpSrtBpTbProvTable = _MscVrPpSrtBpTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 11)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpTbProvTable.setStatus("mandatory")
_MscVrPpSrtBpTbProvEntry_Object = MibTableRow
mscVrPpSrtBpTbProvEntry = _MscVrPpSrtBpTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 11, 1)
)
mscVrPpSrtBpTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpTbProvEntry.setStatus("mandatory")


class _MscVrPpSrtBpSecureOption_Type(Integer32):
    """Custom type mscVrPpSrtBpSecureOption based on Integer32"""
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


_MscVrPpSrtBpSecureOption_Type.__name__ = "Integer32"
_MscVrPpSrtBpSecureOption_Object = MibTableColumn
mscVrPpSrtBpSecureOption = _MscVrPpSrtBpSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 11, 1, 1),
    _MscVrPpSrtBpSecureOption_Type()
)
mscVrPpSrtBpSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSecureOption.setStatus("mandatory")
_MscVrPpSrtBpStpProvTable_Object = MibTable
mscVrPpSrtBpStpProvTable = _MscVrPpSrtBpStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpProvTable.setStatus("mandatory")
_MscVrPpSrtBpStpProvEntry_Object = MibTableRow
mscVrPpSrtBpStpProvEntry = _MscVrPpSrtBpStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1)
)
mscVrPpSrtBpStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpProvEntry.setStatus("mandatory")


class _MscVrPpSrtBpAdminStatus_Type(Integer32):
    """Custom type mscVrPpSrtBpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpSrtBpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSrtBpAdminStatus_Object = MibTableColumn
mscVrPpSrtBpAdminStatus = _MscVrPpSrtBpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1, 1),
    _MscVrPpSrtBpAdminStatus_Type()
)
mscVrPpSrtBpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpAdminStatus.setStatus("mandatory")


class _MscVrPpSrtBpPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpSrtBpPortStateStpControl based on Integer32"""
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


_MscVrPpSrtBpPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpSrtBpPortStateStpControl_Object = MibTableColumn
mscVrPpSrtBpPortStateStpControl = _MscVrPpSrtBpPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1, 2),
    _MscVrPpSrtBpPortStateStpControl_Type()
)
mscVrPpSrtBpPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPortStateStpControl.setStatus("mandatory")


class _MscVrPpSrtBpStpTypeProv_Type(Integer32):
    """Custom type mscVrPpSrtBpStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpSrtBpStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpSrtBpStpTypeProv_Object = MibTableColumn
mscVrPpSrtBpStpTypeProv = _MscVrPpSrtBpStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1, 3),
    _MscVrPpSrtBpStpTypeProv_Type()
)
mscVrPpSrtBpStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpTypeProv.setStatus("mandatory")


class _MscVrPpSrtBpPortPriority_Type(Unsigned32):
    """Custom type mscVrPpSrtBpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrtBpPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpPortPriority_Object = MibTableColumn
mscVrPpSrtBpPortPriority = _MscVrPpSrtBpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1, 4),
    _MscVrPpSrtBpPortPriority_Type()
)
mscVrPpSrtBpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPortPriority.setStatus("mandatory")


class _MscVrPpSrtBpPathCost_Type(Unsigned32):
    """Custom type mscVrPpSrtBpPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrtBpPathCost_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpPathCost_Object = MibTableColumn
mscVrPpSrtBpPathCost = _MscVrPpSrtBpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1, 5),
    _MscVrPpSrtBpPathCost_Type()
)
mscVrPpSrtBpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPathCost.setStatus("mandatory")


class _MscVrPpSrtBpPathCostMethod_Type(Integer32):
    """Custom type mscVrPpSrtBpPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpSrtBpPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpSrtBpPathCostMethod_Object = MibTableColumn
mscVrPpSrtBpPathCostMethod = _MscVrPpSrtBpPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 12, 1, 6),
    _MscVrPpSrtBpPathCostMethod_Type()
)
mscVrPpSrtBpPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPathCostMethod.setStatus("mandatory")
_MscVrPpSrtBpDIProvTable_Object = MibTable
mscVrPpSrtBpDIProvTable = _MscVrPpSrtBpDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 13)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpDIProvTable.setStatus("mandatory")
_MscVrPpSrtBpDIProvEntry_Object = MibTableRow
mscVrPpSrtBpDIProvEntry = _MscVrPpSrtBpDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 13, 1)
)
mscVrPpSrtBpDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpDIProvEntry.setStatus("mandatory")


class _MscVrPpSrtBpDomainNum_Type(Unsigned32):
    """Custom type mscVrPpSrtBpDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpSrtBpDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpDomainNum_Object = MibTableColumn
mscVrPpSrtBpDomainNum = _MscVrPpSrtBpDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 13, 1, 1),
    _MscVrPpSrtBpDomainNum_Type()
)
mscVrPpSrtBpDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDomainNum.setStatus("mandatory")


class _MscVrPpSrtBpPreserveDomain_Type(Integer32):
    """Custom type mscVrPpSrtBpPreserveDomain based on Integer32"""
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


_MscVrPpSrtBpPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpSrtBpPreserveDomain_Object = MibTableColumn
mscVrPpSrtBpPreserveDomain = _MscVrPpSrtBpPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 13, 1, 2),
    _MscVrPpSrtBpPreserveDomain_Type()
)
mscVrPpSrtBpPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPreserveDomain.setStatus("mandatory")
_MscVrPpSrtBpStateTable_Object = MibTable
mscVrPpSrtBpStateTable = _MscVrPpSrtBpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 14)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStateTable.setStatus("mandatory")
_MscVrPpSrtBpStateEntry_Object = MibTableRow
mscVrPpSrtBpStateEntry = _MscVrPpSrtBpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 14, 1)
)
mscVrPpSrtBpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStateEntry.setStatus("mandatory")


class _MscVrPpSrtBpAdminState_Type(Integer32):
    """Custom type mscVrPpSrtBpAdminState based on Integer32"""
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


_MscVrPpSrtBpAdminState_Type.__name__ = "Integer32"
_MscVrPpSrtBpAdminState_Object = MibTableColumn
mscVrPpSrtBpAdminState = _MscVrPpSrtBpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 14, 1, 1),
    _MscVrPpSrtBpAdminState_Type()
)
mscVrPpSrtBpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpAdminState.setStatus("mandatory")


class _MscVrPpSrtBpOperationalState_Type(Integer32):
    """Custom type mscVrPpSrtBpOperationalState based on Integer32"""
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


_MscVrPpSrtBpOperationalState_Type.__name__ = "Integer32"
_MscVrPpSrtBpOperationalState_Object = MibTableColumn
mscVrPpSrtBpOperationalState = _MscVrPpSrtBpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 14, 1, 2),
    _MscVrPpSrtBpOperationalState_Type()
)
mscVrPpSrtBpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpOperationalState.setStatus("mandatory")


class _MscVrPpSrtBpUsageState_Type(Integer32):
    """Custom type mscVrPpSrtBpUsageState based on Integer32"""
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


_MscVrPpSrtBpUsageState_Type.__name__ = "Integer32"
_MscVrPpSrtBpUsageState_Object = MibTableColumn
mscVrPpSrtBpUsageState = _MscVrPpSrtBpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 14, 1, 3),
    _MscVrPpSrtBpUsageState_Type()
)
mscVrPpSrtBpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpUsageState.setStatus("mandatory")
_MscVrPpSrtBpOperStatusTable_Object = MibTable
mscVrPpSrtBpOperStatusTable = _MscVrPpSrtBpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 15)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpOperStatusTable.setStatus("mandatory")
_MscVrPpSrtBpOperStatusEntry_Object = MibTableRow
mscVrPpSrtBpOperStatusEntry = _MscVrPpSrtBpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 15, 1)
)
mscVrPpSrtBpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpOperStatusEntry.setStatus("mandatory")


class _MscVrPpSrtBpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSrtBpSnmpOperStatus based on Integer32"""
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


_MscVrPpSrtBpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSrtBpSnmpOperStatus_Object = MibTableColumn
mscVrPpSrtBpSnmpOperStatus = _MscVrPpSrtBpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 15, 1, 1),
    _MscVrPpSrtBpSnmpOperStatus_Type()
)
mscVrPpSrtBpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSnmpOperStatus.setStatus("mandatory")
_MscVrPpSrtBpOperTable_Object = MibTable
mscVrPpSrtBpOperTable = _MscVrPpSrtBpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpOperTable.setStatus("mandatory")
_MscVrPpSrtBpOperEntry_Object = MibTableRow
mscVrPpSrtBpOperEntry = _MscVrPpSrtBpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1)
)
mscVrPpSrtBpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpOperEntry.setStatus("mandatory")


class _MscVrPpSrtBpPortName_Type(AsciiString):
    """Custom type mscVrPpSrtBpPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpSrtBpPortName_Type.__name__ = "AsciiString"
_MscVrPpSrtBpPortName_Object = MibTableColumn
mscVrPpSrtBpPortName = _MscVrPpSrtBpPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 1),
    _MscVrPpSrtBpPortName_Type()
)
mscVrPpSrtBpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPortName.setStatus("mandatory")


class _MscVrPpSrtBpUpTime_Type(Unsigned32):
    """Custom type mscVrPpSrtBpUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrtBpUpTime_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpUpTime_Object = MibTableColumn
mscVrPpSrtBpUpTime = _MscVrPpSrtBpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 3),
    _MscVrPpSrtBpUpTime_Type()
)
mscVrPpSrtBpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpUpTime.setStatus("mandatory")


class _MscVrPpSrtBpDownTime_Type(Unsigned32):
    """Custom type mscVrPpSrtBpDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrtBpDownTime_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpDownTime_Object = MibTableColumn
mscVrPpSrtBpDownTime = _MscVrPpSrtBpDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 4),
    _MscVrPpSrtBpDownTime_Type()
)
mscVrPpSrtBpDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDownTime.setStatus("mandatory")


class _MscVrPpSrtBpBridgingMode_Type(Integer32):
    """Custom type mscVrPpSrtBpBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpSrtBpBridgingMode_Type.__name__ = "Integer32"
_MscVrPpSrtBpBridgingMode_Object = MibTableColumn
mscVrPpSrtBpBridgingMode = _MscVrPpSrtBpBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 5),
    _MscVrPpSrtBpBridgingMode_Type()
)
mscVrPpSrtBpBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBridgingMode.setStatus("mandatory")


class _MscVrPpSrtBpBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpSrtBpBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpSrtBpBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpSrtBpBridgePortConfig_Object = MibTableColumn
mscVrPpSrtBpBridgePortConfig = _MscVrPpSrtBpBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 6),
    _MscVrPpSrtBpBridgePortConfig_Type()
)
mscVrPpSrtBpBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBridgePortConfig.setStatus("mandatory")


class _MscVrPpSrtBpBridgePortType_Type(Integer32):
    """Custom type mscVrPpSrtBpBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpSrtBpBridgePortType_Type.__name__ = "Integer32"
_MscVrPpSrtBpBridgePortType_Object = MibTableColumn
mscVrPpSrtBpBridgePortType = _MscVrPpSrtBpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 7),
    _MscVrPpSrtBpBridgePortType_Type()
)
mscVrPpSrtBpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBridgePortType.setStatus("mandatory")


class _MscVrPpSrtBpIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpSrtBpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrtBpIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpSrtBpIfIndex_Object = MibTableColumn
mscVrPpSrtBpIfIndex = _MscVrPpSrtBpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 8),
    _MscVrPpSrtBpIfIndex_Type()
)
mscVrPpSrtBpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpIfIndex.setStatus("mandatory")
_MscVrPpSrtBpDelayExceededDiscards_Type = Counter32
_MscVrPpSrtBpDelayExceededDiscards_Object = MibTableColumn
mscVrPpSrtBpDelayExceededDiscards = _MscVrPpSrtBpDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 10),
    _MscVrPpSrtBpDelayExceededDiscards_Type()
)
mscVrPpSrtBpDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDelayExceededDiscards.setStatus("mandatory")
_MscVrPpSrtBpMtuExceededDiscards_Type = Counter32
_MscVrPpSrtBpMtuExceededDiscards_Object = MibTableColumn
mscVrPpSrtBpMtuExceededDiscards = _MscVrPpSrtBpMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 16, 1, 11),
    _MscVrPpSrtBpMtuExceededDiscards_Type()
)
mscVrPpSrtBpMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpMtuExceededDiscards.setStatus("mandatory")
_MscVrPpSrtBpTbOperTable_Object = MibTable
mscVrPpSrtBpTbOperTable = _MscVrPpSrtBpTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpTbOperTable.setStatus("mandatory")
_MscVrPpSrtBpTbOperEntry_Object = MibTableRow
mscVrPpSrtBpTbOperEntry = _MscVrPpSrtBpTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1)
)
mscVrPpSrtBpTbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpTbOperEntry.setStatus("mandatory")


class _MscVrPpSrtBpMaxInfo_Type(Unsigned32):
    """Custom type mscVrPpSrtBpMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrtBpMaxInfo_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpMaxInfo_Object = MibTableColumn
mscVrPpSrtBpMaxInfo = _MscVrPpSrtBpMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 2),
    _MscVrPpSrtBpMaxInfo_Type()
)
mscVrPpSrtBpMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpMaxInfo.setStatus("mandatory")
_MscVrPpSrtBpBadVerifyDiscards_Type = Counter32
_MscVrPpSrtBpBadVerifyDiscards_Object = MibTableColumn
mscVrPpSrtBpBadVerifyDiscards = _MscVrPpSrtBpBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 3),
    _MscVrPpSrtBpBadVerifyDiscards_Type()
)
mscVrPpSrtBpBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBadVerifyDiscards.setStatus("mandatory")
_MscVrPpSrtBpUnicastNoMatches_Type = Counter32
_MscVrPpSrtBpUnicastNoMatches_Object = MibTableColumn
mscVrPpSrtBpUnicastNoMatches = _MscVrPpSrtBpUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 4),
    _MscVrPpSrtBpUnicastNoMatches_Type()
)
mscVrPpSrtBpUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpUnicastNoMatches.setStatus("mandatory")
_MscVrPpSrtBpStaticEntryDiscards_Type = Counter32
_MscVrPpSrtBpStaticEntryDiscards_Object = MibTableColumn
mscVrPpSrtBpStaticEntryDiscards = _MscVrPpSrtBpStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 5),
    _MscVrPpSrtBpStaticEntryDiscards_Type()
)
mscVrPpSrtBpStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpStaticEntryDiscards.setStatus("mandatory")
_MscVrPpSrtBpDynamicEntryDiscards_Type = Counter32
_MscVrPpSrtBpDynamicEntryDiscards_Object = MibTableColumn
mscVrPpSrtBpDynamicEntryDiscards = _MscVrPpSrtBpDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 6),
    _MscVrPpSrtBpDynamicEntryDiscards_Type()
)
mscVrPpSrtBpDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDynamicEntryDiscards.setStatus("mandatory")
_MscVrPpSrtBpLearningDiscards_Type = Counter32
_MscVrPpSrtBpLearningDiscards_Object = MibTableColumn
mscVrPpSrtBpLearningDiscards = _MscVrPpSrtBpLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 7),
    _MscVrPpSrtBpLearningDiscards_Type()
)
mscVrPpSrtBpLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpLearningDiscards.setStatus("mandatory")
_MscVrPpSrtBpInDiscards_Type = Counter32
_MscVrPpSrtBpInDiscards_Object = MibTableColumn
mscVrPpSrtBpInDiscards = _MscVrPpSrtBpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 8),
    _MscVrPpSrtBpInDiscards_Type()
)
mscVrPpSrtBpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpInDiscards.setStatus("mandatory")
_MscVrPpSrtBpInFrames_Type = Counter32
_MscVrPpSrtBpInFrames_Object = MibTableColumn
mscVrPpSrtBpInFrames = _MscVrPpSrtBpInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 9),
    _MscVrPpSrtBpInFrames_Type()
)
mscVrPpSrtBpInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpInFrames.setStatus("mandatory")
_MscVrPpSrtBpOutFrames_Type = Counter32
_MscVrPpSrtBpOutFrames_Object = MibTableColumn
mscVrPpSrtBpOutFrames = _MscVrPpSrtBpOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 17, 1, 10),
    _MscVrPpSrtBpOutFrames_Type()
)
mscVrPpSrtBpOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpOutFrames.setStatus("mandatory")
_MscVrPpSrtBpStpOperTable_Object = MibTable
mscVrPpSrtBpStpOperTable = _MscVrPpSrtBpStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpOperTable.setStatus("mandatory")
_MscVrPpSrtBpStpOperEntry_Object = MibTableRow
mscVrPpSrtBpStpOperEntry = _MscVrPpSrtBpStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1)
)
mscVrPpSrtBpStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpOperEntry.setStatus("mandatory")


class _MscVrPpSrtBpStpPortState_Type(Integer32):
    """Custom type mscVrPpSrtBpStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpSrtBpStpPortState_Type.__name__ = "Integer32"
_MscVrPpSrtBpStpPortState_Object = MibTableColumn
mscVrPpSrtBpStpPortState = _MscVrPpSrtBpStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 2),
    _MscVrPpSrtBpStpPortState_Type()
)
mscVrPpSrtBpStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpPortState.setStatus("mandatory")


class _MscVrPpSrtBpStpTypeOper_Type(Integer32):
    """Custom type mscVrPpSrtBpStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpSrtBpStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpSrtBpStpTypeOper_Object = MibTableColumn
mscVrPpSrtBpStpTypeOper = _MscVrPpSrtBpStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 3),
    _MscVrPpSrtBpStpTypeOper_Type()
)
mscVrPpSrtBpStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpStpTypeOper.setStatus("mandatory")


class _MscVrPpSrtBpDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpSrtBpDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrtBpDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpDesignatedCost_Object = MibTableColumn
mscVrPpSrtBpDesignatedCost = _MscVrPpSrtBpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 4),
    _MscVrPpSrtBpDesignatedCost_Type()
)
mscVrPpSrtBpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDesignatedCost.setStatus("mandatory")


class _MscVrPpSrtBpPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpSrtBpPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrtBpPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpPathCostOper_Object = MibTableColumn
mscVrPpSrtBpPathCostOper = _MscVrPpSrtBpPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 5),
    _MscVrPpSrtBpPathCostOper_Type()
)
mscVrPpSrtBpPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpPathCostOper.setStatus("mandatory")


class _MscVrPpSrtBpDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpSrtBpDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrtBpDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpSrtBpDesignatedBridge_Object = MibTableColumn
mscVrPpSrtBpDesignatedBridge = _MscVrPpSrtBpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 6),
    _MscVrPpSrtBpDesignatedBridge_Type()
)
mscVrPpSrtBpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDesignatedBridge.setStatus("mandatory")


class _MscVrPpSrtBpDesignatedPort_Type(Hex):
    """Custom type mscVrPpSrtBpDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrtBpDesignatedPort_Type.__name__ = "Hex"
_MscVrPpSrtBpDesignatedPort_Object = MibTableColumn
mscVrPpSrtBpDesignatedPort = _MscVrPpSrtBpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 7),
    _MscVrPpSrtBpDesignatedPort_Type()
)
mscVrPpSrtBpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDesignatedPort.setStatus("mandatory")
_MscVrPpSrtBpForwardTransitions_Type = Counter32
_MscVrPpSrtBpForwardTransitions_Object = MibTableColumn
mscVrPpSrtBpForwardTransitions = _MscVrPpSrtBpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 8),
    _MscVrPpSrtBpForwardTransitions_Type()
)
mscVrPpSrtBpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpForwardTransitions.setStatus("mandatory")
_MscVrPpSrtBpBlockingDiscards_Type = Counter32
_MscVrPpSrtBpBlockingDiscards_Object = MibTableColumn
mscVrPpSrtBpBlockingDiscards = _MscVrPpSrtBpBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 9),
    _MscVrPpSrtBpBlockingDiscards_Type()
)
mscVrPpSrtBpBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBlockingDiscards.setStatus("mandatory")


class _MscVrPpSrtBpDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpSrtBpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrtBpDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpSrtBpDesignatedRoot_Object = MibTableColumn
mscVrPpSrtBpDesignatedRoot = _MscVrPpSrtBpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 18, 1, 10),
    _MscVrPpSrtBpDesignatedRoot_Type()
)
mscVrPpSrtBpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDesignatedRoot.setStatus("mandatory")
_MscVrPpSrtBpStatsTable_Object = MibTable
mscVrPpSrtBpStatsTable = _MscVrPpSrtBpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStatsTable.setStatus("mandatory")
_MscVrPpSrtBpStatsEntry_Object = MibTableRow
mscVrPpSrtBpStatsEntry = _MscVrPpSrtBpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19, 1)
)
mscVrPpSrtBpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpStatsEntry.setStatus("mandatory")
_MscVrPpSrtBpBadAbstractDiscards_Type = Counter32
_MscVrPpSrtBpBadAbstractDiscards_Object = MibTableColumn
mscVrPpSrtBpBadAbstractDiscards = _MscVrPpSrtBpBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19, 1, 1),
    _MscVrPpSrtBpBadAbstractDiscards_Type()
)
mscVrPpSrtBpBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBadAbstractDiscards.setStatus("mandatory")
_MscVrPpSrtBpTinygramFramesIn_Type = Counter32
_MscVrPpSrtBpTinygramFramesIn_Object = MibTableColumn
mscVrPpSrtBpTinygramFramesIn = _MscVrPpSrtBpTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19, 1, 2),
    _MscVrPpSrtBpTinygramFramesIn_Type()
)
mscVrPpSrtBpTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpTinygramFramesIn.setStatus("mandatory")
_MscVrPpSrtBpTinygramFramesOut_Type = Counter32
_MscVrPpSrtBpTinygramFramesOut_Object = MibTableColumn
mscVrPpSrtBpTinygramFramesOut = _MscVrPpSrtBpTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19, 1, 3),
    _MscVrPpSrtBpTinygramFramesOut_Type()
)
mscVrPpSrtBpTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpTinygramFramesOut.setStatus("mandatory")
_MscVrPpSrtBpInFilterDiscards_Type = Counter32
_MscVrPpSrtBpInFilterDiscards_Object = MibTableColumn
mscVrPpSrtBpInFilterDiscards = _MscVrPpSrtBpInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19, 1, 4),
    _MscVrPpSrtBpInFilterDiscards_Type()
)
mscVrPpSrtBpInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpInFilterDiscards.setStatus("mandatory")
_MscVrPpSrtBpOutFilterDiscards_Type = Counter32
_MscVrPpSrtBpOutFilterDiscards_Object = MibTableColumn
mscVrPpSrtBpOutFilterDiscards = _MscVrPpSrtBpOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 19, 1, 5),
    _MscVrPpSrtBpOutFilterDiscards_Type()
)
mscVrPpSrtBpOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrtBpSrProvTable_Object = MibTable
mscVrPpSrtBpSrProvTable = _MscVrPpSrtBpSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpSrProvTable.setStatus("mandatory")
_MscVrPpSrtBpSrProvEntry_Object = MibTableRow
mscVrPpSrtBpSrProvEntry = _MscVrPpSrtBpSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1)
)
mscVrPpSrtBpSrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpSrProvEntry.setStatus("mandatory")


class _MscVrPpSrtBpHopCount_Type(Unsigned32):
    """Custom type mscVrPpSrtBpHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrPpSrtBpHopCount_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpHopCount_Object = MibTableColumn
mscVrPpSrtBpHopCount = _MscVrPpSrtBpHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 1),
    _MscVrPpSrtBpHopCount_Type()
)
mscVrPpSrtBpHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpHopCount.setStatus("mandatory")


class _MscVrPpSrtBpExploreFrameTreatment_Type(Integer32):
    """Custom type mscVrPpSrtBpExploreFrameTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encap", 0),
          ("xlate", 1))
    )


_MscVrPpSrtBpExploreFrameTreatment_Type.__name__ = "Integer32"
_MscVrPpSrtBpExploreFrameTreatment_Object = MibTableColumn
mscVrPpSrtBpExploreFrameTreatment = _MscVrPpSrtBpExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 2),
    _MscVrPpSrtBpExploreFrameTreatment_Type()
)
mscVrPpSrtBpExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpExploreFrameTreatment.setStatus("mandatory")


class _MscVrPpSrtBpLanId_Type(Unsigned32):
    """Custom type mscVrPpSrtBpLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrtBpLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpLanId_Object = MibTableColumn
mscVrPpSrtBpLanId = _MscVrPpSrtBpLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 3),
    _MscVrPpSrtBpLanId_Type()
)
mscVrPpSrtBpLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpLanId.setStatus("mandatory")


class _MscVrPpSrtBpInternalLanId_Type(Unsigned32):
    """Custom type mscVrPpSrtBpInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrtBpInternalLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpInternalLanId_Object = MibTableColumn
mscVrPpSrtBpInternalLanId = _MscVrPpSrtBpInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 4),
    _MscVrPpSrtBpInternalLanId_Type()
)
mscVrPpSrtBpInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpInternalLanId.setStatus("mandatory")


class _MscVrPpSrtBpBridgeNum_Type(Unsigned32):
    """Custom type mscVrPpSrtBpBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrPpSrtBpBridgeNum_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpBridgeNum_Object = MibTableColumn
mscVrPpSrtBpBridgeNum = _MscVrPpSrtBpBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 5),
    _MscVrPpSrtBpBridgeNum_Type()
)
mscVrPpSrtBpBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpBridgeNum.setStatus("mandatory")


class _MscVrPpSrtBpLargestFrame_Type(Unsigned32):
    """Custom type mscVrPpSrtBpLargestFrame based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 516),
        ValueRangeConstraint(1470, 1470),
        ValueRangeConstraint(2052, 2052),
        ValueRangeConstraint(4399, 4399),
        ValueRangeConstraint(8130, 8130),
        ValueRangeConstraint(11407, 11407),
        ValueRangeConstraint(17749, 17749),
    )


_MscVrPpSrtBpLargestFrame_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpLargestFrame_Object = MibTableColumn
mscVrPpSrtBpLargestFrame = _MscVrPpSrtBpLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 6),
    _MscVrPpSrtBpLargestFrame_Type()
)
mscVrPpSrtBpLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpLargestFrame.setStatus("mandatory")


class _MscVrPpSrtBpSteSpanMode_Type(Integer32):
    """Custom type mscVrPpSrtBpSteSpanMode based on Integer32"""
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
        *(("autoSpan", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_MscVrPpSrtBpSteSpanMode_Type.__name__ = "Integer32"
_MscVrPpSrtBpSteSpanMode_Object = MibTableColumn
mscVrPpSrtBpSteSpanMode = _MscVrPpSrtBpSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 7),
    _MscVrPpSrtBpSteSpanMode_Type()
)
mscVrPpSrtBpSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSteSpanMode.setStatus("mandatory")


class _MscVrPpSrtBpAreRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrtBpAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrtBpAreRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpAreRdLimit_Object = MibTableColumn
mscVrPpSrtBpAreRdLimit = _MscVrPpSrtBpAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 8),
    _MscVrPpSrtBpAreRdLimit_Type()
)
mscVrPpSrtBpAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpAreRdLimit.setStatus("mandatory")


class _MscVrPpSrtBpSteRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrtBpSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrtBpSteRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrtBpSteRdLimit_Object = MibTableColumn
mscVrPpSrtBpSteRdLimit = _MscVrPpSrtBpSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 20, 1, 9),
    _MscVrPpSrtBpSteRdLimit_Type()
)
mscVrPpSrtBpSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSteRdLimit.setStatus("mandatory")
_MscVrPpSrtBpSrStatsTable_Object = MibTable
mscVrPpSrtBpSrStatsTable = _MscVrPpSrtBpSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21)
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpSrStatsTable.setStatus("mandatory")
_MscVrPpSrtBpSrStatsEntry_Object = MibTableRow
mscVrPpSrtBpSrStatsEntry = _MscVrPpSrtBpSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1)
)
mscVrPpSrtBpSrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrtBpSrStatsEntry.setStatus("mandatory")
_MscVrPpSrtBpSpecInFrames_Type = Counter32
_MscVrPpSrtBpSpecInFrames_Object = MibTableColumn
mscVrPpSrtBpSpecInFrames = _MscVrPpSrtBpSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 1),
    _MscVrPpSrtBpSpecInFrames_Type()
)
mscVrPpSrtBpSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSpecInFrames.setStatus("mandatory")
_MscVrPpSrtBpSpecOutFrames_Type = Counter32
_MscVrPpSrtBpSpecOutFrames_Object = MibTableColumn
mscVrPpSrtBpSpecOutFrames = _MscVrPpSrtBpSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 2),
    _MscVrPpSrtBpSpecOutFrames_Type()
)
mscVrPpSrtBpSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSpecOutFrames.setStatus("mandatory")
_MscVrPpSrtBpApeInFrames_Type = Counter32
_MscVrPpSrtBpApeInFrames_Object = MibTableColumn
mscVrPpSrtBpApeInFrames = _MscVrPpSrtBpApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 3),
    _MscVrPpSrtBpApeInFrames_Type()
)
mscVrPpSrtBpApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpApeInFrames.setStatus("mandatory")
_MscVrPpSrtBpApeOutFrames_Type = Counter32
_MscVrPpSrtBpApeOutFrames_Object = MibTableColumn
mscVrPpSrtBpApeOutFrames = _MscVrPpSrtBpApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 4),
    _MscVrPpSrtBpApeOutFrames_Type()
)
mscVrPpSrtBpApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpApeOutFrames.setStatus("mandatory")
_MscVrPpSrtBpSteInFrames_Type = Counter32
_MscVrPpSrtBpSteInFrames_Object = MibTableColumn
mscVrPpSrtBpSteInFrames = _MscVrPpSrtBpSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 5),
    _MscVrPpSrtBpSteInFrames_Type()
)
mscVrPpSrtBpSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSteInFrames.setStatus("mandatory")
_MscVrPpSrtBpSteOutFrames_Type = Counter32
_MscVrPpSrtBpSteOutFrames_Object = MibTableColumn
mscVrPpSrtBpSteOutFrames = _MscVrPpSrtBpSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 6),
    _MscVrPpSrtBpSteOutFrames_Type()
)
mscVrPpSrtBpSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSteOutFrames.setStatus("mandatory")
_MscVrPpSrtBpSegmentMismatchDiscards_Type = Counter32
_MscVrPpSrtBpSegmentMismatchDiscards_Object = MibTableColumn
mscVrPpSrtBpSegmentMismatchDiscards = _MscVrPpSrtBpSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 7),
    _MscVrPpSrtBpSegmentMismatchDiscards_Type()
)
mscVrPpSrtBpSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpSegmentMismatchDiscards.setStatus("mandatory")
_MscVrPpSrtBpDupSegmentDiscards_Type = Counter32
_MscVrPpSrtBpDupSegmentDiscards_Object = MibTableColumn
mscVrPpSrtBpDupSegmentDiscards = _MscVrPpSrtBpDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 8),
    _MscVrPpSrtBpDupSegmentDiscards_Type()
)
mscVrPpSrtBpDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDupSegmentDiscards.setStatus("mandatory")
_MscVrPpSrtBpHopCountExceededDiscards_Type = Counter32
_MscVrPpSrtBpHopCountExceededDiscards_Object = MibTableColumn
mscVrPpSrtBpHopCountExceededDiscards = _MscVrPpSrtBpHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 9),
    _MscVrPpSrtBpHopCountExceededDiscards_Type()
)
mscVrPpSrtBpHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpHopCountExceededDiscards.setStatus("mandatory")
_MscVrPpSrtBpDupLanIdOrTreeErrors_Type = Counter32
_MscVrPpSrtBpDupLanIdOrTreeErrors_Object = MibTableColumn
mscVrPpSrtBpDupLanIdOrTreeErrors = _MscVrPpSrtBpDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 10),
    _MscVrPpSrtBpDupLanIdOrTreeErrors_Type()
)
mscVrPpSrtBpDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDupLanIdOrTreeErrors.setStatus("mandatory")
_MscVrPpSrtBpLanIdMismatches_Type = Counter32
_MscVrPpSrtBpLanIdMismatches_Object = MibTableColumn
mscVrPpSrtBpLanIdMismatches = _MscVrPpSrtBpLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 11),
    _MscVrPpSrtBpLanIdMismatches_Type()
)
mscVrPpSrtBpLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpLanIdMismatches.setStatus("mandatory")
_MscVrPpSrtBpStaticDiscards_Type = Counter32
_MscVrPpSrtBpStaticDiscards_Object = MibTableColumn
mscVrPpSrtBpStaticDiscards = _MscVrPpSrtBpStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 12),
    _MscVrPpSrtBpStaticDiscards_Type()
)
mscVrPpSrtBpStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpStaticDiscards.setStatus("mandatory")
_MscVrPpSrtBpDynamicDiscards_Type = Counter32
_MscVrPpSrtBpDynamicDiscards_Object = MibTableColumn
mscVrPpSrtBpDynamicDiscards = _MscVrPpSrtBpDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 9, 21, 1, 13),
    _MscVrPpSrtBpDynamicDiscards_Type()
)
mscVrPpSrtBpDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrtBpDynamicDiscards.setStatus("mandatory")
_MscVrPpSrse_ObjectIdentity = ObjectIdentity
mscVrPpSrse = _MscVrPpSrse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10)
)
_MscVrPpSrseRowStatusTable_Object = MibTable
mscVrPpSrseRowStatusTable = _MscVrPpSrseRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrseRowStatusTable.setStatus("mandatory")
_MscVrPpSrseRowStatusEntry_Object = MibTableRow
mscVrPpSrseRowStatusEntry = _MscVrPpSrseRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 1, 1)
)
mscVrPpSrseRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseRowStatusEntry.setStatus("mandatory")
_MscVrPpSrseRowStatus_Type = RowStatus
_MscVrPpSrseRowStatus_Object = MibTableColumn
mscVrPpSrseRowStatus = _MscVrPpSrseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 1, 1, 1),
    _MscVrPpSrseRowStatus_Type()
)
mscVrPpSrseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseRowStatus.setStatus("mandatory")
_MscVrPpSrseComponentName_Type = DisplayString
_MscVrPpSrseComponentName_Object = MibTableColumn
mscVrPpSrseComponentName = _MscVrPpSrseComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 1, 1, 2),
    _MscVrPpSrseComponentName_Type()
)
mscVrPpSrseComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseComponentName.setStatus("mandatory")
_MscVrPpSrseStorageType_Type = StorageType
_MscVrPpSrseStorageType_Object = MibTableColumn
mscVrPpSrseStorageType = _MscVrPpSrseStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 1, 1, 4),
    _MscVrPpSrseStorageType_Type()
)
mscVrPpSrseStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseStorageType.setStatus("mandatory")
_MscVrPpSrseIndex_Type = NonReplicated
_MscVrPpSrseIndex_Object = MibTableColumn
mscVrPpSrseIndex = _MscVrPpSrseIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 1, 1, 10),
    _MscVrPpSrseIndex_Type()
)
mscVrPpSrseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrseIndex.setStatus("mandatory")
_MscVrPpSrseProvTable_Object = MibTable
mscVrPpSrseProvTable = _MscVrPpSrseProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrseProvTable.setStatus("mandatory")
_MscVrPpSrseProvEntry_Object = MibTableRow
mscVrPpSrseProvEntry = _MscVrPpSrseProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10, 1)
)
mscVrPpSrseProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseProvEntry.setStatus("mandatory")


class _MscVrPpSrseTranslateIpx_Type(Integer32):
    """Custom type mscVrPpSrseTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpSrseTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpSrseTranslateIpx_Object = MibTableColumn
mscVrPpSrseTranslateIpx = _MscVrPpSrseTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10, 1, 1),
    _MscVrPpSrseTranslateIpx_Type()
)
mscVrPpSrseTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseTranslateIpx.setStatus("mandatory")


class _MscVrPpSrseFragmentIp_Type(Integer32):
    """Custom type mscVrPpSrseFragmentIp based on Integer32"""
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


_MscVrPpSrseFragmentIp_Type.__name__ = "Integer32"
_MscVrPpSrseFragmentIp_Object = MibTableColumn
mscVrPpSrseFragmentIp = _MscVrPpSrseFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10, 1, 2),
    _MscVrPpSrseFragmentIp_Type()
)
mscVrPpSrseFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseFragmentIp.setStatus("mandatory")


class _MscVrPpSrseServiceClass_Type(Integer32):
    """Custom type mscVrPpSrseServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpSrseServiceClass_Type.__name__ = "Integer32"
_MscVrPpSrseServiceClass_Object = MibTableColumn
mscVrPpSrseServiceClass = _MscVrPpSrseServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10, 1, 3),
    _MscVrPpSrseServiceClass_Type()
)
mscVrPpSrseServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseServiceClass.setStatus("mandatory")


class _MscVrPpSrseConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpSrseConvertArpMacAddress based on Integer32"""
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


_MscVrPpSrseConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpSrseConvertArpMacAddress_Object = MibTableColumn
mscVrPpSrseConvertArpMacAddress = _MscVrPpSrseConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10, 1, 4),
    _MscVrPpSrseConvertArpMacAddress_Type()
)
mscVrPpSrseConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpSrsePortNum_Type(Unsigned32):
    """Custom type mscVrPpSrsePortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpSrsePortNum_Type.__name__ = "Unsigned32"
_MscVrPpSrsePortNum_Object = MibTableColumn
mscVrPpSrsePortNum = _MscVrPpSrsePortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 10, 1, 5),
    _MscVrPpSrsePortNum_Type()
)
mscVrPpSrsePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsePortNum.setStatus("mandatory")
_MscVrPpSrseStpProvTable_Object = MibTable
mscVrPpSrseStpProvTable = _MscVrPpSrseStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12)
)
if mibBuilder.loadTexts:
    mscVrPpSrseStpProvTable.setStatus("mandatory")
_MscVrPpSrseStpProvEntry_Object = MibTableRow
mscVrPpSrseStpProvEntry = _MscVrPpSrseStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1)
)
mscVrPpSrseStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseStpProvEntry.setStatus("mandatory")


class _MscVrPpSrseAdminStatus_Type(Integer32):
    """Custom type mscVrPpSrseAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpSrseAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSrseAdminStatus_Object = MibTableColumn
mscVrPpSrseAdminStatus = _MscVrPpSrseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1, 1),
    _MscVrPpSrseAdminStatus_Type()
)
mscVrPpSrseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseAdminStatus.setStatus("mandatory")


class _MscVrPpSrsePortStateStpControl_Type(Integer32):
    """Custom type mscVrPpSrsePortStateStpControl based on Integer32"""
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


_MscVrPpSrsePortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpSrsePortStateStpControl_Object = MibTableColumn
mscVrPpSrsePortStateStpControl = _MscVrPpSrsePortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1, 2),
    _MscVrPpSrsePortStateStpControl_Type()
)
mscVrPpSrsePortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsePortStateStpControl.setStatus("mandatory")


class _MscVrPpSrseStpTypeProv_Type(Integer32):
    """Custom type mscVrPpSrseStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpSrseStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpSrseStpTypeProv_Object = MibTableColumn
mscVrPpSrseStpTypeProv = _MscVrPpSrseStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1, 3),
    _MscVrPpSrseStpTypeProv_Type()
)
mscVrPpSrseStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseStpTypeProv.setStatus("mandatory")


class _MscVrPpSrsePortPriority_Type(Unsigned32):
    """Custom type mscVrPpSrsePortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrsePortPriority_Type.__name__ = "Unsigned32"
_MscVrPpSrsePortPriority_Object = MibTableColumn
mscVrPpSrsePortPriority = _MscVrPpSrsePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1, 4),
    _MscVrPpSrsePortPriority_Type()
)
mscVrPpSrsePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsePortPriority.setStatus("mandatory")


class _MscVrPpSrsePathCost_Type(Unsigned32):
    """Custom type mscVrPpSrsePathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrsePathCost_Type.__name__ = "Unsigned32"
_MscVrPpSrsePathCost_Object = MibTableColumn
mscVrPpSrsePathCost = _MscVrPpSrsePathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1, 5),
    _MscVrPpSrsePathCost_Type()
)
mscVrPpSrsePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsePathCost.setStatus("mandatory")


class _MscVrPpSrsePathCostMethod_Type(Integer32):
    """Custom type mscVrPpSrsePathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpSrsePathCostMethod_Type.__name__ = "Integer32"
_MscVrPpSrsePathCostMethod_Object = MibTableColumn
mscVrPpSrsePathCostMethod = _MscVrPpSrsePathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 12, 1, 6),
    _MscVrPpSrsePathCostMethod_Type()
)
mscVrPpSrsePathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsePathCostMethod.setStatus("mandatory")
_MscVrPpSrseDIProvTable_Object = MibTable
mscVrPpSrseDIProvTable = _MscVrPpSrseDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 13)
)
if mibBuilder.loadTexts:
    mscVrPpSrseDIProvTable.setStatus("mandatory")
_MscVrPpSrseDIProvEntry_Object = MibTableRow
mscVrPpSrseDIProvEntry = _MscVrPpSrseDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 13, 1)
)
mscVrPpSrseDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseDIProvEntry.setStatus("mandatory")


class _MscVrPpSrseDomainNum_Type(Unsigned32):
    """Custom type mscVrPpSrseDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpSrseDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpSrseDomainNum_Object = MibTableColumn
mscVrPpSrseDomainNum = _MscVrPpSrseDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 13, 1, 1),
    _MscVrPpSrseDomainNum_Type()
)
mscVrPpSrseDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseDomainNum.setStatus("mandatory")


class _MscVrPpSrsePreserveDomain_Type(Integer32):
    """Custom type mscVrPpSrsePreserveDomain based on Integer32"""
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


_MscVrPpSrsePreserveDomain_Type.__name__ = "Integer32"
_MscVrPpSrsePreserveDomain_Object = MibTableColumn
mscVrPpSrsePreserveDomain = _MscVrPpSrsePreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 13, 1, 2),
    _MscVrPpSrsePreserveDomain_Type()
)
mscVrPpSrsePreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsePreserveDomain.setStatus("mandatory")
_MscVrPpSrseStateTable_Object = MibTable
mscVrPpSrseStateTable = _MscVrPpSrseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 14)
)
if mibBuilder.loadTexts:
    mscVrPpSrseStateTable.setStatus("mandatory")
_MscVrPpSrseStateEntry_Object = MibTableRow
mscVrPpSrseStateEntry = _MscVrPpSrseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 14, 1)
)
mscVrPpSrseStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseStateEntry.setStatus("mandatory")


class _MscVrPpSrseAdminState_Type(Integer32):
    """Custom type mscVrPpSrseAdminState based on Integer32"""
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


_MscVrPpSrseAdminState_Type.__name__ = "Integer32"
_MscVrPpSrseAdminState_Object = MibTableColumn
mscVrPpSrseAdminState = _MscVrPpSrseAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 14, 1, 1),
    _MscVrPpSrseAdminState_Type()
)
mscVrPpSrseAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseAdminState.setStatus("mandatory")


class _MscVrPpSrseOperationalState_Type(Integer32):
    """Custom type mscVrPpSrseOperationalState based on Integer32"""
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


_MscVrPpSrseOperationalState_Type.__name__ = "Integer32"
_MscVrPpSrseOperationalState_Object = MibTableColumn
mscVrPpSrseOperationalState = _MscVrPpSrseOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 14, 1, 2),
    _MscVrPpSrseOperationalState_Type()
)
mscVrPpSrseOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseOperationalState.setStatus("mandatory")


class _MscVrPpSrseUsageState_Type(Integer32):
    """Custom type mscVrPpSrseUsageState based on Integer32"""
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


_MscVrPpSrseUsageState_Type.__name__ = "Integer32"
_MscVrPpSrseUsageState_Object = MibTableColumn
mscVrPpSrseUsageState = _MscVrPpSrseUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 14, 1, 3),
    _MscVrPpSrseUsageState_Type()
)
mscVrPpSrseUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseUsageState.setStatus("mandatory")
_MscVrPpSrseOperStatusTable_Object = MibTable
mscVrPpSrseOperStatusTable = _MscVrPpSrseOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 15)
)
if mibBuilder.loadTexts:
    mscVrPpSrseOperStatusTable.setStatus("mandatory")
_MscVrPpSrseOperStatusEntry_Object = MibTableRow
mscVrPpSrseOperStatusEntry = _MscVrPpSrseOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 15, 1)
)
mscVrPpSrseOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseOperStatusEntry.setStatus("mandatory")


class _MscVrPpSrseSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSrseSnmpOperStatus based on Integer32"""
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


_MscVrPpSrseSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSrseSnmpOperStatus_Object = MibTableColumn
mscVrPpSrseSnmpOperStatus = _MscVrPpSrseSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 15, 1, 1),
    _MscVrPpSrseSnmpOperStatus_Type()
)
mscVrPpSrseSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseSnmpOperStatus.setStatus("mandatory")
_MscVrPpSrseOperTable_Object = MibTable
mscVrPpSrseOperTable = _MscVrPpSrseOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16)
)
if mibBuilder.loadTexts:
    mscVrPpSrseOperTable.setStatus("mandatory")
_MscVrPpSrseOperEntry_Object = MibTableRow
mscVrPpSrseOperEntry = _MscVrPpSrseOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1)
)
mscVrPpSrseOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseOperEntry.setStatus("mandatory")


class _MscVrPpSrsePortName_Type(AsciiString):
    """Custom type mscVrPpSrsePortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpSrsePortName_Type.__name__ = "AsciiString"
_MscVrPpSrsePortName_Object = MibTableColumn
mscVrPpSrsePortName = _MscVrPpSrsePortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 1),
    _MscVrPpSrsePortName_Type()
)
mscVrPpSrsePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsePortName.setStatus("mandatory")


class _MscVrPpSrseUpTime_Type(Unsigned32):
    """Custom type mscVrPpSrseUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrseUpTime_Type.__name__ = "Unsigned32"
_MscVrPpSrseUpTime_Object = MibTableColumn
mscVrPpSrseUpTime = _MscVrPpSrseUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 3),
    _MscVrPpSrseUpTime_Type()
)
mscVrPpSrseUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseUpTime.setStatus("mandatory")


class _MscVrPpSrseDownTime_Type(Unsigned32):
    """Custom type mscVrPpSrseDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrseDownTime_Type.__name__ = "Unsigned32"
_MscVrPpSrseDownTime_Object = MibTableColumn
mscVrPpSrseDownTime = _MscVrPpSrseDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 4),
    _MscVrPpSrseDownTime_Type()
)
mscVrPpSrseDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDownTime.setStatus("mandatory")


class _MscVrPpSrseBridgingMode_Type(Integer32):
    """Custom type mscVrPpSrseBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpSrseBridgingMode_Type.__name__ = "Integer32"
_MscVrPpSrseBridgingMode_Object = MibTableColumn
mscVrPpSrseBridgingMode = _MscVrPpSrseBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 5),
    _MscVrPpSrseBridgingMode_Type()
)
mscVrPpSrseBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseBridgingMode.setStatus("mandatory")


class _MscVrPpSrseBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpSrseBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpSrseBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpSrseBridgePortConfig_Object = MibTableColumn
mscVrPpSrseBridgePortConfig = _MscVrPpSrseBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 6),
    _MscVrPpSrseBridgePortConfig_Type()
)
mscVrPpSrseBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseBridgePortConfig.setStatus("mandatory")


class _MscVrPpSrseBridgePortType_Type(Integer32):
    """Custom type mscVrPpSrseBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpSrseBridgePortType_Type.__name__ = "Integer32"
_MscVrPpSrseBridgePortType_Object = MibTableColumn
mscVrPpSrseBridgePortType = _MscVrPpSrseBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 7),
    _MscVrPpSrseBridgePortType_Type()
)
mscVrPpSrseBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseBridgePortType.setStatus("mandatory")


class _MscVrPpSrseIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpSrseIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrseIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpSrseIfIndex_Object = MibTableColumn
mscVrPpSrseIfIndex = _MscVrPpSrseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 8),
    _MscVrPpSrseIfIndex_Type()
)
mscVrPpSrseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseIfIndex.setStatus("mandatory")
_MscVrPpSrseDelayExceededDiscards_Type = Counter32
_MscVrPpSrseDelayExceededDiscards_Object = MibTableColumn
mscVrPpSrseDelayExceededDiscards = _MscVrPpSrseDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 10),
    _MscVrPpSrseDelayExceededDiscards_Type()
)
mscVrPpSrseDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDelayExceededDiscards.setStatus("mandatory")
_MscVrPpSrseMtuExceededDiscards_Type = Counter32
_MscVrPpSrseMtuExceededDiscards_Object = MibTableColumn
mscVrPpSrseMtuExceededDiscards = _MscVrPpSrseMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 16, 1, 11),
    _MscVrPpSrseMtuExceededDiscards_Type()
)
mscVrPpSrseMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseMtuExceededDiscards.setStatus("mandatory")
_MscVrPpSrseStpOperTable_Object = MibTable
mscVrPpSrseStpOperTable = _MscVrPpSrseStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18)
)
if mibBuilder.loadTexts:
    mscVrPpSrseStpOperTable.setStatus("mandatory")
_MscVrPpSrseStpOperEntry_Object = MibTableRow
mscVrPpSrseStpOperEntry = _MscVrPpSrseStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1)
)
mscVrPpSrseStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseStpOperEntry.setStatus("mandatory")


class _MscVrPpSrseStpPortState_Type(Integer32):
    """Custom type mscVrPpSrseStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpSrseStpPortState_Type.__name__ = "Integer32"
_MscVrPpSrseStpPortState_Object = MibTableColumn
mscVrPpSrseStpPortState = _MscVrPpSrseStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 2),
    _MscVrPpSrseStpPortState_Type()
)
mscVrPpSrseStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseStpPortState.setStatus("mandatory")


class _MscVrPpSrseStpTypeOper_Type(Integer32):
    """Custom type mscVrPpSrseStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpSrseStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpSrseStpTypeOper_Object = MibTableColumn
mscVrPpSrseStpTypeOper = _MscVrPpSrseStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 3),
    _MscVrPpSrseStpTypeOper_Type()
)
mscVrPpSrseStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseStpTypeOper.setStatus("mandatory")


class _MscVrPpSrseDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpSrseDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrseDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpSrseDesignatedCost_Object = MibTableColumn
mscVrPpSrseDesignatedCost = _MscVrPpSrseDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 4),
    _MscVrPpSrseDesignatedCost_Type()
)
mscVrPpSrseDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDesignatedCost.setStatus("mandatory")


class _MscVrPpSrsePathCostOper_Type(Unsigned32):
    """Custom type mscVrPpSrsePathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrsePathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpSrsePathCostOper_Object = MibTableColumn
mscVrPpSrsePathCostOper = _MscVrPpSrsePathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 5),
    _MscVrPpSrsePathCostOper_Type()
)
mscVrPpSrsePathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsePathCostOper.setStatus("mandatory")


class _MscVrPpSrseDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpSrseDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrseDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpSrseDesignatedBridge_Object = MibTableColumn
mscVrPpSrseDesignatedBridge = _MscVrPpSrseDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 6),
    _MscVrPpSrseDesignatedBridge_Type()
)
mscVrPpSrseDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDesignatedBridge.setStatus("mandatory")


class _MscVrPpSrseDesignatedPort_Type(Hex):
    """Custom type mscVrPpSrseDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrseDesignatedPort_Type.__name__ = "Hex"
_MscVrPpSrseDesignatedPort_Object = MibTableColumn
mscVrPpSrseDesignatedPort = _MscVrPpSrseDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 7),
    _MscVrPpSrseDesignatedPort_Type()
)
mscVrPpSrseDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDesignatedPort.setStatus("mandatory")
_MscVrPpSrseForwardTransitions_Type = Counter32
_MscVrPpSrseForwardTransitions_Object = MibTableColumn
mscVrPpSrseForwardTransitions = _MscVrPpSrseForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 8),
    _MscVrPpSrseForwardTransitions_Type()
)
mscVrPpSrseForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseForwardTransitions.setStatus("mandatory")
_MscVrPpSrseBlockingDiscards_Type = Counter32
_MscVrPpSrseBlockingDiscards_Object = MibTableColumn
mscVrPpSrseBlockingDiscards = _MscVrPpSrseBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 9),
    _MscVrPpSrseBlockingDiscards_Type()
)
mscVrPpSrseBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseBlockingDiscards.setStatus("mandatory")


class _MscVrPpSrseDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpSrseDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrseDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpSrseDesignatedRoot_Object = MibTableColumn
mscVrPpSrseDesignatedRoot = _MscVrPpSrseDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 18, 1, 10),
    _MscVrPpSrseDesignatedRoot_Type()
)
mscVrPpSrseDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDesignatedRoot.setStatus("mandatory")
_MscVrPpSrseStatsTable_Object = MibTable
mscVrPpSrseStatsTable = _MscVrPpSrseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19)
)
if mibBuilder.loadTexts:
    mscVrPpSrseStatsTable.setStatus("mandatory")
_MscVrPpSrseStatsEntry_Object = MibTableRow
mscVrPpSrseStatsEntry = _MscVrPpSrseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19, 1)
)
mscVrPpSrseStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseStatsEntry.setStatus("mandatory")
_MscVrPpSrseBadAbstractDiscards_Type = Counter32
_MscVrPpSrseBadAbstractDiscards_Object = MibTableColumn
mscVrPpSrseBadAbstractDiscards = _MscVrPpSrseBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19, 1, 1),
    _MscVrPpSrseBadAbstractDiscards_Type()
)
mscVrPpSrseBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseBadAbstractDiscards.setStatus("mandatory")
_MscVrPpSrseTinygramFramesIn_Type = Counter32
_MscVrPpSrseTinygramFramesIn_Object = MibTableColumn
mscVrPpSrseTinygramFramesIn = _MscVrPpSrseTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19, 1, 2),
    _MscVrPpSrseTinygramFramesIn_Type()
)
mscVrPpSrseTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseTinygramFramesIn.setStatus("mandatory")
_MscVrPpSrseTinygramFramesOut_Type = Counter32
_MscVrPpSrseTinygramFramesOut_Object = MibTableColumn
mscVrPpSrseTinygramFramesOut = _MscVrPpSrseTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19, 1, 3),
    _MscVrPpSrseTinygramFramesOut_Type()
)
mscVrPpSrseTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseTinygramFramesOut.setStatus("mandatory")
_MscVrPpSrseInFilterDiscards_Type = Counter32
_MscVrPpSrseInFilterDiscards_Object = MibTableColumn
mscVrPpSrseInFilterDiscards = _MscVrPpSrseInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19, 1, 4),
    _MscVrPpSrseInFilterDiscards_Type()
)
mscVrPpSrseInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseInFilterDiscards.setStatus("mandatory")
_MscVrPpSrseOutFilterDiscards_Type = Counter32
_MscVrPpSrseOutFilterDiscards_Object = MibTableColumn
mscVrPpSrseOutFilterDiscards = _MscVrPpSrseOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 19, 1, 5),
    _MscVrPpSrseOutFilterDiscards_Type()
)
mscVrPpSrseOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrseSrProvTable_Object = MibTable
mscVrPpSrseSrProvTable = _MscVrPpSrseSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20)
)
if mibBuilder.loadTexts:
    mscVrPpSrseSrProvTable.setStatus("mandatory")
_MscVrPpSrseSrProvEntry_Object = MibTableRow
mscVrPpSrseSrProvEntry = _MscVrPpSrseSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1)
)
mscVrPpSrseSrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseSrProvEntry.setStatus("mandatory")


class _MscVrPpSrseHopCount_Type(Unsigned32):
    """Custom type mscVrPpSrseHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrPpSrseHopCount_Type.__name__ = "Unsigned32"
_MscVrPpSrseHopCount_Object = MibTableColumn
mscVrPpSrseHopCount = _MscVrPpSrseHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 1),
    _MscVrPpSrseHopCount_Type()
)
mscVrPpSrseHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseHopCount.setStatus("mandatory")


class _MscVrPpSrseExploreFrameTreatment_Type(Integer32):
    """Custom type mscVrPpSrseExploreFrameTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encap", 0),
          ("xlate", 1))
    )


_MscVrPpSrseExploreFrameTreatment_Type.__name__ = "Integer32"
_MscVrPpSrseExploreFrameTreatment_Object = MibTableColumn
mscVrPpSrseExploreFrameTreatment = _MscVrPpSrseExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 2),
    _MscVrPpSrseExploreFrameTreatment_Type()
)
mscVrPpSrseExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseExploreFrameTreatment.setStatus("mandatory")


class _MscVrPpSrseLanId_Type(Unsigned32):
    """Custom type mscVrPpSrseLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrseLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrseLanId_Object = MibTableColumn
mscVrPpSrseLanId = _MscVrPpSrseLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 3),
    _MscVrPpSrseLanId_Type()
)
mscVrPpSrseLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseLanId.setStatus("mandatory")


class _MscVrPpSrseInternalLanId_Type(Unsigned32):
    """Custom type mscVrPpSrseInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrseInternalLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrseInternalLanId_Object = MibTableColumn
mscVrPpSrseInternalLanId = _MscVrPpSrseInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 4),
    _MscVrPpSrseInternalLanId_Type()
)
mscVrPpSrseInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseInternalLanId.setStatus("mandatory")


class _MscVrPpSrseBridgeNum_Type(Unsigned32):
    """Custom type mscVrPpSrseBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrPpSrseBridgeNum_Type.__name__ = "Unsigned32"
_MscVrPpSrseBridgeNum_Object = MibTableColumn
mscVrPpSrseBridgeNum = _MscVrPpSrseBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 5),
    _MscVrPpSrseBridgeNum_Type()
)
mscVrPpSrseBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseBridgeNum.setStatus("mandatory")


class _MscVrPpSrseLargestFrame_Type(Unsigned32):
    """Custom type mscVrPpSrseLargestFrame based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 516),
        ValueRangeConstraint(1470, 1470),
        ValueRangeConstraint(2052, 2052),
        ValueRangeConstraint(4399, 4399),
        ValueRangeConstraint(8130, 8130),
        ValueRangeConstraint(11407, 11407),
        ValueRangeConstraint(17749, 17749),
    )


_MscVrPpSrseLargestFrame_Type.__name__ = "Unsigned32"
_MscVrPpSrseLargestFrame_Object = MibTableColumn
mscVrPpSrseLargestFrame = _MscVrPpSrseLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 6),
    _MscVrPpSrseLargestFrame_Type()
)
mscVrPpSrseLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseLargestFrame.setStatus("mandatory")


class _MscVrPpSrseSteSpanMode_Type(Integer32):
    """Custom type mscVrPpSrseSteSpanMode based on Integer32"""
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
        *(("autoSpan", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_MscVrPpSrseSteSpanMode_Type.__name__ = "Integer32"
_MscVrPpSrseSteSpanMode_Object = MibTableColumn
mscVrPpSrseSteSpanMode = _MscVrPpSrseSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 7),
    _MscVrPpSrseSteSpanMode_Type()
)
mscVrPpSrseSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseSteSpanMode.setStatus("mandatory")


class _MscVrPpSrseAreRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrseAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrseAreRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrseAreRdLimit_Object = MibTableColumn
mscVrPpSrseAreRdLimit = _MscVrPpSrseAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 8),
    _MscVrPpSrseAreRdLimit_Type()
)
mscVrPpSrseAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseAreRdLimit.setStatus("mandatory")


class _MscVrPpSrseSteRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrseSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrseSteRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrseSteRdLimit_Object = MibTableColumn
mscVrPpSrseSteRdLimit = _MscVrPpSrseSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 20, 1, 9),
    _MscVrPpSrseSteRdLimit_Type()
)
mscVrPpSrseSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrseSteRdLimit.setStatus("mandatory")
_MscVrPpSrseSrStatsTable_Object = MibTable
mscVrPpSrseSrStatsTable = _MscVrPpSrseSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21)
)
if mibBuilder.loadTexts:
    mscVrPpSrseSrStatsTable.setStatus("mandatory")
_MscVrPpSrseSrStatsEntry_Object = MibTableRow
mscVrPpSrseSrStatsEntry = _MscVrPpSrseSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1)
)
mscVrPpSrseSrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrseSrStatsEntry.setStatus("mandatory")
_MscVrPpSrseSpecInFrames_Type = Counter32
_MscVrPpSrseSpecInFrames_Object = MibTableColumn
mscVrPpSrseSpecInFrames = _MscVrPpSrseSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 1),
    _MscVrPpSrseSpecInFrames_Type()
)
mscVrPpSrseSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseSpecInFrames.setStatus("mandatory")
_MscVrPpSrseSpecOutFrames_Type = Counter32
_MscVrPpSrseSpecOutFrames_Object = MibTableColumn
mscVrPpSrseSpecOutFrames = _MscVrPpSrseSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 2),
    _MscVrPpSrseSpecOutFrames_Type()
)
mscVrPpSrseSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseSpecOutFrames.setStatus("mandatory")
_MscVrPpSrseApeInFrames_Type = Counter32
_MscVrPpSrseApeInFrames_Object = MibTableColumn
mscVrPpSrseApeInFrames = _MscVrPpSrseApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 3),
    _MscVrPpSrseApeInFrames_Type()
)
mscVrPpSrseApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseApeInFrames.setStatus("mandatory")
_MscVrPpSrseApeOutFrames_Type = Counter32
_MscVrPpSrseApeOutFrames_Object = MibTableColumn
mscVrPpSrseApeOutFrames = _MscVrPpSrseApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 4),
    _MscVrPpSrseApeOutFrames_Type()
)
mscVrPpSrseApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseApeOutFrames.setStatus("mandatory")
_MscVrPpSrseSteInFrames_Type = Counter32
_MscVrPpSrseSteInFrames_Object = MibTableColumn
mscVrPpSrseSteInFrames = _MscVrPpSrseSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 5),
    _MscVrPpSrseSteInFrames_Type()
)
mscVrPpSrseSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseSteInFrames.setStatus("mandatory")
_MscVrPpSrseSteOutFrames_Type = Counter32
_MscVrPpSrseSteOutFrames_Object = MibTableColumn
mscVrPpSrseSteOutFrames = _MscVrPpSrseSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 6),
    _MscVrPpSrseSteOutFrames_Type()
)
mscVrPpSrseSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseSteOutFrames.setStatus("mandatory")
_MscVrPpSrseSegmentMismatchDiscards_Type = Counter32
_MscVrPpSrseSegmentMismatchDiscards_Object = MibTableColumn
mscVrPpSrseSegmentMismatchDiscards = _MscVrPpSrseSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 7),
    _MscVrPpSrseSegmentMismatchDiscards_Type()
)
mscVrPpSrseSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseSegmentMismatchDiscards.setStatus("mandatory")
_MscVrPpSrseDupSegmentDiscards_Type = Counter32
_MscVrPpSrseDupSegmentDiscards_Object = MibTableColumn
mscVrPpSrseDupSegmentDiscards = _MscVrPpSrseDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 8),
    _MscVrPpSrseDupSegmentDiscards_Type()
)
mscVrPpSrseDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDupSegmentDiscards.setStatus("mandatory")
_MscVrPpSrseHopCountExceededDiscards_Type = Counter32
_MscVrPpSrseHopCountExceededDiscards_Object = MibTableColumn
mscVrPpSrseHopCountExceededDiscards = _MscVrPpSrseHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 9),
    _MscVrPpSrseHopCountExceededDiscards_Type()
)
mscVrPpSrseHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseHopCountExceededDiscards.setStatus("mandatory")
_MscVrPpSrseDupLanIdOrTreeErrors_Type = Counter32
_MscVrPpSrseDupLanIdOrTreeErrors_Object = MibTableColumn
mscVrPpSrseDupLanIdOrTreeErrors = _MscVrPpSrseDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 10),
    _MscVrPpSrseDupLanIdOrTreeErrors_Type()
)
mscVrPpSrseDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDupLanIdOrTreeErrors.setStatus("mandatory")
_MscVrPpSrseLanIdMismatches_Type = Counter32
_MscVrPpSrseLanIdMismatches_Object = MibTableColumn
mscVrPpSrseLanIdMismatches = _MscVrPpSrseLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 11),
    _MscVrPpSrseLanIdMismatches_Type()
)
mscVrPpSrseLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseLanIdMismatches.setStatus("mandatory")
_MscVrPpSrseStaticDiscards_Type = Counter32
_MscVrPpSrseStaticDiscards_Object = MibTableColumn
mscVrPpSrseStaticDiscards = _MscVrPpSrseStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 12),
    _MscVrPpSrseStaticDiscards_Type()
)
mscVrPpSrseStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseStaticDiscards.setStatus("mandatory")
_MscVrPpSrseDynamicDiscards_Type = Counter32
_MscVrPpSrseDynamicDiscards_Object = MibTableColumn
mscVrPpSrseDynamicDiscards = _MscVrPpSrseDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 10, 21, 1, 13),
    _MscVrPpSrseDynamicDiscards_Type()
)
mscVrPpSrseDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrseDynamicDiscards.setStatus("mandatory")
_MscVrPpTbse_ObjectIdentity = ObjectIdentity
mscVrPpTbse = _MscVrPpTbse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11)
)
_MscVrPpTbseRowStatusTable_Object = MibTable
mscVrPpTbseRowStatusTable = _MscVrPpTbseRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 1)
)
if mibBuilder.loadTexts:
    mscVrPpTbseRowStatusTable.setStatus("mandatory")
_MscVrPpTbseRowStatusEntry_Object = MibTableRow
mscVrPpTbseRowStatusEntry = _MscVrPpTbseRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 1, 1)
)
mscVrPpTbseRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseRowStatusEntry.setStatus("mandatory")
_MscVrPpTbseRowStatus_Type = RowStatus
_MscVrPpTbseRowStatus_Object = MibTableColumn
mscVrPpTbseRowStatus = _MscVrPpTbseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 1, 1, 1),
    _MscVrPpTbseRowStatus_Type()
)
mscVrPpTbseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseRowStatus.setStatus("mandatory")
_MscVrPpTbseComponentName_Type = DisplayString
_MscVrPpTbseComponentName_Object = MibTableColumn
mscVrPpTbseComponentName = _MscVrPpTbseComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 1, 1, 2),
    _MscVrPpTbseComponentName_Type()
)
mscVrPpTbseComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseComponentName.setStatus("mandatory")
_MscVrPpTbseStorageType_Type = StorageType
_MscVrPpTbseStorageType_Object = MibTableColumn
mscVrPpTbseStorageType = _MscVrPpTbseStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 1, 1, 4),
    _MscVrPpTbseStorageType_Type()
)
mscVrPpTbseStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseStorageType.setStatus("mandatory")
_MscVrPpTbseIndex_Type = NonReplicated
_MscVrPpTbseIndex_Object = MibTableColumn
mscVrPpTbseIndex = _MscVrPpTbseIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 1, 1, 10),
    _MscVrPpTbseIndex_Type()
)
mscVrPpTbseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpTbseIndex.setStatus("mandatory")
_MscVrPpTbseProvTable_Object = MibTable
mscVrPpTbseProvTable = _MscVrPpTbseProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10)
)
if mibBuilder.loadTexts:
    mscVrPpTbseProvTable.setStatus("mandatory")
_MscVrPpTbseProvEntry_Object = MibTableRow
mscVrPpTbseProvEntry = _MscVrPpTbseProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10, 1)
)
mscVrPpTbseProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseProvEntry.setStatus("mandatory")


class _MscVrPpTbseTranslateIpx_Type(Integer32):
    """Custom type mscVrPpTbseTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpTbseTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpTbseTranslateIpx_Object = MibTableColumn
mscVrPpTbseTranslateIpx = _MscVrPpTbseTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10, 1, 1),
    _MscVrPpTbseTranslateIpx_Type()
)
mscVrPpTbseTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseTranslateIpx.setStatus("mandatory")


class _MscVrPpTbseFragmentIp_Type(Integer32):
    """Custom type mscVrPpTbseFragmentIp based on Integer32"""
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


_MscVrPpTbseFragmentIp_Type.__name__ = "Integer32"
_MscVrPpTbseFragmentIp_Object = MibTableColumn
mscVrPpTbseFragmentIp = _MscVrPpTbseFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10, 1, 2),
    _MscVrPpTbseFragmentIp_Type()
)
mscVrPpTbseFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseFragmentIp.setStatus("mandatory")


class _MscVrPpTbseServiceClass_Type(Integer32):
    """Custom type mscVrPpTbseServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpTbseServiceClass_Type.__name__ = "Integer32"
_MscVrPpTbseServiceClass_Object = MibTableColumn
mscVrPpTbseServiceClass = _MscVrPpTbseServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10, 1, 3),
    _MscVrPpTbseServiceClass_Type()
)
mscVrPpTbseServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseServiceClass.setStatus("mandatory")


class _MscVrPpTbseConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpTbseConvertArpMacAddress based on Integer32"""
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


_MscVrPpTbseConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpTbseConvertArpMacAddress_Object = MibTableColumn
mscVrPpTbseConvertArpMacAddress = _MscVrPpTbseConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10, 1, 4),
    _MscVrPpTbseConvertArpMacAddress_Type()
)
mscVrPpTbseConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpTbsePortNum_Type(Unsigned32):
    """Custom type mscVrPpTbsePortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpTbsePortNum_Type.__name__ = "Unsigned32"
_MscVrPpTbsePortNum_Object = MibTableColumn
mscVrPpTbsePortNum = _MscVrPpTbsePortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 10, 1, 5),
    _MscVrPpTbsePortNum_Type()
)
mscVrPpTbsePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsePortNum.setStatus("mandatory")
_MscVrPpTbseTbProvTable_Object = MibTable
mscVrPpTbseTbProvTable = _MscVrPpTbseTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 11)
)
if mibBuilder.loadTexts:
    mscVrPpTbseTbProvTable.setStatus("mandatory")
_MscVrPpTbseTbProvEntry_Object = MibTableRow
mscVrPpTbseTbProvEntry = _MscVrPpTbseTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 11, 1)
)
mscVrPpTbseTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseTbProvEntry.setStatus("mandatory")


class _MscVrPpTbseSecureOption_Type(Integer32):
    """Custom type mscVrPpTbseSecureOption based on Integer32"""
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


_MscVrPpTbseSecureOption_Type.__name__ = "Integer32"
_MscVrPpTbseSecureOption_Object = MibTableColumn
mscVrPpTbseSecureOption = _MscVrPpTbseSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 11, 1, 1),
    _MscVrPpTbseSecureOption_Type()
)
mscVrPpTbseSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseSecureOption.setStatus("mandatory")
_MscVrPpTbseStpProvTable_Object = MibTable
mscVrPpTbseStpProvTable = _MscVrPpTbseStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12)
)
if mibBuilder.loadTexts:
    mscVrPpTbseStpProvTable.setStatus("mandatory")
_MscVrPpTbseStpProvEntry_Object = MibTableRow
mscVrPpTbseStpProvEntry = _MscVrPpTbseStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1)
)
mscVrPpTbseStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseStpProvEntry.setStatus("mandatory")


class _MscVrPpTbseAdminStatus_Type(Integer32):
    """Custom type mscVrPpTbseAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpTbseAdminStatus_Type.__name__ = "Integer32"
_MscVrPpTbseAdminStatus_Object = MibTableColumn
mscVrPpTbseAdminStatus = _MscVrPpTbseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1, 1),
    _MscVrPpTbseAdminStatus_Type()
)
mscVrPpTbseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseAdminStatus.setStatus("mandatory")


class _MscVrPpTbsePortStateStpControl_Type(Integer32):
    """Custom type mscVrPpTbsePortStateStpControl based on Integer32"""
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


_MscVrPpTbsePortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpTbsePortStateStpControl_Object = MibTableColumn
mscVrPpTbsePortStateStpControl = _MscVrPpTbsePortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1, 2),
    _MscVrPpTbsePortStateStpControl_Type()
)
mscVrPpTbsePortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsePortStateStpControl.setStatus("mandatory")


class _MscVrPpTbseStpTypeProv_Type(Integer32):
    """Custom type mscVrPpTbseStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpTbseStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpTbseStpTypeProv_Object = MibTableColumn
mscVrPpTbseStpTypeProv = _MscVrPpTbseStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1, 3),
    _MscVrPpTbseStpTypeProv_Type()
)
mscVrPpTbseStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseStpTypeProv.setStatus("mandatory")


class _MscVrPpTbsePortPriority_Type(Unsigned32):
    """Custom type mscVrPpTbsePortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbsePortPriority_Type.__name__ = "Unsigned32"
_MscVrPpTbsePortPriority_Object = MibTableColumn
mscVrPpTbsePortPriority = _MscVrPpTbsePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1, 4),
    _MscVrPpTbsePortPriority_Type()
)
mscVrPpTbsePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsePortPriority.setStatus("mandatory")


class _MscVrPpTbsePathCost_Type(Unsigned32):
    """Custom type mscVrPpTbsePathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbsePathCost_Type.__name__ = "Unsigned32"
_MscVrPpTbsePathCost_Object = MibTableColumn
mscVrPpTbsePathCost = _MscVrPpTbsePathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1, 5),
    _MscVrPpTbsePathCost_Type()
)
mscVrPpTbsePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsePathCost.setStatus("mandatory")


class _MscVrPpTbsePathCostMethod_Type(Integer32):
    """Custom type mscVrPpTbsePathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpTbsePathCostMethod_Type.__name__ = "Integer32"
_MscVrPpTbsePathCostMethod_Object = MibTableColumn
mscVrPpTbsePathCostMethod = _MscVrPpTbsePathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 12, 1, 6),
    _MscVrPpTbsePathCostMethod_Type()
)
mscVrPpTbsePathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsePathCostMethod.setStatus("mandatory")
_MscVrPpTbseDIProvTable_Object = MibTable
mscVrPpTbseDIProvTable = _MscVrPpTbseDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 13)
)
if mibBuilder.loadTexts:
    mscVrPpTbseDIProvTable.setStatus("mandatory")
_MscVrPpTbseDIProvEntry_Object = MibTableRow
mscVrPpTbseDIProvEntry = _MscVrPpTbseDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 13, 1)
)
mscVrPpTbseDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseDIProvEntry.setStatus("mandatory")


class _MscVrPpTbseDomainNum_Type(Unsigned32):
    """Custom type mscVrPpTbseDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpTbseDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpTbseDomainNum_Object = MibTableColumn
mscVrPpTbseDomainNum = _MscVrPpTbseDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 13, 1, 1),
    _MscVrPpTbseDomainNum_Type()
)
mscVrPpTbseDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbseDomainNum.setStatus("mandatory")


class _MscVrPpTbsePreserveDomain_Type(Integer32):
    """Custom type mscVrPpTbsePreserveDomain based on Integer32"""
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


_MscVrPpTbsePreserveDomain_Type.__name__ = "Integer32"
_MscVrPpTbsePreserveDomain_Object = MibTableColumn
mscVrPpTbsePreserveDomain = _MscVrPpTbsePreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 13, 1, 2),
    _MscVrPpTbsePreserveDomain_Type()
)
mscVrPpTbsePreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsePreserveDomain.setStatus("mandatory")
_MscVrPpTbseStateTable_Object = MibTable
mscVrPpTbseStateTable = _MscVrPpTbseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 14)
)
if mibBuilder.loadTexts:
    mscVrPpTbseStateTable.setStatus("mandatory")
_MscVrPpTbseStateEntry_Object = MibTableRow
mscVrPpTbseStateEntry = _MscVrPpTbseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 14, 1)
)
mscVrPpTbseStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseStateEntry.setStatus("mandatory")


class _MscVrPpTbseAdminState_Type(Integer32):
    """Custom type mscVrPpTbseAdminState based on Integer32"""
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


_MscVrPpTbseAdminState_Type.__name__ = "Integer32"
_MscVrPpTbseAdminState_Object = MibTableColumn
mscVrPpTbseAdminState = _MscVrPpTbseAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 14, 1, 1),
    _MscVrPpTbseAdminState_Type()
)
mscVrPpTbseAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseAdminState.setStatus("mandatory")


class _MscVrPpTbseOperationalState_Type(Integer32):
    """Custom type mscVrPpTbseOperationalState based on Integer32"""
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


_MscVrPpTbseOperationalState_Type.__name__ = "Integer32"
_MscVrPpTbseOperationalState_Object = MibTableColumn
mscVrPpTbseOperationalState = _MscVrPpTbseOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 14, 1, 2),
    _MscVrPpTbseOperationalState_Type()
)
mscVrPpTbseOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseOperationalState.setStatus("mandatory")


class _MscVrPpTbseUsageState_Type(Integer32):
    """Custom type mscVrPpTbseUsageState based on Integer32"""
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


_MscVrPpTbseUsageState_Type.__name__ = "Integer32"
_MscVrPpTbseUsageState_Object = MibTableColumn
mscVrPpTbseUsageState = _MscVrPpTbseUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 14, 1, 3),
    _MscVrPpTbseUsageState_Type()
)
mscVrPpTbseUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseUsageState.setStatus("mandatory")
_MscVrPpTbseOperStatusTable_Object = MibTable
mscVrPpTbseOperStatusTable = _MscVrPpTbseOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 15)
)
if mibBuilder.loadTexts:
    mscVrPpTbseOperStatusTable.setStatus("mandatory")
_MscVrPpTbseOperStatusEntry_Object = MibTableRow
mscVrPpTbseOperStatusEntry = _MscVrPpTbseOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 15, 1)
)
mscVrPpTbseOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseOperStatusEntry.setStatus("mandatory")


class _MscVrPpTbseSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpTbseSnmpOperStatus based on Integer32"""
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


_MscVrPpTbseSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpTbseSnmpOperStatus_Object = MibTableColumn
mscVrPpTbseSnmpOperStatus = _MscVrPpTbseSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 15, 1, 1),
    _MscVrPpTbseSnmpOperStatus_Type()
)
mscVrPpTbseSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseSnmpOperStatus.setStatus("mandatory")
_MscVrPpTbseOperTable_Object = MibTable
mscVrPpTbseOperTable = _MscVrPpTbseOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16)
)
if mibBuilder.loadTexts:
    mscVrPpTbseOperTable.setStatus("mandatory")
_MscVrPpTbseOperEntry_Object = MibTableRow
mscVrPpTbseOperEntry = _MscVrPpTbseOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1)
)
mscVrPpTbseOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseOperEntry.setStatus("mandatory")


class _MscVrPpTbsePortName_Type(AsciiString):
    """Custom type mscVrPpTbsePortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpTbsePortName_Type.__name__ = "AsciiString"
_MscVrPpTbsePortName_Object = MibTableColumn
mscVrPpTbsePortName = _MscVrPpTbsePortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 1),
    _MscVrPpTbsePortName_Type()
)
mscVrPpTbsePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsePortName.setStatus("mandatory")


class _MscVrPpTbseUpTime_Type(Unsigned32):
    """Custom type mscVrPpTbseUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbseUpTime_Type.__name__ = "Unsigned32"
_MscVrPpTbseUpTime_Object = MibTableColumn
mscVrPpTbseUpTime = _MscVrPpTbseUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 3),
    _MscVrPpTbseUpTime_Type()
)
mscVrPpTbseUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseUpTime.setStatus("mandatory")


class _MscVrPpTbseDownTime_Type(Unsigned32):
    """Custom type mscVrPpTbseDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbseDownTime_Type.__name__ = "Unsigned32"
_MscVrPpTbseDownTime_Object = MibTableColumn
mscVrPpTbseDownTime = _MscVrPpTbseDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 4),
    _MscVrPpTbseDownTime_Type()
)
mscVrPpTbseDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDownTime.setStatus("mandatory")


class _MscVrPpTbseBridgingMode_Type(Integer32):
    """Custom type mscVrPpTbseBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpTbseBridgingMode_Type.__name__ = "Integer32"
_MscVrPpTbseBridgingMode_Object = MibTableColumn
mscVrPpTbseBridgingMode = _MscVrPpTbseBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 5),
    _MscVrPpTbseBridgingMode_Type()
)
mscVrPpTbseBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseBridgingMode.setStatus("mandatory")


class _MscVrPpTbseBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpTbseBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpTbseBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpTbseBridgePortConfig_Object = MibTableColumn
mscVrPpTbseBridgePortConfig = _MscVrPpTbseBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 6),
    _MscVrPpTbseBridgePortConfig_Type()
)
mscVrPpTbseBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseBridgePortConfig.setStatus("mandatory")


class _MscVrPpTbseBridgePortType_Type(Integer32):
    """Custom type mscVrPpTbseBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpTbseBridgePortType_Type.__name__ = "Integer32"
_MscVrPpTbseBridgePortType_Object = MibTableColumn
mscVrPpTbseBridgePortType = _MscVrPpTbseBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 7),
    _MscVrPpTbseBridgePortType_Type()
)
mscVrPpTbseBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseBridgePortType.setStatus("mandatory")


class _MscVrPpTbseIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpTbseIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbseIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpTbseIfIndex_Object = MibTableColumn
mscVrPpTbseIfIndex = _MscVrPpTbseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 8),
    _MscVrPpTbseIfIndex_Type()
)
mscVrPpTbseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseIfIndex.setStatus("mandatory")
_MscVrPpTbseDelayExceededDiscards_Type = Counter32
_MscVrPpTbseDelayExceededDiscards_Object = MibTableColumn
mscVrPpTbseDelayExceededDiscards = _MscVrPpTbseDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 10),
    _MscVrPpTbseDelayExceededDiscards_Type()
)
mscVrPpTbseDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDelayExceededDiscards.setStatus("mandatory")
_MscVrPpTbseMtuExceededDiscards_Type = Counter32
_MscVrPpTbseMtuExceededDiscards_Object = MibTableColumn
mscVrPpTbseMtuExceededDiscards = _MscVrPpTbseMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 16, 1, 11),
    _MscVrPpTbseMtuExceededDiscards_Type()
)
mscVrPpTbseMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseMtuExceededDiscards.setStatus("mandatory")
_MscVrPpTbseTbOperTable_Object = MibTable
mscVrPpTbseTbOperTable = _MscVrPpTbseTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17)
)
if mibBuilder.loadTexts:
    mscVrPpTbseTbOperTable.setStatus("mandatory")
_MscVrPpTbseTbOperEntry_Object = MibTableRow
mscVrPpTbseTbOperEntry = _MscVrPpTbseTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1)
)
mscVrPpTbseTbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseTbOperEntry.setStatus("mandatory")


class _MscVrPpTbseMaxInfo_Type(Unsigned32):
    """Custom type mscVrPpTbseMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbseMaxInfo_Type.__name__ = "Unsigned32"
_MscVrPpTbseMaxInfo_Object = MibTableColumn
mscVrPpTbseMaxInfo = _MscVrPpTbseMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 2),
    _MscVrPpTbseMaxInfo_Type()
)
mscVrPpTbseMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseMaxInfo.setStatus("mandatory")
_MscVrPpTbseBadVerifyDiscards_Type = Counter32
_MscVrPpTbseBadVerifyDiscards_Object = MibTableColumn
mscVrPpTbseBadVerifyDiscards = _MscVrPpTbseBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 3),
    _MscVrPpTbseBadVerifyDiscards_Type()
)
mscVrPpTbseBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseBadVerifyDiscards.setStatus("mandatory")
_MscVrPpTbseUnicastNoMatches_Type = Counter32
_MscVrPpTbseUnicastNoMatches_Object = MibTableColumn
mscVrPpTbseUnicastNoMatches = _MscVrPpTbseUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 4),
    _MscVrPpTbseUnicastNoMatches_Type()
)
mscVrPpTbseUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseUnicastNoMatches.setStatus("mandatory")
_MscVrPpTbseStaticEntryDiscards_Type = Counter32
_MscVrPpTbseStaticEntryDiscards_Object = MibTableColumn
mscVrPpTbseStaticEntryDiscards = _MscVrPpTbseStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 5),
    _MscVrPpTbseStaticEntryDiscards_Type()
)
mscVrPpTbseStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseStaticEntryDiscards.setStatus("mandatory")
_MscVrPpTbseDynamicEntryDiscards_Type = Counter32
_MscVrPpTbseDynamicEntryDiscards_Object = MibTableColumn
mscVrPpTbseDynamicEntryDiscards = _MscVrPpTbseDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 6),
    _MscVrPpTbseDynamicEntryDiscards_Type()
)
mscVrPpTbseDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDynamicEntryDiscards.setStatus("mandatory")
_MscVrPpTbseLearningDiscards_Type = Counter32
_MscVrPpTbseLearningDiscards_Object = MibTableColumn
mscVrPpTbseLearningDiscards = _MscVrPpTbseLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 7),
    _MscVrPpTbseLearningDiscards_Type()
)
mscVrPpTbseLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseLearningDiscards.setStatus("mandatory")
_MscVrPpTbseInDiscards_Type = Counter32
_MscVrPpTbseInDiscards_Object = MibTableColumn
mscVrPpTbseInDiscards = _MscVrPpTbseInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 8),
    _MscVrPpTbseInDiscards_Type()
)
mscVrPpTbseInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseInDiscards.setStatus("mandatory")
_MscVrPpTbseInFrames_Type = Counter32
_MscVrPpTbseInFrames_Object = MibTableColumn
mscVrPpTbseInFrames = _MscVrPpTbseInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 9),
    _MscVrPpTbseInFrames_Type()
)
mscVrPpTbseInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseInFrames.setStatus("mandatory")
_MscVrPpTbseOutFrames_Type = Counter32
_MscVrPpTbseOutFrames_Object = MibTableColumn
mscVrPpTbseOutFrames = _MscVrPpTbseOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 17, 1, 10),
    _MscVrPpTbseOutFrames_Type()
)
mscVrPpTbseOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseOutFrames.setStatus("mandatory")
_MscVrPpTbseStpOperTable_Object = MibTable
mscVrPpTbseStpOperTable = _MscVrPpTbseStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18)
)
if mibBuilder.loadTexts:
    mscVrPpTbseStpOperTable.setStatus("mandatory")
_MscVrPpTbseStpOperEntry_Object = MibTableRow
mscVrPpTbseStpOperEntry = _MscVrPpTbseStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1)
)
mscVrPpTbseStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseStpOperEntry.setStatus("mandatory")


class _MscVrPpTbseStpPortState_Type(Integer32):
    """Custom type mscVrPpTbseStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpTbseStpPortState_Type.__name__ = "Integer32"
_MscVrPpTbseStpPortState_Object = MibTableColumn
mscVrPpTbseStpPortState = _MscVrPpTbseStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 2),
    _MscVrPpTbseStpPortState_Type()
)
mscVrPpTbseStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseStpPortState.setStatus("mandatory")


class _MscVrPpTbseStpTypeOper_Type(Integer32):
    """Custom type mscVrPpTbseStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpTbseStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpTbseStpTypeOper_Object = MibTableColumn
mscVrPpTbseStpTypeOper = _MscVrPpTbseStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 3),
    _MscVrPpTbseStpTypeOper_Type()
)
mscVrPpTbseStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseStpTypeOper.setStatus("mandatory")


class _MscVrPpTbseDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpTbseDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbseDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpTbseDesignatedCost_Object = MibTableColumn
mscVrPpTbseDesignatedCost = _MscVrPpTbseDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 4),
    _MscVrPpTbseDesignatedCost_Type()
)
mscVrPpTbseDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDesignatedCost.setStatus("mandatory")


class _MscVrPpTbsePathCostOper_Type(Unsigned32):
    """Custom type mscVrPpTbsePathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbsePathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpTbsePathCostOper_Object = MibTableColumn
mscVrPpTbsePathCostOper = _MscVrPpTbsePathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 5),
    _MscVrPpTbsePathCostOper_Type()
)
mscVrPpTbsePathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsePathCostOper.setStatus("mandatory")


class _MscVrPpTbseDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpTbseDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbseDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpTbseDesignatedBridge_Object = MibTableColumn
mscVrPpTbseDesignatedBridge = _MscVrPpTbseDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 6),
    _MscVrPpTbseDesignatedBridge_Type()
)
mscVrPpTbseDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDesignatedBridge.setStatus("mandatory")


class _MscVrPpTbseDesignatedPort_Type(Hex):
    """Custom type mscVrPpTbseDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbseDesignatedPort_Type.__name__ = "Hex"
_MscVrPpTbseDesignatedPort_Object = MibTableColumn
mscVrPpTbseDesignatedPort = _MscVrPpTbseDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 7),
    _MscVrPpTbseDesignatedPort_Type()
)
mscVrPpTbseDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDesignatedPort.setStatus("mandatory")
_MscVrPpTbseForwardTransitions_Type = Counter32
_MscVrPpTbseForwardTransitions_Object = MibTableColumn
mscVrPpTbseForwardTransitions = _MscVrPpTbseForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 8),
    _MscVrPpTbseForwardTransitions_Type()
)
mscVrPpTbseForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseForwardTransitions.setStatus("mandatory")
_MscVrPpTbseBlockingDiscards_Type = Counter32
_MscVrPpTbseBlockingDiscards_Object = MibTableColumn
mscVrPpTbseBlockingDiscards = _MscVrPpTbseBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 9),
    _MscVrPpTbseBlockingDiscards_Type()
)
mscVrPpTbseBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseBlockingDiscards.setStatus("mandatory")


class _MscVrPpTbseDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpTbseDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbseDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpTbseDesignatedRoot_Object = MibTableColumn
mscVrPpTbseDesignatedRoot = _MscVrPpTbseDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 18, 1, 10),
    _MscVrPpTbseDesignatedRoot_Type()
)
mscVrPpTbseDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseDesignatedRoot.setStatus("mandatory")
_MscVrPpTbseStatsTable_Object = MibTable
mscVrPpTbseStatsTable = _MscVrPpTbseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19)
)
if mibBuilder.loadTexts:
    mscVrPpTbseStatsTable.setStatus("mandatory")
_MscVrPpTbseStatsEntry_Object = MibTableRow
mscVrPpTbseStatsEntry = _MscVrPpTbseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19, 1)
)
mscVrPpTbseStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbseStatsEntry.setStatus("mandatory")
_MscVrPpTbseBadAbstractDiscards_Type = Counter32
_MscVrPpTbseBadAbstractDiscards_Object = MibTableColumn
mscVrPpTbseBadAbstractDiscards = _MscVrPpTbseBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19, 1, 1),
    _MscVrPpTbseBadAbstractDiscards_Type()
)
mscVrPpTbseBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseBadAbstractDiscards.setStatus("mandatory")
_MscVrPpTbseTinygramFramesIn_Type = Counter32
_MscVrPpTbseTinygramFramesIn_Object = MibTableColumn
mscVrPpTbseTinygramFramesIn = _MscVrPpTbseTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19, 1, 2),
    _MscVrPpTbseTinygramFramesIn_Type()
)
mscVrPpTbseTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseTinygramFramesIn.setStatus("mandatory")
_MscVrPpTbseTinygramFramesOut_Type = Counter32
_MscVrPpTbseTinygramFramesOut_Object = MibTableColumn
mscVrPpTbseTinygramFramesOut = _MscVrPpTbseTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19, 1, 3),
    _MscVrPpTbseTinygramFramesOut_Type()
)
mscVrPpTbseTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseTinygramFramesOut.setStatus("mandatory")
_MscVrPpTbseInFilterDiscards_Type = Counter32
_MscVrPpTbseInFilterDiscards_Object = MibTableColumn
mscVrPpTbseInFilterDiscards = _MscVrPpTbseInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19, 1, 4),
    _MscVrPpTbseInFilterDiscards_Type()
)
mscVrPpTbseInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseInFilterDiscards.setStatus("mandatory")
_MscVrPpTbseOutFilterDiscards_Type = Counter32
_MscVrPpTbseOutFilterDiscards_Object = MibTableColumn
mscVrPpTbseOutFilterDiscards = _MscVrPpTbseOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 11, 19, 1, 5),
    _MscVrPpTbseOutFilterDiscards_Type()
)
mscVrPpTbseOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbseOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrsg_ObjectIdentity = ObjectIdentity
mscVrPpSrsg = _MscVrPpSrsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12)
)
_MscVrPpSrsgRowStatusTable_Object = MibTable
mscVrPpSrsgRowStatusTable = _MscVrPpSrsgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgRowStatusTable.setStatus("mandatory")
_MscVrPpSrsgRowStatusEntry_Object = MibTableRow
mscVrPpSrsgRowStatusEntry = _MscVrPpSrsgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 1, 1)
)
mscVrPpSrsgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgRowStatusEntry.setStatus("mandatory")
_MscVrPpSrsgRowStatus_Type = RowStatus
_MscVrPpSrsgRowStatus_Object = MibTableColumn
mscVrPpSrsgRowStatus = _MscVrPpSrsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 1, 1, 1),
    _MscVrPpSrsgRowStatus_Type()
)
mscVrPpSrsgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgRowStatus.setStatus("mandatory")
_MscVrPpSrsgComponentName_Type = DisplayString
_MscVrPpSrsgComponentName_Object = MibTableColumn
mscVrPpSrsgComponentName = _MscVrPpSrsgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 1, 1, 2),
    _MscVrPpSrsgComponentName_Type()
)
mscVrPpSrsgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgComponentName.setStatus("mandatory")
_MscVrPpSrsgStorageType_Type = StorageType
_MscVrPpSrsgStorageType_Object = MibTableColumn
mscVrPpSrsgStorageType = _MscVrPpSrsgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 1, 1, 4),
    _MscVrPpSrsgStorageType_Type()
)
mscVrPpSrsgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgStorageType.setStatus("mandatory")
_MscVrPpSrsgIndex_Type = NonReplicated
_MscVrPpSrsgIndex_Object = MibTableColumn
mscVrPpSrsgIndex = _MscVrPpSrsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 1, 1, 10),
    _MscVrPpSrsgIndex_Type()
)
mscVrPpSrsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrsgIndex.setStatus("mandatory")
_MscVrPpSrsgProvTable_Object = MibTable
mscVrPpSrsgProvTable = _MscVrPpSrsgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgProvTable.setStatus("mandatory")
_MscVrPpSrsgProvEntry_Object = MibTableRow
mscVrPpSrsgProvEntry = _MscVrPpSrsgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10, 1)
)
mscVrPpSrsgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgProvEntry.setStatus("mandatory")


class _MscVrPpSrsgTranslateIpx_Type(Integer32):
    """Custom type mscVrPpSrsgTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpSrsgTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpSrsgTranslateIpx_Object = MibTableColumn
mscVrPpSrsgTranslateIpx = _MscVrPpSrsgTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10, 1, 1),
    _MscVrPpSrsgTranslateIpx_Type()
)
mscVrPpSrsgTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgTranslateIpx.setStatus("mandatory")


class _MscVrPpSrsgFragmentIp_Type(Integer32):
    """Custom type mscVrPpSrsgFragmentIp based on Integer32"""
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


_MscVrPpSrsgFragmentIp_Type.__name__ = "Integer32"
_MscVrPpSrsgFragmentIp_Object = MibTableColumn
mscVrPpSrsgFragmentIp = _MscVrPpSrsgFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10, 1, 2),
    _MscVrPpSrsgFragmentIp_Type()
)
mscVrPpSrsgFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgFragmentIp.setStatus("mandatory")


class _MscVrPpSrsgServiceClass_Type(Integer32):
    """Custom type mscVrPpSrsgServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpSrsgServiceClass_Type.__name__ = "Integer32"
_MscVrPpSrsgServiceClass_Object = MibTableColumn
mscVrPpSrsgServiceClass = _MscVrPpSrsgServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10, 1, 3),
    _MscVrPpSrsgServiceClass_Type()
)
mscVrPpSrsgServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgServiceClass.setStatus("mandatory")


class _MscVrPpSrsgConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpSrsgConvertArpMacAddress based on Integer32"""
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


_MscVrPpSrsgConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpSrsgConvertArpMacAddress_Object = MibTableColumn
mscVrPpSrsgConvertArpMacAddress = _MscVrPpSrsgConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10, 1, 4),
    _MscVrPpSrsgConvertArpMacAddress_Type()
)
mscVrPpSrsgConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpSrsgPortNum_Type(Unsigned32):
    """Custom type mscVrPpSrsgPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpSrsgPortNum_Type.__name__ = "Unsigned32"
_MscVrPpSrsgPortNum_Object = MibTableColumn
mscVrPpSrsgPortNum = _MscVrPpSrsgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 10, 1, 5),
    _MscVrPpSrsgPortNum_Type()
)
mscVrPpSrsgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgPortNum.setStatus("mandatory")
_MscVrPpSrsgStpProvTable_Object = MibTable
mscVrPpSrsgStpProvTable = _MscVrPpSrsgStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStpProvTable.setStatus("mandatory")
_MscVrPpSrsgStpProvEntry_Object = MibTableRow
mscVrPpSrsgStpProvEntry = _MscVrPpSrsgStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1)
)
mscVrPpSrsgStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStpProvEntry.setStatus("mandatory")


class _MscVrPpSrsgAdminStatus_Type(Integer32):
    """Custom type mscVrPpSrsgAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpSrsgAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSrsgAdminStatus_Object = MibTableColumn
mscVrPpSrsgAdminStatus = _MscVrPpSrsgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1, 1),
    _MscVrPpSrsgAdminStatus_Type()
)
mscVrPpSrsgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgAdminStatus.setStatus("mandatory")


class _MscVrPpSrsgPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpSrsgPortStateStpControl based on Integer32"""
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


_MscVrPpSrsgPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpSrsgPortStateStpControl_Object = MibTableColumn
mscVrPpSrsgPortStateStpControl = _MscVrPpSrsgPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1, 2),
    _MscVrPpSrsgPortStateStpControl_Type()
)
mscVrPpSrsgPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgPortStateStpControl.setStatus("mandatory")


class _MscVrPpSrsgStpTypeProv_Type(Integer32):
    """Custom type mscVrPpSrsgStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpSrsgStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpSrsgStpTypeProv_Object = MibTableColumn
mscVrPpSrsgStpTypeProv = _MscVrPpSrsgStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1, 3),
    _MscVrPpSrsgStpTypeProv_Type()
)
mscVrPpSrsgStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgStpTypeProv.setStatus("mandatory")


class _MscVrPpSrsgPortPriority_Type(Unsigned32):
    """Custom type mscVrPpSrsgPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrsgPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpSrsgPortPriority_Object = MibTableColumn
mscVrPpSrsgPortPriority = _MscVrPpSrsgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1, 4),
    _MscVrPpSrsgPortPriority_Type()
)
mscVrPpSrsgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgPortPriority.setStatus("mandatory")


class _MscVrPpSrsgPathCost_Type(Unsigned32):
    """Custom type mscVrPpSrsgPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrsgPathCost_Type.__name__ = "Unsigned32"
_MscVrPpSrsgPathCost_Object = MibTableColumn
mscVrPpSrsgPathCost = _MscVrPpSrsgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1, 5),
    _MscVrPpSrsgPathCost_Type()
)
mscVrPpSrsgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgPathCost.setStatus("mandatory")


class _MscVrPpSrsgPathCostMethod_Type(Integer32):
    """Custom type mscVrPpSrsgPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpSrsgPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpSrsgPathCostMethod_Object = MibTableColumn
mscVrPpSrsgPathCostMethod = _MscVrPpSrsgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 12, 1, 6),
    _MscVrPpSrsgPathCostMethod_Type()
)
mscVrPpSrsgPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgPathCostMethod.setStatus("mandatory")
_MscVrPpSrsgDIProvTable_Object = MibTable
mscVrPpSrsgDIProvTable = _MscVrPpSrsgDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 13)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgDIProvTable.setStatus("mandatory")
_MscVrPpSrsgDIProvEntry_Object = MibTableRow
mscVrPpSrsgDIProvEntry = _MscVrPpSrsgDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 13, 1)
)
mscVrPpSrsgDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgDIProvEntry.setStatus("mandatory")


class _MscVrPpSrsgDomainNum_Type(Unsigned32):
    """Custom type mscVrPpSrsgDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpSrsgDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpSrsgDomainNum_Object = MibTableColumn
mscVrPpSrsgDomainNum = _MscVrPpSrsgDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 13, 1, 1),
    _MscVrPpSrsgDomainNum_Type()
)
mscVrPpSrsgDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgDomainNum.setStatus("mandatory")


class _MscVrPpSrsgPreserveDomain_Type(Integer32):
    """Custom type mscVrPpSrsgPreserveDomain based on Integer32"""
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


_MscVrPpSrsgPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpSrsgPreserveDomain_Object = MibTableColumn
mscVrPpSrsgPreserveDomain = _MscVrPpSrsgPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 13, 1, 2),
    _MscVrPpSrsgPreserveDomain_Type()
)
mscVrPpSrsgPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgPreserveDomain.setStatus("mandatory")
_MscVrPpSrsgStateTable_Object = MibTable
mscVrPpSrsgStateTable = _MscVrPpSrsgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 14)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStateTable.setStatus("mandatory")
_MscVrPpSrsgStateEntry_Object = MibTableRow
mscVrPpSrsgStateEntry = _MscVrPpSrsgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 14, 1)
)
mscVrPpSrsgStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStateEntry.setStatus("mandatory")


class _MscVrPpSrsgAdminState_Type(Integer32):
    """Custom type mscVrPpSrsgAdminState based on Integer32"""
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


_MscVrPpSrsgAdminState_Type.__name__ = "Integer32"
_MscVrPpSrsgAdminState_Object = MibTableColumn
mscVrPpSrsgAdminState = _MscVrPpSrsgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 14, 1, 1),
    _MscVrPpSrsgAdminState_Type()
)
mscVrPpSrsgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgAdminState.setStatus("mandatory")


class _MscVrPpSrsgOperationalState_Type(Integer32):
    """Custom type mscVrPpSrsgOperationalState based on Integer32"""
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


_MscVrPpSrsgOperationalState_Type.__name__ = "Integer32"
_MscVrPpSrsgOperationalState_Object = MibTableColumn
mscVrPpSrsgOperationalState = _MscVrPpSrsgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 14, 1, 2),
    _MscVrPpSrsgOperationalState_Type()
)
mscVrPpSrsgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgOperationalState.setStatus("mandatory")


class _MscVrPpSrsgUsageState_Type(Integer32):
    """Custom type mscVrPpSrsgUsageState based on Integer32"""
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


_MscVrPpSrsgUsageState_Type.__name__ = "Integer32"
_MscVrPpSrsgUsageState_Object = MibTableColumn
mscVrPpSrsgUsageState = _MscVrPpSrsgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 14, 1, 3),
    _MscVrPpSrsgUsageState_Type()
)
mscVrPpSrsgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgUsageState.setStatus("mandatory")
_MscVrPpSrsgOperStatusTable_Object = MibTable
mscVrPpSrsgOperStatusTable = _MscVrPpSrsgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 15)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgOperStatusTable.setStatus("mandatory")
_MscVrPpSrsgOperStatusEntry_Object = MibTableRow
mscVrPpSrsgOperStatusEntry = _MscVrPpSrsgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 15, 1)
)
mscVrPpSrsgOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgOperStatusEntry.setStatus("mandatory")


class _MscVrPpSrsgSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSrsgSnmpOperStatus based on Integer32"""
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


_MscVrPpSrsgSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSrsgSnmpOperStatus_Object = MibTableColumn
mscVrPpSrsgSnmpOperStatus = _MscVrPpSrsgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 15, 1, 1),
    _MscVrPpSrsgSnmpOperStatus_Type()
)
mscVrPpSrsgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgSnmpOperStatus.setStatus("mandatory")
_MscVrPpSrsgOperTable_Object = MibTable
mscVrPpSrsgOperTable = _MscVrPpSrsgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgOperTable.setStatus("mandatory")
_MscVrPpSrsgOperEntry_Object = MibTableRow
mscVrPpSrsgOperEntry = _MscVrPpSrsgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1)
)
mscVrPpSrsgOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgOperEntry.setStatus("mandatory")


class _MscVrPpSrsgPortName_Type(AsciiString):
    """Custom type mscVrPpSrsgPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpSrsgPortName_Type.__name__ = "AsciiString"
_MscVrPpSrsgPortName_Object = MibTableColumn
mscVrPpSrsgPortName = _MscVrPpSrsgPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 1),
    _MscVrPpSrsgPortName_Type()
)
mscVrPpSrsgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgPortName.setStatus("mandatory")


class _MscVrPpSrsgUpTime_Type(Unsigned32):
    """Custom type mscVrPpSrsgUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrsgUpTime_Type.__name__ = "Unsigned32"
_MscVrPpSrsgUpTime_Object = MibTableColumn
mscVrPpSrsgUpTime = _MscVrPpSrsgUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 3),
    _MscVrPpSrsgUpTime_Type()
)
mscVrPpSrsgUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgUpTime.setStatus("mandatory")


class _MscVrPpSrsgDownTime_Type(Unsigned32):
    """Custom type mscVrPpSrsgDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrsgDownTime_Type.__name__ = "Unsigned32"
_MscVrPpSrsgDownTime_Object = MibTableColumn
mscVrPpSrsgDownTime = _MscVrPpSrsgDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 4),
    _MscVrPpSrsgDownTime_Type()
)
mscVrPpSrsgDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDownTime.setStatus("mandatory")


class _MscVrPpSrsgBridgingMode_Type(Integer32):
    """Custom type mscVrPpSrsgBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpSrsgBridgingMode_Type.__name__ = "Integer32"
_MscVrPpSrsgBridgingMode_Object = MibTableColumn
mscVrPpSrsgBridgingMode = _MscVrPpSrsgBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 5),
    _MscVrPpSrsgBridgingMode_Type()
)
mscVrPpSrsgBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgBridgingMode.setStatus("mandatory")


class _MscVrPpSrsgBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpSrsgBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpSrsgBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpSrsgBridgePortConfig_Object = MibTableColumn
mscVrPpSrsgBridgePortConfig = _MscVrPpSrsgBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 6),
    _MscVrPpSrsgBridgePortConfig_Type()
)
mscVrPpSrsgBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgBridgePortConfig.setStatus("mandatory")


class _MscVrPpSrsgBridgePortType_Type(Integer32):
    """Custom type mscVrPpSrsgBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpSrsgBridgePortType_Type.__name__ = "Integer32"
_MscVrPpSrsgBridgePortType_Object = MibTableColumn
mscVrPpSrsgBridgePortType = _MscVrPpSrsgBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 7),
    _MscVrPpSrsgBridgePortType_Type()
)
mscVrPpSrsgBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgBridgePortType.setStatus("mandatory")


class _MscVrPpSrsgIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpSrsgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrsgIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpSrsgIfIndex_Object = MibTableColumn
mscVrPpSrsgIfIndex = _MscVrPpSrsgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 8),
    _MscVrPpSrsgIfIndex_Type()
)
mscVrPpSrsgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgIfIndex.setStatus("mandatory")
_MscVrPpSrsgDelayExceededDiscards_Type = Counter32
_MscVrPpSrsgDelayExceededDiscards_Object = MibTableColumn
mscVrPpSrsgDelayExceededDiscards = _MscVrPpSrsgDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 10),
    _MscVrPpSrsgDelayExceededDiscards_Type()
)
mscVrPpSrsgDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDelayExceededDiscards.setStatus("mandatory")
_MscVrPpSrsgMtuExceededDiscards_Type = Counter32
_MscVrPpSrsgMtuExceededDiscards_Object = MibTableColumn
mscVrPpSrsgMtuExceededDiscards = _MscVrPpSrsgMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 16, 1, 11),
    _MscVrPpSrsgMtuExceededDiscards_Type()
)
mscVrPpSrsgMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgMtuExceededDiscards.setStatus("mandatory")
_MscVrPpSrsgStpOperTable_Object = MibTable
mscVrPpSrsgStpOperTable = _MscVrPpSrsgStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStpOperTable.setStatus("mandatory")
_MscVrPpSrsgStpOperEntry_Object = MibTableRow
mscVrPpSrsgStpOperEntry = _MscVrPpSrsgStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1)
)
mscVrPpSrsgStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStpOperEntry.setStatus("mandatory")


class _MscVrPpSrsgStpPortState_Type(Integer32):
    """Custom type mscVrPpSrsgStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpSrsgStpPortState_Type.__name__ = "Integer32"
_MscVrPpSrsgStpPortState_Object = MibTableColumn
mscVrPpSrsgStpPortState = _MscVrPpSrsgStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 2),
    _MscVrPpSrsgStpPortState_Type()
)
mscVrPpSrsgStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgStpPortState.setStatus("mandatory")


class _MscVrPpSrsgStpTypeOper_Type(Integer32):
    """Custom type mscVrPpSrsgStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpSrsgStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpSrsgStpTypeOper_Object = MibTableColumn
mscVrPpSrsgStpTypeOper = _MscVrPpSrsgStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 3),
    _MscVrPpSrsgStpTypeOper_Type()
)
mscVrPpSrsgStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgStpTypeOper.setStatus("mandatory")


class _MscVrPpSrsgDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpSrsgDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrsgDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpSrsgDesignatedCost_Object = MibTableColumn
mscVrPpSrsgDesignatedCost = _MscVrPpSrsgDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 4),
    _MscVrPpSrsgDesignatedCost_Type()
)
mscVrPpSrsgDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDesignatedCost.setStatus("mandatory")


class _MscVrPpSrsgPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpSrsgPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrsgPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpSrsgPathCostOper_Object = MibTableColumn
mscVrPpSrsgPathCostOper = _MscVrPpSrsgPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 5),
    _MscVrPpSrsgPathCostOper_Type()
)
mscVrPpSrsgPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgPathCostOper.setStatus("mandatory")


class _MscVrPpSrsgDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpSrsgDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrsgDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpSrsgDesignatedBridge_Object = MibTableColumn
mscVrPpSrsgDesignatedBridge = _MscVrPpSrsgDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 6),
    _MscVrPpSrsgDesignatedBridge_Type()
)
mscVrPpSrsgDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDesignatedBridge.setStatus("mandatory")


class _MscVrPpSrsgDesignatedPort_Type(Hex):
    """Custom type mscVrPpSrsgDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrsgDesignatedPort_Type.__name__ = "Hex"
_MscVrPpSrsgDesignatedPort_Object = MibTableColumn
mscVrPpSrsgDesignatedPort = _MscVrPpSrsgDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 7),
    _MscVrPpSrsgDesignatedPort_Type()
)
mscVrPpSrsgDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDesignatedPort.setStatus("mandatory")
_MscVrPpSrsgForwardTransitions_Type = Counter32
_MscVrPpSrsgForwardTransitions_Object = MibTableColumn
mscVrPpSrsgForwardTransitions = _MscVrPpSrsgForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 8),
    _MscVrPpSrsgForwardTransitions_Type()
)
mscVrPpSrsgForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgForwardTransitions.setStatus("mandatory")
_MscVrPpSrsgBlockingDiscards_Type = Counter32
_MscVrPpSrsgBlockingDiscards_Object = MibTableColumn
mscVrPpSrsgBlockingDiscards = _MscVrPpSrsgBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 9),
    _MscVrPpSrsgBlockingDiscards_Type()
)
mscVrPpSrsgBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgBlockingDiscards.setStatus("mandatory")


class _MscVrPpSrsgDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpSrsgDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrsgDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpSrsgDesignatedRoot_Object = MibTableColumn
mscVrPpSrsgDesignatedRoot = _MscVrPpSrsgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 18, 1, 10),
    _MscVrPpSrsgDesignatedRoot_Type()
)
mscVrPpSrsgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDesignatedRoot.setStatus("mandatory")
_MscVrPpSrsgStatsTable_Object = MibTable
mscVrPpSrsgStatsTable = _MscVrPpSrsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStatsTable.setStatus("mandatory")
_MscVrPpSrsgStatsEntry_Object = MibTableRow
mscVrPpSrsgStatsEntry = _MscVrPpSrsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19, 1)
)
mscVrPpSrsgStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgStatsEntry.setStatus("mandatory")
_MscVrPpSrsgBadAbstractDiscards_Type = Counter32
_MscVrPpSrsgBadAbstractDiscards_Object = MibTableColumn
mscVrPpSrsgBadAbstractDiscards = _MscVrPpSrsgBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19, 1, 1),
    _MscVrPpSrsgBadAbstractDiscards_Type()
)
mscVrPpSrsgBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgBadAbstractDiscards.setStatus("mandatory")
_MscVrPpSrsgTinygramFramesIn_Type = Counter32
_MscVrPpSrsgTinygramFramesIn_Object = MibTableColumn
mscVrPpSrsgTinygramFramesIn = _MscVrPpSrsgTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19, 1, 2),
    _MscVrPpSrsgTinygramFramesIn_Type()
)
mscVrPpSrsgTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgTinygramFramesIn.setStatus("mandatory")
_MscVrPpSrsgTinygramFramesOut_Type = Counter32
_MscVrPpSrsgTinygramFramesOut_Object = MibTableColumn
mscVrPpSrsgTinygramFramesOut = _MscVrPpSrsgTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19, 1, 3),
    _MscVrPpSrsgTinygramFramesOut_Type()
)
mscVrPpSrsgTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgTinygramFramesOut.setStatus("mandatory")
_MscVrPpSrsgInFilterDiscards_Type = Counter32
_MscVrPpSrsgInFilterDiscards_Object = MibTableColumn
mscVrPpSrsgInFilterDiscards = _MscVrPpSrsgInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19, 1, 4),
    _MscVrPpSrsgInFilterDiscards_Type()
)
mscVrPpSrsgInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgInFilterDiscards.setStatus("mandatory")
_MscVrPpSrsgOutFilterDiscards_Type = Counter32
_MscVrPpSrsgOutFilterDiscards_Object = MibTableColumn
mscVrPpSrsgOutFilterDiscards = _MscVrPpSrsgOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 19, 1, 5),
    _MscVrPpSrsgOutFilterDiscards_Type()
)
mscVrPpSrsgOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrsgSrProvTable_Object = MibTable
mscVrPpSrsgSrProvTable = _MscVrPpSrsgSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgSrProvTable.setStatus("mandatory")
_MscVrPpSrsgSrProvEntry_Object = MibTableRow
mscVrPpSrsgSrProvEntry = _MscVrPpSrsgSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1)
)
mscVrPpSrsgSrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgSrProvEntry.setStatus("mandatory")


class _MscVrPpSrsgHopCount_Type(Unsigned32):
    """Custom type mscVrPpSrsgHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrPpSrsgHopCount_Type.__name__ = "Unsigned32"
_MscVrPpSrsgHopCount_Object = MibTableColumn
mscVrPpSrsgHopCount = _MscVrPpSrsgHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 1),
    _MscVrPpSrsgHopCount_Type()
)
mscVrPpSrsgHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgHopCount.setStatus("mandatory")


class _MscVrPpSrsgExploreFrameTreatment_Type(Integer32):
    """Custom type mscVrPpSrsgExploreFrameTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encap", 0),
          ("xlate", 1))
    )


_MscVrPpSrsgExploreFrameTreatment_Type.__name__ = "Integer32"
_MscVrPpSrsgExploreFrameTreatment_Object = MibTableColumn
mscVrPpSrsgExploreFrameTreatment = _MscVrPpSrsgExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 2),
    _MscVrPpSrsgExploreFrameTreatment_Type()
)
mscVrPpSrsgExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgExploreFrameTreatment.setStatus("mandatory")


class _MscVrPpSrsgLanId_Type(Unsigned32):
    """Custom type mscVrPpSrsgLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrsgLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrsgLanId_Object = MibTableColumn
mscVrPpSrsgLanId = _MscVrPpSrsgLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 3),
    _MscVrPpSrsgLanId_Type()
)
mscVrPpSrsgLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgLanId.setStatus("mandatory")


class _MscVrPpSrsgInternalLanId_Type(Unsigned32):
    """Custom type mscVrPpSrsgInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrsgInternalLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrsgInternalLanId_Object = MibTableColumn
mscVrPpSrsgInternalLanId = _MscVrPpSrsgInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 4),
    _MscVrPpSrsgInternalLanId_Type()
)
mscVrPpSrsgInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgInternalLanId.setStatus("mandatory")


class _MscVrPpSrsgBridgeNum_Type(Unsigned32):
    """Custom type mscVrPpSrsgBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrPpSrsgBridgeNum_Type.__name__ = "Unsigned32"
_MscVrPpSrsgBridgeNum_Object = MibTableColumn
mscVrPpSrsgBridgeNum = _MscVrPpSrsgBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 5),
    _MscVrPpSrsgBridgeNum_Type()
)
mscVrPpSrsgBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgBridgeNum.setStatus("mandatory")


class _MscVrPpSrsgLargestFrame_Type(Unsigned32):
    """Custom type mscVrPpSrsgLargestFrame based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 516),
        ValueRangeConstraint(1470, 1470),
        ValueRangeConstraint(2052, 2052),
        ValueRangeConstraint(4399, 4399),
        ValueRangeConstraint(8130, 8130),
        ValueRangeConstraint(11407, 11407),
        ValueRangeConstraint(17749, 17749),
    )


_MscVrPpSrsgLargestFrame_Type.__name__ = "Unsigned32"
_MscVrPpSrsgLargestFrame_Object = MibTableColumn
mscVrPpSrsgLargestFrame = _MscVrPpSrsgLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 6),
    _MscVrPpSrsgLargestFrame_Type()
)
mscVrPpSrsgLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgLargestFrame.setStatus("mandatory")


class _MscVrPpSrsgSteSpanMode_Type(Integer32):
    """Custom type mscVrPpSrsgSteSpanMode based on Integer32"""
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
        *(("autoSpan", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_MscVrPpSrsgSteSpanMode_Type.__name__ = "Integer32"
_MscVrPpSrsgSteSpanMode_Object = MibTableColumn
mscVrPpSrsgSteSpanMode = _MscVrPpSrsgSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 7),
    _MscVrPpSrsgSteSpanMode_Type()
)
mscVrPpSrsgSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgSteSpanMode.setStatus("mandatory")


class _MscVrPpSrsgAreRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrsgAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrsgAreRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrsgAreRdLimit_Object = MibTableColumn
mscVrPpSrsgAreRdLimit = _MscVrPpSrsgAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 8),
    _MscVrPpSrsgAreRdLimit_Type()
)
mscVrPpSrsgAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgAreRdLimit.setStatus("mandatory")


class _MscVrPpSrsgSteRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrsgSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrsgSteRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrsgSteRdLimit_Object = MibTableColumn
mscVrPpSrsgSteRdLimit = _MscVrPpSrsgSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 20, 1, 9),
    _MscVrPpSrsgSteRdLimit_Type()
)
mscVrPpSrsgSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrsgSteRdLimit.setStatus("mandatory")
_MscVrPpSrsgSrStatsTable_Object = MibTable
mscVrPpSrsgSrStatsTable = _MscVrPpSrsgSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21)
)
if mibBuilder.loadTexts:
    mscVrPpSrsgSrStatsTable.setStatus("mandatory")
_MscVrPpSrsgSrStatsEntry_Object = MibTableRow
mscVrPpSrsgSrStatsEntry = _MscVrPpSrsgSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1)
)
mscVrPpSrsgSrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrsgSrStatsEntry.setStatus("mandatory")
_MscVrPpSrsgSpecInFrames_Type = Counter32
_MscVrPpSrsgSpecInFrames_Object = MibTableColumn
mscVrPpSrsgSpecInFrames = _MscVrPpSrsgSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 1),
    _MscVrPpSrsgSpecInFrames_Type()
)
mscVrPpSrsgSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgSpecInFrames.setStatus("mandatory")
_MscVrPpSrsgSpecOutFrames_Type = Counter32
_MscVrPpSrsgSpecOutFrames_Object = MibTableColumn
mscVrPpSrsgSpecOutFrames = _MscVrPpSrsgSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 2),
    _MscVrPpSrsgSpecOutFrames_Type()
)
mscVrPpSrsgSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgSpecOutFrames.setStatus("mandatory")
_MscVrPpSrsgApeInFrames_Type = Counter32
_MscVrPpSrsgApeInFrames_Object = MibTableColumn
mscVrPpSrsgApeInFrames = _MscVrPpSrsgApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 3),
    _MscVrPpSrsgApeInFrames_Type()
)
mscVrPpSrsgApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgApeInFrames.setStatus("mandatory")
_MscVrPpSrsgApeOutFrames_Type = Counter32
_MscVrPpSrsgApeOutFrames_Object = MibTableColumn
mscVrPpSrsgApeOutFrames = _MscVrPpSrsgApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 4),
    _MscVrPpSrsgApeOutFrames_Type()
)
mscVrPpSrsgApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgApeOutFrames.setStatus("mandatory")
_MscVrPpSrsgSteInFrames_Type = Counter32
_MscVrPpSrsgSteInFrames_Object = MibTableColumn
mscVrPpSrsgSteInFrames = _MscVrPpSrsgSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 5),
    _MscVrPpSrsgSteInFrames_Type()
)
mscVrPpSrsgSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgSteInFrames.setStatus("mandatory")
_MscVrPpSrsgSteOutFrames_Type = Counter32
_MscVrPpSrsgSteOutFrames_Object = MibTableColumn
mscVrPpSrsgSteOutFrames = _MscVrPpSrsgSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 6),
    _MscVrPpSrsgSteOutFrames_Type()
)
mscVrPpSrsgSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgSteOutFrames.setStatus("mandatory")
_MscVrPpSrsgSegmentMismatchDiscards_Type = Counter32
_MscVrPpSrsgSegmentMismatchDiscards_Object = MibTableColumn
mscVrPpSrsgSegmentMismatchDiscards = _MscVrPpSrsgSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 7),
    _MscVrPpSrsgSegmentMismatchDiscards_Type()
)
mscVrPpSrsgSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgSegmentMismatchDiscards.setStatus("mandatory")
_MscVrPpSrsgDupSegmentDiscards_Type = Counter32
_MscVrPpSrsgDupSegmentDiscards_Object = MibTableColumn
mscVrPpSrsgDupSegmentDiscards = _MscVrPpSrsgDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 8),
    _MscVrPpSrsgDupSegmentDiscards_Type()
)
mscVrPpSrsgDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDupSegmentDiscards.setStatus("mandatory")
_MscVrPpSrsgHopCountExceededDiscards_Type = Counter32
_MscVrPpSrsgHopCountExceededDiscards_Object = MibTableColumn
mscVrPpSrsgHopCountExceededDiscards = _MscVrPpSrsgHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 9),
    _MscVrPpSrsgHopCountExceededDiscards_Type()
)
mscVrPpSrsgHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgHopCountExceededDiscards.setStatus("mandatory")
_MscVrPpSrsgDupLanIdOrTreeErrors_Type = Counter32
_MscVrPpSrsgDupLanIdOrTreeErrors_Object = MibTableColumn
mscVrPpSrsgDupLanIdOrTreeErrors = _MscVrPpSrsgDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 10),
    _MscVrPpSrsgDupLanIdOrTreeErrors_Type()
)
mscVrPpSrsgDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDupLanIdOrTreeErrors.setStatus("mandatory")
_MscVrPpSrsgLanIdMismatches_Type = Counter32
_MscVrPpSrsgLanIdMismatches_Object = MibTableColumn
mscVrPpSrsgLanIdMismatches = _MscVrPpSrsgLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 11),
    _MscVrPpSrsgLanIdMismatches_Type()
)
mscVrPpSrsgLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgLanIdMismatches.setStatus("mandatory")
_MscVrPpSrsgStaticDiscards_Type = Counter32
_MscVrPpSrsgStaticDiscards_Object = MibTableColumn
mscVrPpSrsgStaticDiscards = _MscVrPpSrsgStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 12),
    _MscVrPpSrsgStaticDiscards_Type()
)
mscVrPpSrsgStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgStaticDiscards.setStatus("mandatory")
_MscVrPpSrsgDynamicDiscards_Type = Counter32
_MscVrPpSrsgDynamicDiscards_Object = MibTableColumn
mscVrPpSrsgDynamicDiscards = _MscVrPpSrsgDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 12, 21, 1, 13),
    _MscVrPpSrsgDynamicDiscards_Type()
)
mscVrPpSrsgDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrsgDynamicDiscards.setStatus("mandatory")
_MscVrPpTbsg_ObjectIdentity = ObjectIdentity
mscVrPpTbsg = _MscVrPpTbsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13)
)
_MscVrPpTbsgRowStatusTable_Object = MibTable
mscVrPpTbsgRowStatusTable = _MscVrPpTbsgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 1)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgRowStatusTable.setStatus("mandatory")
_MscVrPpTbsgRowStatusEntry_Object = MibTableRow
mscVrPpTbsgRowStatusEntry = _MscVrPpTbsgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 1, 1)
)
mscVrPpTbsgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgRowStatusEntry.setStatus("mandatory")
_MscVrPpTbsgRowStatus_Type = RowStatus
_MscVrPpTbsgRowStatus_Object = MibTableColumn
mscVrPpTbsgRowStatus = _MscVrPpTbsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 1, 1, 1),
    _MscVrPpTbsgRowStatus_Type()
)
mscVrPpTbsgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgRowStatus.setStatus("mandatory")
_MscVrPpTbsgComponentName_Type = DisplayString
_MscVrPpTbsgComponentName_Object = MibTableColumn
mscVrPpTbsgComponentName = _MscVrPpTbsgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 1, 1, 2),
    _MscVrPpTbsgComponentName_Type()
)
mscVrPpTbsgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgComponentName.setStatus("mandatory")
_MscVrPpTbsgStorageType_Type = StorageType
_MscVrPpTbsgStorageType_Object = MibTableColumn
mscVrPpTbsgStorageType = _MscVrPpTbsgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 1, 1, 4),
    _MscVrPpTbsgStorageType_Type()
)
mscVrPpTbsgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgStorageType.setStatus("mandatory")
_MscVrPpTbsgIndex_Type = NonReplicated
_MscVrPpTbsgIndex_Object = MibTableColumn
mscVrPpTbsgIndex = _MscVrPpTbsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 1, 1, 10),
    _MscVrPpTbsgIndex_Type()
)
mscVrPpTbsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpTbsgIndex.setStatus("mandatory")
_MscVrPpTbsgProvTable_Object = MibTable
mscVrPpTbsgProvTable = _MscVrPpTbsgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgProvTable.setStatus("mandatory")
_MscVrPpTbsgProvEntry_Object = MibTableRow
mscVrPpTbsgProvEntry = _MscVrPpTbsgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10, 1)
)
mscVrPpTbsgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgProvEntry.setStatus("mandatory")


class _MscVrPpTbsgTranslateIpx_Type(Integer32):
    """Custom type mscVrPpTbsgTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpTbsgTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpTbsgTranslateIpx_Object = MibTableColumn
mscVrPpTbsgTranslateIpx = _MscVrPpTbsgTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10, 1, 1),
    _MscVrPpTbsgTranslateIpx_Type()
)
mscVrPpTbsgTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgTranslateIpx.setStatus("mandatory")


class _MscVrPpTbsgFragmentIp_Type(Integer32):
    """Custom type mscVrPpTbsgFragmentIp based on Integer32"""
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


_MscVrPpTbsgFragmentIp_Type.__name__ = "Integer32"
_MscVrPpTbsgFragmentIp_Object = MibTableColumn
mscVrPpTbsgFragmentIp = _MscVrPpTbsgFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10, 1, 2),
    _MscVrPpTbsgFragmentIp_Type()
)
mscVrPpTbsgFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgFragmentIp.setStatus("mandatory")


class _MscVrPpTbsgServiceClass_Type(Integer32):
    """Custom type mscVrPpTbsgServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpTbsgServiceClass_Type.__name__ = "Integer32"
_MscVrPpTbsgServiceClass_Object = MibTableColumn
mscVrPpTbsgServiceClass = _MscVrPpTbsgServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10, 1, 3),
    _MscVrPpTbsgServiceClass_Type()
)
mscVrPpTbsgServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgServiceClass.setStatus("mandatory")


class _MscVrPpTbsgConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpTbsgConvertArpMacAddress based on Integer32"""
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


_MscVrPpTbsgConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpTbsgConvertArpMacAddress_Object = MibTableColumn
mscVrPpTbsgConvertArpMacAddress = _MscVrPpTbsgConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10, 1, 4),
    _MscVrPpTbsgConvertArpMacAddress_Type()
)
mscVrPpTbsgConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpTbsgPortNum_Type(Unsigned32):
    """Custom type mscVrPpTbsgPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpTbsgPortNum_Type.__name__ = "Unsigned32"
_MscVrPpTbsgPortNum_Object = MibTableColumn
mscVrPpTbsgPortNum = _MscVrPpTbsgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 10, 1, 5),
    _MscVrPpTbsgPortNum_Type()
)
mscVrPpTbsgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgPortNum.setStatus("mandatory")
_MscVrPpTbsgTbProvTable_Object = MibTable
mscVrPpTbsgTbProvTable = _MscVrPpTbsgTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 11)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgTbProvTable.setStatus("mandatory")
_MscVrPpTbsgTbProvEntry_Object = MibTableRow
mscVrPpTbsgTbProvEntry = _MscVrPpTbsgTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 11, 1)
)
mscVrPpTbsgTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgTbProvEntry.setStatus("mandatory")


class _MscVrPpTbsgSecureOption_Type(Integer32):
    """Custom type mscVrPpTbsgSecureOption based on Integer32"""
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


_MscVrPpTbsgSecureOption_Type.__name__ = "Integer32"
_MscVrPpTbsgSecureOption_Object = MibTableColumn
mscVrPpTbsgSecureOption = _MscVrPpTbsgSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 11, 1, 1),
    _MscVrPpTbsgSecureOption_Type()
)
mscVrPpTbsgSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgSecureOption.setStatus("mandatory")
_MscVrPpTbsgStpProvTable_Object = MibTable
mscVrPpTbsgStpProvTable = _MscVrPpTbsgStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStpProvTable.setStatus("mandatory")
_MscVrPpTbsgStpProvEntry_Object = MibTableRow
mscVrPpTbsgStpProvEntry = _MscVrPpTbsgStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1)
)
mscVrPpTbsgStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStpProvEntry.setStatus("mandatory")


class _MscVrPpTbsgAdminStatus_Type(Integer32):
    """Custom type mscVrPpTbsgAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpTbsgAdminStatus_Type.__name__ = "Integer32"
_MscVrPpTbsgAdminStatus_Object = MibTableColumn
mscVrPpTbsgAdminStatus = _MscVrPpTbsgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1, 1),
    _MscVrPpTbsgAdminStatus_Type()
)
mscVrPpTbsgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgAdminStatus.setStatus("mandatory")


class _MscVrPpTbsgPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpTbsgPortStateStpControl based on Integer32"""
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


_MscVrPpTbsgPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpTbsgPortStateStpControl_Object = MibTableColumn
mscVrPpTbsgPortStateStpControl = _MscVrPpTbsgPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1, 2),
    _MscVrPpTbsgPortStateStpControl_Type()
)
mscVrPpTbsgPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgPortStateStpControl.setStatus("mandatory")


class _MscVrPpTbsgStpTypeProv_Type(Integer32):
    """Custom type mscVrPpTbsgStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpTbsgStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpTbsgStpTypeProv_Object = MibTableColumn
mscVrPpTbsgStpTypeProv = _MscVrPpTbsgStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1, 3),
    _MscVrPpTbsgStpTypeProv_Type()
)
mscVrPpTbsgStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgStpTypeProv.setStatus("mandatory")


class _MscVrPpTbsgPortPriority_Type(Unsigned32):
    """Custom type mscVrPpTbsgPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbsgPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpTbsgPortPriority_Object = MibTableColumn
mscVrPpTbsgPortPriority = _MscVrPpTbsgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1, 4),
    _MscVrPpTbsgPortPriority_Type()
)
mscVrPpTbsgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgPortPriority.setStatus("mandatory")


class _MscVrPpTbsgPathCost_Type(Unsigned32):
    """Custom type mscVrPpTbsgPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbsgPathCost_Type.__name__ = "Unsigned32"
_MscVrPpTbsgPathCost_Object = MibTableColumn
mscVrPpTbsgPathCost = _MscVrPpTbsgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1, 5),
    _MscVrPpTbsgPathCost_Type()
)
mscVrPpTbsgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgPathCost.setStatus("mandatory")


class _MscVrPpTbsgPathCostMethod_Type(Integer32):
    """Custom type mscVrPpTbsgPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpTbsgPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpTbsgPathCostMethod_Object = MibTableColumn
mscVrPpTbsgPathCostMethod = _MscVrPpTbsgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 12, 1, 6),
    _MscVrPpTbsgPathCostMethod_Type()
)
mscVrPpTbsgPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgPathCostMethod.setStatus("mandatory")
_MscVrPpTbsgDIProvTable_Object = MibTable
mscVrPpTbsgDIProvTable = _MscVrPpTbsgDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 13)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgDIProvTable.setStatus("mandatory")
_MscVrPpTbsgDIProvEntry_Object = MibTableRow
mscVrPpTbsgDIProvEntry = _MscVrPpTbsgDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 13, 1)
)
mscVrPpTbsgDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgDIProvEntry.setStatus("mandatory")


class _MscVrPpTbsgDomainNum_Type(Unsigned32):
    """Custom type mscVrPpTbsgDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpTbsgDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpTbsgDomainNum_Object = MibTableColumn
mscVrPpTbsgDomainNum = _MscVrPpTbsgDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 13, 1, 1),
    _MscVrPpTbsgDomainNum_Type()
)
mscVrPpTbsgDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgDomainNum.setStatus("mandatory")


class _MscVrPpTbsgPreserveDomain_Type(Integer32):
    """Custom type mscVrPpTbsgPreserveDomain based on Integer32"""
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


_MscVrPpTbsgPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpTbsgPreserveDomain_Object = MibTableColumn
mscVrPpTbsgPreserveDomain = _MscVrPpTbsgPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 13, 1, 2),
    _MscVrPpTbsgPreserveDomain_Type()
)
mscVrPpTbsgPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpTbsgPreserveDomain.setStatus("mandatory")
_MscVrPpTbsgStateTable_Object = MibTable
mscVrPpTbsgStateTable = _MscVrPpTbsgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 14)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStateTable.setStatus("mandatory")
_MscVrPpTbsgStateEntry_Object = MibTableRow
mscVrPpTbsgStateEntry = _MscVrPpTbsgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 14, 1)
)
mscVrPpTbsgStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStateEntry.setStatus("mandatory")


class _MscVrPpTbsgAdminState_Type(Integer32):
    """Custom type mscVrPpTbsgAdminState based on Integer32"""
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


_MscVrPpTbsgAdminState_Type.__name__ = "Integer32"
_MscVrPpTbsgAdminState_Object = MibTableColumn
mscVrPpTbsgAdminState = _MscVrPpTbsgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 14, 1, 1),
    _MscVrPpTbsgAdminState_Type()
)
mscVrPpTbsgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgAdminState.setStatus("mandatory")


class _MscVrPpTbsgOperationalState_Type(Integer32):
    """Custom type mscVrPpTbsgOperationalState based on Integer32"""
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


_MscVrPpTbsgOperationalState_Type.__name__ = "Integer32"
_MscVrPpTbsgOperationalState_Object = MibTableColumn
mscVrPpTbsgOperationalState = _MscVrPpTbsgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 14, 1, 2),
    _MscVrPpTbsgOperationalState_Type()
)
mscVrPpTbsgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgOperationalState.setStatus("mandatory")


class _MscVrPpTbsgUsageState_Type(Integer32):
    """Custom type mscVrPpTbsgUsageState based on Integer32"""
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


_MscVrPpTbsgUsageState_Type.__name__ = "Integer32"
_MscVrPpTbsgUsageState_Object = MibTableColumn
mscVrPpTbsgUsageState = _MscVrPpTbsgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 14, 1, 3),
    _MscVrPpTbsgUsageState_Type()
)
mscVrPpTbsgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgUsageState.setStatus("mandatory")
_MscVrPpTbsgOperStatusTable_Object = MibTable
mscVrPpTbsgOperStatusTable = _MscVrPpTbsgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 15)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgOperStatusTable.setStatus("mandatory")
_MscVrPpTbsgOperStatusEntry_Object = MibTableRow
mscVrPpTbsgOperStatusEntry = _MscVrPpTbsgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 15, 1)
)
mscVrPpTbsgOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgOperStatusEntry.setStatus("mandatory")


class _MscVrPpTbsgSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpTbsgSnmpOperStatus based on Integer32"""
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


_MscVrPpTbsgSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpTbsgSnmpOperStatus_Object = MibTableColumn
mscVrPpTbsgSnmpOperStatus = _MscVrPpTbsgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 15, 1, 1),
    _MscVrPpTbsgSnmpOperStatus_Type()
)
mscVrPpTbsgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgSnmpOperStatus.setStatus("mandatory")
_MscVrPpTbsgOperTable_Object = MibTable
mscVrPpTbsgOperTable = _MscVrPpTbsgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgOperTable.setStatus("mandatory")
_MscVrPpTbsgOperEntry_Object = MibTableRow
mscVrPpTbsgOperEntry = _MscVrPpTbsgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1)
)
mscVrPpTbsgOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgOperEntry.setStatus("mandatory")


class _MscVrPpTbsgPortName_Type(AsciiString):
    """Custom type mscVrPpTbsgPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpTbsgPortName_Type.__name__ = "AsciiString"
_MscVrPpTbsgPortName_Object = MibTableColumn
mscVrPpTbsgPortName = _MscVrPpTbsgPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 1),
    _MscVrPpTbsgPortName_Type()
)
mscVrPpTbsgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgPortName.setStatus("mandatory")


class _MscVrPpTbsgUpTime_Type(Unsigned32):
    """Custom type mscVrPpTbsgUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbsgUpTime_Type.__name__ = "Unsigned32"
_MscVrPpTbsgUpTime_Object = MibTableColumn
mscVrPpTbsgUpTime = _MscVrPpTbsgUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 3),
    _MscVrPpTbsgUpTime_Type()
)
mscVrPpTbsgUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgUpTime.setStatus("mandatory")


class _MscVrPpTbsgDownTime_Type(Unsigned32):
    """Custom type mscVrPpTbsgDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbsgDownTime_Type.__name__ = "Unsigned32"
_MscVrPpTbsgDownTime_Object = MibTableColumn
mscVrPpTbsgDownTime = _MscVrPpTbsgDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 4),
    _MscVrPpTbsgDownTime_Type()
)
mscVrPpTbsgDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDownTime.setStatus("mandatory")


class _MscVrPpTbsgBridgingMode_Type(Integer32):
    """Custom type mscVrPpTbsgBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpTbsgBridgingMode_Type.__name__ = "Integer32"
_MscVrPpTbsgBridgingMode_Object = MibTableColumn
mscVrPpTbsgBridgingMode = _MscVrPpTbsgBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 5),
    _MscVrPpTbsgBridgingMode_Type()
)
mscVrPpTbsgBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgBridgingMode.setStatus("mandatory")


class _MscVrPpTbsgBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpTbsgBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpTbsgBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpTbsgBridgePortConfig_Object = MibTableColumn
mscVrPpTbsgBridgePortConfig = _MscVrPpTbsgBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 6),
    _MscVrPpTbsgBridgePortConfig_Type()
)
mscVrPpTbsgBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgBridgePortConfig.setStatus("mandatory")


class _MscVrPpTbsgBridgePortType_Type(Integer32):
    """Custom type mscVrPpTbsgBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpTbsgBridgePortType_Type.__name__ = "Integer32"
_MscVrPpTbsgBridgePortType_Object = MibTableColumn
mscVrPpTbsgBridgePortType = _MscVrPpTbsgBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 7),
    _MscVrPpTbsgBridgePortType_Type()
)
mscVrPpTbsgBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgBridgePortType.setStatus("mandatory")


class _MscVrPpTbsgIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpTbsgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbsgIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpTbsgIfIndex_Object = MibTableColumn
mscVrPpTbsgIfIndex = _MscVrPpTbsgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 8),
    _MscVrPpTbsgIfIndex_Type()
)
mscVrPpTbsgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgIfIndex.setStatus("mandatory")
_MscVrPpTbsgDelayExceededDiscards_Type = Counter32
_MscVrPpTbsgDelayExceededDiscards_Object = MibTableColumn
mscVrPpTbsgDelayExceededDiscards = _MscVrPpTbsgDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 10),
    _MscVrPpTbsgDelayExceededDiscards_Type()
)
mscVrPpTbsgDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDelayExceededDiscards.setStatus("mandatory")
_MscVrPpTbsgMtuExceededDiscards_Type = Counter32
_MscVrPpTbsgMtuExceededDiscards_Object = MibTableColumn
mscVrPpTbsgMtuExceededDiscards = _MscVrPpTbsgMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 16, 1, 11),
    _MscVrPpTbsgMtuExceededDiscards_Type()
)
mscVrPpTbsgMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgMtuExceededDiscards.setStatus("mandatory")
_MscVrPpTbsgTbOperTable_Object = MibTable
mscVrPpTbsgTbOperTable = _MscVrPpTbsgTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgTbOperTable.setStatus("mandatory")
_MscVrPpTbsgTbOperEntry_Object = MibTableRow
mscVrPpTbsgTbOperEntry = _MscVrPpTbsgTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1)
)
mscVrPpTbsgTbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgTbOperEntry.setStatus("mandatory")


class _MscVrPpTbsgMaxInfo_Type(Unsigned32):
    """Custom type mscVrPpTbsgMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbsgMaxInfo_Type.__name__ = "Unsigned32"
_MscVrPpTbsgMaxInfo_Object = MibTableColumn
mscVrPpTbsgMaxInfo = _MscVrPpTbsgMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 2),
    _MscVrPpTbsgMaxInfo_Type()
)
mscVrPpTbsgMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgMaxInfo.setStatus("mandatory")
_MscVrPpTbsgBadVerifyDiscards_Type = Counter32
_MscVrPpTbsgBadVerifyDiscards_Object = MibTableColumn
mscVrPpTbsgBadVerifyDiscards = _MscVrPpTbsgBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 3),
    _MscVrPpTbsgBadVerifyDiscards_Type()
)
mscVrPpTbsgBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgBadVerifyDiscards.setStatus("mandatory")
_MscVrPpTbsgUnicastNoMatches_Type = Counter32
_MscVrPpTbsgUnicastNoMatches_Object = MibTableColumn
mscVrPpTbsgUnicastNoMatches = _MscVrPpTbsgUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 4),
    _MscVrPpTbsgUnicastNoMatches_Type()
)
mscVrPpTbsgUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgUnicastNoMatches.setStatus("mandatory")
_MscVrPpTbsgStaticEntryDiscards_Type = Counter32
_MscVrPpTbsgStaticEntryDiscards_Object = MibTableColumn
mscVrPpTbsgStaticEntryDiscards = _MscVrPpTbsgStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 5),
    _MscVrPpTbsgStaticEntryDiscards_Type()
)
mscVrPpTbsgStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgStaticEntryDiscards.setStatus("mandatory")
_MscVrPpTbsgDynamicEntryDiscards_Type = Counter32
_MscVrPpTbsgDynamicEntryDiscards_Object = MibTableColumn
mscVrPpTbsgDynamicEntryDiscards = _MscVrPpTbsgDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 6),
    _MscVrPpTbsgDynamicEntryDiscards_Type()
)
mscVrPpTbsgDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDynamicEntryDiscards.setStatus("mandatory")
_MscVrPpTbsgLearningDiscards_Type = Counter32
_MscVrPpTbsgLearningDiscards_Object = MibTableColumn
mscVrPpTbsgLearningDiscards = _MscVrPpTbsgLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 7),
    _MscVrPpTbsgLearningDiscards_Type()
)
mscVrPpTbsgLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgLearningDiscards.setStatus("mandatory")
_MscVrPpTbsgInDiscards_Type = Counter32
_MscVrPpTbsgInDiscards_Object = MibTableColumn
mscVrPpTbsgInDiscards = _MscVrPpTbsgInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 8),
    _MscVrPpTbsgInDiscards_Type()
)
mscVrPpTbsgInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgInDiscards.setStatus("mandatory")
_MscVrPpTbsgInFrames_Type = Counter32
_MscVrPpTbsgInFrames_Object = MibTableColumn
mscVrPpTbsgInFrames = _MscVrPpTbsgInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 9),
    _MscVrPpTbsgInFrames_Type()
)
mscVrPpTbsgInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgInFrames.setStatus("mandatory")
_MscVrPpTbsgOutFrames_Type = Counter32
_MscVrPpTbsgOutFrames_Object = MibTableColumn
mscVrPpTbsgOutFrames = _MscVrPpTbsgOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 17, 1, 10),
    _MscVrPpTbsgOutFrames_Type()
)
mscVrPpTbsgOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgOutFrames.setStatus("mandatory")
_MscVrPpTbsgStpOperTable_Object = MibTable
mscVrPpTbsgStpOperTable = _MscVrPpTbsgStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStpOperTable.setStatus("mandatory")
_MscVrPpTbsgStpOperEntry_Object = MibTableRow
mscVrPpTbsgStpOperEntry = _MscVrPpTbsgStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1)
)
mscVrPpTbsgStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStpOperEntry.setStatus("mandatory")


class _MscVrPpTbsgStpPortState_Type(Integer32):
    """Custom type mscVrPpTbsgStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpTbsgStpPortState_Type.__name__ = "Integer32"
_MscVrPpTbsgStpPortState_Object = MibTableColumn
mscVrPpTbsgStpPortState = _MscVrPpTbsgStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 2),
    _MscVrPpTbsgStpPortState_Type()
)
mscVrPpTbsgStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgStpPortState.setStatus("mandatory")


class _MscVrPpTbsgStpTypeOper_Type(Integer32):
    """Custom type mscVrPpTbsgStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpTbsgStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpTbsgStpTypeOper_Object = MibTableColumn
mscVrPpTbsgStpTypeOper = _MscVrPpTbsgStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 3),
    _MscVrPpTbsgStpTypeOper_Type()
)
mscVrPpTbsgStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgStpTypeOper.setStatus("mandatory")


class _MscVrPpTbsgDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpTbsgDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpTbsgDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpTbsgDesignatedCost_Object = MibTableColumn
mscVrPpTbsgDesignatedCost = _MscVrPpTbsgDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 4),
    _MscVrPpTbsgDesignatedCost_Type()
)
mscVrPpTbsgDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDesignatedCost.setStatus("mandatory")


class _MscVrPpTbsgPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpTbsgPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpTbsgPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpTbsgPathCostOper_Object = MibTableColumn
mscVrPpTbsgPathCostOper = _MscVrPpTbsgPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 5),
    _MscVrPpTbsgPathCostOper_Type()
)
mscVrPpTbsgPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgPathCostOper.setStatus("mandatory")


class _MscVrPpTbsgDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpTbsgDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbsgDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpTbsgDesignatedBridge_Object = MibTableColumn
mscVrPpTbsgDesignatedBridge = _MscVrPpTbsgDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 6),
    _MscVrPpTbsgDesignatedBridge_Type()
)
mscVrPpTbsgDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDesignatedBridge.setStatus("mandatory")


class _MscVrPpTbsgDesignatedPort_Type(Hex):
    """Custom type mscVrPpTbsgDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpTbsgDesignatedPort_Type.__name__ = "Hex"
_MscVrPpTbsgDesignatedPort_Object = MibTableColumn
mscVrPpTbsgDesignatedPort = _MscVrPpTbsgDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 7),
    _MscVrPpTbsgDesignatedPort_Type()
)
mscVrPpTbsgDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDesignatedPort.setStatus("mandatory")
_MscVrPpTbsgForwardTransitions_Type = Counter32
_MscVrPpTbsgForwardTransitions_Object = MibTableColumn
mscVrPpTbsgForwardTransitions = _MscVrPpTbsgForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 8),
    _MscVrPpTbsgForwardTransitions_Type()
)
mscVrPpTbsgForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgForwardTransitions.setStatus("mandatory")
_MscVrPpTbsgBlockingDiscards_Type = Counter32
_MscVrPpTbsgBlockingDiscards_Object = MibTableColumn
mscVrPpTbsgBlockingDiscards = _MscVrPpTbsgBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 9),
    _MscVrPpTbsgBlockingDiscards_Type()
)
mscVrPpTbsgBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgBlockingDiscards.setStatus("mandatory")


class _MscVrPpTbsgDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpTbsgDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpTbsgDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpTbsgDesignatedRoot_Object = MibTableColumn
mscVrPpTbsgDesignatedRoot = _MscVrPpTbsgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 18, 1, 10),
    _MscVrPpTbsgDesignatedRoot_Type()
)
mscVrPpTbsgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgDesignatedRoot.setStatus("mandatory")
_MscVrPpTbsgStatsTable_Object = MibTable
mscVrPpTbsgStatsTable = _MscVrPpTbsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19)
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStatsTable.setStatus("mandatory")
_MscVrPpTbsgStatsEntry_Object = MibTableRow
mscVrPpTbsgStatsEntry = _MscVrPpTbsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19, 1)
)
mscVrPpTbsgStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpTbsgStatsEntry.setStatus("mandatory")
_MscVrPpTbsgBadAbstractDiscards_Type = Counter32
_MscVrPpTbsgBadAbstractDiscards_Object = MibTableColumn
mscVrPpTbsgBadAbstractDiscards = _MscVrPpTbsgBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19, 1, 1),
    _MscVrPpTbsgBadAbstractDiscards_Type()
)
mscVrPpTbsgBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgBadAbstractDiscards.setStatus("mandatory")
_MscVrPpTbsgTinygramFramesIn_Type = Counter32
_MscVrPpTbsgTinygramFramesIn_Object = MibTableColumn
mscVrPpTbsgTinygramFramesIn = _MscVrPpTbsgTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19, 1, 2),
    _MscVrPpTbsgTinygramFramesIn_Type()
)
mscVrPpTbsgTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgTinygramFramesIn.setStatus("mandatory")
_MscVrPpTbsgTinygramFramesOut_Type = Counter32
_MscVrPpTbsgTinygramFramesOut_Object = MibTableColumn
mscVrPpTbsgTinygramFramesOut = _MscVrPpTbsgTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19, 1, 3),
    _MscVrPpTbsgTinygramFramesOut_Type()
)
mscVrPpTbsgTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgTinygramFramesOut.setStatus("mandatory")
_MscVrPpTbsgInFilterDiscards_Type = Counter32
_MscVrPpTbsgInFilterDiscards_Object = MibTableColumn
mscVrPpTbsgInFilterDiscards = _MscVrPpTbsgInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19, 1, 4),
    _MscVrPpTbsgInFilterDiscards_Type()
)
mscVrPpTbsgInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgInFilterDiscards.setStatus("mandatory")
_MscVrPpTbsgOutFilterDiscards_Type = Counter32
_MscVrPpTbsgOutFilterDiscards_Object = MibTableColumn
mscVrPpTbsgOutFilterDiscards = _MscVrPpTbsgOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 13, 19, 1, 5),
    _MscVrPpTbsgOutFilterDiscards_Type()
)
mscVrPpTbsgOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpTbsgOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrcl_ObjectIdentity = ObjectIdentity
mscVrPpSrcl = _MscVrPpSrcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14)
)
_MscVrPpSrclRowStatusTable_Object = MibTable
mscVrPpSrclRowStatusTable = _MscVrPpSrclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrclRowStatusTable.setStatus("mandatory")
_MscVrPpSrclRowStatusEntry_Object = MibTableRow
mscVrPpSrclRowStatusEntry = _MscVrPpSrclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 1, 1)
)
mscVrPpSrclRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclRowStatusEntry.setStatus("mandatory")
_MscVrPpSrclRowStatus_Type = RowStatus
_MscVrPpSrclRowStatus_Object = MibTableColumn
mscVrPpSrclRowStatus = _MscVrPpSrclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 1, 1, 1),
    _MscVrPpSrclRowStatus_Type()
)
mscVrPpSrclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclRowStatus.setStatus("mandatory")
_MscVrPpSrclComponentName_Type = DisplayString
_MscVrPpSrclComponentName_Object = MibTableColumn
mscVrPpSrclComponentName = _MscVrPpSrclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 1, 1, 2),
    _MscVrPpSrclComponentName_Type()
)
mscVrPpSrclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclComponentName.setStatus("mandatory")
_MscVrPpSrclStorageType_Type = StorageType
_MscVrPpSrclStorageType_Object = MibTableColumn
mscVrPpSrclStorageType = _MscVrPpSrclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 1, 1, 4),
    _MscVrPpSrclStorageType_Type()
)
mscVrPpSrclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclStorageType.setStatus("mandatory")
_MscVrPpSrclIndex_Type = NonReplicated
_MscVrPpSrclIndex_Object = MibTableColumn
mscVrPpSrclIndex = _MscVrPpSrclIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 1, 1, 10),
    _MscVrPpSrclIndex_Type()
)
mscVrPpSrclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrclIndex.setStatus("mandatory")
_MscVrPpSrclNs_ObjectIdentity = ObjectIdentity
mscVrPpSrclNs = _MscVrPpSrclNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2)
)
_MscVrPpSrclNsRowStatusTable_Object = MibTable
mscVrPpSrclNsRowStatusTable = _MscVrPpSrclNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSrclNsRowStatusTable.setStatus("mandatory")
_MscVrPpSrclNsRowStatusEntry_Object = MibTableRow
mscVrPpSrclNsRowStatusEntry = _MscVrPpSrclNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 1, 1)
)
mscVrPpSrclNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclNsRowStatusEntry.setStatus("mandatory")
_MscVrPpSrclNsRowStatus_Type = RowStatus
_MscVrPpSrclNsRowStatus_Object = MibTableColumn
mscVrPpSrclNsRowStatus = _MscVrPpSrclNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 1, 1, 1),
    _MscVrPpSrclNsRowStatus_Type()
)
mscVrPpSrclNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclNsRowStatus.setStatus("mandatory")
_MscVrPpSrclNsComponentName_Type = DisplayString
_MscVrPpSrclNsComponentName_Object = MibTableColumn
mscVrPpSrclNsComponentName = _MscVrPpSrclNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 1, 1, 2),
    _MscVrPpSrclNsComponentName_Type()
)
mscVrPpSrclNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclNsComponentName.setStatus("mandatory")
_MscVrPpSrclNsStorageType_Type = StorageType
_MscVrPpSrclNsStorageType_Object = MibTableColumn
mscVrPpSrclNsStorageType = _MscVrPpSrclNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 1, 1, 4),
    _MscVrPpSrclNsStorageType_Type()
)
mscVrPpSrclNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclNsStorageType.setStatus("mandatory")
_MscVrPpSrclNsIndex_Type = NonReplicated
_MscVrPpSrclNsIndex_Object = MibTableColumn
mscVrPpSrclNsIndex = _MscVrPpSrclNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 1, 1, 10),
    _MscVrPpSrclNsIndex_Type()
)
mscVrPpSrclNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSrclNsIndex.setStatus("mandatory")
_MscVrPpSrclNsProvTable_Object = MibTable
mscVrPpSrclNsProvTable = _MscVrPpSrclNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrclNsProvTable.setStatus("mandatory")
_MscVrPpSrclNsProvEntry_Object = MibTableRow
mscVrPpSrclNsProvEntry = _MscVrPpSrclNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 10, 1)
)
mscVrPpSrclNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclNsProvEntry.setStatus("mandatory")


class _MscVrPpSrclNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpSrclNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpSrclNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpSrclNsIncomingFilter_Object = MibTableColumn
mscVrPpSrclNsIncomingFilter = _MscVrPpSrclNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 10, 1, 2),
    _MscVrPpSrclNsIncomingFilter_Type()
)
mscVrPpSrclNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclNsIncomingFilter.setStatus("mandatory")


class _MscVrPpSrclNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpSrclNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpSrclNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpSrclNsOutgoingFilter_Object = MibTableColumn
mscVrPpSrclNsOutgoingFilter = _MscVrPpSrclNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 2, 10, 1, 3),
    _MscVrPpSrclNsOutgoingFilter_Type()
)
mscVrPpSrclNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclNsOutgoingFilter.setStatus("mandatory")
_MscVrPpSrclProvTable_Object = MibTable
mscVrPpSrclProvTable = _MscVrPpSrclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10)
)
if mibBuilder.loadTexts:
    mscVrPpSrclProvTable.setStatus("mandatory")
_MscVrPpSrclProvEntry_Object = MibTableRow
mscVrPpSrclProvEntry = _MscVrPpSrclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10, 1)
)
mscVrPpSrclProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclProvEntry.setStatus("mandatory")


class _MscVrPpSrclTranslateIpx_Type(Integer32):
    """Custom type mscVrPpSrclTranslateIpx based on Integer32"""
    defaultValue = 0

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
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("off", 0),
          ("sap", 4),
          ("snap", 3))
    )


_MscVrPpSrclTranslateIpx_Type.__name__ = "Integer32"
_MscVrPpSrclTranslateIpx_Object = MibTableColumn
mscVrPpSrclTranslateIpx = _MscVrPpSrclTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10, 1, 1),
    _MscVrPpSrclTranslateIpx_Type()
)
mscVrPpSrclTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclTranslateIpx.setStatus("mandatory")


class _MscVrPpSrclFragmentIp_Type(Integer32):
    """Custom type mscVrPpSrclFragmentIp based on Integer32"""
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


_MscVrPpSrclFragmentIp_Type.__name__ = "Integer32"
_MscVrPpSrclFragmentIp_Object = MibTableColumn
mscVrPpSrclFragmentIp = _MscVrPpSrclFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10, 1, 2),
    _MscVrPpSrclFragmentIp_Type()
)
mscVrPpSrclFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclFragmentIp.setStatus("mandatory")


class _MscVrPpSrclServiceClass_Type(Integer32):
    """Custom type mscVrPpSrclServiceClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrdered", 1),
          ("ordered", 0))
    )


_MscVrPpSrclServiceClass_Type.__name__ = "Integer32"
_MscVrPpSrclServiceClass_Object = MibTableColumn
mscVrPpSrclServiceClass = _MscVrPpSrclServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10, 1, 3),
    _MscVrPpSrclServiceClass_Type()
)
mscVrPpSrclServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclServiceClass.setStatus("mandatory")


class _MscVrPpSrclConvertArpMacAddress_Type(Integer32):
    """Custom type mscVrPpSrclConvertArpMacAddress based on Integer32"""
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


_MscVrPpSrclConvertArpMacAddress_Type.__name__ = "Integer32"
_MscVrPpSrclConvertArpMacAddress_Object = MibTableColumn
mscVrPpSrclConvertArpMacAddress = _MscVrPpSrclConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10, 1, 4),
    _MscVrPpSrclConvertArpMacAddress_Type()
)
mscVrPpSrclConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclConvertArpMacAddress.setStatus("mandatory")


class _MscVrPpSrclPortNum_Type(Unsigned32):
    """Custom type mscVrPpSrclPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpSrclPortNum_Type.__name__ = "Unsigned32"
_MscVrPpSrclPortNum_Object = MibTableColumn
mscVrPpSrclPortNum = _MscVrPpSrclPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 10, 1, 5),
    _MscVrPpSrclPortNum_Type()
)
mscVrPpSrclPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclPortNum.setStatus("mandatory")
_MscVrPpSrclStpProvTable_Object = MibTable
mscVrPpSrclStpProvTable = _MscVrPpSrclStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12)
)
if mibBuilder.loadTexts:
    mscVrPpSrclStpProvTable.setStatus("mandatory")
_MscVrPpSrclStpProvEntry_Object = MibTableRow
mscVrPpSrclStpProvEntry = _MscVrPpSrclStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1)
)
mscVrPpSrclStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclStpProvEntry.setStatus("mandatory")


class _MscVrPpSrclAdminStatus_Type(Integer32):
    """Custom type mscVrPpSrclAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpSrclAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSrclAdminStatus_Object = MibTableColumn
mscVrPpSrclAdminStatus = _MscVrPpSrclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1, 1),
    _MscVrPpSrclAdminStatus_Type()
)
mscVrPpSrclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclAdminStatus.setStatus("mandatory")


class _MscVrPpSrclPortStateStpControl_Type(Integer32):
    """Custom type mscVrPpSrclPortStateStpControl based on Integer32"""
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


_MscVrPpSrclPortStateStpControl_Type.__name__ = "Integer32"
_MscVrPpSrclPortStateStpControl_Object = MibTableColumn
mscVrPpSrclPortStateStpControl = _MscVrPpSrclPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1, 2),
    _MscVrPpSrclPortStateStpControl_Type()
)
mscVrPpSrclPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclPortStateStpControl.setStatus("mandatory")


class _MscVrPpSrclStpTypeProv_Type(Integer32):
    """Custom type mscVrPpSrclStpTypeProv based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3))
    )


_MscVrPpSrclStpTypeProv_Type.__name__ = "Integer32"
_MscVrPpSrclStpTypeProv_Object = MibTableColumn
mscVrPpSrclStpTypeProv = _MscVrPpSrclStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1, 3),
    _MscVrPpSrclStpTypeProv_Type()
)
mscVrPpSrclStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclStpTypeProv.setStatus("mandatory")


class _MscVrPpSrclPortPriority_Type(Unsigned32):
    """Custom type mscVrPpSrclPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrclPortPriority_Type.__name__ = "Unsigned32"
_MscVrPpSrclPortPriority_Object = MibTableColumn
mscVrPpSrclPortPriority = _MscVrPpSrclPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1, 4),
    _MscVrPpSrclPortPriority_Type()
)
mscVrPpSrclPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclPortPriority.setStatus("mandatory")


class _MscVrPpSrclPathCost_Type(Unsigned32):
    """Custom type mscVrPpSrclPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrclPathCost_Type.__name__ = "Unsigned32"
_MscVrPpSrclPathCost_Object = MibTableColumn
mscVrPpSrclPathCost = _MscVrPpSrclPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1, 5),
    _MscVrPpSrclPathCost_Type()
)
mscVrPpSrclPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclPathCost.setStatus("mandatory")


class _MscVrPpSrclPathCostMethod_Type(Integer32):
    """Custom type mscVrPpSrclPathCostMethod based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("off", 1))
    )


_MscVrPpSrclPathCostMethod_Type.__name__ = "Integer32"
_MscVrPpSrclPathCostMethod_Object = MibTableColumn
mscVrPpSrclPathCostMethod = _MscVrPpSrclPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 12, 1, 6),
    _MscVrPpSrclPathCostMethod_Type()
)
mscVrPpSrclPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclPathCostMethod.setStatus("mandatory")
_MscVrPpSrclDIProvTable_Object = MibTable
mscVrPpSrclDIProvTable = _MscVrPpSrclDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 13)
)
if mibBuilder.loadTexts:
    mscVrPpSrclDIProvTable.setStatus("mandatory")
_MscVrPpSrclDIProvEntry_Object = MibTableRow
mscVrPpSrclDIProvEntry = _MscVrPpSrclDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 13, 1)
)
mscVrPpSrclDIProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclDIProvEntry.setStatus("mandatory")


class _MscVrPpSrclDomainNum_Type(Unsigned32):
    """Custom type mscVrPpSrclDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_MscVrPpSrclDomainNum_Type.__name__ = "Unsigned32"
_MscVrPpSrclDomainNum_Object = MibTableColumn
mscVrPpSrclDomainNum = _MscVrPpSrclDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 13, 1, 1),
    _MscVrPpSrclDomainNum_Type()
)
mscVrPpSrclDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclDomainNum.setStatus("mandatory")


class _MscVrPpSrclPreserveDomain_Type(Integer32):
    """Custom type mscVrPpSrclPreserveDomain based on Integer32"""
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


_MscVrPpSrclPreserveDomain_Type.__name__ = "Integer32"
_MscVrPpSrclPreserveDomain_Object = MibTableColumn
mscVrPpSrclPreserveDomain = _MscVrPpSrclPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 13, 1, 2),
    _MscVrPpSrclPreserveDomain_Type()
)
mscVrPpSrclPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclPreserveDomain.setStatus("mandatory")
_MscVrPpSrclStateTable_Object = MibTable
mscVrPpSrclStateTable = _MscVrPpSrclStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 14)
)
if mibBuilder.loadTexts:
    mscVrPpSrclStateTable.setStatus("mandatory")
_MscVrPpSrclStateEntry_Object = MibTableRow
mscVrPpSrclStateEntry = _MscVrPpSrclStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 14, 1)
)
mscVrPpSrclStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclStateEntry.setStatus("mandatory")


class _MscVrPpSrclAdminState_Type(Integer32):
    """Custom type mscVrPpSrclAdminState based on Integer32"""
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


_MscVrPpSrclAdminState_Type.__name__ = "Integer32"
_MscVrPpSrclAdminState_Object = MibTableColumn
mscVrPpSrclAdminState = _MscVrPpSrclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 14, 1, 1),
    _MscVrPpSrclAdminState_Type()
)
mscVrPpSrclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclAdminState.setStatus("mandatory")


class _MscVrPpSrclOperationalState_Type(Integer32):
    """Custom type mscVrPpSrclOperationalState based on Integer32"""
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


_MscVrPpSrclOperationalState_Type.__name__ = "Integer32"
_MscVrPpSrclOperationalState_Object = MibTableColumn
mscVrPpSrclOperationalState = _MscVrPpSrclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 14, 1, 2),
    _MscVrPpSrclOperationalState_Type()
)
mscVrPpSrclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclOperationalState.setStatus("mandatory")


class _MscVrPpSrclUsageState_Type(Integer32):
    """Custom type mscVrPpSrclUsageState based on Integer32"""
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


_MscVrPpSrclUsageState_Type.__name__ = "Integer32"
_MscVrPpSrclUsageState_Object = MibTableColumn
mscVrPpSrclUsageState = _MscVrPpSrclUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 14, 1, 3),
    _MscVrPpSrclUsageState_Type()
)
mscVrPpSrclUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclUsageState.setStatus("mandatory")
_MscVrPpSrclOperStatusTable_Object = MibTable
mscVrPpSrclOperStatusTable = _MscVrPpSrclOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 15)
)
if mibBuilder.loadTexts:
    mscVrPpSrclOperStatusTable.setStatus("mandatory")
_MscVrPpSrclOperStatusEntry_Object = MibTableRow
mscVrPpSrclOperStatusEntry = _MscVrPpSrclOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 15, 1)
)
mscVrPpSrclOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclOperStatusEntry.setStatus("mandatory")


class _MscVrPpSrclSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSrclSnmpOperStatus based on Integer32"""
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


_MscVrPpSrclSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSrclSnmpOperStatus_Object = MibTableColumn
mscVrPpSrclSnmpOperStatus = _MscVrPpSrclSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 15, 1, 1),
    _MscVrPpSrclSnmpOperStatus_Type()
)
mscVrPpSrclSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclSnmpOperStatus.setStatus("mandatory")
_MscVrPpSrclOperTable_Object = MibTable
mscVrPpSrclOperTable = _MscVrPpSrclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16)
)
if mibBuilder.loadTexts:
    mscVrPpSrclOperTable.setStatus("mandatory")
_MscVrPpSrclOperEntry_Object = MibTableRow
mscVrPpSrclOperEntry = _MscVrPpSrclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1)
)
mscVrPpSrclOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclOperEntry.setStatus("mandatory")


class _MscVrPpSrclPortName_Type(AsciiString):
    """Custom type mscVrPpSrclPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrPpSrclPortName_Type.__name__ = "AsciiString"
_MscVrPpSrclPortName_Object = MibTableColumn
mscVrPpSrclPortName = _MscVrPpSrclPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 1),
    _MscVrPpSrclPortName_Type()
)
mscVrPpSrclPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclPortName.setStatus("mandatory")


class _MscVrPpSrclUpTime_Type(Unsigned32):
    """Custom type mscVrPpSrclUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrclUpTime_Type.__name__ = "Unsigned32"
_MscVrPpSrclUpTime_Object = MibTableColumn
mscVrPpSrclUpTime = _MscVrPpSrclUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 3),
    _MscVrPpSrclUpTime_Type()
)
mscVrPpSrclUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclUpTime.setStatus("mandatory")


class _MscVrPpSrclDownTime_Type(Unsigned32):
    """Custom type mscVrPpSrclDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrclDownTime_Type.__name__ = "Unsigned32"
_MscVrPpSrclDownTime_Object = MibTableColumn
mscVrPpSrclDownTime = _MscVrPpSrclDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 4),
    _MscVrPpSrclDownTime_Type()
)
mscVrPpSrclDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDownTime.setStatus("mandatory")


class _MscVrPpSrclBridgingMode_Type(Integer32):
    """Custom type mscVrPpSrclBridgingMode based on Integer32"""
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
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2),
          ("unknown", 1))
    )


_MscVrPpSrclBridgingMode_Type.__name__ = "Integer32"
_MscVrPpSrclBridgingMode_Object = MibTableColumn
mscVrPpSrclBridgingMode = _MscVrPpSrclBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 5),
    _MscVrPpSrclBridgingMode_Type()
)
mscVrPpSrclBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclBridgingMode.setStatus("mandatory")


class _MscVrPpSrclBridgePortConfig_Type(Integer32):
    """Custom type mscVrPpSrclBridgePortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrPpSrclBridgePortConfig_Type.__name__ = "Integer32"
_MscVrPpSrclBridgePortConfig_Object = MibTableColumn
mscVrPpSrclBridgePortConfig = _MscVrPpSrclBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 6),
    _MscVrPpSrclBridgePortConfig_Type()
)
mscVrPpSrclBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclBridgePortConfig.setStatus("mandatory")


class _MscVrPpSrclBridgePortType_Type(Integer32):
    """Custom type mscVrPpSrclBridgePortType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeBridgePort", 20),
          ("clusterSrBridgePort", 17),
          ("clusterTbBridgePort", 18),
          ("ethernetBridgePort", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulatingBridgePort", 4),
          ("frameRelayBridgePort", 6),
          ("lanEmulationClientEthernet", 22),
          ("pppBridgePort", 7),
          ("smdsBridgePort", 8),
          ("snaDlrBridgePort", 21),
          ("sourceGateSrBridgePort", 13),
          ("sourceGateTbBridgePort", 14),
          ("srEncapSrBridgePort", 11),
          ("srEncapTbBridgePort", 12),
          ("srtbBridgePort", 15),
          ("tbsrBridgePort", 16),
          ("tokenBusBridgePort", 3),
          ("tokenRingBridgePort", 1),
          ("unknown", 19),
          ("vcpBridgePort", 9),
          ("vnsBridgePort", 5),
          ("x25BridgePort", 10))
    )


_MscVrPpSrclBridgePortType_Type.__name__ = "Integer32"
_MscVrPpSrclBridgePortType_Object = MibTableColumn
mscVrPpSrclBridgePortType = _MscVrPpSrclBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 7),
    _MscVrPpSrclBridgePortType_Type()
)
mscVrPpSrclBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclBridgePortType.setStatus("mandatory")


class _MscVrPpSrclIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpSrclIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrclIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpSrclIfIndex_Object = MibTableColumn
mscVrPpSrclIfIndex = _MscVrPpSrclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 8),
    _MscVrPpSrclIfIndex_Type()
)
mscVrPpSrclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclIfIndex.setStatus("mandatory")
_MscVrPpSrclDelayExceededDiscards_Type = Counter32
_MscVrPpSrclDelayExceededDiscards_Object = MibTableColumn
mscVrPpSrclDelayExceededDiscards = _MscVrPpSrclDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 10),
    _MscVrPpSrclDelayExceededDiscards_Type()
)
mscVrPpSrclDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDelayExceededDiscards.setStatus("mandatory")
_MscVrPpSrclMtuExceededDiscards_Type = Counter32
_MscVrPpSrclMtuExceededDiscards_Object = MibTableColumn
mscVrPpSrclMtuExceededDiscards = _MscVrPpSrclMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 16, 1, 11),
    _MscVrPpSrclMtuExceededDiscards_Type()
)
mscVrPpSrclMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclMtuExceededDiscards.setStatus("mandatory")
_MscVrPpSrclStpOperTable_Object = MibTable
mscVrPpSrclStpOperTable = _MscVrPpSrclStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18)
)
if mibBuilder.loadTexts:
    mscVrPpSrclStpOperTable.setStatus("mandatory")
_MscVrPpSrclStpOperEntry_Object = MibTableRow
mscVrPpSrclStpOperEntry = _MscVrPpSrclStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1)
)
mscVrPpSrclStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclStpOperEntry.setStatus("mandatory")


class _MscVrPpSrclStpPortState_Type(Integer32):
    """Custom type mscVrPpSrclStpPortState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrPpSrclStpPortState_Type.__name__ = "Integer32"
_MscVrPpSrclStpPortState_Object = MibTableColumn
mscVrPpSrclStpPortState = _MscVrPpSrclStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 2),
    _MscVrPpSrclStpPortState_Type()
)
mscVrPpSrclStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclStpPortState.setStatus("mandatory")


class _MscVrPpSrclStpTypeOper_Type(Integer32):
    """Custom type mscVrPpSrclStpTypeOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 3),
          ("none", 0))
    )


_MscVrPpSrclStpTypeOper_Type.__name__ = "Integer32"
_MscVrPpSrclStpTypeOper_Object = MibTableColumn
mscVrPpSrclStpTypeOper = _MscVrPpSrclStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 3),
    _MscVrPpSrclStpTypeOper_Type()
)
mscVrPpSrclStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclStpTypeOper.setStatus("mandatory")


class _MscVrPpSrclDesignatedCost_Type(Unsigned32):
    """Custom type mscVrPpSrclDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpSrclDesignatedCost_Type.__name__ = "Unsigned32"
_MscVrPpSrclDesignatedCost_Object = MibTableColumn
mscVrPpSrclDesignatedCost = _MscVrPpSrclDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 4),
    _MscVrPpSrclDesignatedCost_Type()
)
mscVrPpSrclDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDesignatedCost.setStatus("mandatory")


class _MscVrPpSrclPathCostOper_Type(Unsigned32):
    """Custom type mscVrPpSrclPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpSrclPathCostOper_Type.__name__ = "Unsigned32"
_MscVrPpSrclPathCostOper_Object = MibTableColumn
mscVrPpSrclPathCostOper = _MscVrPpSrclPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 5),
    _MscVrPpSrclPathCostOper_Type()
)
mscVrPpSrclPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclPathCostOper.setStatus("mandatory")


class _MscVrPpSrclDesignatedBridge_Type(BridgeId):
    """Custom type mscVrPpSrclDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrclDesignatedBridge_Type.__name__ = "BridgeId"
_MscVrPpSrclDesignatedBridge_Object = MibTableColumn
mscVrPpSrclDesignatedBridge = _MscVrPpSrclDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 6),
    _MscVrPpSrclDesignatedBridge_Type()
)
mscVrPpSrclDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDesignatedBridge.setStatus("mandatory")


class _MscVrPpSrclDesignatedPort_Type(Hex):
    """Custom type mscVrPpSrclDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpSrclDesignatedPort_Type.__name__ = "Hex"
_MscVrPpSrclDesignatedPort_Object = MibTableColumn
mscVrPpSrclDesignatedPort = _MscVrPpSrclDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 7),
    _MscVrPpSrclDesignatedPort_Type()
)
mscVrPpSrclDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDesignatedPort.setStatus("mandatory")
_MscVrPpSrclForwardTransitions_Type = Counter32
_MscVrPpSrclForwardTransitions_Object = MibTableColumn
mscVrPpSrclForwardTransitions = _MscVrPpSrclForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 8),
    _MscVrPpSrclForwardTransitions_Type()
)
mscVrPpSrclForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclForwardTransitions.setStatus("mandatory")
_MscVrPpSrclBlockingDiscards_Type = Counter32
_MscVrPpSrclBlockingDiscards_Object = MibTableColumn
mscVrPpSrclBlockingDiscards = _MscVrPpSrclBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 9),
    _MscVrPpSrclBlockingDiscards_Type()
)
mscVrPpSrclBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclBlockingDiscards.setStatus("mandatory")


class _MscVrPpSrclDesignatedRoot_Type(BridgeId):
    """Custom type mscVrPpSrclDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrPpSrclDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrPpSrclDesignatedRoot_Object = MibTableColumn
mscVrPpSrclDesignatedRoot = _MscVrPpSrclDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 18, 1, 10),
    _MscVrPpSrclDesignatedRoot_Type()
)
mscVrPpSrclDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDesignatedRoot.setStatus("mandatory")
_MscVrPpSrclStatsTable_Object = MibTable
mscVrPpSrclStatsTable = _MscVrPpSrclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19)
)
if mibBuilder.loadTexts:
    mscVrPpSrclStatsTable.setStatus("mandatory")
_MscVrPpSrclStatsEntry_Object = MibTableRow
mscVrPpSrclStatsEntry = _MscVrPpSrclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19, 1)
)
mscVrPpSrclStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclStatsEntry.setStatus("mandatory")
_MscVrPpSrclBadAbstractDiscards_Type = Counter32
_MscVrPpSrclBadAbstractDiscards_Object = MibTableColumn
mscVrPpSrclBadAbstractDiscards = _MscVrPpSrclBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19, 1, 1),
    _MscVrPpSrclBadAbstractDiscards_Type()
)
mscVrPpSrclBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclBadAbstractDiscards.setStatus("mandatory")
_MscVrPpSrclTinygramFramesIn_Type = Counter32
_MscVrPpSrclTinygramFramesIn_Object = MibTableColumn
mscVrPpSrclTinygramFramesIn = _MscVrPpSrclTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19, 1, 2),
    _MscVrPpSrclTinygramFramesIn_Type()
)
mscVrPpSrclTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclTinygramFramesIn.setStatus("mandatory")
_MscVrPpSrclTinygramFramesOut_Type = Counter32
_MscVrPpSrclTinygramFramesOut_Object = MibTableColumn
mscVrPpSrclTinygramFramesOut = _MscVrPpSrclTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19, 1, 3),
    _MscVrPpSrclTinygramFramesOut_Type()
)
mscVrPpSrclTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclTinygramFramesOut.setStatus("mandatory")
_MscVrPpSrclInFilterDiscards_Type = Counter32
_MscVrPpSrclInFilterDiscards_Object = MibTableColumn
mscVrPpSrclInFilterDiscards = _MscVrPpSrclInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19, 1, 4),
    _MscVrPpSrclInFilterDiscards_Type()
)
mscVrPpSrclInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclInFilterDiscards.setStatus("mandatory")
_MscVrPpSrclOutFilterDiscards_Type = Counter32
_MscVrPpSrclOutFilterDiscards_Object = MibTableColumn
mscVrPpSrclOutFilterDiscards = _MscVrPpSrclOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 19, 1, 5),
    _MscVrPpSrclOutFilterDiscards_Type()
)
mscVrPpSrclOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclOutFilterDiscards.setStatus("mandatory")
_MscVrPpSrclSrProvTable_Object = MibTable
mscVrPpSrclSrProvTable = _MscVrPpSrclSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20)
)
if mibBuilder.loadTexts:
    mscVrPpSrclSrProvTable.setStatus("mandatory")
_MscVrPpSrclSrProvEntry_Object = MibTableRow
mscVrPpSrclSrProvEntry = _MscVrPpSrclSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1)
)
mscVrPpSrclSrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclSrProvEntry.setStatus("mandatory")


class _MscVrPpSrclHopCount_Type(Unsigned32):
    """Custom type mscVrPpSrclHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrPpSrclHopCount_Type.__name__ = "Unsigned32"
_MscVrPpSrclHopCount_Object = MibTableColumn
mscVrPpSrclHopCount = _MscVrPpSrclHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 1),
    _MscVrPpSrclHopCount_Type()
)
mscVrPpSrclHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclHopCount.setStatus("mandatory")


class _MscVrPpSrclExploreFrameTreatment_Type(Integer32):
    """Custom type mscVrPpSrclExploreFrameTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encap", 0),
          ("xlate", 1))
    )


_MscVrPpSrclExploreFrameTreatment_Type.__name__ = "Integer32"
_MscVrPpSrclExploreFrameTreatment_Object = MibTableColumn
mscVrPpSrclExploreFrameTreatment = _MscVrPpSrclExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 2),
    _MscVrPpSrclExploreFrameTreatment_Type()
)
mscVrPpSrclExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclExploreFrameTreatment.setStatus("mandatory")


class _MscVrPpSrclLanId_Type(Unsigned32):
    """Custom type mscVrPpSrclLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrclLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrclLanId_Object = MibTableColumn
mscVrPpSrclLanId = _MscVrPpSrclLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 3),
    _MscVrPpSrclLanId_Type()
)
mscVrPpSrclLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclLanId.setStatus("mandatory")


class _MscVrPpSrclInternalLanId_Type(Unsigned32):
    """Custom type mscVrPpSrclInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrPpSrclInternalLanId_Type.__name__ = "Unsigned32"
_MscVrPpSrclInternalLanId_Object = MibTableColumn
mscVrPpSrclInternalLanId = _MscVrPpSrclInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 4),
    _MscVrPpSrclInternalLanId_Type()
)
mscVrPpSrclInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclInternalLanId.setStatus("mandatory")


class _MscVrPpSrclBridgeNum_Type(Unsigned32):
    """Custom type mscVrPpSrclBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrPpSrclBridgeNum_Type.__name__ = "Unsigned32"
_MscVrPpSrclBridgeNum_Object = MibTableColumn
mscVrPpSrclBridgeNum = _MscVrPpSrclBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 5),
    _MscVrPpSrclBridgeNum_Type()
)
mscVrPpSrclBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclBridgeNum.setStatus("mandatory")


class _MscVrPpSrclLargestFrame_Type(Unsigned32):
    """Custom type mscVrPpSrclLargestFrame based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 516),
        ValueRangeConstraint(1470, 1470),
        ValueRangeConstraint(2052, 2052),
        ValueRangeConstraint(4399, 4399),
        ValueRangeConstraint(8130, 8130),
        ValueRangeConstraint(11407, 11407),
        ValueRangeConstraint(17749, 17749),
    )


_MscVrPpSrclLargestFrame_Type.__name__ = "Unsigned32"
_MscVrPpSrclLargestFrame_Object = MibTableColumn
mscVrPpSrclLargestFrame = _MscVrPpSrclLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 6),
    _MscVrPpSrclLargestFrame_Type()
)
mscVrPpSrclLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclLargestFrame.setStatus("mandatory")


class _MscVrPpSrclSteSpanMode_Type(Integer32):
    """Custom type mscVrPpSrclSteSpanMode based on Integer32"""
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
        *(("autoSpan", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_MscVrPpSrclSteSpanMode_Type.__name__ = "Integer32"
_MscVrPpSrclSteSpanMode_Object = MibTableColumn
mscVrPpSrclSteSpanMode = _MscVrPpSrclSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 7),
    _MscVrPpSrclSteSpanMode_Type()
)
mscVrPpSrclSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclSteSpanMode.setStatus("mandatory")


class _MscVrPpSrclAreRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrclAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrclAreRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrclAreRdLimit_Object = MibTableColumn
mscVrPpSrclAreRdLimit = _MscVrPpSrclAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 8),
    _MscVrPpSrclAreRdLimit_Type()
)
mscVrPpSrclAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclAreRdLimit.setStatus("mandatory")


class _MscVrPpSrclSteRdLimit_Type(Unsigned32):
    """Custom type mscVrPpSrclSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVrPpSrclSteRdLimit_Type.__name__ = "Unsigned32"
_MscVrPpSrclSteRdLimit_Object = MibTableColumn
mscVrPpSrclSteRdLimit = _MscVrPpSrclSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 20, 1, 9),
    _MscVrPpSrclSteRdLimit_Type()
)
mscVrPpSrclSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSrclSteRdLimit.setStatus("mandatory")
_MscVrPpSrclSrStatsTable_Object = MibTable
mscVrPpSrclSrStatsTable = _MscVrPpSrclSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21)
)
if mibBuilder.loadTexts:
    mscVrPpSrclSrStatsTable.setStatus("mandatory")
_MscVrPpSrclSrStatsEntry_Object = MibTableRow
mscVrPpSrclSrStatsEntry = _MscVrPpSrclSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1)
)
mscVrPpSrclSrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSrclSrStatsEntry.setStatus("mandatory")
_MscVrPpSrclSpecInFrames_Type = Counter32
_MscVrPpSrclSpecInFrames_Object = MibTableColumn
mscVrPpSrclSpecInFrames = _MscVrPpSrclSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 1),
    _MscVrPpSrclSpecInFrames_Type()
)
mscVrPpSrclSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclSpecInFrames.setStatus("mandatory")
_MscVrPpSrclSpecOutFrames_Type = Counter32
_MscVrPpSrclSpecOutFrames_Object = MibTableColumn
mscVrPpSrclSpecOutFrames = _MscVrPpSrclSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 2),
    _MscVrPpSrclSpecOutFrames_Type()
)
mscVrPpSrclSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclSpecOutFrames.setStatus("mandatory")
_MscVrPpSrclApeInFrames_Type = Counter32
_MscVrPpSrclApeInFrames_Object = MibTableColumn
mscVrPpSrclApeInFrames = _MscVrPpSrclApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 3),
    _MscVrPpSrclApeInFrames_Type()
)
mscVrPpSrclApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclApeInFrames.setStatus("mandatory")
_MscVrPpSrclApeOutFrames_Type = Counter32
_MscVrPpSrclApeOutFrames_Object = MibTableColumn
mscVrPpSrclApeOutFrames = _MscVrPpSrclApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 4),
    _MscVrPpSrclApeOutFrames_Type()
)
mscVrPpSrclApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclApeOutFrames.setStatus("mandatory")
_MscVrPpSrclSteInFrames_Type = Counter32
_MscVrPpSrclSteInFrames_Object = MibTableColumn
mscVrPpSrclSteInFrames = _MscVrPpSrclSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 5),
    _MscVrPpSrclSteInFrames_Type()
)
mscVrPpSrclSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclSteInFrames.setStatus("mandatory")
_MscVrPpSrclSteOutFrames_Type = Counter32
_MscVrPpSrclSteOutFrames_Object = MibTableColumn
mscVrPpSrclSteOutFrames = _MscVrPpSrclSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 6),
    _MscVrPpSrclSteOutFrames_Type()
)
mscVrPpSrclSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclSteOutFrames.setStatus("mandatory")
_MscVrPpSrclSegmentMismatchDiscards_Type = Counter32
_MscVrPpSrclSegmentMismatchDiscards_Object = MibTableColumn
mscVrPpSrclSegmentMismatchDiscards = _MscVrPpSrclSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 7),
    _MscVrPpSrclSegmentMismatchDiscards_Type()
)
mscVrPpSrclSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclSegmentMismatchDiscards.setStatus("mandatory")
_MscVrPpSrclDupSegmentDiscards_Type = Counter32
_MscVrPpSrclDupSegmentDiscards_Object = MibTableColumn
mscVrPpSrclDupSegmentDiscards = _MscVrPpSrclDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 8),
    _MscVrPpSrclDupSegmentDiscards_Type()
)
mscVrPpSrclDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDupSegmentDiscards.setStatus("mandatory")
_MscVrPpSrclHopCountExceededDiscards_Type = Counter32
_MscVrPpSrclHopCountExceededDiscards_Object = MibTableColumn
mscVrPpSrclHopCountExceededDiscards = _MscVrPpSrclHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 9),
    _MscVrPpSrclHopCountExceededDiscards_Type()
)
mscVrPpSrclHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclHopCountExceededDiscards.setStatus("mandatory")
_MscVrPpSrclDupLanIdOrTreeErrors_Type = Counter32
_MscVrPpSrclDupLanIdOrTreeErrors_Object = MibTableColumn
mscVrPpSrclDupLanIdOrTreeErrors = _MscVrPpSrclDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 10),
    _MscVrPpSrclDupLanIdOrTreeErrors_Type()
)
mscVrPpSrclDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDupLanIdOrTreeErrors.setStatus("mandatory")
_MscVrPpSrclLanIdMismatches_Type = Counter32
_MscVrPpSrclLanIdMismatches_Object = MibTableColumn
mscVrPpSrclLanIdMismatches = _MscVrPpSrclLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 11),
    _MscVrPpSrclLanIdMismatches_Type()
)
mscVrPpSrclLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclLanIdMismatches.setStatus("mandatory")
_MscVrPpSrclStaticDiscards_Type = Counter32
_MscVrPpSrclStaticDiscards_Object = MibTableColumn
mscVrPpSrclStaticDiscards = _MscVrPpSrclStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 12),
    _MscVrPpSrclStaticDiscards_Type()
)
mscVrPpSrclStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclStaticDiscards.setStatus("mandatory")
_MscVrPpSrclDynamicDiscards_Type = Counter32
_MscVrPpSrclDynamicDiscards_Object = MibTableColumn
mscVrPpSrclDynamicDiscards = _MscVrPpSrclDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 14, 21, 1, 13),
    _MscVrPpSrclDynamicDiscards_Type()
)
mscVrPpSrclDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSrclDynamicDiscards.setStatus("mandatory")
_MscVrBr_ObjectIdentity = ObjectIdentity
mscVrBr = _MscVrBr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5)
)
_MscVrBrRowStatusTable_Object = MibTable
mscVrBrRowStatusTable = _MscVrBrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrBrRowStatusTable.setStatus("mandatory")
_MscVrBrRowStatusEntry_Object = MibTableRow
mscVrBrRowStatusEntry = _MscVrBrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 1, 1)
)
mscVrBrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrRowStatusEntry.setStatus("mandatory")
_MscVrBrRowStatus_Type = RowStatus
_MscVrBrRowStatus_Object = MibTableColumn
mscVrBrRowStatus = _MscVrBrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 1, 1, 1),
    _MscVrBrRowStatus_Type()
)
mscVrBrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrRowStatus.setStatus("mandatory")
_MscVrBrComponentName_Type = DisplayString
_MscVrBrComponentName_Object = MibTableColumn
mscVrBrComponentName = _MscVrBrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 1, 1, 2),
    _MscVrBrComponentName_Type()
)
mscVrBrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrComponentName.setStatus("mandatory")
_MscVrBrStorageType_Type = StorageType
_MscVrBrStorageType_Object = MibTableColumn
mscVrBrStorageType = _MscVrBrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 1, 1, 4),
    _MscVrBrStorageType_Type()
)
mscVrBrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrStorageType.setStatus("mandatory")
_MscVrBrIndex_Type = NonReplicated
_MscVrBrIndex_Object = MibTableColumn
mscVrBrIndex = _MscVrBrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 1, 1, 10),
    _MscVrBrIndex_Type()
)
mscVrBrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrIndex.setStatus("mandatory")
_MscVrBrPte_ObjectIdentity = ObjectIdentity
mscVrBrPte = _MscVrBrPte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2)
)
_MscVrBrPteRowStatusTable_Object = MibTable
mscVrBrPteRowStatusTable = _MscVrBrPteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrBrPteRowStatusTable.setStatus("mandatory")
_MscVrBrPteRowStatusEntry_Object = MibTableRow
mscVrBrPteRowStatusEntry = _MscVrBrPteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1)
)
mscVrBrPteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPteDomainNumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPtePortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPteModeIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrPteRowStatusEntry.setStatus("mandatory")
_MscVrBrPteRowStatus_Type = RowStatus
_MscVrBrPteRowStatus_Object = MibTableColumn
mscVrBrPteRowStatus = _MscVrBrPteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1, 1),
    _MscVrBrPteRowStatus_Type()
)
mscVrBrPteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteRowStatus.setStatus("mandatory")
_MscVrBrPteComponentName_Type = DisplayString
_MscVrBrPteComponentName_Object = MibTableColumn
mscVrBrPteComponentName = _MscVrBrPteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1, 2),
    _MscVrBrPteComponentName_Type()
)
mscVrBrPteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteComponentName.setStatus("mandatory")
_MscVrBrPteStorageType_Type = StorageType
_MscVrBrPteStorageType_Object = MibTableColumn
mscVrBrPteStorageType = _MscVrBrPteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1, 4),
    _MscVrBrPteStorageType_Type()
)
mscVrBrPteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteStorageType.setStatus("mandatory")


class _MscVrBrPteDomainNumIndex_Type(Integer32):
    """Custom type mscVrBrPteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrBrPteDomainNumIndex_Type.__name__ = "Integer32"
_MscVrBrPteDomainNumIndex_Object = MibTableColumn
mscVrBrPteDomainNumIndex = _MscVrBrPteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1, 10),
    _MscVrBrPteDomainNumIndex_Type()
)
mscVrBrPteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrPteDomainNumIndex.setStatus("mandatory")


class _MscVrBrPtePortNameIndex_Type(AsciiStringIndex):
    """Custom type mscVrBrPtePortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_MscVrBrPtePortNameIndex_Type.__name__ = "AsciiStringIndex"
_MscVrBrPtePortNameIndex_Object = MibTableColumn
mscVrBrPtePortNameIndex = _MscVrBrPtePortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1, 11),
    _MscVrBrPtePortNameIndex_Type()
)
mscVrBrPtePortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrPtePortNameIndex.setStatus("mandatory")


class _MscVrBrPteModeIndex_Type(Integer32):
    """Custom type mscVrBrPteModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sr", 3),
          ("srt", 4),
          ("tb", 2))
    )


_MscVrBrPteModeIndex_Type.__name__ = "Integer32"
_MscVrBrPteModeIndex_Object = MibTableColumn
mscVrBrPteModeIndex = _MscVrBrPteModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 1, 1, 12),
    _MscVrBrPteModeIndex_Type()
)
mscVrBrPteModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrPteModeIndex.setStatus("mandatory")
_MscVrBrPteOperTable_Object = MibTable
mscVrBrPteOperTable = _MscVrBrPteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrBrPteOperTable.setStatus("mandatory")
_MscVrBrPteOperEntry_Object = MibTableRow
mscVrBrPteOperEntry = _MscVrBrPteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10, 1)
)
mscVrBrPteOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPteDomainNumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPtePortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPteModeIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrPteOperEntry.setStatus("mandatory")


class _MscVrBrPteMacType_Type(Integer32):
    """Custom type mscVrBrPteMacType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("atmMpe", 20),
          ("clusterSr", 17),
          ("clusterTb", 18),
          ("ethernet", 0),
          ("fddiBridgePort", 2),
          ("fddiEncapsulating", 4),
          ("frameRelay", 6),
          ("lecEthernet", 22),
          ("ppp", 7),
          ("smds", 8),
          ("snaDlr", 21),
          ("sourceGateSr", 13),
          ("sourceGateTb", 14),
          ("srEncapSr", 11),
          ("srEncapTb", 12),
          ("srtb", 15),
          ("tbsr", 16),
          ("tokenBus", 3),
          ("tokenRing", 1),
          ("unknown", 19),
          ("vcp", 9),
          ("vns", 5),
          ("x25", 10))
    )


_MscVrBrPteMacType_Type.__name__ = "Integer32"
_MscVrBrPteMacType_Object = MibTableColumn
mscVrBrPteMacType = _MscVrBrPteMacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10, 1, 1),
    _MscVrBrPteMacType_Type()
)
mscVrBrPteMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteMacType.setStatus("mandatory")


class _MscVrBrPteStpState_Type(Integer32):
    """Custom type mscVrBrPteStpState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MscVrBrPteStpState_Type.__name__ = "Integer32"
_MscVrBrPteStpState_Object = MibTableColumn
mscVrBrPteStpState = _MscVrBrPteStpState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10, 1, 2),
    _MscVrBrPteStpState_Type()
)
mscVrBrPteStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteStpState.setStatus("mandatory")


class _MscVrBrPteStpType_Type(Integer32):
    """Custom type mscVrBrPteStpType based on Integer32"""
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
        *(("dec", 2),
          ("ieee8021", 3),
          ("unknown", 1))
    )


_MscVrBrPteStpType_Type.__name__ = "Integer32"
_MscVrBrPteStpType_Object = MibTableColumn
mscVrBrPteStpType = _MscVrBrPteStpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10, 1, 3),
    _MscVrBrPteStpType_Type()
)
mscVrBrPteStpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteStpType.setStatus("mandatory")


class _MscVrBrPteFilterPoints_Type(Integer32):
    """Custom type mscVrBrPteFilterPoints based on Integer32"""
    defaultValue = 4

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
        *(("in", 1),
          ("inOut", 3),
          ("none", 4),
          ("out", 2))
    )


_MscVrBrPteFilterPoints_Type.__name__ = "Integer32"
_MscVrBrPteFilterPoints_Object = MibTableColumn
mscVrBrPteFilterPoints = _MscVrBrPteFilterPoints_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10, 1, 4),
    _MscVrBrPteFilterPoints_Type()
)
mscVrBrPteFilterPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteFilterPoints.setStatus("mandatory")


class _MscVrBrPtePortPointsTo_Type(Integer32):
    """Custom type mscVrBrPtePortPointsTo based on Integer32"""
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
        *(("designatedBridge", 3),
          ("none", 1),
          ("rootBridge", 2))
    )


_MscVrBrPtePortPointsTo_Type.__name__ = "Integer32"
_MscVrBrPtePortPointsTo_Object = MibTableColumn
mscVrBrPtePortPointsTo = _MscVrBrPtePortPointsTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 10, 1, 5),
    _MscVrBrPtePortPointsTo_Type()
)
mscVrBrPtePortPointsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPtePortPointsTo.setStatus("mandatory")
_MscVrBrPteSpOperTable_Object = MibTable
mscVrBrPteSpOperTable = _MscVrBrPteSpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrBrPteSpOperTable.setStatus("mandatory")
_MscVrBrPteSpOperEntry_Object = MibTableRow
mscVrBrPteSpOperEntry = _MscVrBrPteSpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 11, 1)
)
mscVrBrPteSpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPteDomainNumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPtePortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrPteModeIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrPteSpOperEntry.setStatus("mandatory")


class _MscVrBrPteLanId_Type(Unsigned32):
    """Custom type mscVrBrPteLanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscVrBrPteLanId_Type.__name__ = "Unsigned32"
_MscVrBrPteLanId_Object = MibTableColumn
mscVrBrPteLanId = _MscVrBrPteLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 11, 1, 1),
    _MscVrBrPteLanId_Type()
)
mscVrBrPteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteLanId.setStatus("mandatory")


class _MscVrBrPteInternalLanId_Type(Unsigned32):
    """Custom type mscVrBrPteInternalLanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscVrBrPteInternalLanId_Type.__name__ = "Unsigned32"
_MscVrBrPteInternalLanId_Object = MibTableColumn
mscVrBrPteInternalLanId = _MscVrBrPteInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 11, 1, 2),
    _MscVrBrPteInternalLanId_Type()
)
mscVrBrPteInternalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteInternalLanId.setStatus("mandatory")


class _MscVrBrPteBridgeNum_Type(Unsigned32):
    """Custom type mscVrBrPteBridgeNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(65535, 65535),
    )


_MscVrBrPteBridgeNum_Type.__name__ = "Unsigned32"
_MscVrBrPteBridgeNum_Object = MibTableColumn
mscVrBrPteBridgeNum = _MscVrBrPteBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 2, 11, 1, 3),
    _MscVrBrPteBridgeNum_Type()
)
mscVrBrPteBridgeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrPteBridgeNum.setStatus("mandatory")
_MscVrBrNs_ObjectIdentity = ObjectIdentity
mscVrBrNs = _MscVrBrNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3)
)
_MscVrBrNsRowStatusTable_Object = MibTable
mscVrBrNsRowStatusTable = _MscVrBrNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrBrNsRowStatusTable.setStatus("mandatory")
_MscVrBrNsRowStatusEntry_Object = MibTableRow
mscVrBrNsRowStatusEntry = _MscVrBrNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 1, 1)
)
mscVrBrNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrNsRowStatusEntry.setStatus("mandatory")
_MscVrBrNsRowStatus_Type = RowStatus
_MscVrBrNsRowStatus_Object = MibTableColumn
mscVrBrNsRowStatus = _MscVrBrNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 1, 1, 1),
    _MscVrBrNsRowStatus_Type()
)
mscVrBrNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsRowStatus.setStatus("mandatory")
_MscVrBrNsComponentName_Type = DisplayString
_MscVrBrNsComponentName_Object = MibTableColumn
mscVrBrNsComponentName = _MscVrBrNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 1, 1, 2),
    _MscVrBrNsComponentName_Type()
)
mscVrBrNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrNsComponentName.setStatus("mandatory")
_MscVrBrNsStorageType_Type = StorageType
_MscVrBrNsStorageType_Object = MibTableColumn
mscVrBrNsStorageType = _MscVrBrNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 1, 1, 4),
    _MscVrBrNsStorageType_Type()
)
mscVrBrNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrNsStorageType.setStatus("mandatory")
_MscVrBrNsIndex_Type = NonReplicated
_MscVrBrNsIndex_Object = MibTableColumn
mscVrBrNsIndex = _MscVrBrNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 1, 1, 10),
    _MscVrBrNsIndex_Type()
)
mscVrBrNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrNsIndex.setStatus("mandatory")
_MscVrBrNsAte_ObjectIdentity = ObjectIdentity
mscVrBrNsAte = _MscVrBrNsAte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2)
)
_MscVrBrNsAteRowStatusTable_Object = MibTable
mscVrBrNsAteRowStatusTable = _MscVrBrNsAteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrBrNsAteRowStatusTable.setStatus("mandatory")
_MscVrBrNsAteRowStatusEntry_Object = MibTableRow
mscVrBrNsAteRowStatusEntry = _MscVrBrNsAteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 1, 1)
)
mscVrBrNsAteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrNsAteEntryNumberIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrNsAteRowStatusEntry.setStatus("mandatory")
_MscVrBrNsAteRowStatus_Type = RowStatus
_MscVrBrNsAteRowStatus_Object = MibTableColumn
mscVrBrNsAteRowStatus = _MscVrBrNsAteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 1, 1, 1),
    _MscVrBrNsAteRowStatus_Type()
)
mscVrBrNsAteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteRowStatus.setStatus("mandatory")
_MscVrBrNsAteComponentName_Type = DisplayString
_MscVrBrNsAteComponentName_Object = MibTableColumn
mscVrBrNsAteComponentName = _MscVrBrNsAteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 1, 1, 2),
    _MscVrBrNsAteComponentName_Type()
)
mscVrBrNsAteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrNsAteComponentName.setStatus("mandatory")
_MscVrBrNsAteStorageType_Type = StorageType
_MscVrBrNsAteStorageType_Object = MibTableColumn
mscVrBrNsAteStorageType = _MscVrBrNsAteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 1, 1, 4),
    _MscVrBrNsAteStorageType_Type()
)
mscVrBrNsAteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrNsAteStorageType.setStatus("mandatory")


class _MscVrBrNsAteEntryNumberIndex_Type(Integer32):
    """Custom type mscVrBrNsAteEntryNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrBrNsAteEntryNumberIndex_Type.__name__ = "Integer32"
_MscVrBrNsAteEntryNumberIndex_Object = MibTableColumn
mscVrBrNsAteEntryNumberIndex = _MscVrBrNsAteEntryNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 1, 1, 10),
    _MscVrBrNsAteEntryNumberIndex_Type()
)
mscVrBrNsAteEntryNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrNsAteEntryNumberIndex.setStatus("mandatory")
_MscVrBrNsAteProvTable_Object = MibTable
mscVrBrNsAteProvTable = _MscVrBrNsAteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrBrNsAteProvTable.setStatus("mandatory")
_MscVrBrNsAteProvEntry_Object = MibTableRow
mscVrBrNsAteProvEntry = _MscVrBrNsAteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1)
)
mscVrBrNsAteProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrNsAteEntryNumberIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrNsAteProvEntry.setStatus("mandatory")


class _MscVrBrNsAteDomainNum_Type(Unsigned32):
    """Custom type mscVrBrNsAteDomainNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_MscVrBrNsAteDomainNum_Type.__name__ = "Unsigned32"
_MscVrBrNsAteDomainNum_Object = MibTableColumn
mscVrBrNsAteDomainNum = _MscVrBrNsAteDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 1),
    _MscVrBrNsAteDomainNum_Type()
)
mscVrBrNsAteDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteDomainNum.setStatus("mandatory")


class _MscVrBrNsAteFirstMacAddress_Type(MacAddress):
    """Custom type mscVrBrNsAteFirstMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrNsAteFirstMacAddress_Type.__name__ = "MacAddress"
_MscVrBrNsAteFirstMacAddress_Object = MibTableColumn
mscVrBrNsAteFirstMacAddress = _MscVrBrNsAteFirstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 2),
    _MscVrBrNsAteFirstMacAddress_Type()
)
mscVrBrNsAteFirstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteFirstMacAddress.setStatus("mandatory")


class _MscVrBrNsAteFirstMacAddressMask_Type(MacAddress):
    """Custom type mscVrBrNsAteFirstMacAddressMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrNsAteFirstMacAddressMask_Type.__name__ = "MacAddress"
_MscVrBrNsAteFirstMacAddressMask_Object = MibTableColumn
mscVrBrNsAteFirstMacAddressMask = _MscVrBrNsAteFirstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 3),
    _MscVrBrNsAteFirstMacAddressMask_Type()
)
mscVrBrNsAteFirstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteFirstMacAddressMask.setStatus("mandatory")


class _MscVrBrNsAteSecondMacAddress_Type(MacAddress):
    """Custom type mscVrBrNsAteSecondMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrNsAteSecondMacAddress_Type.__name__ = "MacAddress"
_MscVrBrNsAteSecondMacAddress_Object = MibTableColumn
mscVrBrNsAteSecondMacAddress = _MscVrBrNsAteSecondMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 4),
    _MscVrBrNsAteSecondMacAddress_Type()
)
mscVrBrNsAteSecondMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteSecondMacAddress.setStatus("mandatory")


class _MscVrBrNsAteSecondMacAddressMask_Type(MacAddress):
    """Custom type mscVrBrNsAteSecondMacAddressMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrNsAteSecondMacAddressMask_Type.__name__ = "MacAddress"
_MscVrBrNsAteSecondMacAddressMask_Object = MibTableColumn
mscVrBrNsAteSecondMacAddressMask = _MscVrBrNsAteSecondMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 5),
    _MscVrBrNsAteSecondMacAddressMask_Type()
)
mscVrBrNsAteSecondMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteSecondMacAddressMask.setStatus("mandatory")


class _MscVrBrNsAteDirection_Type(Integer32):
    """Custom type mscVrBrNsAteDirection based on Integer32"""
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
        *(("from", 1),
          ("to", 0),
          ("toFrom", 2))
    )


_MscVrBrNsAteDirection_Type.__name__ = "Integer32"
_MscVrBrNsAteDirection_Object = MibTableColumn
mscVrBrNsAteDirection = _MscVrBrNsAteDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 6),
    _MscVrBrNsAteDirection_Type()
)
mscVrBrNsAteDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteDirection.setStatus("mandatory")


class _MscVrBrNsAteFilterName_Type(AsciiString):
    """Custom type mscVrBrNsAteFilterName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrBrNsAteFilterName_Type.__name__ = "AsciiString"
_MscVrBrNsAteFilterName_Object = MibTableColumn
mscVrBrNsAteFilterName = _MscVrBrNsAteFilterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 2, 10, 1, 7),
    _MscVrBrNsAteFilterName_Type()
)
mscVrBrNsAteFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsAteFilterName.setStatus("mandatory")
_MscVrBrNsProvTable_Object = MibTable
mscVrBrNsProvTable = _MscVrBrNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrBrNsProvTable.setStatus("mandatory")
_MscVrBrNsProvEntry_Object = MibTableRow
mscVrBrNsProvEntry = _MscVrBrNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 10, 1)
)
mscVrBrNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrNsProvEntry.setStatus("mandatory")


class _MscVrBrNsFirstFilter_Type(AsciiString):
    """Custom type mscVrBrNsFirstFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrBrNsFirstFilter_Type.__name__ = "AsciiString"
_MscVrBrNsFirstFilter_Object = MibTableColumn
mscVrBrNsFirstFilter = _MscVrBrNsFirstFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 10, 1, 1),
    _MscVrBrNsFirstFilter_Type()
)
mscVrBrNsFirstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsFirstFilter.setStatus("mandatory")


class _MscVrBrNsLastFilter_Type(AsciiString):
    """Custom type mscVrBrNsLastFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrBrNsLastFilter_Type.__name__ = "AsciiString"
_MscVrBrNsLastFilter_Object = MibTableColumn
mscVrBrNsLastFilter = _MscVrBrNsLastFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 3, 10, 1, 2),
    _MscVrBrNsLastFilter_Type()
)
mscVrBrNsLastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrNsLastFilter.setStatus("mandatory")
_MscVrBrTb_ObjectIdentity = ObjectIdentity
mscVrBrTb = _MscVrBrTb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4)
)
_MscVrBrTbRowStatusTable_Object = MibTable
mscVrBrTbRowStatusTable = _MscVrBrTbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrBrTbRowStatusTable.setStatus("mandatory")
_MscVrBrTbRowStatusEntry_Object = MibTableRow
mscVrBrTbRowStatusEntry = _MscVrBrTbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 1, 1)
)
mscVrBrTbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbRowStatusEntry.setStatus("mandatory")
_MscVrBrTbRowStatus_Type = RowStatus
_MscVrBrTbRowStatus_Object = MibTableColumn
mscVrBrTbRowStatus = _MscVrBrTbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 1, 1, 1),
    _MscVrBrTbRowStatus_Type()
)
mscVrBrTbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbRowStatus.setStatus("mandatory")
_MscVrBrTbComponentName_Type = DisplayString
_MscVrBrTbComponentName_Object = MibTableColumn
mscVrBrTbComponentName = _MscVrBrTbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 1, 1, 2),
    _MscVrBrTbComponentName_Type()
)
mscVrBrTbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbComponentName.setStatus("mandatory")
_MscVrBrTbStorageType_Type = StorageType
_MscVrBrTbStorageType_Object = MibTableColumn
mscVrBrTbStorageType = _MscVrBrTbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 1, 1, 4),
    _MscVrBrTbStorageType_Type()
)
mscVrBrTbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStorageType.setStatus("mandatory")
_MscVrBrTbIndex_Type = NonReplicated
_MscVrBrTbIndex_Object = MibTableColumn
mscVrBrTbIndex = _MscVrBrTbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 1, 1, 10),
    _MscVrBrTbIndex_Type()
)
mscVrBrTbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbIndex.setStatus("mandatory")
_MscVrBrTbStp_ObjectIdentity = ObjectIdentity
mscVrBrTbStp = _MscVrBrTbStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2)
)
_MscVrBrTbStpRowStatusTable_Object = MibTable
mscVrBrTbStpRowStatusTable = _MscVrBrTbStpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrBrTbStpRowStatusTable.setStatus("mandatory")
_MscVrBrTbStpRowStatusEntry_Object = MibTableRow
mscVrBrTbStpRowStatusEntry = _MscVrBrTbStpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 1, 1)
)
mscVrBrTbStpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbStpIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbStpRowStatusEntry.setStatus("mandatory")
_MscVrBrTbStpRowStatus_Type = RowStatus
_MscVrBrTbStpRowStatus_Object = MibTableColumn
mscVrBrTbStpRowStatus = _MscVrBrTbStpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 1, 1, 1),
    _MscVrBrTbStpRowStatus_Type()
)
mscVrBrTbStpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpRowStatus.setStatus("mandatory")
_MscVrBrTbStpComponentName_Type = DisplayString
_MscVrBrTbStpComponentName_Object = MibTableColumn
mscVrBrTbStpComponentName = _MscVrBrTbStpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 1, 1, 2),
    _MscVrBrTbStpComponentName_Type()
)
mscVrBrTbStpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpComponentName.setStatus("mandatory")
_MscVrBrTbStpStorageType_Type = StorageType
_MscVrBrTbStpStorageType_Object = MibTableColumn
mscVrBrTbStpStorageType = _MscVrBrTbStpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 1, 1, 4),
    _MscVrBrTbStpStorageType_Type()
)
mscVrBrTbStpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpStorageType.setStatus("mandatory")


class _MscVrBrTbStpIndex_Type(Integer32):
    """Custom type mscVrBrTbStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrBrTbStpIndex_Type.__name__ = "Integer32"
_MscVrBrTbStpIndex_Object = MibTableColumn
mscVrBrTbStpIndex = _MscVrBrTbStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 1, 1, 10),
    _MscVrBrTbStpIndex_Type()
)
mscVrBrTbStpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbStpIndex.setStatus("mandatory")
_MscVrBrTbStpProvTable_Object = MibTable
mscVrBrTbStpProvTable = _MscVrBrTbStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrBrTbStpProvTable.setStatus("mandatory")
_MscVrBrTbStpProvEntry_Object = MibTableRow
mscVrBrTbStpProvEntry = _MscVrBrTbStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1)
)
mscVrBrTbStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbStpIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbStpProvEntry.setStatus("mandatory")


class _MscVrBrTbStpStpMode_Type(Integer32):
    """Custom type mscVrBrTbStpStpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrBrTbStpStpMode_Type.__name__ = "Integer32"
_MscVrBrTbStpStpMode_Object = MibTableColumn
mscVrBrTbStpStpMode = _MscVrBrTbStpStpMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1, 1),
    _MscVrBrTbStpStpMode_Type()
)
mscVrBrTbStpStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpStpMode.setStatus("mandatory")


class _MscVrBrTbStpProtocolSpec_Type(Integer32):
    """Custom type mscVrBrTbStpProtocolSpec based on Integer32"""
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
        *(("both", 1),
          ("dec", 2),
          ("ieee8021d", 3))
    )


_MscVrBrTbStpProtocolSpec_Type.__name__ = "Integer32"
_MscVrBrTbStpProtocolSpec_Object = MibTableColumn
mscVrBrTbStpProtocolSpec = _MscVrBrTbStpProtocolSpec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1, 2),
    _MscVrBrTbStpProtocolSpec_Type()
)
mscVrBrTbStpProtocolSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpProtocolSpec.setStatus("mandatory")


class _MscVrBrTbStpPriority_Type(Unsigned32):
    """Custom type mscVrBrTbStpPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrBrTbStpPriority_Type.__name__ = "Unsigned32"
_MscVrBrTbStpPriority_Object = MibTableColumn
mscVrBrTbStpPriority = _MscVrBrTbStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1, 3),
    _MscVrBrTbStpPriority_Type()
)
mscVrBrTbStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpPriority.setStatus("mandatory")


class _MscVrBrTbStpBridgeMaxAge_Type(Unsigned32):
    """Custom type mscVrBrTbStpBridgeMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MscVrBrTbStpBridgeMaxAge_Type.__name__ = "Unsigned32"
_MscVrBrTbStpBridgeMaxAge_Object = MibTableColumn
mscVrBrTbStpBridgeMaxAge = _MscVrBrTbStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1, 4),
    _MscVrBrTbStpBridgeMaxAge_Type()
)
mscVrBrTbStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpBridgeMaxAge.setStatus("mandatory")


class _MscVrBrTbStpBridgeHelloTime_Type(Unsigned32):
    """Custom type mscVrBrTbStpBridgeHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MscVrBrTbStpBridgeHelloTime_Type.__name__ = "Unsigned32"
_MscVrBrTbStpBridgeHelloTime_Object = MibTableColumn
mscVrBrTbStpBridgeHelloTime = _MscVrBrTbStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1, 5),
    _MscVrBrTbStpBridgeHelloTime_Type()
)
mscVrBrTbStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpBridgeHelloTime.setStatus("mandatory")


class _MscVrBrTbStpBridgeForwardDelay_Type(Unsigned32):
    """Custom type mscVrBrTbStpBridgeForwardDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MscVrBrTbStpBridgeForwardDelay_Type.__name__ = "Unsigned32"
_MscVrBrTbStpBridgeForwardDelay_Object = MibTableColumn
mscVrBrTbStpBridgeForwardDelay = _MscVrBrTbStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 10, 1, 6),
    _MscVrBrTbStpBridgeForwardDelay_Type()
)
mscVrBrTbStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbStpBridgeForwardDelay.setStatus("mandatory")
_MscVrBrTbStpOperTable_Object = MibTable
mscVrBrTbStpOperTable = _MscVrBrTbStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrBrTbStpOperTable.setStatus("mandatory")
_MscVrBrTbStpOperEntry_Object = MibTableRow
mscVrBrTbStpOperEntry = _MscVrBrTbStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1)
)
mscVrBrTbStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbStpIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbStpOperEntry.setStatus("mandatory")


class _MscVrBrTbStpBridgeId_Type(BridgeId):
    """Custom type mscVrBrTbStpBridgeId based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrBrTbStpBridgeId_Type.__name__ = "BridgeId"
_MscVrBrTbStpBridgeId_Object = MibTableColumn
mscVrBrTbStpBridgeId = _MscVrBrTbStpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 1),
    _MscVrBrTbStpBridgeId_Type()
)
mscVrBrTbStpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpBridgeId.setStatus("mandatory")


class _MscVrBrTbStpRootPortName_Type(AsciiString):
    """Custom type mscVrBrTbStpRootPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrBrTbStpRootPortName_Type.__name__ = "AsciiString"
_MscVrBrTbStpRootPortName_Object = MibTableColumn
mscVrBrTbStpRootPortName = _MscVrBrTbStpRootPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 2),
    _MscVrBrTbStpRootPortName_Type()
)
mscVrBrTbStpRootPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpRootPortName.setStatus("mandatory")


class _MscVrBrTbStpTimeSinceTopologyChange_Type(Unsigned32):
    """Custom type mscVrBrTbStpTimeSinceTopologyChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrBrTbStpTimeSinceTopologyChange_Type.__name__ = "Unsigned32"
_MscVrBrTbStpTimeSinceTopologyChange_Object = MibTableColumn
mscVrBrTbStpTimeSinceTopologyChange = _MscVrBrTbStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 3),
    _MscVrBrTbStpTimeSinceTopologyChange_Type()
)
mscVrBrTbStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpTimeSinceTopologyChange.setStatus("mandatory")


class _MscVrBrTbStpTopologyChangeDetect_Type(Integer32):
    """Custom type mscVrBrTbStpTopologyChangeDetect based on Integer32"""
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


_MscVrBrTbStpTopologyChangeDetect_Type.__name__ = "Integer32"
_MscVrBrTbStpTopologyChangeDetect_Object = MibTableColumn
mscVrBrTbStpTopologyChangeDetect = _MscVrBrTbStpTopologyChangeDetect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 4),
    _MscVrBrTbStpTopologyChangeDetect_Type()
)
mscVrBrTbStpTopologyChangeDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpTopologyChangeDetect.setStatus("mandatory")
_MscVrBrTbStpTopologyChanges_Type = Counter32
_MscVrBrTbStpTopologyChanges_Object = MibTableColumn
mscVrBrTbStpTopologyChanges = _MscVrBrTbStpTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 5),
    _MscVrBrTbStpTopologyChanges_Type()
)
mscVrBrTbStpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpTopologyChanges.setStatus("mandatory")


class _MscVrBrTbStpDesignatedRoot_Type(BridgeId):
    """Custom type mscVrBrTbStpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrBrTbStpDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrBrTbStpDesignatedRoot_Object = MibTableColumn
mscVrBrTbStpDesignatedRoot = _MscVrBrTbStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 6),
    _MscVrBrTbStpDesignatedRoot_Type()
)
mscVrBrTbStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpDesignatedRoot.setStatus("mandatory")


class _MscVrBrTbStpRootCost_Type(Unsigned32):
    """Custom type mscVrBrTbStpRootCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrBrTbStpRootCost_Type.__name__ = "Unsigned32"
_MscVrBrTbStpRootCost_Object = MibTableColumn
mscVrBrTbStpRootCost = _MscVrBrTbStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 8),
    _MscVrBrTbStpRootCost_Type()
)
mscVrBrTbStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpRootCost.setStatus("mandatory")


class _MscVrBrTbStpMaxAge_Type(Unsigned32):
    """Custom type mscVrBrTbStpMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MscVrBrTbStpMaxAge_Type.__name__ = "Unsigned32"
_MscVrBrTbStpMaxAge_Object = MibTableColumn
mscVrBrTbStpMaxAge = _MscVrBrTbStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 9),
    _MscVrBrTbStpMaxAge_Type()
)
mscVrBrTbStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpMaxAge.setStatus("mandatory")


class _MscVrBrTbStpAgingTimeOper_Type(Unsigned32):
    """Custom type mscVrBrTbStpAgingTimeOper based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MscVrBrTbStpAgingTimeOper_Type.__name__ = "Unsigned32"
_MscVrBrTbStpAgingTimeOper_Object = MibTableColumn
mscVrBrTbStpAgingTimeOper = _MscVrBrTbStpAgingTimeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 10),
    _MscVrBrTbStpAgingTimeOper_Type()
)
mscVrBrTbStpAgingTimeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpAgingTimeOper.setStatus("mandatory")


class _MscVrBrTbStpHelloTime_Type(Unsigned32):
    """Custom type mscVrBrTbStpHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MscVrBrTbStpHelloTime_Type.__name__ = "Unsigned32"
_MscVrBrTbStpHelloTime_Object = MibTableColumn
mscVrBrTbStpHelloTime = _MscVrBrTbStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 11),
    _MscVrBrTbStpHelloTime_Type()
)
mscVrBrTbStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpHelloTime.setStatus("mandatory")


class _MscVrBrTbStpHoldTime_Type(Unsigned32):
    """Custom type mscVrBrTbStpHoldTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
    )


_MscVrBrTbStpHoldTime_Type.__name__ = "Unsigned32"
_MscVrBrTbStpHoldTime_Object = MibTableColumn
mscVrBrTbStpHoldTime = _MscVrBrTbStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 12),
    _MscVrBrTbStpHoldTime_Type()
)
mscVrBrTbStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpHoldTime.setStatus("mandatory")


class _MscVrBrTbStpFwdDelay_Type(Unsigned32):
    """Custom type mscVrBrTbStpFwdDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MscVrBrTbStpFwdDelay_Type.__name__ = "Unsigned32"
_MscVrBrTbStpFwdDelay_Object = MibTableColumn
mscVrBrTbStpFwdDelay = _MscVrBrTbStpFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 2, 11, 1, 13),
    _MscVrBrTbStpFwdDelay_Type()
)
mscVrBrTbStpFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbStpFwdDelay.setStatus("mandatory")
_MscVrBrTbSte_ObjectIdentity = ObjectIdentity
mscVrBrTbSte = _MscVrBrTbSte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3)
)
_MscVrBrTbSteRowStatusTable_Object = MibTable
mscVrBrTbSteRowStatusTable = _MscVrBrTbSteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrBrTbSteRowStatusTable.setStatus("mandatory")
_MscVrBrTbSteRowStatusEntry_Object = MibTableRow
mscVrBrTbSteRowStatusEntry = _MscVrBrTbSteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1, 1)
)
mscVrBrTbSteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteReceivePortIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbSteRowStatusEntry.setStatus("mandatory")
_MscVrBrTbSteRowStatus_Type = RowStatus
_MscVrBrTbSteRowStatus_Object = MibTableColumn
mscVrBrTbSteRowStatus = _MscVrBrTbSteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1, 1, 1),
    _MscVrBrTbSteRowStatus_Type()
)
mscVrBrTbSteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbSteRowStatus.setStatus("mandatory")
_MscVrBrTbSteComponentName_Type = DisplayString
_MscVrBrTbSteComponentName_Object = MibTableColumn
mscVrBrTbSteComponentName = _MscVrBrTbSteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1, 1, 2),
    _MscVrBrTbSteComponentName_Type()
)
mscVrBrTbSteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbSteComponentName.setStatus("mandatory")
_MscVrBrTbSteStorageType_Type = StorageType
_MscVrBrTbSteStorageType_Object = MibTableColumn
mscVrBrTbSteStorageType = _MscVrBrTbSteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1, 1, 4),
    _MscVrBrTbSteStorageType_Type()
)
mscVrBrTbSteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbSteStorageType.setStatus("mandatory")


class _MscVrBrTbSteAddressIndex_Type(DashedHexString):
    """Custom type mscVrBrTbSteAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrTbSteAddressIndex_Type.__name__ = "DashedHexString"
_MscVrBrTbSteAddressIndex_Object = MibTableColumn
mscVrBrTbSteAddressIndex = _MscVrBrTbSteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1, 1, 10),
    _MscVrBrTbSteAddressIndex_Type()
)
mscVrBrTbSteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbSteAddressIndex.setStatus("mandatory")


class _MscVrBrTbSteReceivePortIndex_Type(AsciiStringIndex):
    """Custom type mscVrBrTbSteReceivePortIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 29),
    )


_MscVrBrTbSteReceivePortIndex_Type.__name__ = "AsciiStringIndex"
_MscVrBrTbSteReceivePortIndex_Object = MibTableColumn
mscVrBrTbSteReceivePortIndex = _MscVrBrTbSteReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 1, 1, 11),
    _MscVrBrTbSteReceivePortIndex_Type()
)
mscVrBrTbSteReceivePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbSteReceivePortIndex.setStatus("mandatory")
_MscVrBrTbSteProvTable_Object = MibTable
mscVrBrTbSteProvTable = _MscVrBrTbSteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrBrTbSteProvTable.setStatus("mandatory")
_MscVrBrTbSteProvEntry_Object = MibTableRow
mscVrBrTbSteProvEntry = _MscVrBrTbSteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 10, 1)
)
mscVrBrTbSteProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteReceivePortIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbSteProvEntry.setStatus("mandatory")


class _MscVrBrTbSteStatus_Type(Integer32):
    """Custom type mscVrBrTbSteStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("permanent", 3)
    )


_MscVrBrTbSteStatus_Type.__name__ = "Integer32"
_MscVrBrTbSteStatus_Object = MibTableColumn
mscVrBrTbSteStatus = _MscVrBrTbSteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 10, 1, 1),
    _MscVrBrTbSteStatus_Type()
)
mscVrBrTbSteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbSteStatus.setStatus("mandatory")
_MscVrBrTbSteAtgtTable_Object = MibTable
mscVrBrTbSteAtgtTable = _MscVrBrTbSteAtgtTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 271)
)
if mibBuilder.loadTexts:
    mscVrBrTbSteAtgtTable.setStatus("mandatory")
_MscVrBrTbSteAtgtEntry_Object = MibTableRow
mscVrBrTbSteAtgtEntry = _MscVrBrTbSteAtgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 271, 1)
)
mscVrBrTbSteAtgtEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteReceivePortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbSteAtgtValue"),
)
if mibBuilder.loadTexts:
    mscVrBrTbSteAtgtEntry.setStatus("mandatory")


class _MscVrBrTbSteAtgtValue_Type(AsciiString):
    """Custom type mscVrBrTbSteAtgtValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrBrTbSteAtgtValue_Type.__name__ = "AsciiString"
_MscVrBrTbSteAtgtValue_Object = MibTableColumn
mscVrBrTbSteAtgtValue = _MscVrBrTbSteAtgtValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 271, 1, 1),
    _MscVrBrTbSteAtgtValue_Type()
)
mscVrBrTbSteAtgtValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbSteAtgtValue.setStatus("mandatory")
_MscVrBrTbSteAtgtRowStatus_Type = RowStatus
_MscVrBrTbSteAtgtRowStatus_Object = MibTableColumn
mscVrBrTbSteAtgtRowStatus = _MscVrBrTbSteAtgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 3, 271, 1, 2),
    _MscVrBrTbSteAtgtRowStatus_Type()
)
mscVrBrTbSteAtgtRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrBrTbSteAtgtRowStatus.setStatus("mandatory")
_MscVrBrTbFte_ObjectIdentity = ObjectIdentity
mscVrBrTbFte = _MscVrBrTbFte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4)
)
_MscVrBrTbFteRowStatusTable_Object = MibTable
mscVrBrTbFteRowStatusTable = _MscVrBrTbFteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrBrTbFteRowStatusTable.setStatus("mandatory")
_MscVrBrTbFteRowStatusEntry_Object = MibTableRow
mscVrBrTbFteRowStatusEntry = _MscVrBrTbFteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1, 1)
)
mscVrBrTbFteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbFteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbFteRowStatusEntry.setStatus("mandatory")
_MscVrBrTbFteRowStatus_Type = RowStatus
_MscVrBrTbFteRowStatus_Object = MibTableColumn
mscVrBrTbFteRowStatus = _MscVrBrTbFteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1, 1, 1),
    _MscVrBrTbFteRowStatus_Type()
)
mscVrBrTbFteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFteRowStatus.setStatus("mandatory")
_MscVrBrTbFteComponentName_Type = DisplayString
_MscVrBrTbFteComponentName_Object = MibTableColumn
mscVrBrTbFteComponentName = _MscVrBrTbFteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1, 1, 2),
    _MscVrBrTbFteComponentName_Type()
)
mscVrBrTbFteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFteComponentName.setStatus("mandatory")
_MscVrBrTbFteStorageType_Type = StorageType
_MscVrBrTbFteStorageType_Object = MibTableColumn
mscVrBrTbFteStorageType = _MscVrBrTbFteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1, 1, 4),
    _MscVrBrTbFteStorageType_Type()
)
mscVrBrTbFteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFteStorageType.setStatus("mandatory")


class _MscVrBrTbFteAddressIndex_Type(DashedHexString):
    """Custom type mscVrBrTbFteAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrTbFteAddressIndex_Type.__name__ = "DashedHexString"
_MscVrBrTbFteAddressIndex_Object = MibTableColumn
mscVrBrTbFteAddressIndex = _MscVrBrTbFteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1, 1, 10),
    _MscVrBrTbFteAddressIndex_Type()
)
mscVrBrTbFteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbFteAddressIndex.setStatus("mandatory")


class _MscVrBrTbFteDomainNumIndex_Type(Integer32):
    """Custom type mscVrBrTbFteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrBrTbFteDomainNumIndex_Type.__name__ = "Integer32"
_MscVrBrTbFteDomainNumIndex_Object = MibTableColumn
mscVrBrTbFteDomainNumIndex = _MscVrBrTbFteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 1, 1, 11),
    _MscVrBrTbFteDomainNumIndex_Type()
)
mscVrBrTbFteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbFteDomainNumIndex.setStatus("mandatory")
_MscVrBrTbFteOperTable_Object = MibTable
mscVrBrTbFteOperTable = _MscVrBrTbFteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrBrTbFteOperTable.setStatus("mandatory")
_MscVrBrTbFteOperEntry_Object = MibTableRow
mscVrBrTbFteOperEntry = _MscVrBrTbFteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 10, 1)
)
mscVrBrTbFteOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbFteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbFteOperEntry.setStatus("mandatory")


class _MscVrBrTbFtePort_Type(AsciiString):
    """Custom type mscVrBrTbFtePort based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrBrTbFtePort_Type.__name__ = "AsciiString"
_MscVrBrTbFtePort_Object = MibTableColumn
mscVrBrTbFtePort = _MscVrBrTbFtePort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 10, 1, 3),
    _MscVrBrTbFtePort_Type()
)
mscVrBrTbFtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFtePort.setStatus("mandatory")


class _MscVrBrTbFteAgeOfEntry_Type(Gauge32):
    """Custom type mscVrBrTbFteAgeOfEntry based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscVrBrTbFteAgeOfEntry_Type.__name__ = "Gauge32"
_MscVrBrTbFteAgeOfEntry_Object = MibTableColumn
mscVrBrTbFteAgeOfEntry = _MscVrBrTbFteAgeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 10, 1, 4),
    _MscVrBrTbFteAgeOfEntry_Type()
)
mscVrBrTbFteAgeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFteAgeOfEntry.setStatus("mandatory")


class _MscVrBrTbFtePeerAddressInfo_Type(BridgeId):
    """Custom type mscVrBrTbFtePeerAddressInfo based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrBrTbFtePeerAddressInfo_Type.__name__ = "BridgeId"
_MscVrBrTbFtePeerAddressInfo_Object = MibTableColumn
mscVrBrTbFtePeerAddressInfo = _MscVrBrTbFtePeerAddressInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 10, 1, 5),
    _MscVrBrTbFtePeerAddressInfo_Type()
)
mscVrBrTbFtePeerAddressInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFtePeerAddressInfo.setStatus("mandatory")


class _MscVrBrTbFteStatus_Type(Integer32):
    """Custom type mscVrBrTbFteStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_MscVrBrTbFteStatus_Type.__name__ = "Integer32"
_MscVrBrTbFteStatus_Object = MibTableColumn
mscVrBrTbFteStatus = _MscVrBrTbFteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 4, 10, 1, 6),
    _MscVrBrTbFteStatus_Type()
)
mscVrBrTbFteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbFteStatus.setStatus("mandatory")
_MscVrBrTbNcFte_ObjectIdentity = ObjectIdentity
mscVrBrTbNcFte = _MscVrBrTbNcFte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5)
)
_MscVrBrTbNcFteRowStatusTable_Object = MibTable
mscVrBrTbNcFteRowStatusTable = _MscVrBrTbNcFteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrBrTbNcFteRowStatusTable.setStatus("mandatory")
_MscVrBrTbNcFteRowStatusEntry_Object = MibTableRow
mscVrBrTbNcFteRowStatusEntry = _MscVrBrTbNcFteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1, 1)
)
mscVrBrTbNcFteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbNcFteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbNcFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbNcFteRowStatusEntry.setStatus("mandatory")
_MscVrBrTbNcFteRowStatus_Type = RowStatus
_MscVrBrTbNcFteRowStatus_Object = MibTableColumn
mscVrBrTbNcFteRowStatus = _MscVrBrTbNcFteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1, 1, 1),
    _MscVrBrTbNcFteRowStatus_Type()
)
mscVrBrTbNcFteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteRowStatus.setStatus("mandatory")
_MscVrBrTbNcFteComponentName_Type = DisplayString
_MscVrBrTbNcFteComponentName_Object = MibTableColumn
mscVrBrTbNcFteComponentName = _MscVrBrTbNcFteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1, 1, 2),
    _MscVrBrTbNcFteComponentName_Type()
)
mscVrBrTbNcFteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteComponentName.setStatus("mandatory")
_MscVrBrTbNcFteStorageType_Type = StorageType
_MscVrBrTbNcFteStorageType_Object = MibTableColumn
mscVrBrTbNcFteStorageType = _MscVrBrTbNcFteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1, 1, 4),
    _MscVrBrTbNcFteStorageType_Type()
)
mscVrBrTbNcFteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteStorageType.setStatus("mandatory")


class _MscVrBrTbNcFteAddressIndex_Type(DashedHexString):
    """Custom type mscVrBrTbNcFteAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrTbNcFteAddressIndex_Type.__name__ = "DashedHexString"
_MscVrBrTbNcFteAddressIndex_Object = MibTableColumn
mscVrBrTbNcFteAddressIndex = _MscVrBrTbNcFteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1, 1, 10),
    _MscVrBrTbNcFteAddressIndex_Type()
)
mscVrBrTbNcFteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteAddressIndex.setStatus("mandatory")


class _MscVrBrTbNcFteDomainNumIndex_Type(Integer32):
    """Custom type mscVrBrTbNcFteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrBrTbNcFteDomainNumIndex_Type.__name__ = "Integer32"
_MscVrBrTbNcFteDomainNumIndex_Object = MibTableColumn
mscVrBrTbNcFteDomainNumIndex = _MscVrBrTbNcFteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 1, 1, 11),
    _MscVrBrTbNcFteDomainNumIndex_Type()
)
mscVrBrTbNcFteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteDomainNumIndex.setStatus("mandatory")
_MscVrBrTbNcFteOperTable_Object = MibTable
mscVrBrTbNcFteOperTable = _MscVrBrTbNcFteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrBrTbNcFteOperTable.setStatus("mandatory")
_MscVrBrTbNcFteOperEntry_Object = MibTableRow
mscVrBrTbNcFteOperEntry = _MscVrBrTbNcFteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 10, 1)
)
mscVrBrTbNcFteOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbNcFteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbNcFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbNcFteOperEntry.setStatus("mandatory")


class _MscVrBrTbNcFtePort_Type(AsciiString):
    """Custom type mscVrBrTbNcFtePort based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrBrTbNcFtePort_Type.__name__ = "AsciiString"
_MscVrBrTbNcFtePort_Object = MibTableColumn
mscVrBrTbNcFtePort = _MscVrBrTbNcFtePort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 10, 1, 3),
    _MscVrBrTbNcFtePort_Type()
)
mscVrBrTbNcFtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFtePort.setStatus("mandatory")


class _MscVrBrTbNcFteAgeOfEntry_Type(Gauge32):
    """Custom type mscVrBrTbNcFteAgeOfEntry based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscVrBrTbNcFteAgeOfEntry_Type.__name__ = "Gauge32"
_MscVrBrTbNcFteAgeOfEntry_Object = MibTableColumn
mscVrBrTbNcFteAgeOfEntry = _MscVrBrTbNcFteAgeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 10, 1, 4),
    _MscVrBrTbNcFteAgeOfEntry_Type()
)
mscVrBrTbNcFteAgeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteAgeOfEntry.setStatus("mandatory")


class _MscVrBrTbNcFtePeerAddressInfo_Type(BridgeId):
    """Custom type mscVrBrTbNcFtePeerAddressInfo based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrBrTbNcFtePeerAddressInfo_Type.__name__ = "BridgeId"
_MscVrBrTbNcFtePeerAddressInfo_Object = MibTableColumn
mscVrBrTbNcFtePeerAddressInfo = _MscVrBrTbNcFtePeerAddressInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 10, 1, 5),
    _MscVrBrTbNcFtePeerAddressInfo_Type()
)
mscVrBrTbNcFtePeerAddressInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFtePeerAddressInfo.setStatus("mandatory")


class _MscVrBrTbNcFteStatus_Type(Integer32):
    """Custom type mscVrBrTbNcFteStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_MscVrBrTbNcFteStatus_Type.__name__ = "Integer32"
_MscVrBrTbNcFteStatus_Object = MibTableColumn
mscVrBrTbNcFteStatus = _MscVrBrTbNcFteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 5, 10, 1, 6),
    _MscVrBrTbNcFteStatus_Type()
)
mscVrBrTbNcFteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNcFteStatus.setStatus("mandatory")
_MscVrBrTbProvTable_Object = MibTable
mscVrBrTbProvTable = _MscVrBrTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrBrTbProvTable.setStatus("mandatory")
_MscVrBrTbProvEntry_Object = MibTableRow
mscVrBrTbProvEntry = _MscVrBrTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 10, 1)
)
mscVrBrTbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbProvEntry.setStatus("mandatory")


class _MscVrBrTbFwdTableNumEntries_Type(Unsigned32):
    """Custom type mscVrBrTbFwdTableNumEntries based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrBrTbFwdTableNumEntries_Type.__name__ = "Unsigned32"
_MscVrBrTbFwdTableNumEntries_Object = MibTableColumn
mscVrBrTbFwdTableNumEntries = _MscVrBrTbFwdTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 10, 1, 1),
    _MscVrBrTbFwdTableNumEntries_Type()
)
mscVrBrTbFwdTableNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbFwdTableNumEntries.setStatus("mandatory")


class _MscVrBrTbAgingTime_Type(Unsigned32):
    """Custom type mscVrBrTbAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MscVrBrTbAgingTime_Type.__name__ = "Unsigned32"
_MscVrBrTbAgingTime_Object = MibTableColumn
mscVrBrTbAgingTime = _MscVrBrTbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 10, 1, 2),
    _MscVrBrTbAgingTime_Type()
)
mscVrBrTbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrTbAgingTime.setStatus("mandatory")
_MscVrBrTbStatsTable_Object = MibTable
mscVrBrTbStatsTable = _MscVrBrTbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mscVrBrTbStatsTable.setStatus("mandatory")
_MscVrBrTbStatsEntry_Object = MibTableRow
mscVrBrTbStatsEntry = _MscVrBrTbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 11, 1)
)
mscVrBrTbStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrTbIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrTbStatsEntry.setStatus("mandatory")
_MscVrBrTbLearnedEntryDiscards_Type = Counter32
_MscVrBrTbLearnedEntryDiscards_Object = MibTableColumn
mscVrBrTbLearnedEntryDiscards = _MscVrBrTbLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 11, 1, 1),
    _MscVrBrTbLearnedEntryDiscards_Type()
)
mscVrBrTbLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbLearnedEntryDiscards.setStatus("mandatory")
_MscVrBrTbTotalForwardingTableEntries_Type = Counter32
_MscVrBrTbTotalForwardingTableEntries_Object = MibTableColumn
mscVrBrTbTotalForwardingTableEntries = _MscVrBrTbTotalForwardingTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 11, 1, 2),
    _MscVrBrTbTotalForwardingTableEntries_Type()
)
mscVrBrTbTotalForwardingTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbTotalForwardingTableEntries.setStatus("mandatory")


class _MscVrBrTbNumFtEntriesFree_Type(Gauge32):
    """Custom type mscVrBrTbNumFtEntriesFree based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrBrTbNumFtEntriesFree_Type.__name__ = "Gauge32"
_MscVrBrTbNumFtEntriesFree_Object = MibTableColumn
mscVrBrTbNumFtEntriesFree = _MscVrBrTbNumFtEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 11, 1, 3),
    _MscVrBrTbNumFtEntriesFree_Type()
)
mscVrBrTbNumFtEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNumFtEntriesFree.setStatus("mandatory")
_MscVrBrTbNumFtEntriesDenied_Type = Counter32
_MscVrBrTbNumFtEntriesDenied_Object = MibTableColumn
mscVrBrTbNumFtEntriesDenied = _MscVrBrTbNumFtEntriesDenied_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 4, 11, 1, 4),
    _MscVrBrTbNumFtEntriesDenied_Type()
)
mscVrBrTbNumFtEntriesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrTbNumFtEntriesDenied.setStatus("mandatory")
_MscVrBrSrb_ObjectIdentity = ObjectIdentity
mscVrBrSrb = _MscVrBrSrb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5)
)
_MscVrBrSrbRowStatusTable_Object = MibTable
mscVrBrSrbRowStatusTable = _MscVrBrSrbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrBrSrbRowStatusTable.setStatus("mandatory")
_MscVrBrSrbRowStatusEntry_Object = MibTableRow
mscVrBrSrbRowStatusEntry = _MscVrBrSrbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 1, 1)
)
mscVrBrSrbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbRowStatusEntry.setStatus("mandatory")
_MscVrBrSrbRowStatus_Type = RowStatus
_MscVrBrSrbRowStatus_Object = MibTableColumn
mscVrBrSrbRowStatus = _MscVrBrSrbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 1, 1, 1),
    _MscVrBrSrbRowStatus_Type()
)
mscVrBrSrbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbRowStatus.setStatus("mandatory")
_MscVrBrSrbComponentName_Type = DisplayString
_MscVrBrSrbComponentName_Object = MibTableColumn
mscVrBrSrbComponentName = _MscVrBrSrbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 1, 1, 2),
    _MscVrBrSrbComponentName_Type()
)
mscVrBrSrbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbComponentName.setStatus("mandatory")
_MscVrBrSrbStorageType_Type = StorageType
_MscVrBrSrbStorageType_Object = MibTableColumn
mscVrBrSrbStorageType = _MscVrBrSrbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 1, 1, 4),
    _MscVrBrSrbStorageType_Type()
)
mscVrBrSrbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStorageType.setStatus("mandatory")
_MscVrBrSrbIndex_Type = NonReplicated
_MscVrBrSrbIndex_Object = MibTableColumn
mscVrBrSrbIndex = _MscVrBrSrbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 1, 1, 10),
    _MscVrBrSrbIndex_Type()
)
mscVrBrSrbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrSrbIndex.setStatus("mandatory")
_MscVrBrSrbStp_ObjectIdentity = ObjectIdentity
mscVrBrSrbStp = _MscVrBrSrbStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2)
)
_MscVrBrSrbStpRowStatusTable_Object = MibTable
mscVrBrSrbStpRowStatusTable = _MscVrBrSrbStpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrBrSrbStpRowStatusTable.setStatus("mandatory")
_MscVrBrSrbStpRowStatusEntry_Object = MibTableRow
mscVrBrSrbStpRowStatusEntry = _MscVrBrSrbStpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 1, 1)
)
mscVrBrSrbStpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbStpIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbStpRowStatusEntry.setStatus("mandatory")
_MscVrBrSrbStpRowStatus_Type = RowStatus
_MscVrBrSrbStpRowStatus_Object = MibTableColumn
mscVrBrSrbStpRowStatus = _MscVrBrSrbStpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 1, 1, 1),
    _MscVrBrSrbStpRowStatus_Type()
)
mscVrBrSrbStpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpRowStatus.setStatus("mandatory")
_MscVrBrSrbStpComponentName_Type = DisplayString
_MscVrBrSrbStpComponentName_Object = MibTableColumn
mscVrBrSrbStpComponentName = _MscVrBrSrbStpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 1, 1, 2),
    _MscVrBrSrbStpComponentName_Type()
)
mscVrBrSrbStpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpComponentName.setStatus("mandatory")
_MscVrBrSrbStpStorageType_Type = StorageType
_MscVrBrSrbStpStorageType_Object = MibTableColumn
mscVrBrSrbStpStorageType = _MscVrBrSrbStpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 1, 1, 4),
    _MscVrBrSrbStpStorageType_Type()
)
mscVrBrSrbStpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpStorageType.setStatus("mandatory")


class _MscVrBrSrbStpIndex_Type(Integer32):
    """Custom type mscVrBrSrbStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrBrSrbStpIndex_Type.__name__ = "Integer32"
_MscVrBrSrbStpIndex_Object = MibTableColumn
mscVrBrSrbStpIndex = _MscVrBrSrbStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 1, 1, 10),
    _MscVrBrSrbStpIndex_Type()
)
mscVrBrSrbStpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrSrbStpIndex.setStatus("mandatory")
_MscVrBrSrbStpProvTable_Object = MibTable
mscVrBrSrbStpProvTable = _MscVrBrSrbStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrBrSrbStpProvTable.setStatus("mandatory")
_MscVrBrSrbStpProvEntry_Object = MibTableRow
mscVrBrSrbStpProvEntry = _MscVrBrSrbStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1)
)
mscVrBrSrbStpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbStpIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbStpProvEntry.setStatus("mandatory")


class _MscVrBrSrbStpStpMode_Type(Integer32):
    """Custom type mscVrBrSrbStpStpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("backbone", 2))
    )


_MscVrBrSrbStpStpMode_Type.__name__ = "Integer32"
_MscVrBrSrbStpStpMode_Object = MibTableColumn
mscVrBrSrbStpStpMode = _MscVrBrSrbStpStpMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1, 1),
    _MscVrBrSrbStpStpMode_Type()
)
mscVrBrSrbStpStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpStpMode.setStatus("mandatory")


class _MscVrBrSrbStpProtocolSpec_Type(Integer32):
    """Custom type mscVrBrSrbStpProtocolSpec based on Integer32"""
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
        *(("both", 1),
          ("dec", 2),
          ("ieee8021d", 3))
    )


_MscVrBrSrbStpProtocolSpec_Type.__name__ = "Integer32"
_MscVrBrSrbStpProtocolSpec_Object = MibTableColumn
mscVrBrSrbStpProtocolSpec = _MscVrBrSrbStpProtocolSpec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1, 2),
    _MscVrBrSrbStpProtocolSpec_Type()
)
mscVrBrSrbStpProtocolSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpProtocolSpec.setStatus("mandatory")


class _MscVrBrSrbStpPriority_Type(Unsigned32):
    """Custom type mscVrBrSrbStpPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrBrSrbStpPriority_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpPriority_Object = MibTableColumn
mscVrBrSrbStpPriority = _MscVrBrSrbStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1, 3),
    _MscVrBrSrbStpPriority_Type()
)
mscVrBrSrbStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpPriority.setStatus("mandatory")


class _MscVrBrSrbStpBridgeMaxAge_Type(Unsigned32):
    """Custom type mscVrBrSrbStpBridgeMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MscVrBrSrbStpBridgeMaxAge_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpBridgeMaxAge_Object = MibTableColumn
mscVrBrSrbStpBridgeMaxAge = _MscVrBrSrbStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1, 4),
    _MscVrBrSrbStpBridgeMaxAge_Type()
)
mscVrBrSrbStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpBridgeMaxAge.setStatus("mandatory")


class _MscVrBrSrbStpBridgeHelloTime_Type(Unsigned32):
    """Custom type mscVrBrSrbStpBridgeHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MscVrBrSrbStpBridgeHelloTime_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpBridgeHelloTime_Object = MibTableColumn
mscVrBrSrbStpBridgeHelloTime = _MscVrBrSrbStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1, 5),
    _MscVrBrSrbStpBridgeHelloTime_Type()
)
mscVrBrSrbStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpBridgeHelloTime.setStatus("mandatory")


class _MscVrBrSrbStpBridgeForwardDelay_Type(Unsigned32):
    """Custom type mscVrBrSrbStpBridgeForwardDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MscVrBrSrbStpBridgeForwardDelay_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpBridgeForwardDelay_Object = MibTableColumn
mscVrBrSrbStpBridgeForwardDelay = _MscVrBrSrbStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 10, 1, 6),
    _MscVrBrSrbStpBridgeForwardDelay_Type()
)
mscVrBrSrbStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbStpBridgeForwardDelay.setStatus("mandatory")
_MscVrBrSrbStpOperTable_Object = MibTable
mscVrBrSrbStpOperTable = _MscVrBrSrbStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrBrSrbStpOperTable.setStatus("mandatory")
_MscVrBrSrbStpOperEntry_Object = MibTableRow
mscVrBrSrbStpOperEntry = _MscVrBrSrbStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1)
)
mscVrBrSrbStpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbStpIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbStpOperEntry.setStatus("mandatory")


class _MscVrBrSrbStpBridgeId_Type(BridgeId):
    """Custom type mscVrBrSrbStpBridgeId based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrBrSrbStpBridgeId_Type.__name__ = "BridgeId"
_MscVrBrSrbStpBridgeId_Object = MibTableColumn
mscVrBrSrbStpBridgeId = _MscVrBrSrbStpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 1),
    _MscVrBrSrbStpBridgeId_Type()
)
mscVrBrSrbStpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpBridgeId.setStatus("mandatory")


class _MscVrBrSrbStpRootPortName_Type(AsciiString):
    """Custom type mscVrBrSrbStpRootPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrBrSrbStpRootPortName_Type.__name__ = "AsciiString"
_MscVrBrSrbStpRootPortName_Object = MibTableColumn
mscVrBrSrbStpRootPortName = _MscVrBrSrbStpRootPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 2),
    _MscVrBrSrbStpRootPortName_Type()
)
mscVrBrSrbStpRootPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpRootPortName.setStatus("mandatory")


class _MscVrBrSrbStpTimeSinceTopologyChange_Type(Unsigned32):
    """Custom type mscVrBrSrbStpTimeSinceTopologyChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrBrSrbStpTimeSinceTopologyChange_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpTimeSinceTopologyChange_Object = MibTableColumn
mscVrBrSrbStpTimeSinceTopologyChange = _MscVrBrSrbStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 3),
    _MscVrBrSrbStpTimeSinceTopologyChange_Type()
)
mscVrBrSrbStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpTimeSinceTopologyChange.setStatus("mandatory")


class _MscVrBrSrbStpTopologyChangeDetect_Type(Integer32):
    """Custom type mscVrBrSrbStpTopologyChangeDetect based on Integer32"""
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


_MscVrBrSrbStpTopologyChangeDetect_Type.__name__ = "Integer32"
_MscVrBrSrbStpTopologyChangeDetect_Object = MibTableColumn
mscVrBrSrbStpTopologyChangeDetect = _MscVrBrSrbStpTopologyChangeDetect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 4),
    _MscVrBrSrbStpTopologyChangeDetect_Type()
)
mscVrBrSrbStpTopologyChangeDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpTopologyChangeDetect.setStatus("mandatory")
_MscVrBrSrbStpTopologyChanges_Type = Counter32
_MscVrBrSrbStpTopologyChanges_Object = MibTableColumn
mscVrBrSrbStpTopologyChanges = _MscVrBrSrbStpTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 5),
    _MscVrBrSrbStpTopologyChanges_Type()
)
mscVrBrSrbStpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpTopologyChanges.setStatus("mandatory")


class _MscVrBrSrbStpDesignatedRoot_Type(BridgeId):
    """Custom type mscVrBrSrbStpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscVrBrSrbStpDesignatedRoot_Type.__name__ = "BridgeId"
_MscVrBrSrbStpDesignatedRoot_Object = MibTableColumn
mscVrBrSrbStpDesignatedRoot = _MscVrBrSrbStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 6),
    _MscVrBrSrbStpDesignatedRoot_Type()
)
mscVrBrSrbStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpDesignatedRoot.setStatus("mandatory")


class _MscVrBrSrbStpRootCost_Type(Unsigned32):
    """Custom type mscVrBrSrbStpRootCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrBrSrbStpRootCost_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpRootCost_Object = MibTableColumn
mscVrBrSrbStpRootCost = _MscVrBrSrbStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 8),
    _MscVrBrSrbStpRootCost_Type()
)
mscVrBrSrbStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpRootCost.setStatus("mandatory")


class _MscVrBrSrbStpMaxAge_Type(Unsigned32):
    """Custom type mscVrBrSrbStpMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MscVrBrSrbStpMaxAge_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpMaxAge_Object = MibTableColumn
mscVrBrSrbStpMaxAge = _MscVrBrSrbStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 9),
    _MscVrBrSrbStpMaxAge_Type()
)
mscVrBrSrbStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpMaxAge.setStatus("mandatory")


class _MscVrBrSrbStpAgingTimeOper_Type(Unsigned32):
    """Custom type mscVrBrSrbStpAgingTimeOper based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MscVrBrSrbStpAgingTimeOper_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpAgingTimeOper_Object = MibTableColumn
mscVrBrSrbStpAgingTimeOper = _MscVrBrSrbStpAgingTimeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 10),
    _MscVrBrSrbStpAgingTimeOper_Type()
)
mscVrBrSrbStpAgingTimeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpAgingTimeOper.setStatus("mandatory")


class _MscVrBrSrbStpHelloTime_Type(Unsigned32):
    """Custom type mscVrBrSrbStpHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MscVrBrSrbStpHelloTime_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpHelloTime_Object = MibTableColumn
mscVrBrSrbStpHelloTime = _MscVrBrSrbStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 11),
    _MscVrBrSrbStpHelloTime_Type()
)
mscVrBrSrbStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpHelloTime.setStatus("mandatory")


class _MscVrBrSrbStpHoldTime_Type(Unsigned32):
    """Custom type mscVrBrSrbStpHoldTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
    )


_MscVrBrSrbStpHoldTime_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpHoldTime_Object = MibTableColumn
mscVrBrSrbStpHoldTime = _MscVrBrSrbStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 12),
    _MscVrBrSrbStpHoldTime_Type()
)
mscVrBrSrbStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpHoldTime.setStatus("mandatory")


class _MscVrBrSrbStpFwdDelay_Type(Unsigned32):
    """Custom type mscVrBrSrbStpFwdDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MscVrBrSrbStpFwdDelay_Type.__name__ = "Unsigned32"
_MscVrBrSrbStpFwdDelay_Object = MibTableColumn
mscVrBrSrbStpFwdDelay = _MscVrBrSrbStpFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 2, 11, 1, 13),
    _MscVrBrSrbStpFwdDelay_Type()
)
mscVrBrSrbStpFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbStpFwdDelay.setStatus("mandatory")
_MscVrBrSrbLte_ObjectIdentity = ObjectIdentity
mscVrBrSrbLte = _MscVrBrSrbLte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3)
)
_MscVrBrSrbLteRowStatusTable_Object = MibTable
mscVrBrSrbLteRowStatusTable = _MscVrBrSrbLteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrBrSrbLteRowStatusTable.setStatus("mandatory")
_MscVrBrSrbLteRowStatusEntry_Object = MibTableRow
mscVrBrSrbLteRowStatusEntry = _MscVrBrSrbLteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1, 1)
)
mscVrBrSrbLteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbLteLanIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbLteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbLteRowStatusEntry.setStatus("mandatory")
_MscVrBrSrbLteRowStatus_Type = RowStatus
_MscVrBrSrbLteRowStatus_Object = MibTableColumn
mscVrBrSrbLteRowStatus = _MscVrBrSrbLteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1, 1, 1),
    _MscVrBrSrbLteRowStatus_Type()
)
mscVrBrSrbLteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLteRowStatus.setStatus("mandatory")
_MscVrBrSrbLteComponentName_Type = DisplayString
_MscVrBrSrbLteComponentName_Object = MibTableColumn
mscVrBrSrbLteComponentName = _MscVrBrSrbLteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1, 1, 2),
    _MscVrBrSrbLteComponentName_Type()
)
mscVrBrSrbLteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLteComponentName.setStatus("mandatory")
_MscVrBrSrbLteStorageType_Type = StorageType
_MscVrBrSrbLteStorageType_Object = MibTableColumn
mscVrBrSrbLteStorageType = _MscVrBrSrbLteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1, 1, 4),
    _MscVrBrSrbLteStorageType_Type()
)
mscVrBrSrbLteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLteStorageType.setStatus("mandatory")


class _MscVrBrSrbLteLanIdIndex_Type(Integer32):
    """Custom type mscVrBrSrbLteLanIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscVrBrSrbLteLanIdIndex_Type.__name__ = "Integer32"
_MscVrBrSrbLteLanIdIndex_Object = MibTableColumn
mscVrBrSrbLteLanIdIndex = _MscVrBrSrbLteLanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1, 1, 10),
    _MscVrBrSrbLteLanIdIndex_Type()
)
mscVrBrSrbLteLanIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrSrbLteLanIdIndex.setStatus("mandatory")


class _MscVrBrSrbLteDomainNumIndex_Type(Integer32):
    """Custom type mscVrBrSrbLteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrBrSrbLteDomainNumIndex_Type.__name__ = "Integer32"
_MscVrBrSrbLteDomainNumIndex_Object = MibTableColumn
mscVrBrSrbLteDomainNumIndex = _MscVrBrSrbLteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 1, 1, 11),
    _MscVrBrSrbLteDomainNumIndex_Type()
)
mscVrBrSrbLteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrBrSrbLteDomainNumIndex.setStatus("mandatory")
_MscVrBrSrbLteOperTable_Object = MibTable
mscVrBrSrbLteOperTable = _MscVrBrSrbLteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrBrSrbLteOperTable.setStatus("mandatory")
_MscVrBrSrbLteOperEntry_Object = MibTableRow
mscVrBrSrbLteOperEntry = _MscVrBrSrbLteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 10, 1)
)
mscVrBrSrbLteOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbLteLanIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbLteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbLteOperEntry.setStatus("mandatory")


class _MscVrBrSrbLtePortName_Type(AsciiString):
    """Custom type mscVrBrSrbLtePortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_MscVrBrSrbLtePortName_Type.__name__ = "AsciiString"
_MscVrBrSrbLtePortName_Object = MibTableColumn
mscVrBrSrbLtePortName = _MscVrBrSrbLtePortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 10, 1, 1),
    _MscVrBrSrbLtePortName_Type()
)
mscVrBrSrbLtePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLtePortName.setStatus("mandatory")


class _MscVrBrSrbLteAgeOfEntry_Type(Unsigned32):
    """Custom type mscVrBrSrbLteAgeOfEntry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrBrSrbLteAgeOfEntry_Type.__name__ = "Unsigned32"
_MscVrBrSrbLteAgeOfEntry_Object = MibTableColumn
mscVrBrSrbLteAgeOfEntry = _MscVrBrSrbLteAgeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 10, 1, 2),
    _MscVrBrSrbLteAgeOfEntry_Type()
)
mscVrBrSrbLteAgeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLteAgeOfEntry.setStatus("mandatory")


class _MscVrBrSrbLtePeerMACAddress_Type(DashedHexString):
    """Custom type mscVrBrSrbLtePeerMACAddress based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrSrbLtePeerMACAddress_Type.__name__ = "DashedHexString"
_MscVrBrSrbLtePeerMACAddress_Object = MibTableColumn
mscVrBrSrbLtePeerMACAddress = _MscVrBrSrbLtePeerMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 10, 1, 3),
    _MscVrBrSrbLtePeerMACAddress_Type()
)
mscVrBrSrbLtePeerMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLtePeerMACAddress.setStatus("mandatory")


class _MscVrBrSrbLteTypeOfEntry_Type(Integer32):
    """Custom type mscVrBrSrbLteTypeOfEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_MscVrBrSrbLteTypeOfEntry_Type.__name__ = "Integer32"
_MscVrBrSrbLteTypeOfEntry_Object = MibTableColumn
mscVrBrSrbLteTypeOfEntry = _MscVrBrSrbLteTypeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 3, 10, 1, 4),
    _MscVrBrSrbLteTypeOfEntry_Type()
)
mscVrBrSrbLteTypeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbLteTypeOfEntry.setStatus("mandatory")
_MscVrBrSrbProvTable_Object = MibTable
mscVrBrSrbProvTable = _MscVrBrSrbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrBrSrbProvTable.setStatus("mandatory")
_MscVrBrSrbProvEntry_Object = MibTableRow
mscVrBrSrbProvEntry = _MscVrBrSrbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 10, 1)
)
mscVrBrSrbProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbProvEntry.setStatus("mandatory")


class _MscVrBrSrbLanIdTableNumEntries_Type(Unsigned32):
    """Custom type mscVrBrSrbLanIdTableNumEntries based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 65535),
    )


_MscVrBrSrbLanIdTableNumEntries_Type.__name__ = "Unsigned32"
_MscVrBrSrbLanIdTableNumEntries_Object = MibTableColumn
mscVrBrSrbLanIdTableNumEntries = _MscVrBrSrbLanIdTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 10, 1, 1),
    _MscVrBrSrbLanIdTableNumEntries_Type()
)
mscVrBrSrbLanIdTableNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbLanIdTableNumEntries.setStatus("mandatory")


class _MscVrBrSrbAgingTime_Type(Unsigned32):
    """Custom type mscVrBrSrbAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MscVrBrSrbAgingTime_Type.__name__ = "Unsigned32"
_MscVrBrSrbAgingTime_Object = MibTableColumn
mscVrBrSrbAgingTime = _MscVrBrSrbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 10, 1, 2),
    _MscVrBrSrbAgingTime_Type()
)
mscVrBrSrbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrSrbAgingTime.setStatus("mandatory")


class _MscVrBrSrbBridgeLfMode_Type(Integer32):
    """Custom type mscVrBrSrbBridgeLfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode3", 1),
          ("mode6", 2))
    )


_MscVrBrSrbBridgeLfMode_Type.__name__ = "Integer32"
_MscVrBrSrbBridgeLfMode_Object = MibTableColumn
mscVrBrSrbBridgeLfMode = _MscVrBrSrbBridgeLfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 10, 1, 3),
    _MscVrBrSrbBridgeLfMode_Type()
)
mscVrBrSrbBridgeLfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbBridgeLfMode.setStatus("mandatory")
_MscVrBrSrbStatsTable_Object = MibTable
mscVrBrSrbStatsTable = _MscVrBrSrbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 11)
)
if mibBuilder.loadTexts:
    mscVrBrSrbStatsTable.setStatus("mandatory")
_MscVrBrSrbStatsEntry_Object = MibTableRow
mscVrBrSrbStatsEntry = _MscVrBrSrbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 11, 1)
)
mscVrBrSrbStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrSrbIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrSrbStatsEntry.setStatus("mandatory")
_MscVrBrSrbTotalLanIdTableEntries_Type = Counter32
_MscVrBrSrbTotalLanIdTableEntries_Object = MibTableColumn
mscVrBrSrbTotalLanIdTableEntries = _MscVrBrSrbTotalLanIdTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 11, 1, 1),
    _MscVrBrSrbTotalLanIdTableEntries_Type()
)
mscVrBrSrbTotalLanIdTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbTotalLanIdTableEntries.setStatus("mandatory")
_MscVrBrSrbNumLanIdtEntriesFree_Type = Counter32
_MscVrBrSrbNumLanIdtEntriesFree_Object = MibTableColumn
mscVrBrSrbNumLanIdtEntriesFree = _MscVrBrSrbNumLanIdtEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 11, 1, 2),
    _MscVrBrSrbNumLanIdtEntriesFree_Type()
)
mscVrBrSrbNumLanIdtEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbNumLanIdtEntriesFree.setStatus("mandatory")
_MscVrBrSrbNumLanIdtEntriesDenied_Type = Counter32
_MscVrBrSrbNumLanIdtEntriesDenied_Object = MibTableColumn
mscVrBrSrbNumLanIdtEntriesDenied = _MscVrBrSrbNumLanIdtEntriesDenied_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 5, 11, 1, 3),
    _MscVrBrSrbNumLanIdtEntriesDenied_Type()
)
mscVrBrSrbNumLanIdtEntriesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSrbNumLanIdtEntriesDenied.setStatus("mandatory")
_MscVrBrAdminControlTable_Object = MibTable
mscVrBrAdminControlTable = _MscVrBrAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrBrAdminControlTable.setStatus("mandatory")
_MscVrBrAdminControlEntry_Object = MibTableRow
mscVrBrAdminControlEntry = _MscVrBrAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 10, 1)
)
mscVrBrAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrAdminControlEntry.setStatus("mandatory")


class _MscVrBrAdminStatus_Type(Integer32):
    """Custom type mscVrBrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrBrAdminStatus_Type.__name__ = "Integer32"
_MscVrBrAdminStatus_Object = MibTableColumn
mscVrBrAdminStatus = _MscVrBrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 10, 1, 1),
    _MscVrBrAdminStatus_Type()
)
mscVrBrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrBrAdminStatus.setStatus("mandatory")
_MscVrBrStateTable_Object = MibTable
mscVrBrStateTable = _MscVrBrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 12)
)
if mibBuilder.loadTexts:
    mscVrBrStateTable.setStatus("mandatory")
_MscVrBrStateEntry_Object = MibTableRow
mscVrBrStateEntry = _MscVrBrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 12, 1)
)
mscVrBrStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrStateEntry.setStatus("mandatory")


class _MscVrBrAdminState_Type(Integer32):
    """Custom type mscVrBrAdminState based on Integer32"""
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


_MscVrBrAdminState_Type.__name__ = "Integer32"
_MscVrBrAdminState_Object = MibTableColumn
mscVrBrAdminState = _MscVrBrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 12, 1, 1),
    _MscVrBrAdminState_Type()
)
mscVrBrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrAdminState.setStatus("mandatory")


class _MscVrBrOperationalState_Type(Integer32):
    """Custom type mscVrBrOperationalState based on Integer32"""
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


_MscVrBrOperationalState_Type.__name__ = "Integer32"
_MscVrBrOperationalState_Object = MibTableColumn
mscVrBrOperationalState = _MscVrBrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 12, 1, 2),
    _MscVrBrOperationalState_Type()
)
mscVrBrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrOperationalState.setStatus("mandatory")


class _MscVrBrUsageState_Type(Integer32):
    """Custom type mscVrBrUsageState based on Integer32"""
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


_MscVrBrUsageState_Type.__name__ = "Integer32"
_MscVrBrUsageState_Object = MibTableColumn
mscVrBrUsageState = _MscVrBrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 12, 1, 3),
    _MscVrBrUsageState_Type()
)
mscVrBrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrUsageState.setStatus("mandatory")
_MscVrBrOperStatusTable_Object = MibTable
mscVrBrOperStatusTable = _MscVrBrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 13)
)
if mibBuilder.loadTexts:
    mscVrBrOperStatusTable.setStatus("mandatory")
_MscVrBrOperStatusEntry_Object = MibTableRow
mscVrBrOperStatusEntry = _MscVrBrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 13, 1)
)
mscVrBrOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrOperStatusEntry.setStatus("mandatory")


class _MscVrBrSnmpOperStatus_Type(Integer32):
    """Custom type mscVrBrSnmpOperStatus based on Integer32"""
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


_MscVrBrSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrBrSnmpOperStatus_Object = MibTableColumn
mscVrBrSnmpOperStatus = _MscVrBrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 13, 1, 1),
    _MscVrBrSnmpOperStatus_Type()
)
mscVrBrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrSnmpOperStatus.setStatus("mandatory")
_MscVrBrOperTable_Object = MibTable
mscVrBrOperTable = _MscVrBrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 14)
)
if mibBuilder.loadTexts:
    mscVrBrOperTable.setStatus("mandatory")
_MscVrBrOperEntry_Object = MibTableRow
mscVrBrOperEntry = _MscVrBrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 14, 1)
)
mscVrBrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscVrBrIndex"),
)
if mibBuilder.loadTexts:
    mscVrBrOperEntry.setStatus("mandatory")


class _MscVrBrBridgeAddress_Type(MacAddress):
    """Custom type mscVrBrBridgeAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrBrBridgeAddress_Type.__name__ = "MacAddress"
_MscVrBrBridgeAddress_Object = MibTableColumn
mscVrBrBridgeAddress = _MscVrBrBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 14, 1, 1),
    _MscVrBrBridgeAddress_Type()
)
mscVrBrBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrBridgeAddress.setStatus("mandatory")


class _MscVrBrNumPorts_Type(Gauge32):
    """Custom type mscVrBrNumPorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrBrNumPorts_Type.__name__ = "Gauge32"
_MscVrBrNumPorts_Object = MibTableColumn
mscVrBrNumPorts = _MscVrBrNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 14, 1, 2),
    _MscVrBrNumPorts_Type()
)
mscVrBrNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrNumPorts.setStatus("mandatory")


class _MscVrBrType_Type(Integer32):
    """Custom type mscVrBrType based on Integer32"""
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
        *(("sourceRouteOnly", 3),
          ("srt", 4),
          ("transparentOnly", 2),
          ("unknown", 1))
    )


_MscVrBrType_Type.__name__ = "Integer32"
_MscVrBrType_Object = MibTableColumn
mscVrBrType = _MscVrBrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 5, 14, 1, 3),
    _MscVrBrType_Type()
)
mscVrBrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrBrType.setStatus("mandatory")
_MscCB_ObjectIdentity = ObjectIdentity
mscCB = _MscCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103)
)
_MscCBRowStatusTable_Object = MibTable
mscCBRowStatusTable = _MscCBRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 1)
)
if mibBuilder.loadTexts:
    mscCBRowStatusTable.setStatus("mandatory")
_MscCBRowStatusEntry_Object = MibTableRow
mscCBRowStatusEntry = _MscCBRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 1, 1)
)
mscCBRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBRowStatusEntry.setStatus("mandatory")
_MscCBRowStatus_Type = RowStatus
_MscCBRowStatus_Object = MibTableColumn
mscCBRowStatus = _MscCBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 1, 1, 1),
    _MscCBRowStatus_Type()
)
mscCBRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCBRowStatus.setStatus("mandatory")
_MscCBComponentName_Type = DisplayString
_MscCBComponentName_Object = MibTableColumn
mscCBComponentName = _MscCBComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 1, 1, 2),
    _MscCBComponentName_Type()
)
mscCBComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBComponentName.setStatus("mandatory")
_MscCBStorageType_Type = StorageType
_MscCBStorageType_Object = MibTableColumn
mscCBStorageType = _MscCBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 1, 1, 4),
    _MscCBStorageType_Type()
)
mscCBStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBStorageType.setStatus("mandatory")
_MscCBIndex_Type = NonReplicated
_MscCBIndex_Object = MibTableColumn
mscCBIndex = _MscCBIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 1, 1, 10),
    _MscCBIndex_Type()
)
mscCBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCBIndex.setStatus("mandatory")
_MscCBAdminControlTable_Object = MibTable
mscCBAdminControlTable = _MscCBAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 10)
)
if mibBuilder.loadTexts:
    mscCBAdminControlTable.setStatus("mandatory")
_MscCBAdminControlEntry_Object = MibTableRow
mscCBAdminControlEntry = _MscCBAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 10, 1)
)
mscCBAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBAdminControlEntry.setStatus("mandatory")


class _MscCBSnmpAdminStatus_Type(Integer32):
    """Custom type mscCBSnmpAdminStatus based on Integer32"""
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


_MscCBSnmpAdminStatus_Type.__name__ = "Integer32"
_MscCBSnmpAdminStatus_Object = MibTableColumn
mscCBSnmpAdminStatus = _MscCBSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 10, 1, 1),
    _MscCBSnmpAdminStatus_Type()
)
mscCBSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCBSnmpAdminStatus.setStatus("obsolete")
_MscCBIfEntryTable_Object = MibTable
mscCBIfEntryTable = _MscCBIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 11)
)
if mibBuilder.loadTexts:
    mscCBIfEntryTable.setStatus("mandatory")
_MscCBIfEntryEntry_Object = MibTableRow
mscCBIfEntryEntry = _MscCBIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 11, 1)
)
mscCBIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBIfEntryEntry.setStatus("mandatory")


class _MscCBIfAdminStatus_Type(Integer32):
    """Custom type mscCBIfAdminStatus based on Integer32"""
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


_MscCBIfAdminStatus_Type.__name__ = "Integer32"
_MscCBIfAdminStatus_Object = MibTableColumn
mscCBIfAdminStatus = _MscCBIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 11, 1, 1),
    _MscCBIfAdminStatus_Type()
)
mscCBIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCBIfAdminStatus.setStatus("mandatory")


class _MscCBIfIndex_Type(InterfaceIndex):
    """Custom type mscCBIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscCBIfIndex_Type.__name__ = "InterfaceIndex"
_MscCBIfIndex_Object = MibTableColumn
mscCBIfIndex = _MscCBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 11, 1, 2),
    _MscCBIfIndex_Type()
)
mscCBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBIfIndex.setStatus("mandatory")
_MscCBMpTable_Object = MibTable
mscCBMpTable = _MscCBMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 12)
)
if mibBuilder.loadTexts:
    mscCBMpTable.setStatus("mandatory")
_MscCBMpEntry_Object = MibTableRow
mscCBMpEntry = _MscCBMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 12, 1)
)
mscCBMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBMpEntry.setStatus("mandatory")
_MscCBLinkToProtocolPort_Type = Link
_MscCBLinkToProtocolPort_Object = MibTableColumn
mscCBLinkToProtocolPort = _MscCBLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 12, 1, 1),
    _MscCBLinkToProtocolPort_Type()
)
mscCBLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCBLinkToProtocolPort.setStatus("mandatory")
_MscCBOperTable_Object = MibTable
mscCBOperTable = _MscCBOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 13)
)
if mibBuilder.loadTexts:
    mscCBOperTable.setStatus("mandatory")
_MscCBOperEntry_Object = MibTableRow
mscCBOperEntry = _MscCBOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 13, 1)
)
mscCBOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBOperEntry.setStatus("mandatory")


class _MscCBMacAddress_Type(MacAddress):
    """Custom type mscCBMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscCBMacAddress_Type.__name__ = "MacAddress"
_MscCBMacAddress_Object = MibTableColumn
mscCBMacAddress = _MscCBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 13, 1, 1),
    _MscCBMacAddress_Type()
)
mscCBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBMacAddress.setStatus("mandatory")
_MscCBStateTable_Object = MibTable
mscCBStateTable = _MscCBStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 14)
)
if mibBuilder.loadTexts:
    mscCBStateTable.setStatus("mandatory")
_MscCBStateEntry_Object = MibTableRow
mscCBStateEntry = _MscCBStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 14, 1)
)
mscCBStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBStateEntry.setStatus("mandatory")


class _MscCBAdminState_Type(Integer32):
    """Custom type mscCBAdminState based on Integer32"""
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


_MscCBAdminState_Type.__name__ = "Integer32"
_MscCBAdminState_Object = MibTableColumn
mscCBAdminState = _MscCBAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 14, 1, 1),
    _MscCBAdminState_Type()
)
mscCBAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBAdminState.setStatus("mandatory")


class _MscCBOperationalState_Type(Integer32):
    """Custom type mscCBOperationalState based on Integer32"""
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


_MscCBOperationalState_Type.__name__ = "Integer32"
_MscCBOperationalState_Object = MibTableColumn
mscCBOperationalState = _MscCBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 14, 1, 2),
    _MscCBOperationalState_Type()
)
mscCBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBOperationalState.setStatus("mandatory")


class _MscCBUsageState_Type(Integer32):
    """Custom type mscCBUsageState based on Integer32"""
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


_MscCBUsageState_Type.__name__ = "Integer32"
_MscCBUsageState_Object = MibTableColumn
mscCBUsageState = _MscCBUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 14, 1, 3),
    _MscCBUsageState_Type()
)
mscCBUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBUsageState.setStatus("mandatory")
_MscCBOperStatusTable_Object = MibTable
mscCBOperStatusTable = _MscCBOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 15)
)
if mibBuilder.loadTexts:
    mscCBOperStatusTable.setStatus("mandatory")
_MscCBOperStatusEntry_Object = MibTableRow
mscCBOperStatusEntry = _MscCBOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 15, 1)
)
mscCBOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscCBIndex"),
)
if mibBuilder.loadTexts:
    mscCBOperStatusEntry.setStatus("mandatory")


class _MscCBSnmpOperStatus_Type(Integer32):
    """Custom type mscCBSnmpOperStatus based on Integer32"""
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


_MscCBSnmpOperStatus_Type.__name__ = "Integer32"
_MscCBSnmpOperStatus_Object = MibTableColumn
mscCBSnmpOperStatus = _MscCBSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 103, 15, 1, 1),
    _MscCBSnmpOperStatus_Type()
)
mscCBSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCBSnmpOperStatus.setStatus("mandatory")
_MscPB_ObjectIdentity = ObjectIdentity
mscPB = _MscPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104)
)
_MscPBRowStatusTable_Object = MibTable
mscPBRowStatusTable = _MscPBRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 1)
)
if mibBuilder.loadTexts:
    mscPBRowStatusTable.setStatus("mandatory")
_MscPBRowStatusEntry_Object = MibTableRow
mscPBRowStatusEntry = _MscPBRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 1, 1)
)
mscPBRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBRowStatusEntry.setStatus("mandatory")
_MscPBRowStatus_Type = RowStatus
_MscPBRowStatus_Object = MibTableColumn
mscPBRowStatus = _MscPBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 1, 1, 1),
    _MscPBRowStatus_Type()
)
mscPBRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPBRowStatus.setStatus("mandatory")
_MscPBComponentName_Type = DisplayString
_MscPBComponentName_Object = MibTableColumn
mscPBComponentName = _MscPBComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 1, 1, 2),
    _MscPBComponentName_Type()
)
mscPBComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBComponentName.setStatus("mandatory")
_MscPBStorageType_Type = StorageType
_MscPBStorageType_Object = MibTableColumn
mscPBStorageType = _MscPBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 1, 1, 4),
    _MscPBStorageType_Type()
)
mscPBStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBStorageType.setStatus("mandatory")
_MscPBIndex_Type = NonReplicated
_MscPBIndex_Object = MibTableColumn
mscPBIndex = _MscPBIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 1, 1, 10),
    _MscPBIndex_Type()
)
mscPBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPBIndex.setStatus("mandatory")
_MscPBAdminControlTable_Object = MibTable
mscPBAdminControlTable = _MscPBAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 10)
)
if mibBuilder.loadTexts:
    mscPBAdminControlTable.setStatus("mandatory")
_MscPBAdminControlEntry_Object = MibTableRow
mscPBAdminControlEntry = _MscPBAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 10, 1)
)
mscPBAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBAdminControlEntry.setStatus("mandatory")


class _MscPBSnmpAdminStatus_Type(Integer32):
    """Custom type mscPBSnmpAdminStatus based on Integer32"""
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


_MscPBSnmpAdminStatus_Type.__name__ = "Integer32"
_MscPBSnmpAdminStatus_Object = MibTableColumn
mscPBSnmpAdminStatus = _MscPBSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 10, 1, 1),
    _MscPBSnmpAdminStatus_Type()
)
mscPBSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPBSnmpAdminStatus.setStatus("obsolete")
_MscPBIfEntryTable_Object = MibTable
mscPBIfEntryTable = _MscPBIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 11)
)
if mibBuilder.loadTexts:
    mscPBIfEntryTable.setStatus("mandatory")
_MscPBIfEntryEntry_Object = MibTableRow
mscPBIfEntryEntry = _MscPBIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 11, 1)
)
mscPBIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBIfEntryEntry.setStatus("mandatory")


class _MscPBIfAdminStatus_Type(Integer32):
    """Custom type mscPBIfAdminStatus based on Integer32"""
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


_MscPBIfAdminStatus_Type.__name__ = "Integer32"
_MscPBIfAdminStatus_Object = MibTableColumn
mscPBIfAdminStatus = _MscPBIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 11, 1, 1),
    _MscPBIfAdminStatus_Type()
)
mscPBIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPBIfAdminStatus.setStatus("mandatory")


class _MscPBIfIndex_Type(InterfaceIndex):
    """Custom type mscPBIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscPBIfIndex_Type.__name__ = "InterfaceIndex"
_MscPBIfIndex_Object = MibTableColumn
mscPBIfIndex = _MscPBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 11, 1, 2),
    _MscPBIfIndex_Type()
)
mscPBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBIfIndex.setStatus("mandatory")
_MscPBMpTable_Object = MibTable
mscPBMpTable = _MscPBMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 12)
)
if mibBuilder.loadTexts:
    mscPBMpTable.setStatus("mandatory")
_MscPBMpEntry_Object = MibTableRow
mscPBMpEntry = _MscPBMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 12, 1)
)
mscPBMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBMpEntry.setStatus("mandatory")
_MscPBLinkToProtocolPort_Type = Link
_MscPBLinkToProtocolPort_Object = MibTableColumn
mscPBLinkToProtocolPort = _MscPBLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 12, 1, 1),
    _MscPBLinkToProtocolPort_Type()
)
mscPBLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPBLinkToProtocolPort.setStatus("mandatory")
_MscPBOperTable_Object = MibTable
mscPBOperTable = _MscPBOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 13)
)
if mibBuilder.loadTexts:
    mscPBOperTable.setStatus("mandatory")
_MscPBOperEntry_Object = MibTableRow
mscPBOperEntry = _MscPBOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 13, 1)
)
mscPBOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBOperEntry.setStatus("mandatory")


class _MscPBMacAddress_Type(HexString):
    """Custom type mscPBMacAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscPBMacAddress_Type.__name__ = "HexString"
_MscPBMacAddress_Object = MibTableColumn
mscPBMacAddress = _MscPBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 13, 1, 1),
    _MscPBMacAddress_Type()
)
mscPBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBMacAddress.setStatus("mandatory")
_MscPBStateTable_Object = MibTable
mscPBStateTable = _MscPBStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 14)
)
if mibBuilder.loadTexts:
    mscPBStateTable.setStatus("mandatory")
_MscPBStateEntry_Object = MibTableRow
mscPBStateEntry = _MscPBStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 14, 1)
)
mscPBStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBStateEntry.setStatus("mandatory")


class _MscPBAdminState_Type(Integer32):
    """Custom type mscPBAdminState based on Integer32"""
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


_MscPBAdminState_Type.__name__ = "Integer32"
_MscPBAdminState_Object = MibTableColumn
mscPBAdminState = _MscPBAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 14, 1, 1),
    _MscPBAdminState_Type()
)
mscPBAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBAdminState.setStatus("mandatory")


class _MscPBOperationalState_Type(Integer32):
    """Custom type mscPBOperationalState based on Integer32"""
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


_MscPBOperationalState_Type.__name__ = "Integer32"
_MscPBOperationalState_Object = MibTableColumn
mscPBOperationalState = _MscPBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 14, 1, 2),
    _MscPBOperationalState_Type()
)
mscPBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBOperationalState.setStatus("mandatory")


class _MscPBUsageState_Type(Integer32):
    """Custom type mscPBUsageState based on Integer32"""
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


_MscPBUsageState_Type.__name__ = "Integer32"
_MscPBUsageState_Object = MibTableColumn
mscPBUsageState = _MscPBUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 14, 1, 3),
    _MscPBUsageState_Type()
)
mscPBUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBUsageState.setStatus("mandatory")
_MscPBOperStatusTable_Object = MibTable
mscPBOperStatusTable = _MscPBOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 15)
)
if mibBuilder.loadTexts:
    mscPBOperStatusTable.setStatus("mandatory")
_MscPBOperStatusEntry_Object = MibTableRow
mscPBOperStatusEntry = _MscPBOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 15, 1)
)
mscPBOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BridgeMIB", "mscPBIndex"),
)
if mibBuilder.loadTexts:
    mscPBOperStatusEntry.setStatus("mandatory")


class _MscPBSnmpOperStatus_Type(Integer32):
    """Custom type mscPBSnmpOperStatus based on Integer32"""
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


_MscPBSnmpOperStatus_Type.__name__ = "Integer32"
_MscPBSnmpOperStatus_Object = MibTableColumn
mscPBSnmpOperStatus = _MscPBSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 104, 15, 1, 1),
    _MscPBSnmpOperStatus_Type()
)
mscPBSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPBSnmpOperStatus.setStatus("mandatory")
_BridgeMIB_ObjectIdentity = ObjectIdentity
bridgeMIB = _BridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25)
)
_BridgeGroup_ObjectIdentity = ObjectIdentity
bridgeGroup = _BridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 1)
)
_BridgeGroupCA_ObjectIdentity = ObjectIdentity
bridgeGroupCA = _BridgeGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 1, 1)
)
_BridgeGroupCA02_ObjectIdentity = ObjectIdentity
bridgeGroupCA02 = _BridgeGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 1, 1, 3)
)
_BridgeGroupCA02A_ObjectIdentity = ObjectIdentity
bridgeGroupCA02A = _BridgeGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 1, 1, 3, 2)
)
_BridgeCapabilities_ObjectIdentity = ObjectIdentity
bridgeCapabilities = _BridgeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 3)
)
_BridgeCapabilitiesCA_ObjectIdentity = ObjectIdentity
bridgeCapabilitiesCA = _BridgeCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 3, 1)
)
_BridgeCapabilitiesCA02_ObjectIdentity = ObjectIdentity
bridgeCapabilitiesCA02 = _BridgeCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 3, 1, 3)
)
_BridgeCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
bridgeCapabilitiesCA02A = _BridgeCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 25, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BridgeMIB",
    **{"mscVrPpTbcl": mscVrPpTbcl,
       "mscVrPpTbclRowStatusTable": mscVrPpTbclRowStatusTable,
       "mscVrPpTbclRowStatusEntry": mscVrPpTbclRowStatusEntry,
       "mscVrPpTbclRowStatus": mscVrPpTbclRowStatus,
       "mscVrPpTbclComponentName": mscVrPpTbclComponentName,
       "mscVrPpTbclStorageType": mscVrPpTbclStorageType,
       "mscVrPpTbclIndex": mscVrPpTbclIndex,
       "mscVrPpTbclNs": mscVrPpTbclNs,
       "mscVrPpTbclNsRowStatusTable": mscVrPpTbclNsRowStatusTable,
       "mscVrPpTbclNsRowStatusEntry": mscVrPpTbclNsRowStatusEntry,
       "mscVrPpTbclNsRowStatus": mscVrPpTbclNsRowStatus,
       "mscVrPpTbclNsComponentName": mscVrPpTbclNsComponentName,
       "mscVrPpTbclNsStorageType": mscVrPpTbclNsStorageType,
       "mscVrPpTbclNsIndex": mscVrPpTbclNsIndex,
       "mscVrPpTbclNsProvTable": mscVrPpTbclNsProvTable,
       "mscVrPpTbclNsProvEntry": mscVrPpTbclNsProvEntry,
       "mscVrPpTbclNsIncomingFilter": mscVrPpTbclNsIncomingFilter,
       "mscVrPpTbclNsOutgoingFilter": mscVrPpTbclNsOutgoingFilter,
       "mscVrPpTbclProvTable": mscVrPpTbclProvTable,
       "mscVrPpTbclProvEntry": mscVrPpTbclProvEntry,
       "mscVrPpTbclTranslateIpx": mscVrPpTbclTranslateIpx,
       "mscVrPpTbclFragmentIp": mscVrPpTbclFragmentIp,
       "mscVrPpTbclServiceClass": mscVrPpTbclServiceClass,
       "mscVrPpTbclConvertArpMacAddress": mscVrPpTbclConvertArpMacAddress,
       "mscVrPpTbclPortNum": mscVrPpTbclPortNum,
       "mscVrPpTbclTbProvTable": mscVrPpTbclTbProvTable,
       "mscVrPpTbclTbProvEntry": mscVrPpTbclTbProvEntry,
       "mscVrPpTbclSecureOption": mscVrPpTbclSecureOption,
       "mscVrPpTbclStpProvTable": mscVrPpTbclStpProvTable,
       "mscVrPpTbclStpProvEntry": mscVrPpTbclStpProvEntry,
       "mscVrPpTbclAdminStatus": mscVrPpTbclAdminStatus,
       "mscVrPpTbclPortStateStpControl": mscVrPpTbclPortStateStpControl,
       "mscVrPpTbclStpTypeProv": mscVrPpTbclStpTypeProv,
       "mscVrPpTbclPortPriority": mscVrPpTbclPortPriority,
       "mscVrPpTbclPathCost": mscVrPpTbclPathCost,
       "mscVrPpTbclPathCostMethod": mscVrPpTbclPathCostMethod,
       "mscVrPpTbclDIProvTable": mscVrPpTbclDIProvTable,
       "mscVrPpTbclDIProvEntry": mscVrPpTbclDIProvEntry,
       "mscVrPpTbclDomainNum": mscVrPpTbclDomainNum,
       "mscVrPpTbclPreserveDomain": mscVrPpTbclPreserveDomain,
       "mscVrPpTbclStateTable": mscVrPpTbclStateTable,
       "mscVrPpTbclStateEntry": mscVrPpTbclStateEntry,
       "mscVrPpTbclAdminState": mscVrPpTbclAdminState,
       "mscVrPpTbclOperationalState": mscVrPpTbclOperationalState,
       "mscVrPpTbclUsageState": mscVrPpTbclUsageState,
       "mscVrPpTbclOperStatusTable": mscVrPpTbclOperStatusTable,
       "mscVrPpTbclOperStatusEntry": mscVrPpTbclOperStatusEntry,
       "mscVrPpTbclSnmpOperStatus": mscVrPpTbclSnmpOperStatus,
       "mscVrPpTbclOperTable": mscVrPpTbclOperTable,
       "mscVrPpTbclOperEntry": mscVrPpTbclOperEntry,
       "mscVrPpTbclPortName": mscVrPpTbclPortName,
       "mscVrPpTbclUpTime": mscVrPpTbclUpTime,
       "mscVrPpTbclDownTime": mscVrPpTbclDownTime,
       "mscVrPpTbclBridgingMode": mscVrPpTbclBridgingMode,
       "mscVrPpTbclBridgePortConfig": mscVrPpTbclBridgePortConfig,
       "mscVrPpTbclBridgePortType": mscVrPpTbclBridgePortType,
       "mscVrPpTbclIfIndex": mscVrPpTbclIfIndex,
       "mscVrPpTbclDelayExceededDiscards": mscVrPpTbclDelayExceededDiscards,
       "mscVrPpTbclMtuExceededDiscards": mscVrPpTbclMtuExceededDiscards,
       "mscVrPpTbclTbOperTable": mscVrPpTbclTbOperTable,
       "mscVrPpTbclTbOperEntry": mscVrPpTbclTbOperEntry,
       "mscVrPpTbclMaxInfo": mscVrPpTbclMaxInfo,
       "mscVrPpTbclBadVerifyDiscards": mscVrPpTbclBadVerifyDiscards,
       "mscVrPpTbclUnicastNoMatches": mscVrPpTbclUnicastNoMatches,
       "mscVrPpTbclStaticEntryDiscards": mscVrPpTbclStaticEntryDiscards,
       "mscVrPpTbclDynamicEntryDiscards": mscVrPpTbclDynamicEntryDiscards,
       "mscVrPpTbclLearningDiscards": mscVrPpTbclLearningDiscards,
       "mscVrPpTbclInDiscards": mscVrPpTbclInDiscards,
       "mscVrPpTbclInFrames": mscVrPpTbclInFrames,
       "mscVrPpTbclOutFrames": mscVrPpTbclOutFrames,
       "mscVrPpTbclStpOperTable": mscVrPpTbclStpOperTable,
       "mscVrPpTbclStpOperEntry": mscVrPpTbclStpOperEntry,
       "mscVrPpTbclStpPortState": mscVrPpTbclStpPortState,
       "mscVrPpTbclStpTypeOper": mscVrPpTbclStpTypeOper,
       "mscVrPpTbclDesignatedCost": mscVrPpTbclDesignatedCost,
       "mscVrPpTbclPathCostOper": mscVrPpTbclPathCostOper,
       "mscVrPpTbclDesignatedBridge": mscVrPpTbclDesignatedBridge,
       "mscVrPpTbclDesignatedPort": mscVrPpTbclDesignatedPort,
       "mscVrPpTbclForwardTransitions": mscVrPpTbclForwardTransitions,
       "mscVrPpTbclBlockingDiscards": mscVrPpTbclBlockingDiscards,
       "mscVrPpTbclDesignatedRoot": mscVrPpTbclDesignatedRoot,
       "mscVrPpTbclStatsTable": mscVrPpTbclStatsTable,
       "mscVrPpTbclStatsEntry": mscVrPpTbclStatsEntry,
       "mscVrPpTbclBadAbstractDiscards": mscVrPpTbclBadAbstractDiscards,
       "mscVrPpTbclTinygramFramesIn": mscVrPpTbclTinygramFramesIn,
       "mscVrPpTbclTinygramFramesOut": mscVrPpTbclTinygramFramesOut,
       "mscVrPpTbclInFilterDiscards": mscVrPpTbclInFilterDiscards,
       "mscVrPpTbclOutFilterDiscards": mscVrPpTbclOutFilterDiscards,
       "mscVrPpFddiETB": mscVrPpFddiETB,
       "mscVrPpFddiETBRowStatusTable": mscVrPpFddiETBRowStatusTable,
       "mscVrPpFddiETBRowStatusEntry": mscVrPpFddiETBRowStatusEntry,
       "mscVrPpFddiETBRowStatus": mscVrPpFddiETBRowStatus,
       "mscVrPpFddiETBComponentName": mscVrPpFddiETBComponentName,
       "mscVrPpFddiETBStorageType": mscVrPpFddiETBStorageType,
       "mscVrPpFddiETBIndex": mscVrPpFddiETBIndex,
       "mscVrPpFddiETBNs": mscVrPpFddiETBNs,
       "mscVrPpFddiETBNsRowStatusTable": mscVrPpFddiETBNsRowStatusTable,
       "mscVrPpFddiETBNsRowStatusEntry": mscVrPpFddiETBNsRowStatusEntry,
       "mscVrPpFddiETBNsRowStatus": mscVrPpFddiETBNsRowStatus,
       "mscVrPpFddiETBNsComponentName": mscVrPpFddiETBNsComponentName,
       "mscVrPpFddiETBNsStorageType": mscVrPpFddiETBNsStorageType,
       "mscVrPpFddiETBNsIndex": mscVrPpFddiETBNsIndex,
       "mscVrPpFddiETBNsProvTable": mscVrPpFddiETBNsProvTable,
       "mscVrPpFddiETBNsProvEntry": mscVrPpFddiETBNsProvEntry,
       "mscVrPpFddiETBNsIncomingFilter": mscVrPpFddiETBNsIncomingFilter,
       "mscVrPpFddiETBNsOutgoingFilter": mscVrPpFddiETBNsOutgoingFilter,
       "mscVrPpFddiETBProvTable": mscVrPpFddiETBProvTable,
       "mscVrPpFddiETBProvEntry": mscVrPpFddiETBProvEntry,
       "mscVrPpFddiETBTranslateIpx": mscVrPpFddiETBTranslateIpx,
       "mscVrPpFddiETBFragmentIp": mscVrPpFddiETBFragmentIp,
       "mscVrPpFddiETBServiceClass": mscVrPpFddiETBServiceClass,
       "mscVrPpFddiETBConvertArpMacAddress": mscVrPpFddiETBConvertArpMacAddress,
       "mscVrPpFddiETBPortNum": mscVrPpFddiETBPortNum,
       "mscVrPpFddiETBTbProvTable": mscVrPpFddiETBTbProvTable,
       "mscVrPpFddiETBTbProvEntry": mscVrPpFddiETBTbProvEntry,
       "mscVrPpFddiETBSecureOption": mscVrPpFddiETBSecureOption,
       "mscVrPpFddiETBStpProvTable": mscVrPpFddiETBStpProvTable,
       "mscVrPpFddiETBStpProvEntry": mscVrPpFddiETBStpProvEntry,
       "mscVrPpFddiETBAdminStatus": mscVrPpFddiETBAdminStatus,
       "mscVrPpFddiETBPortStateStpControl": mscVrPpFddiETBPortStateStpControl,
       "mscVrPpFddiETBStpTypeProv": mscVrPpFddiETBStpTypeProv,
       "mscVrPpFddiETBPortPriority": mscVrPpFddiETBPortPriority,
       "mscVrPpFddiETBPathCost": mscVrPpFddiETBPathCost,
       "mscVrPpFddiETBPathCostMethod": mscVrPpFddiETBPathCostMethod,
       "mscVrPpFddiETBDIProvTable": mscVrPpFddiETBDIProvTable,
       "mscVrPpFddiETBDIProvEntry": mscVrPpFddiETBDIProvEntry,
       "mscVrPpFddiETBDomainNum": mscVrPpFddiETBDomainNum,
       "mscVrPpFddiETBPreserveDomain": mscVrPpFddiETBPreserveDomain,
       "mscVrPpFddiETBStateTable": mscVrPpFddiETBStateTable,
       "mscVrPpFddiETBStateEntry": mscVrPpFddiETBStateEntry,
       "mscVrPpFddiETBAdminState": mscVrPpFddiETBAdminState,
       "mscVrPpFddiETBOperationalState": mscVrPpFddiETBOperationalState,
       "mscVrPpFddiETBUsageState": mscVrPpFddiETBUsageState,
       "mscVrPpFddiETBOperStatusTable": mscVrPpFddiETBOperStatusTable,
       "mscVrPpFddiETBOperStatusEntry": mscVrPpFddiETBOperStatusEntry,
       "mscVrPpFddiETBSnmpOperStatus": mscVrPpFddiETBSnmpOperStatus,
       "mscVrPpFddiETBOperTable": mscVrPpFddiETBOperTable,
       "mscVrPpFddiETBOperEntry": mscVrPpFddiETBOperEntry,
       "mscVrPpFddiETBPortName": mscVrPpFddiETBPortName,
       "mscVrPpFddiETBUpTime": mscVrPpFddiETBUpTime,
       "mscVrPpFddiETBDownTime": mscVrPpFddiETBDownTime,
       "mscVrPpFddiETBBridgingMode": mscVrPpFddiETBBridgingMode,
       "mscVrPpFddiETBBridgePortConfig": mscVrPpFddiETBBridgePortConfig,
       "mscVrPpFddiETBBridgePortType": mscVrPpFddiETBBridgePortType,
       "mscVrPpFddiETBIfIndex": mscVrPpFddiETBIfIndex,
       "mscVrPpFddiETBDelayExceededDiscards": mscVrPpFddiETBDelayExceededDiscards,
       "mscVrPpFddiETBMtuExceededDiscards": mscVrPpFddiETBMtuExceededDiscards,
       "mscVrPpFddiETBTbOperTable": mscVrPpFddiETBTbOperTable,
       "mscVrPpFddiETBTbOperEntry": mscVrPpFddiETBTbOperEntry,
       "mscVrPpFddiETBMaxInfo": mscVrPpFddiETBMaxInfo,
       "mscVrPpFddiETBBadVerifyDiscards": mscVrPpFddiETBBadVerifyDiscards,
       "mscVrPpFddiETBUnicastNoMatches": mscVrPpFddiETBUnicastNoMatches,
       "mscVrPpFddiETBStaticEntryDiscards": mscVrPpFddiETBStaticEntryDiscards,
       "mscVrPpFddiETBDynamicEntryDiscards": mscVrPpFddiETBDynamicEntryDiscards,
       "mscVrPpFddiETBLearningDiscards": mscVrPpFddiETBLearningDiscards,
       "mscVrPpFddiETBInDiscards": mscVrPpFddiETBInDiscards,
       "mscVrPpFddiETBInFrames": mscVrPpFddiETBInFrames,
       "mscVrPpFddiETBOutFrames": mscVrPpFddiETBOutFrames,
       "mscVrPpFddiETBStpOperTable": mscVrPpFddiETBStpOperTable,
       "mscVrPpFddiETBStpOperEntry": mscVrPpFddiETBStpOperEntry,
       "mscVrPpFddiETBStpPortState": mscVrPpFddiETBStpPortState,
       "mscVrPpFddiETBStpTypeOper": mscVrPpFddiETBStpTypeOper,
       "mscVrPpFddiETBDesignatedCost": mscVrPpFddiETBDesignatedCost,
       "mscVrPpFddiETBPathCostOper": mscVrPpFddiETBPathCostOper,
       "mscVrPpFddiETBDesignatedBridge": mscVrPpFddiETBDesignatedBridge,
       "mscVrPpFddiETBDesignatedPort": mscVrPpFddiETBDesignatedPort,
       "mscVrPpFddiETBForwardTransitions": mscVrPpFddiETBForwardTransitions,
       "mscVrPpFddiETBBlockingDiscards": mscVrPpFddiETBBlockingDiscards,
       "mscVrPpFddiETBDesignatedRoot": mscVrPpFddiETBDesignatedRoot,
       "mscVrPpFddiETBStatsTable": mscVrPpFddiETBStatsTable,
       "mscVrPpFddiETBStatsEntry": mscVrPpFddiETBStatsEntry,
       "mscVrPpFddiETBBadAbstractDiscards": mscVrPpFddiETBBadAbstractDiscards,
       "mscVrPpFddiETBTinygramFramesIn": mscVrPpFddiETBTinygramFramesIn,
       "mscVrPpFddiETBTinygramFramesOut": mscVrPpFddiETBTinygramFramesOut,
       "mscVrPpFddiETBInFilterDiscards": mscVrPpFddiETBInFilterDiscards,
       "mscVrPpFddiETBOutFilterDiscards": mscVrPpFddiETBOutFilterDiscards,
       "mscVrPpTbp": mscVrPpTbp,
       "mscVrPpTbpRowStatusTable": mscVrPpTbpRowStatusTable,
       "mscVrPpTbpRowStatusEntry": mscVrPpTbpRowStatusEntry,
       "mscVrPpTbpRowStatus": mscVrPpTbpRowStatus,
       "mscVrPpTbpComponentName": mscVrPpTbpComponentName,
       "mscVrPpTbpStorageType": mscVrPpTbpStorageType,
       "mscVrPpTbpIndex": mscVrPpTbpIndex,
       "mscVrPpTbpNs": mscVrPpTbpNs,
       "mscVrPpTbpNsRowStatusTable": mscVrPpTbpNsRowStatusTable,
       "mscVrPpTbpNsRowStatusEntry": mscVrPpTbpNsRowStatusEntry,
       "mscVrPpTbpNsRowStatus": mscVrPpTbpNsRowStatus,
       "mscVrPpTbpNsComponentName": mscVrPpTbpNsComponentName,
       "mscVrPpTbpNsStorageType": mscVrPpTbpNsStorageType,
       "mscVrPpTbpNsIndex": mscVrPpTbpNsIndex,
       "mscVrPpTbpNsProvTable": mscVrPpTbpNsProvTable,
       "mscVrPpTbpNsProvEntry": mscVrPpTbpNsProvEntry,
       "mscVrPpTbpNsIncomingFilter": mscVrPpTbpNsIncomingFilter,
       "mscVrPpTbpNsOutgoingFilter": mscVrPpTbpNsOutgoingFilter,
       "mscVrPpTbpProvTable": mscVrPpTbpProvTable,
       "mscVrPpTbpProvEntry": mscVrPpTbpProvEntry,
       "mscVrPpTbpTranslateIpx": mscVrPpTbpTranslateIpx,
       "mscVrPpTbpFragmentIp": mscVrPpTbpFragmentIp,
       "mscVrPpTbpServiceClass": mscVrPpTbpServiceClass,
       "mscVrPpTbpConvertArpMacAddress": mscVrPpTbpConvertArpMacAddress,
       "mscVrPpTbpPortNum": mscVrPpTbpPortNum,
       "mscVrPpTbpTbProvTable": mscVrPpTbpTbProvTable,
       "mscVrPpTbpTbProvEntry": mscVrPpTbpTbProvEntry,
       "mscVrPpTbpSecureOption": mscVrPpTbpSecureOption,
       "mscVrPpTbpStpProvTable": mscVrPpTbpStpProvTable,
       "mscVrPpTbpStpProvEntry": mscVrPpTbpStpProvEntry,
       "mscVrPpTbpAdminStatus": mscVrPpTbpAdminStatus,
       "mscVrPpTbpPortStateStpControl": mscVrPpTbpPortStateStpControl,
       "mscVrPpTbpStpTypeProv": mscVrPpTbpStpTypeProv,
       "mscVrPpTbpPortPriority": mscVrPpTbpPortPriority,
       "mscVrPpTbpPathCost": mscVrPpTbpPathCost,
       "mscVrPpTbpPathCostMethod": mscVrPpTbpPathCostMethod,
       "mscVrPpTbpDIProvTable": mscVrPpTbpDIProvTable,
       "mscVrPpTbpDIProvEntry": mscVrPpTbpDIProvEntry,
       "mscVrPpTbpDomainNum": mscVrPpTbpDomainNum,
       "mscVrPpTbpPreserveDomain": mscVrPpTbpPreserveDomain,
       "mscVrPpTbpStateTable": mscVrPpTbpStateTable,
       "mscVrPpTbpStateEntry": mscVrPpTbpStateEntry,
       "mscVrPpTbpAdminState": mscVrPpTbpAdminState,
       "mscVrPpTbpOperationalState": mscVrPpTbpOperationalState,
       "mscVrPpTbpUsageState": mscVrPpTbpUsageState,
       "mscVrPpTbpOperStatusTable": mscVrPpTbpOperStatusTable,
       "mscVrPpTbpOperStatusEntry": mscVrPpTbpOperStatusEntry,
       "mscVrPpTbpSnmpOperStatus": mscVrPpTbpSnmpOperStatus,
       "mscVrPpTbpOperTable": mscVrPpTbpOperTable,
       "mscVrPpTbpOperEntry": mscVrPpTbpOperEntry,
       "mscVrPpTbpPortName": mscVrPpTbpPortName,
       "mscVrPpTbpUpTime": mscVrPpTbpUpTime,
       "mscVrPpTbpDownTime": mscVrPpTbpDownTime,
       "mscVrPpTbpBridgingMode": mscVrPpTbpBridgingMode,
       "mscVrPpTbpBridgePortConfig": mscVrPpTbpBridgePortConfig,
       "mscVrPpTbpBridgePortType": mscVrPpTbpBridgePortType,
       "mscVrPpTbpIfIndex": mscVrPpTbpIfIndex,
       "mscVrPpTbpDelayExceededDiscards": mscVrPpTbpDelayExceededDiscards,
       "mscVrPpTbpMtuExceededDiscards": mscVrPpTbpMtuExceededDiscards,
       "mscVrPpTbpTbOperTable": mscVrPpTbpTbOperTable,
       "mscVrPpTbpTbOperEntry": mscVrPpTbpTbOperEntry,
       "mscVrPpTbpMaxInfo": mscVrPpTbpMaxInfo,
       "mscVrPpTbpBadVerifyDiscards": mscVrPpTbpBadVerifyDiscards,
       "mscVrPpTbpUnicastNoMatches": mscVrPpTbpUnicastNoMatches,
       "mscVrPpTbpStaticEntryDiscards": mscVrPpTbpStaticEntryDiscards,
       "mscVrPpTbpDynamicEntryDiscards": mscVrPpTbpDynamicEntryDiscards,
       "mscVrPpTbpLearningDiscards": mscVrPpTbpLearningDiscards,
       "mscVrPpTbpInDiscards": mscVrPpTbpInDiscards,
       "mscVrPpTbpInFrames": mscVrPpTbpInFrames,
       "mscVrPpTbpOutFrames": mscVrPpTbpOutFrames,
       "mscVrPpTbpStpOperTable": mscVrPpTbpStpOperTable,
       "mscVrPpTbpStpOperEntry": mscVrPpTbpStpOperEntry,
       "mscVrPpTbpStpPortState": mscVrPpTbpStpPortState,
       "mscVrPpTbpStpTypeOper": mscVrPpTbpStpTypeOper,
       "mscVrPpTbpDesignatedCost": mscVrPpTbpDesignatedCost,
       "mscVrPpTbpPathCostOper": mscVrPpTbpPathCostOper,
       "mscVrPpTbpDesignatedBridge": mscVrPpTbpDesignatedBridge,
       "mscVrPpTbpDesignatedPort": mscVrPpTbpDesignatedPort,
       "mscVrPpTbpForwardTransitions": mscVrPpTbpForwardTransitions,
       "mscVrPpTbpBlockingDiscards": mscVrPpTbpBlockingDiscards,
       "mscVrPpTbpDesignatedRoot": mscVrPpTbpDesignatedRoot,
       "mscVrPpTbpStatsTable": mscVrPpTbpStatsTable,
       "mscVrPpTbpStatsEntry": mscVrPpTbpStatsEntry,
       "mscVrPpTbpBadAbstractDiscards": mscVrPpTbpBadAbstractDiscards,
       "mscVrPpTbpTinygramFramesIn": mscVrPpTbpTinygramFramesIn,
       "mscVrPpTbpTinygramFramesOut": mscVrPpTbpTinygramFramesOut,
       "mscVrPpTbpInFilterDiscards": mscVrPpTbpInFilterDiscards,
       "mscVrPpTbpOutFilterDiscards": mscVrPpTbpOutFilterDiscards,
       "mscVrPpSrBp": mscVrPpSrBp,
       "mscVrPpSrBpRowStatusTable": mscVrPpSrBpRowStatusTable,
       "mscVrPpSrBpRowStatusEntry": mscVrPpSrBpRowStatusEntry,
       "mscVrPpSrBpRowStatus": mscVrPpSrBpRowStatus,
       "mscVrPpSrBpComponentName": mscVrPpSrBpComponentName,
       "mscVrPpSrBpStorageType": mscVrPpSrBpStorageType,
       "mscVrPpSrBpIndex": mscVrPpSrBpIndex,
       "mscVrPpSrBpNs": mscVrPpSrBpNs,
       "mscVrPpSrBpNsRowStatusTable": mscVrPpSrBpNsRowStatusTable,
       "mscVrPpSrBpNsRowStatusEntry": mscVrPpSrBpNsRowStatusEntry,
       "mscVrPpSrBpNsRowStatus": mscVrPpSrBpNsRowStatus,
       "mscVrPpSrBpNsComponentName": mscVrPpSrBpNsComponentName,
       "mscVrPpSrBpNsStorageType": mscVrPpSrBpNsStorageType,
       "mscVrPpSrBpNsIndex": mscVrPpSrBpNsIndex,
       "mscVrPpSrBpNsProvTable": mscVrPpSrBpNsProvTable,
       "mscVrPpSrBpNsProvEntry": mscVrPpSrBpNsProvEntry,
       "mscVrPpSrBpNsIncomingFilter": mscVrPpSrBpNsIncomingFilter,
       "mscVrPpSrBpNsOutgoingFilter": mscVrPpSrBpNsOutgoingFilter,
       "mscVrPpSrBpProvTable": mscVrPpSrBpProvTable,
       "mscVrPpSrBpProvEntry": mscVrPpSrBpProvEntry,
       "mscVrPpSrBpTranslateIpx": mscVrPpSrBpTranslateIpx,
       "mscVrPpSrBpFragmentIp": mscVrPpSrBpFragmentIp,
       "mscVrPpSrBpServiceClass": mscVrPpSrBpServiceClass,
       "mscVrPpSrBpConvertArpMacAddress": mscVrPpSrBpConvertArpMacAddress,
       "mscVrPpSrBpPortNum": mscVrPpSrBpPortNum,
       "mscVrPpSrBpStpProvTable": mscVrPpSrBpStpProvTable,
       "mscVrPpSrBpStpProvEntry": mscVrPpSrBpStpProvEntry,
       "mscVrPpSrBpAdminStatus": mscVrPpSrBpAdminStatus,
       "mscVrPpSrBpPortStateStpControl": mscVrPpSrBpPortStateStpControl,
       "mscVrPpSrBpStpTypeProv": mscVrPpSrBpStpTypeProv,
       "mscVrPpSrBpPortPriority": mscVrPpSrBpPortPriority,
       "mscVrPpSrBpPathCost": mscVrPpSrBpPathCost,
       "mscVrPpSrBpPathCostMethod": mscVrPpSrBpPathCostMethod,
       "mscVrPpSrBpDIProvTable": mscVrPpSrBpDIProvTable,
       "mscVrPpSrBpDIProvEntry": mscVrPpSrBpDIProvEntry,
       "mscVrPpSrBpDomainNum": mscVrPpSrBpDomainNum,
       "mscVrPpSrBpPreserveDomain": mscVrPpSrBpPreserveDomain,
       "mscVrPpSrBpStateTable": mscVrPpSrBpStateTable,
       "mscVrPpSrBpStateEntry": mscVrPpSrBpStateEntry,
       "mscVrPpSrBpAdminState": mscVrPpSrBpAdminState,
       "mscVrPpSrBpOperationalState": mscVrPpSrBpOperationalState,
       "mscVrPpSrBpUsageState": mscVrPpSrBpUsageState,
       "mscVrPpSrBpOperStatusTable": mscVrPpSrBpOperStatusTable,
       "mscVrPpSrBpOperStatusEntry": mscVrPpSrBpOperStatusEntry,
       "mscVrPpSrBpSnmpOperStatus": mscVrPpSrBpSnmpOperStatus,
       "mscVrPpSrBpOperTable": mscVrPpSrBpOperTable,
       "mscVrPpSrBpOperEntry": mscVrPpSrBpOperEntry,
       "mscVrPpSrBpPortName": mscVrPpSrBpPortName,
       "mscVrPpSrBpUpTime": mscVrPpSrBpUpTime,
       "mscVrPpSrBpDownTime": mscVrPpSrBpDownTime,
       "mscVrPpSrBpBridgingMode": mscVrPpSrBpBridgingMode,
       "mscVrPpSrBpBridgePortConfig": mscVrPpSrBpBridgePortConfig,
       "mscVrPpSrBpBridgePortType": mscVrPpSrBpBridgePortType,
       "mscVrPpSrBpIfIndex": mscVrPpSrBpIfIndex,
       "mscVrPpSrBpDelayExceededDiscards": mscVrPpSrBpDelayExceededDiscards,
       "mscVrPpSrBpMtuExceededDiscards": mscVrPpSrBpMtuExceededDiscards,
       "mscVrPpSrBpStpOperTable": mscVrPpSrBpStpOperTable,
       "mscVrPpSrBpStpOperEntry": mscVrPpSrBpStpOperEntry,
       "mscVrPpSrBpStpPortState": mscVrPpSrBpStpPortState,
       "mscVrPpSrBpStpTypeOper": mscVrPpSrBpStpTypeOper,
       "mscVrPpSrBpDesignatedCost": mscVrPpSrBpDesignatedCost,
       "mscVrPpSrBpPathCostOper": mscVrPpSrBpPathCostOper,
       "mscVrPpSrBpDesignatedBridge": mscVrPpSrBpDesignatedBridge,
       "mscVrPpSrBpDesignatedPort": mscVrPpSrBpDesignatedPort,
       "mscVrPpSrBpForwardTransitions": mscVrPpSrBpForwardTransitions,
       "mscVrPpSrBpBlockingDiscards": mscVrPpSrBpBlockingDiscards,
       "mscVrPpSrBpDesignatedRoot": mscVrPpSrBpDesignatedRoot,
       "mscVrPpSrBpStatsTable": mscVrPpSrBpStatsTable,
       "mscVrPpSrBpStatsEntry": mscVrPpSrBpStatsEntry,
       "mscVrPpSrBpBadAbstractDiscards": mscVrPpSrBpBadAbstractDiscards,
       "mscVrPpSrBpTinygramFramesIn": mscVrPpSrBpTinygramFramesIn,
       "mscVrPpSrBpTinygramFramesOut": mscVrPpSrBpTinygramFramesOut,
       "mscVrPpSrBpInFilterDiscards": mscVrPpSrBpInFilterDiscards,
       "mscVrPpSrBpOutFilterDiscards": mscVrPpSrBpOutFilterDiscards,
       "mscVrPpSrBpSrProvTable": mscVrPpSrBpSrProvTable,
       "mscVrPpSrBpSrProvEntry": mscVrPpSrBpSrProvEntry,
       "mscVrPpSrBpHopCount": mscVrPpSrBpHopCount,
       "mscVrPpSrBpExploreFrameTreatment": mscVrPpSrBpExploreFrameTreatment,
       "mscVrPpSrBpLanId": mscVrPpSrBpLanId,
       "mscVrPpSrBpInternalLanId": mscVrPpSrBpInternalLanId,
       "mscVrPpSrBpBridgeNum": mscVrPpSrBpBridgeNum,
       "mscVrPpSrBpLargestFrame": mscVrPpSrBpLargestFrame,
       "mscVrPpSrBpSteSpanMode": mscVrPpSrBpSteSpanMode,
       "mscVrPpSrBpAreRdLimit": mscVrPpSrBpAreRdLimit,
       "mscVrPpSrBpSteRdLimit": mscVrPpSrBpSteRdLimit,
       "mscVrPpSrBpSrStatsTable": mscVrPpSrBpSrStatsTable,
       "mscVrPpSrBpSrStatsEntry": mscVrPpSrBpSrStatsEntry,
       "mscVrPpSrBpSpecInFrames": mscVrPpSrBpSpecInFrames,
       "mscVrPpSrBpSpecOutFrames": mscVrPpSrBpSpecOutFrames,
       "mscVrPpSrBpApeInFrames": mscVrPpSrBpApeInFrames,
       "mscVrPpSrBpApeOutFrames": mscVrPpSrBpApeOutFrames,
       "mscVrPpSrBpSteInFrames": mscVrPpSrBpSteInFrames,
       "mscVrPpSrBpSteOutFrames": mscVrPpSrBpSteOutFrames,
       "mscVrPpSrBpSegmentMismatchDiscards": mscVrPpSrBpSegmentMismatchDiscards,
       "mscVrPpSrBpDupSegmentDiscards": mscVrPpSrBpDupSegmentDiscards,
       "mscVrPpSrBpHopCountExceededDiscards": mscVrPpSrBpHopCountExceededDiscards,
       "mscVrPpSrBpDupLanIdOrTreeErrors": mscVrPpSrBpDupLanIdOrTreeErrors,
       "mscVrPpSrBpLanIdMismatches": mscVrPpSrBpLanIdMismatches,
       "mscVrPpSrBpStaticDiscards": mscVrPpSrBpStaticDiscards,
       "mscVrPpSrBpDynamicDiscards": mscVrPpSrBpDynamicDiscards,
       "mscVrPpSrtBp": mscVrPpSrtBp,
       "mscVrPpSrtBpRowStatusTable": mscVrPpSrtBpRowStatusTable,
       "mscVrPpSrtBpRowStatusEntry": mscVrPpSrtBpRowStatusEntry,
       "mscVrPpSrtBpRowStatus": mscVrPpSrtBpRowStatus,
       "mscVrPpSrtBpComponentName": mscVrPpSrtBpComponentName,
       "mscVrPpSrtBpStorageType": mscVrPpSrtBpStorageType,
       "mscVrPpSrtBpIndex": mscVrPpSrtBpIndex,
       "mscVrPpSrtBpNs": mscVrPpSrtBpNs,
       "mscVrPpSrtBpNsRowStatusTable": mscVrPpSrtBpNsRowStatusTable,
       "mscVrPpSrtBpNsRowStatusEntry": mscVrPpSrtBpNsRowStatusEntry,
       "mscVrPpSrtBpNsRowStatus": mscVrPpSrtBpNsRowStatus,
       "mscVrPpSrtBpNsComponentName": mscVrPpSrtBpNsComponentName,
       "mscVrPpSrtBpNsStorageType": mscVrPpSrtBpNsStorageType,
       "mscVrPpSrtBpNsIndex": mscVrPpSrtBpNsIndex,
       "mscVrPpSrtBpNsProvTable": mscVrPpSrtBpNsProvTable,
       "mscVrPpSrtBpNsProvEntry": mscVrPpSrtBpNsProvEntry,
       "mscVrPpSrtBpNsIncomingFilter": mscVrPpSrtBpNsIncomingFilter,
       "mscVrPpSrtBpNsOutgoingFilter": mscVrPpSrtBpNsOutgoingFilter,
       "mscVrPpSrtBpProvTable": mscVrPpSrtBpProvTable,
       "mscVrPpSrtBpProvEntry": mscVrPpSrtBpProvEntry,
       "mscVrPpSrtBpTranslateIpx": mscVrPpSrtBpTranslateIpx,
       "mscVrPpSrtBpFragmentIp": mscVrPpSrtBpFragmentIp,
       "mscVrPpSrtBpServiceClass": mscVrPpSrtBpServiceClass,
       "mscVrPpSrtBpConvertArpMacAddress": mscVrPpSrtBpConvertArpMacAddress,
       "mscVrPpSrtBpPortNum": mscVrPpSrtBpPortNum,
       "mscVrPpSrtBpTbProvTable": mscVrPpSrtBpTbProvTable,
       "mscVrPpSrtBpTbProvEntry": mscVrPpSrtBpTbProvEntry,
       "mscVrPpSrtBpSecureOption": mscVrPpSrtBpSecureOption,
       "mscVrPpSrtBpStpProvTable": mscVrPpSrtBpStpProvTable,
       "mscVrPpSrtBpStpProvEntry": mscVrPpSrtBpStpProvEntry,
       "mscVrPpSrtBpAdminStatus": mscVrPpSrtBpAdminStatus,
       "mscVrPpSrtBpPortStateStpControl": mscVrPpSrtBpPortStateStpControl,
       "mscVrPpSrtBpStpTypeProv": mscVrPpSrtBpStpTypeProv,
       "mscVrPpSrtBpPortPriority": mscVrPpSrtBpPortPriority,
       "mscVrPpSrtBpPathCost": mscVrPpSrtBpPathCost,
       "mscVrPpSrtBpPathCostMethod": mscVrPpSrtBpPathCostMethod,
       "mscVrPpSrtBpDIProvTable": mscVrPpSrtBpDIProvTable,
       "mscVrPpSrtBpDIProvEntry": mscVrPpSrtBpDIProvEntry,
       "mscVrPpSrtBpDomainNum": mscVrPpSrtBpDomainNum,
       "mscVrPpSrtBpPreserveDomain": mscVrPpSrtBpPreserveDomain,
       "mscVrPpSrtBpStateTable": mscVrPpSrtBpStateTable,
       "mscVrPpSrtBpStateEntry": mscVrPpSrtBpStateEntry,
       "mscVrPpSrtBpAdminState": mscVrPpSrtBpAdminState,
       "mscVrPpSrtBpOperationalState": mscVrPpSrtBpOperationalState,
       "mscVrPpSrtBpUsageState": mscVrPpSrtBpUsageState,
       "mscVrPpSrtBpOperStatusTable": mscVrPpSrtBpOperStatusTable,
       "mscVrPpSrtBpOperStatusEntry": mscVrPpSrtBpOperStatusEntry,
       "mscVrPpSrtBpSnmpOperStatus": mscVrPpSrtBpSnmpOperStatus,
       "mscVrPpSrtBpOperTable": mscVrPpSrtBpOperTable,
       "mscVrPpSrtBpOperEntry": mscVrPpSrtBpOperEntry,
       "mscVrPpSrtBpPortName": mscVrPpSrtBpPortName,
       "mscVrPpSrtBpUpTime": mscVrPpSrtBpUpTime,
       "mscVrPpSrtBpDownTime": mscVrPpSrtBpDownTime,
       "mscVrPpSrtBpBridgingMode": mscVrPpSrtBpBridgingMode,
       "mscVrPpSrtBpBridgePortConfig": mscVrPpSrtBpBridgePortConfig,
       "mscVrPpSrtBpBridgePortType": mscVrPpSrtBpBridgePortType,
       "mscVrPpSrtBpIfIndex": mscVrPpSrtBpIfIndex,
       "mscVrPpSrtBpDelayExceededDiscards": mscVrPpSrtBpDelayExceededDiscards,
       "mscVrPpSrtBpMtuExceededDiscards": mscVrPpSrtBpMtuExceededDiscards,
       "mscVrPpSrtBpTbOperTable": mscVrPpSrtBpTbOperTable,
       "mscVrPpSrtBpTbOperEntry": mscVrPpSrtBpTbOperEntry,
       "mscVrPpSrtBpMaxInfo": mscVrPpSrtBpMaxInfo,
       "mscVrPpSrtBpBadVerifyDiscards": mscVrPpSrtBpBadVerifyDiscards,
       "mscVrPpSrtBpUnicastNoMatches": mscVrPpSrtBpUnicastNoMatches,
       "mscVrPpSrtBpStaticEntryDiscards": mscVrPpSrtBpStaticEntryDiscards,
       "mscVrPpSrtBpDynamicEntryDiscards": mscVrPpSrtBpDynamicEntryDiscards,
       "mscVrPpSrtBpLearningDiscards": mscVrPpSrtBpLearningDiscards,
       "mscVrPpSrtBpInDiscards": mscVrPpSrtBpInDiscards,
       "mscVrPpSrtBpInFrames": mscVrPpSrtBpInFrames,
       "mscVrPpSrtBpOutFrames": mscVrPpSrtBpOutFrames,
       "mscVrPpSrtBpStpOperTable": mscVrPpSrtBpStpOperTable,
       "mscVrPpSrtBpStpOperEntry": mscVrPpSrtBpStpOperEntry,
       "mscVrPpSrtBpStpPortState": mscVrPpSrtBpStpPortState,
       "mscVrPpSrtBpStpTypeOper": mscVrPpSrtBpStpTypeOper,
       "mscVrPpSrtBpDesignatedCost": mscVrPpSrtBpDesignatedCost,
       "mscVrPpSrtBpPathCostOper": mscVrPpSrtBpPathCostOper,
       "mscVrPpSrtBpDesignatedBridge": mscVrPpSrtBpDesignatedBridge,
       "mscVrPpSrtBpDesignatedPort": mscVrPpSrtBpDesignatedPort,
       "mscVrPpSrtBpForwardTransitions": mscVrPpSrtBpForwardTransitions,
       "mscVrPpSrtBpBlockingDiscards": mscVrPpSrtBpBlockingDiscards,
       "mscVrPpSrtBpDesignatedRoot": mscVrPpSrtBpDesignatedRoot,
       "mscVrPpSrtBpStatsTable": mscVrPpSrtBpStatsTable,
       "mscVrPpSrtBpStatsEntry": mscVrPpSrtBpStatsEntry,
       "mscVrPpSrtBpBadAbstractDiscards": mscVrPpSrtBpBadAbstractDiscards,
       "mscVrPpSrtBpTinygramFramesIn": mscVrPpSrtBpTinygramFramesIn,
       "mscVrPpSrtBpTinygramFramesOut": mscVrPpSrtBpTinygramFramesOut,
       "mscVrPpSrtBpInFilterDiscards": mscVrPpSrtBpInFilterDiscards,
       "mscVrPpSrtBpOutFilterDiscards": mscVrPpSrtBpOutFilterDiscards,
       "mscVrPpSrtBpSrProvTable": mscVrPpSrtBpSrProvTable,
       "mscVrPpSrtBpSrProvEntry": mscVrPpSrtBpSrProvEntry,
       "mscVrPpSrtBpHopCount": mscVrPpSrtBpHopCount,
       "mscVrPpSrtBpExploreFrameTreatment": mscVrPpSrtBpExploreFrameTreatment,
       "mscVrPpSrtBpLanId": mscVrPpSrtBpLanId,
       "mscVrPpSrtBpInternalLanId": mscVrPpSrtBpInternalLanId,
       "mscVrPpSrtBpBridgeNum": mscVrPpSrtBpBridgeNum,
       "mscVrPpSrtBpLargestFrame": mscVrPpSrtBpLargestFrame,
       "mscVrPpSrtBpSteSpanMode": mscVrPpSrtBpSteSpanMode,
       "mscVrPpSrtBpAreRdLimit": mscVrPpSrtBpAreRdLimit,
       "mscVrPpSrtBpSteRdLimit": mscVrPpSrtBpSteRdLimit,
       "mscVrPpSrtBpSrStatsTable": mscVrPpSrtBpSrStatsTable,
       "mscVrPpSrtBpSrStatsEntry": mscVrPpSrtBpSrStatsEntry,
       "mscVrPpSrtBpSpecInFrames": mscVrPpSrtBpSpecInFrames,
       "mscVrPpSrtBpSpecOutFrames": mscVrPpSrtBpSpecOutFrames,
       "mscVrPpSrtBpApeInFrames": mscVrPpSrtBpApeInFrames,
       "mscVrPpSrtBpApeOutFrames": mscVrPpSrtBpApeOutFrames,
       "mscVrPpSrtBpSteInFrames": mscVrPpSrtBpSteInFrames,
       "mscVrPpSrtBpSteOutFrames": mscVrPpSrtBpSteOutFrames,
       "mscVrPpSrtBpSegmentMismatchDiscards": mscVrPpSrtBpSegmentMismatchDiscards,
       "mscVrPpSrtBpDupSegmentDiscards": mscVrPpSrtBpDupSegmentDiscards,
       "mscVrPpSrtBpHopCountExceededDiscards": mscVrPpSrtBpHopCountExceededDiscards,
       "mscVrPpSrtBpDupLanIdOrTreeErrors": mscVrPpSrtBpDupLanIdOrTreeErrors,
       "mscVrPpSrtBpLanIdMismatches": mscVrPpSrtBpLanIdMismatches,
       "mscVrPpSrtBpStaticDiscards": mscVrPpSrtBpStaticDiscards,
       "mscVrPpSrtBpDynamicDiscards": mscVrPpSrtBpDynamicDiscards,
       "mscVrPpSrse": mscVrPpSrse,
       "mscVrPpSrseRowStatusTable": mscVrPpSrseRowStatusTable,
       "mscVrPpSrseRowStatusEntry": mscVrPpSrseRowStatusEntry,
       "mscVrPpSrseRowStatus": mscVrPpSrseRowStatus,
       "mscVrPpSrseComponentName": mscVrPpSrseComponentName,
       "mscVrPpSrseStorageType": mscVrPpSrseStorageType,
       "mscVrPpSrseIndex": mscVrPpSrseIndex,
       "mscVrPpSrseProvTable": mscVrPpSrseProvTable,
       "mscVrPpSrseProvEntry": mscVrPpSrseProvEntry,
       "mscVrPpSrseTranslateIpx": mscVrPpSrseTranslateIpx,
       "mscVrPpSrseFragmentIp": mscVrPpSrseFragmentIp,
       "mscVrPpSrseServiceClass": mscVrPpSrseServiceClass,
       "mscVrPpSrseConvertArpMacAddress": mscVrPpSrseConvertArpMacAddress,
       "mscVrPpSrsePortNum": mscVrPpSrsePortNum,
       "mscVrPpSrseStpProvTable": mscVrPpSrseStpProvTable,
       "mscVrPpSrseStpProvEntry": mscVrPpSrseStpProvEntry,
       "mscVrPpSrseAdminStatus": mscVrPpSrseAdminStatus,
       "mscVrPpSrsePortStateStpControl": mscVrPpSrsePortStateStpControl,
       "mscVrPpSrseStpTypeProv": mscVrPpSrseStpTypeProv,
       "mscVrPpSrsePortPriority": mscVrPpSrsePortPriority,
       "mscVrPpSrsePathCost": mscVrPpSrsePathCost,
       "mscVrPpSrsePathCostMethod": mscVrPpSrsePathCostMethod,
       "mscVrPpSrseDIProvTable": mscVrPpSrseDIProvTable,
       "mscVrPpSrseDIProvEntry": mscVrPpSrseDIProvEntry,
       "mscVrPpSrseDomainNum": mscVrPpSrseDomainNum,
       "mscVrPpSrsePreserveDomain": mscVrPpSrsePreserveDomain,
       "mscVrPpSrseStateTable": mscVrPpSrseStateTable,
       "mscVrPpSrseStateEntry": mscVrPpSrseStateEntry,
       "mscVrPpSrseAdminState": mscVrPpSrseAdminState,
       "mscVrPpSrseOperationalState": mscVrPpSrseOperationalState,
       "mscVrPpSrseUsageState": mscVrPpSrseUsageState,
       "mscVrPpSrseOperStatusTable": mscVrPpSrseOperStatusTable,
       "mscVrPpSrseOperStatusEntry": mscVrPpSrseOperStatusEntry,
       "mscVrPpSrseSnmpOperStatus": mscVrPpSrseSnmpOperStatus,
       "mscVrPpSrseOperTable": mscVrPpSrseOperTable,
       "mscVrPpSrseOperEntry": mscVrPpSrseOperEntry,
       "mscVrPpSrsePortName": mscVrPpSrsePortName,
       "mscVrPpSrseUpTime": mscVrPpSrseUpTime,
       "mscVrPpSrseDownTime": mscVrPpSrseDownTime,
       "mscVrPpSrseBridgingMode": mscVrPpSrseBridgingMode,
       "mscVrPpSrseBridgePortConfig": mscVrPpSrseBridgePortConfig,
       "mscVrPpSrseBridgePortType": mscVrPpSrseBridgePortType,
       "mscVrPpSrseIfIndex": mscVrPpSrseIfIndex,
       "mscVrPpSrseDelayExceededDiscards": mscVrPpSrseDelayExceededDiscards,
       "mscVrPpSrseMtuExceededDiscards": mscVrPpSrseMtuExceededDiscards,
       "mscVrPpSrseStpOperTable": mscVrPpSrseStpOperTable,
       "mscVrPpSrseStpOperEntry": mscVrPpSrseStpOperEntry,
       "mscVrPpSrseStpPortState": mscVrPpSrseStpPortState,
       "mscVrPpSrseStpTypeOper": mscVrPpSrseStpTypeOper,
       "mscVrPpSrseDesignatedCost": mscVrPpSrseDesignatedCost,
       "mscVrPpSrsePathCostOper": mscVrPpSrsePathCostOper,
       "mscVrPpSrseDesignatedBridge": mscVrPpSrseDesignatedBridge,
       "mscVrPpSrseDesignatedPort": mscVrPpSrseDesignatedPort,
       "mscVrPpSrseForwardTransitions": mscVrPpSrseForwardTransitions,
       "mscVrPpSrseBlockingDiscards": mscVrPpSrseBlockingDiscards,
       "mscVrPpSrseDesignatedRoot": mscVrPpSrseDesignatedRoot,
       "mscVrPpSrseStatsTable": mscVrPpSrseStatsTable,
       "mscVrPpSrseStatsEntry": mscVrPpSrseStatsEntry,
       "mscVrPpSrseBadAbstractDiscards": mscVrPpSrseBadAbstractDiscards,
       "mscVrPpSrseTinygramFramesIn": mscVrPpSrseTinygramFramesIn,
       "mscVrPpSrseTinygramFramesOut": mscVrPpSrseTinygramFramesOut,
       "mscVrPpSrseInFilterDiscards": mscVrPpSrseInFilterDiscards,
       "mscVrPpSrseOutFilterDiscards": mscVrPpSrseOutFilterDiscards,
       "mscVrPpSrseSrProvTable": mscVrPpSrseSrProvTable,
       "mscVrPpSrseSrProvEntry": mscVrPpSrseSrProvEntry,
       "mscVrPpSrseHopCount": mscVrPpSrseHopCount,
       "mscVrPpSrseExploreFrameTreatment": mscVrPpSrseExploreFrameTreatment,
       "mscVrPpSrseLanId": mscVrPpSrseLanId,
       "mscVrPpSrseInternalLanId": mscVrPpSrseInternalLanId,
       "mscVrPpSrseBridgeNum": mscVrPpSrseBridgeNum,
       "mscVrPpSrseLargestFrame": mscVrPpSrseLargestFrame,
       "mscVrPpSrseSteSpanMode": mscVrPpSrseSteSpanMode,
       "mscVrPpSrseAreRdLimit": mscVrPpSrseAreRdLimit,
       "mscVrPpSrseSteRdLimit": mscVrPpSrseSteRdLimit,
       "mscVrPpSrseSrStatsTable": mscVrPpSrseSrStatsTable,
       "mscVrPpSrseSrStatsEntry": mscVrPpSrseSrStatsEntry,
       "mscVrPpSrseSpecInFrames": mscVrPpSrseSpecInFrames,
       "mscVrPpSrseSpecOutFrames": mscVrPpSrseSpecOutFrames,
       "mscVrPpSrseApeInFrames": mscVrPpSrseApeInFrames,
       "mscVrPpSrseApeOutFrames": mscVrPpSrseApeOutFrames,
       "mscVrPpSrseSteInFrames": mscVrPpSrseSteInFrames,
       "mscVrPpSrseSteOutFrames": mscVrPpSrseSteOutFrames,
       "mscVrPpSrseSegmentMismatchDiscards": mscVrPpSrseSegmentMismatchDiscards,
       "mscVrPpSrseDupSegmentDiscards": mscVrPpSrseDupSegmentDiscards,
       "mscVrPpSrseHopCountExceededDiscards": mscVrPpSrseHopCountExceededDiscards,
       "mscVrPpSrseDupLanIdOrTreeErrors": mscVrPpSrseDupLanIdOrTreeErrors,
       "mscVrPpSrseLanIdMismatches": mscVrPpSrseLanIdMismatches,
       "mscVrPpSrseStaticDiscards": mscVrPpSrseStaticDiscards,
       "mscVrPpSrseDynamicDiscards": mscVrPpSrseDynamicDiscards,
       "mscVrPpTbse": mscVrPpTbse,
       "mscVrPpTbseRowStatusTable": mscVrPpTbseRowStatusTable,
       "mscVrPpTbseRowStatusEntry": mscVrPpTbseRowStatusEntry,
       "mscVrPpTbseRowStatus": mscVrPpTbseRowStatus,
       "mscVrPpTbseComponentName": mscVrPpTbseComponentName,
       "mscVrPpTbseStorageType": mscVrPpTbseStorageType,
       "mscVrPpTbseIndex": mscVrPpTbseIndex,
       "mscVrPpTbseProvTable": mscVrPpTbseProvTable,
       "mscVrPpTbseProvEntry": mscVrPpTbseProvEntry,
       "mscVrPpTbseTranslateIpx": mscVrPpTbseTranslateIpx,
       "mscVrPpTbseFragmentIp": mscVrPpTbseFragmentIp,
       "mscVrPpTbseServiceClass": mscVrPpTbseServiceClass,
       "mscVrPpTbseConvertArpMacAddress": mscVrPpTbseConvertArpMacAddress,
       "mscVrPpTbsePortNum": mscVrPpTbsePortNum,
       "mscVrPpTbseTbProvTable": mscVrPpTbseTbProvTable,
       "mscVrPpTbseTbProvEntry": mscVrPpTbseTbProvEntry,
       "mscVrPpTbseSecureOption": mscVrPpTbseSecureOption,
       "mscVrPpTbseStpProvTable": mscVrPpTbseStpProvTable,
       "mscVrPpTbseStpProvEntry": mscVrPpTbseStpProvEntry,
       "mscVrPpTbseAdminStatus": mscVrPpTbseAdminStatus,
       "mscVrPpTbsePortStateStpControl": mscVrPpTbsePortStateStpControl,
       "mscVrPpTbseStpTypeProv": mscVrPpTbseStpTypeProv,
       "mscVrPpTbsePortPriority": mscVrPpTbsePortPriority,
       "mscVrPpTbsePathCost": mscVrPpTbsePathCost,
       "mscVrPpTbsePathCostMethod": mscVrPpTbsePathCostMethod,
       "mscVrPpTbseDIProvTable": mscVrPpTbseDIProvTable,
       "mscVrPpTbseDIProvEntry": mscVrPpTbseDIProvEntry,
       "mscVrPpTbseDomainNum": mscVrPpTbseDomainNum,
       "mscVrPpTbsePreserveDomain": mscVrPpTbsePreserveDomain,
       "mscVrPpTbseStateTable": mscVrPpTbseStateTable,
       "mscVrPpTbseStateEntry": mscVrPpTbseStateEntry,
       "mscVrPpTbseAdminState": mscVrPpTbseAdminState,
       "mscVrPpTbseOperationalState": mscVrPpTbseOperationalState,
       "mscVrPpTbseUsageState": mscVrPpTbseUsageState,
       "mscVrPpTbseOperStatusTable": mscVrPpTbseOperStatusTable,
       "mscVrPpTbseOperStatusEntry": mscVrPpTbseOperStatusEntry,
       "mscVrPpTbseSnmpOperStatus": mscVrPpTbseSnmpOperStatus,
       "mscVrPpTbseOperTable": mscVrPpTbseOperTable,
       "mscVrPpTbseOperEntry": mscVrPpTbseOperEntry,
       "mscVrPpTbsePortName": mscVrPpTbsePortName,
       "mscVrPpTbseUpTime": mscVrPpTbseUpTime,
       "mscVrPpTbseDownTime": mscVrPpTbseDownTime,
       "mscVrPpTbseBridgingMode": mscVrPpTbseBridgingMode,
       "mscVrPpTbseBridgePortConfig": mscVrPpTbseBridgePortConfig,
       "mscVrPpTbseBridgePortType": mscVrPpTbseBridgePortType,
       "mscVrPpTbseIfIndex": mscVrPpTbseIfIndex,
       "mscVrPpTbseDelayExceededDiscards": mscVrPpTbseDelayExceededDiscards,
       "mscVrPpTbseMtuExceededDiscards": mscVrPpTbseMtuExceededDiscards,
       "mscVrPpTbseTbOperTable": mscVrPpTbseTbOperTable,
       "mscVrPpTbseTbOperEntry": mscVrPpTbseTbOperEntry,
       "mscVrPpTbseMaxInfo": mscVrPpTbseMaxInfo,
       "mscVrPpTbseBadVerifyDiscards": mscVrPpTbseBadVerifyDiscards,
       "mscVrPpTbseUnicastNoMatches": mscVrPpTbseUnicastNoMatches,
       "mscVrPpTbseStaticEntryDiscards": mscVrPpTbseStaticEntryDiscards,
       "mscVrPpTbseDynamicEntryDiscards": mscVrPpTbseDynamicEntryDiscards,
       "mscVrPpTbseLearningDiscards": mscVrPpTbseLearningDiscards,
       "mscVrPpTbseInDiscards": mscVrPpTbseInDiscards,
       "mscVrPpTbseInFrames": mscVrPpTbseInFrames,
       "mscVrPpTbseOutFrames": mscVrPpTbseOutFrames,
       "mscVrPpTbseStpOperTable": mscVrPpTbseStpOperTable,
       "mscVrPpTbseStpOperEntry": mscVrPpTbseStpOperEntry,
       "mscVrPpTbseStpPortState": mscVrPpTbseStpPortState,
       "mscVrPpTbseStpTypeOper": mscVrPpTbseStpTypeOper,
       "mscVrPpTbseDesignatedCost": mscVrPpTbseDesignatedCost,
       "mscVrPpTbsePathCostOper": mscVrPpTbsePathCostOper,
       "mscVrPpTbseDesignatedBridge": mscVrPpTbseDesignatedBridge,
       "mscVrPpTbseDesignatedPort": mscVrPpTbseDesignatedPort,
       "mscVrPpTbseForwardTransitions": mscVrPpTbseForwardTransitions,
       "mscVrPpTbseBlockingDiscards": mscVrPpTbseBlockingDiscards,
       "mscVrPpTbseDesignatedRoot": mscVrPpTbseDesignatedRoot,
       "mscVrPpTbseStatsTable": mscVrPpTbseStatsTable,
       "mscVrPpTbseStatsEntry": mscVrPpTbseStatsEntry,
       "mscVrPpTbseBadAbstractDiscards": mscVrPpTbseBadAbstractDiscards,
       "mscVrPpTbseTinygramFramesIn": mscVrPpTbseTinygramFramesIn,
       "mscVrPpTbseTinygramFramesOut": mscVrPpTbseTinygramFramesOut,
       "mscVrPpTbseInFilterDiscards": mscVrPpTbseInFilterDiscards,
       "mscVrPpTbseOutFilterDiscards": mscVrPpTbseOutFilterDiscards,
       "mscVrPpSrsg": mscVrPpSrsg,
       "mscVrPpSrsgRowStatusTable": mscVrPpSrsgRowStatusTable,
       "mscVrPpSrsgRowStatusEntry": mscVrPpSrsgRowStatusEntry,
       "mscVrPpSrsgRowStatus": mscVrPpSrsgRowStatus,
       "mscVrPpSrsgComponentName": mscVrPpSrsgComponentName,
       "mscVrPpSrsgStorageType": mscVrPpSrsgStorageType,
       "mscVrPpSrsgIndex": mscVrPpSrsgIndex,
       "mscVrPpSrsgProvTable": mscVrPpSrsgProvTable,
       "mscVrPpSrsgProvEntry": mscVrPpSrsgProvEntry,
       "mscVrPpSrsgTranslateIpx": mscVrPpSrsgTranslateIpx,
       "mscVrPpSrsgFragmentIp": mscVrPpSrsgFragmentIp,
       "mscVrPpSrsgServiceClass": mscVrPpSrsgServiceClass,
       "mscVrPpSrsgConvertArpMacAddress": mscVrPpSrsgConvertArpMacAddress,
       "mscVrPpSrsgPortNum": mscVrPpSrsgPortNum,
       "mscVrPpSrsgStpProvTable": mscVrPpSrsgStpProvTable,
       "mscVrPpSrsgStpProvEntry": mscVrPpSrsgStpProvEntry,
       "mscVrPpSrsgAdminStatus": mscVrPpSrsgAdminStatus,
       "mscVrPpSrsgPortStateStpControl": mscVrPpSrsgPortStateStpControl,
       "mscVrPpSrsgStpTypeProv": mscVrPpSrsgStpTypeProv,
       "mscVrPpSrsgPortPriority": mscVrPpSrsgPortPriority,
       "mscVrPpSrsgPathCost": mscVrPpSrsgPathCost,
       "mscVrPpSrsgPathCostMethod": mscVrPpSrsgPathCostMethod,
       "mscVrPpSrsgDIProvTable": mscVrPpSrsgDIProvTable,
       "mscVrPpSrsgDIProvEntry": mscVrPpSrsgDIProvEntry,
       "mscVrPpSrsgDomainNum": mscVrPpSrsgDomainNum,
       "mscVrPpSrsgPreserveDomain": mscVrPpSrsgPreserveDomain,
       "mscVrPpSrsgStateTable": mscVrPpSrsgStateTable,
       "mscVrPpSrsgStateEntry": mscVrPpSrsgStateEntry,
       "mscVrPpSrsgAdminState": mscVrPpSrsgAdminState,
       "mscVrPpSrsgOperationalState": mscVrPpSrsgOperationalState,
       "mscVrPpSrsgUsageState": mscVrPpSrsgUsageState,
       "mscVrPpSrsgOperStatusTable": mscVrPpSrsgOperStatusTable,
       "mscVrPpSrsgOperStatusEntry": mscVrPpSrsgOperStatusEntry,
       "mscVrPpSrsgSnmpOperStatus": mscVrPpSrsgSnmpOperStatus,
       "mscVrPpSrsgOperTable": mscVrPpSrsgOperTable,
       "mscVrPpSrsgOperEntry": mscVrPpSrsgOperEntry,
       "mscVrPpSrsgPortName": mscVrPpSrsgPortName,
       "mscVrPpSrsgUpTime": mscVrPpSrsgUpTime,
       "mscVrPpSrsgDownTime": mscVrPpSrsgDownTime,
       "mscVrPpSrsgBridgingMode": mscVrPpSrsgBridgingMode,
       "mscVrPpSrsgBridgePortConfig": mscVrPpSrsgBridgePortConfig,
       "mscVrPpSrsgBridgePortType": mscVrPpSrsgBridgePortType,
       "mscVrPpSrsgIfIndex": mscVrPpSrsgIfIndex,
       "mscVrPpSrsgDelayExceededDiscards": mscVrPpSrsgDelayExceededDiscards,
       "mscVrPpSrsgMtuExceededDiscards": mscVrPpSrsgMtuExceededDiscards,
       "mscVrPpSrsgStpOperTable": mscVrPpSrsgStpOperTable,
       "mscVrPpSrsgStpOperEntry": mscVrPpSrsgStpOperEntry,
       "mscVrPpSrsgStpPortState": mscVrPpSrsgStpPortState,
       "mscVrPpSrsgStpTypeOper": mscVrPpSrsgStpTypeOper,
       "mscVrPpSrsgDesignatedCost": mscVrPpSrsgDesignatedCost,
       "mscVrPpSrsgPathCostOper": mscVrPpSrsgPathCostOper,
       "mscVrPpSrsgDesignatedBridge": mscVrPpSrsgDesignatedBridge,
       "mscVrPpSrsgDesignatedPort": mscVrPpSrsgDesignatedPort,
       "mscVrPpSrsgForwardTransitions": mscVrPpSrsgForwardTransitions,
       "mscVrPpSrsgBlockingDiscards": mscVrPpSrsgBlockingDiscards,
       "mscVrPpSrsgDesignatedRoot": mscVrPpSrsgDesignatedRoot,
       "mscVrPpSrsgStatsTable": mscVrPpSrsgStatsTable,
       "mscVrPpSrsgStatsEntry": mscVrPpSrsgStatsEntry,
       "mscVrPpSrsgBadAbstractDiscards": mscVrPpSrsgBadAbstractDiscards,
       "mscVrPpSrsgTinygramFramesIn": mscVrPpSrsgTinygramFramesIn,
       "mscVrPpSrsgTinygramFramesOut": mscVrPpSrsgTinygramFramesOut,
       "mscVrPpSrsgInFilterDiscards": mscVrPpSrsgInFilterDiscards,
       "mscVrPpSrsgOutFilterDiscards": mscVrPpSrsgOutFilterDiscards,
       "mscVrPpSrsgSrProvTable": mscVrPpSrsgSrProvTable,
       "mscVrPpSrsgSrProvEntry": mscVrPpSrsgSrProvEntry,
       "mscVrPpSrsgHopCount": mscVrPpSrsgHopCount,
       "mscVrPpSrsgExploreFrameTreatment": mscVrPpSrsgExploreFrameTreatment,
       "mscVrPpSrsgLanId": mscVrPpSrsgLanId,
       "mscVrPpSrsgInternalLanId": mscVrPpSrsgInternalLanId,
       "mscVrPpSrsgBridgeNum": mscVrPpSrsgBridgeNum,
       "mscVrPpSrsgLargestFrame": mscVrPpSrsgLargestFrame,
       "mscVrPpSrsgSteSpanMode": mscVrPpSrsgSteSpanMode,
       "mscVrPpSrsgAreRdLimit": mscVrPpSrsgAreRdLimit,
       "mscVrPpSrsgSteRdLimit": mscVrPpSrsgSteRdLimit,
       "mscVrPpSrsgSrStatsTable": mscVrPpSrsgSrStatsTable,
       "mscVrPpSrsgSrStatsEntry": mscVrPpSrsgSrStatsEntry,
       "mscVrPpSrsgSpecInFrames": mscVrPpSrsgSpecInFrames,
       "mscVrPpSrsgSpecOutFrames": mscVrPpSrsgSpecOutFrames,
       "mscVrPpSrsgApeInFrames": mscVrPpSrsgApeInFrames,
       "mscVrPpSrsgApeOutFrames": mscVrPpSrsgApeOutFrames,
       "mscVrPpSrsgSteInFrames": mscVrPpSrsgSteInFrames,
       "mscVrPpSrsgSteOutFrames": mscVrPpSrsgSteOutFrames,
       "mscVrPpSrsgSegmentMismatchDiscards": mscVrPpSrsgSegmentMismatchDiscards,
       "mscVrPpSrsgDupSegmentDiscards": mscVrPpSrsgDupSegmentDiscards,
       "mscVrPpSrsgHopCountExceededDiscards": mscVrPpSrsgHopCountExceededDiscards,
       "mscVrPpSrsgDupLanIdOrTreeErrors": mscVrPpSrsgDupLanIdOrTreeErrors,
       "mscVrPpSrsgLanIdMismatches": mscVrPpSrsgLanIdMismatches,
       "mscVrPpSrsgStaticDiscards": mscVrPpSrsgStaticDiscards,
       "mscVrPpSrsgDynamicDiscards": mscVrPpSrsgDynamicDiscards,
       "mscVrPpTbsg": mscVrPpTbsg,
       "mscVrPpTbsgRowStatusTable": mscVrPpTbsgRowStatusTable,
       "mscVrPpTbsgRowStatusEntry": mscVrPpTbsgRowStatusEntry,
       "mscVrPpTbsgRowStatus": mscVrPpTbsgRowStatus,
       "mscVrPpTbsgComponentName": mscVrPpTbsgComponentName,
       "mscVrPpTbsgStorageType": mscVrPpTbsgStorageType,
       "mscVrPpTbsgIndex": mscVrPpTbsgIndex,
       "mscVrPpTbsgProvTable": mscVrPpTbsgProvTable,
       "mscVrPpTbsgProvEntry": mscVrPpTbsgProvEntry,
       "mscVrPpTbsgTranslateIpx": mscVrPpTbsgTranslateIpx,
       "mscVrPpTbsgFragmentIp": mscVrPpTbsgFragmentIp,
       "mscVrPpTbsgServiceClass": mscVrPpTbsgServiceClass,
       "mscVrPpTbsgConvertArpMacAddress": mscVrPpTbsgConvertArpMacAddress,
       "mscVrPpTbsgPortNum": mscVrPpTbsgPortNum,
       "mscVrPpTbsgTbProvTable": mscVrPpTbsgTbProvTable,
       "mscVrPpTbsgTbProvEntry": mscVrPpTbsgTbProvEntry,
       "mscVrPpTbsgSecureOption": mscVrPpTbsgSecureOption,
       "mscVrPpTbsgStpProvTable": mscVrPpTbsgStpProvTable,
       "mscVrPpTbsgStpProvEntry": mscVrPpTbsgStpProvEntry,
       "mscVrPpTbsgAdminStatus": mscVrPpTbsgAdminStatus,
       "mscVrPpTbsgPortStateStpControl": mscVrPpTbsgPortStateStpControl,
       "mscVrPpTbsgStpTypeProv": mscVrPpTbsgStpTypeProv,
       "mscVrPpTbsgPortPriority": mscVrPpTbsgPortPriority,
       "mscVrPpTbsgPathCost": mscVrPpTbsgPathCost,
       "mscVrPpTbsgPathCostMethod": mscVrPpTbsgPathCostMethod,
       "mscVrPpTbsgDIProvTable": mscVrPpTbsgDIProvTable,
       "mscVrPpTbsgDIProvEntry": mscVrPpTbsgDIProvEntry,
       "mscVrPpTbsgDomainNum": mscVrPpTbsgDomainNum,
       "mscVrPpTbsgPreserveDomain": mscVrPpTbsgPreserveDomain,
       "mscVrPpTbsgStateTable": mscVrPpTbsgStateTable,
       "mscVrPpTbsgStateEntry": mscVrPpTbsgStateEntry,
       "mscVrPpTbsgAdminState": mscVrPpTbsgAdminState,
       "mscVrPpTbsgOperationalState": mscVrPpTbsgOperationalState,
       "mscVrPpTbsgUsageState": mscVrPpTbsgUsageState,
       "mscVrPpTbsgOperStatusTable": mscVrPpTbsgOperStatusTable,
       "mscVrPpTbsgOperStatusEntry": mscVrPpTbsgOperStatusEntry,
       "mscVrPpTbsgSnmpOperStatus": mscVrPpTbsgSnmpOperStatus,
       "mscVrPpTbsgOperTable": mscVrPpTbsgOperTable,
       "mscVrPpTbsgOperEntry": mscVrPpTbsgOperEntry,
       "mscVrPpTbsgPortName": mscVrPpTbsgPortName,
       "mscVrPpTbsgUpTime": mscVrPpTbsgUpTime,
       "mscVrPpTbsgDownTime": mscVrPpTbsgDownTime,
       "mscVrPpTbsgBridgingMode": mscVrPpTbsgBridgingMode,
       "mscVrPpTbsgBridgePortConfig": mscVrPpTbsgBridgePortConfig,
       "mscVrPpTbsgBridgePortType": mscVrPpTbsgBridgePortType,
       "mscVrPpTbsgIfIndex": mscVrPpTbsgIfIndex,
       "mscVrPpTbsgDelayExceededDiscards": mscVrPpTbsgDelayExceededDiscards,
       "mscVrPpTbsgMtuExceededDiscards": mscVrPpTbsgMtuExceededDiscards,
       "mscVrPpTbsgTbOperTable": mscVrPpTbsgTbOperTable,
       "mscVrPpTbsgTbOperEntry": mscVrPpTbsgTbOperEntry,
       "mscVrPpTbsgMaxInfo": mscVrPpTbsgMaxInfo,
       "mscVrPpTbsgBadVerifyDiscards": mscVrPpTbsgBadVerifyDiscards,
       "mscVrPpTbsgUnicastNoMatches": mscVrPpTbsgUnicastNoMatches,
       "mscVrPpTbsgStaticEntryDiscards": mscVrPpTbsgStaticEntryDiscards,
       "mscVrPpTbsgDynamicEntryDiscards": mscVrPpTbsgDynamicEntryDiscards,
       "mscVrPpTbsgLearningDiscards": mscVrPpTbsgLearningDiscards,
       "mscVrPpTbsgInDiscards": mscVrPpTbsgInDiscards,
       "mscVrPpTbsgInFrames": mscVrPpTbsgInFrames,
       "mscVrPpTbsgOutFrames": mscVrPpTbsgOutFrames,
       "mscVrPpTbsgStpOperTable": mscVrPpTbsgStpOperTable,
       "mscVrPpTbsgStpOperEntry": mscVrPpTbsgStpOperEntry,
       "mscVrPpTbsgStpPortState": mscVrPpTbsgStpPortState,
       "mscVrPpTbsgStpTypeOper": mscVrPpTbsgStpTypeOper,
       "mscVrPpTbsgDesignatedCost": mscVrPpTbsgDesignatedCost,
       "mscVrPpTbsgPathCostOper": mscVrPpTbsgPathCostOper,
       "mscVrPpTbsgDesignatedBridge": mscVrPpTbsgDesignatedBridge,
       "mscVrPpTbsgDesignatedPort": mscVrPpTbsgDesignatedPort,
       "mscVrPpTbsgForwardTransitions": mscVrPpTbsgForwardTransitions,
       "mscVrPpTbsgBlockingDiscards": mscVrPpTbsgBlockingDiscards,
       "mscVrPpTbsgDesignatedRoot": mscVrPpTbsgDesignatedRoot,
       "mscVrPpTbsgStatsTable": mscVrPpTbsgStatsTable,
       "mscVrPpTbsgStatsEntry": mscVrPpTbsgStatsEntry,
       "mscVrPpTbsgBadAbstractDiscards": mscVrPpTbsgBadAbstractDiscards,
       "mscVrPpTbsgTinygramFramesIn": mscVrPpTbsgTinygramFramesIn,
       "mscVrPpTbsgTinygramFramesOut": mscVrPpTbsgTinygramFramesOut,
       "mscVrPpTbsgInFilterDiscards": mscVrPpTbsgInFilterDiscards,
       "mscVrPpTbsgOutFilterDiscards": mscVrPpTbsgOutFilterDiscards,
       "mscVrPpSrcl": mscVrPpSrcl,
       "mscVrPpSrclRowStatusTable": mscVrPpSrclRowStatusTable,
       "mscVrPpSrclRowStatusEntry": mscVrPpSrclRowStatusEntry,
       "mscVrPpSrclRowStatus": mscVrPpSrclRowStatus,
       "mscVrPpSrclComponentName": mscVrPpSrclComponentName,
       "mscVrPpSrclStorageType": mscVrPpSrclStorageType,
       "mscVrPpSrclIndex": mscVrPpSrclIndex,
       "mscVrPpSrclNs": mscVrPpSrclNs,
       "mscVrPpSrclNsRowStatusTable": mscVrPpSrclNsRowStatusTable,
       "mscVrPpSrclNsRowStatusEntry": mscVrPpSrclNsRowStatusEntry,
       "mscVrPpSrclNsRowStatus": mscVrPpSrclNsRowStatus,
       "mscVrPpSrclNsComponentName": mscVrPpSrclNsComponentName,
       "mscVrPpSrclNsStorageType": mscVrPpSrclNsStorageType,
       "mscVrPpSrclNsIndex": mscVrPpSrclNsIndex,
       "mscVrPpSrclNsProvTable": mscVrPpSrclNsProvTable,
       "mscVrPpSrclNsProvEntry": mscVrPpSrclNsProvEntry,
       "mscVrPpSrclNsIncomingFilter": mscVrPpSrclNsIncomingFilter,
       "mscVrPpSrclNsOutgoingFilter": mscVrPpSrclNsOutgoingFilter,
       "mscVrPpSrclProvTable": mscVrPpSrclProvTable,
       "mscVrPpSrclProvEntry": mscVrPpSrclProvEntry,
       "mscVrPpSrclTranslateIpx": mscVrPpSrclTranslateIpx,
       "mscVrPpSrclFragmentIp": mscVrPpSrclFragmentIp,
       "mscVrPpSrclServiceClass": mscVrPpSrclServiceClass,
       "mscVrPpSrclConvertArpMacAddress": mscVrPpSrclConvertArpMacAddress,
       "mscVrPpSrclPortNum": mscVrPpSrclPortNum,
       "mscVrPpSrclStpProvTable": mscVrPpSrclStpProvTable,
       "mscVrPpSrclStpProvEntry": mscVrPpSrclStpProvEntry,
       "mscVrPpSrclAdminStatus": mscVrPpSrclAdminStatus,
       "mscVrPpSrclPortStateStpControl": mscVrPpSrclPortStateStpControl,
       "mscVrPpSrclStpTypeProv": mscVrPpSrclStpTypeProv,
       "mscVrPpSrclPortPriority": mscVrPpSrclPortPriority,
       "mscVrPpSrclPathCost": mscVrPpSrclPathCost,
       "mscVrPpSrclPathCostMethod": mscVrPpSrclPathCostMethod,
       "mscVrPpSrclDIProvTable": mscVrPpSrclDIProvTable,
       "mscVrPpSrclDIProvEntry": mscVrPpSrclDIProvEntry,
       "mscVrPpSrclDomainNum": mscVrPpSrclDomainNum,
       "mscVrPpSrclPreserveDomain": mscVrPpSrclPreserveDomain,
       "mscVrPpSrclStateTable": mscVrPpSrclStateTable,
       "mscVrPpSrclStateEntry": mscVrPpSrclStateEntry,
       "mscVrPpSrclAdminState": mscVrPpSrclAdminState,
       "mscVrPpSrclOperationalState": mscVrPpSrclOperationalState,
       "mscVrPpSrclUsageState": mscVrPpSrclUsageState,
       "mscVrPpSrclOperStatusTable": mscVrPpSrclOperStatusTable,
       "mscVrPpSrclOperStatusEntry": mscVrPpSrclOperStatusEntry,
       "mscVrPpSrclSnmpOperStatus": mscVrPpSrclSnmpOperStatus,
       "mscVrPpSrclOperTable": mscVrPpSrclOperTable,
       "mscVrPpSrclOperEntry": mscVrPpSrclOperEntry,
       "mscVrPpSrclPortName": mscVrPpSrclPortName,
       "mscVrPpSrclUpTime": mscVrPpSrclUpTime,
       "mscVrPpSrclDownTime": mscVrPpSrclDownTime,
       "mscVrPpSrclBridgingMode": mscVrPpSrclBridgingMode,
       "mscVrPpSrclBridgePortConfig": mscVrPpSrclBridgePortConfig,
       "mscVrPpSrclBridgePortType": mscVrPpSrclBridgePortType,
       "mscVrPpSrclIfIndex": mscVrPpSrclIfIndex,
       "mscVrPpSrclDelayExceededDiscards": mscVrPpSrclDelayExceededDiscards,
       "mscVrPpSrclMtuExceededDiscards": mscVrPpSrclMtuExceededDiscards,
       "mscVrPpSrclStpOperTable": mscVrPpSrclStpOperTable,
       "mscVrPpSrclStpOperEntry": mscVrPpSrclStpOperEntry,
       "mscVrPpSrclStpPortState": mscVrPpSrclStpPortState,
       "mscVrPpSrclStpTypeOper": mscVrPpSrclStpTypeOper,
       "mscVrPpSrclDesignatedCost": mscVrPpSrclDesignatedCost,
       "mscVrPpSrclPathCostOper": mscVrPpSrclPathCostOper,
       "mscVrPpSrclDesignatedBridge": mscVrPpSrclDesignatedBridge,
       "mscVrPpSrclDesignatedPort": mscVrPpSrclDesignatedPort,
       "mscVrPpSrclForwardTransitions": mscVrPpSrclForwardTransitions,
       "mscVrPpSrclBlockingDiscards": mscVrPpSrclBlockingDiscards,
       "mscVrPpSrclDesignatedRoot": mscVrPpSrclDesignatedRoot,
       "mscVrPpSrclStatsTable": mscVrPpSrclStatsTable,
       "mscVrPpSrclStatsEntry": mscVrPpSrclStatsEntry,
       "mscVrPpSrclBadAbstractDiscards": mscVrPpSrclBadAbstractDiscards,
       "mscVrPpSrclTinygramFramesIn": mscVrPpSrclTinygramFramesIn,
       "mscVrPpSrclTinygramFramesOut": mscVrPpSrclTinygramFramesOut,
       "mscVrPpSrclInFilterDiscards": mscVrPpSrclInFilterDiscards,
       "mscVrPpSrclOutFilterDiscards": mscVrPpSrclOutFilterDiscards,
       "mscVrPpSrclSrProvTable": mscVrPpSrclSrProvTable,
       "mscVrPpSrclSrProvEntry": mscVrPpSrclSrProvEntry,
       "mscVrPpSrclHopCount": mscVrPpSrclHopCount,
       "mscVrPpSrclExploreFrameTreatment": mscVrPpSrclExploreFrameTreatment,
       "mscVrPpSrclLanId": mscVrPpSrclLanId,
       "mscVrPpSrclInternalLanId": mscVrPpSrclInternalLanId,
       "mscVrPpSrclBridgeNum": mscVrPpSrclBridgeNum,
       "mscVrPpSrclLargestFrame": mscVrPpSrclLargestFrame,
       "mscVrPpSrclSteSpanMode": mscVrPpSrclSteSpanMode,
       "mscVrPpSrclAreRdLimit": mscVrPpSrclAreRdLimit,
       "mscVrPpSrclSteRdLimit": mscVrPpSrclSteRdLimit,
       "mscVrPpSrclSrStatsTable": mscVrPpSrclSrStatsTable,
       "mscVrPpSrclSrStatsEntry": mscVrPpSrclSrStatsEntry,
       "mscVrPpSrclSpecInFrames": mscVrPpSrclSpecInFrames,
       "mscVrPpSrclSpecOutFrames": mscVrPpSrclSpecOutFrames,
       "mscVrPpSrclApeInFrames": mscVrPpSrclApeInFrames,
       "mscVrPpSrclApeOutFrames": mscVrPpSrclApeOutFrames,
       "mscVrPpSrclSteInFrames": mscVrPpSrclSteInFrames,
       "mscVrPpSrclSteOutFrames": mscVrPpSrclSteOutFrames,
       "mscVrPpSrclSegmentMismatchDiscards": mscVrPpSrclSegmentMismatchDiscards,
       "mscVrPpSrclDupSegmentDiscards": mscVrPpSrclDupSegmentDiscards,
       "mscVrPpSrclHopCountExceededDiscards": mscVrPpSrclHopCountExceededDiscards,
       "mscVrPpSrclDupLanIdOrTreeErrors": mscVrPpSrclDupLanIdOrTreeErrors,
       "mscVrPpSrclLanIdMismatches": mscVrPpSrclLanIdMismatches,
       "mscVrPpSrclStaticDiscards": mscVrPpSrclStaticDiscards,
       "mscVrPpSrclDynamicDiscards": mscVrPpSrclDynamicDiscards,
       "mscVrBr": mscVrBr,
       "mscVrBrRowStatusTable": mscVrBrRowStatusTable,
       "mscVrBrRowStatusEntry": mscVrBrRowStatusEntry,
       "mscVrBrRowStatus": mscVrBrRowStatus,
       "mscVrBrComponentName": mscVrBrComponentName,
       "mscVrBrStorageType": mscVrBrStorageType,
       "mscVrBrIndex": mscVrBrIndex,
       "mscVrBrPte": mscVrBrPte,
       "mscVrBrPteRowStatusTable": mscVrBrPteRowStatusTable,
       "mscVrBrPteRowStatusEntry": mscVrBrPteRowStatusEntry,
       "mscVrBrPteRowStatus": mscVrBrPteRowStatus,
       "mscVrBrPteComponentName": mscVrBrPteComponentName,
       "mscVrBrPteStorageType": mscVrBrPteStorageType,
       "mscVrBrPteDomainNumIndex": mscVrBrPteDomainNumIndex,
       "mscVrBrPtePortNameIndex": mscVrBrPtePortNameIndex,
       "mscVrBrPteModeIndex": mscVrBrPteModeIndex,
       "mscVrBrPteOperTable": mscVrBrPteOperTable,
       "mscVrBrPteOperEntry": mscVrBrPteOperEntry,
       "mscVrBrPteMacType": mscVrBrPteMacType,
       "mscVrBrPteStpState": mscVrBrPteStpState,
       "mscVrBrPteStpType": mscVrBrPteStpType,
       "mscVrBrPteFilterPoints": mscVrBrPteFilterPoints,
       "mscVrBrPtePortPointsTo": mscVrBrPtePortPointsTo,
       "mscVrBrPteSpOperTable": mscVrBrPteSpOperTable,
       "mscVrBrPteSpOperEntry": mscVrBrPteSpOperEntry,
       "mscVrBrPteLanId": mscVrBrPteLanId,
       "mscVrBrPteInternalLanId": mscVrBrPteInternalLanId,
       "mscVrBrPteBridgeNum": mscVrBrPteBridgeNum,
       "mscVrBrNs": mscVrBrNs,
       "mscVrBrNsRowStatusTable": mscVrBrNsRowStatusTable,
       "mscVrBrNsRowStatusEntry": mscVrBrNsRowStatusEntry,
       "mscVrBrNsRowStatus": mscVrBrNsRowStatus,
       "mscVrBrNsComponentName": mscVrBrNsComponentName,
       "mscVrBrNsStorageType": mscVrBrNsStorageType,
       "mscVrBrNsIndex": mscVrBrNsIndex,
       "mscVrBrNsAte": mscVrBrNsAte,
       "mscVrBrNsAteRowStatusTable": mscVrBrNsAteRowStatusTable,
       "mscVrBrNsAteRowStatusEntry": mscVrBrNsAteRowStatusEntry,
       "mscVrBrNsAteRowStatus": mscVrBrNsAteRowStatus,
       "mscVrBrNsAteComponentName": mscVrBrNsAteComponentName,
       "mscVrBrNsAteStorageType": mscVrBrNsAteStorageType,
       "mscVrBrNsAteEntryNumberIndex": mscVrBrNsAteEntryNumberIndex,
       "mscVrBrNsAteProvTable": mscVrBrNsAteProvTable,
       "mscVrBrNsAteProvEntry": mscVrBrNsAteProvEntry,
       "mscVrBrNsAteDomainNum": mscVrBrNsAteDomainNum,
       "mscVrBrNsAteFirstMacAddress": mscVrBrNsAteFirstMacAddress,
       "mscVrBrNsAteFirstMacAddressMask": mscVrBrNsAteFirstMacAddressMask,
       "mscVrBrNsAteSecondMacAddress": mscVrBrNsAteSecondMacAddress,
       "mscVrBrNsAteSecondMacAddressMask": mscVrBrNsAteSecondMacAddressMask,
       "mscVrBrNsAteDirection": mscVrBrNsAteDirection,
       "mscVrBrNsAteFilterName": mscVrBrNsAteFilterName,
       "mscVrBrNsProvTable": mscVrBrNsProvTable,
       "mscVrBrNsProvEntry": mscVrBrNsProvEntry,
       "mscVrBrNsFirstFilter": mscVrBrNsFirstFilter,
       "mscVrBrNsLastFilter": mscVrBrNsLastFilter,
       "mscVrBrTb": mscVrBrTb,
       "mscVrBrTbRowStatusTable": mscVrBrTbRowStatusTable,
       "mscVrBrTbRowStatusEntry": mscVrBrTbRowStatusEntry,
       "mscVrBrTbRowStatus": mscVrBrTbRowStatus,
       "mscVrBrTbComponentName": mscVrBrTbComponentName,
       "mscVrBrTbStorageType": mscVrBrTbStorageType,
       "mscVrBrTbIndex": mscVrBrTbIndex,
       "mscVrBrTbStp": mscVrBrTbStp,
       "mscVrBrTbStpRowStatusTable": mscVrBrTbStpRowStatusTable,
       "mscVrBrTbStpRowStatusEntry": mscVrBrTbStpRowStatusEntry,
       "mscVrBrTbStpRowStatus": mscVrBrTbStpRowStatus,
       "mscVrBrTbStpComponentName": mscVrBrTbStpComponentName,
       "mscVrBrTbStpStorageType": mscVrBrTbStpStorageType,
       "mscVrBrTbStpIndex": mscVrBrTbStpIndex,
       "mscVrBrTbStpProvTable": mscVrBrTbStpProvTable,
       "mscVrBrTbStpProvEntry": mscVrBrTbStpProvEntry,
       "mscVrBrTbStpStpMode": mscVrBrTbStpStpMode,
       "mscVrBrTbStpProtocolSpec": mscVrBrTbStpProtocolSpec,
       "mscVrBrTbStpPriority": mscVrBrTbStpPriority,
       "mscVrBrTbStpBridgeMaxAge": mscVrBrTbStpBridgeMaxAge,
       "mscVrBrTbStpBridgeHelloTime": mscVrBrTbStpBridgeHelloTime,
       "mscVrBrTbStpBridgeForwardDelay": mscVrBrTbStpBridgeForwardDelay,
       "mscVrBrTbStpOperTable": mscVrBrTbStpOperTable,
       "mscVrBrTbStpOperEntry": mscVrBrTbStpOperEntry,
       "mscVrBrTbStpBridgeId": mscVrBrTbStpBridgeId,
       "mscVrBrTbStpRootPortName": mscVrBrTbStpRootPortName,
       "mscVrBrTbStpTimeSinceTopologyChange": mscVrBrTbStpTimeSinceTopologyChange,
       "mscVrBrTbStpTopologyChangeDetect": mscVrBrTbStpTopologyChangeDetect,
       "mscVrBrTbStpTopologyChanges": mscVrBrTbStpTopologyChanges,
       "mscVrBrTbStpDesignatedRoot": mscVrBrTbStpDesignatedRoot,
       "mscVrBrTbStpRootCost": mscVrBrTbStpRootCost,
       "mscVrBrTbStpMaxAge": mscVrBrTbStpMaxAge,
       "mscVrBrTbStpAgingTimeOper": mscVrBrTbStpAgingTimeOper,
       "mscVrBrTbStpHelloTime": mscVrBrTbStpHelloTime,
       "mscVrBrTbStpHoldTime": mscVrBrTbStpHoldTime,
       "mscVrBrTbStpFwdDelay": mscVrBrTbStpFwdDelay,
       "mscVrBrTbSte": mscVrBrTbSte,
       "mscVrBrTbSteRowStatusTable": mscVrBrTbSteRowStatusTable,
       "mscVrBrTbSteRowStatusEntry": mscVrBrTbSteRowStatusEntry,
       "mscVrBrTbSteRowStatus": mscVrBrTbSteRowStatus,
       "mscVrBrTbSteComponentName": mscVrBrTbSteComponentName,
       "mscVrBrTbSteStorageType": mscVrBrTbSteStorageType,
       "mscVrBrTbSteAddressIndex": mscVrBrTbSteAddressIndex,
       "mscVrBrTbSteReceivePortIndex": mscVrBrTbSteReceivePortIndex,
       "mscVrBrTbSteProvTable": mscVrBrTbSteProvTable,
       "mscVrBrTbSteProvEntry": mscVrBrTbSteProvEntry,
       "mscVrBrTbSteStatus": mscVrBrTbSteStatus,
       "mscVrBrTbSteAtgtTable": mscVrBrTbSteAtgtTable,
       "mscVrBrTbSteAtgtEntry": mscVrBrTbSteAtgtEntry,
       "mscVrBrTbSteAtgtValue": mscVrBrTbSteAtgtValue,
       "mscVrBrTbSteAtgtRowStatus": mscVrBrTbSteAtgtRowStatus,
       "mscVrBrTbFte": mscVrBrTbFte,
       "mscVrBrTbFteRowStatusTable": mscVrBrTbFteRowStatusTable,
       "mscVrBrTbFteRowStatusEntry": mscVrBrTbFteRowStatusEntry,
       "mscVrBrTbFteRowStatus": mscVrBrTbFteRowStatus,
       "mscVrBrTbFteComponentName": mscVrBrTbFteComponentName,
       "mscVrBrTbFteStorageType": mscVrBrTbFteStorageType,
       "mscVrBrTbFteAddressIndex": mscVrBrTbFteAddressIndex,
       "mscVrBrTbFteDomainNumIndex": mscVrBrTbFteDomainNumIndex,
       "mscVrBrTbFteOperTable": mscVrBrTbFteOperTable,
       "mscVrBrTbFteOperEntry": mscVrBrTbFteOperEntry,
       "mscVrBrTbFtePort": mscVrBrTbFtePort,
       "mscVrBrTbFteAgeOfEntry": mscVrBrTbFteAgeOfEntry,
       "mscVrBrTbFtePeerAddressInfo": mscVrBrTbFtePeerAddressInfo,
       "mscVrBrTbFteStatus": mscVrBrTbFteStatus,
       "mscVrBrTbNcFte": mscVrBrTbNcFte,
       "mscVrBrTbNcFteRowStatusTable": mscVrBrTbNcFteRowStatusTable,
       "mscVrBrTbNcFteRowStatusEntry": mscVrBrTbNcFteRowStatusEntry,
       "mscVrBrTbNcFteRowStatus": mscVrBrTbNcFteRowStatus,
       "mscVrBrTbNcFteComponentName": mscVrBrTbNcFteComponentName,
       "mscVrBrTbNcFteStorageType": mscVrBrTbNcFteStorageType,
       "mscVrBrTbNcFteAddressIndex": mscVrBrTbNcFteAddressIndex,
       "mscVrBrTbNcFteDomainNumIndex": mscVrBrTbNcFteDomainNumIndex,
       "mscVrBrTbNcFteOperTable": mscVrBrTbNcFteOperTable,
       "mscVrBrTbNcFteOperEntry": mscVrBrTbNcFteOperEntry,
       "mscVrBrTbNcFtePort": mscVrBrTbNcFtePort,
       "mscVrBrTbNcFteAgeOfEntry": mscVrBrTbNcFteAgeOfEntry,
       "mscVrBrTbNcFtePeerAddressInfo": mscVrBrTbNcFtePeerAddressInfo,
       "mscVrBrTbNcFteStatus": mscVrBrTbNcFteStatus,
       "mscVrBrTbProvTable": mscVrBrTbProvTable,
       "mscVrBrTbProvEntry": mscVrBrTbProvEntry,
       "mscVrBrTbFwdTableNumEntries": mscVrBrTbFwdTableNumEntries,
       "mscVrBrTbAgingTime": mscVrBrTbAgingTime,
       "mscVrBrTbStatsTable": mscVrBrTbStatsTable,
       "mscVrBrTbStatsEntry": mscVrBrTbStatsEntry,
       "mscVrBrTbLearnedEntryDiscards": mscVrBrTbLearnedEntryDiscards,
       "mscVrBrTbTotalForwardingTableEntries": mscVrBrTbTotalForwardingTableEntries,
       "mscVrBrTbNumFtEntriesFree": mscVrBrTbNumFtEntriesFree,
       "mscVrBrTbNumFtEntriesDenied": mscVrBrTbNumFtEntriesDenied,
       "mscVrBrSrb": mscVrBrSrb,
       "mscVrBrSrbRowStatusTable": mscVrBrSrbRowStatusTable,
       "mscVrBrSrbRowStatusEntry": mscVrBrSrbRowStatusEntry,
       "mscVrBrSrbRowStatus": mscVrBrSrbRowStatus,
       "mscVrBrSrbComponentName": mscVrBrSrbComponentName,
       "mscVrBrSrbStorageType": mscVrBrSrbStorageType,
       "mscVrBrSrbIndex": mscVrBrSrbIndex,
       "mscVrBrSrbStp": mscVrBrSrbStp,
       "mscVrBrSrbStpRowStatusTable": mscVrBrSrbStpRowStatusTable,
       "mscVrBrSrbStpRowStatusEntry": mscVrBrSrbStpRowStatusEntry,
       "mscVrBrSrbStpRowStatus": mscVrBrSrbStpRowStatus,
       "mscVrBrSrbStpComponentName": mscVrBrSrbStpComponentName,
       "mscVrBrSrbStpStorageType": mscVrBrSrbStpStorageType,
       "mscVrBrSrbStpIndex": mscVrBrSrbStpIndex,
       "mscVrBrSrbStpProvTable": mscVrBrSrbStpProvTable,
       "mscVrBrSrbStpProvEntry": mscVrBrSrbStpProvEntry,
       "mscVrBrSrbStpStpMode": mscVrBrSrbStpStpMode,
       "mscVrBrSrbStpProtocolSpec": mscVrBrSrbStpProtocolSpec,
       "mscVrBrSrbStpPriority": mscVrBrSrbStpPriority,
       "mscVrBrSrbStpBridgeMaxAge": mscVrBrSrbStpBridgeMaxAge,
       "mscVrBrSrbStpBridgeHelloTime": mscVrBrSrbStpBridgeHelloTime,
       "mscVrBrSrbStpBridgeForwardDelay": mscVrBrSrbStpBridgeForwardDelay,
       "mscVrBrSrbStpOperTable": mscVrBrSrbStpOperTable,
       "mscVrBrSrbStpOperEntry": mscVrBrSrbStpOperEntry,
       "mscVrBrSrbStpBridgeId": mscVrBrSrbStpBridgeId,
       "mscVrBrSrbStpRootPortName": mscVrBrSrbStpRootPortName,
       "mscVrBrSrbStpTimeSinceTopologyChange": mscVrBrSrbStpTimeSinceTopologyChange,
       "mscVrBrSrbStpTopologyChangeDetect": mscVrBrSrbStpTopologyChangeDetect,
       "mscVrBrSrbStpTopologyChanges": mscVrBrSrbStpTopologyChanges,
       "mscVrBrSrbStpDesignatedRoot": mscVrBrSrbStpDesignatedRoot,
       "mscVrBrSrbStpRootCost": mscVrBrSrbStpRootCost,
       "mscVrBrSrbStpMaxAge": mscVrBrSrbStpMaxAge,
       "mscVrBrSrbStpAgingTimeOper": mscVrBrSrbStpAgingTimeOper,
       "mscVrBrSrbStpHelloTime": mscVrBrSrbStpHelloTime,
       "mscVrBrSrbStpHoldTime": mscVrBrSrbStpHoldTime,
       "mscVrBrSrbStpFwdDelay": mscVrBrSrbStpFwdDelay,
       "mscVrBrSrbLte": mscVrBrSrbLte,
       "mscVrBrSrbLteRowStatusTable": mscVrBrSrbLteRowStatusTable,
       "mscVrBrSrbLteRowStatusEntry": mscVrBrSrbLteRowStatusEntry,
       "mscVrBrSrbLteRowStatus": mscVrBrSrbLteRowStatus,
       "mscVrBrSrbLteComponentName": mscVrBrSrbLteComponentName,
       "mscVrBrSrbLteStorageType": mscVrBrSrbLteStorageType,
       "mscVrBrSrbLteLanIdIndex": mscVrBrSrbLteLanIdIndex,
       "mscVrBrSrbLteDomainNumIndex": mscVrBrSrbLteDomainNumIndex,
       "mscVrBrSrbLteOperTable": mscVrBrSrbLteOperTable,
       "mscVrBrSrbLteOperEntry": mscVrBrSrbLteOperEntry,
       "mscVrBrSrbLtePortName": mscVrBrSrbLtePortName,
       "mscVrBrSrbLteAgeOfEntry": mscVrBrSrbLteAgeOfEntry,
       "mscVrBrSrbLtePeerMACAddress": mscVrBrSrbLtePeerMACAddress,
       "mscVrBrSrbLteTypeOfEntry": mscVrBrSrbLteTypeOfEntry,
       "mscVrBrSrbProvTable": mscVrBrSrbProvTable,
       "mscVrBrSrbProvEntry": mscVrBrSrbProvEntry,
       "mscVrBrSrbLanIdTableNumEntries": mscVrBrSrbLanIdTableNumEntries,
       "mscVrBrSrbAgingTime": mscVrBrSrbAgingTime,
       "mscVrBrSrbBridgeLfMode": mscVrBrSrbBridgeLfMode,
       "mscVrBrSrbStatsTable": mscVrBrSrbStatsTable,
       "mscVrBrSrbStatsEntry": mscVrBrSrbStatsEntry,
       "mscVrBrSrbTotalLanIdTableEntries": mscVrBrSrbTotalLanIdTableEntries,
       "mscVrBrSrbNumLanIdtEntriesFree": mscVrBrSrbNumLanIdtEntriesFree,
       "mscVrBrSrbNumLanIdtEntriesDenied": mscVrBrSrbNumLanIdtEntriesDenied,
       "mscVrBrAdminControlTable": mscVrBrAdminControlTable,
       "mscVrBrAdminControlEntry": mscVrBrAdminControlEntry,
       "mscVrBrAdminStatus": mscVrBrAdminStatus,
       "mscVrBrStateTable": mscVrBrStateTable,
       "mscVrBrStateEntry": mscVrBrStateEntry,
       "mscVrBrAdminState": mscVrBrAdminState,
       "mscVrBrOperationalState": mscVrBrOperationalState,
       "mscVrBrUsageState": mscVrBrUsageState,
       "mscVrBrOperStatusTable": mscVrBrOperStatusTable,
       "mscVrBrOperStatusEntry": mscVrBrOperStatusEntry,
       "mscVrBrSnmpOperStatus": mscVrBrSnmpOperStatus,
       "mscVrBrOperTable": mscVrBrOperTable,
       "mscVrBrOperEntry": mscVrBrOperEntry,
       "mscVrBrBridgeAddress": mscVrBrBridgeAddress,
       "mscVrBrNumPorts": mscVrBrNumPorts,
       "mscVrBrType": mscVrBrType,
       "mscCB": mscCB,
       "mscCBRowStatusTable": mscCBRowStatusTable,
       "mscCBRowStatusEntry": mscCBRowStatusEntry,
       "mscCBRowStatus": mscCBRowStatus,
       "mscCBComponentName": mscCBComponentName,
       "mscCBStorageType": mscCBStorageType,
       "mscCBIndex": mscCBIndex,
       "mscCBAdminControlTable": mscCBAdminControlTable,
       "mscCBAdminControlEntry": mscCBAdminControlEntry,
       "mscCBSnmpAdminStatus": mscCBSnmpAdminStatus,
       "mscCBIfEntryTable": mscCBIfEntryTable,
       "mscCBIfEntryEntry": mscCBIfEntryEntry,
       "mscCBIfAdminStatus": mscCBIfAdminStatus,
       "mscCBIfIndex": mscCBIfIndex,
       "mscCBMpTable": mscCBMpTable,
       "mscCBMpEntry": mscCBMpEntry,
       "mscCBLinkToProtocolPort": mscCBLinkToProtocolPort,
       "mscCBOperTable": mscCBOperTable,
       "mscCBOperEntry": mscCBOperEntry,
       "mscCBMacAddress": mscCBMacAddress,
       "mscCBStateTable": mscCBStateTable,
       "mscCBStateEntry": mscCBStateEntry,
       "mscCBAdminState": mscCBAdminState,
       "mscCBOperationalState": mscCBOperationalState,
       "mscCBUsageState": mscCBUsageState,
       "mscCBOperStatusTable": mscCBOperStatusTable,
       "mscCBOperStatusEntry": mscCBOperStatusEntry,
       "mscCBSnmpOperStatus": mscCBSnmpOperStatus,
       "mscPB": mscPB,
       "mscPBRowStatusTable": mscPBRowStatusTable,
       "mscPBRowStatusEntry": mscPBRowStatusEntry,
       "mscPBRowStatus": mscPBRowStatus,
       "mscPBComponentName": mscPBComponentName,
       "mscPBStorageType": mscPBStorageType,
       "mscPBIndex": mscPBIndex,
       "mscPBAdminControlTable": mscPBAdminControlTable,
       "mscPBAdminControlEntry": mscPBAdminControlEntry,
       "mscPBSnmpAdminStatus": mscPBSnmpAdminStatus,
       "mscPBIfEntryTable": mscPBIfEntryTable,
       "mscPBIfEntryEntry": mscPBIfEntryEntry,
       "mscPBIfAdminStatus": mscPBIfAdminStatus,
       "mscPBIfIndex": mscPBIfIndex,
       "mscPBMpTable": mscPBMpTable,
       "mscPBMpEntry": mscPBMpEntry,
       "mscPBLinkToProtocolPort": mscPBLinkToProtocolPort,
       "mscPBOperTable": mscPBOperTable,
       "mscPBOperEntry": mscPBOperEntry,
       "mscPBMacAddress": mscPBMacAddress,
       "mscPBStateTable": mscPBStateTable,
       "mscPBStateEntry": mscPBStateEntry,
       "mscPBAdminState": mscPBAdminState,
       "mscPBOperationalState": mscPBOperationalState,
       "mscPBUsageState": mscPBUsageState,
       "mscPBOperStatusTable": mscPBOperStatusTable,
       "mscPBOperStatusEntry": mscPBOperStatusEntry,
       "mscPBSnmpOperStatus": mscPBSnmpOperStatus,
       "bridgeMIB": bridgeMIB,
       "bridgeGroup": bridgeGroup,
       "bridgeGroupCA": bridgeGroupCA,
       "bridgeGroupCA02": bridgeGroupCA02,
       "bridgeGroupCA02A": bridgeGroupCA02A,
       "bridgeCapabilities": bridgeCapabilities,
       "bridgeCapabilitiesCA": bridgeCapabilitiesCA,
       "bridgeCapabilitiesCA02": bridgeCapabilitiesCA02,
       "bridgeCapabilitiesCA02A": bridgeCapabilitiesCA02A}
)
