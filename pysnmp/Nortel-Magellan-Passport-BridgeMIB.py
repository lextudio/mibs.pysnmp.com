# SNMP MIB module (Nortel-Magellan-Passport-BridgeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-BridgeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:28 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

(vr,
 vrIndex,
 vrPp,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
    "vrIndex",
    "vrPp",
    "vrPpIndex")

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

_VrPpTbcl_ObjectIdentity = ObjectIdentity
vrPpTbcl = _VrPpTbcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2)
)
_VrPpTbclRowStatusTable_Object = MibTable
vrPpTbclRowStatusTable = _VrPpTbclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpTbclRowStatusTable.setStatus("mandatory")
_VrPpTbclRowStatusEntry_Object = MibTableRow
vrPpTbclRowStatusEntry = _VrPpTbclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 1, 1)
)
vrPpTbclRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclRowStatusEntry.setStatus("mandatory")
_VrPpTbclRowStatus_Type = RowStatus
_VrPpTbclRowStatus_Object = MibTableColumn
vrPpTbclRowStatus = _VrPpTbclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 1, 1, 1),
    _VrPpTbclRowStatus_Type()
)
vrPpTbclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclRowStatus.setStatus("mandatory")
_VrPpTbclComponentName_Type = DisplayString
_VrPpTbclComponentName_Object = MibTableColumn
vrPpTbclComponentName = _VrPpTbclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 1, 1, 2),
    _VrPpTbclComponentName_Type()
)
vrPpTbclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclComponentName.setStatus("mandatory")
_VrPpTbclStorageType_Type = StorageType
_VrPpTbclStorageType_Object = MibTableColumn
vrPpTbclStorageType = _VrPpTbclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 1, 1, 4),
    _VrPpTbclStorageType_Type()
)
vrPpTbclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclStorageType.setStatus("mandatory")
_VrPpTbclIndex_Type = NonReplicated
_VrPpTbclIndex_Object = MibTableColumn
vrPpTbclIndex = _VrPpTbclIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 1, 1, 10),
    _VrPpTbclIndex_Type()
)
vrPpTbclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpTbclIndex.setStatus("mandatory")
_VrPpTbclNs_ObjectIdentity = ObjectIdentity
vrPpTbclNs = _VrPpTbclNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2)
)
_VrPpTbclNsRowStatusTable_Object = MibTable
vrPpTbclNsRowStatusTable = _VrPpTbclNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpTbclNsRowStatusTable.setStatus("mandatory")
_VrPpTbclNsRowStatusEntry_Object = MibTableRow
vrPpTbclNsRowStatusEntry = _VrPpTbclNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 1, 1)
)
vrPpTbclNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclNsRowStatusEntry.setStatus("mandatory")
_VrPpTbclNsRowStatus_Type = RowStatus
_VrPpTbclNsRowStatus_Object = MibTableColumn
vrPpTbclNsRowStatus = _VrPpTbclNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 1, 1, 1),
    _VrPpTbclNsRowStatus_Type()
)
vrPpTbclNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclNsRowStatus.setStatus("mandatory")
_VrPpTbclNsComponentName_Type = DisplayString
_VrPpTbclNsComponentName_Object = MibTableColumn
vrPpTbclNsComponentName = _VrPpTbclNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 1, 1, 2),
    _VrPpTbclNsComponentName_Type()
)
vrPpTbclNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclNsComponentName.setStatus("mandatory")
_VrPpTbclNsStorageType_Type = StorageType
_VrPpTbclNsStorageType_Object = MibTableColumn
vrPpTbclNsStorageType = _VrPpTbclNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 1, 1, 4),
    _VrPpTbclNsStorageType_Type()
)
vrPpTbclNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclNsStorageType.setStatus("mandatory")
_VrPpTbclNsIndex_Type = NonReplicated
_VrPpTbclNsIndex_Object = MibTableColumn
vrPpTbclNsIndex = _VrPpTbclNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 1, 1, 10),
    _VrPpTbclNsIndex_Type()
)
vrPpTbclNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpTbclNsIndex.setStatus("mandatory")
_VrPpTbclNsProvTable_Object = MibTable
vrPpTbclNsProvTable = _VrPpTbclNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpTbclNsProvTable.setStatus("mandatory")
_VrPpTbclNsProvEntry_Object = MibTableRow
vrPpTbclNsProvEntry = _VrPpTbclNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 10, 1)
)
vrPpTbclNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclNsProvEntry.setStatus("mandatory")


class _VrPpTbclNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpTbclNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpTbclNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpTbclNsIncomingFilter_Object = MibTableColumn
vrPpTbclNsIncomingFilter = _VrPpTbclNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 10, 1, 2),
    _VrPpTbclNsIncomingFilter_Type()
)
vrPpTbclNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclNsIncomingFilter.setStatus("mandatory")


class _VrPpTbclNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpTbclNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpTbclNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpTbclNsOutgoingFilter_Object = MibTableColumn
vrPpTbclNsOutgoingFilter = _VrPpTbclNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 2, 10, 1, 3),
    _VrPpTbclNsOutgoingFilter_Type()
)
vrPpTbclNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclNsOutgoingFilter.setStatus("mandatory")
_VrPpTbclProvTable_Object = MibTable
vrPpTbclProvTable = _VrPpTbclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpTbclProvTable.setStatus("mandatory")
_VrPpTbclProvEntry_Object = MibTableRow
vrPpTbclProvEntry = _VrPpTbclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1)
)
vrPpTbclProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclProvEntry.setStatus("mandatory")


class _VrPpTbclTranslateIpx_Type(Integer32):
    """Custom type vrPpTbclTranslateIpx based on Integer32"""
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


_VrPpTbclTranslateIpx_Type.__name__ = "Integer32"
_VrPpTbclTranslateIpx_Object = MibTableColumn
vrPpTbclTranslateIpx = _VrPpTbclTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1, 1),
    _VrPpTbclTranslateIpx_Type()
)
vrPpTbclTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclTranslateIpx.setStatus("mandatory")


class _VrPpTbclFragmentIp_Type(Integer32):
    """Custom type vrPpTbclFragmentIp based on Integer32"""
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


_VrPpTbclFragmentIp_Type.__name__ = "Integer32"
_VrPpTbclFragmentIp_Object = MibTableColumn
vrPpTbclFragmentIp = _VrPpTbclFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1, 2),
    _VrPpTbclFragmentIp_Type()
)
vrPpTbclFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclFragmentIp.setStatus("mandatory")


class _VrPpTbclServiceClass_Type(Integer32):
    """Custom type vrPpTbclServiceClass based on Integer32"""
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


_VrPpTbclServiceClass_Type.__name__ = "Integer32"
_VrPpTbclServiceClass_Object = MibTableColumn
vrPpTbclServiceClass = _VrPpTbclServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1, 3),
    _VrPpTbclServiceClass_Type()
)
vrPpTbclServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclServiceClass.setStatus("mandatory")


class _VrPpTbclConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpTbclConvertArpMacAddress based on Integer32"""
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


_VrPpTbclConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpTbclConvertArpMacAddress_Object = MibTableColumn
vrPpTbclConvertArpMacAddress = _VrPpTbclConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1, 4),
    _VrPpTbclConvertArpMacAddress_Type()
)
vrPpTbclConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclConvertArpMacAddress.setStatus("mandatory")


class _VrPpTbclPortNum_Type(Unsigned32):
    """Custom type vrPpTbclPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpTbclPortNum_Type.__name__ = "Unsigned32"
_VrPpTbclPortNum_Object = MibTableColumn
vrPpTbclPortNum = _VrPpTbclPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1, 5),
    _VrPpTbclPortNum_Type()
)
vrPpTbclPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclPortNum.setStatus("mandatory")


class _VrPpTbclOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpTbclOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpTbclOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpTbclOutboundFrameMediaType_Object = MibTableColumn
vrPpTbclOutboundFrameMediaType = _VrPpTbclOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 10, 1, 6),
    _VrPpTbclOutboundFrameMediaType_Type()
)
vrPpTbclOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclOutboundFrameMediaType.setStatus("mandatory")
_VrPpTbclTbProvTable_Object = MibTable
vrPpTbclTbProvTable = _VrPpTbclTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 11)
)
if mibBuilder.loadTexts:
    vrPpTbclTbProvTable.setStatus("mandatory")
_VrPpTbclTbProvEntry_Object = MibTableRow
vrPpTbclTbProvEntry = _VrPpTbclTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 11, 1)
)
vrPpTbclTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclTbProvEntry.setStatus("mandatory")


class _VrPpTbclSecureOption_Type(Integer32):
    """Custom type vrPpTbclSecureOption based on Integer32"""
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


_VrPpTbclSecureOption_Type.__name__ = "Integer32"
_VrPpTbclSecureOption_Object = MibTableColumn
vrPpTbclSecureOption = _VrPpTbclSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 11, 1, 1),
    _VrPpTbclSecureOption_Type()
)
vrPpTbclSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclSecureOption.setStatus("mandatory")
_VrPpTbclStpProvTable_Object = MibTable
vrPpTbclStpProvTable = _VrPpTbclStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12)
)
if mibBuilder.loadTexts:
    vrPpTbclStpProvTable.setStatus("mandatory")
_VrPpTbclStpProvEntry_Object = MibTableRow
vrPpTbclStpProvEntry = _VrPpTbclStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1)
)
vrPpTbclStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclStpProvEntry.setStatus("mandatory")


class _VrPpTbclAdminStatus_Type(Integer32):
    """Custom type vrPpTbclAdminStatus based on Integer32"""
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


_VrPpTbclAdminStatus_Type.__name__ = "Integer32"
_VrPpTbclAdminStatus_Object = MibTableColumn
vrPpTbclAdminStatus = _VrPpTbclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1, 1),
    _VrPpTbclAdminStatus_Type()
)
vrPpTbclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclAdminStatus.setStatus("mandatory")


class _VrPpTbclPortStateStpControl_Type(Integer32):
    """Custom type vrPpTbclPortStateStpControl based on Integer32"""
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


_VrPpTbclPortStateStpControl_Type.__name__ = "Integer32"
_VrPpTbclPortStateStpControl_Object = MibTableColumn
vrPpTbclPortStateStpControl = _VrPpTbclPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1, 2),
    _VrPpTbclPortStateStpControl_Type()
)
vrPpTbclPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclPortStateStpControl.setStatus("mandatory")


class _VrPpTbclStpTypeProv_Type(Integer32):
    """Custom type vrPpTbclStpTypeProv based on Integer32"""
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


_VrPpTbclStpTypeProv_Type.__name__ = "Integer32"
_VrPpTbclStpTypeProv_Object = MibTableColumn
vrPpTbclStpTypeProv = _VrPpTbclStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1, 3),
    _VrPpTbclStpTypeProv_Type()
)
vrPpTbclStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclStpTypeProv.setStatus("mandatory")


class _VrPpTbclPortPriority_Type(Unsigned32):
    """Custom type vrPpTbclPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbclPortPriority_Type.__name__ = "Unsigned32"
_VrPpTbclPortPriority_Object = MibTableColumn
vrPpTbclPortPriority = _VrPpTbclPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1, 4),
    _VrPpTbclPortPriority_Type()
)
vrPpTbclPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclPortPriority.setStatus("mandatory")


class _VrPpTbclPathCost_Type(Unsigned32):
    """Custom type vrPpTbclPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbclPathCost_Type.__name__ = "Unsigned32"
_VrPpTbclPathCost_Object = MibTableColumn
vrPpTbclPathCost = _VrPpTbclPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1, 5),
    _VrPpTbclPathCost_Type()
)
vrPpTbclPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclPathCost.setStatus("mandatory")


class _VrPpTbclPathCostMethod_Type(Integer32):
    """Custom type vrPpTbclPathCostMethod based on Integer32"""
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


_VrPpTbclPathCostMethod_Type.__name__ = "Integer32"
_VrPpTbclPathCostMethod_Object = MibTableColumn
vrPpTbclPathCostMethod = _VrPpTbclPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 12, 1, 6),
    _VrPpTbclPathCostMethod_Type()
)
vrPpTbclPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclPathCostMethod.setStatus("mandatory")
_VrPpTbclDIProvTable_Object = MibTable
vrPpTbclDIProvTable = _VrPpTbclDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 13)
)
if mibBuilder.loadTexts:
    vrPpTbclDIProvTable.setStatus("mandatory")
_VrPpTbclDIProvEntry_Object = MibTableRow
vrPpTbclDIProvEntry = _VrPpTbclDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 13, 1)
)
vrPpTbclDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclDIProvEntry.setStatus("mandatory")


class _VrPpTbclDomainNum_Type(Unsigned32):
    """Custom type vrPpTbclDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpTbclDomainNum_Type.__name__ = "Unsigned32"
_VrPpTbclDomainNum_Object = MibTableColumn
vrPpTbclDomainNum = _VrPpTbclDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 13, 1, 1),
    _VrPpTbclDomainNum_Type()
)
vrPpTbclDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclDomainNum.setStatus("mandatory")


class _VrPpTbclPreserveDomain_Type(Integer32):
    """Custom type vrPpTbclPreserveDomain based on Integer32"""
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


_VrPpTbclPreserveDomain_Type.__name__ = "Integer32"
_VrPpTbclPreserveDomain_Object = MibTableColumn
vrPpTbclPreserveDomain = _VrPpTbclPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 13, 1, 2),
    _VrPpTbclPreserveDomain_Type()
)
vrPpTbclPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbclPreserveDomain.setStatus("mandatory")
_VrPpTbclStateTable_Object = MibTable
vrPpTbclStateTable = _VrPpTbclStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 14)
)
if mibBuilder.loadTexts:
    vrPpTbclStateTable.setStatus("mandatory")
_VrPpTbclStateEntry_Object = MibTableRow
vrPpTbclStateEntry = _VrPpTbclStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 14, 1)
)
vrPpTbclStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclStateEntry.setStatus("mandatory")


class _VrPpTbclAdminState_Type(Integer32):
    """Custom type vrPpTbclAdminState based on Integer32"""
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


_VrPpTbclAdminState_Type.__name__ = "Integer32"
_VrPpTbclAdminState_Object = MibTableColumn
vrPpTbclAdminState = _VrPpTbclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 14, 1, 1),
    _VrPpTbclAdminState_Type()
)
vrPpTbclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclAdminState.setStatus("mandatory")


class _VrPpTbclOperationalState_Type(Integer32):
    """Custom type vrPpTbclOperationalState based on Integer32"""
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


_VrPpTbclOperationalState_Type.__name__ = "Integer32"
_VrPpTbclOperationalState_Object = MibTableColumn
vrPpTbclOperationalState = _VrPpTbclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 14, 1, 2),
    _VrPpTbclOperationalState_Type()
)
vrPpTbclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclOperationalState.setStatus("mandatory")


class _VrPpTbclUsageState_Type(Integer32):
    """Custom type vrPpTbclUsageState based on Integer32"""
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


_VrPpTbclUsageState_Type.__name__ = "Integer32"
_VrPpTbclUsageState_Object = MibTableColumn
vrPpTbclUsageState = _VrPpTbclUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 14, 1, 3),
    _VrPpTbclUsageState_Type()
)
vrPpTbclUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclUsageState.setStatus("mandatory")
_VrPpTbclOperStatusTable_Object = MibTable
vrPpTbclOperStatusTable = _VrPpTbclOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 15)
)
if mibBuilder.loadTexts:
    vrPpTbclOperStatusTable.setStatus("mandatory")
_VrPpTbclOperStatusEntry_Object = MibTableRow
vrPpTbclOperStatusEntry = _VrPpTbclOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 15, 1)
)
vrPpTbclOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclOperStatusEntry.setStatus("mandatory")


class _VrPpTbclSnmpOperStatus_Type(Integer32):
    """Custom type vrPpTbclSnmpOperStatus based on Integer32"""
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


_VrPpTbclSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpTbclSnmpOperStatus_Object = MibTableColumn
vrPpTbclSnmpOperStatus = _VrPpTbclSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 15, 1, 1),
    _VrPpTbclSnmpOperStatus_Type()
)
vrPpTbclSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclSnmpOperStatus.setStatus("mandatory")
_VrPpTbclOperTable_Object = MibTable
vrPpTbclOperTable = _VrPpTbclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16)
)
if mibBuilder.loadTexts:
    vrPpTbclOperTable.setStatus("mandatory")
_VrPpTbclOperEntry_Object = MibTableRow
vrPpTbclOperEntry = _VrPpTbclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1)
)
vrPpTbclOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclOperEntry.setStatus("mandatory")


class _VrPpTbclPortName_Type(AsciiString):
    """Custom type vrPpTbclPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpTbclPortName_Type.__name__ = "AsciiString"
_VrPpTbclPortName_Object = MibTableColumn
vrPpTbclPortName = _VrPpTbclPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 1),
    _VrPpTbclPortName_Type()
)
vrPpTbclPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclPortName.setStatus("mandatory")


class _VrPpTbclUpTime_Type(Unsigned32):
    """Custom type vrPpTbclUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbclUpTime_Type.__name__ = "Unsigned32"
_VrPpTbclUpTime_Object = MibTableColumn
vrPpTbclUpTime = _VrPpTbclUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 3),
    _VrPpTbclUpTime_Type()
)
vrPpTbclUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclUpTime.setStatus("mandatory")


class _VrPpTbclDownTime_Type(Unsigned32):
    """Custom type vrPpTbclDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbclDownTime_Type.__name__ = "Unsigned32"
_VrPpTbclDownTime_Object = MibTableColumn
vrPpTbclDownTime = _VrPpTbclDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 4),
    _VrPpTbclDownTime_Type()
)
vrPpTbclDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDownTime.setStatus("mandatory")


class _VrPpTbclBridgingMode_Type(Integer32):
    """Custom type vrPpTbclBridgingMode based on Integer32"""
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


_VrPpTbclBridgingMode_Type.__name__ = "Integer32"
_VrPpTbclBridgingMode_Object = MibTableColumn
vrPpTbclBridgingMode = _VrPpTbclBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 5),
    _VrPpTbclBridgingMode_Type()
)
vrPpTbclBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclBridgingMode.setStatus("mandatory")


class _VrPpTbclBridgePortConfig_Type(Integer32):
    """Custom type vrPpTbclBridgePortConfig based on Integer32"""
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


_VrPpTbclBridgePortConfig_Type.__name__ = "Integer32"
_VrPpTbclBridgePortConfig_Object = MibTableColumn
vrPpTbclBridgePortConfig = _VrPpTbclBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 6),
    _VrPpTbclBridgePortConfig_Type()
)
vrPpTbclBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclBridgePortConfig.setStatus("mandatory")


class _VrPpTbclBridgePortType_Type(Integer32):
    """Custom type vrPpTbclBridgePortType based on Integer32"""
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


_VrPpTbclBridgePortType_Type.__name__ = "Integer32"
_VrPpTbclBridgePortType_Object = MibTableColumn
vrPpTbclBridgePortType = _VrPpTbclBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 7),
    _VrPpTbclBridgePortType_Type()
)
vrPpTbclBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclBridgePortType.setStatus("mandatory")


class _VrPpTbclIfIndex_Type(InterfaceIndex):
    """Custom type vrPpTbclIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbclIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpTbclIfIndex_Object = MibTableColumn
vrPpTbclIfIndex = _VrPpTbclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 8),
    _VrPpTbclIfIndex_Type()
)
vrPpTbclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclIfIndex.setStatus("mandatory")
_VrPpTbclDelayExceededDiscards_Type = Counter32
_VrPpTbclDelayExceededDiscards_Object = MibTableColumn
vrPpTbclDelayExceededDiscards = _VrPpTbclDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 10),
    _VrPpTbclDelayExceededDiscards_Type()
)
vrPpTbclDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDelayExceededDiscards.setStatus("mandatory")
_VrPpTbclMtuExceededDiscards_Type = Counter32
_VrPpTbclMtuExceededDiscards_Object = MibTableColumn
vrPpTbclMtuExceededDiscards = _VrPpTbclMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 16, 1, 11),
    _VrPpTbclMtuExceededDiscards_Type()
)
vrPpTbclMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclMtuExceededDiscards.setStatus("mandatory")
_VrPpTbclTbOperTable_Object = MibTable
vrPpTbclTbOperTable = _VrPpTbclTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17)
)
if mibBuilder.loadTexts:
    vrPpTbclTbOperTable.setStatus("mandatory")
_VrPpTbclTbOperEntry_Object = MibTableRow
vrPpTbclTbOperEntry = _VrPpTbclTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1)
)
vrPpTbclTbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclTbOperEntry.setStatus("mandatory")


class _VrPpTbclMaxInfo_Type(Unsigned32):
    """Custom type vrPpTbclMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbclMaxInfo_Type.__name__ = "Unsigned32"
_VrPpTbclMaxInfo_Object = MibTableColumn
vrPpTbclMaxInfo = _VrPpTbclMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 2),
    _VrPpTbclMaxInfo_Type()
)
vrPpTbclMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclMaxInfo.setStatus("mandatory")
_VrPpTbclBadVerifyDiscards_Type = Counter32
_VrPpTbclBadVerifyDiscards_Object = MibTableColumn
vrPpTbclBadVerifyDiscards = _VrPpTbclBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 3),
    _VrPpTbclBadVerifyDiscards_Type()
)
vrPpTbclBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclBadVerifyDiscards.setStatus("mandatory")
_VrPpTbclUnicastNoMatches_Type = Counter32
_VrPpTbclUnicastNoMatches_Object = MibTableColumn
vrPpTbclUnicastNoMatches = _VrPpTbclUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 4),
    _VrPpTbclUnicastNoMatches_Type()
)
vrPpTbclUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclUnicastNoMatches.setStatus("mandatory")
_VrPpTbclStaticEntryDiscards_Type = Counter32
_VrPpTbclStaticEntryDiscards_Object = MibTableColumn
vrPpTbclStaticEntryDiscards = _VrPpTbclStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 5),
    _VrPpTbclStaticEntryDiscards_Type()
)
vrPpTbclStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclStaticEntryDiscards.setStatus("mandatory")
_VrPpTbclDynamicEntryDiscards_Type = Counter32
_VrPpTbclDynamicEntryDiscards_Object = MibTableColumn
vrPpTbclDynamicEntryDiscards = _VrPpTbclDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 6),
    _VrPpTbclDynamicEntryDiscards_Type()
)
vrPpTbclDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDynamicEntryDiscards.setStatus("mandatory")
_VrPpTbclLearningDiscards_Type = Counter32
_VrPpTbclLearningDiscards_Object = MibTableColumn
vrPpTbclLearningDiscards = _VrPpTbclLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 7),
    _VrPpTbclLearningDiscards_Type()
)
vrPpTbclLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclLearningDiscards.setStatus("mandatory")
_VrPpTbclInDiscards_Type = Counter32
_VrPpTbclInDiscards_Object = MibTableColumn
vrPpTbclInDiscards = _VrPpTbclInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 8),
    _VrPpTbclInDiscards_Type()
)
vrPpTbclInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclInDiscards.setStatus("mandatory")
_VrPpTbclInFrames_Type = Counter32
_VrPpTbclInFrames_Object = MibTableColumn
vrPpTbclInFrames = _VrPpTbclInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 9),
    _VrPpTbclInFrames_Type()
)
vrPpTbclInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclInFrames.setStatus("mandatory")
_VrPpTbclOutFrames_Type = Counter32
_VrPpTbclOutFrames_Object = MibTableColumn
vrPpTbclOutFrames = _VrPpTbclOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 17, 1, 10),
    _VrPpTbclOutFrames_Type()
)
vrPpTbclOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclOutFrames.setStatus("mandatory")
_VrPpTbclStpOperTable_Object = MibTable
vrPpTbclStpOperTable = _VrPpTbclStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18)
)
if mibBuilder.loadTexts:
    vrPpTbclStpOperTable.setStatus("mandatory")
_VrPpTbclStpOperEntry_Object = MibTableRow
vrPpTbclStpOperEntry = _VrPpTbclStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1)
)
vrPpTbclStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclStpOperEntry.setStatus("mandatory")


class _VrPpTbclStpPortState_Type(Integer32):
    """Custom type vrPpTbclStpPortState based on Integer32"""
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


_VrPpTbclStpPortState_Type.__name__ = "Integer32"
_VrPpTbclStpPortState_Object = MibTableColumn
vrPpTbclStpPortState = _VrPpTbclStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 2),
    _VrPpTbclStpPortState_Type()
)
vrPpTbclStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclStpPortState.setStatus("mandatory")


class _VrPpTbclStpTypeOper_Type(Integer32):
    """Custom type vrPpTbclStpTypeOper based on Integer32"""
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


_VrPpTbclStpTypeOper_Type.__name__ = "Integer32"
_VrPpTbclStpTypeOper_Object = MibTableColumn
vrPpTbclStpTypeOper = _VrPpTbclStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 3),
    _VrPpTbclStpTypeOper_Type()
)
vrPpTbclStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclStpTypeOper.setStatus("mandatory")


class _VrPpTbclDesignatedCost_Type(Unsigned32):
    """Custom type vrPpTbclDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbclDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpTbclDesignatedCost_Object = MibTableColumn
vrPpTbclDesignatedCost = _VrPpTbclDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 4),
    _VrPpTbclDesignatedCost_Type()
)
vrPpTbclDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDesignatedCost.setStatus("mandatory")


class _VrPpTbclPathCostOper_Type(Unsigned32):
    """Custom type vrPpTbclPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbclPathCostOper_Type.__name__ = "Unsigned32"
_VrPpTbclPathCostOper_Object = MibTableColumn
vrPpTbclPathCostOper = _VrPpTbclPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 5),
    _VrPpTbclPathCostOper_Type()
)
vrPpTbclPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclPathCostOper.setStatus("mandatory")


class _VrPpTbclDesignatedBridge_Type(BridgeId):
    """Custom type vrPpTbclDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbclDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpTbclDesignatedBridge_Object = MibTableColumn
vrPpTbclDesignatedBridge = _VrPpTbclDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 6),
    _VrPpTbclDesignatedBridge_Type()
)
vrPpTbclDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDesignatedBridge.setStatus("mandatory")


class _VrPpTbclDesignatedPort_Type(Hex):
    """Custom type vrPpTbclDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbclDesignatedPort_Type.__name__ = "Hex"
_VrPpTbclDesignatedPort_Object = MibTableColumn
vrPpTbclDesignatedPort = _VrPpTbclDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 7),
    _VrPpTbclDesignatedPort_Type()
)
vrPpTbclDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDesignatedPort.setStatus("mandatory")
_VrPpTbclForwardTransitions_Type = Counter32
_VrPpTbclForwardTransitions_Object = MibTableColumn
vrPpTbclForwardTransitions = _VrPpTbclForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 8),
    _VrPpTbclForwardTransitions_Type()
)
vrPpTbclForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclForwardTransitions.setStatus("mandatory")
_VrPpTbclBlockingDiscards_Type = Counter32
_VrPpTbclBlockingDiscards_Object = MibTableColumn
vrPpTbclBlockingDiscards = _VrPpTbclBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 9),
    _VrPpTbclBlockingDiscards_Type()
)
vrPpTbclBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclBlockingDiscards.setStatus("mandatory")


class _VrPpTbclDesignatedRoot_Type(BridgeId):
    """Custom type vrPpTbclDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbclDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpTbclDesignatedRoot_Object = MibTableColumn
vrPpTbclDesignatedRoot = _VrPpTbclDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 18, 1, 10),
    _VrPpTbclDesignatedRoot_Type()
)
vrPpTbclDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclDesignatedRoot.setStatus("mandatory")
_VrPpTbclStatsTable_Object = MibTable
vrPpTbclStatsTable = _VrPpTbclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19)
)
if mibBuilder.loadTexts:
    vrPpTbclStatsTable.setStatus("mandatory")
_VrPpTbclStatsEntry_Object = MibTableRow
vrPpTbclStatsEntry = _VrPpTbclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19, 1)
)
vrPpTbclStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbclIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbclStatsEntry.setStatus("mandatory")
_VrPpTbclBadAbstractDiscards_Type = Counter32
_VrPpTbclBadAbstractDiscards_Object = MibTableColumn
vrPpTbclBadAbstractDiscards = _VrPpTbclBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19, 1, 1),
    _VrPpTbclBadAbstractDiscards_Type()
)
vrPpTbclBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclBadAbstractDiscards.setStatus("mandatory")
_VrPpTbclTinygramFramesIn_Type = Counter32
_VrPpTbclTinygramFramesIn_Object = MibTableColumn
vrPpTbclTinygramFramesIn = _VrPpTbclTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19, 1, 2),
    _VrPpTbclTinygramFramesIn_Type()
)
vrPpTbclTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclTinygramFramesIn.setStatus("mandatory")
_VrPpTbclTinygramFramesOut_Type = Counter32
_VrPpTbclTinygramFramesOut_Object = MibTableColumn
vrPpTbclTinygramFramesOut = _VrPpTbclTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19, 1, 3),
    _VrPpTbclTinygramFramesOut_Type()
)
vrPpTbclTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclTinygramFramesOut.setStatus("mandatory")
_VrPpTbclInFilterDiscards_Type = Counter32
_VrPpTbclInFilterDiscards_Object = MibTableColumn
vrPpTbclInFilterDiscards = _VrPpTbclInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19, 1, 4),
    _VrPpTbclInFilterDiscards_Type()
)
vrPpTbclInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclInFilterDiscards.setStatus("mandatory")
_VrPpTbclOutFilterDiscards_Type = Counter32
_VrPpTbclOutFilterDiscards_Object = MibTableColumn
vrPpTbclOutFilterDiscards = _VrPpTbclOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 2, 19, 1, 5),
    _VrPpTbclOutFilterDiscards_Type()
)
vrPpTbclOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbclOutFilterDiscards.setStatus("mandatory")
_VrPpFddiETB_ObjectIdentity = ObjectIdentity
vrPpFddiETB = _VrPpFddiETB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3)
)
_VrPpFddiETBRowStatusTable_Object = MibTable
vrPpFddiETBRowStatusTable = _VrPpFddiETBRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vrPpFddiETBRowStatusTable.setStatus("mandatory")
_VrPpFddiETBRowStatusEntry_Object = MibTableRow
vrPpFddiETBRowStatusEntry = _VrPpFddiETBRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 1, 1)
)
vrPpFddiETBRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBRowStatusEntry.setStatus("mandatory")
_VrPpFddiETBRowStatus_Type = RowStatus
_VrPpFddiETBRowStatus_Object = MibTableColumn
vrPpFddiETBRowStatus = _VrPpFddiETBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 1, 1, 1),
    _VrPpFddiETBRowStatus_Type()
)
vrPpFddiETBRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBRowStatus.setStatus("mandatory")
_VrPpFddiETBComponentName_Type = DisplayString
_VrPpFddiETBComponentName_Object = MibTableColumn
vrPpFddiETBComponentName = _VrPpFddiETBComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 1, 1, 2),
    _VrPpFddiETBComponentName_Type()
)
vrPpFddiETBComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBComponentName.setStatus("mandatory")
_VrPpFddiETBStorageType_Type = StorageType
_VrPpFddiETBStorageType_Object = MibTableColumn
vrPpFddiETBStorageType = _VrPpFddiETBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 1, 1, 4),
    _VrPpFddiETBStorageType_Type()
)
vrPpFddiETBStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBStorageType.setStatus("mandatory")
_VrPpFddiETBIndex_Type = NonReplicated
_VrPpFddiETBIndex_Object = MibTableColumn
vrPpFddiETBIndex = _VrPpFddiETBIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 1, 1, 10),
    _VrPpFddiETBIndex_Type()
)
vrPpFddiETBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpFddiETBIndex.setStatus("mandatory")
_VrPpFddiETBNs_ObjectIdentity = ObjectIdentity
vrPpFddiETBNs = _VrPpFddiETBNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2)
)
_VrPpFddiETBNsRowStatusTable_Object = MibTable
vrPpFddiETBNsRowStatusTable = _VrPpFddiETBNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpFddiETBNsRowStatusTable.setStatus("mandatory")
_VrPpFddiETBNsRowStatusEntry_Object = MibTableRow
vrPpFddiETBNsRowStatusEntry = _VrPpFddiETBNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 1, 1)
)
vrPpFddiETBNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBNsRowStatusEntry.setStatus("mandatory")
_VrPpFddiETBNsRowStatus_Type = RowStatus
_VrPpFddiETBNsRowStatus_Object = MibTableColumn
vrPpFddiETBNsRowStatus = _VrPpFddiETBNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 1, 1, 1),
    _VrPpFddiETBNsRowStatus_Type()
)
vrPpFddiETBNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBNsRowStatus.setStatus("mandatory")
_VrPpFddiETBNsComponentName_Type = DisplayString
_VrPpFddiETBNsComponentName_Object = MibTableColumn
vrPpFddiETBNsComponentName = _VrPpFddiETBNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 1, 1, 2),
    _VrPpFddiETBNsComponentName_Type()
)
vrPpFddiETBNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBNsComponentName.setStatus("mandatory")
_VrPpFddiETBNsStorageType_Type = StorageType
_VrPpFddiETBNsStorageType_Object = MibTableColumn
vrPpFddiETBNsStorageType = _VrPpFddiETBNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 1, 1, 4),
    _VrPpFddiETBNsStorageType_Type()
)
vrPpFddiETBNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBNsStorageType.setStatus("mandatory")
_VrPpFddiETBNsIndex_Type = NonReplicated
_VrPpFddiETBNsIndex_Object = MibTableColumn
vrPpFddiETBNsIndex = _VrPpFddiETBNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 1, 1, 10),
    _VrPpFddiETBNsIndex_Type()
)
vrPpFddiETBNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpFddiETBNsIndex.setStatus("mandatory")
_VrPpFddiETBNsProvTable_Object = MibTable
vrPpFddiETBNsProvTable = _VrPpFddiETBNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpFddiETBNsProvTable.setStatus("mandatory")
_VrPpFddiETBNsProvEntry_Object = MibTableRow
vrPpFddiETBNsProvEntry = _VrPpFddiETBNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 10, 1)
)
vrPpFddiETBNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBNsProvEntry.setStatus("mandatory")


class _VrPpFddiETBNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpFddiETBNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpFddiETBNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpFddiETBNsIncomingFilter_Object = MibTableColumn
vrPpFddiETBNsIncomingFilter = _VrPpFddiETBNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 10, 1, 2),
    _VrPpFddiETBNsIncomingFilter_Type()
)
vrPpFddiETBNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBNsIncomingFilter.setStatus("mandatory")


class _VrPpFddiETBNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpFddiETBNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpFddiETBNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpFddiETBNsOutgoingFilter_Object = MibTableColumn
vrPpFddiETBNsOutgoingFilter = _VrPpFddiETBNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 2, 10, 1, 3),
    _VrPpFddiETBNsOutgoingFilter_Type()
)
vrPpFddiETBNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBNsOutgoingFilter.setStatus("mandatory")
_VrPpFddiETBProvTable_Object = MibTable
vrPpFddiETBProvTable = _VrPpFddiETBProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10)
)
if mibBuilder.loadTexts:
    vrPpFddiETBProvTable.setStatus("mandatory")
_VrPpFddiETBProvEntry_Object = MibTableRow
vrPpFddiETBProvEntry = _VrPpFddiETBProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1)
)
vrPpFddiETBProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBProvEntry.setStatus("mandatory")


class _VrPpFddiETBTranslateIpx_Type(Integer32):
    """Custom type vrPpFddiETBTranslateIpx based on Integer32"""
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


_VrPpFddiETBTranslateIpx_Type.__name__ = "Integer32"
_VrPpFddiETBTranslateIpx_Object = MibTableColumn
vrPpFddiETBTranslateIpx = _VrPpFddiETBTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1, 1),
    _VrPpFddiETBTranslateIpx_Type()
)
vrPpFddiETBTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBTranslateIpx.setStatus("mandatory")


class _VrPpFddiETBFragmentIp_Type(Integer32):
    """Custom type vrPpFddiETBFragmentIp based on Integer32"""
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


_VrPpFddiETBFragmentIp_Type.__name__ = "Integer32"
_VrPpFddiETBFragmentIp_Object = MibTableColumn
vrPpFddiETBFragmentIp = _VrPpFddiETBFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1, 2),
    _VrPpFddiETBFragmentIp_Type()
)
vrPpFddiETBFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBFragmentIp.setStatus("mandatory")


class _VrPpFddiETBServiceClass_Type(Integer32):
    """Custom type vrPpFddiETBServiceClass based on Integer32"""
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


_VrPpFddiETBServiceClass_Type.__name__ = "Integer32"
_VrPpFddiETBServiceClass_Object = MibTableColumn
vrPpFddiETBServiceClass = _VrPpFddiETBServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1, 3),
    _VrPpFddiETBServiceClass_Type()
)
vrPpFddiETBServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBServiceClass.setStatus("mandatory")


class _VrPpFddiETBConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpFddiETBConvertArpMacAddress based on Integer32"""
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


_VrPpFddiETBConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpFddiETBConvertArpMacAddress_Object = MibTableColumn
vrPpFddiETBConvertArpMacAddress = _VrPpFddiETBConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1, 4),
    _VrPpFddiETBConvertArpMacAddress_Type()
)
vrPpFddiETBConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBConvertArpMacAddress.setStatus("mandatory")


class _VrPpFddiETBPortNum_Type(Unsigned32):
    """Custom type vrPpFddiETBPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpFddiETBPortNum_Type.__name__ = "Unsigned32"
_VrPpFddiETBPortNum_Object = MibTableColumn
vrPpFddiETBPortNum = _VrPpFddiETBPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1, 5),
    _VrPpFddiETBPortNum_Type()
)
vrPpFddiETBPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBPortNum.setStatus("mandatory")


class _VrPpFddiETBOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpFddiETBOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpFddiETBOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpFddiETBOutboundFrameMediaType_Object = MibTableColumn
vrPpFddiETBOutboundFrameMediaType = _VrPpFddiETBOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 10, 1, 6),
    _VrPpFddiETBOutboundFrameMediaType_Type()
)
vrPpFddiETBOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBOutboundFrameMediaType.setStatus("mandatory")
_VrPpFddiETBTbProvTable_Object = MibTable
vrPpFddiETBTbProvTable = _VrPpFddiETBTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 11)
)
if mibBuilder.loadTexts:
    vrPpFddiETBTbProvTable.setStatus("mandatory")
_VrPpFddiETBTbProvEntry_Object = MibTableRow
vrPpFddiETBTbProvEntry = _VrPpFddiETBTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 11, 1)
)
vrPpFddiETBTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBTbProvEntry.setStatus("mandatory")


class _VrPpFddiETBSecureOption_Type(Integer32):
    """Custom type vrPpFddiETBSecureOption based on Integer32"""
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


_VrPpFddiETBSecureOption_Type.__name__ = "Integer32"
_VrPpFddiETBSecureOption_Object = MibTableColumn
vrPpFddiETBSecureOption = _VrPpFddiETBSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 11, 1, 1),
    _VrPpFddiETBSecureOption_Type()
)
vrPpFddiETBSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBSecureOption.setStatus("mandatory")
_VrPpFddiETBStpProvTable_Object = MibTable
vrPpFddiETBStpProvTable = _VrPpFddiETBStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12)
)
if mibBuilder.loadTexts:
    vrPpFddiETBStpProvTable.setStatus("mandatory")
_VrPpFddiETBStpProvEntry_Object = MibTableRow
vrPpFddiETBStpProvEntry = _VrPpFddiETBStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1)
)
vrPpFddiETBStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBStpProvEntry.setStatus("mandatory")


class _VrPpFddiETBAdminStatus_Type(Integer32):
    """Custom type vrPpFddiETBAdminStatus based on Integer32"""
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


_VrPpFddiETBAdminStatus_Type.__name__ = "Integer32"
_VrPpFddiETBAdminStatus_Object = MibTableColumn
vrPpFddiETBAdminStatus = _VrPpFddiETBAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1, 1),
    _VrPpFddiETBAdminStatus_Type()
)
vrPpFddiETBAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBAdminStatus.setStatus("mandatory")


class _VrPpFddiETBPortStateStpControl_Type(Integer32):
    """Custom type vrPpFddiETBPortStateStpControl based on Integer32"""
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


_VrPpFddiETBPortStateStpControl_Type.__name__ = "Integer32"
_VrPpFddiETBPortStateStpControl_Object = MibTableColumn
vrPpFddiETBPortStateStpControl = _VrPpFddiETBPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1, 2),
    _VrPpFddiETBPortStateStpControl_Type()
)
vrPpFddiETBPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBPortStateStpControl.setStatus("mandatory")


class _VrPpFddiETBStpTypeProv_Type(Integer32):
    """Custom type vrPpFddiETBStpTypeProv based on Integer32"""
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


_VrPpFddiETBStpTypeProv_Type.__name__ = "Integer32"
_VrPpFddiETBStpTypeProv_Object = MibTableColumn
vrPpFddiETBStpTypeProv = _VrPpFddiETBStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1, 3),
    _VrPpFddiETBStpTypeProv_Type()
)
vrPpFddiETBStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBStpTypeProv.setStatus("mandatory")


class _VrPpFddiETBPortPriority_Type(Unsigned32):
    """Custom type vrPpFddiETBPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpFddiETBPortPriority_Type.__name__ = "Unsigned32"
_VrPpFddiETBPortPriority_Object = MibTableColumn
vrPpFddiETBPortPriority = _VrPpFddiETBPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1, 4),
    _VrPpFddiETBPortPriority_Type()
)
vrPpFddiETBPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBPortPriority.setStatus("mandatory")


class _VrPpFddiETBPathCost_Type(Unsigned32):
    """Custom type vrPpFddiETBPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpFddiETBPathCost_Type.__name__ = "Unsigned32"
_VrPpFddiETBPathCost_Object = MibTableColumn
vrPpFddiETBPathCost = _VrPpFddiETBPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1, 5),
    _VrPpFddiETBPathCost_Type()
)
vrPpFddiETBPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBPathCost.setStatus("mandatory")


class _VrPpFddiETBPathCostMethod_Type(Integer32):
    """Custom type vrPpFddiETBPathCostMethod based on Integer32"""
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


_VrPpFddiETBPathCostMethod_Type.__name__ = "Integer32"
_VrPpFddiETBPathCostMethod_Object = MibTableColumn
vrPpFddiETBPathCostMethod = _VrPpFddiETBPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 12, 1, 6),
    _VrPpFddiETBPathCostMethod_Type()
)
vrPpFddiETBPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBPathCostMethod.setStatus("mandatory")
_VrPpFddiETBDIProvTable_Object = MibTable
vrPpFddiETBDIProvTable = _VrPpFddiETBDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 13)
)
if mibBuilder.loadTexts:
    vrPpFddiETBDIProvTable.setStatus("mandatory")
_VrPpFddiETBDIProvEntry_Object = MibTableRow
vrPpFddiETBDIProvEntry = _VrPpFddiETBDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 13, 1)
)
vrPpFddiETBDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBDIProvEntry.setStatus("mandatory")


class _VrPpFddiETBDomainNum_Type(Unsigned32):
    """Custom type vrPpFddiETBDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpFddiETBDomainNum_Type.__name__ = "Unsigned32"
_VrPpFddiETBDomainNum_Object = MibTableColumn
vrPpFddiETBDomainNum = _VrPpFddiETBDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 13, 1, 1),
    _VrPpFddiETBDomainNum_Type()
)
vrPpFddiETBDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBDomainNum.setStatus("mandatory")


class _VrPpFddiETBPreserveDomain_Type(Integer32):
    """Custom type vrPpFddiETBPreserveDomain based on Integer32"""
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


_VrPpFddiETBPreserveDomain_Type.__name__ = "Integer32"
_VrPpFddiETBPreserveDomain_Object = MibTableColumn
vrPpFddiETBPreserveDomain = _VrPpFddiETBPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 13, 1, 2),
    _VrPpFddiETBPreserveDomain_Type()
)
vrPpFddiETBPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpFddiETBPreserveDomain.setStatus("mandatory")
_VrPpFddiETBStateTable_Object = MibTable
vrPpFddiETBStateTable = _VrPpFddiETBStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 14)
)
if mibBuilder.loadTexts:
    vrPpFddiETBStateTable.setStatus("mandatory")
_VrPpFddiETBStateEntry_Object = MibTableRow
vrPpFddiETBStateEntry = _VrPpFddiETBStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 14, 1)
)
vrPpFddiETBStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBStateEntry.setStatus("mandatory")


class _VrPpFddiETBAdminState_Type(Integer32):
    """Custom type vrPpFddiETBAdminState based on Integer32"""
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


_VrPpFddiETBAdminState_Type.__name__ = "Integer32"
_VrPpFddiETBAdminState_Object = MibTableColumn
vrPpFddiETBAdminState = _VrPpFddiETBAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 14, 1, 1),
    _VrPpFddiETBAdminState_Type()
)
vrPpFddiETBAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBAdminState.setStatus("mandatory")


class _VrPpFddiETBOperationalState_Type(Integer32):
    """Custom type vrPpFddiETBOperationalState based on Integer32"""
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


_VrPpFddiETBOperationalState_Type.__name__ = "Integer32"
_VrPpFddiETBOperationalState_Object = MibTableColumn
vrPpFddiETBOperationalState = _VrPpFddiETBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 14, 1, 2),
    _VrPpFddiETBOperationalState_Type()
)
vrPpFddiETBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBOperationalState.setStatus("mandatory")


class _VrPpFddiETBUsageState_Type(Integer32):
    """Custom type vrPpFddiETBUsageState based on Integer32"""
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


_VrPpFddiETBUsageState_Type.__name__ = "Integer32"
_VrPpFddiETBUsageState_Object = MibTableColumn
vrPpFddiETBUsageState = _VrPpFddiETBUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 14, 1, 3),
    _VrPpFddiETBUsageState_Type()
)
vrPpFddiETBUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBUsageState.setStatus("mandatory")
_VrPpFddiETBOperStatusTable_Object = MibTable
vrPpFddiETBOperStatusTable = _VrPpFddiETBOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 15)
)
if mibBuilder.loadTexts:
    vrPpFddiETBOperStatusTable.setStatus("mandatory")
_VrPpFddiETBOperStatusEntry_Object = MibTableRow
vrPpFddiETBOperStatusEntry = _VrPpFddiETBOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 15, 1)
)
vrPpFddiETBOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBOperStatusEntry.setStatus("mandatory")


class _VrPpFddiETBSnmpOperStatus_Type(Integer32):
    """Custom type vrPpFddiETBSnmpOperStatus based on Integer32"""
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


_VrPpFddiETBSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpFddiETBSnmpOperStatus_Object = MibTableColumn
vrPpFddiETBSnmpOperStatus = _VrPpFddiETBSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 15, 1, 1),
    _VrPpFddiETBSnmpOperStatus_Type()
)
vrPpFddiETBSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBSnmpOperStatus.setStatus("mandatory")
_VrPpFddiETBOperTable_Object = MibTable
vrPpFddiETBOperTable = _VrPpFddiETBOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16)
)
if mibBuilder.loadTexts:
    vrPpFddiETBOperTable.setStatus("mandatory")
_VrPpFddiETBOperEntry_Object = MibTableRow
vrPpFddiETBOperEntry = _VrPpFddiETBOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1)
)
vrPpFddiETBOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBOperEntry.setStatus("mandatory")


class _VrPpFddiETBPortName_Type(AsciiString):
    """Custom type vrPpFddiETBPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpFddiETBPortName_Type.__name__ = "AsciiString"
_VrPpFddiETBPortName_Object = MibTableColumn
vrPpFddiETBPortName = _VrPpFddiETBPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 1),
    _VrPpFddiETBPortName_Type()
)
vrPpFddiETBPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBPortName.setStatus("mandatory")


class _VrPpFddiETBUpTime_Type(Unsigned32):
    """Custom type vrPpFddiETBUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpFddiETBUpTime_Type.__name__ = "Unsigned32"
_VrPpFddiETBUpTime_Object = MibTableColumn
vrPpFddiETBUpTime = _VrPpFddiETBUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 3),
    _VrPpFddiETBUpTime_Type()
)
vrPpFddiETBUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBUpTime.setStatus("mandatory")


class _VrPpFddiETBDownTime_Type(Unsigned32):
    """Custom type vrPpFddiETBDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpFddiETBDownTime_Type.__name__ = "Unsigned32"
_VrPpFddiETBDownTime_Object = MibTableColumn
vrPpFddiETBDownTime = _VrPpFddiETBDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 4),
    _VrPpFddiETBDownTime_Type()
)
vrPpFddiETBDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDownTime.setStatus("mandatory")


class _VrPpFddiETBBridgingMode_Type(Integer32):
    """Custom type vrPpFddiETBBridgingMode based on Integer32"""
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


_VrPpFddiETBBridgingMode_Type.__name__ = "Integer32"
_VrPpFddiETBBridgingMode_Object = MibTableColumn
vrPpFddiETBBridgingMode = _VrPpFddiETBBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 5),
    _VrPpFddiETBBridgingMode_Type()
)
vrPpFddiETBBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBBridgingMode.setStatus("mandatory")


class _VrPpFddiETBBridgePortConfig_Type(Integer32):
    """Custom type vrPpFddiETBBridgePortConfig based on Integer32"""
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


_VrPpFddiETBBridgePortConfig_Type.__name__ = "Integer32"
_VrPpFddiETBBridgePortConfig_Object = MibTableColumn
vrPpFddiETBBridgePortConfig = _VrPpFddiETBBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 6),
    _VrPpFddiETBBridgePortConfig_Type()
)
vrPpFddiETBBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBBridgePortConfig.setStatus("mandatory")


class _VrPpFddiETBBridgePortType_Type(Integer32):
    """Custom type vrPpFddiETBBridgePortType based on Integer32"""
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


_VrPpFddiETBBridgePortType_Type.__name__ = "Integer32"
_VrPpFddiETBBridgePortType_Object = MibTableColumn
vrPpFddiETBBridgePortType = _VrPpFddiETBBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 7),
    _VrPpFddiETBBridgePortType_Type()
)
vrPpFddiETBBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBBridgePortType.setStatus("mandatory")


class _VrPpFddiETBIfIndex_Type(InterfaceIndex):
    """Custom type vrPpFddiETBIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpFddiETBIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpFddiETBIfIndex_Object = MibTableColumn
vrPpFddiETBIfIndex = _VrPpFddiETBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 8),
    _VrPpFddiETBIfIndex_Type()
)
vrPpFddiETBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBIfIndex.setStatus("mandatory")
_VrPpFddiETBDelayExceededDiscards_Type = Counter32
_VrPpFddiETBDelayExceededDiscards_Object = MibTableColumn
vrPpFddiETBDelayExceededDiscards = _VrPpFddiETBDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 10),
    _VrPpFddiETBDelayExceededDiscards_Type()
)
vrPpFddiETBDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDelayExceededDiscards.setStatus("mandatory")
_VrPpFddiETBMtuExceededDiscards_Type = Counter32
_VrPpFddiETBMtuExceededDiscards_Object = MibTableColumn
vrPpFddiETBMtuExceededDiscards = _VrPpFddiETBMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 16, 1, 11),
    _VrPpFddiETBMtuExceededDiscards_Type()
)
vrPpFddiETBMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBMtuExceededDiscards.setStatus("mandatory")
_VrPpFddiETBTbOperTable_Object = MibTable
vrPpFddiETBTbOperTable = _VrPpFddiETBTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17)
)
if mibBuilder.loadTexts:
    vrPpFddiETBTbOperTable.setStatus("mandatory")
_VrPpFddiETBTbOperEntry_Object = MibTableRow
vrPpFddiETBTbOperEntry = _VrPpFddiETBTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1)
)
vrPpFddiETBTbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBTbOperEntry.setStatus("mandatory")


class _VrPpFddiETBMaxInfo_Type(Unsigned32):
    """Custom type vrPpFddiETBMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpFddiETBMaxInfo_Type.__name__ = "Unsigned32"
_VrPpFddiETBMaxInfo_Object = MibTableColumn
vrPpFddiETBMaxInfo = _VrPpFddiETBMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 2),
    _VrPpFddiETBMaxInfo_Type()
)
vrPpFddiETBMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBMaxInfo.setStatus("mandatory")
_VrPpFddiETBBadVerifyDiscards_Type = Counter32
_VrPpFddiETBBadVerifyDiscards_Object = MibTableColumn
vrPpFddiETBBadVerifyDiscards = _VrPpFddiETBBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 3),
    _VrPpFddiETBBadVerifyDiscards_Type()
)
vrPpFddiETBBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBBadVerifyDiscards.setStatus("mandatory")
_VrPpFddiETBUnicastNoMatches_Type = Counter32
_VrPpFddiETBUnicastNoMatches_Object = MibTableColumn
vrPpFddiETBUnicastNoMatches = _VrPpFddiETBUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 4),
    _VrPpFddiETBUnicastNoMatches_Type()
)
vrPpFddiETBUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBUnicastNoMatches.setStatus("mandatory")
_VrPpFddiETBStaticEntryDiscards_Type = Counter32
_VrPpFddiETBStaticEntryDiscards_Object = MibTableColumn
vrPpFddiETBStaticEntryDiscards = _VrPpFddiETBStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 5),
    _VrPpFddiETBStaticEntryDiscards_Type()
)
vrPpFddiETBStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBStaticEntryDiscards.setStatus("mandatory")
_VrPpFddiETBDynamicEntryDiscards_Type = Counter32
_VrPpFddiETBDynamicEntryDiscards_Object = MibTableColumn
vrPpFddiETBDynamicEntryDiscards = _VrPpFddiETBDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 6),
    _VrPpFddiETBDynamicEntryDiscards_Type()
)
vrPpFddiETBDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDynamicEntryDiscards.setStatus("mandatory")
_VrPpFddiETBLearningDiscards_Type = Counter32
_VrPpFddiETBLearningDiscards_Object = MibTableColumn
vrPpFddiETBLearningDiscards = _VrPpFddiETBLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 7),
    _VrPpFddiETBLearningDiscards_Type()
)
vrPpFddiETBLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBLearningDiscards.setStatus("mandatory")
_VrPpFddiETBInDiscards_Type = Counter32
_VrPpFddiETBInDiscards_Object = MibTableColumn
vrPpFddiETBInDiscards = _VrPpFddiETBInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 8),
    _VrPpFddiETBInDiscards_Type()
)
vrPpFddiETBInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBInDiscards.setStatus("mandatory")
_VrPpFddiETBInFrames_Type = Counter32
_VrPpFddiETBInFrames_Object = MibTableColumn
vrPpFddiETBInFrames = _VrPpFddiETBInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 9),
    _VrPpFddiETBInFrames_Type()
)
vrPpFddiETBInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBInFrames.setStatus("mandatory")
_VrPpFddiETBOutFrames_Type = Counter32
_VrPpFddiETBOutFrames_Object = MibTableColumn
vrPpFddiETBOutFrames = _VrPpFddiETBOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 17, 1, 10),
    _VrPpFddiETBOutFrames_Type()
)
vrPpFddiETBOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBOutFrames.setStatus("mandatory")
_VrPpFddiETBStpOperTable_Object = MibTable
vrPpFddiETBStpOperTable = _VrPpFddiETBStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18)
)
if mibBuilder.loadTexts:
    vrPpFddiETBStpOperTable.setStatus("mandatory")
_VrPpFddiETBStpOperEntry_Object = MibTableRow
vrPpFddiETBStpOperEntry = _VrPpFddiETBStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1)
)
vrPpFddiETBStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBStpOperEntry.setStatus("mandatory")


class _VrPpFddiETBStpPortState_Type(Integer32):
    """Custom type vrPpFddiETBStpPortState based on Integer32"""
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


_VrPpFddiETBStpPortState_Type.__name__ = "Integer32"
_VrPpFddiETBStpPortState_Object = MibTableColumn
vrPpFddiETBStpPortState = _VrPpFddiETBStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 2),
    _VrPpFddiETBStpPortState_Type()
)
vrPpFddiETBStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBStpPortState.setStatus("mandatory")


class _VrPpFddiETBStpTypeOper_Type(Integer32):
    """Custom type vrPpFddiETBStpTypeOper based on Integer32"""
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


_VrPpFddiETBStpTypeOper_Type.__name__ = "Integer32"
_VrPpFddiETBStpTypeOper_Object = MibTableColumn
vrPpFddiETBStpTypeOper = _VrPpFddiETBStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 3),
    _VrPpFddiETBStpTypeOper_Type()
)
vrPpFddiETBStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBStpTypeOper.setStatus("mandatory")


class _VrPpFddiETBDesignatedCost_Type(Unsigned32):
    """Custom type vrPpFddiETBDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpFddiETBDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpFddiETBDesignatedCost_Object = MibTableColumn
vrPpFddiETBDesignatedCost = _VrPpFddiETBDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 4),
    _VrPpFddiETBDesignatedCost_Type()
)
vrPpFddiETBDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDesignatedCost.setStatus("mandatory")


class _VrPpFddiETBPathCostOper_Type(Unsigned32):
    """Custom type vrPpFddiETBPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpFddiETBPathCostOper_Type.__name__ = "Unsigned32"
_VrPpFddiETBPathCostOper_Object = MibTableColumn
vrPpFddiETBPathCostOper = _VrPpFddiETBPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 5),
    _VrPpFddiETBPathCostOper_Type()
)
vrPpFddiETBPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBPathCostOper.setStatus("mandatory")


class _VrPpFddiETBDesignatedBridge_Type(BridgeId):
    """Custom type vrPpFddiETBDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpFddiETBDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpFddiETBDesignatedBridge_Object = MibTableColumn
vrPpFddiETBDesignatedBridge = _VrPpFddiETBDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 6),
    _VrPpFddiETBDesignatedBridge_Type()
)
vrPpFddiETBDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDesignatedBridge.setStatus("mandatory")


class _VrPpFddiETBDesignatedPort_Type(Hex):
    """Custom type vrPpFddiETBDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpFddiETBDesignatedPort_Type.__name__ = "Hex"
_VrPpFddiETBDesignatedPort_Object = MibTableColumn
vrPpFddiETBDesignatedPort = _VrPpFddiETBDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 7),
    _VrPpFddiETBDesignatedPort_Type()
)
vrPpFddiETBDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDesignatedPort.setStatus("mandatory")
_VrPpFddiETBForwardTransitions_Type = Counter32
_VrPpFddiETBForwardTransitions_Object = MibTableColumn
vrPpFddiETBForwardTransitions = _VrPpFddiETBForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 8),
    _VrPpFddiETBForwardTransitions_Type()
)
vrPpFddiETBForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBForwardTransitions.setStatus("mandatory")
_VrPpFddiETBBlockingDiscards_Type = Counter32
_VrPpFddiETBBlockingDiscards_Object = MibTableColumn
vrPpFddiETBBlockingDiscards = _VrPpFddiETBBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 9),
    _VrPpFddiETBBlockingDiscards_Type()
)
vrPpFddiETBBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBBlockingDiscards.setStatus("mandatory")


class _VrPpFddiETBDesignatedRoot_Type(BridgeId):
    """Custom type vrPpFddiETBDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpFddiETBDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpFddiETBDesignatedRoot_Object = MibTableColumn
vrPpFddiETBDesignatedRoot = _VrPpFddiETBDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 18, 1, 10),
    _VrPpFddiETBDesignatedRoot_Type()
)
vrPpFddiETBDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBDesignatedRoot.setStatus("mandatory")
_VrPpFddiETBStatsTable_Object = MibTable
vrPpFddiETBStatsTable = _VrPpFddiETBStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19)
)
if mibBuilder.loadTexts:
    vrPpFddiETBStatsTable.setStatus("mandatory")
_VrPpFddiETBStatsEntry_Object = MibTableRow
vrPpFddiETBStatsEntry = _VrPpFddiETBStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19, 1)
)
vrPpFddiETBStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpFddiETBIndex"),
)
if mibBuilder.loadTexts:
    vrPpFddiETBStatsEntry.setStatus("mandatory")
_VrPpFddiETBBadAbstractDiscards_Type = Counter32
_VrPpFddiETBBadAbstractDiscards_Object = MibTableColumn
vrPpFddiETBBadAbstractDiscards = _VrPpFddiETBBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19, 1, 1),
    _VrPpFddiETBBadAbstractDiscards_Type()
)
vrPpFddiETBBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBBadAbstractDiscards.setStatus("mandatory")
_VrPpFddiETBTinygramFramesIn_Type = Counter32
_VrPpFddiETBTinygramFramesIn_Object = MibTableColumn
vrPpFddiETBTinygramFramesIn = _VrPpFddiETBTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19, 1, 2),
    _VrPpFddiETBTinygramFramesIn_Type()
)
vrPpFddiETBTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBTinygramFramesIn.setStatus("mandatory")
_VrPpFddiETBTinygramFramesOut_Type = Counter32
_VrPpFddiETBTinygramFramesOut_Object = MibTableColumn
vrPpFddiETBTinygramFramesOut = _VrPpFddiETBTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19, 1, 3),
    _VrPpFddiETBTinygramFramesOut_Type()
)
vrPpFddiETBTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBTinygramFramesOut.setStatus("mandatory")
_VrPpFddiETBInFilterDiscards_Type = Counter32
_VrPpFddiETBInFilterDiscards_Object = MibTableColumn
vrPpFddiETBInFilterDiscards = _VrPpFddiETBInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19, 1, 4),
    _VrPpFddiETBInFilterDiscards_Type()
)
vrPpFddiETBInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBInFilterDiscards.setStatus("mandatory")
_VrPpFddiETBOutFilterDiscards_Type = Counter32
_VrPpFddiETBOutFilterDiscards_Object = MibTableColumn
vrPpFddiETBOutFilterDiscards = _VrPpFddiETBOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 3, 19, 1, 5),
    _VrPpFddiETBOutFilterDiscards_Type()
)
vrPpFddiETBOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpFddiETBOutFilterDiscards.setStatus("mandatory")
_VrPpTbp_ObjectIdentity = ObjectIdentity
vrPpTbp = _VrPpTbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4)
)
_VrPpTbpRowStatusTable_Object = MibTable
vrPpTbpRowStatusTable = _VrPpTbpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 1)
)
if mibBuilder.loadTexts:
    vrPpTbpRowStatusTable.setStatus("mandatory")
_VrPpTbpRowStatusEntry_Object = MibTableRow
vrPpTbpRowStatusEntry = _VrPpTbpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 1, 1)
)
vrPpTbpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpRowStatusEntry.setStatus("mandatory")
_VrPpTbpRowStatus_Type = RowStatus
_VrPpTbpRowStatus_Object = MibTableColumn
vrPpTbpRowStatus = _VrPpTbpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 1, 1, 1),
    _VrPpTbpRowStatus_Type()
)
vrPpTbpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpRowStatus.setStatus("mandatory")
_VrPpTbpComponentName_Type = DisplayString
_VrPpTbpComponentName_Object = MibTableColumn
vrPpTbpComponentName = _VrPpTbpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 1, 1, 2),
    _VrPpTbpComponentName_Type()
)
vrPpTbpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpComponentName.setStatus("mandatory")
_VrPpTbpStorageType_Type = StorageType
_VrPpTbpStorageType_Object = MibTableColumn
vrPpTbpStorageType = _VrPpTbpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 1, 1, 4),
    _VrPpTbpStorageType_Type()
)
vrPpTbpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpStorageType.setStatus("mandatory")
_VrPpTbpIndex_Type = NonReplicated
_VrPpTbpIndex_Object = MibTableColumn
vrPpTbpIndex = _VrPpTbpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 1, 1, 10),
    _VrPpTbpIndex_Type()
)
vrPpTbpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpTbpIndex.setStatus("mandatory")
_VrPpTbpNs_ObjectIdentity = ObjectIdentity
vrPpTbpNs = _VrPpTbpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2)
)
_VrPpTbpNsRowStatusTable_Object = MibTable
vrPpTbpNsRowStatusTable = _VrPpTbpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpTbpNsRowStatusTable.setStatus("mandatory")
_VrPpTbpNsRowStatusEntry_Object = MibTableRow
vrPpTbpNsRowStatusEntry = _VrPpTbpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 1, 1)
)
vrPpTbpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpNsRowStatusEntry.setStatus("mandatory")
_VrPpTbpNsRowStatus_Type = RowStatus
_VrPpTbpNsRowStatus_Object = MibTableColumn
vrPpTbpNsRowStatus = _VrPpTbpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 1, 1, 1),
    _VrPpTbpNsRowStatus_Type()
)
vrPpTbpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpNsRowStatus.setStatus("mandatory")
_VrPpTbpNsComponentName_Type = DisplayString
_VrPpTbpNsComponentName_Object = MibTableColumn
vrPpTbpNsComponentName = _VrPpTbpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 1, 1, 2),
    _VrPpTbpNsComponentName_Type()
)
vrPpTbpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpNsComponentName.setStatus("mandatory")
_VrPpTbpNsStorageType_Type = StorageType
_VrPpTbpNsStorageType_Object = MibTableColumn
vrPpTbpNsStorageType = _VrPpTbpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 1, 1, 4),
    _VrPpTbpNsStorageType_Type()
)
vrPpTbpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpNsStorageType.setStatus("mandatory")
_VrPpTbpNsIndex_Type = NonReplicated
_VrPpTbpNsIndex_Object = MibTableColumn
vrPpTbpNsIndex = _VrPpTbpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 1, 1, 10),
    _VrPpTbpNsIndex_Type()
)
vrPpTbpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpTbpNsIndex.setStatus("mandatory")
_VrPpTbpNsProvTable_Object = MibTable
vrPpTbpNsProvTable = _VrPpTbpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpTbpNsProvTable.setStatus("mandatory")
_VrPpTbpNsProvEntry_Object = MibTableRow
vrPpTbpNsProvEntry = _VrPpTbpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 10, 1)
)
vrPpTbpNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpNsProvEntry.setStatus("mandatory")


class _VrPpTbpNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpTbpNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpTbpNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpTbpNsIncomingFilter_Object = MibTableColumn
vrPpTbpNsIncomingFilter = _VrPpTbpNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 10, 1, 2),
    _VrPpTbpNsIncomingFilter_Type()
)
vrPpTbpNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpNsIncomingFilter.setStatus("mandatory")


class _VrPpTbpNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpTbpNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpTbpNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpTbpNsOutgoingFilter_Object = MibTableColumn
vrPpTbpNsOutgoingFilter = _VrPpTbpNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 2, 10, 1, 3),
    _VrPpTbpNsOutgoingFilter_Type()
)
vrPpTbpNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpNsOutgoingFilter.setStatus("mandatory")
_VrPpTbpProvTable_Object = MibTable
vrPpTbpProvTable = _VrPpTbpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10)
)
if mibBuilder.loadTexts:
    vrPpTbpProvTable.setStatus("mandatory")
_VrPpTbpProvEntry_Object = MibTableRow
vrPpTbpProvEntry = _VrPpTbpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1)
)
vrPpTbpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpProvEntry.setStatus("mandatory")


class _VrPpTbpTranslateIpx_Type(Integer32):
    """Custom type vrPpTbpTranslateIpx based on Integer32"""
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


_VrPpTbpTranslateIpx_Type.__name__ = "Integer32"
_VrPpTbpTranslateIpx_Object = MibTableColumn
vrPpTbpTranslateIpx = _VrPpTbpTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1, 1),
    _VrPpTbpTranslateIpx_Type()
)
vrPpTbpTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpTranslateIpx.setStatus("mandatory")


class _VrPpTbpFragmentIp_Type(Integer32):
    """Custom type vrPpTbpFragmentIp based on Integer32"""
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


_VrPpTbpFragmentIp_Type.__name__ = "Integer32"
_VrPpTbpFragmentIp_Object = MibTableColumn
vrPpTbpFragmentIp = _VrPpTbpFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1, 2),
    _VrPpTbpFragmentIp_Type()
)
vrPpTbpFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpFragmentIp.setStatus("mandatory")


class _VrPpTbpServiceClass_Type(Integer32):
    """Custom type vrPpTbpServiceClass based on Integer32"""
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


_VrPpTbpServiceClass_Type.__name__ = "Integer32"
_VrPpTbpServiceClass_Object = MibTableColumn
vrPpTbpServiceClass = _VrPpTbpServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1, 3),
    _VrPpTbpServiceClass_Type()
)
vrPpTbpServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpServiceClass.setStatus("mandatory")


class _VrPpTbpConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpTbpConvertArpMacAddress based on Integer32"""
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


_VrPpTbpConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpTbpConvertArpMacAddress_Object = MibTableColumn
vrPpTbpConvertArpMacAddress = _VrPpTbpConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1, 4),
    _VrPpTbpConvertArpMacAddress_Type()
)
vrPpTbpConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpConvertArpMacAddress.setStatus("mandatory")


class _VrPpTbpPortNum_Type(Unsigned32):
    """Custom type vrPpTbpPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpTbpPortNum_Type.__name__ = "Unsigned32"
_VrPpTbpPortNum_Object = MibTableColumn
vrPpTbpPortNum = _VrPpTbpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1, 5),
    _VrPpTbpPortNum_Type()
)
vrPpTbpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpPortNum.setStatus("mandatory")


class _VrPpTbpOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpTbpOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpTbpOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpTbpOutboundFrameMediaType_Object = MibTableColumn
vrPpTbpOutboundFrameMediaType = _VrPpTbpOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 10, 1, 6),
    _VrPpTbpOutboundFrameMediaType_Type()
)
vrPpTbpOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpOutboundFrameMediaType.setStatus("mandatory")
_VrPpTbpTbProvTable_Object = MibTable
vrPpTbpTbProvTable = _VrPpTbpTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 11)
)
if mibBuilder.loadTexts:
    vrPpTbpTbProvTable.setStatus("mandatory")
_VrPpTbpTbProvEntry_Object = MibTableRow
vrPpTbpTbProvEntry = _VrPpTbpTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 11, 1)
)
vrPpTbpTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpTbProvEntry.setStatus("mandatory")


class _VrPpTbpSecureOption_Type(Integer32):
    """Custom type vrPpTbpSecureOption based on Integer32"""
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


_VrPpTbpSecureOption_Type.__name__ = "Integer32"
_VrPpTbpSecureOption_Object = MibTableColumn
vrPpTbpSecureOption = _VrPpTbpSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 11, 1, 1),
    _VrPpTbpSecureOption_Type()
)
vrPpTbpSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpSecureOption.setStatus("mandatory")
_VrPpTbpStpProvTable_Object = MibTable
vrPpTbpStpProvTable = _VrPpTbpStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12)
)
if mibBuilder.loadTexts:
    vrPpTbpStpProvTable.setStatus("mandatory")
_VrPpTbpStpProvEntry_Object = MibTableRow
vrPpTbpStpProvEntry = _VrPpTbpStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1)
)
vrPpTbpStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpStpProvEntry.setStatus("mandatory")


class _VrPpTbpAdminStatus_Type(Integer32):
    """Custom type vrPpTbpAdminStatus based on Integer32"""
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


_VrPpTbpAdminStatus_Type.__name__ = "Integer32"
_VrPpTbpAdminStatus_Object = MibTableColumn
vrPpTbpAdminStatus = _VrPpTbpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1, 1),
    _VrPpTbpAdminStatus_Type()
)
vrPpTbpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpAdminStatus.setStatus("mandatory")


class _VrPpTbpPortStateStpControl_Type(Integer32):
    """Custom type vrPpTbpPortStateStpControl based on Integer32"""
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


_VrPpTbpPortStateStpControl_Type.__name__ = "Integer32"
_VrPpTbpPortStateStpControl_Object = MibTableColumn
vrPpTbpPortStateStpControl = _VrPpTbpPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1, 2),
    _VrPpTbpPortStateStpControl_Type()
)
vrPpTbpPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpPortStateStpControl.setStatus("mandatory")


class _VrPpTbpStpTypeProv_Type(Integer32):
    """Custom type vrPpTbpStpTypeProv based on Integer32"""
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


_VrPpTbpStpTypeProv_Type.__name__ = "Integer32"
_VrPpTbpStpTypeProv_Object = MibTableColumn
vrPpTbpStpTypeProv = _VrPpTbpStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1, 3),
    _VrPpTbpStpTypeProv_Type()
)
vrPpTbpStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpStpTypeProv.setStatus("mandatory")


class _VrPpTbpPortPriority_Type(Unsigned32):
    """Custom type vrPpTbpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbpPortPriority_Type.__name__ = "Unsigned32"
_VrPpTbpPortPriority_Object = MibTableColumn
vrPpTbpPortPriority = _VrPpTbpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1, 4),
    _VrPpTbpPortPriority_Type()
)
vrPpTbpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpPortPriority.setStatus("mandatory")


class _VrPpTbpPathCost_Type(Unsigned32):
    """Custom type vrPpTbpPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbpPathCost_Type.__name__ = "Unsigned32"
_VrPpTbpPathCost_Object = MibTableColumn
vrPpTbpPathCost = _VrPpTbpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1, 5),
    _VrPpTbpPathCost_Type()
)
vrPpTbpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpPathCost.setStatus("mandatory")


class _VrPpTbpPathCostMethod_Type(Integer32):
    """Custom type vrPpTbpPathCostMethod based on Integer32"""
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


_VrPpTbpPathCostMethod_Type.__name__ = "Integer32"
_VrPpTbpPathCostMethod_Object = MibTableColumn
vrPpTbpPathCostMethod = _VrPpTbpPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 12, 1, 6),
    _VrPpTbpPathCostMethod_Type()
)
vrPpTbpPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpPathCostMethod.setStatus("mandatory")
_VrPpTbpDIProvTable_Object = MibTable
vrPpTbpDIProvTable = _VrPpTbpDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 13)
)
if mibBuilder.loadTexts:
    vrPpTbpDIProvTable.setStatus("mandatory")
_VrPpTbpDIProvEntry_Object = MibTableRow
vrPpTbpDIProvEntry = _VrPpTbpDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 13, 1)
)
vrPpTbpDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpDIProvEntry.setStatus("mandatory")


class _VrPpTbpDomainNum_Type(Unsigned32):
    """Custom type vrPpTbpDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpTbpDomainNum_Type.__name__ = "Unsigned32"
_VrPpTbpDomainNum_Object = MibTableColumn
vrPpTbpDomainNum = _VrPpTbpDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 13, 1, 1),
    _VrPpTbpDomainNum_Type()
)
vrPpTbpDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpDomainNum.setStatus("mandatory")


class _VrPpTbpPreserveDomain_Type(Integer32):
    """Custom type vrPpTbpPreserveDomain based on Integer32"""
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


_VrPpTbpPreserveDomain_Type.__name__ = "Integer32"
_VrPpTbpPreserveDomain_Object = MibTableColumn
vrPpTbpPreserveDomain = _VrPpTbpPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 13, 1, 2),
    _VrPpTbpPreserveDomain_Type()
)
vrPpTbpPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbpPreserveDomain.setStatus("mandatory")
_VrPpTbpStateTable_Object = MibTable
vrPpTbpStateTable = _VrPpTbpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 14)
)
if mibBuilder.loadTexts:
    vrPpTbpStateTable.setStatus("mandatory")
_VrPpTbpStateEntry_Object = MibTableRow
vrPpTbpStateEntry = _VrPpTbpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 14, 1)
)
vrPpTbpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpStateEntry.setStatus("mandatory")


class _VrPpTbpAdminState_Type(Integer32):
    """Custom type vrPpTbpAdminState based on Integer32"""
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


_VrPpTbpAdminState_Type.__name__ = "Integer32"
_VrPpTbpAdminState_Object = MibTableColumn
vrPpTbpAdminState = _VrPpTbpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 14, 1, 1),
    _VrPpTbpAdminState_Type()
)
vrPpTbpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpAdminState.setStatus("mandatory")


class _VrPpTbpOperationalState_Type(Integer32):
    """Custom type vrPpTbpOperationalState based on Integer32"""
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


_VrPpTbpOperationalState_Type.__name__ = "Integer32"
_VrPpTbpOperationalState_Object = MibTableColumn
vrPpTbpOperationalState = _VrPpTbpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 14, 1, 2),
    _VrPpTbpOperationalState_Type()
)
vrPpTbpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpOperationalState.setStatus("mandatory")


class _VrPpTbpUsageState_Type(Integer32):
    """Custom type vrPpTbpUsageState based on Integer32"""
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


_VrPpTbpUsageState_Type.__name__ = "Integer32"
_VrPpTbpUsageState_Object = MibTableColumn
vrPpTbpUsageState = _VrPpTbpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 14, 1, 3),
    _VrPpTbpUsageState_Type()
)
vrPpTbpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpUsageState.setStatus("mandatory")
_VrPpTbpOperStatusTable_Object = MibTable
vrPpTbpOperStatusTable = _VrPpTbpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 15)
)
if mibBuilder.loadTexts:
    vrPpTbpOperStatusTable.setStatus("mandatory")
_VrPpTbpOperStatusEntry_Object = MibTableRow
vrPpTbpOperStatusEntry = _VrPpTbpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 15, 1)
)
vrPpTbpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpOperStatusEntry.setStatus("mandatory")


class _VrPpTbpSnmpOperStatus_Type(Integer32):
    """Custom type vrPpTbpSnmpOperStatus based on Integer32"""
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


_VrPpTbpSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpTbpSnmpOperStatus_Object = MibTableColumn
vrPpTbpSnmpOperStatus = _VrPpTbpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 15, 1, 1),
    _VrPpTbpSnmpOperStatus_Type()
)
vrPpTbpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpSnmpOperStatus.setStatus("mandatory")
_VrPpTbpOperTable_Object = MibTable
vrPpTbpOperTable = _VrPpTbpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16)
)
if mibBuilder.loadTexts:
    vrPpTbpOperTable.setStatus("mandatory")
_VrPpTbpOperEntry_Object = MibTableRow
vrPpTbpOperEntry = _VrPpTbpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1)
)
vrPpTbpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpOperEntry.setStatus("mandatory")


class _VrPpTbpPortName_Type(AsciiString):
    """Custom type vrPpTbpPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpTbpPortName_Type.__name__ = "AsciiString"
_VrPpTbpPortName_Object = MibTableColumn
vrPpTbpPortName = _VrPpTbpPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 1),
    _VrPpTbpPortName_Type()
)
vrPpTbpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpPortName.setStatus("mandatory")


class _VrPpTbpUpTime_Type(Unsigned32):
    """Custom type vrPpTbpUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbpUpTime_Type.__name__ = "Unsigned32"
_VrPpTbpUpTime_Object = MibTableColumn
vrPpTbpUpTime = _VrPpTbpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 3),
    _VrPpTbpUpTime_Type()
)
vrPpTbpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpUpTime.setStatus("mandatory")


class _VrPpTbpDownTime_Type(Unsigned32):
    """Custom type vrPpTbpDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbpDownTime_Type.__name__ = "Unsigned32"
_VrPpTbpDownTime_Object = MibTableColumn
vrPpTbpDownTime = _VrPpTbpDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 4),
    _VrPpTbpDownTime_Type()
)
vrPpTbpDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDownTime.setStatus("mandatory")


class _VrPpTbpBridgingMode_Type(Integer32):
    """Custom type vrPpTbpBridgingMode based on Integer32"""
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


_VrPpTbpBridgingMode_Type.__name__ = "Integer32"
_VrPpTbpBridgingMode_Object = MibTableColumn
vrPpTbpBridgingMode = _VrPpTbpBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 5),
    _VrPpTbpBridgingMode_Type()
)
vrPpTbpBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpBridgingMode.setStatus("mandatory")


class _VrPpTbpBridgePortConfig_Type(Integer32):
    """Custom type vrPpTbpBridgePortConfig based on Integer32"""
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


_VrPpTbpBridgePortConfig_Type.__name__ = "Integer32"
_VrPpTbpBridgePortConfig_Object = MibTableColumn
vrPpTbpBridgePortConfig = _VrPpTbpBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 6),
    _VrPpTbpBridgePortConfig_Type()
)
vrPpTbpBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpBridgePortConfig.setStatus("mandatory")


class _VrPpTbpBridgePortType_Type(Integer32):
    """Custom type vrPpTbpBridgePortType based on Integer32"""
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


_VrPpTbpBridgePortType_Type.__name__ = "Integer32"
_VrPpTbpBridgePortType_Object = MibTableColumn
vrPpTbpBridgePortType = _VrPpTbpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 7),
    _VrPpTbpBridgePortType_Type()
)
vrPpTbpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpBridgePortType.setStatus("mandatory")


class _VrPpTbpIfIndex_Type(InterfaceIndex):
    """Custom type vrPpTbpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbpIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpTbpIfIndex_Object = MibTableColumn
vrPpTbpIfIndex = _VrPpTbpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 8),
    _VrPpTbpIfIndex_Type()
)
vrPpTbpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpIfIndex.setStatus("mandatory")
_VrPpTbpDelayExceededDiscards_Type = Counter32
_VrPpTbpDelayExceededDiscards_Object = MibTableColumn
vrPpTbpDelayExceededDiscards = _VrPpTbpDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 10),
    _VrPpTbpDelayExceededDiscards_Type()
)
vrPpTbpDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDelayExceededDiscards.setStatus("mandatory")
_VrPpTbpMtuExceededDiscards_Type = Counter32
_VrPpTbpMtuExceededDiscards_Object = MibTableColumn
vrPpTbpMtuExceededDiscards = _VrPpTbpMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 16, 1, 11),
    _VrPpTbpMtuExceededDiscards_Type()
)
vrPpTbpMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpMtuExceededDiscards.setStatus("mandatory")
_VrPpTbpTbOperTable_Object = MibTable
vrPpTbpTbOperTable = _VrPpTbpTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17)
)
if mibBuilder.loadTexts:
    vrPpTbpTbOperTable.setStatus("mandatory")
_VrPpTbpTbOperEntry_Object = MibTableRow
vrPpTbpTbOperEntry = _VrPpTbpTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1)
)
vrPpTbpTbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpTbOperEntry.setStatus("mandatory")


class _VrPpTbpMaxInfo_Type(Unsigned32):
    """Custom type vrPpTbpMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbpMaxInfo_Type.__name__ = "Unsigned32"
_VrPpTbpMaxInfo_Object = MibTableColumn
vrPpTbpMaxInfo = _VrPpTbpMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 2),
    _VrPpTbpMaxInfo_Type()
)
vrPpTbpMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpMaxInfo.setStatus("mandatory")
_VrPpTbpBadVerifyDiscards_Type = Counter32
_VrPpTbpBadVerifyDiscards_Object = MibTableColumn
vrPpTbpBadVerifyDiscards = _VrPpTbpBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 3),
    _VrPpTbpBadVerifyDiscards_Type()
)
vrPpTbpBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpBadVerifyDiscards.setStatus("mandatory")
_VrPpTbpUnicastNoMatches_Type = Counter32
_VrPpTbpUnicastNoMatches_Object = MibTableColumn
vrPpTbpUnicastNoMatches = _VrPpTbpUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 4),
    _VrPpTbpUnicastNoMatches_Type()
)
vrPpTbpUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpUnicastNoMatches.setStatus("mandatory")
_VrPpTbpStaticEntryDiscards_Type = Counter32
_VrPpTbpStaticEntryDiscards_Object = MibTableColumn
vrPpTbpStaticEntryDiscards = _VrPpTbpStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 5),
    _VrPpTbpStaticEntryDiscards_Type()
)
vrPpTbpStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpStaticEntryDiscards.setStatus("mandatory")
_VrPpTbpDynamicEntryDiscards_Type = Counter32
_VrPpTbpDynamicEntryDiscards_Object = MibTableColumn
vrPpTbpDynamicEntryDiscards = _VrPpTbpDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 6),
    _VrPpTbpDynamicEntryDiscards_Type()
)
vrPpTbpDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDynamicEntryDiscards.setStatus("mandatory")
_VrPpTbpLearningDiscards_Type = Counter32
_VrPpTbpLearningDiscards_Object = MibTableColumn
vrPpTbpLearningDiscards = _VrPpTbpLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 7),
    _VrPpTbpLearningDiscards_Type()
)
vrPpTbpLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpLearningDiscards.setStatus("mandatory")
_VrPpTbpInDiscards_Type = Counter32
_VrPpTbpInDiscards_Object = MibTableColumn
vrPpTbpInDiscards = _VrPpTbpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 8),
    _VrPpTbpInDiscards_Type()
)
vrPpTbpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpInDiscards.setStatus("mandatory")
_VrPpTbpInFrames_Type = Counter32
_VrPpTbpInFrames_Object = MibTableColumn
vrPpTbpInFrames = _VrPpTbpInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 9),
    _VrPpTbpInFrames_Type()
)
vrPpTbpInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpInFrames.setStatus("mandatory")
_VrPpTbpOutFrames_Type = Counter32
_VrPpTbpOutFrames_Object = MibTableColumn
vrPpTbpOutFrames = _VrPpTbpOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 17, 1, 10),
    _VrPpTbpOutFrames_Type()
)
vrPpTbpOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpOutFrames.setStatus("mandatory")
_VrPpTbpStpOperTable_Object = MibTable
vrPpTbpStpOperTable = _VrPpTbpStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18)
)
if mibBuilder.loadTexts:
    vrPpTbpStpOperTable.setStatus("mandatory")
_VrPpTbpStpOperEntry_Object = MibTableRow
vrPpTbpStpOperEntry = _VrPpTbpStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1)
)
vrPpTbpStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpStpOperEntry.setStatus("mandatory")


class _VrPpTbpStpPortState_Type(Integer32):
    """Custom type vrPpTbpStpPortState based on Integer32"""
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


_VrPpTbpStpPortState_Type.__name__ = "Integer32"
_VrPpTbpStpPortState_Object = MibTableColumn
vrPpTbpStpPortState = _VrPpTbpStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 2),
    _VrPpTbpStpPortState_Type()
)
vrPpTbpStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpStpPortState.setStatus("mandatory")


class _VrPpTbpStpTypeOper_Type(Integer32):
    """Custom type vrPpTbpStpTypeOper based on Integer32"""
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


_VrPpTbpStpTypeOper_Type.__name__ = "Integer32"
_VrPpTbpStpTypeOper_Object = MibTableColumn
vrPpTbpStpTypeOper = _VrPpTbpStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 3),
    _VrPpTbpStpTypeOper_Type()
)
vrPpTbpStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpStpTypeOper.setStatus("mandatory")


class _VrPpTbpDesignatedCost_Type(Unsigned32):
    """Custom type vrPpTbpDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbpDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpTbpDesignatedCost_Object = MibTableColumn
vrPpTbpDesignatedCost = _VrPpTbpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 4),
    _VrPpTbpDesignatedCost_Type()
)
vrPpTbpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDesignatedCost.setStatus("mandatory")


class _VrPpTbpPathCostOper_Type(Unsigned32):
    """Custom type vrPpTbpPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbpPathCostOper_Type.__name__ = "Unsigned32"
_VrPpTbpPathCostOper_Object = MibTableColumn
vrPpTbpPathCostOper = _VrPpTbpPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 5),
    _VrPpTbpPathCostOper_Type()
)
vrPpTbpPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpPathCostOper.setStatus("mandatory")


class _VrPpTbpDesignatedBridge_Type(BridgeId):
    """Custom type vrPpTbpDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbpDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpTbpDesignatedBridge_Object = MibTableColumn
vrPpTbpDesignatedBridge = _VrPpTbpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 6),
    _VrPpTbpDesignatedBridge_Type()
)
vrPpTbpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDesignatedBridge.setStatus("mandatory")


class _VrPpTbpDesignatedPort_Type(Hex):
    """Custom type vrPpTbpDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbpDesignatedPort_Type.__name__ = "Hex"
_VrPpTbpDesignatedPort_Object = MibTableColumn
vrPpTbpDesignatedPort = _VrPpTbpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 7),
    _VrPpTbpDesignatedPort_Type()
)
vrPpTbpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDesignatedPort.setStatus("mandatory")
_VrPpTbpForwardTransitions_Type = Counter32
_VrPpTbpForwardTransitions_Object = MibTableColumn
vrPpTbpForwardTransitions = _VrPpTbpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 8),
    _VrPpTbpForwardTransitions_Type()
)
vrPpTbpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpForwardTransitions.setStatus("mandatory")
_VrPpTbpBlockingDiscards_Type = Counter32
_VrPpTbpBlockingDiscards_Object = MibTableColumn
vrPpTbpBlockingDiscards = _VrPpTbpBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 9),
    _VrPpTbpBlockingDiscards_Type()
)
vrPpTbpBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpBlockingDiscards.setStatus("mandatory")


class _VrPpTbpDesignatedRoot_Type(BridgeId):
    """Custom type vrPpTbpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbpDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpTbpDesignatedRoot_Object = MibTableColumn
vrPpTbpDesignatedRoot = _VrPpTbpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 18, 1, 10),
    _VrPpTbpDesignatedRoot_Type()
)
vrPpTbpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpDesignatedRoot.setStatus("mandatory")
_VrPpTbpStatsTable_Object = MibTable
vrPpTbpStatsTable = _VrPpTbpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19)
)
if mibBuilder.loadTexts:
    vrPpTbpStatsTable.setStatus("mandatory")
_VrPpTbpStatsEntry_Object = MibTableRow
vrPpTbpStatsEntry = _VrPpTbpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19, 1)
)
vrPpTbpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbpIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbpStatsEntry.setStatus("mandatory")
_VrPpTbpBadAbstractDiscards_Type = Counter32
_VrPpTbpBadAbstractDiscards_Object = MibTableColumn
vrPpTbpBadAbstractDiscards = _VrPpTbpBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19, 1, 1),
    _VrPpTbpBadAbstractDiscards_Type()
)
vrPpTbpBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpBadAbstractDiscards.setStatus("mandatory")
_VrPpTbpTinygramFramesIn_Type = Counter32
_VrPpTbpTinygramFramesIn_Object = MibTableColumn
vrPpTbpTinygramFramesIn = _VrPpTbpTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19, 1, 2),
    _VrPpTbpTinygramFramesIn_Type()
)
vrPpTbpTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpTinygramFramesIn.setStatus("mandatory")
_VrPpTbpTinygramFramesOut_Type = Counter32
_VrPpTbpTinygramFramesOut_Object = MibTableColumn
vrPpTbpTinygramFramesOut = _VrPpTbpTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19, 1, 3),
    _VrPpTbpTinygramFramesOut_Type()
)
vrPpTbpTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpTinygramFramesOut.setStatus("mandatory")
_VrPpTbpInFilterDiscards_Type = Counter32
_VrPpTbpInFilterDiscards_Object = MibTableColumn
vrPpTbpInFilterDiscards = _VrPpTbpInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19, 1, 4),
    _VrPpTbpInFilterDiscards_Type()
)
vrPpTbpInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpInFilterDiscards.setStatus("mandatory")
_VrPpTbpOutFilterDiscards_Type = Counter32
_VrPpTbpOutFilterDiscards_Object = MibTableColumn
vrPpTbpOutFilterDiscards = _VrPpTbpOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 4, 19, 1, 5),
    _VrPpTbpOutFilterDiscards_Type()
)
vrPpTbpOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbpOutFilterDiscards.setStatus("mandatory")
_VrPpSrBp_ObjectIdentity = ObjectIdentity
vrPpSrBp = _VrPpSrBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8)
)
_VrPpSrBpRowStatusTable_Object = MibTable
vrPpSrBpRowStatusTable = _VrPpSrBpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 1)
)
if mibBuilder.loadTexts:
    vrPpSrBpRowStatusTable.setStatus("mandatory")
_VrPpSrBpRowStatusEntry_Object = MibTableRow
vrPpSrBpRowStatusEntry = _VrPpSrBpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 1, 1)
)
vrPpSrBpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpRowStatusEntry.setStatus("mandatory")
_VrPpSrBpRowStatus_Type = RowStatus
_VrPpSrBpRowStatus_Object = MibTableColumn
vrPpSrBpRowStatus = _VrPpSrBpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 1, 1, 1),
    _VrPpSrBpRowStatus_Type()
)
vrPpSrBpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpRowStatus.setStatus("mandatory")
_VrPpSrBpComponentName_Type = DisplayString
_VrPpSrBpComponentName_Object = MibTableColumn
vrPpSrBpComponentName = _VrPpSrBpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 1, 1, 2),
    _VrPpSrBpComponentName_Type()
)
vrPpSrBpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpComponentName.setStatus("mandatory")
_VrPpSrBpStorageType_Type = StorageType
_VrPpSrBpStorageType_Object = MibTableColumn
vrPpSrBpStorageType = _VrPpSrBpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 1, 1, 4),
    _VrPpSrBpStorageType_Type()
)
vrPpSrBpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpStorageType.setStatus("mandatory")
_VrPpSrBpIndex_Type = NonReplicated
_VrPpSrBpIndex_Object = MibTableColumn
vrPpSrBpIndex = _VrPpSrBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 1, 1, 10),
    _VrPpSrBpIndex_Type()
)
vrPpSrBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrBpIndex.setStatus("mandatory")
_VrPpSrBpNs_ObjectIdentity = ObjectIdentity
vrPpSrBpNs = _VrPpSrBpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2)
)
_VrPpSrBpNsRowStatusTable_Object = MibTable
vrPpSrBpNsRowStatusTable = _VrPpSrBpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpSrBpNsRowStatusTable.setStatus("mandatory")
_VrPpSrBpNsRowStatusEntry_Object = MibTableRow
vrPpSrBpNsRowStatusEntry = _VrPpSrBpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 1, 1)
)
vrPpSrBpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpNsRowStatusEntry.setStatus("mandatory")
_VrPpSrBpNsRowStatus_Type = RowStatus
_VrPpSrBpNsRowStatus_Object = MibTableColumn
vrPpSrBpNsRowStatus = _VrPpSrBpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 1, 1, 1),
    _VrPpSrBpNsRowStatus_Type()
)
vrPpSrBpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpNsRowStatus.setStatus("mandatory")
_VrPpSrBpNsComponentName_Type = DisplayString
_VrPpSrBpNsComponentName_Object = MibTableColumn
vrPpSrBpNsComponentName = _VrPpSrBpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 1, 1, 2),
    _VrPpSrBpNsComponentName_Type()
)
vrPpSrBpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpNsComponentName.setStatus("mandatory")
_VrPpSrBpNsStorageType_Type = StorageType
_VrPpSrBpNsStorageType_Object = MibTableColumn
vrPpSrBpNsStorageType = _VrPpSrBpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 1, 1, 4),
    _VrPpSrBpNsStorageType_Type()
)
vrPpSrBpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpNsStorageType.setStatus("mandatory")
_VrPpSrBpNsIndex_Type = NonReplicated
_VrPpSrBpNsIndex_Object = MibTableColumn
vrPpSrBpNsIndex = _VrPpSrBpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 1, 1, 10),
    _VrPpSrBpNsIndex_Type()
)
vrPpSrBpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrBpNsIndex.setStatus("mandatory")
_VrPpSrBpNsProvTable_Object = MibTable
vrPpSrBpNsProvTable = _VrPpSrBpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpSrBpNsProvTable.setStatus("mandatory")
_VrPpSrBpNsProvEntry_Object = MibTableRow
vrPpSrBpNsProvEntry = _VrPpSrBpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 10, 1)
)
vrPpSrBpNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpNsProvEntry.setStatus("mandatory")


class _VrPpSrBpNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpSrBpNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpSrBpNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpSrBpNsIncomingFilter_Object = MibTableColumn
vrPpSrBpNsIncomingFilter = _VrPpSrBpNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 10, 1, 2),
    _VrPpSrBpNsIncomingFilter_Type()
)
vrPpSrBpNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpNsIncomingFilter.setStatus("mandatory")


class _VrPpSrBpNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpSrBpNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpSrBpNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpSrBpNsOutgoingFilter_Object = MibTableColumn
vrPpSrBpNsOutgoingFilter = _VrPpSrBpNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 2, 10, 1, 3),
    _VrPpSrBpNsOutgoingFilter_Type()
)
vrPpSrBpNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpNsOutgoingFilter.setStatus("mandatory")
_VrPpSrBpProvTable_Object = MibTable
vrPpSrBpProvTable = _VrPpSrBpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10)
)
if mibBuilder.loadTexts:
    vrPpSrBpProvTable.setStatus("mandatory")
_VrPpSrBpProvEntry_Object = MibTableRow
vrPpSrBpProvEntry = _VrPpSrBpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1)
)
vrPpSrBpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpProvEntry.setStatus("mandatory")


class _VrPpSrBpTranslateIpx_Type(Integer32):
    """Custom type vrPpSrBpTranslateIpx based on Integer32"""
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


_VrPpSrBpTranslateIpx_Type.__name__ = "Integer32"
_VrPpSrBpTranslateIpx_Object = MibTableColumn
vrPpSrBpTranslateIpx = _VrPpSrBpTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1, 1),
    _VrPpSrBpTranslateIpx_Type()
)
vrPpSrBpTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpTranslateIpx.setStatus("mandatory")


class _VrPpSrBpFragmentIp_Type(Integer32):
    """Custom type vrPpSrBpFragmentIp based on Integer32"""
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


_VrPpSrBpFragmentIp_Type.__name__ = "Integer32"
_VrPpSrBpFragmentIp_Object = MibTableColumn
vrPpSrBpFragmentIp = _VrPpSrBpFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1, 2),
    _VrPpSrBpFragmentIp_Type()
)
vrPpSrBpFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpFragmentIp.setStatus("mandatory")


class _VrPpSrBpServiceClass_Type(Integer32):
    """Custom type vrPpSrBpServiceClass based on Integer32"""
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


_VrPpSrBpServiceClass_Type.__name__ = "Integer32"
_VrPpSrBpServiceClass_Object = MibTableColumn
vrPpSrBpServiceClass = _VrPpSrBpServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1, 3),
    _VrPpSrBpServiceClass_Type()
)
vrPpSrBpServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpServiceClass.setStatus("mandatory")


class _VrPpSrBpConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpSrBpConvertArpMacAddress based on Integer32"""
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


_VrPpSrBpConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpSrBpConvertArpMacAddress_Object = MibTableColumn
vrPpSrBpConvertArpMacAddress = _VrPpSrBpConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1, 4),
    _VrPpSrBpConvertArpMacAddress_Type()
)
vrPpSrBpConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpConvertArpMacAddress.setStatus("mandatory")


class _VrPpSrBpPortNum_Type(Unsigned32):
    """Custom type vrPpSrBpPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpSrBpPortNum_Type.__name__ = "Unsigned32"
_VrPpSrBpPortNum_Object = MibTableColumn
vrPpSrBpPortNum = _VrPpSrBpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1, 5),
    _VrPpSrBpPortNum_Type()
)
vrPpSrBpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpPortNum.setStatus("mandatory")


class _VrPpSrBpOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpSrBpOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpSrBpOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpSrBpOutboundFrameMediaType_Object = MibTableColumn
vrPpSrBpOutboundFrameMediaType = _VrPpSrBpOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 10, 1, 6),
    _VrPpSrBpOutboundFrameMediaType_Type()
)
vrPpSrBpOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpOutboundFrameMediaType.setStatus("mandatory")
_VrPpSrBpStpProvTable_Object = MibTable
vrPpSrBpStpProvTable = _VrPpSrBpStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12)
)
if mibBuilder.loadTexts:
    vrPpSrBpStpProvTable.setStatus("mandatory")
_VrPpSrBpStpProvEntry_Object = MibTableRow
vrPpSrBpStpProvEntry = _VrPpSrBpStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1)
)
vrPpSrBpStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpStpProvEntry.setStatus("mandatory")


class _VrPpSrBpAdminStatus_Type(Integer32):
    """Custom type vrPpSrBpAdminStatus based on Integer32"""
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


_VrPpSrBpAdminStatus_Type.__name__ = "Integer32"
_VrPpSrBpAdminStatus_Object = MibTableColumn
vrPpSrBpAdminStatus = _VrPpSrBpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1, 1),
    _VrPpSrBpAdminStatus_Type()
)
vrPpSrBpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpAdminStatus.setStatus("mandatory")


class _VrPpSrBpPortStateStpControl_Type(Integer32):
    """Custom type vrPpSrBpPortStateStpControl based on Integer32"""
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


_VrPpSrBpPortStateStpControl_Type.__name__ = "Integer32"
_VrPpSrBpPortStateStpControl_Object = MibTableColumn
vrPpSrBpPortStateStpControl = _VrPpSrBpPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1, 2),
    _VrPpSrBpPortStateStpControl_Type()
)
vrPpSrBpPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpPortStateStpControl.setStatus("mandatory")


class _VrPpSrBpStpTypeProv_Type(Integer32):
    """Custom type vrPpSrBpStpTypeProv based on Integer32"""
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


_VrPpSrBpStpTypeProv_Type.__name__ = "Integer32"
_VrPpSrBpStpTypeProv_Object = MibTableColumn
vrPpSrBpStpTypeProv = _VrPpSrBpStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1, 3),
    _VrPpSrBpStpTypeProv_Type()
)
vrPpSrBpStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpStpTypeProv.setStatus("mandatory")


class _VrPpSrBpPortPriority_Type(Unsigned32):
    """Custom type vrPpSrBpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrBpPortPriority_Type.__name__ = "Unsigned32"
_VrPpSrBpPortPriority_Object = MibTableColumn
vrPpSrBpPortPriority = _VrPpSrBpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1, 4),
    _VrPpSrBpPortPriority_Type()
)
vrPpSrBpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpPortPriority.setStatus("mandatory")


class _VrPpSrBpPathCost_Type(Unsigned32):
    """Custom type vrPpSrBpPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrBpPathCost_Type.__name__ = "Unsigned32"
_VrPpSrBpPathCost_Object = MibTableColumn
vrPpSrBpPathCost = _VrPpSrBpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1, 5),
    _VrPpSrBpPathCost_Type()
)
vrPpSrBpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpPathCost.setStatus("mandatory")


class _VrPpSrBpPathCostMethod_Type(Integer32):
    """Custom type vrPpSrBpPathCostMethod based on Integer32"""
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


_VrPpSrBpPathCostMethod_Type.__name__ = "Integer32"
_VrPpSrBpPathCostMethod_Object = MibTableColumn
vrPpSrBpPathCostMethod = _VrPpSrBpPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 12, 1, 6),
    _VrPpSrBpPathCostMethod_Type()
)
vrPpSrBpPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpPathCostMethod.setStatus("mandatory")
_VrPpSrBpDIProvTable_Object = MibTable
vrPpSrBpDIProvTable = _VrPpSrBpDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 13)
)
if mibBuilder.loadTexts:
    vrPpSrBpDIProvTable.setStatus("mandatory")
_VrPpSrBpDIProvEntry_Object = MibTableRow
vrPpSrBpDIProvEntry = _VrPpSrBpDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 13, 1)
)
vrPpSrBpDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpDIProvEntry.setStatus("mandatory")


class _VrPpSrBpDomainNum_Type(Unsigned32):
    """Custom type vrPpSrBpDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpSrBpDomainNum_Type.__name__ = "Unsigned32"
_VrPpSrBpDomainNum_Object = MibTableColumn
vrPpSrBpDomainNum = _VrPpSrBpDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 13, 1, 1),
    _VrPpSrBpDomainNum_Type()
)
vrPpSrBpDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpDomainNum.setStatus("mandatory")


class _VrPpSrBpPreserveDomain_Type(Integer32):
    """Custom type vrPpSrBpPreserveDomain based on Integer32"""
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


_VrPpSrBpPreserveDomain_Type.__name__ = "Integer32"
_VrPpSrBpPreserveDomain_Object = MibTableColumn
vrPpSrBpPreserveDomain = _VrPpSrBpPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 13, 1, 2),
    _VrPpSrBpPreserveDomain_Type()
)
vrPpSrBpPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpPreserveDomain.setStatus("mandatory")
_VrPpSrBpStateTable_Object = MibTable
vrPpSrBpStateTable = _VrPpSrBpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 14)
)
if mibBuilder.loadTexts:
    vrPpSrBpStateTable.setStatus("mandatory")
_VrPpSrBpStateEntry_Object = MibTableRow
vrPpSrBpStateEntry = _VrPpSrBpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 14, 1)
)
vrPpSrBpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpStateEntry.setStatus("mandatory")


class _VrPpSrBpAdminState_Type(Integer32):
    """Custom type vrPpSrBpAdminState based on Integer32"""
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


_VrPpSrBpAdminState_Type.__name__ = "Integer32"
_VrPpSrBpAdminState_Object = MibTableColumn
vrPpSrBpAdminState = _VrPpSrBpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 14, 1, 1),
    _VrPpSrBpAdminState_Type()
)
vrPpSrBpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpAdminState.setStatus("mandatory")


class _VrPpSrBpOperationalState_Type(Integer32):
    """Custom type vrPpSrBpOperationalState based on Integer32"""
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


_VrPpSrBpOperationalState_Type.__name__ = "Integer32"
_VrPpSrBpOperationalState_Object = MibTableColumn
vrPpSrBpOperationalState = _VrPpSrBpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 14, 1, 2),
    _VrPpSrBpOperationalState_Type()
)
vrPpSrBpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpOperationalState.setStatus("mandatory")


class _VrPpSrBpUsageState_Type(Integer32):
    """Custom type vrPpSrBpUsageState based on Integer32"""
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


_VrPpSrBpUsageState_Type.__name__ = "Integer32"
_VrPpSrBpUsageState_Object = MibTableColumn
vrPpSrBpUsageState = _VrPpSrBpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 14, 1, 3),
    _VrPpSrBpUsageState_Type()
)
vrPpSrBpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpUsageState.setStatus("mandatory")
_VrPpSrBpOperStatusTable_Object = MibTable
vrPpSrBpOperStatusTable = _VrPpSrBpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 15)
)
if mibBuilder.loadTexts:
    vrPpSrBpOperStatusTable.setStatus("mandatory")
_VrPpSrBpOperStatusEntry_Object = MibTableRow
vrPpSrBpOperStatusEntry = _VrPpSrBpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 15, 1)
)
vrPpSrBpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpOperStatusEntry.setStatus("mandatory")


class _VrPpSrBpSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSrBpSnmpOperStatus based on Integer32"""
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


_VrPpSrBpSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSrBpSnmpOperStatus_Object = MibTableColumn
vrPpSrBpSnmpOperStatus = _VrPpSrBpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 15, 1, 1),
    _VrPpSrBpSnmpOperStatus_Type()
)
vrPpSrBpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpSnmpOperStatus.setStatus("mandatory")
_VrPpSrBpOperTable_Object = MibTable
vrPpSrBpOperTable = _VrPpSrBpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16)
)
if mibBuilder.loadTexts:
    vrPpSrBpOperTable.setStatus("mandatory")
_VrPpSrBpOperEntry_Object = MibTableRow
vrPpSrBpOperEntry = _VrPpSrBpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1)
)
vrPpSrBpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpOperEntry.setStatus("mandatory")


class _VrPpSrBpPortName_Type(AsciiString):
    """Custom type vrPpSrBpPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpSrBpPortName_Type.__name__ = "AsciiString"
_VrPpSrBpPortName_Object = MibTableColumn
vrPpSrBpPortName = _VrPpSrBpPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 1),
    _VrPpSrBpPortName_Type()
)
vrPpSrBpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpPortName.setStatus("mandatory")


class _VrPpSrBpUpTime_Type(Unsigned32):
    """Custom type vrPpSrBpUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrBpUpTime_Type.__name__ = "Unsigned32"
_VrPpSrBpUpTime_Object = MibTableColumn
vrPpSrBpUpTime = _VrPpSrBpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 3),
    _VrPpSrBpUpTime_Type()
)
vrPpSrBpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpUpTime.setStatus("mandatory")


class _VrPpSrBpDownTime_Type(Unsigned32):
    """Custom type vrPpSrBpDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrBpDownTime_Type.__name__ = "Unsigned32"
_VrPpSrBpDownTime_Object = MibTableColumn
vrPpSrBpDownTime = _VrPpSrBpDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 4),
    _VrPpSrBpDownTime_Type()
)
vrPpSrBpDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDownTime.setStatus("mandatory")


class _VrPpSrBpBridgingMode_Type(Integer32):
    """Custom type vrPpSrBpBridgingMode based on Integer32"""
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


_VrPpSrBpBridgingMode_Type.__name__ = "Integer32"
_VrPpSrBpBridgingMode_Object = MibTableColumn
vrPpSrBpBridgingMode = _VrPpSrBpBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 5),
    _VrPpSrBpBridgingMode_Type()
)
vrPpSrBpBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpBridgingMode.setStatus("mandatory")


class _VrPpSrBpBridgePortConfig_Type(Integer32):
    """Custom type vrPpSrBpBridgePortConfig based on Integer32"""
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


_VrPpSrBpBridgePortConfig_Type.__name__ = "Integer32"
_VrPpSrBpBridgePortConfig_Object = MibTableColumn
vrPpSrBpBridgePortConfig = _VrPpSrBpBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 6),
    _VrPpSrBpBridgePortConfig_Type()
)
vrPpSrBpBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpBridgePortConfig.setStatus("mandatory")


class _VrPpSrBpBridgePortType_Type(Integer32):
    """Custom type vrPpSrBpBridgePortType based on Integer32"""
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


_VrPpSrBpBridgePortType_Type.__name__ = "Integer32"
_VrPpSrBpBridgePortType_Object = MibTableColumn
vrPpSrBpBridgePortType = _VrPpSrBpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 7),
    _VrPpSrBpBridgePortType_Type()
)
vrPpSrBpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpBridgePortType.setStatus("mandatory")


class _VrPpSrBpIfIndex_Type(InterfaceIndex):
    """Custom type vrPpSrBpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrBpIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpSrBpIfIndex_Object = MibTableColumn
vrPpSrBpIfIndex = _VrPpSrBpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 8),
    _VrPpSrBpIfIndex_Type()
)
vrPpSrBpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpIfIndex.setStatus("mandatory")
_VrPpSrBpDelayExceededDiscards_Type = Counter32
_VrPpSrBpDelayExceededDiscards_Object = MibTableColumn
vrPpSrBpDelayExceededDiscards = _VrPpSrBpDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 10),
    _VrPpSrBpDelayExceededDiscards_Type()
)
vrPpSrBpDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDelayExceededDiscards.setStatus("mandatory")
_VrPpSrBpMtuExceededDiscards_Type = Counter32
_VrPpSrBpMtuExceededDiscards_Object = MibTableColumn
vrPpSrBpMtuExceededDiscards = _VrPpSrBpMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 16, 1, 11),
    _VrPpSrBpMtuExceededDiscards_Type()
)
vrPpSrBpMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpMtuExceededDiscards.setStatus("mandatory")
_VrPpSrBpStpOperTable_Object = MibTable
vrPpSrBpStpOperTable = _VrPpSrBpStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18)
)
if mibBuilder.loadTexts:
    vrPpSrBpStpOperTable.setStatus("mandatory")
_VrPpSrBpStpOperEntry_Object = MibTableRow
vrPpSrBpStpOperEntry = _VrPpSrBpStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1)
)
vrPpSrBpStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpStpOperEntry.setStatus("mandatory")


class _VrPpSrBpStpPortState_Type(Integer32):
    """Custom type vrPpSrBpStpPortState based on Integer32"""
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


_VrPpSrBpStpPortState_Type.__name__ = "Integer32"
_VrPpSrBpStpPortState_Object = MibTableColumn
vrPpSrBpStpPortState = _VrPpSrBpStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 2),
    _VrPpSrBpStpPortState_Type()
)
vrPpSrBpStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpStpPortState.setStatus("mandatory")


class _VrPpSrBpStpTypeOper_Type(Integer32):
    """Custom type vrPpSrBpStpTypeOper based on Integer32"""
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


_VrPpSrBpStpTypeOper_Type.__name__ = "Integer32"
_VrPpSrBpStpTypeOper_Object = MibTableColumn
vrPpSrBpStpTypeOper = _VrPpSrBpStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 3),
    _VrPpSrBpStpTypeOper_Type()
)
vrPpSrBpStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpStpTypeOper.setStatus("mandatory")


class _VrPpSrBpDesignatedCost_Type(Unsigned32):
    """Custom type vrPpSrBpDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrBpDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpSrBpDesignatedCost_Object = MibTableColumn
vrPpSrBpDesignatedCost = _VrPpSrBpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 4),
    _VrPpSrBpDesignatedCost_Type()
)
vrPpSrBpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDesignatedCost.setStatus("mandatory")


class _VrPpSrBpPathCostOper_Type(Unsigned32):
    """Custom type vrPpSrBpPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrBpPathCostOper_Type.__name__ = "Unsigned32"
_VrPpSrBpPathCostOper_Object = MibTableColumn
vrPpSrBpPathCostOper = _VrPpSrBpPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 5),
    _VrPpSrBpPathCostOper_Type()
)
vrPpSrBpPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpPathCostOper.setStatus("mandatory")


class _VrPpSrBpDesignatedBridge_Type(BridgeId):
    """Custom type vrPpSrBpDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrBpDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpSrBpDesignatedBridge_Object = MibTableColumn
vrPpSrBpDesignatedBridge = _VrPpSrBpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 6),
    _VrPpSrBpDesignatedBridge_Type()
)
vrPpSrBpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDesignatedBridge.setStatus("mandatory")


class _VrPpSrBpDesignatedPort_Type(Hex):
    """Custom type vrPpSrBpDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrBpDesignatedPort_Type.__name__ = "Hex"
_VrPpSrBpDesignatedPort_Object = MibTableColumn
vrPpSrBpDesignatedPort = _VrPpSrBpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 7),
    _VrPpSrBpDesignatedPort_Type()
)
vrPpSrBpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDesignatedPort.setStatus("mandatory")
_VrPpSrBpForwardTransitions_Type = Counter32
_VrPpSrBpForwardTransitions_Object = MibTableColumn
vrPpSrBpForwardTransitions = _VrPpSrBpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 8),
    _VrPpSrBpForwardTransitions_Type()
)
vrPpSrBpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpForwardTransitions.setStatus("mandatory")
_VrPpSrBpBlockingDiscards_Type = Counter32
_VrPpSrBpBlockingDiscards_Object = MibTableColumn
vrPpSrBpBlockingDiscards = _VrPpSrBpBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 9),
    _VrPpSrBpBlockingDiscards_Type()
)
vrPpSrBpBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpBlockingDiscards.setStatus("mandatory")


class _VrPpSrBpDesignatedRoot_Type(BridgeId):
    """Custom type vrPpSrBpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrBpDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpSrBpDesignatedRoot_Object = MibTableColumn
vrPpSrBpDesignatedRoot = _VrPpSrBpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 18, 1, 10),
    _VrPpSrBpDesignatedRoot_Type()
)
vrPpSrBpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDesignatedRoot.setStatus("mandatory")
_VrPpSrBpStatsTable_Object = MibTable
vrPpSrBpStatsTable = _VrPpSrBpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19)
)
if mibBuilder.loadTexts:
    vrPpSrBpStatsTable.setStatus("mandatory")
_VrPpSrBpStatsEntry_Object = MibTableRow
vrPpSrBpStatsEntry = _VrPpSrBpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19, 1)
)
vrPpSrBpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpStatsEntry.setStatus("mandatory")
_VrPpSrBpBadAbstractDiscards_Type = Counter32
_VrPpSrBpBadAbstractDiscards_Object = MibTableColumn
vrPpSrBpBadAbstractDiscards = _VrPpSrBpBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19, 1, 1),
    _VrPpSrBpBadAbstractDiscards_Type()
)
vrPpSrBpBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpBadAbstractDiscards.setStatus("mandatory")
_VrPpSrBpTinygramFramesIn_Type = Counter32
_VrPpSrBpTinygramFramesIn_Object = MibTableColumn
vrPpSrBpTinygramFramesIn = _VrPpSrBpTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19, 1, 2),
    _VrPpSrBpTinygramFramesIn_Type()
)
vrPpSrBpTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpTinygramFramesIn.setStatus("mandatory")
_VrPpSrBpTinygramFramesOut_Type = Counter32
_VrPpSrBpTinygramFramesOut_Object = MibTableColumn
vrPpSrBpTinygramFramesOut = _VrPpSrBpTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19, 1, 3),
    _VrPpSrBpTinygramFramesOut_Type()
)
vrPpSrBpTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpTinygramFramesOut.setStatus("mandatory")
_VrPpSrBpInFilterDiscards_Type = Counter32
_VrPpSrBpInFilterDiscards_Object = MibTableColumn
vrPpSrBpInFilterDiscards = _VrPpSrBpInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19, 1, 4),
    _VrPpSrBpInFilterDiscards_Type()
)
vrPpSrBpInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpInFilterDiscards.setStatus("mandatory")
_VrPpSrBpOutFilterDiscards_Type = Counter32
_VrPpSrBpOutFilterDiscards_Object = MibTableColumn
vrPpSrBpOutFilterDiscards = _VrPpSrBpOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 19, 1, 5),
    _VrPpSrBpOutFilterDiscards_Type()
)
vrPpSrBpOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpOutFilterDiscards.setStatus("mandatory")
_VrPpSrBpSrProvTable_Object = MibTable
vrPpSrBpSrProvTable = _VrPpSrBpSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20)
)
if mibBuilder.loadTexts:
    vrPpSrBpSrProvTable.setStatus("mandatory")
_VrPpSrBpSrProvEntry_Object = MibTableRow
vrPpSrBpSrProvEntry = _VrPpSrBpSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1)
)
vrPpSrBpSrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpSrProvEntry.setStatus("mandatory")


class _VrPpSrBpHopCount_Type(Unsigned32):
    """Custom type vrPpSrBpHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrPpSrBpHopCount_Type.__name__ = "Unsigned32"
_VrPpSrBpHopCount_Object = MibTableColumn
vrPpSrBpHopCount = _VrPpSrBpHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 1),
    _VrPpSrBpHopCount_Type()
)
vrPpSrBpHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpHopCount.setStatus("mandatory")


class _VrPpSrBpExploreFrameTreatment_Type(Integer32):
    """Custom type vrPpSrBpExploreFrameTreatment based on Integer32"""
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


_VrPpSrBpExploreFrameTreatment_Type.__name__ = "Integer32"
_VrPpSrBpExploreFrameTreatment_Object = MibTableColumn
vrPpSrBpExploreFrameTreatment = _VrPpSrBpExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 2),
    _VrPpSrBpExploreFrameTreatment_Type()
)
vrPpSrBpExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpExploreFrameTreatment.setStatus("mandatory")


class _VrPpSrBpLanId_Type(Unsigned32):
    """Custom type vrPpSrBpLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrBpLanId_Type.__name__ = "Unsigned32"
_VrPpSrBpLanId_Object = MibTableColumn
vrPpSrBpLanId = _VrPpSrBpLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 3),
    _VrPpSrBpLanId_Type()
)
vrPpSrBpLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpLanId.setStatus("mandatory")


class _VrPpSrBpInternalLanId_Type(Unsigned32):
    """Custom type vrPpSrBpInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrBpInternalLanId_Type.__name__ = "Unsigned32"
_VrPpSrBpInternalLanId_Object = MibTableColumn
vrPpSrBpInternalLanId = _VrPpSrBpInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 4),
    _VrPpSrBpInternalLanId_Type()
)
vrPpSrBpInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpInternalLanId.setStatus("mandatory")


class _VrPpSrBpBridgeNum_Type(Unsigned32):
    """Custom type vrPpSrBpBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrPpSrBpBridgeNum_Type.__name__ = "Unsigned32"
_VrPpSrBpBridgeNum_Object = MibTableColumn
vrPpSrBpBridgeNum = _VrPpSrBpBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 5),
    _VrPpSrBpBridgeNum_Type()
)
vrPpSrBpBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpBridgeNum.setStatus("mandatory")


class _VrPpSrBpLargestFrame_Type(Unsigned32):
    """Custom type vrPpSrBpLargestFrame based on Unsigned32"""
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


_VrPpSrBpLargestFrame_Type.__name__ = "Unsigned32"
_VrPpSrBpLargestFrame_Object = MibTableColumn
vrPpSrBpLargestFrame = _VrPpSrBpLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 6),
    _VrPpSrBpLargestFrame_Type()
)
vrPpSrBpLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpLargestFrame.setStatus("mandatory")


class _VrPpSrBpSteSpanMode_Type(Integer32):
    """Custom type vrPpSrBpSteSpanMode based on Integer32"""
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


_VrPpSrBpSteSpanMode_Type.__name__ = "Integer32"
_VrPpSrBpSteSpanMode_Object = MibTableColumn
vrPpSrBpSteSpanMode = _VrPpSrBpSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 7),
    _VrPpSrBpSteSpanMode_Type()
)
vrPpSrBpSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpSteSpanMode.setStatus("mandatory")


class _VrPpSrBpAreRdLimit_Type(Unsigned32):
    """Custom type vrPpSrBpAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrBpAreRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrBpAreRdLimit_Object = MibTableColumn
vrPpSrBpAreRdLimit = _VrPpSrBpAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 8),
    _VrPpSrBpAreRdLimit_Type()
)
vrPpSrBpAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpAreRdLimit.setStatus("mandatory")


class _VrPpSrBpSteRdLimit_Type(Unsigned32):
    """Custom type vrPpSrBpSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrBpSteRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrBpSteRdLimit_Object = MibTableColumn
vrPpSrBpSteRdLimit = _VrPpSrBpSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 20, 1, 9),
    _VrPpSrBpSteRdLimit_Type()
)
vrPpSrBpSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrBpSteRdLimit.setStatus("mandatory")
_VrPpSrBpSrStatsTable_Object = MibTable
vrPpSrBpSrStatsTable = _VrPpSrBpSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21)
)
if mibBuilder.loadTexts:
    vrPpSrBpSrStatsTable.setStatus("mandatory")
_VrPpSrBpSrStatsEntry_Object = MibTableRow
vrPpSrBpSrStatsEntry = _VrPpSrBpSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1)
)
vrPpSrBpSrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrBpSrStatsEntry.setStatus("mandatory")
_VrPpSrBpSpecInFrames_Type = Counter32
_VrPpSrBpSpecInFrames_Object = MibTableColumn
vrPpSrBpSpecInFrames = _VrPpSrBpSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 1),
    _VrPpSrBpSpecInFrames_Type()
)
vrPpSrBpSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpSpecInFrames.setStatus("mandatory")
_VrPpSrBpSpecOutFrames_Type = Counter32
_VrPpSrBpSpecOutFrames_Object = MibTableColumn
vrPpSrBpSpecOutFrames = _VrPpSrBpSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 2),
    _VrPpSrBpSpecOutFrames_Type()
)
vrPpSrBpSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpSpecOutFrames.setStatus("mandatory")
_VrPpSrBpApeInFrames_Type = Counter32
_VrPpSrBpApeInFrames_Object = MibTableColumn
vrPpSrBpApeInFrames = _VrPpSrBpApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 3),
    _VrPpSrBpApeInFrames_Type()
)
vrPpSrBpApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpApeInFrames.setStatus("mandatory")
_VrPpSrBpApeOutFrames_Type = Counter32
_VrPpSrBpApeOutFrames_Object = MibTableColumn
vrPpSrBpApeOutFrames = _VrPpSrBpApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 4),
    _VrPpSrBpApeOutFrames_Type()
)
vrPpSrBpApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpApeOutFrames.setStatus("mandatory")
_VrPpSrBpSteInFrames_Type = Counter32
_VrPpSrBpSteInFrames_Object = MibTableColumn
vrPpSrBpSteInFrames = _VrPpSrBpSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 5),
    _VrPpSrBpSteInFrames_Type()
)
vrPpSrBpSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpSteInFrames.setStatus("mandatory")
_VrPpSrBpSteOutFrames_Type = Counter32
_VrPpSrBpSteOutFrames_Object = MibTableColumn
vrPpSrBpSteOutFrames = _VrPpSrBpSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 6),
    _VrPpSrBpSteOutFrames_Type()
)
vrPpSrBpSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpSteOutFrames.setStatus("mandatory")
_VrPpSrBpSegmentMismatchDiscards_Type = Counter32
_VrPpSrBpSegmentMismatchDiscards_Object = MibTableColumn
vrPpSrBpSegmentMismatchDiscards = _VrPpSrBpSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 7),
    _VrPpSrBpSegmentMismatchDiscards_Type()
)
vrPpSrBpSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpSegmentMismatchDiscards.setStatus("mandatory")
_VrPpSrBpDupSegmentDiscards_Type = Counter32
_VrPpSrBpDupSegmentDiscards_Object = MibTableColumn
vrPpSrBpDupSegmentDiscards = _VrPpSrBpDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 8),
    _VrPpSrBpDupSegmentDiscards_Type()
)
vrPpSrBpDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDupSegmentDiscards.setStatus("mandatory")
_VrPpSrBpHopCountExceededDiscards_Type = Counter32
_VrPpSrBpHopCountExceededDiscards_Object = MibTableColumn
vrPpSrBpHopCountExceededDiscards = _VrPpSrBpHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 9),
    _VrPpSrBpHopCountExceededDiscards_Type()
)
vrPpSrBpHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpHopCountExceededDiscards.setStatus("mandatory")
_VrPpSrBpDupLanIdOrTreeErrors_Type = Counter32
_VrPpSrBpDupLanIdOrTreeErrors_Object = MibTableColumn
vrPpSrBpDupLanIdOrTreeErrors = _VrPpSrBpDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 10),
    _VrPpSrBpDupLanIdOrTreeErrors_Type()
)
vrPpSrBpDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDupLanIdOrTreeErrors.setStatus("mandatory")
_VrPpSrBpLanIdMismatches_Type = Counter32
_VrPpSrBpLanIdMismatches_Object = MibTableColumn
vrPpSrBpLanIdMismatches = _VrPpSrBpLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 11),
    _VrPpSrBpLanIdMismatches_Type()
)
vrPpSrBpLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpLanIdMismatches.setStatus("mandatory")
_VrPpSrBpStaticDiscards_Type = Counter32
_VrPpSrBpStaticDiscards_Object = MibTableColumn
vrPpSrBpStaticDiscards = _VrPpSrBpStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 12),
    _VrPpSrBpStaticDiscards_Type()
)
vrPpSrBpStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpStaticDiscards.setStatus("mandatory")
_VrPpSrBpDynamicDiscards_Type = Counter32
_VrPpSrBpDynamicDiscards_Object = MibTableColumn
vrPpSrBpDynamicDiscards = _VrPpSrBpDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 8, 21, 1, 13),
    _VrPpSrBpDynamicDiscards_Type()
)
vrPpSrBpDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrBpDynamicDiscards.setStatus("mandatory")
_VrPpSrtBp_ObjectIdentity = ObjectIdentity
vrPpSrtBp = _VrPpSrtBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9)
)
_VrPpSrtBpRowStatusTable_Object = MibTable
vrPpSrtBpRowStatusTable = _VrPpSrtBpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 1)
)
if mibBuilder.loadTexts:
    vrPpSrtBpRowStatusTable.setStatus("mandatory")
_VrPpSrtBpRowStatusEntry_Object = MibTableRow
vrPpSrtBpRowStatusEntry = _VrPpSrtBpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 1, 1)
)
vrPpSrtBpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpRowStatusEntry.setStatus("mandatory")
_VrPpSrtBpRowStatus_Type = RowStatus
_VrPpSrtBpRowStatus_Object = MibTableColumn
vrPpSrtBpRowStatus = _VrPpSrtBpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 1, 1, 1),
    _VrPpSrtBpRowStatus_Type()
)
vrPpSrtBpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpRowStatus.setStatus("mandatory")
_VrPpSrtBpComponentName_Type = DisplayString
_VrPpSrtBpComponentName_Object = MibTableColumn
vrPpSrtBpComponentName = _VrPpSrtBpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 1, 1, 2),
    _VrPpSrtBpComponentName_Type()
)
vrPpSrtBpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpComponentName.setStatus("mandatory")
_VrPpSrtBpStorageType_Type = StorageType
_VrPpSrtBpStorageType_Object = MibTableColumn
vrPpSrtBpStorageType = _VrPpSrtBpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 1, 1, 4),
    _VrPpSrtBpStorageType_Type()
)
vrPpSrtBpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpStorageType.setStatus("mandatory")
_VrPpSrtBpIndex_Type = NonReplicated
_VrPpSrtBpIndex_Object = MibTableColumn
vrPpSrtBpIndex = _VrPpSrtBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 1, 1, 10),
    _VrPpSrtBpIndex_Type()
)
vrPpSrtBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrtBpIndex.setStatus("mandatory")
_VrPpSrtBpNs_ObjectIdentity = ObjectIdentity
vrPpSrtBpNs = _VrPpSrtBpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2)
)
_VrPpSrtBpNsRowStatusTable_Object = MibTable
vrPpSrtBpNsRowStatusTable = _VrPpSrtBpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpSrtBpNsRowStatusTable.setStatus("mandatory")
_VrPpSrtBpNsRowStatusEntry_Object = MibTableRow
vrPpSrtBpNsRowStatusEntry = _VrPpSrtBpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 1, 1)
)
vrPpSrtBpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpNsRowStatusEntry.setStatus("mandatory")
_VrPpSrtBpNsRowStatus_Type = RowStatus
_VrPpSrtBpNsRowStatus_Object = MibTableColumn
vrPpSrtBpNsRowStatus = _VrPpSrtBpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 1, 1, 1),
    _VrPpSrtBpNsRowStatus_Type()
)
vrPpSrtBpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpNsRowStatus.setStatus("mandatory")
_VrPpSrtBpNsComponentName_Type = DisplayString
_VrPpSrtBpNsComponentName_Object = MibTableColumn
vrPpSrtBpNsComponentName = _VrPpSrtBpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 1, 1, 2),
    _VrPpSrtBpNsComponentName_Type()
)
vrPpSrtBpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpNsComponentName.setStatus("mandatory")
_VrPpSrtBpNsStorageType_Type = StorageType
_VrPpSrtBpNsStorageType_Object = MibTableColumn
vrPpSrtBpNsStorageType = _VrPpSrtBpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 1, 1, 4),
    _VrPpSrtBpNsStorageType_Type()
)
vrPpSrtBpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpNsStorageType.setStatus("mandatory")
_VrPpSrtBpNsIndex_Type = NonReplicated
_VrPpSrtBpNsIndex_Object = MibTableColumn
vrPpSrtBpNsIndex = _VrPpSrtBpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 1, 1, 10),
    _VrPpSrtBpNsIndex_Type()
)
vrPpSrtBpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrtBpNsIndex.setStatus("mandatory")
_VrPpSrtBpNsProvTable_Object = MibTable
vrPpSrtBpNsProvTable = _VrPpSrtBpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpSrtBpNsProvTable.setStatus("mandatory")
_VrPpSrtBpNsProvEntry_Object = MibTableRow
vrPpSrtBpNsProvEntry = _VrPpSrtBpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 10, 1)
)
vrPpSrtBpNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpNsProvEntry.setStatus("mandatory")


class _VrPpSrtBpNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpSrtBpNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpSrtBpNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpSrtBpNsIncomingFilter_Object = MibTableColumn
vrPpSrtBpNsIncomingFilter = _VrPpSrtBpNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 10, 1, 2),
    _VrPpSrtBpNsIncomingFilter_Type()
)
vrPpSrtBpNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpNsIncomingFilter.setStatus("mandatory")


class _VrPpSrtBpNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpSrtBpNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpSrtBpNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpSrtBpNsOutgoingFilter_Object = MibTableColumn
vrPpSrtBpNsOutgoingFilter = _VrPpSrtBpNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 2, 10, 1, 3),
    _VrPpSrtBpNsOutgoingFilter_Type()
)
vrPpSrtBpNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpNsOutgoingFilter.setStatus("mandatory")
_VrPpSrtBpProvTable_Object = MibTable
vrPpSrtBpProvTable = _VrPpSrtBpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10)
)
if mibBuilder.loadTexts:
    vrPpSrtBpProvTable.setStatus("mandatory")
_VrPpSrtBpProvEntry_Object = MibTableRow
vrPpSrtBpProvEntry = _VrPpSrtBpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1)
)
vrPpSrtBpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpProvEntry.setStatus("mandatory")


class _VrPpSrtBpTranslateIpx_Type(Integer32):
    """Custom type vrPpSrtBpTranslateIpx based on Integer32"""
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


_VrPpSrtBpTranslateIpx_Type.__name__ = "Integer32"
_VrPpSrtBpTranslateIpx_Object = MibTableColumn
vrPpSrtBpTranslateIpx = _VrPpSrtBpTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1, 1),
    _VrPpSrtBpTranslateIpx_Type()
)
vrPpSrtBpTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpTranslateIpx.setStatus("mandatory")


class _VrPpSrtBpFragmentIp_Type(Integer32):
    """Custom type vrPpSrtBpFragmentIp based on Integer32"""
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


_VrPpSrtBpFragmentIp_Type.__name__ = "Integer32"
_VrPpSrtBpFragmentIp_Object = MibTableColumn
vrPpSrtBpFragmentIp = _VrPpSrtBpFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1, 2),
    _VrPpSrtBpFragmentIp_Type()
)
vrPpSrtBpFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpFragmentIp.setStatus("mandatory")


class _VrPpSrtBpServiceClass_Type(Integer32):
    """Custom type vrPpSrtBpServiceClass based on Integer32"""
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


_VrPpSrtBpServiceClass_Type.__name__ = "Integer32"
_VrPpSrtBpServiceClass_Object = MibTableColumn
vrPpSrtBpServiceClass = _VrPpSrtBpServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1, 3),
    _VrPpSrtBpServiceClass_Type()
)
vrPpSrtBpServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpServiceClass.setStatus("mandatory")


class _VrPpSrtBpConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpSrtBpConvertArpMacAddress based on Integer32"""
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


_VrPpSrtBpConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpSrtBpConvertArpMacAddress_Object = MibTableColumn
vrPpSrtBpConvertArpMacAddress = _VrPpSrtBpConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1, 4),
    _VrPpSrtBpConvertArpMacAddress_Type()
)
vrPpSrtBpConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpConvertArpMacAddress.setStatus("mandatory")


class _VrPpSrtBpPortNum_Type(Unsigned32):
    """Custom type vrPpSrtBpPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpSrtBpPortNum_Type.__name__ = "Unsigned32"
_VrPpSrtBpPortNum_Object = MibTableColumn
vrPpSrtBpPortNum = _VrPpSrtBpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1, 5),
    _VrPpSrtBpPortNum_Type()
)
vrPpSrtBpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpPortNum.setStatus("mandatory")


class _VrPpSrtBpOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpSrtBpOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpSrtBpOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpSrtBpOutboundFrameMediaType_Object = MibTableColumn
vrPpSrtBpOutboundFrameMediaType = _VrPpSrtBpOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 10, 1, 6),
    _VrPpSrtBpOutboundFrameMediaType_Type()
)
vrPpSrtBpOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpOutboundFrameMediaType.setStatus("mandatory")
_VrPpSrtBpTbProvTable_Object = MibTable
vrPpSrtBpTbProvTable = _VrPpSrtBpTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 11)
)
if mibBuilder.loadTexts:
    vrPpSrtBpTbProvTable.setStatus("mandatory")
_VrPpSrtBpTbProvEntry_Object = MibTableRow
vrPpSrtBpTbProvEntry = _VrPpSrtBpTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 11, 1)
)
vrPpSrtBpTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpTbProvEntry.setStatus("mandatory")


class _VrPpSrtBpSecureOption_Type(Integer32):
    """Custom type vrPpSrtBpSecureOption based on Integer32"""
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


_VrPpSrtBpSecureOption_Type.__name__ = "Integer32"
_VrPpSrtBpSecureOption_Object = MibTableColumn
vrPpSrtBpSecureOption = _VrPpSrtBpSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 11, 1, 1),
    _VrPpSrtBpSecureOption_Type()
)
vrPpSrtBpSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpSecureOption.setStatus("mandatory")
_VrPpSrtBpStpProvTable_Object = MibTable
vrPpSrtBpStpProvTable = _VrPpSrtBpStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12)
)
if mibBuilder.loadTexts:
    vrPpSrtBpStpProvTable.setStatus("mandatory")
_VrPpSrtBpStpProvEntry_Object = MibTableRow
vrPpSrtBpStpProvEntry = _VrPpSrtBpStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1)
)
vrPpSrtBpStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpStpProvEntry.setStatus("mandatory")


class _VrPpSrtBpAdminStatus_Type(Integer32):
    """Custom type vrPpSrtBpAdminStatus based on Integer32"""
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


_VrPpSrtBpAdminStatus_Type.__name__ = "Integer32"
_VrPpSrtBpAdminStatus_Object = MibTableColumn
vrPpSrtBpAdminStatus = _VrPpSrtBpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1, 1),
    _VrPpSrtBpAdminStatus_Type()
)
vrPpSrtBpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpAdminStatus.setStatus("mandatory")


class _VrPpSrtBpPortStateStpControl_Type(Integer32):
    """Custom type vrPpSrtBpPortStateStpControl based on Integer32"""
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


_VrPpSrtBpPortStateStpControl_Type.__name__ = "Integer32"
_VrPpSrtBpPortStateStpControl_Object = MibTableColumn
vrPpSrtBpPortStateStpControl = _VrPpSrtBpPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1, 2),
    _VrPpSrtBpPortStateStpControl_Type()
)
vrPpSrtBpPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpPortStateStpControl.setStatus("mandatory")


class _VrPpSrtBpStpTypeProv_Type(Integer32):
    """Custom type vrPpSrtBpStpTypeProv based on Integer32"""
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


_VrPpSrtBpStpTypeProv_Type.__name__ = "Integer32"
_VrPpSrtBpStpTypeProv_Object = MibTableColumn
vrPpSrtBpStpTypeProv = _VrPpSrtBpStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1, 3),
    _VrPpSrtBpStpTypeProv_Type()
)
vrPpSrtBpStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpStpTypeProv.setStatus("mandatory")


class _VrPpSrtBpPortPriority_Type(Unsigned32):
    """Custom type vrPpSrtBpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrtBpPortPriority_Type.__name__ = "Unsigned32"
_VrPpSrtBpPortPriority_Object = MibTableColumn
vrPpSrtBpPortPriority = _VrPpSrtBpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1, 4),
    _VrPpSrtBpPortPriority_Type()
)
vrPpSrtBpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpPortPriority.setStatus("mandatory")


class _VrPpSrtBpPathCost_Type(Unsigned32):
    """Custom type vrPpSrtBpPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrtBpPathCost_Type.__name__ = "Unsigned32"
_VrPpSrtBpPathCost_Object = MibTableColumn
vrPpSrtBpPathCost = _VrPpSrtBpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1, 5),
    _VrPpSrtBpPathCost_Type()
)
vrPpSrtBpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpPathCost.setStatus("mandatory")


class _VrPpSrtBpPathCostMethod_Type(Integer32):
    """Custom type vrPpSrtBpPathCostMethod based on Integer32"""
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


_VrPpSrtBpPathCostMethod_Type.__name__ = "Integer32"
_VrPpSrtBpPathCostMethod_Object = MibTableColumn
vrPpSrtBpPathCostMethod = _VrPpSrtBpPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 12, 1, 6),
    _VrPpSrtBpPathCostMethod_Type()
)
vrPpSrtBpPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpPathCostMethod.setStatus("mandatory")
_VrPpSrtBpDIProvTable_Object = MibTable
vrPpSrtBpDIProvTable = _VrPpSrtBpDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 13)
)
if mibBuilder.loadTexts:
    vrPpSrtBpDIProvTable.setStatus("mandatory")
_VrPpSrtBpDIProvEntry_Object = MibTableRow
vrPpSrtBpDIProvEntry = _VrPpSrtBpDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 13, 1)
)
vrPpSrtBpDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpDIProvEntry.setStatus("mandatory")


class _VrPpSrtBpDomainNum_Type(Unsigned32):
    """Custom type vrPpSrtBpDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpSrtBpDomainNum_Type.__name__ = "Unsigned32"
_VrPpSrtBpDomainNum_Object = MibTableColumn
vrPpSrtBpDomainNum = _VrPpSrtBpDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 13, 1, 1),
    _VrPpSrtBpDomainNum_Type()
)
vrPpSrtBpDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpDomainNum.setStatus("mandatory")


class _VrPpSrtBpPreserveDomain_Type(Integer32):
    """Custom type vrPpSrtBpPreserveDomain based on Integer32"""
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


_VrPpSrtBpPreserveDomain_Type.__name__ = "Integer32"
_VrPpSrtBpPreserveDomain_Object = MibTableColumn
vrPpSrtBpPreserveDomain = _VrPpSrtBpPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 13, 1, 2),
    _VrPpSrtBpPreserveDomain_Type()
)
vrPpSrtBpPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpPreserveDomain.setStatus("mandatory")
_VrPpSrtBpStateTable_Object = MibTable
vrPpSrtBpStateTable = _VrPpSrtBpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 14)
)
if mibBuilder.loadTexts:
    vrPpSrtBpStateTable.setStatus("mandatory")
_VrPpSrtBpStateEntry_Object = MibTableRow
vrPpSrtBpStateEntry = _VrPpSrtBpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 14, 1)
)
vrPpSrtBpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpStateEntry.setStatus("mandatory")


class _VrPpSrtBpAdminState_Type(Integer32):
    """Custom type vrPpSrtBpAdminState based on Integer32"""
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


_VrPpSrtBpAdminState_Type.__name__ = "Integer32"
_VrPpSrtBpAdminState_Object = MibTableColumn
vrPpSrtBpAdminState = _VrPpSrtBpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 14, 1, 1),
    _VrPpSrtBpAdminState_Type()
)
vrPpSrtBpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpAdminState.setStatus("mandatory")


class _VrPpSrtBpOperationalState_Type(Integer32):
    """Custom type vrPpSrtBpOperationalState based on Integer32"""
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


_VrPpSrtBpOperationalState_Type.__name__ = "Integer32"
_VrPpSrtBpOperationalState_Object = MibTableColumn
vrPpSrtBpOperationalState = _VrPpSrtBpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 14, 1, 2),
    _VrPpSrtBpOperationalState_Type()
)
vrPpSrtBpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpOperationalState.setStatus("mandatory")


class _VrPpSrtBpUsageState_Type(Integer32):
    """Custom type vrPpSrtBpUsageState based on Integer32"""
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


_VrPpSrtBpUsageState_Type.__name__ = "Integer32"
_VrPpSrtBpUsageState_Object = MibTableColumn
vrPpSrtBpUsageState = _VrPpSrtBpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 14, 1, 3),
    _VrPpSrtBpUsageState_Type()
)
vrPpSrtBpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpUsageState.setStatus("mandatory")
_VrPpSrtBpOperStatusTable_Object = MibTable
vrPpSrtBpOperStatusTable = _VrPpSrtBpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 15)
)
if mibBuilder.loadTexts:
    vrPpSrtBpOperStatusTable.setStatus("mandatory")
_VrPpSrtBpOperStatusEntry_Object = MibTableRow
vrPpSrtBpOperStatusEntry = _VrPpSrtBpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 15, 1)
)
vrPpSrtBpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpOperStatusEntry.setStatus("mandatory")


class _VrPpSrtBpSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSrtBpSnmpOperStatus based on Integer32"""
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


_VrPpSrtBpSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSrtBpSnmpOperStatus_Object = MibTableColumn
vrPpSrtBpSnmpOperStatus = _VrPpSrtBpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 15, 1, 1),
    _VrPpSrtBpSnmpOperStatus_Type()
)
vrPpSrtBpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpSnmpOperStatus.setStatus("mandatory")
_VrPpSrtBpOperTable_Object = MibTable
vrPpSrtBpOperTable = _VrPpSrtBpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16)
)
if mibBuilder.loadTexts:
    vrPpSrtBpOperTable.setStatus("mandatory")
_VrPpSrtBpOperEntry_Object = MibTableRow
vrPpSrtBpOperEntry = _VrPpSrtBpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1)
)
vrPpSrtBpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpOperEntry.setStatus("mandatory")


class _VrPpSrtBpPortName_Type(AsciiString):
    """Custom type vrPpSrtBpPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpSrtBpPortName_Type.__name__ = "AsciiString"
_VrPpSrtBpPortName_Object = MibTableColumn
vrPpSrtBpPortName = _VrPpSrtBpPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 1),
    _VrPpSrtBpPortName_Type()
)
vrPpSrtBpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpPortName.setStatus("mandatory")


class _VrPpSrtBpUpTime_Type(Unsigned32):
    """Custom type vrPpSrtBpUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrtBpUpTime_Type.__name__ = "Unsigned32"
_VrPpSrtBpUpTime_Object = MibTableColumn
vrPpSrtBpUpTime = _VrPpSrtBpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 3),
    _VrPpSrtBpUpTime_Type()
)
vrPpSrtBpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpUpTime.setStatus("mandatory")


class _VrPpSrtBpDownTime_Type(Unsigned32):
    """Custom type vrPpSrtBpDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrtBpDownTime_Type.__name__ = "Unsigned32"
_VrPpSrtBpDownTime_Object = MibTableColumn
vrPpSrtBpDownTime = _VrPpSrtBpDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 4),
    _VrPpSrtBpDownTime_Type()
)
vrPpSrtBpDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDownTime.setStatus("mandatory")


class _VrPpSrtBpBridgingMode_Type(Integer32):
    """Custom type vrPpSrtBpBridgingMode based on Integer32"""
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


_VrPpSrtBpBridgingMode_Type.__name__ = "Integer32"
_VrPpSrtBpBridgingMode_Object = MibTableColumn
vrPpSrtBpBridgingMode = _VrPpSrtBpBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 5),
    _VrPpSrtBpBridgingMode_Type()
)
vrPpSrtBpBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpBridgingMode.setStatus("mandatory")


class _VrPpSrtBpBridgePortConfig_Type(Integer32):
    """Custom type vrPpSrtBpBridgePortConfig based on Integer32"""
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


_VrPpSrtBpBridgePortConfig_Type.__name__ = "Integer32"
_VrPpSrtBpBridgePortConfig_Object = MibTableColumn
vrPpSrtBpBridgePortConfig = _VrPpSrtBpBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 6),
    _VrPpSrtBpBridgePortConfig_Type()
)
vrPpSrtBpBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpBridgePortConfig.setStatus("mandatory")


class _VrPpSrtBpBridgePortType_Type(Integer32):
    """Custom type vrPpSrtBpBridgePortType based on Integer32"""
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


_VrPpSrtBpBridgePortType_Type.__name__ = "Integer32"
_VrPpSrtBpBridgePortType_Object = MibTableColumn
vrPpSrtBpBridgePortType = _VrPpSrtBpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 7),
    _VrPpSrtBpBridgePortType_Type()
)
vrPpSrtBpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpBridgePortType.setStatus("mandatory")


class _VrPpSrtBpIfIndex_Type(InterfaceIndex):
    """Custom type vrPpSrtBpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrtBpIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpSrtBpIfIndex_Object = MibTableColumn
vrPpSrtBpIfIndex = _VrPpSrtBpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 8),
    _VrPpSrtBpIfIndex_Type()
)
vrPpSrtBpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpIfIndex.setStatus("mandatory")
_VrPpSrtBpDelayExceededDiscards_Type = Counter32
_VrPpSrtBpDelayExceededDiscards_Object = MibTableColumn
vrPpSrtBpDelayExceededDiscards = _VrPpSrtBpDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 10),
    _VrPpSrtBpDelayExceededDiscards_Type()
)
vrPpSrtBpDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDelayExceededDiscards.setStatus("mandatory")
_VrPpSrtBpMtuExceededDiscards_Type = Counter32
_VrPpSrtBpMtuExceededDiscards_Object = MibTableColumn
vrPpSrtBpMtuExceededDiscards = _VrPpSrtBpMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 16, 1, 11),
    _VrPpSrtBpMtuExceededDiscards_Type()
)
vrPpSrtBpMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpMtuExceededDiscards.setStatus("mandatory")
_VrPpSrtBpTbOperTable_Object = MibTable
vrPpSrtBpTbOperTable = _VrPpSrtBpTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17)
)
if mibBuilder.loadTexts:
    vrPpSrtBpTbOperTable.setStatus("mandatory")
_VrPpSrtBpTbOperEntry_Object = MibTableRow
vrPpSrtBpTbOperEntry = _VrPpSrtBpTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1)
)
vrPpSrtBpTbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpTbOperEntry.setStatus("mandatory")


class _VrPpSrtBpMaxInfo_Type(Unsigned32):
    """Custom type vrPpSrtBpMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrtBpMaxInfo_Type.__name__ = "Unsigned32"
_VrPpSrtBpMaxInfo_Object = MibTableColumn
vrPpSrtBpMaxInfo = _VrPpSrtBpMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 2),
    _VrPpSrtBpMaxInfo_Type()
)
vrPpSrtBpMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpMaxInfo.setStatus("mandatory")
_VrPpSrtBpBadVerifyDiscards_Type = Counter32
_VrPpSrtBpBadVerifyDiscards_Object = MibTableColumn
vrPpSrtBpBadVerifyDiscards = _VrPpSrtBpBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 3),
    _VrPpSrtBpBadVerifyDiscards_Type()
)
vrPpSrtBpBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpBadVerifyDiscards.setStatus("mandatory")
_VrPpSrtBpUnicastNoMatches_Type = Counter32
_VrPpSrtBpUnicastNoMatches_Object = MibTableColumn
vrPpSrtBpUnicastNoMatches = _VrPpSrtBpUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 4),
    _VrPpSrtBpUnicastNoMatches_Type()
)
vrPpSrtBpUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpUnicastNoMatches.setStatus("mandatory")
_VrPpSrtBpStaticEntryDiscards_Type = Counter32
_VrPpSrtBpStaticEntryDiscards_Object = MibTableColumn
vrPpSrtBpStaticEntryDiscards = _VrPpSrtBpStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 5),
    _VrPpSrtBpStaticEntryDiscards_Type()
)
vrPpSrtBpStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpStaticEntryDiscards.setStatus("mandatory")
_VrPpSrtBpDynamicEntryDiscards_Type = Counter32
_VrPpSrtBpDynamicEntryDiscards_Object = MibTableColumn
vrPpSrtBpDynamicEntryDiscards = _VrPpSrtBpDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 6),
    _VrPpSrtBpDynamicEntryDiscards_Type()
)
vrPpSrtBpDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDynamicEntryDiscards.setStatus("mandatory")
_VrPpSrtBpLearningDiscards_Type = Counter32
_VrPpSrtBpLearningDiscards_Object = MibTableColumn
vrPpSrtBpLearningDiscards = _VrPpSrtBpLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 7),
    _VrPpSrtBpLearningDiscards_Type()
)
vrPpSrtBpLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpLearningDiscards.setStatus("mandatory")
_VrPpSrtBpInDiscards_Type = Counter32
_VrPpSrtBpInDiscards_Object = MibTableColumn
vrPpSrtBpInDiscards = _VrPpSrtBpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 8),
    _VrPpSrtBpInDiscards_Type()
)
vrPpSrtBpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpInDiscards.setStatus("mandatory")
_VrPpSrtBpInFrames_Type = Counter32
_VrPpSrtBpInFrames_Object = MibTableColumn
vrPpSrtBpInFrames = _VrPpSrtBpInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 9),
    _VrPpSrtBpInFrames_Type()
)
vrPpSrtBpInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpInFrames.setStatus("mandatory")
_VrPpSrtBpOutFrames_Type = Counter32
_VrPpSrtBpOutFrames_Object = MibTableColumn
vrPpSrtBpOutFrames = _VrPpSrtBpOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 17, 1, 10),
    _VrPpSrtBpOutFrames_Type()
)
vrPpSrtBpOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpOutFrames.setStatus("mandatory")
_VrPpSrtBpStpOperTable_Object = MibTable
vrPpSrtBpStpOperTable = _VrPpSrtBpStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18)
)
if mibBuilder.loadTexts:
    vrPpSrtBpStpOperTable.setStatus("mandatory")
_VrPpSrtBpStpOperEntry_Object = MibTableRow
vrPpSrtBpStpOperEntry = _VrPpSrtBpStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1)
)
vrPpSrtBpStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpStpOperEntry.setStatus("mandatory")


class _VrPpSrtBpStpPortState_Type(Integer32):
    """Custom type vrPpSrtBpStpPortState based on Integer32"""
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


_VrPpSrtBpStpPortState_Type.__name__ = "Integer32"
_VrPpSrtBpStpPortState_Object = MibTableColumn
vrPpSrtBpStpPortState = _VrPpSrtBpStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 2),
    _VrPpSrtBpStpPortState_Type()
)
vrPpSrtBpStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpStpPortState.setStatus("mandatory")


class _VrPpSrtBpStpTypeOper_Type(Integer32):
    """Custom type vrPpSrtBpStpTypeOper based on Integer32"""
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


_VrPpSrtBpStpTypeOper_Type.__name__ = "Integer32"
_VrPpSrtBpStpTypeOper_Object = MibTableColumn
vrPpSrtBpStpTypeOper = _VrPpSrtBpStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 3),
    _VrPpSrtBpStpTypeOper_Type()
)
vrPpSrtBpStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpStpTypeOper.setStatus("mandatory")


class _VrPpSrtBpDesignatedCost_Type(Unsigned32):
    """Custom type vrPpSrtBpDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrtBpDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpSrtBpDesignatedCost_Object = MibTableColumn
vrPpSrtBpDesignatedCost = _VrPpSrtBpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 4),
    _VrPpSrtBpDesignatedCost_Type()
)
vrPpSrtBpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDesignatedCost.setStatus("mandatory")


class _VrPpSrtBpPathCostOper_Type(Unsigned32):
    """Custom type vrPpSrtBpPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrtBpPathCostOper_Type.__name__ = "Unsigned32"
_VrPpSrtBpPathCostOper_Object = MibTableColumn
vrPpSrtBpPathCostOper = _VrPpSrtBpPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 5),
    _VrPpSrtBpPathCostOper_Type()
)
vrPpSrtBpPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpPathCostOper.setStatus("mandatory")


class _VrPpSrtBpDesignatedBridge_Type(BridgeId):
    """Custom type vrPpSrtBpDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrtBpDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpSrtBpDesignatedBridge_Object = MibTableColumn
vrPpSrtBpDesignatedBridge = _VrPpSrtBpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 6),
    _VrPpSrtBpDesignatedBridge_Type()
)
vrPpSrtBpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDesignatedBridge.setStatus("mandatory")


class _VrPpSrtBpDesignatedPort_Type(Hex):
    """Custom type vrPpSrtBpDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrtBpDesignatedPort_Type.__name__ = "Hex"
_VrPpSrtBpDesignatedPort_Object = MibTableColumn
vrPpSrtBpDesignatedPort = _VrPpSrtBpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 7),
    _VrPpSrtBpDesignatedPort_Type()
)
vrPpSrtBpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDesignatedPort.setStatus("mandatory")
_VrPpSrtBpForwardTransitions_Type = Counter32
_VrPpSrtBpForwardTransitions_Object = MibTableColumn
vrPpSrtBpForwardTransitions = _VrPpSrtBpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 8),
    _VrPpSrtBpForwardTransitions_Type()
)
vrPpSrtBpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpForwardTransitions.setStatus("mandatory")
_VrPpSrtBpBlockingDiscards_Type = Counter32
_VrPpSrtBpBlockingDiscards_Object = MibTableColumn
vrPpSrtBpBlockingDiscards = _VrPpSrtBpBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 9),
    _VrPpSrtBpBlockingDiscards_Type()
)
vrPpSrtBpBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpBlockingDiscards.setStatus("mandatory")


class _VrPpSrtBpDesignatedRoot_Type(BridgeId):
    """Custom type vrPpSrtBpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrtBpDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpSrtBpDesignatedRoot_Object = MibTableColumn
vrPpSrtBpDesignatedRoot = _VrPpSrtBpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 18, 1, 10),
    _VrPpSrtBpDesignatedRoot_Type()
)
vrPpSrtBpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDesignatedRoot.setStatus("mandatory")
_VrPpSrtBpStatsTable_Object = MibTable
vrPpSrtBpStatsTable = _VrPpSrtBpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19)
)
if mibBuilder.loadTexts:
    vrPpSrtBpStatsTable.setStatus("mandatory")
_VrPpSrtBpStatsEntry_Object = MibTableRow
vrPpSrtBpStatsEntry = _VrPpSrtBpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19, 1)
)
vrPpSrtBpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpStatsEntry.setStatus("mandatory")
_VrPpSrtBpBadAbstractDiscards_Type = Counter32
_VrPpSrtBpBadAbstractDiscards_Object = MibTableColumn
vrPpSrtBpBadAbstractDiscards = _VrPpSrtBpBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19, 1, 1),
    _VrPpSrtBpBadAbstractDiscards_Type()
)
vrPpSrtBpBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpBadAbstractDiscards.setStatus("mandatory")
_VrPpSrtBpTinygramFramesIn_Type = Counter32
_VrPpSrtBpTinygramFramesIn_Object = MibTableColumn
vrPpSrtBpTinygramFramesIn = _VrPpSrtBpTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19, 1, 2),
    _VrPpSrtBpTinygramFramesIn_Type()
)
vrPpSrtBpTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpTinygramFramesIn.setStatus("mandatory")
_VrPpSrtBpTinygramFramesOut_Type = Counter32
_VrPpSrtBpTinygramFramesOut_Object = MibTableColumn
vrPpSrtBpTinygramFramesOut = _VrPpSrtBpTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19, 1, 3),
    _VrPpSrtBpTinygramFramesOut_Type()
)
vrPpSrtBpTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpTinygramFramesOut.setStatus("mandatory")
_VrPpSrtBpInFilterDiscards_Type = Counter32
_VrPpSrtBpInFilterDiscards_Object = MibTableColumn
vrPpSrtBpInFilterDiscards = _VrPpSrtBpInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19, 1, 4),
    _VrPpSrtBpInFilterDiscards_Type()
)
vrPpSrtBpInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpInFilterDiscards.setStatus("mandatory")
_VrPpSrtBpOutFilterDiscards_Type = Counter32
_VrPpSrtBpOutFilterDiscards_Object = MibTableColumn
vrPpSrtBpOutFilterDiscards = _VrPpSrtBpOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 19, 1, 5),
    _VrPpSrtBpOutFilterDiscards_Type()
)
vrPpSrtBpOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpOutFilterDiscards.setStatus("mandatory")
_VrPpSrtBpSrProvTable_Object = MibTable
vrPpSrtBpSrProvTable = _VrPpSrtBpSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20)
)
if mibBuilder.loadTexts:
    vrPpSrtBpSrProvTable.setStatus("mandatory")
_VrPpSrtBpSrProvEntry_Object = MibTableRow
vrPpSrtBpSrProvEntry = _VrPpSrtBpSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1)
)
vrPpSrtBpSrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpSrProvEntry.setStatus("mandatory")


class _VrPpSrtBpHopCount_Type(Unsigned32):
    """Custom type vrPpSrtBpHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrPpSrtBpHopCount_Type.__name__ = "Unsigned32"
_VrPpSrtBpHopCount_Object = MibTableColumn
vrPpSrtBpHopCount = _VrPpSrtBpHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 1),
    _VrPpSrtBpHopCount_Type()
)
vrPpSrtBpHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpHopCount.setStatus("mandatory")


class _VrPpSrtBpExploreFrameTreatment_Type(Integer32):
    """Custom type vrPpSrtBpExploreFrameTreatment based on Integer32"""
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


_VrPpSrtBpExploreFrameTreatment_Type.__name__ = "Integer32"
_VrPpSrtBpExploreFrameTreatment_Object = MibTableColumn
vrPpSrtBpExploreFrameTreatment = _VrPpSrtBpExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 2),
    _VrPpSrtBpExploreFrameTreatment_Type()
)
vrPpSrtBpExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpExploreFrameTreatment.setStatus("mandatory")


class _VrPpSrtBpLanId_Type(Unsigned32):
    """Custom type vrPpSrtBpLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrtBpLanId_Type.__name__ = "Unsigned32"
_VrPpSrtBpLanId_Object = MibTableColumn
vrPpSrtBpLanId = _VrPpSrtBpLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 3),
    _VrPpSrtBpLanId_Type()
)
vrPpSrtBpLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpLanId.setStatus("mandatory")


class _VrPpSrtBpInternalLanId_Type(Unsigned32):
    """Custom type vrPpSrtBpInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrtBpInternalLanId_Type.__name__ = "Unsigned32"
_VrPpSrtBpInternalLanId_Object = MibTableColumn
vrPpSrtBpInternalLanId = _VrPpSrtBpInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 4),
    _VrPpSrtBpInternalLanId_Type()
)
vrPpSrtBpInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpInternalLanId.setStatus("mandatory")


class _VrPpSrtBpBridgeNum_Type(Unsigned32):
    """Custom type vrPpSrtBpBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrPpSrtBpBridgeNum_Type.__name__ = "Unsigned32"
_VrPpSrtBpBridgeNum_Object = MibTableColumn
vrPpSrtBpBridgeNum = _VrPpSrtBpBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 5),
    _VrPpSrtBpBridgeNum_Type()
)
vrPpSrtBpBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpBridgeNum.setStatus("mandatory")


class _VrPpSrtBpLargestFrame_Type(Unsigned32):
    """Custom type vrPpSrtBpLargestFrame based on Unsigned32"""
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


_VrPpSrtBpLargestFrame_Type.__name__ = "Unsigned32"
_VrPpSrtBpLargestFrame_Object = MibTableColumn
vrPpSrtBpLargestFrame = _VrPpSrtBpLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 6),
    _VrPpSrtBpLargestFrame_Type()
)
vrPpSrtBpLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpLargestFrame.setStatus("mandatory")


class _VrPpSrtBpSteSpanMode_Type(Integer32):
    """Custom type vrPpSrtBpSteSpanMode based on Integer32"""
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


_VrPpSrtBpSteSpanMode_Type.__name__ = "Integer32"
_VrPpSrtBpSteSpanMode_Object = MibTableColumn
vrPpSrtBpSteSpanMode = _VrPpSrtBpSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 7),
    _VrPpSrtBpSteSpanMode_Type()
)
vrPpSrtBpSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpSteSpanMode.setStatus("mandatory")


class _VrPpSrtBpAreRdLimit_Type(Unsigned32):
    """Custom type vrPpSrtBpAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrtBpAreRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrtBpAreRdLimit_Object = MibTableColumn
vrPpSrtBpAreRdLimit = _VrPpSrtBpAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 8),
    _VrPpSrtBpAreRdLimit_Type()
)
vrPpSrtBpAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpAreRdLimit.setStatus("mandatory")


class _VrPpSrtBpSteRdLimit_Type(Unsigned32):
    """Custom type vrPpSrtBpSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrtBpSteRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrtBpSteRdLimit_Object = MibTableColumn
vrPpSrtBpSteRdLimit = _VrPpSrtBpSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 20, 1, 9),
    _VrPpSrtBpSteRdLimit_Type()
)
vrPpSrtBpSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrtBpSteRdLimit.setStatus("mandatory")
_VrPpSrtBpSrStatsTable_Object = MibTable
vrPpSrtBpSrStatsTable = _VrPpSrtBpSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21)
)
if mibBuilder.loadTexts:
    vrPpSrtBpSrStatsTable.setStatus("mandatory")
_VrPpSrtBpSrStatsEntry_Object = MibTableRow
vrPpSrtBpSrStatsEntry = _VrPpSrtBpSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1)
)
vrPpSrtBpSrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrtBpIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrtBpSrStatsEntry.setStatus("mandatory")
_VrPpSrtBpSpecInFrames_Type = Counter32
_VrPpSrtBpSpecInFrames_Object = MibTableColumn
vrPpSrtBpSpecInFrames = _VrPpSrtBpSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 1),
    _VrPpSrtBpSpecInFrames_Type()
)
vrPpSrtBpSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpSpecInFrames.setStatus("mandatory")
_VrPpSrtBpSpecOutFrames_Type = Counter32
_VrPpSrtBpSpecOutFrames_Object = MibTableColumn
vrPpSrtBpSpecOutFrames = _VrPpSrtBpSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 2),
    _VrPpSrtBpSpecOutFrames_Type()
)
vrPpSrtBpSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpSpecOutFrames.setStatus("mandatory")
_VrPpSrtBpApeInFrames_Type = Counter32
_VrPpSrtBpApeInFrames_Object = MibTableColumn
vrPpSrtBpApeInFrames = _VrPpSrtBpApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 3),
    _VrPpSrtBpApeInFrames_Type()
)
vrPpSrtBpApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpApeInFrames.setStatus("mandatory")
_VrPpSrtBpApeOutFrames_Type = Counter32
_VrPpSrtBpApeOutFrames_Object = MibTableColumn
vrPpSrtBpApeOutFrames = _VrPpSrtBpApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 4),
    _VrPpSrtBpApeOutFrames_Type()
)
vrPpSrtBpApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpApeOutFrames.setStatus("mandatory")
_VrPpSrtBpSteInFrames_Type = Counter32
_VrPpSrtBpSteInFrames_Object = MibTableColumn
vrPpSrtBpSteInFrames = _VrPpSrtBpSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 5),
    _VrPpSrtBpSteInFrames_Type()
)
vrPpSrtBpSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpSteInFrames.setStatus("mandatory")
_VrPpSrtBpSteOutFrames_Type = Counter32
_VrPpSrtBpSteOutFrames_Object = MibTableColumn
vrPpSrtBpSteOutFrames = _VrPpSrtBpSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 6),
    _VrPpSrtBpSteOutFrames_Type()
)
vrPpSrtBpSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpSteOutFrames.setStatus("mandatory")
_VrPpSrtBpSegmentMismatchDiscards_Type = Counter32
_VrPpSrtBpSegmentMismatchDiscards_Object = MibTableColumn
vrPpSrtBpSegmentMismatchDiscards = _VrPpSrtBpSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 7),
    _VrPpSrtBpSegmentMismatchDiscards_Type()
)
vrPpSrtBpSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpSegmentMismatchDiscards.setStatus("mandatory")
_VrPpSrtBpDupSegmentDiscards_Type = Counter32
_VrPpSrtBpDupSegmentDiscards_Object = MibTableColumn
vrPpSrtBpDupSegmentDiscards = _VrPpSrtBpDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 8),
    _VrPpSrtBpDupSegmentDiscards_Type()
)
vrPpSrtBpDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDupSegmentDiscards.setStatus("mandatory")
_VrPpSrtBpHopCountExceededDiscards_Type = Counter32
_VrPpSrtBpHopCountExceededDiscards_Object = MibTableColumn
vrPpSrtBpHopCountExceededDiscards = _VrPpSrtBpHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 9),
    _VrPpSrtBpHopCountExceededDiscards_Type()
)
vrPpSrtBpHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpHopCountExceededDiscards.setStatus("mandatory")
_VrPpSrtBpDupLanIdOrTreeErrors_Type = Counter32
_VrPpSrtBpDupLanIdOrTreeErrors_Object = MibTableColumn
vrPpSrtBpDupLanIdOrTreeErrors = _VrPpSrtBpDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 10),
    _VrPpSrtBpDupLanIdOrTreeErrors_Type()
)
vrPpSrtBpDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDupLanIdOrTreeErrors.setStatus("mandatory")
_VrPpSrtBpLanIdMismatches_Type = Counter32
_VrPpSrtBpLanIdMismatches_Object = MibTableColumn
vrPpSrtBpLanIdMismatches = _VrPpSrtBpLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 11),
    _VrPpSrtBpLanIdMismatches_Type()
)
vrPpSrtBpLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpLanIdMismatches.setStatus("mandatory")
_VrPpSrtBpStaticDiscards_Type = Counter32
_VrPpSrtBpStaticDiscards_Object = MibTableColumn
vrPpSrtBpStaticDiscards = _VrPpSrtBpStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 12),
    _VrPpSrtBpStaticDiscards_Type()
)
vrPpSrtBpStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpStaticDiscards.setStatus("mandatory")
_VrPpSrtBpDynamicDiscards_Type = Counter32
_VrPpSrtBpDynamicDiscards_Object = MibTableColumn
vrPpSrtBpDynamicDiscards = _VrPpSrtBpDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 9, 21, 1, 13),
    _VrPpSrtBpDynamicDiscards_Type()
)
vrPpSrtBpDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrtBpDynamicDiscards.setStatus("mandatory")
_VrPpSrse_ObjectIdentity = ObjectIdentity
vrPpSrse = _VrPpSrse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10)
)
_VrPpSrseRowStatusTable_Object = MibTable
vrPpSrseRowStatusTable = _VrPpSrseRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 1)
)
if mibBuilder.loadTexts:
    vrPpSrseRowStatusTable.setStatus("mandatory")
_VrPpSrseRowStatusEntry_Object = MibTableRow
vrPpSrseRowStatusEntry = _VrPpSrseRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 1, 1)
)
vrPpSrseRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseRowStatusEntry.setStatus("mandatory")
_VrPpSrseRowStatus_Type = RowStatus
_VrPpSrseRowStatus_Object = MibTableColumn
vrPpSrseRowStatus = _VrPpSrseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 1, 1, 1),
    _VrPpSrseRowStatus_Type()
)
vrPpSrseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseRowStatus.setStatus("mandatory")
_VrPpSrseComponentName_Type = DisplayString
_VrPpSrseComponentName_Object = MibTableColumn
vrPpSrseComponentName = _VrPpSrseComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 1, 1, 2),
    _VrPpSrseComponentName_Type()
)
vrPpSrseComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseComponentName.setStatus("mandatory")
_VrPpSrseStorageType_Type = StorageType
_VrPpSrseStorageType_Object = MibTableColumn
vrPpSrseStorageType = _VrPpSrseStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 1, 1, 4),
    _VrPpSrseStorageType_Type()
)
vrPpSrseStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseStorageType.setStatus("mandatory")
_VrPpSrseIndex_Type = NonReplicated
_VrPpSrseIndex_Object = MibTableColumn
vrPpSrseIndex = _VrPpSrseIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 1, 1, 10),
    _VrPpSrseIndex_Type()
)
vrPpSrseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrseIndex.setStatus("mandatory")
_VrPpSrseProvTable_Object = MibTable
vrPpSrseProvTable = _VrPpSrseProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10)
)
if mibBuilder.loadTexts:
    vrPpSrseProvTable.setStatus("mandatory")
_VrPpSrseProvEntry_Object = MibTableRow
vrPpSrseProvEntry = _VrPpSrseProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1)
)
vrPpSrseProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseProvEntry.setStatus("mandatory")


class _VrPpSrseTranslateIpx_Type(Integer32):
    """Custom type vrPpSrseTranslateIpx based on Integer32"""
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


_VrPpSrseTranslateIpx_Type.__name__ = "Integer32"
_VrPpSrseTranslateIpx_Object = MibTableColumn
vrPpSrseTranslateIpx = _VrPpSrseTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1, 1),
    _VrPpSrseTranslateIpx_Type()
)
vrPpSrseTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseTranslateIpx.setStatus("mandatory")


class _VrPpSrseFragmentIp_Type(Integer32):
    """Custom type vrPpSrseFragmentIp based on Integer32"""
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


_VrPpSrseFragmentIp_Type.__name__ = "Integer32"
_VrPpSrseFragmentIp_Object = MibTableColumn
vrPpSrseFragmentIp = _VrPpSrseFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1, 2),
    _VrPpSrseFragmentIp_Type()
)
vrPpSrseFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseFragmentIp.setStatus("mandatory")


class _VrPpSrseServiceClass_Type(Integer32):
    """Custom type vrPpSrseServiceClass based on Integer32"""
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


_VrPpSrseServiceClass_Type.__name__ = "Integer32"
_VrPpSrseServiceClass_Object = MibTableColumn
vrPpSrseServiceClass = _VrPpSrseServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1, 3),
    _VrPpSrseServiceClass_Type()
)
vrPpSrseServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseServiceClass.setStatus("mandatory")


class _VrPpSrseConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpSrseConvertArpMacAddress based on Integer32"""
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


_VrPpSrseConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpSrseConvertArpMacAddress_Object = MibTableColumn
vrPpSrseConvertArpMacAddress = _VrPpSrseConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1, 4),
    _VrPpSrseConvertArpMacAddress_Type()
)
vrPpSrseConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseConvertArpMacAddress.setStatus("mandatory")


class _VrPpSrsePortNum_Type(Unsigned32):
    """Custom type vrPpSrsePortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpSrsePortNum_Type.__name__ = "Unsigned32"
_VrPpSrsePortNum_Object = MibTableColumn
vrPpSrsePortNum = _VrPpSrsePortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1, 5),
    _VrPpSrsePortNum_Type()
)
vrPpSrsePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsePortNum.setStatus("mandatory")


class _VrPpSrseOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpSrseOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpSrseOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpSrseOutboundFrameMediaType_Object = MibTableColumn
vrPpSrseOutboundFrameMediaType = _VrPpSrseOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 10, 1, 6),
    _VrPpSrseOutboundFrameMediaType_Type()
)
vrPpSrseOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseOutboundFrameMediaType.setStatus("mandatory")
_VrPpSrseStpProvTable_Object = MibTable
vrPpSrseStpProvTable = _VrPpSrseStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12)
)
if mibBuilder.loadTexts:
    vrPpSrseStpProvTable.setStatus("mandatory")
_VrPpSrseStpProvEntry_Object = MibTableRow
vrPpSrseStpProvEntry = _VrPpSrseStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1)
)
vrPpSrseStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseStpProvEntry.setStatus("mandatory")


class _VrPpSrseAdminStatus_Type(Integer32):
    """Custom type vrPpSrseAdminStatus based on Integer32"""
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


_VrPpSrseAdminStatus_Type.__name__ = "Integer32"
_VrPpSrseAdminStatus_Object = MibTableColumn
vrPpSrseAdminStatus = _VrPpSrseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1, 1),
    _VrPpSrseAdminStatus_Type()
)
vrPpSrseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseAdminStatus.setStatus("mandatory")


class _VrPpSrsePortStateStpControl_Type(Integer32):
    """Custom type vrPpSrsePortStateStpControl based on Integer32"""
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


_VrPpSrsePortStateStpControl_Type.__name__ = "Integer32"
_VrPpSrsePortStateStpControl_Object = MibTableColumn
vrPpSrsePortStateStpControl = _VrPpSrsePortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1, 2),
    _VrPpSrsePortStateStpControl_Type()
)
vrPpSrsePortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsePortStateStpControl.setStatus("mandatory")


class _VrPpSrseStpTypeProv_Type(Integer32):
    """Custom type vrPpSrseStpTypeProv based on Integer32"""
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


_VrPpSrseStpTypeProv_Type.__name__ = "Integer32"
_VrPpSrseStpTypeProv_Object = MibTableColumn
vrPpSrseStpTypeProv = _VrPpSrseStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1, 3),
    _VrPpSrseStpTypeProv_Type()
)
vrPpSrseStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseStpTypeProv.setStatus("mandatory")


class _VrPpSrsePortPriority_Type(Unsigned32):
    """Custom type vrPpSrsePortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrsePortPriority_Type.__name__ = "Unsigned32"
_VrPpSrsePortPriority_Object = MibTableColumn
vrPpSrsePortPriority = _VrPpSrsePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1, 4),
    _VrPpSrsePortPriority_Type()
)
vrPpSrsePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsePortPriority.setStatus("mandatory")


class _VrPpSrsePathCost_Type(Unsigned32):
    """Custom type vrPpSrsePathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrsePathCost_Type.__name__ = "Unsigned32"
_VrPpSrsePathCost_Object = MibTableColumn
vrPpSrsePathCost = _VrPpSrsePathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1, 5),
    _VrPpSrsePathCost_Type()
)
vrPpSrsePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsePathCost.setStatus("mandatory")


class _VrPpSrsePathCostMethod_Type(Integer32):
    """Custom type vrPpSrsePathCostMethod based on Integer32"""
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


_VrPpSrsePathCostMethod_Type.__name__ = "Integer32"
_VrPpSrsePathCostMethod_Object = MibTableColumn
vrPpSrsePathCostMethod = _VrPpSrsePathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 12, 1, 6),
    _VrPpSrsePathCostMethod_Type()
)
vrPpSrsePathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsePathCostMethod.setStatus("mandatory")
_VrPpSrseDIProvTable_Object = MibTable
vrPpSrseDIProvTable = _VrPpSrseDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 13)
)
if mibBuilder.loadTexts:
    vrPpSrseDIProvTable.setStatus("mandatory")
_VrPpSrseDIProvEntry_Object = MibTableRow
vrPpSrseDIProvEntry = _VrPpSrseDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 13, 1)
)
vrPpSrseDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseDIProvEntry.setStatus("mandatory")


class _VrPpSrseDomainNum_Type(Unsigned32):
    """Custom type vrPpSrseDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpSrseDomainNum_Type.__name__ = "Unsigned32"
_VrPpSrseDomainNum_Object = MibTableColumn
vrPpSrseDomainNum = _VrPpSrseDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 13, 1, 1),
    _VrPpSrseDomainNum_Type()
)
vrPpSrseDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseDomainNum.setStatus("mandatory")


class _VrPpSrsePreserveDomain_Type(Integer32):
    """Custom type vrPpSrsePreserveDomain based on Integer32"""
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


_VrPpSrsePreserveDomain_Type.__name__ = "Integer32"
_VrPpSrsePreserveDomain_Object = MibTableColumn
vrPpSrsePreserveDomain = _VrPpSrsePreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 13, 1, 2),
    _VrPpSrsePreserveDomain_Type()
)
vrPpSrsePreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsePreserveDomain.setStatus("mandatory")
_VrPpSrseStateTable_Object = MibTable
vrPpSrseStateTable = _VrPpSrseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 14)
)
if mibBuilder.loadTexts:
    vrPpSrseStateTable.setStatus("mandatory")
_VrPpSrseStateEntry_Object = MibTableRow
vrPpSrseStateEntry = _VrPpSrseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 14, 1)
)
vrPpSrseStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseStateEntry.setStatus("mandatory")


class _VrPpSrseAdminState_Type(Integer32):
    """Custom type vrPpSrseAdminState based on Integer32"""
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


_VrPpSrseAdminState_Type.__name__ = "Integer32"
_VrPpSrseAdminState_Object = MibTableColumn
vrPpSrseAdminState = _VrPpSrseAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 14, 1, 1),
    _VrPpSrseAdminState_Type()
)
vrPpSrseAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseAdminState.setStatus("mandatory")


class _VrPpSrseOperationalState_Type(Integer32):
    """Custom type vrPpSrseOperationalState based on Integer32"""
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


_VrPpSrseOperationalState_Type.__name__ = "Integer32"
_VrPpSrseOperationalState_Object = MibTableColumn
vrPpSrseOperationalState = _VrPpSrseOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 14, 1, 2),
    _VrPpSrseOperationalState_Type()
)
vrPpSrseOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseOperationalState.setStatus("mandatory")


class _VrPpSrseUsageState_Type(Integer32):
    """Custom type vrPpSrseUsageState based on Integer32"""
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


_VrPpSrseUsageState_Type.__name__ = "Integer32"
_VrPpSrseUsageState_Object = MibTableColumn
vrPpSrseUsageState = _VrPpSrseUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 14, 1, 3),
    _VrPpSrseUsageState_Type()
)
vrPpSrseUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseUsageState.setStatus("mandatory")
_VrPpSrseOperStatusTable_Object = MibTable
vrPpSrseOperStatusTable = _VrPpSrseOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 15)
)
if mibBuilder.loadTexts:
    vrPpSrseOperStatusTable.setStatus("mandatory")
_VrPpSrseOperStatusEntry_Object = MibTableRow
vrPpSrseOperStatusEntry = _VrPpSrseOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 15, 1)
)
vrPpSrseOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseOperStatusEntry.setStatus("mandatory")


class _VrPpSrseSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSrseSnmpOperStatus based on Integer32"""
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


_VrPpSrseSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSrseSnmpOperStatus_Object = MibTableColumn
vrPpSrseSnmpOperStatus = _VrPpSrseSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 15, 1, 1),
    _VrPpSrseSnmpOperStatus_Type()
)
vrPpSrseSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseSnmpOperStatus.setStatus("mandatory")
_VrPpSrseOperTable_Object = MibTable
vrPpSrseOperTable = _VrPpSrseOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16)
)
if mibBuilder.loadTexts:
    vrPpSrseOperTable.setStatus("mandatory")
_VrPpSrseOperEntry_Object = MibTableRow
vrPpSrseOperEntry = _VrPpSrseOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1)
)
vrPpSrseOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseOperEntry.setStatus("mandatory")


class _VrPpSrsePortName_Type(AsciiString):
    """Custom type vrPpSrsePortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpSrsePortName_Type.__name__ = "AsciiString"
_VrPpSrsePortName_Object = MibTableColumn
vrPpSrsePortName = _VrPpSrsePortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 1),
    _VrPpSrsePortName_Type()
)
vrPpSrsePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsePortName.setStatus("mandatory")


class _VrPpSrseUpTime_Type(Unsigned32):
    """Custom type vrPpSrseUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrseUpTime_Type.__name__ = "Unsigned32"
_VrPpSrseUpTime_Object = MibTableColumn
vrPpSrseUpTime = _VrPpSrseUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 3),
    _VrPpSrseUpTime_Type()
)
vrPpSrseUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseUpTime.setStatus("mandatory")


class _VrPpSrseDownTime_Type(Unsigned32):
    """Custom type vrPpSrseDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrseDownTime_Type.__name__ = "Unsigned32"
_VrPpSrseDownTime_Object = MibTableColumn
vrPpSrseDownTime = _VrPpSrseDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 4),
    _VrPpSrseDownTime_Type()
)
vrPpSrseDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDownTime.setStatus("mandatory")


class _VrPpSrseBridgingMode_Type(Integer32):
    """Custom type vrPpSrseBridgingMode based on Integer32"""
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


_VrPpSrseBridgingMode_Type.__name__ = "Integer32"
_VrPpSrseBridgingMode_Object = MibTableColumn
vrPpSrseBridgingMode = _VrPpSrseBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 5),
    _VrPpSrseBridgingMode_Type()
)
vrPpSrseBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseBridgingMode.setStatus("mandatory")


class _VrPpSrseBridgePortConfig_Type(Integer32):
    """Custom type vrPpSrseBridgePortConfig based on Integer32"""
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


_VrPpSrseBridgePortConfig_Type.__name__ = "Integer32"
_VrPpSrseBridgePortConfig_Object = MibTableColumn
vrPpSrseBridgePortConfig = _VrPpSrseBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 6),
    _VrPpSrseBridgePortConfig_Type()
)
vrPpSrseBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseBridgePortConfig.setStatus("mandatory")


class _VrPpSrseBridgePortType_Type(Integer32):
    """Custom type vrPpSrseBridgePortType based on Integer32"""
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


_VrPpSrseBridgePortType_Type.__name__ = "Integer32"
_VrPpSrseBridgePortType_Object = MibTableColumn
vrPpSrseBridgePortType = _VrPpSrseBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 7),
    _VrPpSrseBridgePortType_Type()
)
vrPpSrseBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseBridgePortType.setStatus("mandatory")


class _VrPpSrseIfIndex_Type(InterfaceIndex):
    """Custom type vrPpSrseIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrseIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpSrseIfIndex_Object = MibTableColumn
vrPpSrseIfIndex = _VrPpSrseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 8),
    _VrPpSrseIfIndex_Type()
)
vrPpSrseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseIfIndex.setStatus("mandatory")
_VrPpSrseDelayExceededDiscards_Type = Counter32
_VrPpSrseDelayExceededDiscards_Object = MibTableColumn
vrPpSrseDelayExceededDiscards = _VrPpSrseDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 10),
    _VrPpSrseDelayExceededDiscards_Type()
)
vrPpSrseDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDelayExceededDiscards.setStatus("mandatory")
_VrPpSrseMtuExceededDiscards_Type = Counter32
_VrPpSrseMtuExceededDiscards_Object = MibTableColumn
vrPpSrseMtuExceededDiscards = _VrPpSrseMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 16, 1, 11),
    _VrPpSrseMtuExceededDiscards_Type()
)
vrPpSrseMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseMtuExceededDiscards.setStatus("mandatory")
_VrPpSrseStpOperTable_Object = MibTable
vrPpSrseStpOperTable = _VrPpSrseStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18)
)
if mibBuilder.loadTexts:
    vrPpSrseStpOperTable.setStatus("mandatory")
_VrPpSrseStpOperEntry_Object = MibTableRow
vrPpSrseStpOperEntry = _VrPpSrseStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1)
)
vrPpSrseStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseStpOperEntry.setStatus("mandatory")


class _VrPpSrseStpPortState_Type(Integer32):
    """Custom type vrPpSrseStpPortState based on Integer32"""
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


_VrPpSrseStpPortState_Type.__name__ = "Integer32"
_VrPpSrseStpPortState_Object = MibTableColumn
vrPpSrseStpPortState = _VrPpSrseStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 2),
    _VrPpSrseStpPortState_Type()
)
vrPpSrseStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseStpPortState.setStatus("mandatory")


class _VrPpSrseStpTypeOper_Type(Integer32):
    """Custom type vrPpSrseStpTypeOper based on Integer32"""
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


_VrPpSrseStpTypeOper_Type.__name__ = "Integer32"
_VrPpSrseStpTypeOper_Object = MibTableColumn
vrPpSrseStpTypeOper = _VrPpSrseStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 3),
    _VrPpSrseStpTypeOper_Type()
)
vrPpSrseStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseStpTypeOper.setStatus("mandatory")


class _VrPpSrseDesignatedCost_Type(Unsigned32):
    """Custom type vrPpSrseDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrseDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpSrseDesignatedCost_Object = MibTableColumn
vrPpSrseDesignatedCost = _VrPpSrseDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 4),
    _VrPpSrseDesignatedCost_Type()
)
vrPpSrseDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDesignatedCost.setStatus("mandatory")


class _VrPpSrsePathCostOper_Type(Unsigned32):
    """Custom type vrPpSrsePathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrsePathCostOper_Type.__name__ = "Unsigned32"
_VrPpSrsePathCostOper_Object = MibTableColumn
vrPpSrsePathCostOper = _VrPpSrsePathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 5),
    _VrPpSrsePathCostOper_Type()
)
vrPpSrsePathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsePathCostOper.setStatus("mandatory")


class _VrPpSrseDesignatedBridge_Type(BridgeId):
    """Custom type vrPpSrseDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrseDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpSrseDesignatedBridge_Object = MibTableColumn
vrPpSrseDesignatedBridge = _VrPpSrseDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 6),
    _VrPpSrseDesignatedBridge_Type()
)
vrPpSrseDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDesignatedBridge.setStatus("mandatory")


class _VrPpSrseDesignatedPort_Type(Hex):
    """Custom type vrPpSrseDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrseDesignatedPort_Type.__name__ = "Hex"
_VrPpSrseDesignatedPort_Object = MibTableColumn
vrPpSrseDesignatedPort = _VrPpSrseDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 7),
    _VrPpSrseDesignatedPort_Type()
)
vrPpSrseDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDesignatedPort.setStatus("mandatory")
_VrPpSrseForwardTransitions_Type = Counter32
_VrPpSrseForwardTransitions_Object = MibTableColumn
vrPpSrseForwardTransitions = _VrPpSrseForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 8),
    _VrPpSrseForwardTransitions_Type()
)
vrPpSrseForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseForwardTransitions.setStatus("mandatory")
_VrPpSrseBlockingDiscards_Type = Counter32
_VrPpSrseBlockingDiscards_Object = MibTableColumn
vrPpSrseBlockingDiscards = _VrPpSrseBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 9),
    _VrPpSrseBlockingDiscards_Type()
)
vrPpSrseBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseBlockingDiscards.setStatus("mandatory")


class _VrPpSrseDesignatedRoot_Type(BridgeId):
    """Custom type vrPpSrseDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrseDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpSrseDesignatedRoot_Object = MibTableColumn
vrPpSrseDesignatedRoot = _VrPpSrseDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 18, 1, 10),
    _VrPpSrseDesignatedRoot_Type()
)
vrPpSrseDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDesignatedRoot.setStatus("mandatory")
_VrPpSrseStatsTable_Object = MibTable
vrPpSrseStatsTable = _VrPpSrseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19)
)
if mibBuilder.loadTexts:
    vrPpSrseStatsTable.setStatus("mandatory")
_VrPpSrseStatsEntry_Object = MibTableRow
vrPpSrseStatsEntry = _VrPpSrseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19, 1)
)
vrPpSrseStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseStatsEntry.setStatus("mandatory")
_VrPpSrseBadAbstractDiscards_Type = Counter32
_VrPpSrseBadAbstractDiscards_Object = MibTableColumn
vrPpSrseBadAbstractDiscards = _VrPpSrseBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19, 1, 1),
    _VrPpSrseBadAbstractDiscards_Type()
)
vrPpSrseBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseBadAbstractDiscards.setStatus("mandatory")
_VrPpSrseTinygramFramesIn_Type = Counter32
_VrPpSrseTinygramFramesIn_Object = MibTableColumn
vrPpSrseTinygramFramesIn = _VrPpSrseTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19, 1, 2),
    _VrPpSrseTinygramFramesIn_Type()
)
vrPpSrseTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseTinygramFramesIn.setStatus("mandatory")
_VrPpSrseTinygramFramesOut_Type = Counter32
_VrPpSrseTinygramFramesOut_Object = MibTableColumn
vrPpSrseTinygramFramesOut = _VrPpSrseTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19, 1, 3),
    _VrPpSrseTinygramFramesOut_Type()
)
vrPpSrseTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseTinygramFramesOut.setStatus("mandatory")
_VrPpSrseInFilterDiscards_Type = Counter32
_VrPpSrseInFilterDiscards_Object = MibTableColumn
vrPpSrseInFilterDiscards = _VrPpSrseInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19, 1, 4),
    _VrPpSrseInFilterDiscards_Type()
)
vrPpSrseInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseInFilterDiscards.setStatus("mandatory")
_VrPpSrseOutFilterDiscards_Type = Counter32
_VrPpSrseOutFilterDiscards_Object = MibTableColumn
vrPpSrseOutFilterDiscards = _VrPpSrseOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 19, 1, 5),
    _VrPpSrseOutFilterDiscards_Type()
)
vrPpSrseOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseOutFilterDiscards.setStatus("mandatory")
_VrPpSrseSrProvTable_Object = MibTable
vrPpSrseSrProvTable = _VrPpSrseSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20)
)
if mibBuilder.loadTexts:
    vrPpSrseSrProvTable.setStatus("mandatory")
_VrPpSrseSrProvEntry_Object = MibTableRow
vrPpSrseSrProvEntry = _VrPpSrseSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1)
)
vrPpSrseSrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseSrProvEntry.setStatus("mandatory")


class _VrPpSrseHopCount_Type(Unsigned32):
    """Custom type vrPpSrseHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrPpSrseHopCount_Type.__name__ = "Unsigned32"
_VrPpSrseHopCount_Object = MibTableColumn
vrPpSrseHopCount = _VrPpSrseHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 1),
    _VrPpSrseHopCount_Type()
)
vrPpSrseHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseHopCount.setStatus("mandatory")


class _VrPpSrseExploreFrameTreatment_Type(Integer32):
    """Custom type vrPpSrseExploreFrameTreatment based on Integer32"""
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


_VrPpSrseExploreFrameTreatment_Type.__name__ = "Integer32"
_VrPpSrseExploreFrameTreatment_Object = MibTableColumn
vrPpSrseExploreFrameTreatment = _VrPpSrseExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 2),
    _VrPpSrseExploreFrameTreatment_Type()
)
vrPpSrseExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseExploreFrameTreatment.setStatus("mandatory")


class _VrPpSrseLanId_Type(Unsigned32):
    """Custom type vrPpSrseLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrseLanId_Type.__name__ = "Unsigned32"
_VrPpSrseLanId_Object = MibTableColumn
vrPpSrseLanId = _VrPpSrseLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 3),
    _VrPpSrseLanId_Type()
)
vrPpSrseLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseLanId.setStatus("mandatory")


class _VrPpSrseInternalLanId_Type(Unsigned32):
    """Custom type vrPpSrseInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrseInternalLanId_Type.__name__ = "Unsigned32"
_VrPpSrseInternalLanId_Object = MibTableColumn
vrPpSrseInternalLanId = _VrPpSrseInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 4),
    _VrPpSrseInternalLanId_Type()
)
vrPpSrseInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseInternalLanId.setStatus("mandatory")


class _VrPpSrseBridgeNum_Type(Unsigned32):
    """Custom type vrPpSrseBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrPpSrseBridgeNum_Type.__name__ = "Unsigned32"
_VrPpSrseBridgeNum_Object = MibTableColumn
vrPpSrseBridgeNum = _VrPpSrseBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 5),
    _VrPpSrseBridgeNum_Type()
)
vrPpSrseBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseBridgeNum.setStatus("mandatory")


class _VrPpSrseLargestFrame_Type(Unsigned32):
    """Custom type vrPpSrseLargestFrame based on Unsigned32"""
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


_VrPpSrseLargestFrame_Type.__name__ = "Unsigned32"
_VrPpSrseLargestFrame_Object = MibTableColumn
vrPpSrseLargestFrame = _VrPpSrseLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 6),
    _VrPpSrseLargestFrame_Type()
)
vrPpSrseLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseLargestFrame.setStatus("mandatory")


class _VrPpSrseSteSpanMode_Type(Integer32):
    """Custom type vrPpSrseSteSpanMode based on Integer32"""
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


_VrPpSrseSteSpanMode_Type.__name__ = "Integer32"
_VrPpSrseSteSpanMode_Object = MibTableColumn
vrPpSrseSteSpanMode = _VrPpSrseSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 7),
    _VrPpSrseSteSpanMode_Type()
)
vrPpSrseSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseSteSpanMode.setStatus("mandatory")


class _VrPpSrseAreRdLimit_Type(Unsigned32):
    """Custom type vrPpSrseAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrseAreRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrseAreRdLimit_Object = MibTableColumn
vrPpSrseAreRdLimit = _VrPpSrseAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 8),
    _VrPpSrseAreRdLimit_Type()
)
vrPpSrseAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseAreRdLimit.setStatus("mandatory")


class _VrPpSrseSteRdLimit_Type(Unsigned32):
    """Custom type vrPpSrseSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrseSteRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrseSteRdLimit_Object = MibTableColumn
vrPpSrseSteRdLimit = _VrPpSrseSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 20, 1, 9),
    _VrPpSrseSteRdLimit_Type()
)
vrPpSrseSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrseSteRdLimit.setStatus("mandatory")
_VrPpSrseSrStatsTable_Object = MibTable
vrPpSrseSrStatsTable = _VrPpSrseSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21)
)
if mibBuilder.loadTexts:
    vrPpSrseSrStatsTable.setStatus("mandatory")
_VrPpSrseSrStatsEntry_Object = MibTableRow
vrPpSrseSrStatsEntry = _VrPpSrseSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1)
)
vrPpSrseSrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrseIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrseSrStatsEntry.setStatus("mandatory")
_VrPpSrseSpecInFrames_Type = Counter32
_VrPpSrseSpecInFrames_Object = MibTableColumn
vrPpSrseSpecInFrames = _VrPpSrseSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 1),
    _VrPpSrseSpecInFrames_Type()
)
vrPpSrseSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseSpecInFrames.setStatus("mandatory")
_VrPpSrseSpecOutFrames_Type = Counter32
_VrPpSrseSpecOutFrames_Object = MibTableColumn
vrPpSrseSpecOutFrames = _VrPpSrseSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 2),
    _VrPpSrseSpecOutFrames_Type()
)
vrPpSrseSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseSpecOutFrames.setStatus("mandatory")
_VrPpSrseApeInFrames_Type = Counter32
_VrPpSrseApeInFrames_Object = MibTableColumn
vrPpSrseApeInFrames = _VrPpSrseApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 3),
    _VrPpSrseApeInFrames_Type()
)
vrPpSrseApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseApeInFrames.setStatus("mandatory")
_VrPpSrseApeOutFrames_Type = Counter32
_VrPpSrseApeOutFrames_Object = MibTableColumn
vrPpSrseApeOutFrames = _VrPpSrseApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 4),
    _VrPpSrseApeOutFrames_Type()
)
vrPpSrseApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseApeOutFrames.setStatus("mandatory")
_VrPpSrseSteInFrames_Type = Counter32
_VrPpSrseSteInFrames_Object = MibTableColumn
vrPpSrseSteInFrames = _VrPpSrseSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 5),
    _VrPpSrseSteInFrames_Type()
)
vrPpSrseSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseSteInFrames.setStatus("mandatory")
_VrPpSrseSteOutFrames_Type = Counter32
_VrPpSrseSteOutFrames_Object = MibTableColumn
vrPpSrseSteOutFrames = _VrPpSrseSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 6),
    _VrPpSrseSteOutFrames_Type()
)
vrPpSrseSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseSteOutFrames.setStatus("mandatory")
_VrPpSrseSegmentMismatchDiscards_Type = Counter32
_VrPpSrseSegmentMismatchDiscards_Object = MibTableColumn
vrPpSrseSegmentMismatchDiscards = _VrPpSrseSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 7),
    _VrPpSrseSegmentMismatchDiscards_Type()
)
vrPpSrseSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseSegmentMismatchDiscards.setStatus("mandatory")
_VrPpSrseDupSegmentDiscards_Type = Counter32
_VrPpSrseDupSegmentDiscards_Object = MibTableColumn
vrPpSrseDupSegmentDiscards = _VrPpSrseDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 8),
    _VrPpSrseDupSegmentDiscards_Type()
)
vrPpSrseDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDupSegmentDiscards.setStatus("mandatory")
_VrPpSrseHopCountExceededDiscards_Type = Counter32
_VrPpSrseHopCountExceededDiscards_Object = MibTableColumn
vrPpSrseHopCountExceededDiscards = _VrPpSrseHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 9),
    _VrPpSrseHopCountExceededDiscards_Type()
)
vrPpSrseHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseHopCountExceededDiscards.setStatus("mandatory")
_VrPpSrseDupLanIdOrTreeErrors_Type = Counter32
_VrPpSrseDupLanIdOrTreeErrors_Object = MibTableColumn
vrPpSrseDupLanIdOrTreeErrors = _VrPpSrseDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 10),
    _VrPpSrseDupLanIdOrTreeErrors_Type()
)
vrPpSrseDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDupLanIdOrTreeErrors.setStatus("mandatory")
_VrPpSrseLanIdMismatches_Type = Counter32
_VrPpSrseLanIdMismatches_Object = MibTableColumn
vrPpSrseLanIdMismatches = _VrPpSrseLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 11),
    _VrPpSrseLanIdMismatches_Type()
)
vrPpSrseLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseLanIdMismatches.setStatus("mandatory")
_VrPpSrseStaticDiscards_Type = Counter32
_VrPpSrseStaticDiscards_Object = MibTableColumn
vrPpSrseStaticDiscards = _VrPpSrseStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 12),
    _VrPpSrseStaticDiscards_Type()
)
vrPpSrseStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseStaticDiscards.setStatus("mandatory")
_VrPpSrseDynamicDiscards_Type = Counter32
_VrPpSrseDynamicDiscards_Object = MibTableColumn
vrPpSrseDynamicDiscards = _VrPpSrseDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 10, 21, 1, 13),
    _VrPpSrseDynamicDiscards_Type()
)
vrPpSrseDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrseDynamicDiscards.setStatus("mandatory")
_VrPpTbse_ObjectIdentity = ObjectIdentity
vrPpTbse = _VrPpTbse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11)
)
_VrPpTbseRowStatusTable_Object = MibTable
vrPpTbseRowStatusTable = _VrPpTbseRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 1)
)
if mibBuilder.loadTexts:
    vrPpTbseRowStatusTable.setStatus("mandatory")
_VrPpTbseRowStatusEntry_Object = MibTableRow
vrPpTbseRowStatusEntry = _VrPpTbseRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 1, 1)
)
vrPpTbseRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseRowStatusEntry.setStatus("mandatory")
_VrPpTbseRowStatus_Type = RowStatus
_VrPpTbseRowStatus_Object = MibTableColumn
vrPpTbseRowStatus = _VrPpTbseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 1, 1, 1),
    _VrPpTbseRowStatus_Type()
)
vrPpTbseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseRowStatus.setStatus("mandatory")
_VrPpTbseComponentName_Type = DisplayString
_VrPpTbseComponentName_Object = MibTableColumn
vrPpTbseComponentName = _VrPpTbseComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 1, 1, 2),
    _VrPpTbseComponentName_Type()
)
vrPpTbseComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseComponentName.setStatus("mandatory")
_VrPpTbseStorageType_Type = StorageType
_VrPpTbseStorageType_Object = MibTableColumn
vrPpTbseStorageType = _VrPpTbseStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 1, 1, 4),
    _VrPpTbseStorageType_Type()
)
vrPpTbseStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseStorageType.setStatus("mandatory")
_VrPpTbseIndex_Type = NonReplicated
_VrPpTbseIndex_Object = MibTableColumn
vrPpTbseIndex = _VrPpTbseIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 1, 1, 10),
    _VrPpTbseIndex_Type()
)
vrPpTbseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpTbseIndex.setStatus("mandatory")
_VrPpTbseProvTable_Object = MibTable
vrPpTbseProvTable = _VrPpTbseProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10)
)
if mibBuilder.loadTexts:
    vrPpTbseProvTable.setStatus("mandatory")
_VrPpTbseProvEntry_Object = MibTableRow
vrPpTbseProvEntry = _VrPpTbseProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1)
)
vrPpTbseProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseProvEntry.setStatus("mandatory")


class _VrPpTbseTranslateIpx_Type(Integer32):
    """Custom type vrPpTbseTranslateIpx based on Integer32"""
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


_VrPpTbseTranslateIpx_Type.__name__ = "Integer32"
_VrPpTbseTranslateIpx_Object = MibTableColumn
vrPpTbseTranslateIpx = _VrPpTbseTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1, 1),
    _VrPpTbseTranslateIpx_Type()
)
vrPpTbseTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseTranslateIpx.setStatus("mandatory")


class _VrPpTbseFragmentIp_Type(Integer32):
    """Custom type vrPpTbseFragmentIp based on Integer32"""
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


_VrPpTbseFragmentIp_Type.__name__ = "Integer32"
_VrPpTbseFragmentIp_Object = MibTableColumn
vrPpTbseFragmentIp = _VrPpTbseFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1, 2),
    _VrPpTbseFragmentIp_Type()
)
vrPpTbseFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseFragmentIp.setStatus("mandatory")


class _VrPpTbseServiceClass_Type(Integer32):
    """Custom type vrPpTbseServiceClass based on Integer32"""
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


_VrPpTbseServiceClass_Type.__name__ = "Integer32"
_VrPpTbseServiceClass_Object = MibTableColumn
vrPpTbseServiceClass = _VrPpTbseServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1, 3),
    _VrPpTbseServiceClass_Type()
)
vrPpTbseServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseServiceClass.setStatus("mandatory")


class _VrPpTbseConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpTbseConvertArpMacAddress based on Integer32"""
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


_VrPpTbseConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpTbseConvertArpMacAddress_Object = MibTableColumn
vrPpTbseConvertArpMacAddress = _VrPpTbseConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1, 4),
    _VrPpTbseConvertArpMacAddress_Type()
)
vrPpTbseConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseConvertArpMacAddress.setStatus("mandatory")


class _VrPpTbsePortNum_Type(Unsigned32):
    """Custom type vrPpTbsePortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpTbsePortNum_Type.__name__ = "Unsigned32"
_VrPpTbsePortNum_Object = MibTableColumn
vrPpTbsePortNum = _VrPpTbsePortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1, 5),
    _VrPpTbsePortNum_Type()
)
vrPpTbsePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsePortNum.setStatus("mandatory")


class _VrPpTbseOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpTbseOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpTbseOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpTbseOutboundFrameMediaType_Object = MibTableColumn
vrPpTbseOutboundFrameMediaType = _VrPpTbseOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 10, 1, 6),
    _VrPpTbseOutboundFrameMediaType_Type()
)
vrPpTbseOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseOutboundFrameMediaType.setStatus("mandatory")
_VrPpTbseTbProvTable_Object = MibTable
vrPpTbseTbProvTable = _VrPpTbseTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 11)
)
if mibBuilder.loadTexts:
    vrPpTbseTbProvTable.setStatus("mandatory")
_VrPpTbseTbProvEntry_Object = MibTableRow
vrPpTbseTbProvEntry = _VrPpTbseTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 11, 1)
)
vrPpTbseTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseTbProvEntry.setStatus("mandatory")


class _VrPpTbseSecureOption_Type(Integer32):
    """Custom type vrPpTbseSecureOption based on Integer32"""
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


_VrPpTbseSecureOption_Type.__name__ = "Integer32"
_VrPpTbseSecureOption_Object = MibTableColumn
vrPpTbseSecureOption = _VrPpTbseSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 11, 1, 1),
    _VrPpTbseSecureOption_Type()
)
vrPpTbseSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseSecureOption.setStatus("mandatory")
_VrPpTbseStpProvTable_Object = MibTable
vrPpTbseStpProvTable = _VrPpTbseStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12)
)
if mibBuilder.loadTexts:
    vrPpTbseStpProvTable.setStatus("mandatory")
_VrPpTbseStpProvEntry_Object = MibTableRow
vrPpTbseStpProvEntry = _VrPpTbseStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1)
)
vrPpTbseStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseStpProvEntry.setStatus("mandatory")


class _VrPpTbseAdminStatus_Type(Integer32):
    """Custom type vrPpTbseAdminStatus based on Integer32"""
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


_VrPpTbseAdminStatus_Type.__name__ = "Integer32"
_VrPpTbseAdminStatus_Object = MibTableColumn
vrPpTbseAdminStatus = _VrPpTbseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1, 1),
    _VrPpTbseAdminStatus_Type()
)
vrPpTbseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseAdminStatus.setStatus("mandatory")


class _VrPpTbsePortStateStpControl_Type(Integer32):
    """Custom type vrPpTbsePortStateStpControl based on Integer32"""
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


_VrPpTbsePortStateStpControl_Type.__name__ = "Integer32"
_VrPpTbsePortStateStpControl_Object = MibTableColumn
vrPpTbsePortStateStpControl = _VrPpTbsePortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1, 2),
    _VrPpTbsePortStateStpControl_Type()
)
vrPpTbsePortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsePortStateStpControl.setStatus("mandatory")


class _VrPpTbseStpTypeProv_Type(Integer32):
    """Custom type vrPpTbseStpTypeProv based on Integer32"""
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


_VrPpTbseStpTypeProv_Type.__name__ = "Integer32"
_VrPpTbseStpTypeProv_Object = MibTableColumn
vrPpTbseStpTypeProv = _VrPpTbseStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1, 3),
    _VrPpTbseStpTypeProv_Type()
)
vrPpTbseStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseStpTypeProv.setStatus("mandatory")


class _VrPpTbsePortPriority_Type(Unsigned32):
    """Custom type vrPpTbsePortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbsePortPriority_Type.__name__ = "Unsigned32"
_VrPpTbsePortPriority_Object = MibTableColumn
vrPpTbsePortPriority = _VrPpTbsePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1, 4),
    _VrPpTbsePortPriority_Type()
)
vrPpTbsePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsePortPriority.setStatus("mandatory")


class _VrPpTbsePathCost_Type(Unsigned32):
    """Custom type vrPpTbsePathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbsePathCost_Type.__name__ = "Unsigned32"
_VrPpTbsePathCost_Object = MibTableColumn
vrPpTbsePathCost = _VrPpTbsePathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1, 5),
    _VrPpTbsePathCost_Type()
)
vrPpTbsePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsePathCost.setStatus("mandatory")


class _VrPpTbsePathCostMethod_Type(Integer32):
    """Custom type vrPpTbsePathCostMethod based on Integer32"""
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


_VrPpTbsePathCostMethod_Type.__name__ = "Integer32"
_VrPpTbsePathCostMethod_Object = MibTableColumn
vrPpTbsePathCostMethod = _VrPpTbsePathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 12, 1, 6),
    _VrPpTbsePathCostMethod_Type()
)
vrPpTbsePathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsePathCostMethod.setStatus("mandatory")
_VrPpTbseDIProvTable_Object = MibTable
vrPpTbseDIProvTable = _VrPpTbseDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 13)
)
if mibBuilder.loadTexts:
    vrPpTbseDIProvTable.setStatus("mandatory")
_VrPpTbseDIProvEntry_Object = MibTableRow
vrPpTbseDIProvEntry = _VrPpTbseDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 13, 1)
)
vrPpTbseDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseDIProvEntry.setStatus("mandatory")


class _VrPpTbseDomainNum_Type(Unsigned32):
    """Custom type vrPpTbseDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpTbseDomainNum_Type.__name__ = "Unsigned32"
_VrPpTbseDomainNum_Object = MibTableColumn
vrPpTbseDomainNum = _VrPpTbseDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 13, 1, 1),
    _VrPpTbseDomainNum_Type()
)
vrPpTbseDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbseDomainNum.setStatus("mandatory")


class _VrPpTbsePreserveDomain_Type(Integer32):
    """Custom type vrPpTbsePreserveDomain based on Integer32"""
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


_VrPpTbsePreserveDomain_Type.__name__ = "Integer32"
_VrPpTbsePreserveDomain_Object = MibTableColumn
vrPpTbsePreserveDomain = _VrPpTbsePreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 13, 1, 2),
    _VrPpTbsePreserveDomain_Type()
)
vrPpTbsePreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsePreserveDomain.setStatus("mandatory")
_VrPpTbseStateTable_Object = MibTable
vrPpTbseStateTable = _VrPpTbseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 14)
)
if mibBuilder.loadTexts:
    vrPpTbseStateTable.setStatus("mandatory")
_VrPpTbseStateEntry_Object = MibTableRow
vrPpTbseStateEntry = _VrPpTbseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 14, 1)
)
vrPpTbseStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseStateEntry.setStatus("mandatory")


class _VrPpTbseAdminState_Type(Integer32):
    """Custom type vrPpTbseAdminState based on Integer32"""
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


_VrPpTbseAdminState_Type.__name__ = "Integer32"
_VrPpTbseAdminState_Object = MibTableColumn
vrPpTbseAdminState = _VrPpTbseAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 14, 1, 1),
    _VrPpTbseAdminState_Type()
)
vrPpTbseAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseAdminState.setStatus("mandatory")


class _VrPpTbseOperationalState_Type(Integer32):
    """Custom type vrPpTbseOperationalState based on Integer32"""
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


_VrPpTbseOperationalState_Type.__name__ = "Integer32"
_VrPpTbseOperationalState_Object = MibTableColumn
vrPpTbseOperationalState = _VrPpTbseOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 14, 1, 2),
    _VrPpTbseOperationalState_Type()
)
vrPpTbseOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseOperationalState.setStatus("mandatory")


class _VrPpTbseUsageState_Type(Integer32):
    """Custom type vrPpTbseUsageState based on Integer32"""
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


_VrPpTbseUsageState_Type.__name__ = "Integer32"
_VrPpTbseUsageState_Object = MibTableColumn
vrPpTbseUsageState = _VrPpTbseUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 14, 1, 3),
    _VrPpTbseUsageState_Type()
)
vrPpTbseUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseUsageState.setStatus("mandatory")
_VrPpTbseOperStatusTable_Object = MibTable
vrPpTbseOperStatusTable = _VrPpTbseOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 15)
)
if mibBuilder.loadTexts:
    vrPpTbseOperStatusTable.setStatus("mandatory")
_VrPpTbseOperStatusEntry_Object = MibTableRow
vrPpTbseOperStatusEntry = _VrPpTbseOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 15, 1)
)
vrPpTbseOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseOperStatusEntry.setStatus("mandatory")


class _VrPpTbseSnmpOperStatus_Type(Integer32):
    """Custom type vrPpTbseSnmpOperStatus based on Integer32"""
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


_VrPpTbseSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpTbseSnmpOperStatus_Object = MibTableColumn
vrPpTbseSnmpOperStatus = _VrPpTbseSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 15, 1, 1),
    _VrPpTbseSnmpOperStatus_Type()
)
vrPpTbseSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseSnmpOperStatus.setStatus("mandatory")
_VrPpTbseOperTable_Object = MibTable
vrPpTbseOperTable = _VrPpTbseOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16)
)
if mibBuilder.loadTexts:
    vrPpTbseOperTable.setStatus("mandatory")
_VrPpTbseOperEntry_Object = MibTableRow
vrPpTbseOperEntry = _VrPpTbseOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1)
)
vrPpTbseOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseOperEntry.setStatus("mandatory")


class _VrPpTbsePortName_Type(AsciiString):
    """Custom type vrPpTbsePortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpTbsePortName_Type.__name__ = "AsciiString"
_VrPpTbsePortName_Object = MibTableColumn
vrPpTbsePortName = _VrPpTbsePortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 1),
    _VrPpTbsePortName_Type()
)
vrPpTbsePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsePortName.setStatus("mandatory")


class _VrPpTbseUpTime_Type(Unsigned32):
    """Custom type vrPpTbseUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbseUpTime_Type.__name__ = "Unsigned32"
_VrPpTbseUpTime_Object = MibTableColumn
vrPpTbseUpTime = _VrPpTbseUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 3),
    _VrPpTbseUpTime_Type()
)
vrPpTbseUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseUpTime.setStatus("mandatory")


class _VrPpTbseDownTime_Type(Unsigned32):
    """Custom type vrPpTbseDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbseDownTime_Type.__name__ = "Unsigned32"
_VrPpTbseDownTime_Object = MibTableColumn
vrPpTbseDownTime = _VrPpTbseDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 4),
    _VrPpTbseDownTime_Type()
)
vrPpTbseDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDownTime.setStatus("mandatory")


class _VrPpTbseBridgingMode_Type(Integer32):
    """Custom type vrPpTbseBridgingMode based on Integer32"""
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


_VrPpTbseBridgingMode_Type.__name__ = "Integer32"
_VrPpTbseBridgingMode_Object = MibTableColumn
vrPpTbseBridgingMode = _VrPpTbseBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 5),
    _VrPpTbseBridgingMode_Type()
)
vrPpTbseBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseBridgingMode.setStatus("mandatory")


class _VrPpTbseBridgePortConfig_Type(Integer32):
    """Custom type vrPpTbseBridgePortConfig based on Integer32"""
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


_VrPpTbseBridgePortConfig_Type.__name__ = "Integer32"
_VrPpTbseBridgePortConfig_Object = MibTableColumn
vrPpTbseBridgePortConfig = _VrPpTbseBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 6),
    _VrPpTbseBridgePortConfig_Type()
)
vrPpTbseBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseBridgePortConfig.setStatus("mandatory")


class _VrPpTbseBridgePortType_Type(Integer32):
    """Custom type vrPpTbseBridgePortType based on Integer32"""
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


_VrPpTbseBridgePortType_Type.__name__ = "Integer32"
_VrPpTbseBridgePortType_Object = MibTableColumn
vrPpTbseBridgePortType = _VrPpTbseBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 7),
    _VrPpTbseBridgePortType_Type()
)
vrPpTbseBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseBridgePortType.setStatus("mandatory")


class _VrPpTbseIfIndex_Type(InterfaceIndex):
    """Custom type vrPpTbseIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbseIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpTbseIfIndex_Object = MibTableColumn
vrPpTbseIfIndex = _VrPpTbseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 8),
    _VrPpTbseIfIndex_Type()
)
vrPpTbseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseIfIndex.setStatus("mandatory")
_VrPpTbseDelayExceededDiscards_Type = Counter32
_VrPpTbseDelayExceededDiscards_Object = MibTableColumn
vrPpTbseDelayExceededDiscards = _VrPpTbseDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 10),
    _VrPpTbseDelayExceededDiscards_Type()
)
vrPpTbseDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDelayExceededDiscards.setStatus("mandatory")
_VrPpTbseMtuExceededDiscards_Type = Counter32
_VrPpTbseMtuExceededDiscards_Object = MibTableColumn
vrPpTbseMtuExceededDiscards = _VrPpTbseMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 16, 1, 11),
    _VrPpTbseMtuExceededDiscards_Type()
)
vrPpTbseMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseMtuExceededDiscards.setStatus("mandatory")
_VrPpTbseTbOperTable_Object = MibTable
vrPpTbseTbOperTable = _VrPpTbseTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17)
)
if mibBuilder.loadTexts:
    vrPpTbseTbOperTable.setStatus("mandatory")
_VrPpTbseTbOperEntry_Object = MibTableRow
vrPpTbseTbOperEntry = _VrPpTbseTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1)
)
vrPpTbseTbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseTbOperEntry.setStatus("mandatory")


class _VrPpTbseMaxInfo_Type(Unsigned32):
    """Custom type vrPpTbseMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbseMaxInfo_Type.__name__ = "Unsigned32"
_VrPpTbseMaxInfo_Object = MibTableColumn
vrPpTbseMaxInfo = _VrPpTbseMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 2),
    _VrPpTbseMaxInfo_Type()
)
vrPpTbseMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseMaxInfo.setStatus("mandatory")
_VrPpTbseBadVerifyDiscards_Type = Counter32
_VrPpTbseBadVerifyDiscards_Object = MibTableColumn
vrPpTbseBadVerifyDiscards = _VrPpTbseBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 3),
    _VrPpTbseBadVerifyDiscards_Type()
)
vrPpTbseBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseBadVerifyDiscards.setStatus("mandatory")
_VrPpTbseUnicastNoMatches_Type = Counter32
_VrPpTbseUnicastNoMatches_Object = MibTableColumn
vrPpTbseUnicastNoMatches = _VrPpTbseUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 4),
    _VrPpTbseUnicastNoMatches_Type()
)
vrPpTbseUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseUnicastNoMatches.setStatus("mandatory")
_VrPpTbseStaticEntryDiscards_Type = Counter32
_VrPpTbseStaticEntryDiscards_Object = MibTableColumn
vrPpTbseStaticEntryDiscards = _VrPpTbseStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 5),
    _VrPpTbseStaticEntryDiscards_Type()
)
vrPpTbseStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseStaticEntryDiscards.setStatus("mandatory")
_VrPpTbseDynamicEntryDiscards_Type = Counter32
_VrPpTbseDynamicEntryDiscards_Object = MibTableColumn
vrPpTbseDynamicEntryDiscards = _VrPpTbseDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 6),
    _VrPpTbseDynamicEntryDiscards_Type()
)
vrPpTbseDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDynamicEntryDiscards.setStatus("mandatory")
_VrPpTbseLearningDiscards_Type = Counter32
_VrPpTbseLearningDiscards_Object = MibTableColumn
vrPpTbseLearningDiscards = _VrPpTbseLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 7),
    _VrPpTbseLearningDiscards_Type()
)
vrPpTbseLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseLearningDiscards.setStatus("mandatory")
_VrPpTbseInDiscards_Type = Counter32
_VrPpTbseInDiscards_Object = MibTableColumn
vrPpTbseInDiscards = _VrPpTbseInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 8),
    _VrPpTbseInDiscards_Type()
)
vrPpTbseInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseInDiscards.setStatus("mandatory")
_VrPpTbseInFrames_Type = Counter32
_VrPpTbseInFrames_Object = MibTableColumn
vrPpTbseInFrames = _VrPpTbseInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 9),
    _VrPpTbseInFrames_Type()
)
vrPpTbseInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseInFrames.setStatus("mandatory")
_VrPpTbseOutFrames_Type = Counter32
_VrPpTbseOutFrames_Object = MibTableColumn
vrPpTbseOutFrames = _VrPpTbseOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 17, 1, 10),
    _VrPpTbseOutFrames_Type()
)
vrPpTbseOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseOutFrames.setStatus("mandatory")
_VrPpTbseStpOperTable_Object = MibTable
vrPpTbseStpOperTable = _VrPpTbseStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18)
)
if mibBuilder.loadTexts:
    vrPpTbseStpOperTable.setStatus("mandatory")
_VrPpTbseStpOperEntry_Object = MibTableRow
vrPpTbseStpOperEntry = _VrPpTbseStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1)
)
vrPpTbseStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseStpOperEntry.setStatus("mandatory")


class _VrPpTbseStpPortState_Type(Integer32):
    """Custom type vrPpTbseStpPortState based on Integer32"""
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


_VrPpTbseStpPortState_Type.__name__ = "Integer32"
_VrPpTbseStpPortState_Object = MibTableColumn
vrPpTbseStpPortState = _VrPpTbseStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 2),
    _VrPpTbseStpPortState_Type()
)
vrPpTbseStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseStpPortState.setStatus("mandatory")


class _VrPpTbseStpTypeOper_Type(Integer32):
    """Custom type vrPpTbseStpTypeOper based on Integer32"""
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


_VrPpTbseStpTypeOper_Type.__name__ = "Integer32"
_VrPpTbseStpTypeOper_Object = MibTableColumn
vrPpTbseStpTypeOper = _VrPpTbseStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 3),
    _VrPpTbseStpTypeOper_Type()
)
vrPpTbseStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseStpTypeOper.setStatus("mandatory")


class _VrPpTbseDesignatedCost_Type(Unsigned32):
    """Custom type vrPpTbseDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbseDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpTbseDesignatedCost_Object = MibTableColumn
vrPpTbseDesignatedCost = _VrPpTbseDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 4),
    _VrPpTbseDesignatedCost_Type()
)
vrPpTbseDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDesignatedCost.setStatus("mandatory")


class _VrPpTbsePathCostOper_Type(Unsigned32):
    """Custom type vrPpTbsePathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbsePathCostOper_Type.__name__ = "Unsigned32"
_VrPpTbsePathCostOper_Object = MibTableColumn
vrPpTbsePathCostOper = _VrPpTbsePathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 5),
    _VrPpTbsePathCostOper_Type()
)
vrPpTbsePathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsePathCostOper.setStatus("mandatory")


class _VrPpTbseDesignatedBridge_Type(BridgeId):
    """Custom type vrPpTbseDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbseDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpTbseDesignatedBridge_Object = MibTableColumn
vrPpTbseDesignatedBridge = _VrPpTbseDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 6),
    _VrPpTbseDesignatedBridge_Type()
)
vrPpTbseDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDesignatedBridge.setStatus("mandatory")


class _VrPpTbseDesignatedPort_Type(Hex):
    """Custom type vrPpTbseDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbseDesignatedPort_Type.__name__ = "Hex"
_VrPpTbseDesignatedPort_Object = MibTableColumn
vrPpTbseDesignatedPort = _VrPpTbseDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 7),
    _VrPpTbseDesignatedPort_Type()
)
vrPpTbseDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDesignatedPort.setStatus("mandatory")
_VrPpTbseForwardTransitions_Type = Counter32
_VrPpTbseForwardTransitions_Object = MibTableColumn
vrPpTbseForwardTransitions = _VrPpTbseForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 8),
    _VrPpTbseForwardTransitions_Type()
)
vrPpTbseForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseForwardTransitions.setStatus("mandatory")
_VrPpTbseBlockingDiscards_Type = Counter32
_VrPpTbseBlockingDiscards_Object = MibTableColumn
vrPpTbseBlockingDiscards = _VrPpTbseBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 9),
    _VrPpTbseBlockingDiscards_Type()
)
vrPpTbseBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseBlockingDiscards.setStatus("mandatory")


class _VrPpTbseDesignatedRoot_Type(BridgeId):
    """Custom type vrPpTbseDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbseDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpTbseDesignatedRoot_Object = MibTableColumn
vrPpTbseDesignatedRoot = _VrPpTbseDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 18, 1, 10),
    _VrPpTbseDesignatedRoot_Type()
)
vrPpTbseDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseDesignatedRoot.setStatus("mandatory")
_VrPpTbseStatsTable_Object = MibTable
vrPpTbseStatsTable = _VrPpTbseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19)
)
if mibBuilder.loadTexts:
    vrPpTbseStatsTable.setStatus("mandatory")
_VrPpTbseStatsEntry_Object = MibTableRow
vrPpTbseStatsEntry = _VrPpTbseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19, 1)
)
vrPpTbseStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbseIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbseStatsEntry.setStatus("mandatory")
_VrPpTbseBadAbstractDiscards_Type = Counter32
_VrPpTbseBadAbstractDiscards_Object = MibTableColumn
vrPpTbseBadAbstractDiscards = _VrPpTbseBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19, 1, 1),
    _VrPpTbseBadAbstractDiscards_Type()
)
vrPpTbseBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseBadAbstractDiscards.setStatus("mandatory")
_VrPpTbseTinygramFramesIn_Type = Counter32
_VrPpTbseTinygramFramesIn_Object = MibTableColumn
vrPpTbseTinygramFramesIn = _VrPpTbseTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19, 1, 2),
    _VrPpTbseTinygramFramesIn_Type()
)
vrPpTbseTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseTinygramFramesIn.setStatus("mandatory")
_VrPpTbseTinygramFramesOut_Type = Counter32
_VrPpTbseTinygramFramesOut_Object = MibTableColumn
vrPpTbseTinygramFramesOut = _VrPpTbseTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19, 1, 3),
    _VrPpTbseTinygramFramesOut_Type()
)
vrPpTbseTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseTinygramFramesOut.setStatus("mandatory")
_VrPpTbseInFilterDiscards_Type = Counter32
_VrPpTbseInFilterDiscards_Object = MibTableColumn
vrPpTbseInFilterDiscards = _VrPpTbseInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19, 1, 4),
    _VrPpTbseInFilterDiscards_Type()
)
vrPpTbseInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseInFilterDiscards.setStatus("mandatory")
_VrPpTbseOutFilterDiscards_Type = Counter32
_VrPpTbseOutFilterDiscards_Object = MibTableColumn
vrPpTbseOutFilterDiscards = _VrPpTbseOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 11, 19, 1, 5),
    _VrPpTbseOutFilterDiscards_Type()
)
vrPpTbseOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbseOutFilterDiscards.setStatus("mandatory")
_VrPpSrsg_ObjectIdentity = ObjectIdentity
vrPpSrsg = _VrPpSrsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12)
)
_VrPpSrsgRowStatusTable_Object = MibTable
vrPpSrsgRowStatusTable = _VrPpSrsgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 1)
)
if mibBuilder.loadTexts:
    vrPpSrsgRowStatusTable.setStatus("mandatory")
_VrPpSrsgRowStatusEntry_Object = MibTableRow
vrPpSrsgRowStatusEntry = _VrPpSrsgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 1, 1)
)
vrPpSrsgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgRowStatusEntry.setStatus("mandatory")
_VrPpSrsgRowStatus_Type = RowStatus
_VrPpSrsgRowStatus_Object = MibTableColumn
vrPpSrsgRowStatus = _VrPpSrsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 1, 1, 1),
    _VrPpSrsgRowStatus_Type()
)
vrPpSrsgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgRowStatus.setStatus("mandatory")
_VrPpSrsgComponentName_Type = DisplayString
_VrPpSrsgComponentName_Object = MibTableColumn
vrPpSrsgComponentName = _VrPpSrsgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 1, 1, 2),
    _VrPpSrsgComponentName_Type()
)
vrPpSrsgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgComponentName.setStatus("mandatory")
_VrPpSrsgStorageType_Type = StorageType
_VrPpSrsgStorageType_Object = MibTableColumn
vrPpSrsgStorageType = _VrPpSrsgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 1, 1, 4),
    _VrPpSrsgStorageType_Type()
)
vrPpSrsgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgStorageType.setStatus("mandatory")
_VrPpSrsgIndex_Type = NonReplicated
_VrPpSrsgIndex_Object = MibTableColumn
vrPpSrsgIndex = _VrPpSrsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 1, 1, 10),
    _VrPpSrsgIndex_Type()
)
vrPpSrsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrsgIndex.setStatus("mandatory")
_VrPpSrsgProvTable_Object = MibTable
vrPpSrsgProvTable = _VrPpSrsgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10)
)
if mibBuilder.loadTexts:
    vrPpSrsgProvTable.setStatus("mandatory")
_VrPpSrsgProvEntry_Object = MibTableRow
vrPpSrsgProvEntry = _VrPpSrsgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1)
)
vrPpSrsgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgProvEntry.setStatus("mandatory")


class _VrPpSrsgTranslateIpx_Type(Integer32):
    """Custom type vrPpSrsgTranslateIpx based on Integer32"""
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


_VrPpSrsgTranslateIpx_Type.__name__ = "Integer32"
_VrPpSrsgTranslateIpx_Object = MibTableColumn
vrPpSrsgTranslateIpx = _VrPpSrsgTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1, 1),
    _VrPpSrsgTranslateIpx_Type()
)
vrPpSrsgTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgTranslateIpx.setStatus("mandatory")


class _VrPpSrsgFragmentIp_Type(Integer32):
    """Custom type vrPpSrsgFragmentIp based on Integer32"""
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


_VrPpSrsgFragmentIp_Type.__name__ = "Integer32"
_VrPpSrsgFragmentIp_Object = MibTableColumn
vrPpSrsgFragmentIp = _VrPpSrsgFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1, 2),
    _VrPpSrsgFragmentIp_Type()
)
vrPpSrsgFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgFragmentIp.setStatus("mandatory")


class _VrPpSrsgServiceClass_Type(Integer32):
    """Custom type vrPpSrsgServiceClass based on Integer32"""
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


_VrPpSrsgServiceClass_Type.__name__ = "Integer32"
_VrPpSrsgServiceClass_Object = MibTableColumn
vrPpSrsgServiceClass = _VrPpSrsgServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1, 3),
    _VrPpSrsgServiceClass_Type()
)
vrPpSrsgServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgServiceClass.setStatus("mandatory")


class _VrPpSrsgConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpSrsgConvertArpMacAddress based on Integer32"""
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


_VrPpSrsgConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpSrsgConvertArpMacAddress_Object = MibTableColumn
vrPpSrsgConvertArpMacAddress = _VrPpSrsgConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1, 4),
    _VrPpSrsgConvertArpMacAddress_Type()
)
vrPpSrsgConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgConvertArpMacAddress.setStatus("mandatory")


class _VrPpSrsgPortNum_Type(Unsigned32):
    """Custom type vrPpSrsgPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpSrsgPortNum_Type.__name__ = "Unsigned32"
_VrPpSrsgPortNum_Object = MibTableColumn
vrPpSrsgPortNum = _VrPpSrsgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1, 5),
    _VrPpSrsgPortNum_Type()
)
vrPpSrsgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgPortNum.setStatus("mandatory")


class _VrPpSrsgOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpSrsgOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpSrsgOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpSrsgOutboundFrameMediaType_Object = MibTableColumn
vrPpSrsgOutboundFrameMediaType = _VrPpSrsgOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 10, 1, 6),
    _VrPpSrsgOutboundFrameMediaType_Type()
)
vrPpSrsgOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgOutboundFrameMediaType.setStatus("mandatory")
_VrPpSrsgStpProvTable_Object = MibTable
vrPpSrsgStpProvTable = _VrPpSrsgStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12)
)
if mibBuilder.loadTexts:
    vrPpSrsgStpProvTable.setStatus("mandatory")
_VrPpSrsgStpProvEntry_Object = MibTableRow
vrPpSrsgStpProvEntry = _VrPpSrsgStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1)
)
vrPpSrsgStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgStpProvEntry.setStatus("mandatory")


class _VrPpSrsgAdminStatus_Type(Integer32):
    """Custom type vrPpSrsgAdminStatus based on Integer32"""
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


_VrPpSrsgAdminStatus_Type.__name__ = "Integer32"
_VrPpSrsgAdminStatus_Object = MibTableColumn
vrPpSrsgAdminStatus = _VrPpSrsgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1, 1),
    _VrPpSrsgAdminStatus_Type()
)
vrPpSrsgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgAdminStatus.setStatus("mandatory")


class _VrPpSrsgPortStateStpControl_Type(Integer32):
    """Custom type vrPpSrsgPortStateStpControl based on Integer32"""
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


_VrPpSrsgPortStateStpControl_Type.__name__ = "Integer32"
_VrPpSrsgPortStateStpControl_Object = MibTableColumn
vrPpSrsgPortStateStpControl = _VrPpSrsgPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1, 2),
    _VrPpSrsgPortStateStpControl_Type()
)
vrPpSrsgPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgPortStateStpControl.setStatus("mandatory")


class _VrPpSrsgStpTypeProv_Type(Integer32):
    """Custom type vrPpSrsgStpTypeProv based on Integer32"""
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


_VrPpSrsgStpTypeProv_Type.__name__ = "Integer32"
_VrPpSrsgStpTypeProv_Object = MibTableColumn
vrPpSrsgStpTypeProv = _VrPpSrsgStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1, 3),
    _VrPpSrsgStpTypeProv_Type()
)
vrPpSrsgStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgStpTypeProv.setStatus("mandatory")


class _VrPpSrsgPortPriority_Type(Unsigned32):
    """Custom type vrPpSrsgPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrsgPortPriority_Type.__name__ = "Unsigned32"
_VrPpSrsgPortPriority_Object = MibTableColumn
vrPpSrsgPortPriority = _VrPpSrsgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1, 4),
    _VrPpSrsgPortPriority_Type()
)
vrPpSrsgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgPortPriority.setStatus("mandatory")


class _VrPpSrsgPathCost_Type(Unsigned32):
    """Custom type vrPpSrsgPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrsgPathCost_Type.__name__ = "Unsigned32"
_VrPpSrsgPathCost_Object = MibTableColumn
vrPpSrsgPathCost = _VrPpSrsgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1, 5),
    _VrPpSrsgPathCost_Type()
)
vrPpSrsgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgPathCost.setStatus("mandatory")


class _VrPpSrsgPathCostMethod_Type(Integer32):
    """Custom type vrPpSrsgPathCostMethod based on Integer32"""
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


_VrPpSrsgPathCostMethod_Type.__name__ = "Integer32"
_VrPpSrsgPathCostMethod_Object = MibTableColumn
vrPpSrsgPathCostMethod = _VrPpSrsgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 12, 1, 6),
    _VrPpSrsgPathCostMethod_Type()
)
vrPpSrsgPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgPathCostMethod.setStatus("mandatory")
_VrPpSrsgDIProvTable_Object = MibTable
vrPpSrsgDIProvTable = _VrPpSrsgDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 13)
)
if mibBuilder.loadTexts:
    vrPpSrsgDIProvTable.setStatus("mandatory")
_VrPpSrsgDIProvEntry_Object = MibTableRow
vrPpSrsgDIProvEntry = _VrPpSrsgDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 13, 1)
)
vrPpSrsgDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgDIProvEntry.setStatus("mandatory")


class _VrPpSrsgDomainNum_Type(Unsigned32):
    """Custom type vrPpSrsgDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpSrsgDomainNum_Type.__name__ = "Unsigned32"
_VrPpSrsgDomainNum_Object = MibTableColumn
vrPpSrsgDomainNum = _VrPpSrsgDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 13, 1, 1),
    _VrPpSrsgDomainNum_Type()
)
vrPpSrsgDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgDomainNum.setStatus("mandatory")


class _VrPpSrsgPreserveDomain_Type(Integer32):
    """Custom type vrPpSrsgPreserveDomain based on Integer32"""
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


_VrPpSrsgPreserveDomain_Type.__name__ = "Integer32"
_VrPpSrsgPreserveDomain_Object = MibTableColumn
vrPpSrsgPreserveDomain = _VrPpSrsgPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 13, 1, 2),
    _VrPpSrsgPreserveDomain_Type()
)
vrPpSrsgPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgPreserveDomain.setStatus("mandatory")
_VrPpSrsgStateTable_Object = MibTable
vrPpSrsgStateTable = _VrPpSrsgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 14)
)
if mibBuilder.loadTexts:
    vrPpSrsgStateTable.setStatus("mandatory")
_VrPpSrsgStateEntry_Object = MibTableRow
vrPpSrsgStateEntry = _VrPpSrsgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 14, 1)
)
vrPpSrsgStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgStateEntry.setStatus("mandatory")


class _VrPpSrsgAdminState_Type(Integer32):
    """Custom type vrPpSrsgAdminState based on Integer32"""
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


_VrPpSrsgAdminState_Type.__name__ = "Integer32"
_VrPpSrsgAdminState_Object = MibTableColumn
vrPpSrsgAdminState = _VrPpSrsgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 14, 1, 1),
    _VrPpSrsgAdminState_Type()
)
vrPpSrsgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgAdminState.setStatus("mandatory")


class _VrPpSrsgOperationalState_Type(Integer32):
    """Custom type vrPpSrsgOperationalState based on Integer32"""
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


_VrPpSrsgOperationalState_Type.__name__ = "Integer32"
_VrPpSrsgOperationalState_Object = MibTableColumn
vrPpSrsgOperationalState = _VrPpSrsgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 14, 1, 2),
    _VrPpSrsgOperationalState_Type()
)
vrPpSrsgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgOperationalState.setStatus("mandatory")


class _VrPpSrsgUsageState_Type(Integer32):
    """Custom type vrPpSrsgUsageState based on Integer32"""
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


_VrPpSrsgUsageState_Type.__name__ = "Integer32"
_VrPpSrsgUsageState_Object = MibTableColumn
vrPpSrsgUsageState = _VrPpSrsgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 14, 1, 3),
    _VrPpSrsgUsageState_Type()
)
vrPpSrsgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgUsageState.setStatus("mandatory")
_VrPpSrsgOperStatusTable_Object = MibTable
vrPpSrsgOperStatusTable = _VrPpSrsgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 15)
)
if mibBuilder.loadTexts:
    vrPpSrsgOperStatusTable.setStatus("mandatory")
_VrPpSrsgOperStatusEntry_Object = MibTableRow
vrPpSrsgOperStatusEntry = _VrPpSrsgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 15, 1)
)
vrPpSrsgOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgOperStatusEntry.setStatus("mandatory")


class _VrPpSrsgSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSrsgSnmpOperStatus based on Integer32"""
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


_VrPpSrsgSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSrsgSnmpOperStatus_Object = MibTableColumn
vrPpSrsgSnmpOperStatus = _VrPpSrsgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 15, 1, 1),
    _VrPpSrsgSnmpOperStatus_Type()
)
vrPpSrsgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgSnmpOperStatus.setStatus("mandatory")
_VrPpSrsgOperTable_Object = MibTable
vrPpSrsgOperTable = _VrPpSrsgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16)
)
if mibBuilder.loadTexts:
    vrPpSrsgOperTable.setStatus("mandatory")
_VrPpSrsgOperEntry_Object = MibTableRow
vrPpSrsgOperEntry = _VrPpSrsgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1)
)
vrPpSrsgOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgOperEntry.setStatus("mandatory")


class _VrPpSrsgPortName_Type(AsciiString):
    """Custom type vrPpSrsgPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpSrsgPortName_Type.__name__ = "AsciiString"
_VrPpSrsgPortName_Object = MibTableColumn
vrPpSrsgPortName = _VrPpSrsgPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 1),
    _VrPpSrsgPortName_Type()
)
vrPpSrsgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgPortName.setStatus("mandatory")


class _VrPpSrsgUpTime_Type(Unsigned32):
    """Custom type vrPpSrsgUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrsgUpTime_Type.__name__ = "Unsigned32"
_VrPpSrsgUpTime_Object = MibTableColumn
vrPpSrsgUpTime = _VrPpSrsgUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 3),
    _VrPpSrsgUpTime_Type()
)
vrPpSrsgUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgUpTime.setStatus("mandatory")


class _VrPpSrsgDownTime_Type(Unsigned32):
    """Custom type vrPpSrsgDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrsgDownTime_Type.__name__ = "Unsigned32"
_VrPpSrsgDownTime_Object = MibTableColumn
vrPpSrsgDownTime = _VrPpSrsgDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 4),
    _VrPpSrsgDownTime_Type()
)
vrPpSrsgDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDownTime.setStatus("mandatory")


class _VrPpSrsgBridgingMode_Type(Integer32):
    """Custom type vrPpSrsgBridgingMode based on Integer32"""
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


_VrPpSrsgBridgingMode_Type.__name__ = "Integer32"
_VrPpSrsgBridgingMode_Object = MibTableColumn
vrPpSrsgBridgingMode = _VrPpSrsgBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 5),
    _VrPpSrsgBridgingMode_Type()
)
vrPpSrsgBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgBridgingMode.setStatus("mandatory")


class _VrPpSrsgBridgePortConfig_Type(Integer32):
    """Custom type vrPpSrsgBridgePortConfig based on Integer32"""
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


_VrPpSrsgBridgePortConfig_Type.__name__ = "Integer32"
_VrPpSrsgBridgePortConfig_Object = MibTableColumn
vrPpSrsgBridgePortConfig = _VrPpSrsgBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 6),
    _VrPpSrsgBridgePortConfig_Type()
)
vrPpSrsgBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgBridgePortConfig.setStatus("mandatory")


class _VrPpSrsgBridgePortType_Type(Integer32):
    """Custom type vrPpSrsgBridgePortType based on Integer32"""
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


_VrPpSrsgBridgePortType_Type.__name__ = "Integer32"
_VrPpSrsgBridgePortType_Object = MibTableColumn
vrPpSrsgBridgePortType = _VrPpSrsgBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 7),
    _VrPpSrsgBridgePortType_Type()
)
vrPpSrsgBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgBridgePortType.setStatus("mandatory")


class _VrPpSrsgIfIndex_Type(InterfaceIndex):
    """Custom type vrPpSrsgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrsgIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpSrsgIfIndex_Object = MibTableColumn
vrPpSrsgIfIndex = _VrPpSrsgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 8),
    _VrPpSrsgIfIndex_Type()
)
vrPpSrsgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgIfIndex.setStatus("mandatory")
_VrPpSrsgDelayExceededDiscards_Type = Counter32
_VrPpSrsgDelayExceededDiscards_Object = MibTableColumn
vrPpSrsgDelayExceededDiscards = _VrPpSrsgDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 10),
    _VrPpSrsgDelayExceededDiscards_Type()
)
vrPpSrsgDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDelayExceededDiscards.setStatus("mandatory")
_VrPpSrsgMtuExceededDiscards_Type = Counter32
_VrPpSrsgMtuExceededDiscards_Object = MibTableColumn
vrPpSrsgMtuExceededDiscards = _VrPpSrsgMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 16, 1, 11),
    _VrPpSrsgMtuExceededDiscards_Type()
)
vrPpSrsgMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgMtuExceededDiscards.setStatus("mandatory")
_VrPpSrsgStpOperTable_Object = MibTable
vrPpSrsgStpOperTable = _VrPpSrsgStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18)
)
if mibBuilder.loadTexts:
    vrPpSrsgStpOperTable.setStatus("mandatory")
_VrPpSrsgStpOperEntry_Object = MibTableRow
vrPpSrsgStpOperEntry = _VrPpSrsgStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1)
)
vrPpSrsgStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgStpOperEntry.setStatus("mandatory")


class _VrPpSrsgStpPortState_Type(Integer32):
    """Custom type vrPpSrsgStpPortState based on Integer32"""
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


_VrPpSrsgStpPortState_Type.__name__ = "Integer32"
_VrPpSrsgStpPortState_Object = MibTableColumn
vrPpSrsgStpPortState = _VrPpSrsgStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 2),
    _VrPpSrsgStpPortState_Type()
)
vrPpSrsgStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgStpPortState.setStatus("mandatory")


class _VrPpSrsgStpTypeOper_Type(Integer32):
    """Custom type vrPpSrsgStpTypeOper based on Integer32"""
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


_VrPpSrsgStpTypeOper_Type.__name__ = "Integer32"
_VrPpSrsgStpTypeOper_Object = MibTableColumn
vrPpSrsgStpTypeOper = _VrPpSrsgStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 3),
    _VrPpSrsgStpTypeOper_Type()
)
vrPpSrsgStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgStpTypeOper.setStatus("mandatory")


class _VrPpSrsgDesignatedCost_Type(Unsigned32):
    """Custom type vrPpSrsgDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrsgDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpSrsgDesignatedCost_Object = MibTableColumn
vrPpSrsgDesignatedCost = _VrPpSrsgDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 4),
    _VrPpSrsgDesignatedCost_Type()
)
vrPpSrsgDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDesignatedCost.setStatus("mandatory")


class _VrPpSrsgPathCostOper_Type(Unsigned32):
    """Custom type vrPpSrsgPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrsgPathCostOper_Type.__name__ = "Unsigned32"
_VrPpSrsgPathCostOper_Object = MibTableColumn
vrPpSrsgPathCostOper = _VrPpSrsgPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 5),
    _VrPpSrsgPathCostOper_Type()
)
vrPpSrsgPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgPathCostOper.setStatus("mandatory")


class _VrPpSrsgDesignatedBridge_Type(BridgeId):
    """Custom type vrPpSrsgDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrsgDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpSrsgDesignatedBridge_Object = MibTableColumn
vrPpSrsgDesignatedBridge = _VrPpSrsgDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 6),
    _VrPpSrsgDesignatedBridge_Type()
)
vrPpSrsgDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDesignatedBridge.setStatus("mandatory")


class _VrPpSrsgDesignatedPort_Type(Hex):
    """Custom type vrPpSrsgDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrsgDesignatedPort_Type.__name__ = "Hex"
_VrPpSrsgDesignatedPort_Object = MibTableColumn
vrPpSrsgDesignatedPort = _VrPpSrsgDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 7),
    _VrPpSrsgDesignatedPort_Type()
)
vrPpSrsgDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDesignatedPort.setStatus("mandatory")
_VrPpSrsgForwardTransitions_Type = Counter32
_VrPpSrsgForwardTransitions_Object = MibTableColumn
vrPpSrsgForwardTransitions = _VrPpSrsgForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 8),
    _VrPpSrsgForwardTransitions_Type()
)
vrPpSrsgForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgForwardTransitions.setStatus("mandatory")
_VrPpSrsgBlockingDiscards_Type = Counter32
_VrPpSrsgBlockingDiscards_Object = MibTableColumn
vrPpSrsgBlockingDiscards = _VrPpSrsgBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 9),
    _VrPpSrsgBlockingDiscards_Type()
)
vrPpSrsgBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgBlockingDiscards.setStatus("mandatory")


class _VrPpSrsgDesignatedRoot_Type(BridgeId):
    """Custom type vrPpSrsgDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrsgDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpSrsgDesignatedRoot_Object = MibTableColumn
vrPpSrsgDesignatedRoot = _VrPpSrsgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 18, 1, 10),
    _VrPpSrsgDesignatedRoot_Type()
)
vrPpSrsgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDesignatedRoot.setStatus("mandatory")
_VrPpSrsgStatsTable_Object = MibTable
vrPpSrsgStatsTable = _VrPpSrsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19)
)
if mibBuilder.loadTexts:
    vrPpSrsgStatsTable.setStatus("mandatory")
_VrPpSrsgStatsEntry_Object = MibTableRow
vrPpSrsgStatsEntry = _VrPpSrsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19, 1)
)
vrPpSrsgStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgStatsEntry.setStatus("mandatory")
_VrPpSrsgBadAbstractDiscards_Type = Counter32
_VrPpSrsgBadAbstractDiscards_Object = MibTableColumn
vrPpSrsgBadAbstractDiscards = _VrPpSrsgBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19, 1, 1),
    _VrPpSrsgBadAbstractDiscards_Type()
)
vrPpSrsgBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgBadAbstractDiscards.setStatus("mandatory")
_VrPpSrsgTinygramFramesIn_Type = Counter32
_VrPpSrsgTinygramFramesIn_Object = MibTableColumn
vrPpSrsgTinygramFramesIn = _VrPpSrsgTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19, 1, 2),
    _VrPpSrsgTinygramFramesIn_Type()
)
vrPpSrsgTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgTinygramFramesIn.setStatus("mandatory")
_VrPpSrsgTinygramFramesOut_Type = Counter32
_VrPpSrsgTinygramFramesOut_Object = MibTableColumn
vrPpSrsgTinygramFramesOut = _VrPpSrsgTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19, 1, 3),
    _VrPpSrsgTinygramFramesOut_Type()
)
vrPpSrsgTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgTinygramFramesOut.setStatus("mandatory")
_VrPpSrsgInFilterDiscards_Type = Counter32
_VrPpSrsgInFilterDiscards_Object = MibTableColumn
vrPpSrsgInFilterDiscards = _VrPpSrsgInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19, 1, 4),
    _VrPpSrsgInFilterDiscards_Type()
)
vrPpSrsgInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgInFilterDiscards.setStatus("mandatory")
_VrPpSrsgOutFilterDiscards_Type = Counter32
_VrPpSrsgOutFilterDiscards_Object = MibTableColumn
vrPpSrsgOutFilterDiscards = _VrPpSrsgOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 19, 1, 5),
    _VrPpSrsgOutFilterDiscards_Type()
)
vrPpSrsgOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgOutFilterDiscards.setStatus("mandatory")
_VrPpSrsgSrProvTable_Object = MibTable
vrPpSrsgSrProvTable = _VrPpSrsgSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20)
)
if mibBuilder.loadTexts:
    vrPpSrsgSrProvTable.setStatus("mandatory")
_VrPpSrsgSrProvEntry_Object = MibTableRow
vrPpSrsgSrProvEntry = _VrPpSrsgSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1)
)
vrPpSrsgSrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgSrProvEntry.setStatus("mandatory")


class _VrPpSrsgHopCount_Type(Unsigned32):
    """Custom type vrPpSrsgHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrPpSrsgHopCount_Type.__name__ = "Unsigned32"
_VrPpSrsgHopCount_Object = MibTableColumn
vrPpSrsgHopCount = _VrPpSrsgHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 1),
    _VrPpSrsgHopCount_Type()
)
vrPpSrsgHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgHopCount.setStatus("mandatory")


class _VrPpSrsgExploreFrameTreatment_Type(Integer32):
    """Custom type vrPpSrsgExploreFrameTreatment based on Integer32"""
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


_VrPpSrsgExploreFrameTreatment_Type.__name__ = "Integer32"
_VrPpSrsgExploreFrameTreatment_Object = MibTableColumn
vrPpSrsgExploreFrameTreatment = _VrPpSrsgExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 2),
    _VrPpSrsgExploreFrameTreatment_Type()
)
vrPpSrsgExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgExploreFrameTreatment.setStatus("mandatory")


class _VrPpSrsgLanId_Type(Unsigned32):
    """Custom type vrPpSrsgLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrsgLanId_Type.__name__ = "Unsigned32"
_VrPpSrsgLanId_Object = MibTableColumn
vrPpSrsgLanId = _VrPpSrsgLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 3),
    _VrPpSrsgLanId_Type()
)
vrPpSrsgLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgLanId.setStatus("mandatory")


class _VrPpSrsgInternalLanId_Type(Unsigned32):
    """Custom type vrPpSrsgInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrsgInternalLanId_Type.__name__ = "Unsigned32"
_VrPpSrsgInternalLanId_Object = MibTableColumn
vrPpSrsgInternalLanId = _VrPpSrsgInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 4),
    _VrPpSrsgInternalLanId_Type()
)
vrPpSrsgInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgInternalLanId.setStatus("mandatory")


class _VrPpSrsgBridgeNum_Type(Unsigned32):
    """Custom type vrPpSrsgBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrPpSrsgBridgeNum_Type.__name__ = "Unsigned32"
_VrPpSrsgBridgeNum_Object = MibTableColumn
vrPpSrsgBridgeNum = _VrPpSrsgBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 5),
    _VrPpSrsgBridgeNum_Type()
)
vrPpSrsgBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgBridgeNum.setStatus("mandatory")


class _VrPpSrsgLargestFrame_Type(Unsigned32):
    """Custom type vrPpSrsgLargestFrame based on Unsigned32"""
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


_VrPpSrsgLargestFrame_Type.__name__ = "Unsigned32"
_VrPpSrsgLargestFrame_Object = MibTableColumn
vrPpSrsgLargestFrame = _VrPpSrsgLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 6),
    _VrPpSrsgLargestFrame_Type()
)
vrPpSrsgLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgLargestFrame.setStatus("mandatory")


class _VrPpSrsgSteSpanMode_Type(Integer32):
    """Custom type vrPpSrsgSteSpanMode based on Integer32"""
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


_VrPpSrsgSteSpanMode_Type.__name__ = "Integer32"
_VrPpSrsgSteSpanMode_Object = MibTableColumn
vrPpSrsgSteSpanMode = _VrPpSrsgSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 7),
    _VrPpSrsgSteSpanMode_Type()
)
vrPpSrsgSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgSteSpanMode.setStatus("mandatory")


class _VrPpSrsgAreRdLimit_Type(Unsigned32):
    """Custom type vrPpSrsgAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrsgAreRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrsgAreRdLimit_Object = MibTableColumn
vrPpSrsgAreRdLimit = _VrPpSrsgAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 8),
    _VrPpSrsgAreRdLimit_Type()
)
vrPpSrsgAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgAreRdLimit.setStatus("mandatory")


class _VrPpSrsgSteRdLimit_Type(Unsigned32):
    """Custom type vrPpSrsgSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrsgSteRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrsgSteRdLimit_Object = MibTableColumn
vrPpSrsgSteRdLimit = _VrPpSrsgSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 20, 1, 9),
    _VrPpSrsgSteRdLimit_Type()
)
vrPpSrsgSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrsgSteRdLimit.setStatus("mandatory")
_VrPpSrsgSrStatsTable_Object = MibTable
vrPpSrsgSrStatsTable = _VrPpSrsgSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21)
)
if mibBuilder.loadTexts:
    vrPpSrsgSrStatsTable.setStatus("mandatory")
_VrPpSrsgSrStatsEntry_Object = MibTableRow
vrPpSrsgSrStatsEntry = _VrPpSrsgSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1)
)
vrPpSrsgSrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrsgSrStatsEntry.setStatus("mandatory")
_VrPpSrsgSpecInFrames_Type = Counter32
_VrPpSrsgSpecInFrames_Object = MibTableColumn
vrPpSrsgSpecInFrames = _VrPpSrsgSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 1),
    _VrPpSrsgSpecInFrames_Type()
)
vrPpSrsgSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgSpecInFrames.setStatus("mandatory")
_VrPpSrsgSpecOutFrames_Type = Counter32
_VrPpSrsgSpecOutFrames_Object = MibTableColumn
vrPpSrsgSpecOutFrames = _VrPpSrsgSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 2),
    _VrPpSrsgSpecOutFrames_Type()
)
vrPpSrsgSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgSpecOutFrames.setStatus("mandatory")
_VrPpSrsgApeInFrames_Type = Counter32
_VrPpSrsgApeInFrames_Object = MibTableColumn
vrPpSrsgApeInFrames = _VrPpSrsgApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 3),
    _VrPpSrsgApeInFrames_Type()
)
vrPpSrsgApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgApeInFrames.setStatus("mandatory")
_VrPpSrsgApeOutFrames_Type = Counter32
_VrPpSrsgApeOutFrames_Object = MibTableColumn
vrPpSrsgApeOutFrames = _VrPpSrsgApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 4),
    _VrPpSrsgApeOutFrames_Type()
)
vrPpSrsgApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgApeOutFrames.setStatus("mandatory")
_VrPpSrsgSteInFrames_Type = Counter32
_VrPpSrsgSteInFrames_Object = MibTableColumn
vrPpSrsgSteInFrames = _VrPpSrsgSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 5),
    _VrPpSrsgSteInFrames_Type()
)
vrPpSrsgSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgSteInFrames.setStatus("mandatory")
_VrPpSrsgSteOutFrames_Type = Counter32
_VrPpSrsgSteOutFrames_Object = MibTableColumn
vrPpSrsgSteOutFrames = _VrPpSrsgSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 6),
    _VrPpSrsgSteOutFrames_Type()
)
vrPpSrsgSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgSteOutFrames.setStatus("mandatory")
_VrPpSrsgSegmentMismatchDiscards_Type = Counter32
_VrPpSrsgSegmentMismatchDiscards_Object = MibTableColumn
vrPpSrsgSegmentMismatchDiscards = _VrPpSrsgSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 7),
    _VrPpSrsgSegmentMismatchDiscards_Type()
)
vrPpSrsgSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgSegmentMismatchDiscards.setStatus("mandatory")
_VrPpSrsgDupSegmentDiscards_Type = Counter32
_VrPpSrsgDupSegmentDiscards_Object = MibTableColumn
vrPpSrsgDupSegmentDiscards = _VrPpSrsgDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 8),
    _VrPpSrsgDupSegmentDiscards_Type()
)
vrPpSrsgDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDupSegmentDiscards.setStatus("mandatory")
_VrPpSrsgHopCountExceededDiscards_Type = Counter32
_VrPpSrsgHopCountExceededDiscards_Object = MibTableColumn
vrPpSrsgHopCountExceededDiscards = _VrPpSrsgHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 9),
    _VrPpSrsgHopCountExceededDiscards_Type()
)
vrPpSrsgHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgHopCountExceededDiscards.setStatus("mandatory")
_VrPpSrsgDupLanIdOrTreeErrors_Type = Counter32
_VrPpSrsgDupLanIdOrTreeErrors_Object = MibTableColumn
vrPpSrsgDupLanIdOrTreeErrors = _VrPpSrsgDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 10),
    _VrPpSrsgDupLanIdOrTreeErrors_Type()
)
vrPpSrsgDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDupLanIdOrTreeErrors.setStatus("mandatory")
_VrPpSrsgLanIdMismatches_Type = Counter32
_VrPpSrsgLanIdMismatches_Object = MibTableColumn
vrPpSrsgLanIdMismatches = _VrPpSrsgLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 11),
    _VrPpSrsgLanIdMismatches_Type()
)
vrPpSrsgLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgLanIdMismatches.setStatus("mandatory")
_VrPpSrsgStaticDiscards_Type = Counter32
_VrPpSrsgStaticDiscards_Object = MibTableColumn
vrPpSrsgStaticDiscards = _VrPpSrsgStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 12),
    _VrPpSrsgStaticDiscards_Type()
)
vrPpSrsgStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgStaticDiscards.setStatus("mandatory")
_VrPpSrsgDynamicDiscards_Type = Counter32
_VrPpSrsgDynamicDiscards_Object = MibTableColumn
vrPpSrsgDynamicDiscards = _VrPpSrsgDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 12, 21, 1, 13),
    _VrPpSrsgDynamicDiscards_Type()
)
vrPpSrsgDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrsgDynamicDiscards.setStatus("mandatory")
_VrPpTbsg_ObjectIdentity = ObjectIdentity
vrPpTbsg = _VrPpTbsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13)
)
_VrPpTbsgRowStatusTable_Object = MibTable
vrPpTbsgRowStatusTable = _VrPpTbsgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 1)
)
if mibBuilder.loadTexts:
    vrPpTbsgRowStatusTable.setStatus("mandatory")
_VrPpTbsgRowStatusEntry_Object = MibTableRow
vrPpTbsgRowStatusEntry = _VrPpTbsgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 1, 1)
)
vrPpTbsgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgRowStatusEntry.setStatus("mandatory")
_VrPpTbsgRowStatus_Type = RowStatus
_VrPpTbsgRowStatus_Object = MibTableColumn
vrPpTbsgRowStatus = _VrPpTbsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 1, 1, 1),
    _VrPpTbsgRowStatus_Type()
)
vrPpTbsgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgRowStatus.setStatus("mandatory")
_VrPpTbsgComponentName_Type = DisplayString
_VrPpTbsgComponentName_Object = MibTableColumn
vrPpTbsgComponentName = _VrPpTbsgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 1, 1, 2),
    _VrPpTbsgComponentName_Type()
)
vrPpTbsgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgComponentName.setStatus("mandatory")
_VrPpTbsgStorageType_Type = StorageType
_VrPpTbsgStorageType_Object = MibTableColumn
vrPpTbsgStorageType = _VrPpTbsgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 1, 1, 4),
    _VrPpTbsgStorageType_Type()
)
vrPpTbsgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgStorageType.setStatus("mandatory")
_VrPpTbsgIndex_Type = NonReplicated
_VrPpTbsgIndex_Object = MibTableColumn
vrPpTbsgIndex = _VrPpTbsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 1, 1, 10),
    _VrPpTbsgIndex_Type()
)
vrPpTbsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpTbsgIndex.setStatus("mandatory")
_VrPpTbsgProvTable_Object = MibTable
vrPpTbsgProvTable = _VrPpTbsgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10)
)
if mibBuilder.loadTexts:
    vrPpTbsgProvTable.setStatus("mandatory")
_VrPpTbsgProvEntry_Object = MibTableRow
vrPpTbsgProvEntry = _VrPpTbsgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1)
)
vrPpTbsgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgProvEntry.setStatus("mandatory")


class _VrPpTbsgTranslateIpx_Type(Integer32):
    """Custom type vrPpTbsgTranslateIpx based on Integer32"""
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


_VrPpTbsgTranslateIpx_Type.__name__ = "Integer32"
_VrPpTbsgTranslateIpx_Object = MibTableColumn
vrPpTbsgTranslateIpx = _VrPpTbsgTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1, 1),
    _VrPpTbsgTranslateIpx_Type()
)
vrPpTbsgTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgTranslateIpx.setStatus("mandatory")


class _VrPpTbsgFragmentIp_Type(Integer32):
    """Custom type vrPpTbsgFragmentIp based on Integer32"""
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


_VrPpTbsgFragmentIp_Type.__name__ = "Integer32"
_VrPpTbsgFragmentIp_Object = MibTableColumn
vrPpTbsgFragmentIp = _VrPpTbsgFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1, 2),
    _VrPpTbsgFragmentIp_Type()
)
vrPpTbsgFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgFragmentIp.setStatus("mandatory")


class _VrPpTbsgServiceClass_Type(Integer32):
    """Custom type vrPpTbsgServiceClass based on Integer32"""
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


_VrPpTbsgServiceClass_Type.__name__ = "Integer32"
_VrPpTbsgServiceClass_Object = MibTableColumn
vrPpTbsgServiceClass = _VrPpTbsgServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1, 3),
    _VrPpTbsgServiceClass_Type()
)
vrPpTbsgServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgServiceClass.setStatus("mandatory")


class _VrPpTbsgConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpTbsgConvertArpMacAddress based on Integer32"""
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


_VrPpTbsgConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpTbsgConvertArpMacAddress_Object = MibTableColumn
vrPpTbsgConvertArpMacAddress = _VrPpTbsgConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1, 4),
    _VrPpTbsgConvertArpMacAddress_Type()
)
vrPpTbsgConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgConvertArpMacAddress.setStatus("mandatory")


class _VrPpTbsgPortNum_Type(Unsigned32):
    """Custom type vrPpTbsgPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpTbsgPortNum_Type.__name__ = "Unsigned32"
_VrPpTbsgPortNum_Object = MibTableColumn
vrPpTbsgPortNum = _VrPpTbsgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1, 5),
    _VrPpTbsgPortNum_Type()
)
vrPpTbsgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgPortNum.setStatus("mandatory")


class _VrPpTbsgOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpTbsgOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpTbsgOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpTbsgOutboundFrameMediaType_Object = MibTableColumn
vrPpTbsgOutboundFrameMediaType = _VrPpTbsgOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 10, 1, 6),
    _VrPpTbsgOutboundFrameMediaType_Type()
)
vrPpTbsgOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgOutboundFrameMediaType.setStatus("mandatory")
_VrPpTbsgTbProvTable_Object = MibTable
vrPpTbsgTbProvTable = _VrPpTbsgTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 11)
)
if mibBuilder.loadTexts:
    vrPpTbsgTbProvTable.setStatus("mandatory")
_VrPpTbsgTbProvEntry_Object = MibTableRow
vrPpTbsgTbProvEntry = _VrPpTbsgTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 11, 1)
)
vrPpTbsgTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgTbProvEntry.setStatus("mandatory")


class _VrPpTbsgSecureOption_Type(Integer32):
    """Custom type vrPpTbsgSecureOption based on Integer32"""
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


_VrPpTbsgSecureOption_Type.__name__ = "Integer32"
_VrPpTbsgSecureOption_Object = MibTableColumn
vrPpTbsgSecureOption = _VrPpTbsgSecureOption_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 11, 1, 1),
    _VrPpTbsgSecureOption_Type()
)
vrPpTbsgSecureOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgSecureOption.setStatus("mandatory")
_VrPpTbsgStpProvTable_Object = MibTable
vrPpTbsgStpProvTable = _VrPpTbsgStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12)
)
if mibBuilder.loadTexts:
    vrPpTbsgStpProvTable.setStatus("mandatory")
_VrPpTbsgStpProvEntry_Object = MibTableRow
vrPpTbsgStpProvEntry = _VrPpTbsgStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1)
)
vrPpTbsgStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgStpProvEntry.setStatus("mandatory")


class _VrPpTbsgAdminStatus_Type(Integer32):
    """Custom type vrPpTbsgAdminStatus based on Integer32"""
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


_VrPpTbsgAdminStatus_Type.__name__ = "Integer32"
_VrPpTbsgAdminStatus_Object = MibTableColumn
vrPpTbsgAdminStatus = _VrPpTbsgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1, 1),
    _VrPpTbsgAdminStatus_Type()
)
vrPpTbsgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgAdminStatus.setStatus("mandatory")


class _VrPpTbsgPortStateStpControl_Type(Integer32):
    """Custom type vrPpTbsgPortStateStpControl based on Integer32"""
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


_VrPpTbsgPortStateStpControl_Type.__name__ = "Integer32"
_VrPpTbsgPortStateStpControl_Object = MibTableColumn
vrPpTbsgPortStateStpControl = _VrPpTbsgPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1, 2),
    _VrPpTbsgPortStateStpControl_Type()
)
vrPpTbsgPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgPortStateStpControl.setStatus("mandatory")


class _VrPpTbsgStpTypeProv_Type(Integer32):
    """Custom type vrPpTbsgStpTypeProv based on Integer32"""
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


_VrPpTbsgStpTypeProv_Type.__name__ = "Integer32"
_VrPpTbsgStpTypeProv_Object = MibTableColumn
vrPpTbsgStpTypeProv = _VrPpTbsgStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1, 3),
    _VrPpTbsgStpTypeProv_Type()
)
vrPpTbsgStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgStpTypeProv.setStatus("mandatory")


class _VrPpTbsgPortPriority_Type(Unsigned32):
    """Custom type vrPpTbsgPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbsgPortPriority_Type.__name__ = "Unsigned32"
_VrPpTbsgPortPriority_Object = MibTableColumn
vrPpTbsgPortPriority = _VrPpTbsgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1, 4),
    _VrPpTbsgPortPriority_Type()
)
vrPpTbsgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgPortPriority.setStatus("mandatory")


class _VrPpTbsgPathCost_Type(Unsigned32):
    """Custom type vrPpTbsgPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbsgPathCost_Type.__name__ = "Unsigned32"
_VrPpTbsgPathCost_Object = MibTableColumn
vrPpTbsgPathCost = _VrPpTbsgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1, 5),
    _VrPpTbsgPathCost_Type()
)
vrPpTbsgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgPathCost.setStatus("mandatory")


class _VrPpTbsgPathCostMethod_Type(Integer32):
    """Custom type vrPpTbsgPathCostMethod based on Integer32"""
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


_VrPpTbsgPathCostMethod_Type.__name__ = "Integer32"
_VrPpTbsgPathCostMethod_Object = MibTableColumn
vrPpTbsgPathCostMethod = _VrPpTbsgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 12, 1, 6),
    _VrPpTbsgPathCostMethod_Type()
)
vrPpTbsgPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgPathCostMethod.setStatus("mandatory")
_VrPpTbsgDIProvTable_Object = MibTable
vrPpTbsgDIProvTable = _VrPpTbsgDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 13)
)
if mibBuilder.loadTexts:
    vrPpTbsgDIProvTable.setStatus("mandatory")
_VrPpTbsgDIProvEntry_Object = MibTableRow
vrPpTbsgDIProvEntry = _VrPpTbsgDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 13, 1)
)
vrPpTbsgDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgDIProvEntry.setStatus("mandatory")


class _VrPpTbsgDomainNum_Type(Unsigned32):
    """Custom type vrPpTbsgDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpTbsgDomainNum_Type.__name__ = "Unsigned32"
_VrPpTbsgDomainNum_Object = MibTableColumn
vrPpTbsgDomainNum = _VrPpTbsgDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 13, 1, 1),
    _VrPpTbsgDomainNum_Type()
)
vrPpTbsgDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgDomainNum.setStatus("mandatory")


class _VrPpTbsgPreserveDomain_Type(Integer32):
    """Custom type vrPpTbsgPreserveDomain based on Integer32"""
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


_VrPpTbsgPreserveDomain_Type.__name__ = "Integer32"
_VrPpTbsgPreserveDomain_Object = MibTableColumn
vrPpTbsgPreserveDomain = _VrPpTbsgPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 13, 1, 2),
    _VrPpTbsgPreserveDomain_Type()
)
vrPpTbsgPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpTbsgPreserveDomain.setStatus("mandatory")
_VrPpTbsgStateTable_Object = MibTable
vrPpTbsgStateTable = _VrPpTbsgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 14)
)
if mibBuilder.loadTexts:
    vrPpTbsgStateTable.setStatus("mandatory")
_VrPpTbsgStateEntry_Object = MibTableRow
vrPpTbsgStateEntry = _VrPpTbsgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 14, 1)
)
vrPpTbsgStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgStateEntry.setStatus("mandatory")


class _VrPpTbsgAdminState_Type(Integer32):
    """Custom type vrPpTbsgAdminState based on Integer32"""
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


_VrPpTbsgAdminState_Type.__name__ = "Integer32"
_VrPpTbsgAdminState_Object = MibTableColumn
vrPpTbsgAdminState = _VrPpTbsgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 14, 1, 1),
    _VrPpTbsgAdminState_Type()
)
vrPpTbsgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgAdminState.setStatus("mandatory")


class _VrPpTbsgOperationalState_Type(Integer32):
    """Custom type vrPpTbsgOperationalState based on Integer32"""
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


_VrPpTbsgOperationalState_Type.__name__ = "Integer32"
_VrPpTbsgOperationalState_Object = MibTableColumn
vrPpTbsgOperationalState = _VrPpTbsgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 14, 1, 2),
    _VrPpTbsgOperationalState_Type()
)
vrPpTbsgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgOperationalState.setStatus("mandatory")


class _VrPpTbsgUsageState_Type(Integer32):
    """Custom type vrPpTbsgUsageState based on Integer32"""
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


_VrPpTbsgUsageState_Type.__name__ = "Integer32"
_VrPpTbsgUsageState_Object = MibTableColumn
vrPpTbsgUsageState = _VrPpTbsgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 14, 1, 3),
    _VrPpTbsgUsageState_Type()
)
vrPpTbsgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgUsageState.setStatus("mandatory")
_VrPpTbsgOperStatusTable_Object = MibTable
vrPpTbsgOperStatusTable = _VrPpTbsgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 15)
)
if mibBuilder.loadTexts:
    vrPpTbsgOperStatusTable.setStatus("mandatory")
_VrPpTbsgOperStatusEntry_Object = MibTableRow
vrPpTbsgOperStatusEntry = _VrPpTbsgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 15, 1)
)
vrPpTbsgOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgOperStatusEntry.setStatus("mandatory")


class _VrPpTbsgSnmpOperStatus_Type(Integer32):
    """Custom type vrPpTbsgSnmpOperStatus based on Integer32"""
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


_VrPpTbsgSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpTbsgSnmpOperStatus_Object = MibTableColumn
vrPpTbsgSnmpOperStatus = _VrPpTbsgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 15, 1, 1),
    _VrPpTbsgSnmpOperStatus_Type()
)
vrPpTbsgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgSnmpOperStatus.setStatus("mandatory")
_VrPpTbsgOperTable_Object = MibTable
vrPpTbsgOperTable = _VrPpTbsgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16)
)
if mibBuilder.loadTexts:
    vrPpTbsgOperTable.setStatus("mandatory")
_VrPpTbsgOperEntry_Object = MibTableRow
vrPpTbsgOperEntry = _VrPpTbsgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1)
)
vrPpTbsgOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgOperEntry.setStatus("mandatory")


class _VrPpTbsgPortName_Type(AsciiString):
    """Custom type vrPpTbsgPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpTbsgPortName_Type.__name__ = "AsciiString"
_VrPpTbsgPortName_Object = MibTableColumn
vrPpTbsgPortName = _VrPpTbsgPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 1),
    _VrPpTbsgPortName_Type()
)
vrPpTbsgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgPortName.setStatus("mandatory")


class _VrPpTbsgUpTime_Type(Unsigned32):
    """Custom type vrPpTbsgUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbsgUpTime_Type.__name__ = "Unsigned32"
_VrPpTbsgUpTime_Object = MibTableColumn
vrPpTbsgUpTime = _VrPpTbsgUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 3),
    _VrPpTbsgUpTime_Type()
)
vrPpTbsgUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgUpTime.setStatus("mandatory")


class _VrPpTbsgDownTime_Type(Unsigned32):
    """Custom type vrPpTbsgDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbsgDownTime_Type.__name__ = "Unsigned32"
_VrPpTbsgDownTime_Object = MibTableColumn
vrPpTbsgDownTime = _VrPpTbsgDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 4),
    _VrPpTbsgDownTime_Type()
)
vrPpTbsgDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDownTime.setStatus("mandatory")


class _VrPpTbsgBridgingMode_Type(Integer32):
    """Custom type vrPpTbsgBridgingMode based on Integer32"""
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


_VrPpTbsgBridgingMode_Type.__name__ = "Integer32"
_VrPpTbsgBridgingMode_Object = MibTableColumn
vrPpTbsgBridgingMode = _VrPpTbsgBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 5),
    _VrPpTbsgBridgingMode_Type()
)
vrPpTbsgBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgBridgingMode.setStatus("mandatory")


class _VrPpTbsgBridgePortConfig_Type(Integer32):
    """Custom type vrPpTbsgBridgePortConfig based on Integer32"""
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


_VrPpTbsgBridgePortConfig_Type.__name__ = "Integer32"
_VrPpTbsgBridgePortConfig_Object = MibTableColumn
vrPpTbsgBridgePortConfig = _VrPpTbsgBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 6),
    _VrPpTbsgBridgePortConfig_Type()
)
vrPpTbsgBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgBridgePortConfig.setStatus("mandatory")


class _VrPpTbsgBridgePortType_Type(Integer32):
    """Custom type vrPpTbsgBridgePortType based on Integer32"""
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


_VrPpTbsgBridgePortType_Type.__name__ = "Integer32"
_VrPpTbsgBridgePortType_Object = MibTableColumn
vrPpTbsgBridgePortType = _VrPpTbsgBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 7),
    _VrPpTbsgBridgePortType_Type()
)
vrPpTbsgBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgBridgePortType.setStatus("mandatory")


class _VrPpTbsgIfIndex_Type(InterfaceIndex):
    """Custom type vrPpTbsgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbsgIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpTbsgIfIndex_Object = MibTableColumn
vrPpTbsgIfIndex = _VrPpTbsgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 8),
    _VrPpTbsgIfIndex_Type()
)
vrPpTbsgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgIfIndex.setStatus("mandatory")
_VrPpTbsgDelayExceededDiscards_Type = Counter32
_VrPpTbsgDelayExceededDiscards_Object = MibTableColumn
vrPpTbsgDelayExceededDiscards = _VrPpTbsgDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 10),
    _VrPpTbsgDelayExceededDiscards_Type()
)
vrPpTbsgDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDelayExceededDiscards.setStatus("mandatory")
_VrPpTbsgMtuExceededDiscards_Type = Counter32
_VrPpTbsgMtuExceededDiscards_Object = MibTableColumn
vrPpTbsgMtuExceededDiscards = _VrPpTbsgMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 16, 1, 11),
    _VrPpTbsgMtuExceededDiscards_Type()
)
vrPpTbsgMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgMtuExceededDiscards.setStatus("mandatory")
_VrPpTbsgTbOperTable_Object = MibTable
vrPpTbsgTbOperTable = _VrPpTbsgTbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17)
)
if mibBuilder.loadTexts:
    vrPpTbsgTbOperTable.setStatus("mandatory")
_VrPpTbsgTbOperEntry_Object = MibTableRow
vrPpTbsgTbOperEntry = _VrPpTbsgTbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1)
)
vrPpTbsgTbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgTbOperEntry.setStatus("mandatory")


class _VrPpTbsgMaxInfo_Type(Unsigned32):
    """Custom type vrPpTbsgMaxInfo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbsgMaxInfo_Type.__name__ = "Unsigned32"
_VrPpTbsgMaxInfo_Object = MibTableColumn
vrPpTbsgMaxInfo = _VrPpTbsgMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 2),
    _VrPpTbsgMaxInfo_Type()
)
vrPpTbsgMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgMaxInfo.setStatus("mandatory")
_VrPpTbsgBadVerifyDiscards_Type = Counter32
_VrPpTbsgBadVerifyDiscards_Object = MibTableColumn
vrPpTbsgBadVerifyDiscards = _VrPpTbsgBadVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 3),
    _VrPpTbsgBadVerifyDiscards_Type()
)
vrPpTbsgBadVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgBadVerifyDiscards.setStatus("mandatory")
_VrPpTbsgUnicastNoMatches_Type = Counter32
_VrPpTbsgUnicastNoMatches_Object = MibTableColumn
vrPpTbsgUnicastNoMatches = _VrPpTbsgUnicastNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 4),
    _VrPpTbsgUnicastNoMatches_Type()
)
vrPpTbsgUnicastNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgUnicastNoMatches.setStatus("mandatory")
_VrPpTbsgStaticEntryDiscards_Type = Counter32
_VrPpTbsgStaticEntryDiscards_Object = MibTableColumn
vrPpTbsgStaticEntryDiscards = _VrPpTbsgStaticEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 5),
    _VrPpTbsgStaticEntryDiscards_Type()
)
vrPpTbsgStaticEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgStaticEntryDiscards.setStatus("mandatory")
_VrPpTbsgDynamicEntryDiscards_Type = Counter32
_VrPpTbsgDynamicEntryDiscards_Object = MibTableColumn
vrPpTbsgDynamicEntryDiscards = _VrPpTbsgDynamicEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 6),
    _VrPpTbsgDynamicEntryDiscards_Type()
)
vrPpTbsgDynamicEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDynamicEntryDiscards.setStatus("mandatory")
_VrPpTbsgLearningDiscards_Type = Counter32
_VrPpTbsgLearningDiscards_Object = MibTableColumn
vrPpTbsgLearningDiscards = _VrPpTbsgLearningDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 7),
    _VrPpTbsgLearningDiscards_Type()
)
vrPpTbsgLearningDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgLearningDiscards.setStatus("mandatory")
_VrPpTbsgInDiscards_Type = Counter32
_VrPpTbsgInDiscards_Object = MibTableColumn
vrPpTbsgInDiscards = _VrPpTbsgInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 8),
    _VrPpTbsgInDiscards_Type()
)
vrPpTbsgInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgInDiscards.setStatus("mandatory")
_VrPpTbsgInFrames_Type = Counter32
_VrPpTbsgInFrames_Object = MibTableColumn
vrPpTbsgInFrames = _VrPpTbsgInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 9),
    _VrPpTbsgInFrames_Type()
)
vrPpTbsgInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgInFrames.setStatus("mandatory")
_VrPpTbsgOutFrames_Type = Counter32
_VrPpTbsgOutFrames_Object = MibTableColumn
vrPpTbsgOutFrames = _VrPpTbsgOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 17, 1, 10),
    _VrPpTbsgOutFrames_Type()
)
vrPpTbsgOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgOutFrames.setStatus("mandatory")
_VrPpTbsgStpOperTable_Object = MibTable
vrPpTbsgStpOperTable = _VrPpTbsgStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18)
)
if mibBuilder.loadTexts:
    vrPpTbsgStpOperTable.setStatus("mandatory")
_VrPpTbsgStpOperEntry_Object = MibTableRow
vrPpTbsgStpOperEntry = _VrPpTbsgStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1)
)
vrPpTbsgStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgStpOperEntry.setStatus("mandatory")


class _VrPpTbsgStpPortState_Type(Integer32):
    """Custom type vrPpTbsgStpPortState based on Integer32"""
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


_VrPpTbsgStpPortState_Type.__name__ = "Integer32"
_VrPpTbsgStpPortState_Object = MibTableColumn
vrPpTbsgStpPortState = _VrPpTbsgStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 2),
    _VrPpTbsgStpPortState_Type()
)
vrPpTbsgStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgStpPortState.setStatus("mandatory")


class _VrPpTbsgStpTypeOper_Type(Integer32):
    """Custom type vrPpTbsgStpTypeOper based on Integer32"""
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


_VrPpTbsgStpTypeOper_Type.__name__ = "Integer32"
_VrPpTbsgStpTypeOper_Object = MibTableColumn
vrPpTbsgStpTypeOper = _VrPpTbsgStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 3),
    _VrPpTbsgStpTypeOper_Type()
)
vrPpTbsgStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgStpTypeOper.setStatus("mandatory")


class _VrPpTbsgDesignatedCost_Type(Unsigned32):
    """Custom type vrPpTbsgDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpTbsgDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpTbsgDesignatedCost_Object = MibTableColumn
vrPpTbsgDesignatedCost = _VrPpTbsgDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 4),
    _VrPpTbsgDesignatedCost_Type()
)
vrPpTbsgDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDesignatedCost.setStatus("mandatory")


class _VrPpTbsgPathCostOper_Type(Unsigned32):
    """Custom type vrPpTbsgPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpTbsgPathCostOper_Type.__name__ = "Unsigned32"
_VrPpTbsgPathCostOper_Object = MibTableColumn
vrPpTbsgPathCostOper = _VrPpTbsgPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 5),
    _VrPpTbsgPathCostOper_Type()
)
vrPpTbsgPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgPathCostOper.setStatus("mandatory")


class _VrPpTbsgDesignatedBridge_Type(BridgeId):
    """Custom type vrPpTbsgDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbsgDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpTbsgDesignatedBridge_Object = MibTableColumn
vrPpTbsgDesignatedBridge = _VrPpTbsgDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 6),
    _VrPpTbsgDesignatedBridge_Type()
)
vrPpTbsgDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDesignatedBridge.setStatus("mandatory")


class _VrPpTbsgDesignatedPort_Type(Hex):
    """Custom type vrPpTbsgDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpTbsgDesignatedPort_Type.__name__ = "Hex"
_VrPpTbsgDesignatedPort_Object = MibTableColumn
vrPpTbsgDesignatedPort = _VrPpTbsgDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 7),
    _VrPpTbsgDesignatedPort_Type()
)
vrPpTbsgDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDesignatedPort.setStatus("mandatory")
_VrPpTbsgForwardTransitions_Type = Counter32
_VrPpTbsgForwardTransitions_Object = MibTableColumn
vrPpTbsgForwardTransitions = _VrPpTbsgForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 8),
    _VrPpTbsgForwardTransitions_Type()
)
vrPpTbsgForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgForwardTransitions.setStatus("mandatory")
_VrPpTbsgBlockingDiscards_Type = Counter32
_VrPpTbsgBlockingDiscards_Object = MibTableColumn
vrPpTbsgBlockingDiscards = _VrPpTbsgBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 9),
    _VrPpTbsgBlockingDiscards_Type()
)
vrPpTbsgBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgBlockingDiscards.setStatus("mandatory")


class _VrPpTbsgDesignatedRoot_Type(BridgeId):
    """Custom type vrPpTbsgDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpTbsgDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpTbsgDesignatedRoot_Object = MibTableColumn
vrPpTbsgDesignatedRoot = _VrPpTbsgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 18, 1, 10),
    _VrPpTbsgDesignatedRoot_Type()
)
vrPpTbsgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgDesignatedRoot.setStatus("mandatory")
_VrPpTbsgStatsTable_Object = MibTable
vrPpTbsgStatsTable = _VrPpTbsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19)
)
if mibBuilder.loadTexts:
    vrPpTbsgStatsTable.setStatus("mandatory")
_VrPpTbsgStatsEntry_Object = MibTableRow
vrPpTbsgStatsEntry = _VrPpTbsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19, 1)
)
vrPpTbsgStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpTbsgIndex"),
)
if mibBuilder.loadTexts:
    vrPpTbsgStatsEntry.setStatus("mandatory")
_VrPpTbsgBadAbstractDiscards_Type = Counter32
_VrPpTbsgBadAbstractDiscards_Object = MibTableColumn
vrPpTbsgBadAbstractDiscards = _VrPpTbsgBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19, 1, 1),
    _VrPpTbsgBadAbstractDiscards_Type()
)
vrPpTbsgBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgBadAbstractDiscards.setStatus("mandatory")
_VrPpTbsgTinygramFramesIn_Type = Counter32
_VrPpTbsgTinygramFramesIn_Object = MibTableColumn
vrPpTbsgTinygramFramesIn = _VrPpTbsgTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19, 1, 2),
    _VrPpTbsgTinygramFramesIn_Type()
)
vrPpTbsgTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgTinygramFramesIn.setStatus("mandatory")
_VrPpTbsgTinygramFramesOut_Type = Counter32
_VrPpTbsgTinygramFramesOut_Object = MibTableColumn
vrPpTbsgTinygramFramesOut = _VrPpTbsgTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19, 1, 3),
    _VrPpTbsgTinygramFramesOut_Type()
)
vrPpTbsgTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgTinygramFramesOut.setStatus("mandatory")
_VrPpTbsgInFilterDiscards_Type = Counter32
_VrPpTbsgInFilterDiscards_Object = MibTableColumn
vrPpTbsgInFilterDiscards = _VrPpTbsgInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19, 1, 4),
    _VrPpTbsgInFilterDiscards_Type()
)
vrPpTbsgInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgInFilterDiscards.setStatus("mandatory")
_VrPpTbsgOutFilterDiscards_Type = Counter32
_VrPpTbsgOutFilterDiscards_Object = MibTableColumn
vrPpTbsgOutFilterDiscards = _VrPpTbsgOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 13, 19, 1, 5),
    _VrPpTbsgOutFilterDiscards_Type()
)
vrPpTbsgOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpTbsgOutFilterDiscards.setStatus("mandatory")
_VrPpSrcl_ObjectIdentity = ObjectIdentity
vrPpSrcl = _VrPpSrcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14)
)
_VrPpSrclRowStatusTable_Object = MibTable
vrPpSrclRowStatusTable = _VrPpSrclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 1)
)
if mibBuilder.loadTexts:
    vrPpSrclRowStatusTable.setStatus("mandatory")
_VrPpSrclRowStatusEntry_Object = MibTableRow
vrPpSrclRowStatusEntry = _VrPpSrclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 1, 1)
)
vrPpSrclRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclRowStatusEntry.setStatus("mandatory")
_VrPpSrclRowStatus_Type = RowStatus
_VrPpSrclRowStatus_Object = MibTableColumn
vrPpSrclRowStatus = _VrPpSrclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 1, 1, 1),
    _VrPpSrclRowStatus_Type()
)
vrPpSrclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclRowStatus.setStatus("mandatory")
_VrPpSrclComponentName_Type = DisplayString
_VrPpSrclComponentName_Object = MibTableColumn
vrPpSrclComponentName = _VrPpSrclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 1, 1, 2),
    _VrPpSrclComponentName_Type()
)
vrPpSrclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclComponentName.setStatus("mandatory")
_VrPpSrclStorageType_Type = StorageType
_VrPpSrclStorageType_Object = MibTableColumn
vrPpSrclStorageType = _VrPpSrclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 1, 1, 4),
    _VrPpSrclStorageType_Type()
)
vrPpSrclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclStorageType.setStatus("mandatory")
_VrPpSrclIndex_Type = NonReplicated
_VrPpSrclIndex_Object = MibTableColumn
vrPpSrclIndex = _VrPpSrclIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 1, 1, 10),
    _VrPpSrclIndex_Type()
)
vrPpSrclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrclIndex.setStatus("mandatory")
_VrPpSrclNs_ObjectIdentity = ObjectIdentity
vrPpSrclNs = _VrPpSrclNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2)
)
_VrPpSrclNsRowStatusTable_Object = MibTable
vrPpSrclNsRowStatusTable = _VrPpSrclNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpSrclNsRowStatusTable.setStatus("mandatory")
_VrPpSrclNsRowStatusEntry_Object = MibTableRow
vrPpSrclNsRowStatusEntry = _VrPpSrclNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 1, 1)
)
vrPpSrclNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclNsRowStatusEntry.setStatus("mandatory")
_VrPpSrclNsRowStatus_Type = RowStatus
_VrPpSrclNsRowStatus_Object = MibTableColumn
vrPpSrclNsRowStatus = _VrPpSrclNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 1, 1, 1),
    _VrPpSrclNsRowStatus_Type()
)
vrPpSrclNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclNsRowStatus.setStatus("mandatory")
_VrPpSrclNsComponentName_Type = DisplayString
_VrPpSrclNsComponentName_Object = MibTableColumn
vrPpSrclNsComponentName = _VrPpSrclNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 1, 1, 2),
    _VrPpSrclNsComponentName_Type()
)
vrPpSrclNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclNsComponentName.setStatus("mandatory")
_VrPpSrclNsStorageType_Type = StorageType
_VrPpSrclNsStorageType_Object = MibTableColumn
vrPpSrclNsStorageType = _VrPpSrclNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 1, 1, 4),
    _VrPpSrclNsStorageType_Type()
)
vrPpSrclNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclNsStorageType.setStatus("mandatory")
_VrPpSrclNsIndex_Type = NonReplicated
_VrPpSrclNsIndex_Object = MibTableColumn
vrPpSrclNsIndex = _VrPpSrclNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 1, 1, 10),
    _VrPpSrclNsIndex_Type()
)
vrPpSrclNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSrclNsIndex.setStatus("mandatory")
_VrPpSrclNsProvTable_Object = MibTable
vrPpSrclNsProvTable = _VrPpSrclNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpSrclNsProvTable.setStatus("mandatory")
_VrPpSrclNsProvEntry_Object = MibTableRow
vrPpSrclNsProvEntry = _VrPpSrclNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 10, 1)
)
vrPpSrclNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclNsProvEntry.setStatus("mandatory")


class _VrPpSrclNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpSrclNsIncomingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpSrclNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpSrclNsIncomingFilter_Object = MibTableColumn
vrPpSrclNsIncomingFilter = _VrPpSrclNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 10, 1, 2),
    _VrPpSrclNsIncomingFilter_Type()
)
vrPpSrclNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclNsIncomingFilter.setStatus("mandatory")


class _VrPpSrclNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpSrclNsOutgoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpSrclNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpSrclNsOutgoingFilter_Object = MibTableColumn
vrPpSrclNsOutgoingFilter = _VrPpSrclNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 2, 10, 1, 3),
    _VrPpSrclNsOutgoingFilter_Type()
)
vrPpSrclNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclNsOutgoingFilter.setStatus("mandatory")
_VrPpSrclProvTable_Object = MibTable
vrPpSrclProvTable = _VrPpSrclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10)
)
if mibBuilder.loadTexts:
    vrPpSrclProvTable.setStatus("mandatory")
_VrPpSrclProvEntry_Object = MibTableRow
vrPpSrclProvEntry = _VrPpSrclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1)
)
vrPpSrclProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclProvEntry.setStatus("mandatory")


class _VrPpSrclTranslateIpx_Type(Integer32):
    """Custom type vrPpSrclTranslateIpx based on Integer32"""
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


_VrPpSrclTranslateIpx_Type.__name__ = "Integer32"
_VrPpSrclTranslateIpx_Object = MibTableColumn
vrPpSrclTranslateIpx = _VrPpSrclTranslateIpx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1, 1),
    _VrPpSrclTranslateIpx_Type()
)
vrPpSrclTranslateIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclTranslateIpx.setStatus("mandatory")


class _VrPpSrclFragmentIp_Type(Integer32):
    """Custom type vrPpSrclFragmentIp based on Integer32"""
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


_VrPpSrclFragmentIp_Type.__name__ = "Integer32"
_VrPpSrclFragmentIp_Object = MibTableColumn
vrPpSrclFragmentIp = _VrPpSrclFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1, 2),
    _VrPpSrclFragmentIp_Type()
)
vrPpSrclFragmentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclFragmentIp.setStatus("mandatory")


class _VrPpSrclServiceClass_Type(Integer32):
    """Custom type vrPpSrclServiceClass based on Integer32"""
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


_VrPpSrclServiceClass_Type.__name__ = "Integer32"
_VrPpSrclServiceClass_Object = MibTableColumn
vrPpSrclServiceClass = _VrPpSrclServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1, 3),
    _VrPpSrclServiceClass_Type()
)
vrPpSrclServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclServiceClass.setStatus("mandatory")


class _VrPpSrclConvertArpMacAddress_Type(Integer32):
    """Custom type vrPpSrclConvertArpMacAddress based on Integer32"""
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


_VrPpSrclConvertArpMacAddress_Type.__name__ = "Integer32"
_VrPpSrclConvertArpMacAddress_Object = MibTableColumn
vrPpSrclConvertArpMacAddress = _VrPpSrclConvertArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1, 4),
    _VrPpSrclConvertArpMacAddress_Type()
)
vrPpSrclConvertArpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclConvertArpMacAddress.setStatus("mandatory")


class _VrPpSrclPortNum_Type(Unsigned32):
    """Custom type vrPpSrclPortNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpSrclPortNum_Type.__name__ = "Unsigned32"
_VrPpSrclPortNum_Object = MibTableColumn
vrPpSrclPortNum = _VrPpSrclPortNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1, 5),
    _VrPpSrclPortNum_Type()
)
vrPpSrclPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclPortNum.setStatus("mandatory")


class _VrPpSrclOutboundFrameMediaType_Type(Integer32):
    """Custom type vrPpSrclOutboundFrameMediaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetConv", 2),
          ("unaltered", 1))
    )


_VrPpSrclOutboundFrameMediaType_Type.__name__ = "Integer32"
_VrPpSrclOutboundFrameMediaType_Object = MibTableColumn
vrPpSrclOutboundFrameMediaType = _VrPpSrclOutboundFrameMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 10, 1, 6),
    _VrPpSrclOutboundFrameMediaType_Type()
)
vrPpSrclOutboundFrameMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclOutboundFrameMediaType.setStatus("mandatory")
_VrPpSrclStpProvTable_Object = MibTable
vrPpSrclStpProvTable = _VrPpSrclStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12)
)
if mibBuilder.loadTexts:
    vrPpSrclStpProvTable.setStatus("mandatory")
_VrPpSrclStpProvEntry_Object = MibTableRow
vrPpSrclStpProvEntry = _VrPpSrclStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1)
)
vrPpSrclStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclStpProvEntry.setStatus("mandatory")


class _VrPpSrclAdminStatus_Type(Integer32):
    """Custom type vrPpSrclAdminStatus based on Integer32"""
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


_VrPpSrclAdminStatus_Type.__name__ = "Integer32"
_VrPpSrclAdminStatus_Object = MibTableColumn
vrPpSrclAdminStatus = _VrPpSrclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1, 1),
    _VrPpSrclAdminStatus_Type()
)
vrPpSrclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclAdminStatus.setStatus("mandatory")


class _VrPpSrclPortStateStpControl_Type(Integer32):
    """Custom type vrPpSrclPortStateStpControl based on Integer32"""
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


_VrPpSrclPortStateStpControl_Type.__name__ = "Integer32"
_VrPpSrclPortStateStpControl_Object = MibTableColumn
vrPpSrclPortStateStpControl = _VrPpSrclPortStateStpControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1, 2),
    _VrPpSrclPortStateStpControl_Type()
)
vrPpSrclPortStateStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclPortStateStpControl.setStatus("mandatory")


class _VrPpSrclStpTypeProv_Type(Integer32):
    """Custom type vrPpSrclStpTypeProv based on Integer32"""
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


_VrPpSrclStpTypeProv_Type.__name__ = "Integer32"
_VrPpSrclStpTypeProv_Object = MibTableColumn
vrPpSrclStpTypeProv = _VrPpSrclStpTypeProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1, 3),
    _VrPpSrclStpTypeProv_Type()
)
vrPpSrclStpTypeProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclStpTypeProv.setStatus("mandatory")


class _VrPpSrclPortPriority_Type(Unsigned32):
    """Custom type vrPpSrclPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrclPortPriority_Type.__name__ = "Unsigned32"
_VrPpSrclPortPriority_Object = MibTableColumn
vrPpSrclPortPriority = _VrPpSrclPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1, 4),
    _VrPpSrclPortPriority_Type()
)
vrPpSrclPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclPortPriority.setStatus("mandatory")


class _VrPpSrclPathCost_Type(Unsigned32):
    """Custom type vrPpSrclPathCost based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrclPathCost_Type.__name__ = "Unsigned32"
_VrPpSrclPathCost_Object = MibTableColumn
vrPpSrclPathCost = _VrPpSrclPathCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1, 5),
    _VrPpSrclPathCost_Type()
)
vrPpSrclPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclPathCost.setStatus("mandatory")


class _VrPpSrclPathCostMethod_Type(Integer32):
    """Custom type vrPpSrclPathCostMethod based on Integer32"""
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


_VrPpSrclPathCostMethod_Type.__name__ = "Integer32"
_VrPpSrclPathCostMethod_Object = MibTableColumn
vrPpSrclPathCostMethod = _VrPpSrclPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 12, 1, 6),
    _VrPpSrclPathCostMethod_Type()
)
vrPpSrclPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclPathCostMethod.setStatus("mandatory")
_VrPpSrclDIProvTable_Object = MibTable
vrPpSrclDIProvTable = _VrPpSrclDIProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 13)
)
if mibBuilder.loadTexts:
    vrPpSrclDIProvTable.setStatus("mandatory")
_VrPpSrclDIProvEntry_Object = MibTableRow
vrPpSrclDIProvEntry = _VrPpSrclDIProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 13, 1)
)
vrPpSrclDIProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclDIProvEntry.setStatus("mandatory")


class _VrPpSrclDomainNum_Type(Unsigned32):
    """Custom type vrPpSrclDomainNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967293),
    )


_VrPpSrclDomainNum_Type.__name__ = "Unsigned32"
_VrPpSrclDomainNum_Object = MibTableColumn
vrPpSrclDomainNum = _VrPpSrclDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 13, 1, 1),
    _VrPpSrclDomainNum_Type()
)
vrPpSrclDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclDomainNum.setStatus("mandatory")


class _VrPpSrclPreserveDomain_Type(Integer32):
    """Custom type vrPpSrclPreserveDomain based on Integer32"""
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


_VrPpSrclPreserveDomain_Type.__name__ = "Integer32"
_VrPpSrclPreserveDomain_Object = MibTableColumn
vrPpSrclPreserveDomain = _VrPpSrclPreserveDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 13, 1, 2),
    _VrPpSrclPreserveDomain_Type()
)
vrPpSrclPreserveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclPreserveDomain.setStatus("mandatory")
_VrPpSrclStateTable_Object = MibTable
vrPpSrclStateTable = _VrPpSrclStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 14)
)
if mibBuilder.loadTexts:
    vrPpSrclStateTable.setStatus("mandatory")
_VrPpSrclStateEntry_Object = MibTableRow
vrPpSrclStateEntry = _VrPpSrclStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 14, 1)
)
vrPpSrclStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclStateEntry.setStatus("mandatory")


class _VrPpSrclAdminState_Type(Integer32):
    """Custom type vrPpSrclAdminState based on Integer32"""
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


_VrPpSrclAdminState_Type.__name__ = "Integer32"
_VrPpSrclAdminState_Object = MibTableColumn
vrPpSrclAdminState = _VrPpSrclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 14, 1, 1),
    _VrPpSrclAdminState_Type()
)
vrPpSrclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclAdminState.setStatus("mandatory")


class _VrPpSrclOperationalState_Type(Integer32):
    """Custom type vrPpSrclOperationalState based on Integer32"""
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


_VrPpSrclOperationalState_Type.__name__ = "Integer32"
_VrPpSrclOperationalState_Object = MibTableColumn
vrPpSrclOperationalState = _VrPpSrclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 14, 1, 2),
    _VrPpSrclOperationalState_Type()
)
vrPpSrclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclOperationalState.setStatus("mandatory")


class _VrPpSrclUsageState_Type(Integer32):
    """Custom type vrPpSrclUsageState based on Integer32"""
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


_VrPpSrclUsageState_Type.__name__ = "Integer32"
_VrPpSrclUsageState_Object = MibTableColumn
vrPpSrclUsageState = _VrPpSrclUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 14, 1, 3),
    _VrPpSrclUsageState_Type()
)
vrPpSrclUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclUsageState.setStatus("mandatory")
_VrPpSrclOperStatusTable_Object = MibTable
vrPpSrclOperStatusTable = _VrPpSrclOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 15)
)
if mibBuilder.loadTexts:
    vrPpSrclOperStatusTable.setStatus("mandatory")
_VrPpSrclOperStatusEntry_Object = MibTableRow
vrPpSrclOperStatusEntry = _VrPpSrclOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 15, 1)
)
vrPpSrclOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclOperStatusEntry.setStatus("mandatory")


class _VrPpSrclSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSrclSnmpOperStatus based on Integer32"""
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


_VrPpSrclSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSrclSnmpOperStatus_Object = MibTableColumn
vrPpSrclSnmpOperStatus = _VrPpSrclSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 15, 1, 1),
    _VrPpSrclSnmpOperStatus_Type()
)
vrPpSrclSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclSnmpOperStatus.setStatus("mandatory")
_VrPpSrclOperTable_Object = MibTable
vrPpSrclOperTable = _VrPpSrclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16)
)
if mibBuilder.loadTexts:
    vrPpSrclOperTable.setStatus("mandatory")
_VrPpSrclOperEntry_Object = MibTableRow
vrPpSrclOperEntry = _VrPpSrclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1)
)
vrPpSrclOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclOperEntry.setStatus("mandatory")


class _VrPpSrclPortName_Type(AsciiString):
    """Custom type vrPpSrclPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrPpSrclPortName_Type.__name__ = "AsciiString"
_VrPpSrclPortName_Object = MibTableColumn
vrPpSrclPortName = _VrPpSrclPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 1),
    _VrPpSrclPortName_Type()
)
vrPpSrclPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclPortName.setStatus("mandatory")


class _VrPpSrclUpTime_Type(Unsigned32):
    """Custom type vrPpSrclUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrclUpTime_Type.__name__ = "Unsigned32"
_VrPpSrclUpTime_Object = MibTableColumn
vrPpSrclUpTime = _VrPpSrclUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 3),
    _VrPpSrclUpTime_Type()
)
vrPpSrclUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclUpTime.setStatus("mandatory")


class _VrPpSrclDownTime_Type(Unsigned32):
    """Custom type vrPpSrclDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrclDownTime_Type.__name__ = "Unsigned32"
_VrPpSrclDownTime_Object = MibTableColumn
vrPpSrclDownTime = _VrPpSrclDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 4),
    _VrPpSrclDownTime_Type()
)
vrPpSrclDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDownTime.setStatus("mandatory")


class _VrPpSrclBridgingMode_Type(Integer32):
    """Custom type vrPpSrclBridgingMode based on Integer32"""
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


_VrPpSrclBridgingMode_Type.__name__ = "Integer32"
_VrPpSrclBridgingMode_Object = MibTableColumn
vrPpSrclBridgingMode = _VrPpSrclBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 5),
    _VrPpSrclBridgingMode_Type()
)
vrPpSrclBridgingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclBridgingMode.setStatus("mandatory")


class _VrPpSrclBridgePortConfig_Type(Integer32):
    """Custom type vrPpSrclBridgePortConfig based on Integer32"""
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


_VrPpSrclBridgePortConfig_Type.__name__ = "Integer32"
_VrPpSrclBridgePortConfig_Object = MibTableColumn
vrPpSrclBridgePortConfig = _VrPpSrclBridgePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 6),
    _VrPpSrclBridgePortConfig_Type()
)
vrPpSrclBridgePortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclBridgePortConfig.setStatus("mandatory")


class _VrPpSrclBridgePortType_Type(Integer32):
    """Custom type vrPpSrclBridgePortType based on Integer32"""
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


_VrPpSrclBridgePortType_Type.__name__ = "Integer32"
_VrPpSrclBridgePortType_Object = MibTableColumn
vrPpSrclBridgePortType = _VrPpSrclBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 7),
    _VrPpSrclBridgePortType_Type()
)
vrPpSrclBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclBridgePortType.setStatus("mandatory")


class _VrPpSrclIfIndex_Type(InterfaceIndex):
    """Custom type vrPpSrclIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrclIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpSrclIfIndex_Object = MibTableColumn
vrPpSrclIfIndex = _VrPpSrclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 8),
    _VrPpSrclIfIndex_Type()
)
vrPpSrclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclIfIndex.setStatus("mandatory")
_VrPpSrclDelayExceededDiscards_Type = Counter32
_VrPpSrclDelayExceededDiscards_Object = MibTableColumn
vrPpSrclDelayExceededDiscards = _VrPpSrclDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 10),
    _VrPpSrclDelayExceededDiscards_Type()
)
vrPpSrclDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDelayExceededDiscards.setStatus("mandatory")
_VrPpSrclMtuExceededDiscards_Type = Counter32
_VrPpSrclMtuExceededDiscards_Object = MibTableColumn
vrPpSrclMtuExceededDiscards = _VrPpSrclMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 16, 1, 11),
    _VrPpSrclMtuExceededDiscards_Type()
)
vrPpSrclMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclMtuExceededDiscards.setStatus("mandatory")
_VrPpSrclStpOperTable_Object = MibTable
vrPpSrclStpOperTable = _VrPpSrclStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18)
)
if mibBuilder.loadTexts:
    vrPpSrclStpOperTable.setStatus("mandatory")
_VrPpSrclStpOperEntry_Object = MibTableRow
vrPpSrclStpOperEntry = _VrPpSrclStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1)
)
vrPpSrclStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclStpOperEntry.setStatus("mandatory")


class _VrPpSrclStpPortState_Type(Integer32):
    """Custom type vrPpSrclStpPortState based on Integer32"""
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


_VrPpSrclStpPortState_Type.__name__ = "Integer32"
_VrPpSrclStpPortState_Object = MibTableColumn
vrPpSrclStpPortState = _VrPpSrclStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 2),
    _VrPpSrclStpPortState_Type()
)
vrPpSrclStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclStpPortState.setStatus("mandatory")


class _VrPpSrclStpTypeOper_Type(Integer32):
    """Custom type vrPpSrclStpTypeOper based on Integer32"""
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


_VrPpSrclStpTypeOper_Type.__name__ = "Integer32"
_VrPpSrclStpTypeOper_Object = MibTableColumn
vrPpSrclStpTypeOper = _VrPpSrclStpTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 3),
    _VrPpSrclStpTypeOper_Type()
)
vrPpSrclStpTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclStpTypeOper.setStatus("mandatory")


class _VrPpSrclDesignatedCost_Type(Unsigned32):
    """Custom type vrPpSrclDesignatedCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpSrclDesignatedCost_Type.__name__ = "Unsigned32"
_VrPpSrclDesignatedCost_Object = MibTableColumn
vrPpSrclDesignatedCost = _VrPpSrclDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 4),
    _VrPpSrclDesignatedCost_Type()
)
vrPpSrclDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDesignatedCost.setStatus("mandatory")


class _VrPpSrclPathCostOper_Type(Unsigned32):
    """Custom type vrPpSrclPathCostOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpSrclPathCostOper_Type.__name__ = "Unsigned32"
_VrPpSrclPathCostOper_Object = MibTableColumn
vrPpSrclPathCostOper = _VrPpSrclPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 5),
    _VrPpSrclPathCostOper_Type()
)
vrPpSrclPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclPathCostOper.setStatus("mandatory")


class _VrPpSrclDesignatedBridge_Type(BridgeId):
    """Custom type vrPpSrclDesignatedBridge based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrclDesignatedBridge_Type.__name__ = "BridgeId"
_VrPpSrclDesignatedBridge_Object = MibTableColumn
vrPpSrclDesignatedBridge = _VrPpSrclDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 6),
    _VrPpSrclDesignatedBridge_Type()
)
vrPpSrclDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDesignatedBridge.setStatus("mandatory")


class _VrPpSrclDesignatedPort_Type(Hex):
    """Custom type vrPpSrclDesignatedPort based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpSrclDesignatedPort_Type.__name__ = "Hex"
_VrPpSrclDesignatedPort_Object = MibTableColumn
vrPpSrclDesignatedPort = _VrPpSrclDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 7),
    _VrPpSrclDesignatedPort_Type()
)
vrPpSrclDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDesignatedPort.setStatus("mandatory")
_VrPpSrclForwardTransitions_Type = Counter32
_VrPpSrclForwardTransitions_Object = MibTableColumn
vrPpSrclForwardTransitions = _VrPpSrclForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 8),
    _VrPpSrclForwardTransitions_Type()
)
vrPpSrclForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclForwardTransitions.setStatus("mandatory")
_VrPpSrclBlockingDiscards_Type = Counter32
_VrPpSrclBlockingDiscards_Object = MibTableColumn
vrPpSrclBlockingDiscards = _VrPpSrclBlockingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 9),
    _VrPpSrclBlockingDiscards_Type()
)
vrPpSrclBlockingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclBlockingDiscards.setStatus("mandatory")


class _VrPpSrclDesignatedRoot_Type(BridgeId):
    """Custom type vrPpSrclDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrPpSrclDesignatedRoot_Type.__name__ = "BridgeId"
_VrPpSrclDesignatedRoot_Object = MibTableColumn
vrPpSrclDesignatedRoot = _VrPpSrclDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 18, 1, 10),
    _VrPpSrclDesignatedRoot_Type()
)
vrPpSrclDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDesignatedRoot.setStatus("mandatory")
_VrPpSrclStatsTable_Object = MibTable
vrPpSrclStatsTable = _VrPpSrclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19)
)
if mibBuilder.loadTexts:
    vrPpSrclStatsTable.setStatus("mandatory")
_VrPpSrclStatsEntry_Object = MibTableRow
vrPpSrclStatsEntry = _VrPpSrclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19, 1)
)
vrPpSrclStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclStatsEntry.setStatus("mandatory")
_VrPpSrclBadAbstractDiscards_Type = Counter32
_VrPpSrclBadAbstractDiscards_Object = MibTableColumn
vrPpSrclBadAbstractDiscards = _VrPpSrclBadAbstractDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19, 1, 1),
    _VrPpSrclBadAbstractDiscards_Type()
)
vrPpSrclBadAbstractDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclBadAbstractDiscards.setStatus("mandatory")
_VrPpSrclTinygramFramesIn_Type = Counter32
_VrPpSrclTinygramFramesIn_Object = MibTableColumn
vrPpSrclTinygramFramesIn = _VrPpSrclTinygramFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19, 1, 2),
    _VrPpSrclTinygramFramesIn_Type()
)
vrPpSrclTinygramFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclTinygramFramesIn.setStatus("mandatory")
_VrPpSrclTinygramFramesOut_Type = Counter32
_VrPpSrclTinygramFramesOut_Object = MibTableColumn
vrPpSrclTinygramFramesOut = _VrPpSrclTinygramFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19, 1, 3),
    _VrPpSrclTinygramFramesOut_Type()
)
vrPpSrclTinygramFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclTinygramFramesOut.setStatus("mandatory")
_VrPpSrclInFilterDiscards_Type = Counter32
_VrPpSrclInFilterDiscards_Object = MibTableColumn
vrPpSrclInFilterDiscards = _VrPpSrclInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19, 1, 4),
    _VrPpSrclInFilterDiscards_Type()
)
vrPpSrclInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclInFilterDiscards.setStatus("mandatory")
_VrPpSrclOutFilterDiscards_Type = Counter32
_VrPpSrclOutFilterDiscards_Object = MibTableColumn
vrPpSrclOutFilterDiscards = _VrPpSrclOutFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 19, 1, 5),
    _VrPpSrclOutFilterDiscards_Type()
)
vrPpSrclOutFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclOutFilterDiscards.setStatus("mandatory")
_VrPpSrclSrProvTable_Object = MibTable
vrPpSrclSrProvTable = _VrPpSrclSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20)
)
if mibBuilder.loadTexts:
    vrPpSrclSrProvTable.setStatus("mandatory")
_VrPpSrclSrProvEntry_Object = MibTableRow
vrPpSrclSrProvEntry = _VrPpSrclSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1)
)
vrPpSrclSrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclSrProvEntry.setStatus("mandatory")


class _VrPpSrclHopCount_Type(Unsigned32):
    """Custom type vrPpSrclHopCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrPpSrclHopCount_Type.__name__ = "Unsigned32"
_VrPpSrclHopCount_Object = MibTableColumn
vrPpSrclHopCount = _VrPpSrclHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 1),
    _VrPpSrclHopCount_Type()
)
vrPpSrclHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclHopCount.setStatus("mandatory")


class _VrPpSrclExploreFrameTreatment_Type(Integer32):
    """Custom type vrPpSrclExploreFrameTreatment based on Integer32"""
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


_VrPpSrclExploreFrameTreatment_Type.__name__ = "Integer32"
_VrPpSrclExploreFrameTreatment_Object = MibTableColumn
vrPpSrclExploreFrameTreatment = _VrPpSrclExploreFrameTreatment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 2),
    _VrPpSrclExploreFrameTreatment_Type()
)
vrPpSrclExploreFrameTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclExploreFrameTreatment.setStatus("mandatory")


class _VrPpSrclLanId_Type(Unsigned32):
    """Custom type vrPpSrclLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrclLanId_Type.__name__ = "Unsigned32"
_VrPpSrclLanId_Object = MibTableColumn
vrPpSrclLanId = _VrPpSrclLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 3),
    _VrPpSrclLanId_Type()
)
vrPpSrclLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclLanId.setStatus("mandatory")


class _VrPpSrclInternalLanId_Type(Unsigned32):
    """Custom type vrPpSrclInternalLanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrPpSrclInternalLanId_Type.__name__ = "Unsigned32"
_VrPpSrclInternalLanId_Object = MibTableColumn
vrPpSrclInternalLanId = _VrPpSrclInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 4),
    _VrPpSrclInternalLanId_Type()
)
vrPpSrclInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclInternalLanId.setStatus("mandatory")


class _VrPpSrclBridgeNum_Type(Unsigned32):
    """Custom type vrPpSrclBridgeNum based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrPpSrclBridgeNum_Type.__name__ = "Unsigned32"
_VrPpSrclBridgeNum_Object = MibTableColumn
vrPpSrclBridgeNum = _VrPpSrclBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 5),
    _VrPpSrclBridgeNum_Type()
)
vrPpSrclBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclBridgeNum.setStatus("mandatory")


class _VrPpSrclLargestFrame_Type(Unsigned32):
    """Custom type vrPpSrclLargestFrame based on Unsigned32"""
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


_VrPpSrclLargestFrame_Type.__name__ = "Unsigned32"
_VrPpSrclLargestFrame_Object = MibTableColumn
vrPpSrclLargestFrame = _VrPpSrclLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 6),
    _VrPpSrclLargestFrame_Type()
)
vrPpSrclLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclLargestFrame.setStatus("mandatory")


class _VrPpSrclSteSpanMode_Type(Integer32):
    """Custom type vrPpSrclSteSpanMode based on Integer32"""
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


_VrPpSrclSteSpanMode_Type.__name__ = "Integer32"
_VrPpSrclSteSpanMode_Object = MibTableColumn
vrPpSrclSteSpanMode = _VrPpSrclSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 7),
    _VrPpSrclSteSpanMode_Type()
)
vrPpSrclSteSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclSteSpanMode.setStatus("mandatory")


class _VrPpSrclAreRdLimit_Type(Unsigned32):
    """Custom type vrPpSrclAreRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrclAreRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrclAreRdLimit_Object = MibTableColumn
vrPpSrclAreRdLimit = _VrPpSrclAreRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 8),
    _VrPpSrclAreRdLimit_Type()
)
vrPpSrclAreRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclAreRdLimit.setStatus("mandatory")


class _VrPpSrclSteRdLimit_Type(Unsigned32):
    """Custom type vrPpSrclSteRdLimit based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VrPpSrclSteRdLimit_Type.__name__ = "Unsigned32"
_VrPpSrclSteRdLimit_Object = MibTableColumn
vrPpSrclSteRdLimit = _VrPpSrclSteRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 20, 1, 9),
    _VrPpSrclSteRdLimit_Type()
)
vrPpSrclSteRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSrclSteRdLimit.setStatus("mandatory")
_VrPpSrclSrStatsTable_Object = MibTable
vrPpSrclSrStatsTable = _VrPpSrclSrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21)
)
if mibBuilder.loadTexts:
    vrPpSrclSrStatsTable.setStatus("mandatory")
_VrPpSrclSrStatsEntry_Object = MibTableRow
vrPpSrclSrStatsEntry = _VrPpSrclSrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1)
)
vrPpSrclSrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrPpSrclIndex"),
)
if mibBuilder.loadTexts:
    vrPpSrclSrStatsEntry.setStatus("mandatory")
_VrPpSrclSpecInFrames_Type = Counter32
_VrPpSrclSpecInFrames_Object = MibTableColumn
vrPpSrclSpecInFrames = _VrPpSrclSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 1),
    _VrPpSrclSpecInFrames_Type()
)
vrPpSrclSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclSpecInFrames.setStatus("mandatory")
_VrPpSrclSpecOutFrames_Type = Counter32
_VrPpSrclSpecOutFrames_Object = MibTableColumn
vrPpSrclSpecOutFrames = _VrPpSrclSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 2),
    _VrPpSrclSpecOutFrames_Type()
)
vrPpSrclSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclSpecOutFrames.setStatus("mandatory")
_VrPpSrclApeInFrames_Type = Counter32
_VrPpSrclApeInFrames_Object = MibTableColumn
vrPpSrclApeInFrames = _VrPpSrclApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 3),
    _VrPpSrclApeInFrames_Type()
)
vrPpSrclApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclApeInFrames.setStatus("mandatory")
_VrPpSrclApeOutFrames_Type = Counter32
_VrPpSrclApeOutFrames_Object = MibTableColumn
vrPpSrclApeOutFrames = _VrPpSrclApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 4),
    _VrPpSrclApeOutFrames_Type()
)
vrPpSrclApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclApeOutFrames.setStatus("mandatory")
_VrPpSrclSteInFrames_Type = Counter32
_VrPpSrclSteInFrames_Object = MibTableColumn
vrPpSrclSteInFrames = _VrPpSrclSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 5),
    _VrPpSrclSteInFrames_Type()
)
vrPpSrclSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclSteInFrames.setStatus("mandatory")
_VrPpSrclSteOutFrames_Type = Counter32
_VrPpSrclSteOutFrames_Object = MibTableColumn
vrPpSrclSteOutFrames = _VrPpSrclSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 6),
    _VrPpSrclSteOutFrames_Type()
)
vrPpSrclSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclSteOutFrames.setStatus("mandatory")
_VrPpSrclSegmentMismatchDiscards_Type = Counter32
_VrPpSrclSegmentMismatchDiscards_Object = MibTableColumn
vrPpSrclSegmentMismatchDiscards = _VrPpSrclSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 7),
    _VrPpSrclSegmentMismatchDiscards_Type()
)
vrPpSrclSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclSegmentMismatchDiscards.setStatus("mandatory")
_VrPpSrclDupSegmentDiscards_Type = Counter32
_VrPpSrclDupSegmentDiscards_Object = MibTableColumn
vrPpSrclDupSegmentDiscards = _VrPpSrclDupSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 8),
    _VrPpSrclDupSegmentDiscards_Type()
)
vrPpSrclDupSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDupSegmentDiscards.setStatus("mandatory")
_VrPpSrclHopCountExceededDiscards_Type = Counter32
_VrPpSrclHopCountExceededDiscards_Object = MibTableColumn
vrPpSrclHopCountExceededDiscards = _VrPpSrclHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 9),
    _VrPpSrclHopCountExceededDiscards_Type()
)
vrPpSrclHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclHopCountExceededDiscards.setStatus("mandatory")
_VrPpSrclDupLanIdOrTreeErrors_Type = Counter32
_VrPpSrclDupLanIdOrTreeErrors_Object = MibTableColumn
vrPpSrclDupLanIdOrTreeErrors = _VrPpSrclDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 10),
    _VrPpSrclDupLanIdOrTreeErrors_Type()
)
vrPpSrclDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDupLanIdOrTreeErrors.setStatus("mandatory")
_VrPpSrclLanIdMismatches_Type = Counter32
_VrPpSrclLanIdMismatches_Object = MibTableColumn
vrPpSrclLanIdMismatches = _VrPpSrclLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 11),
    _VrPpSrclLanIdMismatches_Type()
)
vrPpSrclLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclLanIdMismatches.setStatus("mandatory")
_VrPpSrclStaticDiscards_Type = Counter32
_VrPpSrclStaticDiscards_Object = MibTableColumn
vrPpSrclStaticDiscards = _VrPpSrclStaticDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 12),
    _VrPpSrclStaticDiscards_Type()
)
vrPpSrclStaticDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclStaticDiscards.setStatus("mandatory")
_VrPpSrclDynamicDiscards_Type = Counter32
_VrPpSrclDynamicDiscards_Object = MibTableColumn
vrPpSrclDynamicDiscards = _VrPpSrclDynamicDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 14, 21, 1, 13),
    _VrPpSrclDynamicDiscards_Type()
)
vrPpSrclDynamicDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSrclDynamicDiscards.setStatus("mandatory")
_VrBr_ObjectIdentity = ObjectIdentity
vrBr = _VrBr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5)
)
_VrBrRowStatusTable_Object = MibTable
vrBrRowStatusTable = _VrBrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 1)
)
if mibBuilder.loadTexts:
    vrBrRowStatusTable.setStatus("mandatory")
_VrBrRowStatusEntry_Object = MibTableRow
vrBrRowStatusEntry = _VrBrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 1, 1)
)
vrBrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
)
if mibBuilder.loadTexts:
    vrBrRowStatusEntry.setStatus("mandatory")
_VrBrRowStatus_Type = RowStatus
_VrBrRowStatus_Object = MibTableColumn
vrBrRowStatus = _VrBrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 1, 1, 1),
    _VrBrRowStatus_Type()
)
vrBrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrRowStatus.setStatus("mandatory")
_VrBrComponentName_Type = DisplayString
_VrBrComponentName_Object = MibTableColumn
vrBrComponentName = _VrBrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 1, 1, 2),
    _VrBrComponentName_Type()
)
vrBrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrComponentName.setStatus("mandatory")
_VrBrStorageType_Type = StorageType
_VrBrStorageType_Object = MibTableColumn
vrBrStorageType = _VrBrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 1, 1, 4),
    _VrBrStorageType_Type()
)
vrBrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrStorageType.setStatus("mandatory")
_VrBrIndex_Type = NonReplicated
_VrBrIndex_Object = MibTableColumn
vrBrIndex = _VrBrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 1, 1, 10),
    _VrBrIndex_Type()
)
vrBrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrIndex.setStatus("mandatory")
_VrBrPte_ObjectIdentity = ObjectIdentity
vrBrPte = _VrBrPte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2)
)
_VrBrPteRowStatusTable_Object = MibTable
vrBrPteRowStatusTable = _VrBrPteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vrBrPteRowStatusTable.setStatus("mandatory")
_VrBrPteRowStatusEntry_Object = MibTableRow
vrBrPteRowStatusEntry = _VrBrPteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1)
)
vrBrPteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPteDomainNumIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPtePortNameIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPteModeIndex"),
)
if mibBuilder.loadTexts:
    vrBrPteRowStatusEntry.setStatus("mandatory")
_VrBrPteRowStatus_Type = RowStatus
_VrBrPteRowStatus_Object = MibTableColumn
vrBrPteRowStatus = _VrBrPteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1, 1),
    _VrBrPteRowStatus_Type()
)
vrBrPteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteRowStatus.setStatus("mandatory")
_VrBrPteComponentName_Type = DisplayString
_VrBrPteComponentName_Object = MibTableColumn
vrBrPteComponentName = _VrBrPteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1, 2),
    _VrBrPteComponentName_Type()
)
vrBrPteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteComponentName.setStatus("mandatory")
_VrBrPteStorageType_Type = StorageType
_VrBrPteStorageType_Object = MibTableColumn
vrBrPteStorageType = _VrBrPteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1, 4),
    _VrBrPteStorageType_Type()
)
vrBrPteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteStorageType.setStatus("mandatory")


class _VrBrPteDomainNumIndex_Type(Integer32):
    """Custom type vrBrPteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrBrPteDomainNumIndex_Type.__name__ = "Integer32"
_VrBrPteDomainNumIndex_Object = MibTableColumn
vrBrPteDomainNumIndex = _VrBrPteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1, 10),
    _VrBrPteDomainNumIndex_Type()
)
vrBrPteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrPteDomainNumIndex.setStatus("mandatory")


class _VrBrPtePortNameIndex_Type(AsciiStringIndex):
    """Custom type vrBrPtePortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_VrBrPtePortNameIndex_Type.__name__ = "AsciiStringIndex"
_VrBrPtePortNameIndex_Object = MibTableColumn
vrBrPtePortNameIndex = _VrBrPtePortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1, 11),
    _VrBrPtePortNameIndex_Type()
)
vrBrPtePortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrPtePortNameIndex.setStatus("mandatory")


class _VrBrPteModeIndex_Type(Integer32):
    """Custom type vrBrPteModeIndex based on Integer32"""
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


_VrBrPteModeIndex_Type.__name__ = "Integer32"
_VrBrPteModeIndex_Object = MibTableColumn
vrBrPteModeIndex = _VrBrPteModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 1, 1, 12),
    _VrBrPteModeIndex_Type()
)
vrBrPteModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrPteModeIndex.setStatus("mandatory")
_VrBrPteOperTable_Object = MibTable
vrBrPteOperTable = _VrBrPteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10)
)
if mibBuilder.loadTexts:
    vrBrPteOperTable.setStatus("mandatory")
_VrBrPteOperEntry_Object = MibTableRow
vrBrPteOperEntry = _VrBrPteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10, 1)
)
vrBrPteOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPteDomainNumIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPtePortNameIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPteModeIndex"),
)
if mibBuilder.loadTexts:
    vrBrPteOperEntry.setStatus("mandatory")


class _VrBrPteMacType_Type(Integer32):
    """Custom type vrBrPteMacType based on Integer32"""
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


_VrBrPteMacType_Type.__name__ = "Integer32"
_VrBrPteMacType_Object = MibTableColumn
vrBrPteMacType = _VrBrPteMacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10, 1, 1),
    _VrBrPteMacType_Type()
)
vrBrPteMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteMacType.setStatus("mandatory")


class _VrBrPteStpState_Type(Integer32):
    """Custom type vrBrPteStpState based on Integer32"""
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


_VrBrPteStpState_Type.__name__ = "Integer32"
_VrBrPteStpState_Object = MibTableColumn
vrBrPteStpState = _VrBrPteStpState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10, 1, 2),
    _VrBrPteStpState_Type()
)
vrBrPteStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteStpState.setStatus("mandatory")


class _VrBrPteStpType_Type(Integer32):
    """Custom type vrBrPteStpType based on Integer32"""
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


_VrBrPteStpType_Type.__name__ = "Integer32"
_VrBrPteStpType_Object = MibTableColumn
vrBrPteStpType = _VrBrPteStpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10, 1, 3),
    _VrBrPteStpType_Type()
)
vrBrPteStpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteStpType.setStatus("mandatory")


class _VrBrPteFilterPoints_Type(Integer32):
    """Custom type vrBrPteFilterPoints based on Integer32"""
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


_VrBrPteFilterPoints_Type.__name__ = "Integer32"
_VrBrPteFilterPoints_Object = MibTableColumn
vrBrPteFilterPoints = _VrBrPteFilterPoints_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10, 1, 4),
    _VrBrPteFilterPoints_Type()
)
vrBrPteFilterPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteFilterPoints.setStatus("mandatory")


class _VrBrPtePortPointsTo_Type(Integer32):
    """Custom type vrBrPtePortPointsTo based on Integer32"""
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


_VrBrPtePortPointsTo_Type.__name__ = "Integer32"
_VrBrPtePortPointsTo_Object = MibTableColumn
vrBrPtePortPointsTo = _VrBrPtePortPointsTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 10, 1, 5),
    _VrBrPtePortPointsTo_Type()
)
vrBrPtePortPointsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPtePortPointsTo.setStatus("mandatory")
_VrBrPteSpOperTable_Object = MibTable
vrBrPteSpOperTable = _VrBrPteSpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 11)
)
if mibBuilder.loadTexts:
    vrBrPteSpOperTable.setStatus("mandatory")
_VrBrPteSpOperEntry_Object = MibTableRow
vrBrPteSpOperEntry = _VrBrPteSpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 11, 1)
)
vrBrPteSpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPteDomainNumIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPtePortNameIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrPteModeIndex"),
)
if mibBuilder.loadTexts:
    vrBrPteSpOperEntry.setStatus("mandatory")


class _VrBrPteLanId_Type(Unsigned32):
    """Custom type vrBrPteLanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_VrBrPteLanId_Type.__name__ = "Unsigned32"
_VrBrPteLanId_Object = MibTableColumn
vrBrPteLanId = _VrBrPteLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 11, 1, 1),
    _VrBrPteLanId_Type()
)
vrBrPteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteLanId.setStatus("mandatory")


class _VrBrPteInternalLanId_Type(Unsigned32):
    """Custom type vrBrPteInternalLanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_VrBrPteInternalLanId_Type.__name__ = "Unsigned32"
_VrBrPteInternalLanId_Object = MibTableColumn
vrBrPteInternalLanId = _VrBrPteInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 11, 1, 2),
    _VrBrPteInternalLanId_Type()
)
vrBrPteInternalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteInternalLanId.setStatus("mandatory")


class _VrBrPteBridgeNum_Type(Unsigned32):
    """Custom type vrBrPteBridgeNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(65535, 65535),
    )


_VrBrPteBridgeNum_Type.__name__ = "Unsigned32"
_VrBrPteBridgeNum_Object = MibTableColumn
vrBrPteBridgeNum = _VrBrPteBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 2, 11, 1, 3),
    _VrBrPteBridgeNum_Type()
)
vrBrPteBridgeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrPteBridgeNum.setStatus("mandatory")
_VrBrNs_ObjectIdentity = ObjectIdentity
vrBrNs = _VrBrNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3)
)
_VrBrNsRowStatusTable_Object = MibTable
vrBrNsRowStatusTable = _VrBrNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 1)
)
if mibBuilder.loadTexts:
    vrBrNsRowStatusTable.setStatus("mandatory")
_VrBrNsRowStatusEntry_Object = MibTableRow
vrBrNsRowStatusEntry = _VrBrNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 1, 1)
)
vrBrNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrNsIndex"),
)
if mibBuilder.loadTexts:
    vrBrNsRowStatusEntry.setStatus("mandatory")
_VrBrNsRowStatus_Type = RowStatus
_VrBrNsRowStatus_Object = MibTableColumn
vrBrNsRowStatus = _VrBrNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 1, 1, 1),
    _VrBrNsRowStatus_Type()
)
vrBrNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsRowStatus.setStatus("mandatory")
_VrBrNsComponentName_Type = DisplayString
_VrBrNsComponentName_Object = MibTableColumn
vrBrNsComponentName = _VrBrNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 1, 1, 2),
    _VrBrNsComponentName_Type()
)
vrBrNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrNsComponentName.setStatus("mandatory")
_VrBrNsStorageType_Type = StorageType
_VrBrNsStorageType_Object = MibTableColumn
vrBrNsStorageType = _VrBrNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 1, 1, 4),
    _VrBrNsStorageType_Type()
)
vrBrNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrNsStorageType.setStatus("mandatory")
_VrBrNsIndex_Type = NonReplicated
_VrBrNsIndex_Object = MibTableColumn
vrBrNsIndex = _VrBrNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 1, 1, 10),
    _VrBrNsIndex_Type()
)
vrBrNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrNsIndex.setStatus("mandatory")
_VrBrNsAte_ObjectIdentity = ObjectIdentity
vrBrNsAte = _VrBrNsAte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2)
)
_VrBrNsAteRowStatusTable_Object = MibTable
vrBrNsAteRowStatusTable = _VrBrNsAteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrBrNsAteRowStatusTable.setStatus("mandatory")
_VrBrNsAteRowStatusEntry_Object = MibTableRow
vrBrNsAteRowStatusEntry = _VrBrNsAteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 1, 1)
)
vrBrNsAteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrNsIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrNsAteEntryNumberIndex"),
)
if mibBuilder.loadTexts:
    vrBrNsAteRowStatusEntry.setStatus("mandatory")
_VrBrNsAteRowStatus_Type = RowStatus
_VrBrNsAteRowStatus_Object = MibTableColumn
vrBrNsAteRowStatus = _VrBrNsAteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 1, 1, 1),
    _VrBrNsAteRowStatus_Type()
)
vrBrNsAteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteRowStatus.setStatus("mandatory")
_VrBrNsAteComponentName_Type = DisplayString
_VrBrNsAteComponentName_Object = MibTableColumn
vrBrNsAteComponentName = _VrBrNsAteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 1, 1, 2),
    _VrBrNsAteComponentName_Type()
)
vrBrNsAteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrNsAteComponentName.setStatus("mandatory")
_VrBrNsAteStorageType_Type = StorageType
_VrBrNsAteStorageType_Object = MibTableColumn
vrBrNsAteStorageType = _VrBrNsAteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 1, 1, 4),
    _VrBrNsAteStorageType_Type()
)
vrBrNsAteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrNsAteStorageType.setStatus("mandatory")


class _VrBrNsAteEntryNumberIndex_Type(Integer32):
    """Custom type vrBrNsAteEntryNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrBrNsAteEntryNumberIndex_Type.__name__ = "Integer32"
_VrBrNsAteEntryNumberIndex_Object = MibTableColumn
vrBrNsAteEntryNumberIndex = _VrBrNsAteEntryNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 1, 1, 10),
    _VrBrNsAteEntryNumberIndex_Type()
)
vrBrNsAteEntryNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrNsAteEntryNumberIndex.setStatus("mandatory")
_VrBrNsAteProvTable_Object = MibTable
vrBrNsAteProvTable = _VrBrNsAteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrBrNsAteProvTable.setStatus("mandatory")
_VrBrNsAteProvEntry_Object = MibTableRow
vrBrNsAteProvEntry = _VrBrNsAteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1)
)
vrBrNsAteProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrNsIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrNsAteEntryNumberIndex"),
)
if mibBuilder.loadTexts:
    vrBrNsAteProvEntry.setStatus("mandatory")


class _VrBrNsAteDomainNum_Type(Unsigned32):
    """Custom type vrBrNsAteDomainNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_VrBrNsAteDomainNum_Type.__name__ = "Unsigned32"
_VrBrNsAteDomainNum_Object = MibTableColumn
vrBrNsAteDomainNum = _VrBrNsAteDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 1),
    _VrBrNsAteDomainNum_Type()
)
vrBrNsAteDomainNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteDomainNum.setStatus("mandatory")


class _VrBrNsAteFirstMacAddress_Type(MacAddress):
    """Custom type vrBrNsAteFirstMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrNsAteFirstMacAddress_Type.__name__ = "MacAddress"
_VrBrNsAteFirstMacAddress_Object = MibTableColumn
vrBrNsAteFirstMacAddress = _VrBrNsAteFirstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 2),
    _VrBrNsAteFirstMacAddress_Type()
)
vrBrNsAteFirstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteFirstMacAddress.setStatus("mandatory")


class _VrBrNsAteFirstMacAddressMask_Type(MacAddress):
    """Custom type vrBrNsAteFirstMacAddressMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrNsAteFirstMacAddressMask_Type.__name__ = "MacAddress"
_VrBrNsAteFirstMacAddressMask_Object = MibTableColumn
vrBrNsAteFirstMacAddressMask = _VrBrNsAteFirstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 3),
    _VrBrNsAteFirstMacAddressMask_Type()
)
vrBrNsAteFirstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteFirstMacAddressMask.setStatus("mandatory")


class _VrBrNsAteSecondMacAddress_Type(MacAddress):
    """Custom type vrBrNsAteSecondMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrNsAteSecondMacAddress_Type.__name__ = "MacAddress"
_VrBrNsAteSecondMacAddress_Object = MibTableColumn
vrBrNsAteSecondMacAddress = _VrBrNsAteSecondMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 4),
    _VrBrNsAteSecondMacAddress_Type()
)
vrBrNsAteSecondMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteSecondMacAddress.setStatus("mandatory")


class _VrBrNsAteSecondMacAddressMask_Type(MacAddress):
    """Custom type vrBrNsAteSecondMacAddressMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrNsAteSecondMacAddressMask_Type.__name__ = "MacAddress"
_VrBrNsAteSecondMacAddressMask_Object = MibTableColumn
vrBrNsAteSecondMacAddressMask = _VrBrNsAteSecondMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 5),
    _VrBrNsAteSecondMacAddressMask_Type()
)
vrBrNsAteSecondMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteSecondMacAddressMask.setStatus("mandatory")


class _VrBrNsAteDirection_Type(Integer32):
    """Custom type vrBrNsAteDirection based on Integer32"""
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


_VrBrNsAteDirection_Type.__name__ = "Integer32"
_VrBrNsAteDirection_Object = MibTableColumn
vrBrNsAteDirection = _VrBrNsAteDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 6),
    _VrBrNsAteDirection_Type()
)
vrBrNsAteDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteDirection.setStatus("mandatory")


class _VrBrNsAteFilterName_Type(AsciiString):
    """Custom type vrBrNsAteFilterName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrBrNsAteFilterName_Type.__name__ = "AsciiString"
_VrBrNsAteFilterName_Object = MibTableColumn
vrBrNsAteFilterName = _VrBrNsAteFilterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 2, 10, 1, 7),
    _VrBrNsAteFilterName_Type()
)
vrBrNsAteFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsAteFilterName.setStatus("mandatory")
_VrBrNsProvTable_Object = MibTable
vrBrNsProvTable = _VrBrNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 10)
)
if mibBuilder.loadTexts:
    vrBrNsProvTable.setStatus("mandatory")
_VrBrNsProvEntry_Object = MibTableRow
vrBrNsProvEntry = _VrBrNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 10, 1)
)
vrBrNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrNsIndex"),
)
if mibBuilder.loadTexts:
    vrBrNsProvEntry.setStatus("mandatory")


class _VrBrNsFirstFilter_Type(AsciiString):
    """Custom type vrBrNsFirstFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrBrNsFirstFilter_Type.__name__ = "AsciiString"
_VrBrNsFirstFilter_Object = MibTableColumn
vrBrNsFirstFilter = _VrBrNsFirstFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 10, 1, 1),
    _VrBrNsFirstFilter_Type()
)
vrBrNsFirstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsFirstFilter.setStatus("mandatory")


class _VrBrNsLastFilter_Type(AsciiString):
    """Custom type vrBrNsLastFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrBrNsLastFilter_Type.__name__ = "AsciiString"
_VrBrNsLastFilter_Object = MibTableColumn
vrBrNsLastFilter = _VrBrNsLastFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 3, 10, 1, 2),
    _VrBrNsLastFilter_Type()
)
vrBrNsLastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrNsLastFilter.setStatus("mandatory")
_VrBrTb_ObjectIdentity = ObjectIdentity
vrBrTb = _VrBrTb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4)
)
_VrBrTbRowStatusTable_Object = MibTable
vrBrTbRowStatusTable = _VrBrTbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 1)
)
if mibBuilder.loadTexts:
    vrBrTbRowStatusTable.setStatus("mandatory")
_VrBrTbRowStatusEntry_Object = MibTableRow
vrBrTbRowStatusEntry = _VrBrTbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 1, 1)
)
vrBrTbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbRowStatusEntry.setStatus("mandatory")
_VrBrTbRowStatus_Type = RowStatus
_VrBrTbRowStatus_Object = MibTableColumn
vrBrTbRowStatus = _VrBrTbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 1, 1, 1),
    _VrBrTbRowStatus_Type()
)
vrBrTbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbRowStatus.setStatus("mandatory")
_VrBrTbComponentName_Type = DisplayString
_VrBrTbComponentName_Object = MibTableColumn
vrBrTbComponentName = _VrBrTbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 1, 1, 2),
    _VrBrTbComponentName_Type()
)
vrBrTbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbComponentName.setStatus("mandatory")
_VrBrTbStorageType_Type = StorageType
_VrBrTbStorageType_Object = MibTableColumn
vrBrTbStorageType = _VrBrTbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 1, 1, 4),
    _VrBrTbStorageType_Type()
)
vrBrTbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStorageType.setStatus("mandatory")
_VrBrTbIndex_Type = NonReplicated
_VrBrTbIndex_Object = MibTableColumn
vrBrTbIndex = _VrBrTbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 1, 1, 10),
    _VrBrTbIndex_Type()
)
vrBrTbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbIndex.setStatus("mandatory")
_VrBrTbStp_ObjectIdentity = ObjectIdentity
vrBrTbStp = _VrBrTbStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2)
)
_VrBrTbStpRowStatusTable_Object = MibTable
vrBrTbStpRowStatusTable = _VrBrTbStpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrBrTbStpRowStatusTable.setStatus("mandatory")
_VrBrTbStpRowStatusEntry_Object = MibTableRow
vrBrTbStpRowStatusEntry = _VrBrTbStpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 1, 1)
)
vrBrTbStpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbStpIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbStpRowStatusEntry.setStatus("mandatory")
_VrBrTbStpRowStatus_Type = RowStatus
_VrBrTbStpRowStatus_Object = MibTableColumn
vrBrTbStpRowStatus = _VrBrTbStpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 1, 1, 1),
    _VrBrTbStpRowStatus_Type()
)
vrBrTbStpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpRowStatus.setStatus("mandatory")
_VrBrTbStpComponentName_Type = DisplayString
_VrBrTbStpComponentName_Object = MibTableColumn
vrBrTbStpComponentName = _VrBrTbStpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 1, 1, 2),
    _VrBrTbStpComponentName_Type()
)
vrBrTbStpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpComponentName.setStatus("mandatory")
_VrBrTbStpStorageType_Type = StorageType
_VrBrTbStpStorageType_Object = MibTableColumn
vrBrTbStpStorageType = _VrBrTbStpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 1, 1, 4),
    _VrBrTbStpStorageType_Type()
)
vrBrTbStpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpStorageType.setStatus("mandatory")


class _VrBrTbStpIndex_Type(Integer32):
    """Custom type vrBrTbStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrBrTbStpIndex_Type.__name__ = "Integer32"
_VrBrTbStpIndex_Object = MibTableColumn
vrBrTbStpIndex = _VrBrTbStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 1, 1, 10),
    _VrBrTbStpIndex_Type()
)
vrBrTbStpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbStpIndex.setStatus("mandatory")
_VrBrTbStpProvTable_Object = MibTable
vrBrTbStpProvTable = _VrBrTbStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10)
)
if mibBuilder.loadTexts:
    vrBrTbStpProvTable.setStatus("mandatory")
_VrBrTbStpProvEntry_Object = MibTableRow
vrBrTbStpProvEntry = _VrBrTbStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1)
)
vrBrTbStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbStpIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbStpProvEntry.setStatus("mandatory")


class _VrBrTbStpStpMode_Type(Integer32):
    """Custom type vrBrTbStpStpMode based on Integer32"""
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


_VrBrTbStpStpMode_Type.__name__ = "Integer32"
_VrBrTbStpStpMode_Object = MibTableColumn
vrBrTbStpStpMode = _VrBrTbStpStpMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1, 1),
    _VrBrTbStpStpMode_Type()
)
vrBrTbStpStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpStpMode.setStatus("mandatory")


class _VrBrTbStpProtocolSpec_Type(Integer32):
    """Custom type vrBrTbStpProtocolSpec based on Integer32"""
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


_VrBrTbStpProtocolSpec_Type.__name__ = "Integer32"
_VrBrTbStpProtocolSpec_Object = MibTableColumn
vrBrTbStpProtocolSpec = _VrBrTbStpProtocolSpec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1, 2),
    _VrBrTbStpProtocolSpec_Type()
)
vrBrTbStpProtocolSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpProtocolSpec.setStatus("mandatory")


class _VrBrTbStpPriority_Type(Unsigned32):
    """Custom type vrBrTbStpPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrBrTbStpPriority_Type.__name__ = "Unsigned32"
_VrBrTbStpPriority_Object = MibTableColumn
vrBrTbStpPriority = _VrBrTbStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1, 3),
    _VrBrTbStpPriority_Type()
)
vrBrTbStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpPriority.setStatus("mandatory")


class _VrBrTbStpBridgeMaxAge_Type(Unsigned32):
    """Custom type vrBrTbStpBridgeMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_VrBrTbStpBridgeMaxAge_Type.__name__ = "Unsigned32"
_VrBrTbStpBridgeMaxAge_Object = MibTableColumn
vrBrTbStpBridgeMaxAge = _VrBrTbStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1, 4),
    _VrBrTbStpBridgeMaxAge_Type()
)
vrBrTbStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpBridgeMaxAge.setStatus("mandatory")


class _VrBrTbStpBridgeHelloTime_Type(Unsigned32):
    """Custom type vrBrTbStpBridgeHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VrBrTbStpBridgeHelloTime_Type.__name__ = "Unsigned32"
_VrBrTbStpBridgeHelloTime_Object = MibTableColumn
vrBrTbStpBridgeHelloTime = _VrBrTbStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1, 5),
    _VrBrTbStpBridgeHelloTime_Type()
)
vrBrTbStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpBridgeHelloTime.setStatus("mandatory")


class _VrBrTbStpBridgeForwardDelay_Type(Unsigned32):
    """Custom type vrBrTbStpBridgeForwardDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_VrBrTbStpBridgeForwardDelay_Type.__name__ = "Unsigned32"
_VrBrTbStpBridgeForwardDelay_Object = MibTableColumn
vrBrTbStpBridgeForwardDelay = _VrBrTbStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 10, 1, 6),
    _VrBrTbStpBridgeForwardDelay_Type()
)
vrBrTbStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbStpBridgeForwardDelay.setStatus("mandatory")
_VrBrTbStpOperTable_Object = MibTable
vrBrTbStpOperTable = _VrBrTbStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11)
)
if mibBuilder.loadTexts:
    vrBrTbStpOperTable.setStatus("mandatory")
_VrBrTbStpOperEntry_Object = MibTableRow
vrBrTbStpOperEntry = _VrBrTbStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1)
)
vrBrTbStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbStpIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbStpOperEntry.setStatus("mandatory")


class _VrBrTbStpBridgeId_Type(BridgeId):
    """Custom type vrBrTbStpBridgeId based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrBrTbStpBridgeId_Type.__name__ = "BridgeId"
_VrBrTbStpBridgeId_Object = MibTableColumn
vrBrTbStpBridgeId = _VrBrTbStpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 1),
    _VrBrTbStpBridgeId_Type()
)
vrBrTbStpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpBridgeId.setStatus("mandatory")


class _VrBrTbStpRootPortName_Type(AsciiString):
    """Custom type vrBrTbStpRootPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrBrTbStpRootPortName_Type.__name__ = "AsciiString"
_VrBrTbStpRootPortName_Object = MibTableColumn
vrBrTbStpRootPortName = _VrBrTbStpRootPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 2),
    _VrBrTbStpRootPortName_Type()
)
vrBrTbStpRootPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpRootPortName.setStatus("mandatory")


class _VrBrTbStpTimeSinceTopologyChange_Type(Unsigned32):
    """Custom type vrBrTbStpTimeSinceTopologyChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrBrTbStpTimeSinceTopologyChange_Type.__name__ = "Unsigned32"
_VrBrTbStpTimeSinceTopologyChange_Object = MibTableColumn
vrBrTbStpTimeSinceTopologyChange = _VrBrTbStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 3),
    _VrBrTbStpTimeSinceTopologyChange_Type()
)
vrBrTbStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpTimeSinceTopologyChange.setStatus("mandatory")


class _VrBrTbStpTopologyChangeDetect_Type(Integer32):
    """Custom type vrBrTbStpTopologyChangeDetect based on Integer32"""
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


_VrBrTbStpTopologyChangeDetect_Type.__name__ = "Integer32"
_VrBrTbStpTopologyChangeDetect_Object = MibTableColumn
vrBrTbStpTopologyChangeDetect = _VrBrTbStpTopologyChangeDetect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 4),
    _VrBrTbStpTopologyChangeDetect_Type()
)
vrBrTbStpTopologyChangeDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpTopologyChangeDetect.setStatus("mandatory")
_VrBrTbStpTopologyChanges_Type = Counter32
_VrBrTbStpTopologyChanges_Object = MibTableColumn
vrBrTbStpTopologyChanges = _VrBrTbStpTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 5),
    _VrBrTbStpTopologyChanges_Type()
)
vrBrTbStpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpTopologyChanges.setStatus("mandatory")


class _VrBrTbStpDesignatedRoot_Type(BridgeId):
    """Custom type vrBrTbStpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrBrTbStpDesignatedRoot_Type.__name__ = "BridgeId"
_VrBrTbStpDesignatedRoot_Object = MibTableColumn
vrBrTbStpDesignatedRoot = _VrBrTbStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 6),
    _VrBrTbStpDesignatedRoot_Type()
)
vrBrTbStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpDesignatedRoot.setStatus("mandatory")


class _VrBrTbStpRootCost_Type(Unsigned32):
    """Custom type vrBrTbStpRootCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrBrTbStpRootCost_Type.__name__ = "Unsigned32"
_VrBrTbStpRootCost_Object = MibTableColumn
vrBrTbStpRootCost = _VrBrTbStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 8),
    _VrBrTbStpRootCost_Type()
)
vrBrTbStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpRootCost.setStatus("mandatory")


class _VrBrTbStpMaxAge_Type(Unsigned32):
    """Custom type vrBrTbStpMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_VrBrTbStpMaxAge_Type.__name__ = "Unsigned32"
_VrBrTbStpMaxAge_Object = MibTableColumn
vrBrTbStpMaxAge = _VrBrTbStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 9),
    _VrBrTbStpMaxAge_Type()
)
vrBrTbStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpMaxAge.setStatus("mandatory")


class _VrBrTbStpAgingTimeOper_Type(Unsigned32):
    """Custom type vrBrTbStpAgingTimeOper based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VrBrTbStpAgingTimeOper_Type.__name__ = "Unsigned32"
_VrBrTbStpAgingTimeOper_Object = MibTableColumn
vrBrTbStpAgingTimeOper = _VrBrTbStpAgingTimeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 10),
    _VrBrTbStpAgingTimeOper_Type()
)
vrBrTbStpAgingTimeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpAgingTimeOper.setStatus("mandatory")


class _VrBrTbStpHelloTime_Type(Unsigned32):
    """Custom type vrBrTbStpHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VrBrTbStpHelloTime_Type.__name__ = "Unsigned32"
_VrBrTbStpHelloTime_Object = MibTableColumn
vrBrTbStpHelloTime = _VrBrTbStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 11),
    _VrBrTbStpHelloTime_Type()
)
vrBrTbStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpHelloTime.setStatus("mandatory")


class _VrBrTbStpHoldTime_Type(Unsigned32):
    """Custom type vrBrTbStpHoldTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
    )


_VrBrTbStpHoldTime_Type.__name__ = "Unsigned32"
_VrBrTbStpHoldTime_Object = MibTableColumn
vrBrTbStpHoldTime = _VrBrTbStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 12),
    _VrBrTbStpHoldTime_Type()
)
vrBrTbStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpHoldTime.setStatus("mandatory")


class _VrBrTbStpFwdDelay_Type(Unsigned32):
    """Custom type vrBrTbStpFwdDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_VrBrTbStpFwdDelay_Type.__name__ = "Unsigned32"
_VrBrTbStpFwdDelay_Object = MibTableColumn
vrBrTbStpFwdDelay = _VrBrTbStpFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 2, 11, 1, 13),
    _VrBrTbStpFwdDelay_Type()
)
vrBrTbStpFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbStpFwdDelay.setStatus("mandatory")
_VrBrTbSte_ObjectIdentity = ObjectIdentity
vrBrTbSte = _VrBrTbSte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3)
)
_VrBrTbSteRowStatusTable_Object = MibTable
vrBrTbSteRowStatusTable = _VrBrTbSteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    vrBrTbSteRowStatusTable.setStatus("mandatory")
_VrBrTbSteRowStatusEntry_Object = MibTableRow
vrBrTbSteRowStatusEntry = _VrBrTbSteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1, 1)
)
vrBrTbSteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteReceivePortIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbSteRowStatusEntry.setStatus("mandatory")
_VrBrTbSteRowStatus_Type = RowStatus
_VrBrTbSteRowStatus_Object = MibTableColumn
vrBrTbSteRowStatus = _VrBrTbSteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1, 1, 1),
    _VrBrTbSteRowStatus_Type()
)
vrBrTbSteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbSteRowStatus.setStatus("mandatory")
_VrBrTbSteComponentName_Type = DisplayString
_VrBrTbSteComponentName_Object = MibTableColumn
vrBrTbSteComponentName = _VrBrTbSteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1, 1, 2),
    _VrBrTbSteComponentName_Type()
)
vrBrTbSteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbSteComponentName.setStatus("mandatory")
_VrBrTbSteStorageType_Type = StorageType
_VrBrTbSteStorageType_Object = MibTableColumn
vrBrTbSteStorageType = _VrBrTbSteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1, 1, 4),
    _VrBrTbSteStorageType_Type()
)
vrBrTbSteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbSteStorageType.setStatus("mandatory")


class _VrBrTbSteAddressIndex_Type(DashedHexString):
    """Custom type vrBrTbSteAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrTbSteAddressIndex_Type.__name__ = "DashedHexString"
_VrBrTbSteAddressIndex_Object = MibTableColumn
vrBrTbSteAddressIndex = _VrBrTbSteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1, 1, 10),
    _VrBrTbSteAddressIndex_Type()
)
vrBrTbSteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbSteAddressIndex.setStatus("mandatory")


class _VrBrTbSteReceivePortIndex_Type(AsciiStringIndex):
    """Custom type vrBrTbSteReceivePortIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 29),
    )


_VrBrTbSteReceivePortIndex_Type.__name__ = "AsciiStringIndex"
_VrBrTbSteReceivePortIndex_Object = MibTableColumn
vrBrTbSteReceivePortIndex = _VrBrTbSteReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 1, 1, 11),
    _VrBrTbSteReceivePortIndex_Type()
)
vrBrTbSteReceivePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbSteReceivePortIndex.setStatus("mandatory")
_VrBrTbSteProvTable_Object = MibTable
vrBrTbSteProvTable = _VrBrTbSteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 10)
)
if mibBuilder.loadTexts:
    vrBrTbSteProvTable.setStatus("mandatory")
_VrBrTbSteProvEntry_Object = MibTableRow
vrBrTbSteProvEntry = _VrBrTbSteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 10, 1)
)
vrBrTbSteProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteReceivePortIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbSteProvEntry.setStatus("mandatory")


class _VrBrTbSteStatus_Type(Integer32):
    """Custom type vrBrTbSteStatus based on Integer32"""
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


_VrBrTbSteStatus_Type.__name__ = "Integer32"
_VrBrTbSteStatus_Object = MibTableColumn
vrBrTbSteStatus = _VrBrTbSteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 10, 1, 1),
    _VrBrTbSteStatus_Type()
)
vrBrTbSteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbSteStatus.setStatus("mandatory")
_VrBrTbSteAtgtTable_Object = MibTable
vrBrTbSteAtgtTable = _VrBrTbSteAtgtTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 271)
)
if mibBuilder.loadTexts:
    vrBrTbSteAtgtTable.setStatus("mandatory")
_VrBrTbSteAtgtEntry_Object = MibTableRow
vrBrTbSteAtgtEntry = _VrBrTbSteAtgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 271, 1)
)
vrBrTbSteAtgtEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteReceivePortIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbSteAtgtValue"),
)
if mibBuilder.loadTexts:
    vrBrTbSteAtgtEntry.setStatus("mandatory")


class _VrBrTbSteAtgtValue_Type(AsciiString):
    """Custom type vrBrTbSteAtgtValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrBrTbSteAtgtValue_Type.__name__ = "AsciiString"
_VrBrTbSteAtgtValue_Object = MibTableColumn
vrBrTbSteAtgtValue = _VrBrTbSteAtgtValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 271, 1, 1),
    _VrBrTbSteAtgtValue_Type()
)
vrBrTbSteAtgtValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbSteAtgtValue.setStatus("mandatory")
_VrBrTbSteAtgtRowStatus_Type = RowStatus
_VrBrTbSteAtgtRowStatus_Object = MibTableColumn
vrBrTbSteAtgtRowStatus = _VrBrTbSteAtgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 3, 271, 1, 2),
    _VrBrTbSteAtgtRowStatus_Type()
)
vrBrTbSteAtgtRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrBrTbSteAtgtRowStatus.setStatus("mandatory")
_VrBrTbFte_ObjectIdentity = ObjectIdentity
vrBrTbFte = _VrBrTbFte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4)
)
_VrBrTbFteRowStatusTable_Object = MibTable
vrBrTbFteRowStatusTable = _VrBrTbFteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    vrBrTbFteRowStatusTable.setStatus("mandatory")
_VrBrTbFteRowStatusEntry_Object = MibTableRow
vrBrTbFteRowStatusEntry = _VrBrTbFteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1, 1)
)
vrBrTbFteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbFteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbFteRowStatusEntry.setStatus("mandatory")
_VrBrTbFteRowStatus_Type = RowStatus
_VrBrTbFteRowStatus_Object = MibTableColumn
vrBrTbFteRowStatus = _VrBrTbFteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1, 1, 1),
    _VrBrTbFteRowStatus_Type()
)
vrBrTbFteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFteRowStatus.setStatus("mandatory")
_VrBrTbFteComponentName_Type = DisplayString
_VrBrTbFteComponentName_Object = MibTableColumn
vrBrTbFteComponentName = _VrBrTbFteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1, 1, 2),
    _VrBrTbFteComponentName_Type()
)
vrBrTbFteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFteComponentName.setStatus("mandatory")
_VrBrTbFteStorageType_Type = StorageType
_VrBrTbFteStorageType_Object = MibTableColumn
vrBrTbFteStorageType = _VrBrTbFteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1, 1, 4),
    _VrBrTbFteStorageType_Type()
)
vrBrTbFteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFteStorageType.setStatus("mandatory")


class _VrBrTbFteAddressIndex_Type(DashedHexString):
    """Custom type vrBrTbFteAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrTbFteAddressIndex_Type.__name__ = "DashedHexString"
_VrBrTbFteAddressIndex_Object = MibTableColumn
vrBrTbFteAddressIndex = _VrBrTbFteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1, 1, 10),
    _VrBrTbFteAddressIndex_Type()
)
vrBrTbFteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbFteAddressIndex.setStatus("mandatory")


class _VrBrTbFteDomainNumIndex_Type(Integer32):
    """Custom type vrBrTbFteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrBrTbFteDomainNumIndex_Type.__name__ = "Integer32"
_VrBrTbFteDomainNumIndex_Object = MibTableColumn
vrBrTbFteDomainNumIndex = _VrBrTbFteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 1, 1, 11),
    _VrBrTbFteDomainNumIndex_Type()
)
vrBrTbFteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbFteDomainNumIndex.setStatus("mandatory")
_VrBrTbFteOperTable_Object = MibTable
vrBrTbFteOperTable = _VrBrTbFteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 10)
)
if mibBuilder.loadTexts:
    vrBrTbFteOperTable.setStatus("mandatory")
_VrBrTbFteOperEntry_Object = MibTableRow
vrBrTbFteOperEntry = _VrBrTbFteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 10, 1)
)
vrBrTbFteOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbFteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbFteOperEntry.setStatus("mandatory")


class _VrBrTbFtePort_Type(AsciiString):
    """Custom type vrBrTbFtePort based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrBrTbFtePort_Type.__name__ = "AsciiString"
_VrBrTbFtePort_Object = MibTableColumn
vrBrTbFtePort = _VrBrTbFtePort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 10, 1, 3),
    _VrBrTbFtePort_Type()
)
vrBrTbFtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFtePort.setStatus("mandatory")


class _VrBrTbFteAgeOfEntry_Type(Gauge32):
    """Custom type vrBrTbFteAgeOfEntry based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_VrBrTbFteAgeOfEntry_Type.__name__ = "Gauge32"
_VrBrTbFteAgeOfEntry_Object = MibTableColumn
vrBrTbFteAgeOfEntry = _VrBrTbFteAgeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 10, 1, 4),
    _VrBrTbFteAgeOfEntry_Type()
)
vrBrTbFteAgeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFteAgeOfEntry.setStatus("mandatory")


class _VrBrTbFtePeerAddressInfo_Type(BridgeId):
    """Custom type vrBrTbFtePeerAddressInfo based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrBrTbFtePeerAddressInfo_Type.__name__ = "BridgeId"
_VrBrTbFtePeerAddressInfo_Object = MibTableColumn
vrBrTbFtePeerAddressInfo = _VrBrTbFtePeerAddressInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 10, 1, 5),
    _VrBrTbFtePeerAddressInfo_Type()
)
vrBrTbFtePeerAddressInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFtePeerAddressInfo.setStatus("mandatory")


class _VrBrTbFteStatus_Type(Integer32):
    """Custom type vrBrTbFteStatus based on Integer32"""
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


_VrBrTbFteStatus_Type.__name__ = "Integer32"
_VrBrTbFteStatus_Object = MibTableColumn
vrBrTbFteStatus = _VrBrTbFteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 4, 10, 1, 6),
    _VrBrTbFteStatus_Type()
)
vrBrTbFteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbFteStatus.setStatus("mandatory")
_VrBrTbNcFte_ObjectIdentity = ObjectIdentity
vrBrTbNcFte = _VrBrTbNcFte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5)
)
_VrBrTbNcFteRowStatusTable_Object = MibTable
vrBrTbNcFteRowStatusTable = _VrBrTbNcFteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1)
)
if mibBuilder.loadTexts:
    vrBrTbNcFteRowStatusTable.setStatus("mandatory")
_VrBrTbNcFteRowStatusEntry_Object = MibTableRow
vrBrTbNcFteRowStatusEntry = _VrBrTbNcFteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1, 1)
)
vrBrTbNcFteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbNcFteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbNcFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbNcFteRowStatusEntry.setStatus("mandatory")
_VrBrTbNcFteRowStatus_Type = RowStatus
_VrBrTbNcFteRowStatus_Object = MibTableColumn
vrBrTbNcFteRowStatus = _VrBrTbNcFteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1, 1, 1),
    _VrBrTbNcFteRowStatus_Type()
)
vrBrTbNcFteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFteRowStatus.setStatus("mandatory")
_VrBrTbNcFteComponentName_Type = DisplayString
_VrBrTbNcFteComponentName_Object = MibTableColumn
vrBrTbNcFteComponentName = _VrBrTbNcFteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1, 1, 2),
    _VrBrTbNcFteComponentName_Type()
)
vrBrTbNcFteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFteComponentName.setStatus("mandatory")
_VrBrTbNcFteStorageType_Type = StorageType
_VrBrTbNcFteStorageType_Object = MibTableColumn
vrBrTbNcFteStorageType = _VrBrTbNcFteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1, 1, 4),
    _VrBrTbNcFteStorageType_Type()
)
vrBrTbNcFteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFteStorageType.setStatus("mandatory")


class _VrBrTbNcFteAddressIndex_Type(DashedHexString):
    """Custom type vrBrTbNcFteAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrTbNcFteAddressIndex_Type.__name__ = "DashedHexString"
_VrBrTbNcFteAddressIndex_Object = MibTableColumn
vrBrTbNcFteAddressIndex = _VrBrTbNcFteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1, 1, 10),
    _VrBrTbNcFteAddressIndex_Type()
)
vrBrTbNcFteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbNcFteAddressIndex.setStatus("mandatory")


class _VrBrTbNcFteDomainNumIndex_Type(Integer32):
    """Custom type vrBrTbNcFteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrBrTbNcFteDomainNumIndex_Type.__name__ = "Integer32"
_VrBrTbNcFteDomainNumIndex_Object = MibTableColumn
vrBrTbNcFteDomainNumIndex = _VrBrTbNcFteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 1, 1, 11),
    _VrBrTbNcFteDomainNumIndex_Type()
)
vrBrTbNcFteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrTbNcFteDomainNumIndex.setStatus("mandatory")
_VrBrTbNcFteOperTable_Object = MibTable
vrBrTbNcFteOperTable = _VrBrTbNcFteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 10)
)
if mibBuilder.loadTexts:
    vrBrTbNcFteOperTable.setStatus("mandatory")
_VrBrTbNcFteOperEntry_Object = MibTableRow
vrBrTbNcFteOperEntry = _VrBrTbNcFteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 10, 1)
)
vrBrTbNcFteOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbNcFteAddressIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbNcFteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbNcFteOperEntry.setStatus("mandatory")


class _VrBrTbNcFtePort_Type(AsciiString):
    """Custom type vrBrTbNcFtePort based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrBrTbNcFtePort_Type.__name__ = "AsciiString"
_VrBrTbNcFtePort_Object = MibTableColumn
vrBrTbNcFtePort = _VrBrTbNcFtePort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 10, 1, 3),
    _VrBrTbNcFtePort_Type()
)
vrBrTbNcFtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFtePort.setStatus("mandatory")


class _VrBrTbNcFteAgeOfEntry_Type(Gauge32):
    """Custom type vrBrTbNcFteAgeOfEntry based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_VrBrTbNcFteAgeOfEntry_Type.__name__ = "Gauge32"
_VrBrTbNcFteAgeOfEntry_Object = MibTableColumn
vrBrTbNcFteAgeOfEntry = _VrBrTbNcFteAgeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 10, 1, 4),
    _VrBrTbNcFteAgeOfEntry_Type()
)
vrBrTbNcFteAgeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFteAgeOfEntry.setStatus("mandatory")


class _VrBrTbNcFtePeerAddressInfo_Type(BridgeId):
    """Custom type vrBrTbNcFtePeerAddressInfo based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrBrTbNcFtePeerAddressInfo_Type.__name__ = "BridgeId"
_VrBrTbNcFtePeerAddressInfo_Object = MibTableColumn
vrBrTbNcFtePeerAddressInfo = _VrBrTbNcFtePeerAddressInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 10, 1, 5),
    _VrBrTbNcFtePeerAddressInfo_Type()
)
vrBrTbNcFtePeerAddressInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFtePeerAddressInfo.setStatus("mandatory")


class _VrBrTbNcFteStatus_Type(Integer32):
    """Custom type vrBrTbNcFteStatus based on Integer32"""
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


_VrBrTbNcFteStatus_Type.__name__ = "Integer32"
_VrBrTbNcFteStatus_Object = MibTableColumn
vrBrTbNcFteStatus = _VrBrTbNcFteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 5, 10, 1, 6),
    _VrBrTbNcFteStatus_Type()
)
vrBrTbNcFteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNcFteStatus.setStatus("mandatory")
_VrBrTbProvTable_Object = MibTable
vrBrTbProvTable = _VrBrTbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 10)
)
if mibBuilder.loadTexts:
    vrBrTbProvTable.setStatus("mandatory")
_VrBrTbProvEntry_Object = MibTableRow
vrBrTbProvEntry = _VrBrTbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 10, 1)
)
vrBrTbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbProvEntry.setStatus("mandatory")


class _VrBrTbFwdTableNumEntries_Type(Unsigned32):
    """Custom type vrBrTbFwdTableNumEntries based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrBrTbFwdTableNumEntries_Type.__name__ = "Unsigned32"
_VrBrTbFwdTableNumEntries_Object = MibTableColumn
vrBrTbFwdTableNumEntries = _VrBrTbFwdTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 10, 1, 1),
    _VrBrTbFwdTableNumEntries_Type()
)
vrBrTbFwdTableNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbFwdTableNumEntries.setStatus("mandatory")


class _VrBrTbAgingTime_Type(Unsigned32):
    """Custom type vrBrTbAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VrBrTbAgingTime_Type.__name__ = "Unsigned32"
_VrBrTbAgingTime_Object = MibTableColumn
vrBrTbAgingTime = _VrBrTbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 10, 1, 2),
    _VrBrTbAgingTime_Type()
)
vrBrTbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrTbAgingTime.setStatus("mandatory")
_VrBrTbStatsTable_Object = MibTable
vrBrTbStatsTable = _VrBrTbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 11)
)
if mibBuilder.loadTexts:
    vrBrTbStatsTable.setStatus("mandatory")
_VrBrTbStatsEntry_Object = MibTableRow
vrBrTbStatsEntry = _VrBrTbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 11, 1)
)
vrBrTbStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrTbIndex"),
)
if mibBuilder.loadTexts:
    vrBrTbStatsEntry.setStatus("mandatory")
_VrBrTbLearnedEntryDiscards_Type = Counter32
_VrBrTbLearnedEntryDiscards_Object = MibTableColumn
vrBrTbLearnedEntryDiscards = _VrBrTbLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 11, 1, 1),
    _VrBrTbLearnedEntryDiscards_Type()
)
vrBrTbLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbLearnedEntryDiscards.setStatus("mandatory")
_VrBrTbTotalForwardingTableEntries_Type = Counter32
_VrBrTbTotalForwardingTableEntries_Object = MibTableColumn
vrBrTbTotalForwardingTableEntries = _VrBrTbTotalForwardingTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 11, 1, 2),
    _VrBrTbTotalForwardingTableEntries_Type()
)
vrBrTbTotalForwardingTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbTotalForwardingTableEntries.setStatus("mandatory")


class _VrBrTbNumFtEntriesFree_Type(Gauge32):
    """Custom type vrBrTbNumFtEntriesFree based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrBrTbNumFtEntriesFree_Type.__name__ = "Gauge32"
_VrBrTbNumFtEntriesFree_Object = MibTableColumn
vrBrTbNumFtEntriesFree = _VrBrTbNumFtEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 11, 1, 3),
    _VrBrTbNumFtEntriesFree_Type()
)
vrBrTbNumFtEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNumFtEntriesFree.setStatus("mandatory")
_VrBrTbNumFtEntriesDenied_Type = Counter32
_VrBrTbNumFtEntriesDenied_Object = MibTableColumn
vrBrTbNumFtEntriesDenied = _VrBrTbNumFtEntriesDenied_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 4, 11, 1, 4),
    _VrBrTbNumFtEntriesDenied_Type()
)
vrBrTbNumFtEntriesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrTbNumFtEntriesDenied.setStatus("mandatory")
_VrBrSrb_ObjectIdentity = ObjectIdentity
vrBrSrb = _VrBrSrb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5)
)
_VrBrSrbRowStatusTable_Object = MibTable
vrBrSrbRowStatusTable = _VrBrSrbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 1)
)
if mibBuilder.loadTexts:
    vrBrSrbRowStatusTable.setStatus("mandatory")
_VrBrSrbRowStatusEntry_Object = MibTableRow
vrBrSrbRowStatusEntry = _VrBrSrbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 1, 1)
)
vrBrSrbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbRowStatusEntry.setStatus("mandatory")
_VrBrSrbRowStatus_Type = RowStatus
_VrBrSrbRowStatus_Object = MibTableColumn
vrBrSrbRowStatus = _VrBrSrbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 1, 1, 1),
    _VrBrSrbRowStatus_Type()
)
vrBrSrbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbRowStatus.setStatus("mandatory")
_VrBrSrbComponentName_Type = DisplayString
_VrBrSrbComponentName_Object = MibTableColumn
vrBrSrbComponentName = _VrBrSrbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 1, 1, 2),
    _VrBrSrbComponentName_Type()
)
vrBrSrbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbComponentName.setStatus("mandatory")
_VrBrSrbStorageType_Type = StorageType
_VrBrSrbStorageType_Object = MibTableColumn
vrBrSrbStorageType = _VrBrSrbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 1, 1, 4),
    _VrBrSrbStorageType_Type()
)
vrBrSrbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStorageType.setStatus("mandatory")
_VrBrSrbIndex_Type = NonReplicated
_VrBrSrbIndex_Object = MibTableColumn
vrBrSrbIndex = _VrBrSrbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 1, 1, 10),
    _VrBrSrbIndex_Type()
)
vrBrSrbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrSrbIndex.setStatus("mandatory")
_VrBrSrbStp_ObjectIdentity = ObjectIdentity
vrBrSrbStp = _VrBrSrbStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2)
)
_VrBrSrbStpRowStatusTable_Object = MibTable
vrBrSrbStpRowStatusTable = _VrBrSrbStpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vrBrSrbStpRowStatusTable.setStatus("mandatory")
_VrBrSrbStpRowStatusEntry_Object = MibTableRow
vrBrSrbStpRowStatusEntry = _VrBrSrbStpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 1, 1)
)
vrBrSrbStpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbStpIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbStpRowStatusEntry.setStatus("mandatory")
_VrBrSrbStpRowStatus_Type = RowStatus
_VrBrSrbStpRowStatus_Object = MibTableColumn
vrBrSrbStpRowStatus = _VrBrSrbStpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 1, 1, 1),
    _VrBrSrbStpRowStatus_Type()
)
vrBrSrbStpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpRowStatus.setStatus("mandatory")
_VrBrSrbStpComponentName_Type = DisplayString
_VrBrSrbStpComponentName_Object = MibTableColumn
vrBrSrbStpComponentName = _VrBrSrbStpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 1, 1, 2),
    _VrBrSrbStpComponentName_Type()
)
vrBrSrbStpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpComponentName.setStatus("mandatory")
_VrBrSrbStpStorageType_Type = StorageType
_VrBrSrbStpStorageType_Object = MibTableColumn
vrBrSrbStpStorageType = _VrBrSrbStpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 1, 1, 4),
    _VrBrSrbStpStorageType_Type()
)
vrBrSrbStpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpStorageType.setStatus("mandatory")


class _VrBrSrbStpIndex_Type(Integer32):
    """Custom type vrBrSrbStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrBrSrbStpIndex_Type.__name__ = "Integer32"
_VrBrSrbStpIndex_Object = MibTableColumn
vrBrSrbStpIndex = _VrBrSrbStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 1, 1, 10),
    _VrBrSrbStpIndex_Type()
)
vrBrSrbStpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrSrbStpIndex.setStatus("mandatory")
_VrBrSrbStpProvTable_Object = MibTable
vrBrSrbStpProvTable = _VrBrSrbStpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10)
)
if mibBuilder.loadTexts:
    vrBrSrbStpProvTable.setStatus("mandatory")
_VrBrSrbStpProvEntry_Object = MibTableRow
vrBrSrbStpProvEntry = _VrBrSrbStpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1)
)
vrBrSrbStpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbStpIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbStpProvEntry.setStatus("mandatory")


class _VrBrSrbStpStpMode_Type(Integer32):
    """Custom type vrBrSrbStpStpMode based on Integer32"""
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


_VrBrSrbStpStpMode_Type.__name__ = "Integer32"
_VrBrSrbStpStpMode_Object = MibTableColumn
vrBrSrbStpStpMode = _VrBrSrbStpStpMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1, 1),
    _VrBrSrbStpStpMode_Type()
)
vrBrSrbStpStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpStpMode.setStatus("mandatory")


class _VrBrSrbStpProtocolSpec_Type(Integer32):
    """Custom type vrBrSrbStpProtocolSpec based on Integer32"""
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


_VrBrSrbStpProtocolSpec_Type.__name__ = "Integer32"
_VrBrSrbStpProtocolSpec_Object = MibTableColumn
vrBrSrbStpProtocolSpec = _VrBrSrbStpProtocolSpec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1, 2),
    _VrBrSrbStpProtocolSpec_Type()
)
vrBrSrbStpProtocolSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpProtocolSpec.setStatus("mandatory")


class _VrBrSrbStpPriority_Type(Unsigned32):
    """Custom type vrBrSrbStpPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrBrSrbStpPriority_Type.__name__ = "Unsigned32"
_VrBrSrbStpPriority_Object = MibTableColumn
vrBrSrbStpPriority = _VrBrSrbStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1, 3),
    _VrBrSrbStpPriority_Type()
)
vrBrSrbStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpPriority.setStatus("mandatory")


class _VrBrSrbStpBridgeMaxAge_Type(Unsigned32):
    """Custom type vrBrSrbStpBridgeMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_VrBrSrbStpBridgeMaxAge_Type.__name__ = "Unsigned32"
_VrBrSrbStpBridgeMaxAge_Object = MibTableColumn
vrBrSrbStpBridgeMaxAge = _VrBrSrbStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1, 4),
    _VrBrSrbStpBridgeMaxAge_Type()
)
vrBrSrbStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpBridgeMaxAge.setStatus("mandatory")


class _VrBrSrbStpBridgeHelloTime_Type(Unsigned32):
    """Custom type vrBrSrbStpBridgeHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VrBrSrbStpBridgeHelloTime_Type.__name__ = "Unsigned32"
_VrBrSrbStpBridgeHelloTime_Object = MibTableColumn
vrBrSrbStpBridgeHelloTime = _VrBrSrbStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1, 5),
    _VrBrSrbStpBridgeHelloTime_Type()
)
vrBrSrbStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpBridgeHelloTime.setStatus("mandatory")


class _VrBrSrbStpBridgeForwardDelay_Type(Unsigned32):
    """Custom type vrBrSrbStpBridgeForwardDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_VrBrSrbStpBridgeForwardDelay_Type.__name__ = "Unsigned32"
_VrBrSrbStpBridgeForwardDelay_Object = MibTableColumn
vrBrSrbStpBridgeForwardDelay = _VrBrSrbStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 10, 1, 6),
    _VrBrSrbStpBridgeForwardDelay_Type()
)
vrBrSrbStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbStpBridgeForwardDelay.setStatus("mandatory")
_VrBrSrbStpOperTable_Object = MibTable
vrBrSrbStpOperTable = _VrBrSrbStpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11)
)
if mibBuilder.loadTexts:
    vrBrSrbStpOperTable.setStatus("mandatory")
_VrBrSrbStpOperEntry_Object = MibTableRow
vrBrSrbStpOperEntry = _VrBrSrbStpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1)
)
vrBrSrbStpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbStpIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbStpOperEntry.setStatus("mandatory")


class _VrBrSrbStpBridgeId_Type(BridgeId):
    """Custom type vrBrSrbStpBridgeId based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrBrSrbStpBridgeId_Type.__name__ = "BridgeId"
_VrBrSrbStpBridgeId_Object = MibTableColumn
vrBrSrbStpBridgeId = _VrBrSrbStpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 1),
    _VrBrSrbStpBridgeId_Type()
)
vrBrSrbStpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpBridgeId.setStatus("mandatory")


class _VrBrSrbStpRootPortName_Type(AsciiString):
    """Custom type vrBrSrbStpRootPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrBrSrbStpRootPortName_Type.__name__ = "AsciiString"
_VrBrSrbStpRootPortName_Object = MibTableColumn
vrBrSrbStpRootPortName = _VrBrSrbStpRootPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 2),
    _VrBrSrbStpRootPortName_Type()
)
vrBrSrbStpRootPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpRootPortName.setStatus("mandatory")


class _VrBrSrbStpTimeSinceTopologyChange_Type(Unsigned32):
    """Custom type vrBrSrbStpTimeSinceTopologyChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrBrSrbStpTimeSinceTopologyChange_Type.__name__ = "Unsigned32"
_VrBrSrbStpTimeSinceTopologyChange_Object = MibTableColumn
vrBrSrbStpTimeSinceTopologyChange = _VrBrSrbStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 3),
    _VrBrSrbStpTimeSinceTopologyChange_Type()
)
vrBrSrbStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpTimeSinceTopologyChange.setStatus("mandatory")


class _VrBrSrbStpTopologyChangeDetect_Type(Integer32):
    """Custom type vrBrSrbStpTopologyChangeDetect based on Integer32"""
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


_VrBrSrbStpTopologyChangeDetect_Type.__name__ = "Integer32"
_VrBrSrbStpTopologyChangeDetect_Object = MibTableColumn
vrBrSrbStpTopologyChangeDetect = _VrBrSrbStpTopologyChangeDetect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 4),
    _VrBrSrbStpTopologyChangeDetect_Type()
)
vrBrSrbStpTopologyChangeDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpTopologyChangeDetect.setStatus("mandatory")
_VrBrSrbStpTopologyChanges_Type = Counter32
_VrBrSrbStpTopologyChanges_Object = MibTableColumn
vrBrSrbStpTopologyChanges = _VrBrSrbStpTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 5),
    _VrBrSrbStpTopologyChanges_Type()
)
vrBrSrbStpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpTopologyChanges.setStatus("mandatory")


class _VrBrSrbStpDesignatedRoot_Type(BridgeId):
    """Custom type vrBrSrbStpDesignatedRoot based on BridgeId"""
    subtypeSpec = BridgeId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VrBrSrbStpDesignatedRoot_Type.__name__ = "BridgeId"
_VrBrSrbStpDesignatedRoot_Object = MibTableColumn
vrBrSrbStpDesignatedRoot = _VrBrSrbStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 6),
    _VrBrSrbStpDesignatedRoot_Type()
)
vrBrSrbStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpDesignatedRoot.setStatus("mandatory")


class _VrBrSrbStpRootCost_Type(Unsigned32):
    """Custom type vrBrSrbStpRootCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrBrSrbStpRootCost_Type.__name__ = "Unsigned32"
_VrBrSrbStpRootCost_Object = MibTableColumn
vrBrSrbStpRootCost = _VrBrSrbStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 8),
    _VrBrSrbStpRootCost_Type()
)
vrBrSrbStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpRootCost.setStatus("mandatory")


class _VrBrSrbStpMaxAge_Type(Unsigned32):
    """Custom type vrBrSrbStpMaxAge based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_VrBrSrbStpMaxAge_Type.__name__ = "Unsigned32"
_VrBrSrbStpMaxAge_Object = MibTableColumn
vrBrSrbStpMaxAge = _VrBrSrbStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 9),
    _VrBrSrbStpMaxAge_Type()
)
vrBrSrbStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpMaxAge.setStatus("mandatory")


class _VrBrSrbStpAgingTimeOper_Type(Unsigned32):
    """Custom type vrBrSrbStpAgingTimeOper based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VrBrSrbStpAgingTimeOper_Type.__name__ = "Unsigned32"
_VrBrSrbStpAgingTimeOper_Object = MibTableColumn
vrBrSrbStpAgingTimeOper = _VrBrSrbStpAgingTimeOper_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 10),
    _VrBrSrbStpAgingTimeOper_Type()
)
vrBrSrbStpAgingTimeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpAgingTimeOper.setStatus("mandatory")


class _VrBrSrbStpHelloTime_Type(Unsigned32):
    """Custom type vrBrSrbStpHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VrBrSrbStpHelloTime_Type.__name__ = "Unsigned32"
_VrBrSrbStpHelloTime_Object = MibTableColumn
vrBrSrbStpHelloTime = _VrBrSrbStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 11),
    _VrBrSrbStpHelloTime_Type()
)
vrBrSrbStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpHelloTime.setStatus("mandatory")


class _VrBrSrbStpHoldTime_Type(Unsigned32):
    """Custom type vrBrSrbStpHoldTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
    )


_VrBrSrbStpHoldTime_Type.__name__ = "Unsigned32"
_VrBrSrbStpHoldTime_Object = MibTableColumn
vrBrSrbStpHoldTime = _VrBrSrbStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 12),
    _VrBrSrbStpHoldTime_Type()
)
vrBrSrbStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpHoldTime.setStatus("mandatory")


class _VrBrSrbStpFwdDelay_Type(Unsigned32):
    """Custom type vrBrSrbStpFwdDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_VrBrSrbStpFwdDelay_Type.__name__ = "Unsigned32"
_VrBrSrbStpFwdDelay_Object = MibTableColumn
vrBrSrbStpFwdDelay = _VrBrSrbStpFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 2, 11, 1, 13),
    _VrBrSrbStpFwdDelay_Type()
)
vrBrSrbStpFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbStpFwdDelay.setStatus("mandatory")
_VrBrSrbLte_ObjectIdentity = ObjectIdentity
vrBrSrbLte = _VrBrSrbLte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3)
)
_VrBrSrbLteRowStatusTable_Object = MibTable
vrBrSrbLteRowStatusTable = _VrBrSrbLteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1)
)
if mibBuilder.loadTexts:
    vrBrSrbLteRowStatusTable.setStatus("mandatory")
_VrBrSrbLteRowStatusEntry_Object = MibTableRow
vrBrSrbLteRowStatusEntry = _VrBrSrbLteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1, 1)
)
vrBrSrbLteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbLteLanIdIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbLteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbLteRowStatusEntry.setStatus("mandatory")
_VrBrSrbLteRowStatus_Type = RowStatus
_VrBrSrbLteRowStatus_Object = MibTableColumn
vrBrSrbLteRowStatus = _VrBrSrbLteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1, 1, 1),
    _VrBrSrbLteRowStatus_Type()
)
vrBrSrbLteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLteRowStatus.setStatus("mandatory")
_VrBrSrbLteComponentName_Type = DisplayString
_VrBrSrbLteComponentName_Object = MibTableColumn
vrBrSrbLteComponentName = _VrBrSrbLteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1, 1, 2),
    _VrBrSrbLteComponentName_Type()
)
vrBrSrbLteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLteComponentName.setStatus("mandatory")
_VrBrSrbLteStorageType_Type = StorageType
_VrBrSrbLteStorageType_Object = MibTableColumn
vrBrSrbLteStorageType = _VrBrSrbLteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1, 1, 4),
    _VrBrSrbLteStorageType_Type()
)
vrBrSrbLteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLteStorageType.setStatus("mandatory")


class _VrBrSrbLteLanIdIndex_Type(Integer32):
    """Custom type vrBrSrbLteLanIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_VrBrSrbLteLanIdIndex_Type.__name__ = "Integer32"
_VrBrSrbLteLanIdIndex_Object = MibTableColumn
vrBrSrbLteLanIdIndex = _VrBrSrbLteLanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1, 1, 10),
    _VrBrSrbLteLanIdIndex_Type()
)
vrBrSrbLteLanIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrSrbLteLanIdIndex.setStatus("mandatory")


class _VrBrSrbLteDomainNumIndex_Type(Integer32):
    """Custom type vrBrSrbLteDomainNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrBrSrbLteDomainNumIndex_Type.__name__ = "Integer32"
_VrBrSrbLteDomainNumIndex_Object = MibTableColumn
vrBrSrbLteDomainNumIndex = _VrBrSrbLteDomainNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 1, 1, 11),
    _VrBrSrbLteDomainNumIndex_Type()
)
vrBrSrbLteDomainNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrBrSrbLteDomainNumIndex.setStatus("mandatory")
_VrBrSrbLteOperTable_Object = MibTable
vrBrSrbLteOperTable = _VrBrSrbLteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 10)
)
if mibBuilder.loadTexts:
    vrBrSrbLteOperTable.setStatus("mandatory")
_VrBrSrbLteOperEntry_Object = MibTableRow
vrBrSrbLteOperEntry = _VrBrSrbLteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 10, 1)
)
vrBrSrbLteOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbLteLanIdIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbLteDomainNumIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbLteOperEntry.setStatus("mandatory")


class _VrBrSrbLtePortName_Type(AsciiString):
    """Custom type vrBrSrbLtePortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 29),
    )


_VrBrSrbLtePortName_Type.__name__ = "AsciiString"
_VrBrSrbLtePortName_Object = MibTableColumn
vrBrSrbLtePortName = _VrBrSrbLtePortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 10, 1, 1),
    _VrBrSrbLtePortName_Type()
)
vrBrSrbLtePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLtePortName.setStatus("mandatory")


class _VrBrSrbLteAgeOfEntry_Type(Unsigned32):
    """Custom type vrBrSrbLteAgeOfEntry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrBrSrbLteAgeOfEntry_Type.__name__ = "Unsigned32"
_VrBrSrbLteAgeOfEntry_Object = MibTableColumn
vrBrSrbLteAgeOfEntry = _VrBrSrbLteAgeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 10, 1, 2),
    _VrBrSrbLteAgeOfEntry_Type()
)
vrBrSrbLteAgeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLteAgeOfEntry.setStatus("mandatory")


class _VrBrSrbLtePeerMACAddress_Type(DashedHexString):
    """Custom type vrBrSrbLtePeerMACAddress based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrSrbLtePeerMACAddress_Type.__name__ = "DashedHexString"
_VrBrSrbLtePeerMACAddress_Object = MibTableColumn
vrBrSrbLtePeerMACAddress = _VrBrSrbLtePeerMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 10, 1, 3),
    _VrBrSrbLtePeerMACAddress_Type()
)
vrBrSrbLtePeerMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLtePeerMACAddress.setStatus("mandatory")


class _VrBrSrbLteTypeOfEntry_Type(Integer32):
    """Custom type vrBrSrbLteTypeOfEntry based on Integer32"""
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


_VrBrSrbLteTypeOfEntry_Type.__name__ = "Integer32"
_VrBrSrbLteTypeOfEntry_Object = MibTableColumn
vrBrSrbLteTypeOfEntry = _VrBrSrbLteTypeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 3, 10, 1, 4),
    _VrBrSrbLteTypeOfEntry_Type()
)
vrBrSrbLteTypeOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbLteTypeOfEntry.setStatus("mandatory")
_VrBrSrbProvTable_Object = MibTable
vrBrSrbProvTable = _VrBrSrbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 10)
)
if mibBuilder.loadTexts:
    vrBrSrbProvTable.setStatus("mandatory")
_VrBrSrbProvEntry_Object = MibTableRow
vrBrSrbProvEntry = _VrBrSrbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 10, 1)
)
vrBrSrbProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbProvEntry.setStatus("mandatory")


class _VrBrSrbLanIdTableNumEntries_Type(Unsigned32):
    """Custom type vrBrSrbLanIdTableNumEntries based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 65535),
    )


_VrBrSrbLanIdTableNumEntries_Type.__name__ = "Unsigned32"
_VrBrSrbLanIdTableNumEntries_Object = MibTableColumn
vrBrSrbLanIdTableNumEntries = _VrBrSrbLanIdTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 10, 1, 1),
    _VrBrSrbLanIdTableNumEntries_Type()
)
vrBrSrbLanIdTableNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbLanIdTableNumEntries.setStatus("mandatory")


class _VrBrSrbAgingTime_Type(Unsigned32):
    """Custom type vrBrSrbAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VrBrSrbAgingTime_Type.__name__ = "Unsigned32"
_VrBrSrbAgingTime_Object = MibTableColumn
vrBrSrbAgingTime = _VrBrSrbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 10, 1, 2),
    _VrBrSrbAgingTime_Type()
)
vrBrSrbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrSrbAgingTime.setStatus("mandatory")


class _VrBrSrbBridgeLfMode_Type(Integer32):
    """Custom type vrBrSrbBridgeLfMode based on Integer32"""
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


_VrBrSrbBridgeLfMode_Type.__name__ = "Integer32"
_VrBrSrbBridgeLfMode_Object = MibTableColumn
vrBrSrbBridgeLfMode = _VrBrSrbBridgeLfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 10, 1, 3),
    _VrBrSrbBridgeLfMode_Type()
)
vrBrSrbBridgeLfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbBridgeLfMode.setStatus("mandatory")
_VrBrSrbStatsTable_Object = MibTable
vrBrSrbStatsTable = _VrBrSrbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 11)
)
if mibBuilder.loadTexts:
    vrBrSrbStatsTable.setStatus("mandatory")
_VrBrSrbStatsEntry_Object = MibTableRow
vrBrSrbStatsEntry = _VrBrSrbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 11, 1)
)
vrBrSrbStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrSrbIndex"),
)
if mibBuilder.loadTexts:
    vrBrSrbStatsEntry.setStatus("mandatory")
_VrBrSrbTotalLanIdTableEntries_Type = Counter32
_VrBrSrbTotalLanIdTableEntries_Object = MibTableColumn
vrBrSrbTotalLanIdTableEntries = _VrBrSrbTotalLanIdTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 11, 1, 1),
    _VrBrSrbTotalLanIdTableEntries_Type()
)
vrBrSrbTotalLanIdTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbTotalLanIdTableEntries.setStatus("mandatory")
_VrBrSrbNumLanIdtEntriesFree_Type = Counter32
_VrBrSrbNumLanIdtEntriesFree_Object = MibTableColumn
vrBrSrbNumLanIdtEntriesFree = _VrBrSrbNumLanIdtEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 11, 1, 2),
    _VrBrSrbNumLanIdtEntriesFree_Type()
)
vrBrSrbNumLanIdtEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbNumLanIdtEntriesFree.setStatus("mandatory")
_VrBrSrbNumLanIdtEntriesDenied_Type = Counter32
_VrBrSrbNumLanIdtEntriesDenied_Object = MibTableColumn
vrBrSrbNumLanIdtEntriesDenied = _VrBrSrbNumLanIdtEntriesDenied_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 5, 11, 1, 3),
    _VrBrSrbNumLanIdtEntriesDenied_Type()
)
vrBrSrbNumLanIdtEntriesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSrbNumLanIdtEntriesDenied.setStatus("mandatory")
_VrBrAdminControlTable_Object = MibTable
vrBrAdminControlTable = _VrBrAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 10)
)
if mibBuilder.loadTexts:
    vrBrAdminControlTable.setStatus("mandatory")
_VrBrAdminControlEntry_Object = MibTableRow
vrBrAdminControlEntry = _VrBrAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 10, 1)
)
vrBrAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
)
if mibBuilder.loadTexts:
    vrBrAdminControlEntry.setStatus("mandatory")


class _VrBrAdminStatus_Type(Integer32):
    """Custom type vrBrAdminStatus based on Integer32"""
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


_VrBrAdminStatus_Type.__name__ = "Integer32"
_VrBrAdminStatus_Object = MibTableColumn
vrBrAdminStatus = _VrBrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 10, 1, 1),
    _VrBrAdminStatus_Type()
)
vrBrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBrAdminStatus.setStatus("mandatory")
_VrBrStateTable_Object = MibTable
vrBrStateTable = _VrBrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 12)
)
if mibBuilder.loadTexts:
    vrBrStateTable.setStatus("mandatory")
_VrBrStateEntry_Object = MibTableRow
vrBrStateEntry = _VrBrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 12, 1)
)
vrBrStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
)
if mibBuilder.loadTexts:
    vrBrStateEntry.setStatus("mandatory")


class _VrBrAdminState_Type(Integer32):
    """Custom type vrBrAdminState based on Integer32"""
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


_VrBrAdminState_Type.__name__ = "Integer32"
_VrBrAdminState_Object = MibTableColumn
vrBrAdminState = _VrBrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 12, 1, 1),
    _VrBrAdminState_Type()
)
vrBrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrAdminState.setStatus("mandatory")


class _VrBrOperationalState_Type(Integer32):
    """Custom type vrBrOperationalState based on Integer32"""
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


_VrBrOperationalState_Type.__name__ = "Integer32"
_VrBrOperationalState_Object = MibTableColumn
vrBrOperationalState = _VrBrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 12, 1, 2),
    _VrBrOperationalState_Type()
)
vrBrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrOperationalState.setStatus("mandatory")


class _VrBrUsageState_Type(Integer32):
    """Custom type vrBrUsageState based on Integer32"""
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


_VrBrUsageState_Type.__name__ = "Integer32"
_VrBrUsageState_Object = MibTableColumn
vrBrUsageState = _VrBrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 12, 1, 3),
    _VrBrUsageState_Type()
)
vrBrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrUsageState.setStatus("mandatory")
_VrBrOperStatusTable_Object = MibTable
vrBrOperStatusTable = _VrBrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 13)
)
if mibBuilder.loadTexts:
    vrBrOperStatusTable.setStatus("mandatory")
_VrBrOperStatusEntry_Object = MibTableRow
vrBrOperStatusEntry = _VrBrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 13, 1)
)
vrBrOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
)
if mibBuilder.loadTexts:
    vrBrOperStatusEntry.setStatus("mandatory")


class _VrBrSnmpOperStatus_Type(Integer32):
    """Custom type vrBrSnmpOperStatus based on Integer32"""
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


_VrBrSnmpOperStatus_Type.__name__ = "Integer32"
_VrBrSnmpOperStatus_Object = MibTableColumn
vrBrSnmpOperStatus = _VrBrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 13, 1, 1),
    _VrBrSnmpOperStatus_Type()
)
vrBrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrSnmpOperStatus.setStatus("mandatory")
_VrBrOperTable_Object = MibTable
vrBrOperTable = _VrBrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 14)
)
if mibBuilder.loadTexts:
    vrBrOperTable.setStatus("mandatory")
_VrBrOperEntry_Object = MibTableRow
vrBrOperEntry = _VrBrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 14, 1)
)
vrBrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BridgeMIB", "vrBrIndex"),
)
if mibBuilder.loadTexts:
    vrBrOperEntry.setStatus("mandatory")


class _VrBrBridgeAddress_Type(MacAddress):
    """Custom type vrBrBridgeAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrBrBridgeAddress_Type.__name__ = "MacAddress"
_VrBrBridgeAddress_Object = MibTableColumn
vrBrBridgeAddress = _VrBrBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 14, 1, 1),
    _VrBrBridgeAddress_Type()
)
vrBrBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrBridgeAddress.setStatus("mandatory")


class _VrBrNumPorts_Type(Gauge32):
    """Custom type vrBrNumPorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrBrNumPorts_Type.__name__ = "Gauge32"
_VrBrNumPorts_Object = MibTableColumn
vrBrNumPorts = _VrBrNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 14, 1, 2),
    _VrBrNumPorts_Type()
)
vrBrNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrNumPorts.setStatus("mandatory")


class _VrBrType_Type(Integer32):
    """Custom type vrBrType based on Integer32"""
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


_VrBrType_Type.__name__ = "Integer32"
_VrBrType_Object = MibTableColumn
vrBrType = _VrBrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 5, 14, 1, 3),
    _VrBrType_Type()
)
vrBrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBrType.setStatus("mandatory")
_CB_ObjectIdentity = ObjectIdentity
cB = _CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103)
)
_CBRowStatusTable_Object = MibTable
cBRowStatusTable = _CBRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 1)
)
if mibBuilder.loadTexts:
    cBRowStatusTable.setStatus("mandatory")
_CBRowStatusEntry_Object = MibTableRow
cBRowStatusEntry = _CBRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 1, 1)
)
cBRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBRowStatusEntry.setStatus("mandatory")
_CBRowStatus_Type = RowStatus
_CBRowStatus_Object = MibTableColumn
cBRowStatus = _CBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 1, 1, 1),
    _CBRowStatus_Type()
)
cBRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBRowStatus.setStatus("mandatory")
_CBComponentName_Type = DisplayString
_CBComponentName_Object = MibTableColumn
cBComponentName = _CBComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 1, 1, 2),
    _CBComponentName_Type()
)
cBComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBComponentName.setStatus("mandatory")
_CBStorageType_Type = StorageType
_CBStorageType_Object = MibTableColumn
cBStorageType = _CBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 1, 1, 4),
    _CBStorageType_Type()
)
cBStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBStorageType.setStatus("mandatory")
_CBIndex_Type = NonReplicated
_CBIndex_Object = MibTableColumn
cBIndex = _CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 1, 1, 10),
    _CBIndex_Type()
)
cBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cBIndex.setStatus("mandatory")
_CBAdminControlTable_Object = MibTable
cBAdminControlTable = _CBAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 10)
)
if mibBuilder.loadTexts:
    cBAdminControlTable.setStatus("mandatory")
_CBAdminControlEntry_Object = MibTableRow
cBAdminControlEntry = _CBAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 10, 1)
)
cBAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBAdminControlEntry.setStatus("mandatory")


class _CBSnmpAdminStatus_Type(Integer32):
    """Custom type cBSnmpAdminStatus based on Integer32"""
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


_CBSnmpAdminStatus_Type.__name__ = "Integer32"
_CBSnmpAdminStatus_Object = MibTableColumn
cBSnmpAdminStatus = _CBSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 10, 1, 1),
    _CBSnmpAdminStatus_Type()
)
cBSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBSnmpAdminStatus.setStatus("obsolete")
_CBIfEntryTable_Object = MibTable
cBIfEntryTable = _CBIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 11)
)
if mibBuilder.loadTexts:
    cBIfEntryTable.setStatus("mandatory")
_CBIfEntryEntry_Object = MibTableRow
cBIfEntryEntry = _CBIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 11, 1)
)
cBIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBIfEntryEntry.setStatus("mandatory")


class _CBIfAdminStatus_Type(Integer32):
    """Custom type cBIfAdminStatus based on Integer32"""
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


_CBIfAdminStatus_Type.__name__ = "Integer32"
_CBIfAdminStatus_Object = MibTableColumn
cBIfAdminStatus = _CBIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 11, 1, 1),
    _CBIfAdminStatus_Type()
)
cBIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBIfAdminStatus.setStatus("mandatory")


class _CBIfIndex_Type(InterfaceIndex):
    """Custom type cBIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CBIfIndex_Type.__name__ = "InterfaceIndex"
_CBIfIndex_Object = MibTableColumn
cBIfIndex = _CBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 11, 1, 2),
    _CBIfIndex_Type()
)
cBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBIfIndex.setStatus("mandatory")
_CBMpTable_Object = MibTable
cBMpTable = _CBMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 12)
)
if mibBuilder.loadTexts:
    cBMpTable.setStatus("mandatory")
_CBMpEntry_Object = MibTableRow
cBMpEntry = _CBMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 12, 1)
)
cBMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBMpEntry.setStatus("mandatory")
_CBLinkToProtocolPort_Type = Link
_CBLinkToProtocolPort_Object = MibTableColumn
cBLinkToProtocolPort = _CBLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 12, 1, 1),
    _CBLinkToProtocolPort_Type()
)
cBLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBLinkToProtocolPort.setStatus("mandatory")
_CBOperTable_Object = MibTable
cBOperTable = _CBOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 13)
)
if mibBuilder.loadTexts:
    cBOperTable.setStatus("mandatory")
_CBOperEntry_Object = MibTableRow
cBOperEntry = _CBOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 13, 1)
)
cBOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBOperEntry.setStatus("mandatory")


class _CBMacAddress_Type(MacAddress):
    """Custom type cBMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CBMacAddress_Type.__name__ = "MacAddress"
_CBMacAddress_Object = MibTableColumn
cBMacAddress = _CBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 13, 1, 1),
    _CBMacAddress_Type()
)
cBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBMacAddress.setStatus("mandatory")
_CBStateTable_Object = MibTable
cBStateTable = _CBStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 14)
)
if mibBuilder.loadTexts:
    cBStateTable.setStatus("mandatory")
_CBStateEntry_Object = MibTableRow
cBStateEntry = _CBStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 14, 1)
)
cBStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBStateEntry.setStatus("mandatory")


class _CBAdminState_Type(Integer32):
    """Custom type cBAdminState based on Integer32"""
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


_CBAdminState_Type.__name__ = "Integer32"
_CBAdminState_Object = MibTableColumn
cBAdminState = _CBAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 14, 1, 1),
    _CBAdminState_Type()
)
cBAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBAdminState.setStatus("mandatory")


class _CBOperationalState_Type(Integer32):
    """Custom type cBOperationalState based on Integer32"""
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


_CBOperationalState_Type.__name__ = "Integer32"
_CBOperationalState_Object = MibTableColumn
cBOperationalState = _CBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 14, 1, 2),
    _CBOperationalState_Type()
)
cBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBOperationalState.setStatus("mandatory")


class _CBUsageState_Type(Integer32):
    """Custom type cBUsageState based on Integer32"""
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


_CBUsageState_Type.__name__ = "Integer32"
_CBUsageState_Object = MibTableColumn
cBUsageState = _CBUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 14, 1, 3),
    _CBUsageState_Type()
)
cBUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBUsageState.setStatus("mandatory")
_CBOperStatusTable_Object = MibTable
cBOperStatusTable = _CBOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 15)
)
if mibBuilder.loadTexts:
    cBOperStatusTable.setStatus("mandatory")
_CBOperStatusEntry_Object = MibTableRow
cBOperStatusEntry = _CBOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 15, 1)
)
cBOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "cBIndex"),
)
if mibBuilder.loadTexts:
    cBOperStatusEntry.setStatus("mandatory")


class _CBSnmpOperStatus_Type(Integer32):
    """Custom type cBSnmpOperStatus based on Integer32"""
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


_CBSnmpOperStatus_Type.__name__ = "Integer32"
_CBSnmpOperStatus_Object = MibTableColumn
cBSnmpOperStatus = _CBSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 103, 15, 1, 1),
    _CBSnmpOperStatus_Type()
)
cBSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBSnmpOperStatus.setStatus("mandatory")
_PB_ObjectIdentity = ObjectIdentity
pB = _PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104)
)
_PBRowStatusTable_Object = MibTable
pBRowStatusTable = _PBRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 1)
)
if mibBuilder.loadTexts:
    pBRowStatusTable.setStatus("mandatory")
_PBRowStatusEntry_Object = MibTableRow
pBRowStatusEntry = _PBRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 1, 1)
)
pBRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBRowStatusEntry.setStatus("mandatory")
_PBRowStatus_Type = RowStatus
_PBRowStatus_Object = MibTableColumn
pBRowStatus = _PBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 1, 1, 1),
    _PBRowStatus_Type()
)
pBRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBRowStatus.setStatus("mandatory")
_PBComponentName_Type = DisplayString
_PBComponentName_Object = MibTableColumn
pBComponentName = _PBComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 1, 1, 2),
    _PBComponentName_Type()
)
pBComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBComponentName.setStatus("mandatory")
_PBStorageType_Type = StorageType
_PBStorageType_Object = MibTableColumn
pBStorageType = _PBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 1, 1, 4),
    _PBStorageType_Type()
)
pBStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBStorageType.setStatus("mandatory")
_PBIndex_Type = NonReplicated
_PBIndex_Object = MibTableColumn
pBIndex = _PBIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 1, 1, 10),
    _PBIndex_Type()
)
pBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pBIndex.setStatus("mandatory")
_PBAdminControlTable_Object = MibTable
pBAdminControlTable = _PBAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 10)
)
if mibBuilder.loadTexts:
    pBAdminControlTable.setStatus("mandatory")
_PBAdminControlEntry_Object = MibTableRow
pBAdminControlEntry = _PBAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 10, 1)
)
pBAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBAdminControlEntry.setStatus("mandatory")


class _PBSnmpAdminStatus_Type(Integer32):
    """Custom type pBSnmpAdminStatus based on Integer32"""
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


_PBSnmpAdminStatus_Type.__name__ = "Integer32"
_PBSnmpAdminStatus_Object = MibTableColumn
pBSnmpAdminStatus = _PBSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 10, 1, 1),
    _PBSnmpAdminStatus_Type()
)
pBSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBSnmpAdminStatus.setStatus("obsolete")
_PBIfEntryTable_Object = MibTable
pBIfEntryTable = _PBIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 11)
)
if mibBuilder.loadTexts:
    pBIfEntryTable.setStatus("mandatory")
_PBIfEntryEntry_Object = MibTableRow
pBIfEntryEntry = _PBIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 11, 1)
)
pBIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBIfEntryEntry.setStatus("mandatory")


class _PBIfAdminStatus_Type(Integer32):
    """Custom type pBIfAdminStatus based on Integer32"""
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


_PBIfAdminStatus_Type.__name__ = "Integer32"
_PBIfAdminStatus_Object = MibTableColumn
pBIfAdminStatus = _PBIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 11, 1, 1),
    _PBIfAdminStatus_Type()
)
pBIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBIfAdminStatus.setStatus("mandatory")


class _PBIfIndex_Type(InterfaceIndex):
    """Custom type pBIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PBIfIndex_Type.__name__ = "InterfaceIndex"
_PBIfIndex_Object = MibTableColumn
pBIfIndex = _PBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 11, 1, 2),
    _PBIfIndex_Type()
)
pBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBIfIndex.setStatus("mandatory")
_PBMpTable_Object = MibTable
pBMpTable = _PBMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 12)
)
if mibBuilder.loadTexts:
    pBMpTable.setStatus("mandatory")
_PBMpEntry_Object = MibTableRow
pBMpEntry = _PBMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 12, 1)
)
pBMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBMpEntry.setStatus("mandatory")
_PBLinkToProtocolPort_Type = Link
_PBLinkToProtocolPort_Object = MibTableColumn
pBLinkToProtocolPort = _PBLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 12, 1, 1),
    _PBLinkToProtocolPort_Type()
)
pBLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBLinkToProtocolPort.setStatus("mandatory")
_PBOperTable_Object = MibTable
pBOperTable = _PBOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 13)
)
if mibBuilder.loadTexts:
    pBOperTable.setStatus("mandatory")
_PBOperEntry_Object = MibTableRow
pBOperEntry = _PBOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 13, 1)
)
pBOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBOperEntry.setStatus("mandatory")


class _PBMacAddress_Type(HexString):
    """Custom type pBMacAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PBMacAddress_Type.__name__ = "HexString"
_PBMacAddress_Object = MibTableColumn
pBMacAddress = _PBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 13, 1, 1),
    _PBMacAddress_Type()
)
pBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBMacAddress.setStatus("mandatory")
_PBStateTable_Object = MibTable
pBStateTable = _PBStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 14)
)
if mibBuilder.loadTexts:
    pBStateTable.setStatus("mandatory")
_PBStateEntry_Object = MibTableRow
pBStateEntry = _PBStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 14, 1)
)
pBStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBStateEntry.setStatus("mandatory")


class _PBAdminState_Type(Integer32):
    """Custom type pBAdminState based on Integer32"""
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


_PBAdminState_Type.__name__ = "Integer32"
_PBAdminState_Object = MibTableColumn
pBAdminState = _PBAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 14, 1, 1),
    _PBAdminState_Type()
)
pBAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBAdminState.setStatus("mandatory")


class _PBOperationalState_Type(Integer32):
    """Custom type pBOperationalState based on Integer32"""
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


_PBOperationalState_Type.__name__ = "Integer32"
_PBOperationalState_Object = MibTableColumn
pBOperationalState = _PBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 14, 1, 2),
    _PBOperationalState_Type()
)
pBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBOperationalState.setStatus("mandatory")


class _PBUsageState_Type(Integer32):
    """Custom type pBUsageState based on Integer32"""
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


_PBUsageState_Type.__name__ = "Integer32"
_PBUsageState_Object = MibTableColumn
pBUsageState = _PBUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 14, 1, 3),
    _PBUsageState_Type()
)
pBUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBUsageState.setStatus("mandatory")
_PBOperStatusTable_Object = MibTable
pBOperStatusTable = _PBOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 15)
)
if mibBuilder.loadTexts:
    pBOperStatusTable.setStatus("mandatory")
_PBOperStatusEntry_Object = MibTableRow
pBOperStatusEntry = _PBOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 15, 1)
)
pBOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BridgeMIB", "pBIndex"),
)
if mibBuilder.loadTexts:
    pBOperStatusEntry.setStatus("mandatory")


class _PBSnmpOperStatus_Type(Integer32):
    """Custom type pBSnmpOperStatus based on Integer32"""
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


_PBSnmpOperStatus_Type.__name__ = "Integer32"
_PBSnmpOperStatus_Object = MibTableColumn
pBSnmpOperStatus = _PBSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 104, 15, 1, 1),
    _PBSnmpOperStatus_Type()
)
pBSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBSnmpOperStatus.setStatus("mandatory")
_BridgeMIB_ObjectIdentity = ObjectIdentity
bridgeMIB = _BridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25)
)
_BridgeGroup_ObjectIdentity = ObjectIdentity
bridgeGroup = _BridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 1)
)
_BridgeGroupBE_ObjectIdentity = ObjectIdentity
bridgeGroupBE = _BridgeGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 1, 5)
)
_BridgeGroupBE01_ObjectIdentity = ObjectIdentity
bridgeGroupBE01 = _BridgeGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 1, 5, 2)
)
_BridgeGroupBE01A_ObjectIdentity = ObjectIdentity
bridgeGroupBE01A = _BridgeGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 1, 5, 2, 2)
)
_BridgeCapabilities_ObjectIdentity = ObjectIdentity
bridgeCapabilities = _BridgeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 3)
)
_BridgeCapabilitiesBE_ObjectIdentity = ObjectIdentity
bridgeCapabilitiesBE = _BridgeCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 3, 5)
)
_BridgeCapabilitiesBE01_ObjectIdentity = ObjectIdentity
bridgeCapabilitiesBE01 = _BridgeCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 3, 5, 2)
)
_BridgeCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
bridgeCapabilitiesBE01A = _BridgeCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 25, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-BridgeMIB",
    **{"vrPpTbcl": vrPpTbcl,
       "vrPpTbclRowStatusTable": vrPpTbclRowStatusTable,
       "vrPpTbclRowStatusEntry": vrPpTbclRowStatusEntry,
       "vrPpTbclRowStatus": vrPpTbclRowStatus,
       "vrPpTbclComponentName": vrPpTbclComponentName,
       "vrPpTbclStorageType": vrPpTbclStorageType,
       "vrPpTbclIndex": vrPpTbclIndex,
       "vrPpTbclNs": vrPpTbclNs,
       "vrPpTbclNsRowStatusTable": vrPpTbclNsRowStatusTable,
       "vrPpTbclNsRowStatusEntry": vrPpTbclNsRowStatusEntry,
       "vrPpTbclNsRowStatus": vrPpTbclNsRowStatus,
       "vrPpTbclNsComponentName": vrPpTbclNsComponentName,
       "vrPpTbclNsStorageType": vrPpTbclNsStorageType,
       "vrPpTbclNsIndex": vrPpTbclNsIndex,
       "vrPpTbclNsProvTable": vrPpTbclNsProvTable,
       "vrPpTbclNsProvEntry": vrPpTbclNsProvEntry,
       "vrPpTbclNsIncomingFilter": vrPpTbclNsIncomingFilter,
       "vrPpTbclNsOutgoingFilter": vrPpTbclNsOutgoingFilter,
       "vrPpTbclProvTable": vrPpTbclProvTable,
       "vrPpTbclProvEntry": vrPpTbclProvEntry,
       "vrPpTbclTranslateIpx": vrPpTbclTranslateIpx,
       "vrPpTbclFragmentIp": vrPpTbclFragmentIp,
       "vrPpTbclServiceClass": vrPpTbclServiceClass,
       "vrPpTbclConvertArpMacAddress": vrPpTbclConvertArpMacAddress,
       "vrPpTbclPortNum": vrPpTbclPortNum,
       "vrPpTbclOutboundFrameMediaType": vrPpTbclOutboundFrameMediaType,
       "vrPpTbclTbProvTable": vrPpTbclTbProvTable,
       "vrPpTbclTbProvEntry": vrPpTbclTbProvEntry,
       "vrPpTbclSecureOption": vrPpTbclSecureOption,
       "vrPpTbclStpProvTable": vrPpTbclStpProvTable,
       "vrPpTbclStpProvEntry": vrPpTbclStpProvEntry,
       "vrPpTbclAdminStatus": vrPpTbclAdminStatus,
       "vrPpTbclPortStateStpControl": vrPpTbclPortStateStpControl,
       "vrPpTbclStpTypeProv": vrPpTbclStpTypeProv,
       "vrPpTbclPortPriority": vrPpTbclPortPriority,
       "vrPpTbclPathCost": vrPpTbclPathCost,
       "vrPpTbclPathCostMethod": vrPpTbclPathCostMethod,
       "vrPpTbclDIProvTable": vrPpTbclDIProvTable,
       "vrPpTbclDIProvEntry": vrPpTbclDIProvEntry,
       "vrPpTbclDomainNum": vrPpTbclDomainNum,
       "vrPpTbclPreserveDomain": vrPpTbclPreserveDomain,
       "vrPpTbclStateTable": vrPpTbclStateTable,
       "vrPpTbclStateEntry": vrPpTbclStateEntry,
       "vrPpTbclAdminState": vrPpTbclAdminState,
       "vrPpTbclOperationalState": vrPpTbclOperationalState,
       "vrPpTbclUsageState": vrPpTbclUsageState,
       "vrPpTbclOperStatusTable": vrPpTbclOperStatusTable,
       "vrPpTbclOperStatusEntry": vrPpTbclOperStatusEntry,
       "vrPpTbclSnmpOperStatus": vrPpTbclSnmpOperStatus,
       "vrPpTbclOperTable": vrPpTbclOperTable,
       "vrPpTbclOperEntry": vrPpTbclOperEntry,
       "vrPpTbclPortName": vrPpTbclPortName,
       "vrPpTbclUpTime": vrPpTbclUpTime,
       "vrPpTbclDownTime": vrPpTbclDownTime,
       "vrPpTbclBridgingMode": vrPpTbclBridgingMode,
       "vrPpTbclBridgePortConfig": vrPpTbclBridgePortConfig,
       "vrPpTbclBridgePortType": vrPpTbclBridgePortType,
       "vrPpTbclIfIndex": vrPpTbclIfIndex,
       "vrPpTbclDelayExceededDiscards": vrPpTbclDelayExceededDiscards,
       "vrPpTbclMtuExceededDiscards": vrPpTbclMtuExceededDiscards,
       "vrPpTbclTbOperTable": vrPpTbclTbOperTable,
       "vrPpTbclTbOperEntry": vrPpTbclTbOperEntry,
       "vrPpTbclMaxInfo": vrPpTbclMaxInfo,
       "vrPpTbclBadVerifyDiscards": vrPpTbclBadVerifyDiscards,
       "vrPpTbclUnicastNoMatches": vrPpTbclUnicastNoMatches,
       "vrPpTbclStaticEntryDiscards": vrPpTbclStaticEntryDiscards,
       "vrPpTbclDynamicEntryDiscards": vrPpTbclDynamicEntryDiscards,
       "vrPpTbclLearningDiscards": vrPpTbclLearningDiscards,
       "vrPpTbclInDiscards": vrPpTbclInDiscards,
       "vrPpTbclInFrames": vrPpTbclInFrames,
       "vrPpTbclOutFrames": vrPpTbclOutFrames,
       "vrPpTbclStpOperTable": vrPpTbclStpOperTable,
       "vrPpTbclStpOperEntry": vrPpTbclStpOperEntry,
       "vrPpTbclStpPortState": vrPpTbclStpPortState,
       "vrPpTbclStpTypeOper": vrPpTbclStpTypeOper,
       "vrPpTbclDesignatedCost": vrPpTbclDesignatedCost,
       "vrPpTbclPathCostOper": vrPpTbclPathCostOper,
       "vrPpTbclDesignatedBridge": vrPpTbclDesignatedBridge,
       "vrPpTbclDesignatedPort": vrPpTbclDesignatedPort,
       "vrPpTbclForwardTransitions": vrPpTbclForwardTransitions,
       "vrPpTbclBlockingDiscards": vrPpTbclBlockingDiscards,
       "vrPpTbclDesignatedRoot": vrPpTbclDesignatedRoot,
       "vrPpTbclStatsTable": vrPpTbclStatsTable,
       "vrPpTbclStatsEntry": vrPpTbclStatsEntry,
       "vrPpTbclBadAbstractDiscards": vrPpTbclBadAbstractDiscards,
       "vrPpTbclTinygramFramesIn": vrPpTbclTinygramFramesIn,
       "vrPpTbclTinygramFramesOut": vrPpTbclTinygramFramesOut,
       "vrPpTbclInFilterDiscards": vrPpTbclInFilterDiscards,
       "vrPpTbclOutFilterDiscards": vrPpTbclOutFilterDiscards,
       "vrPpFddiETB": vrPpFddiETB,
       "vrPpFddiETBRowStatusTable": vrPpFddiETBRowStatusTable,
       "vrPpFddiETBRowStatusEntry": vrPpFddiETBRowStatusEntry,
       "vrPpFddiETBRowStatus": vrPpFddiETBRowStatus,
       "vrPpFddiETBComponentName": vrPpFddiETBComponentName,
       "vrPpFddiETBStorageType": vrPpFddiETBStorageType,
       "vrPpFddiETBIndex": vrPpFddiETBIndex,
       "vrPpFddiETBNs": vrPpFddiETBNs,
       "vrPpFddiETBNsRowStatusTable": vrPpFddiETBNsRowStatusTable,
       "vrPpFddiETBNsRowStatusEntry": vrPpFddiETBNsRowStatusEntry,
       "vrPpFddiETBNsRowStatus": vrPpFddiETBNsRowStatus,
       "vrPpFddiETBNsComponentName": vrPpFddiETBNsComponentName,
       "vrPpFddiETBNsStorageType": vrPpFddiETBNsStorageType,
       "vrPpFddiETBNsIndex": vrPpFddiETBNsIndex,
       "vrPpFddiETBNsProvTable": vrPpFddiETBNsProvTable,
       "vrPpFddiETBNsProvEntry": vrPpFddiETBNsProvEntry,
       "vrPpFddiETBNsIncomingFilter": vrPpFddiETBNsIncomingFilter,
       "vrPpFddiETBNsOutgoingFilter": vrPpFddiETBNsOutgoingFilter,
       "vrPpFddiETBProvTable": vrPpFddiETBProvTable,
       "vrPpFddiETBProvEntry": vrPpFddiETBProvEntry,
       "vrPpFddiETBTranslateIpx": vrPpFddiETBTranslateIpx,
       "vrPpFddiETBFragmentIp": vrPpFddiETBFragmentIp,
       "vrPpFddiETBServiceClass": vrPpFddiETBServiceClass,
       "vrPpFddiETBConvertArpMacAddress": vrPpFddiETBConvertArpMacAddress,
       "vrPpFddiETBPortNum": vrPpFddiETBPortNum,
       "vrPpFddiETBOutboundFrameMediaType": vrPpFddiETBOutboundFrameMediaType,
       "vrPpFddiETBTbProvTable": vrPpFddiETBTbProvTable,
       "vrPpFddiETBTbProvEntry": vrPpFddiETBTbProvEntry,
       "vrPpFddiETBSecureOption": vrPpFddiETBSecureOption,
       "vrPpFddiETBStpProvTable": vrPpFddiETBStpProvTable,
       "vrPpFddiETBStpProvEntry": vrPpFddiETBStpProvEntry,
       "vrPpFddiETBAdminStatus": vrPpFddiETBAdminStatus,
       "vrPpFddiETBPortStateStpControl": vrPpFddiETBPortStateStpControl,
       "vrPpFddiETBStpTypeProv": vrPpFddiETBStpTypeProv,
       "vrPpFddiETBPortPriority": vrPpFddiETBPortPriority,
       "vrPpFddiETBPathCost": vrPpFddiETBPathCost,
       "vrPpFddiETBPathCostMethod": vrPpFddiETBPathCostMethod,
       "vrPpFddiETBDIProvTable": vrPpFddiETBDIProvTable,
       "vrPpFddiETBDIProvEntry": vrPpFddiETBDIProvEntry,
       "vrPpFddiETBDomainNum": vrPpFddiETBDomainNum,
       "vrPpFddiETBPreserveDomain": vrPpFddiETBPreserveDomain,
       "vrPpFddiETBStateTable": vrPpFddiETBStateTable,
       "vrPpFddiETBStateEntry": vrPpFddiETBStateEntry,
       "vrPpFddiETBAdminState": vrPpFddiETBAdminState,
       "vrPpFddiETBOperationalState": vrPpFddiETBOperationalState,
       "vrPpFddiETBUsageState": vrPpFddiETBUsageState,
       "vrPpFddiETBOperStatusTable": vrPpFddiETBOperStatusTable,
       "vrPpFddiETBOperStatusEntry": vrPpFddiETBOperStatusEntry,
       "vrPpFddiETBSnmpOperStatus": vrPpFddiETBSnmpOperStatus,
       "vrPpFddiETBOperTable": vrPpFddiETBOperTable,
       "vrPpFddiETBOperEntry": vrPpFddiETBOperEntry,
       "vrPpFddiETBPortName": vrPpFddiETBPortName,
       "vrPpFddiETBUpTime": vrPpFddiETBUpTime,
       "vrPpFddiETBDownTime": vrPpFddiETBDownTime,
       "vrPpFddiETBBridgingMode": vrPpFddiETBBridgingMode,
       "vrPpFddiETBBridgePortConfig": vrPpFddiETBBridgePortConfig,
       "vrPpFddiETBBridgePortType": vrPpFddiETBBridgePortType,
       "vrPpFddiETBIfIndex": vrPpFddiETBIfIndex,
       "vrPpFddiETBDelayExceededDiscards": vrPpFddiETBDelayExceededDiscards,
       "vrPpFddiETBMtuExceededDiscards": vrPpFddiETBMtuExceededDiscards,
       "vrPpFddiETBTbOperTable": vrPpFddiETBTbOperTable,
       "vrPpFddiETBTbOperEntry": vrPpFddiETBTbOperEntry,
       "vrPpFddiETBMaxInfo": vrPpFddiETBMaxInfo,
       "vrPpFddiETBBadVerifyDiscards": vrPpFddiETBBadVerifyDiscards,
       "vrPpFddiETBUnicastNoMatches": vrPpFddiETBUnicastNoMatches,
       "vrPpFddiETBStaticEntryDiscards": vrPpFddiETBStaticEntryDiscards,
       "vrPpFddiETBDynamicEntryDiscards": vrPpFddiETBDynamicEntryDiscards,
       "vrPpFddiETBLearningDiscards": vrPpFddiETBLearningDiscards,
       "vrPpFddiETBInDiscards": vrPpFddiETBInDiscards,
       "vrPpFddiETBInFrames": vrPpFddiETBInFrames,
       "vrPpFddiETBOutFrames": vrPpFddiETBOutFrames,
       "vrPpFddiETBStpOperTable": vrPpFddiETBStpOperTable,
       "vrPpFddiETBStpOperEntry": vrPpFddiETBStpOperEntry,
       "vrPpFddiETBStpPortState": vrPpFddiETBStpPortState,
       "vrPpFddiETBStpTypeOper": vrPpFddiETBStpTypeOper,
       "vrPpFddiETBDesignatedCost": vrPpFddiETBDesignatedCost,
       "vrPpFddiETBPathCostOper": vrPpFddiETBPathCostOper,
       "vrPpFddiETBDesignatedBridge": vrPpFddiETBDesignatedBridge,
       "vrPpFddiETBDesignatedPort": vrPpFddiETBDesignatedPort,
       "vrPpFddiETBForwardTransitions": vrPpFddiETBForwardTransitions,
       "vrPpFddiETBBlockingDiscards": vrPpFddiETBBlockingDiscards,
       "vrPpFddiETBDesignatedRoot": vrPpFddiETBDesignatedRoot,
       "vrPpFddiETBStatsTable": vrPpFddiETBStatsTable,
       "vrPpFddiETBStatsEntry": vrPpFddiETBStatsEntry,
       "vrPpFddiETBBadAbstractDiscards": vrPpFddiETBBadAbstractDiscards,
       "vrPpFddiETBTinygramFramesIn": vrPpFddiETBTinygramFramesIn,
       "vrPpFddiETBTinygramFramesOut": vrPpFddiETBTinygramFramesOut,
       "vrPpFddiETBInFilterDiscards": vrPpFddiETBInFilterDiscards,
       "vrPpFddiETBOutFilterDiscards": vrPpFddiETBOutFilterDiscards,
       "vrPpTbp": vrPpTbp,
       "vrPpTbpRowStatusTable": vrPpTbpRowStatusTable,
       "vrPpTbpRowStatusEntry": vrPpTbpRowStatusEntry,
       "vrPpTbpRowStatus": vrPpTbpRowStatus,
       "vrPpTbpComponentName": vrPpTbpComponentName,
       "vrPpTbpStorageType": vrPpTbpStorageType,
       "vrPpTbpIndex": vrPpTbpIndex,
       "vrPpTbpNs": vrPpTbpNs,
       "vrPpTbpNsRowStatusTable": vrPpTbpNsRowStatusTable,
       "vrPpTbpNsRowStatusEntry": vrPpTbpNsRowStatusEntry,
       "vrPpTbpNsRowStatus": vrPpTbpNsRowStatus,
       "vrPpTbpNsComponentName": vrPpTbpNsComponentName,
       "vrPpTbpNsStorageType": vrPpTbpNsStorageType,
       "vrPpTbpNsIndex": vrPpTbpNsIndex,
       "vrPpTbpNsProvTable": vrPpTbpNsProvTable,
       "vrPpTbpNsProvEntry": vrPpTbpNsProvEntry,
       "vrPpTbpNsIncomingFilter": vrPpTbpNsIncomingFilter,
       "vrPpTbpNsOutgoingFilter": vrPpTbpNsOutgoingFilter,
       "vrPpTbpProvTable": vrPpTbpProvTable,
       "vrPpTbpProvEntry": vrPpTbpProvEntry,
       "vrPpTbpTranslateIpx": vrPpTbpTranslateIpx,
       "vrPpTbpFragmentIp": vrPpTbpFragmentIp,
       "vrPpTbpServiceClass": vrPpTbpServiceClass,
       "vrPpTbpConvertArpMacAddress": vrPpTbpConvertArpMacAddress,
       "vrPpTbpPortNum": vrPpTbpPortNum,
       "vrPpTbpOutboundFrameMediaType": vrPpTbpOutboundFrameMediaType,
       "vrPpTbpTbProvTable": vrPpTbpTbProvTable,
       "vrPpTbpTbProvEntry": vrPpTbpTbProvEntry,
       "vrPpTbpSecureOption": vrPpTbpSecureOption,
       "vrPpTbpStpProvTable": vrPpTbpStpProvTable,
       "vrPpTbpStpProvEntry": vrPpTbpStpProvEntry,
       "vrPpTbpAdminStatus": vrPpTbpAdminStatus,
       "vrPpTbpPortStateStpControl": vrPpTbpPortStateStpControl,
       "vrPpTbpStpTypeProv": vrPpTbpStpTypeProv,
       "vrPpTbpPortPriority": vrPpTbpPortPriority,
       "vrPpTbpPathCost": vrPpTbpPathCost,
       "vrPpTbpPathCostMethod": vrPpTbpPathCostMethod,
       "vrPpTbpDIProvTable": vrPpTbpDIProvTable,
       "vrPpTbpDIProvEntry": vrPpTbpDIProvEntry,
       "vrPpTbpDomainNum": vrPpTbpDomainNum,
       "vrPpTbpPreserveDomain": vrPpTbpPreserveDomain,
       "vrPpTbpStateTable": vrPpTbpStateTable,
       "vrPpTbpStateEntry": vrPpTbpStateEntry,
       "vrPpTbpAdminState": vrPpTbpAdminState,
       "vrPpTbpOperationalState": vrPpTbpOperationalState,
       "vrPpTbpUsageState": vrPpTbpUsageState,
       "vrPpTbpOperStatusTable": vrPpTbpOperStatusTable,
       "vrPpTbpOperStatusEntry": vrPpTbpOperStatusEntry,
       "vrPpTbpSnmpOperStatus": vrPpTbpSnmpOperStatus,
       "vrPpTbpOperTable": vrPpTbpOperTable,
       "vrPpTbpOperEntry": vrPpTbpOperEntry,
       "vrPpTbpPortName": vrPpTbpPortName,
       "vrPpTbpUpTime": vrPpTbpUpTime,
       "vrPpTbpDownTime": vrPpTbpDownTime,
       "vrPpTbpBridgingMode": vrPpTbpBridgingMode,
       "vrPpTbpBridgePortConfig": vrPpTbpBridgePortConfig,
       "vrPpTbpBridgePortType": vrPpTbpBridgePortType,
       "vrPpTbpIfIndex": vrPpTbpIfIndex,
       "vrPpTbpDelayExceededDiscards": vrPpTbpDelayExceededDiscards,
       "vrPpTbpMtuExceededDiscards": vrPpTbpMtuExceededDiscards,
       "vrPpTbpTbOperTable": vrPpTbpTbOperTable,
       "vrPpTbpTbOperEntry": vrPpTbpTbOperEntry,
       "vrPpTbpMaxInfo": vrPpTbpMaxInfo,
       "vrPpTbpBadVerifyDiscards": vrPpTbpBadVerifyDiscards,
       "vrPpTbpUnicastNoMatches": vrPpTbpUnicastNoMatches,
       "vrPpTbpStaticEntryDiscards": vrPpTbpStaticEntryDiscards,
       "vrPpTbpDynamicEntryDiscards": vrPpTbpDynamicEntryDiscards,
       "vrPpTbpLearningDiscards": vrPpTbpLearningDiscards,
       "vrPpTbpInDiscards": vrPpTbpInDiscards,
       "vrPpTbpInFrames": vrPpTbpInFrames,
       "vrPpTbpOutFrames": vrPpTbpOutFrames,
       "vrPpTbpStpOperTable": vrPpTbpStpOperTable,
       "vrPpTbpStpOperEntry": vrPpTbpStpOperEntry,
       "vrPpTbpStpPortState": vrPpTbpStpPortState,
       "vrPpTbpStpTypeOper": vrPpTbpStpTypeOper,
       "vrPpTbpDesignatedCost": vrPpTbpDesignatedCost,
       "vrPpTbpPathCostOper": vrPpTbpPathCostOper,
       "vrPpTbpDesignatedBridge": vrPpTbpDesignatedBridge,
       "vrPpTbpDesignatedPort": vrPpTbpDesignatedPort,
       "vrPpTbpForwardTransitions": vrPpTbpForwardTransitions,
       "vrPpTbpBlockingDiscards": vrPpTbpBlockingDiscards,
       "vrPpTbpDesignatedRoot": vrPpTbpDesignatedRoot,
       "vrPpTbpStatsTable": vrPpTbpStatsTable,
       "vrPpTbpStatsEntry": vrPpTbpStatsEntry,
       "vrPpTbpBadAbstractDiscards": vrPpTbpBadAbstractDiscards,
       "vrPpTbpTinygramFramesIn": vrPpTbpTinygramFramesIn,
       "vrPpTbpTinygramFramesOut": vrPpTbpTinygramFramesOut,
       "vrPpTbpInFilterDiscards": vrPpTbpInFilterDiscards,
       "vrPpTbpOutFilterDiscards": vrPpTbpOutFilterDiscards,
       "vrPpSrBp": vrPpSrBp,
       "vrPpSrBpRowStatusTable": vrPpSrBpRowStatusTable,
       "vrPpSrBpRowStatusEntry": vrPpSrBpRowStatusEntry,
       "vrPpSrBpRowStatus": vrPpSrBpRowStatus,
       "vrPpSrBpComponentName": vrPpSrBpComponentName,
       "vrPpSrBpStorageType": vrPpSrBpStorageType,
       "vrPpSrBpIndex": vrPpSrBpIndex,
       "vrPpSrBpNs": vrPpSrBpNs,
       "vrPpSrBpNsRowStatusTable": vrPpSrBpNsRowStatusTable,
       "vrPpSrBpNsRowStatusEntry": vrPpSrBpNsRowStatusEntry,
       "vrPpSrBpNsRowStatus": vrPpSrBpNsRowStatus,
       "vrPpSrBpNsComponentName": vrPpSrBpNsComponentName,
       "vrPpSrBpNsStorageType": vrPpSrBpNsStorageType,
       "vrPpSrBpNsIndex": vrPpSrBpNsIndex,
       "vrPpSrBpNsProvTable": vrPpSrBpNsProvTable,
       "vrPpSrBpNsProvEntry": vrPpSrBpNsProvEntry,
       "vrPpSrBpNsIncomingFilter": vrPpSrBpNsIncomingFilter,
       "vrPpSrBpNsOutgoingFilter": vrPpSrBpNsOutgoingFilter,
       "vrPpSrBpProvTable": vrPpSrBpProvTable,
       "vrPpSrBpProvEntry": vrPpSrBpProvEntry,
       "vrPpSrBpTranslateIpx": vrPpSrBpTranslateIpx,
       "vrPpSrBpFragmentIp": vrPpSrBpFragmentIp,
       "vrPpSrBpServiceClass": vrPpSrBpServiceClass,
       "vrPpSrBpConvertArpMacAddress": vrPpSrBpConvertArpMacAddress,
       "vrPpSrBpPortNum": vrPpSrBpPortNum,
       "vrPpSrBpOutboundFrameMediaType": vrPpSrBpOutboundFrameMediaType,
       "vrPpSrBpStpProvTable": vrPpSrBpStpProvTable,
       "vrPpSrBpStpProvEntry": vrPpSrBpStpProvEntry,
       "vrPpSrBpAdminStatus": vrPpSrBpAdminStatus,
       "vrPpSrBpPortStateStpControl": vrPpSrBpPortStateStpControl,
       "vrPpSrBpStpTypeProv": vrPpSrBpStpTypeProv,
       "vrPpSrBpPortPriority": vrPpSrBpPortPriority,
       "vrPpSrBpPathCost": vrPpSrBpPathCost,
       "vrPpSrBpPathCostMethod": vrPpSrBpPathCostMethod,
       "vrPpSrBpDIProvTable": vrPpSrBpDIProvTable,
       "vrPpSrBpDIProvEntry": vrPpSrBpDIProvEntry,
       "vrPpSrBpDomainNum": vrPpSrBpDomainNum,
       "vrPpSrBpPreserveDomain": vrPpSrBpPreserveDomain,
       "vrPpSrBpStateTable": vrPpSrBpStateTable,
       "vrPpSrBpStateEntry": vrPpSrBpStateEntry,
       "vrPpSrBpAdminState": vrPpSrBpAdminState,
       "vrPpSrBpOperationalState": vrPpSrBpOperationalState,
       "vrPpSrBpUsageState": vrPpSrBpUsageState,
       "vrPpSrBpOperStatusTable": vrPpSrBpOperStatusTable,
       "vrPpSrBpOperStatusEntry": vrPpSrBpOperStatusEntry,
       "vrPpSrBpSnmpOperStatus": vrPpSrBpSnmpOperStatus,
       "vrPpSrBpOperTable": vrPpSrBpOperTable,
       "vrPpSrBpOperEntry": vrPpSrBpOperEntry,
       "vrPpSrBpPortName": vrPpSrBpPortName,
       "vrPpSrBpUpTime": vrPpSrBpUpTime,
       "vrPpSrBpDownTime": vrPpSrBpDownTime,
       "vrPpSrBpBridgingMode": vrPpSrBpBridgingMode,
       "vrPpSrBpBridgePortConfig": vrPpSrBpBridgePortConfig,
       "vrPpSrBpBridgePortType": vrPpSrBpBridgePortType,
       "vrPpSrBpIfIndex": vrPpSrBpIfIndex,
       "vrPpSrBpDelayExceededDiscards": vrPpSrBpDelayExceededDiscards,
       "vrPpSrBpMtuExceededDiscards": vrPpSrBpMtuExceededDiscards,
       "vrPpSrBpStpOperTable": vrPpSrBpStpOperTable,
       "vrPpSrBpStpOperEntry": vrPpSrBpStpOperEntry,
       "vrPpSrBpStpPortState": vrPpSrBpStpPortState,
       "vrPpSrBpStpTypeOper": vrPpSrBpStpTypeOper,
       "vrPpSrBpDesignatedCost": vrPpSrBpDesignatedCost,
       "vrPpSrBpPathCostOper": vrPpSrBpPathCostOper,
       "vrPpSrBpDesignatedBridge": vrPpSrBpDesignatedBridge,
       "vrPpSrBpDesignatedPort": vrPpSrBpDesignatedPort,
       "vrPpSrBpForwardTransitions": vrPpSrBpForwardTransitions,
       "vrPpSrBpBlockingDiscards": vrPpSrBpBlockingDiscards,
       "vrPpSrBpDesignatedRoot": vrPpSrBpDesignatedRoot,
       "vrPpSrBpStatsTable": vrPpSrBpStatsTable,
       "vrPpSrBpStatsEntry": vrPpSrBpStatsEntry,
       "vrPpSrBpBadAbstractDiscards": vrPpSrBpBadAbstractDiscards,
       "vrPpSrBpTinygramFramesIn": vrPpSrBpTinygramFramesIn,
       "vrPpSrBpTinygramFramesOut": vrPpSrBpTinygramFramesOut,
       "vrPpSrBpInFilterDiscards": vrPpSrBpInFilterDiscards,
       "vrPpSrBpOutFilterDiscards": vrPpSrBpOutFilterDiscards,
       "vrPpSrBpSrProvTable": vrPpSrBpSrProvTable,
       "vrPpSrBpSrProvEntry": vrPpSrBpSrProvEntry,
       "vrPpSrBpHopCount": vrPpSrBpHopCount,
       "vrPpSrBpExploreFrameTreatment": vrPpSrBpExploreFrameTreatment,
       "vrPpSrBpLanId": vrPpSrBpLanId,
       "vrPpSrBpInternalLanId": vrPpSrBpInternalLanId,
       "vrPpSrBpBridgeNum": vrPpSrBpBridgeNum,
       "vrPpSrBpLargestFrame": vrPpSrBpLargestFrame,
       "vrPpSrBpSteSpanMode": vrPpSrBpSteSpanMode,
       "vrPpSrBpAreRdLimit": vrPpSrBpAreRdLimit,
       "vrPpSrBpSteRdLimit": vrPpSrBpSteRdLimit,
       "vrPpSrBpSrStatsTable": vrPpSrBpSrStatsTable,
       "vrPpSrBpSrStatsEntry": vrPpSrBpSrStatsEntry,
       "vrPpSrBpSpecInFrames": vrPpSrBpSpecInFrames,
       "vrPpSrBpSpecOutFrames": vrPpSrBpSpecOutFrames,
       "vrPpSrBpApeInFrames": vrPpSrBpApeInFrames,
       "vrPpSrBpApeOutFrames": vrPpSrBpApeOutFrames,
       "vrPpSrBpSteInFrames": vrPpSrBpSteInFrames,
       "vrPpSrBpSteOutFrames": vrPpSrBpSteOutFrames,
       "vrPpSrBpSegmentMismatchDiscards": vrPpSrBpSegmentMismatchDiscards,
       "vrPpSrBpDupSegmentDiscards": vrPpSrBpDupSegmentDiscards,
       "vrPpSrBpHopCountExceededDiscards": vrPpSrBpHopCountExceededDiscards,
       "vrPpSrBpDupLanIdOrTreeErrors": vrPpSrBpDupLanIdOrTreeErrors,
       "vrPpSrBpLanIdMismatches": vrPpSrBpLanIdMismatches,
       "vrPpSrBpStaticDiscards": vrPpSrBpStaticDiscards,
       "vrPpSrBpDynamicDiscards": vrPpSrBpDynamicDiscards,
       "vrPpSrtBp": vrPpSrtBp,
       "vrPpSrtBpRowStatusTable": vrPpSrtBpRowStatusTable,
       "vrPpSrtBpRowStatusEntry": vrPpSrtBpRowStatusEntry,
       "vrPpSrtBpRowStatus": vrPpSrtBpRowStatus,
       "vrPpSrtBpComponentName": vrPpSrtBpComponentName,
       "vrPpSrtBpStorageType": vrPpSrtBpStorageType,
       "vrPpSrtBpIndex": vrPpSrtBpIndex,
       "vrPpSrtBpNs": vrPpSrtBpNs,
       "vrPpSrtBpNsRowStatusTable": vrPpSrtBpNsRowStatusTable,
       "vrPpSrtBpNsRowStatusEntry": vrPpSrtBpNsRowStatusEntry,
       "vrPpSrtBpNsRowStatus": vrPpSrtBpNsRowStatus,
       "vrPpSrtBpNsComponentName": vrPpSrtBpNsComponentName,
       "vrPpSrtBpNsStorageType": vrPpSrtBpNsStorageType,
       "vrPpSrtBpNsIndex": vrPpSrtBpNsIndex,
       "vrPpSrtBpNsProvTable": vrPpSrtBpNsProvTable,
       "vrPpSrtBpNsProvEntry": vrPpSrtBpNsProvEntry,
       "vrPpSrtBpNsIncomingFilter": vrPpSrtBpNsIncomingFilter,
       "vrPpSrtBpNsOutgoingFilter": vrPpSrtBpNsOutgoingFilter,
       "vrPpSrtBpProvTable": vrPpSrtBpProvTable,
       "vrPpSrtBpProvEntry": vrPpSrtBpProvEntry,
       "vrPpSrtBpTranslateIpx": vrPpSrtBpTranslateIpx,
       "vrPpSrtBpFragmentIp": vrPpSrtBpFragmentIp,
       "vrPpSrtBpServiceClass": vrPpSrtBpServiceClass,
       "vrPpSrtBpConvertArpMacAddress": vrPpSrtBpConvertArpMacAddress,
       "vrPpSrtBpPortNum": vrPpSrtBpPortNum,
       "vrPpSrtBpOutboundFrameMediaType": vrPpSrtBpOutboundFrameMediaType,
       "vrPpSrtBpTbProvTable": vrPpSrtBpTbProvTable,
       "vrPpSrtBpTbProvEntry": vrPpSrtBpTbProvEntry,
       "vrPpSrtBpSecureOption": vrPpSrtBpSecureOption,
       "vrPpSrtBpStpProvTable": vrPpSrtBpStpProvTable,
       "vrPpSrtBpStpProvEntry": vrPpSrtBpStpProvEntry,
       "vrPpSrtBpAdminStatus": vrPpSrtBpAdminStatus,
       "vrPpSrtBpPortStateStpControl": vrPpSrtBpPortStateStpControl,
       "vrPpSrtBpStpTypeProv": vrPpSrtBpStpTypeProv,
       "vrPpSrtBpPortPriority": vrPpSrtBpPortPriority,
       "vrPpSrtBpPathCost": vrPpSrtBpPathCost,
       "vrPpSrtBpPathCostMethod": vrPpSrtBpPathCostMethod,
       "vrPpSrtBpDIProvTable": vrPpSrtBpDIProvTable,
       "vrPpSrtBpDIProvEntry": vrPpSrtBpDIProvEntry,
       "vrPpSrtBpDomainNum": vrPpSrtBpDomainNum,
       "vrPpSrtBpPreserveDomain": vrPpSrtBpPreserveDomain,
       "vrPpSrtBpStateTable": vrPpSrtBpStateTable,
       "vrPpSrtBpStateEntry": vrPpSrtBpStateEntry,
       "vrPpSrtBpAdminState": vrPpSrtBpAdminState,
       "vrPpSrtBpOperationalState": vrPpSrtBpOperationalState,
       "vrPpSrtBpUsageState": vrPpSrtBpUsageState,
       "vrPpSrtBpOperStatusTable": vrPpSrtBpOperStatusTable,
       "vrPpSrtBpOperStatusEntry": vrPpSrtBpOperStatusEntry,
       "vrPpSrtBpSnmpOperStatus": vrPpSrtBpSnmpOperStatus,
       "vrPpSrtBpOperTable": vrPpSrtBpOperTable,
       "vrPpSrtBpOperEntry": vrPpSrtBpOperEntry,
       "vrPpSrtBpPortName": vrPpSrtBpPortName,
       "vrPpSrtBpUpTime": vrPpSrtBpUpTime,
       "vrPpSrtBpDownTime": vrPpSrtBpDownTime,
       "vrPpSrtBpBridgingMode": vrPpSrtBpBridgingMode,
       "vrPpSrtBpBridgePortConfig": vrPpSrtBpBridgePortConfig,
       "vrPpSrtBpBridgePortType": vrPpSrtBpBridgePortType,
       "vrPpSrtBpIfIndex": vrPpSrtBpIfIndex,
       "vrPpSrtBpDelayExceededDiscards": vrPpSrtBpDelayExceededDiscards,
       "vrPpSrtBpMtuExceededDiscards": vrPpSrtBpMtuExceededDiscards,
       "vrPpSrtBpTbOperTable": vrPpSrtBpTbOperTable,
       "vrPpSrtBpTbOperEntry": vrPpSrtBpTbOperEntry,
       "vrPpSrtBpMaxInfo": vrPpSrtBpMaxInfo,
       "vrPpSrtBpBadVerifyDiscards": vrPpSrtBpBadVerifyDiscards,
       "vrPpSrtBpUnicastNoMatches": vrPpSrtBpUnicastNoMatches,
       "vrPpSrtBpStaticEntryDiscards": vrPpSrtBpStaticEntryDiscards,
       "vrPpSrtBpDynamicEntryDiscards": vrPpSrtBpDynamicEntryDiscards,
       "vrPpSrtBpLearningDiscards": vrPpSrtBpLearningDiscards,
       "vrPpSrtBpInDiscards": vrPpSrtBpInDiscards,
       "vrPpSrtBpInFrames": vrPpSrtBpInFrames,
       "vrPpSrtBpOutFrames": vrPpSrtBpOutFrames,
       "vrPpSrtBpStpOperTable": vrPpSrtBpStpOperTable,
       "vrPpSrtBpStpOperEntry": vrPpSrtBpStpOperEntry,
       "vrPpSrtBpStpPortState": vrPpSrtBpStpPortState,
       "vrPpSrtBpStpTypeOper": vrPpSrtBpStpTypeOper,
       "vrPpSrtBpDesignatedCost": vrPpSrtBpDesignatedCost,
       "vrPpSrtBpPathCostOper": vrPpSrtBpPathCostOper,
       "vrPpSrtBpDesignatedBridge": vrPpSrtBpDesignatedBridge,
       "vrPpSrtBpDesignatedPort": vrPpSrtBpDesignatedPort,
       "vrPpSrtBpForwardTransitions": vrPpSrtBpForwardTransitions,
       "vrPpSrtBpBlockingDiscards": vrPpSrtBpBlockingDiscards,
       "vrPpSrtBpDesignatedRoot": vrPpSrtBpDesignatedRoot,
       "vrPpSrtBpStatsTable": vrPpSrtBpStatsTable,
       "vrPpSrtBpStatsEntry": vrPpSrtBpStatsEntry,
       "vrPpSrtBpBadAbstractDiscards": vrPpSrtBpBadAbstractDiscards,
       "vrPpSrtBpTinygramFramesIn": vrPpSrtBpTinygramFramesIn,
       "vrPpSrtBpTinygramFramesOut": vrPpSrtBpTinygramFramesOut,
       "vrPpSrtBpInFilterDiscards": vrPpSrtBpInFilterDiscards,
       "vrPpSrtBpOutFilterDiscards": vrPpSrtBpOutFilterDiscards,
       "vrPpSrtBpSrProvTable": vrPpSrtBpSrProvTable,
       "vrPpSrtBpSrProvEntry": vrPpSrtBpSrProvEntry,
       "vrPpSrtBpHopCount": vrPpSrtBpHopCount,
       "vrPpSrtBpExploreFrameTreatment": vrPpSrtBpExploreFrameTreatment,
       "vrPpSrtBpLanId": vrPpSrtBpLanId,
       "vrPpSrtBpInternalLanId": vrPpSrtBpInternalLanId,
       "vrPpSrtBpBridgeNum": vrPpSrtBpBridgeNum,
       "vrPpSrtBpLargestFrame": vrPpSrtBpLargestFrame,
       "vrPpSrtBpSteSpanMode": vrPpSrtBpSteSpanMode,
       "vrPpSrtBpAreRdLimit": vrPpSrtBpAreRdLimit,
       "vrPpSrtBpSteRdLimit": vrPpSrtBpSteRdLimit,
       "vrPpSrtBpSrStatsTable": vrPpSrtBpSrStatsTable,
       "vrPpSrtBpSrStatsEntry": vrPpSrtBpSrStatsEntry,
       "vrPpSrtBpSpecInFrames": vrPpSrtBpSpecInFrames,
       "vrPpSrtBpSpecOutFrames": vrPpSrtBpSpecOutFrames,
       "vrPpSrtBpApeInFrames": vrPpSrtBpApeInFrames,
       "vrPpSrtBpApeOutFrames": vrPpSrtBpApeOutFrames,
       "vrPpSrtBpSteInFrames": vrPpSrtBpSteInFrames,
       "vrPpSrtBpSteOutFrames": vrPpSrtBpSteOutFrames,
       "vrPpSrtBpSegmentMismatchDiscards": vrPpSrtBpSegmentMismatchDiscards,
       "vrPpSrtBpDupSegmentDiscards": vrPpSrtBpDupSegmentDiscards,
       "vrPpSrtBpHopCountExceededDiscards": vrPpSrtBpHopCountExceededDiscards,
       "vrPpSrtBpDupLanIdOrTreeErrors": vrPpSrtBpDupLanIdOrTreeErrors,
       "vrPpSrtBpLanIdMismatches": vrPpSrtBpLanIdMismatches,
       "vrPpSrtBpStaticDiscards": vrPpSrtBpStaticDiscards,
       "vrPpSrtBpDynamicDiscards": vrPpSrtBpDynamicDiscards,
       "vrPpSrse": vrPpSrse,
       "vrPpSrseRowStatusTable": vrPpSrseRowStatusTable,
       "vrPpSrseRowStatusEntry": vrPpSrseRowStatusEntry,
       "vrPpSrseRowStatus": vrPpSrseRowStatus,
       "vrPpSrseComponentName": vrPpSrseComponentName,
       "vrPpSrseStorageType": vrPpSrseStorageType,
       "vrPpSrseIndex": vrPpSrseIndex,
       "vrPpSrseProvTable": vrPpSrseProvTable,
       "vrPpSrseProvEntry": vrPpSrseProvEntry,
       "vrPpSrseTranslateIpx": vrPpSrseTranslateIpx,
       "vrPpSrseFragmentIp": vrPpSrseFragmentIp,
       "vrPpSrseServiceClass": vrPpSrseServiceClass,
       "vrPpSrseConvertArpMacAddress": vrPpSrseConvertArpMacAddress,
       "vrPpSrsePortNum": vrPpSrsePortNum,
       "vrPpSrseOutboundFrameMediaType": vrPpSrseOutboundFrameMediaType,
       "vrPpSrseStpProvTable": vrPpSrseStpProvTable,
       "vrPpSrseStpProvEntry": vrPpSrseStpProvEntry,
       "vrPpSrseAdminStatus": vrPpSrseAdminStatus,
       "vrPpSrsePortStateStpControl": vrPpSrsePortStateStpControl,
       "vrPpSrseStpTypeProv": vrPpSrseStpTypeProv,
       "vrPpSrsePortPriority": vrPpSrsePortPriority,
       "vrPpSrsePathCost": vrPpSrsePathCost,
       "vrPpSrsePathCostMethod": vrPpSrsePathCostMethod,
       "vrPpSrseDIProvTable": vrPpSrseDIProvTable,
       "vrPpSrseDIProvEntry": vrPpSrseDIProvEntry,
       "vrPpSrseDomainNum": vrPpSrseDomainNum,
       "vrPpSrsePreserveDomain": vrPpSrsePreserveDomain,
       "vrPpSrseStateTable": vrPpSrseStateTable,
       "vrPpSrseStateEntry": vrPpSrseStateEntry,
       "vrPpSrseAdminState": vrPpSrseAdminState,
       "vrPpSrseOperationalState": vrPpSrseOperationalState,
       "vrPpSrseUsageState": vrPpSrseUsageState,
       "vrPpSrseOperStatusTable": vrPpSrseOperStatusTable,
       "vrPpSrseOperStatusEntry": vrPpSrseOperStatusEntry,
       "vrPpSrseSnmpOperStatus": vrPpSrseSnmpOperStatus,
       "vrPpSrseOperTable": vrPpSrseOperTable,
       "vrPpSrseOperEntry": vrPpSrseOperEntry,
       "vrPpSrsePortName": vrPpSrsePortName,
       "vrPpSrseUpTime": vrPpSrseUpTime,
       "vrPpSrseDownTime": vrPpSrseDownTime,
       "vrPpSrseBridgingMode": vrPpSrseBridgingMode,
       "vrPpSrseBridgePortConfig": vrPpSrseBridgePortConfig,
       "vrPpSrseBridgePortType": vrPpSrseBridgePortType,
       "vrPpSrseIfIndex": vrPpSrseIfIndex,
       "vrPpSrseDelayExceededDiscards": vrPpSrseDelayExceededDiscards,
       "vrPpSrseMtuExceededDiscards": vrPpSrseMtuExceededDiscards,
       "vrPpSrseStpOperTable": vrPpSrseStpOperTable,
       "vrPpSrseStpOperEntry": vrPpSrseStpOperEntry,
       "vrPpSrseStpPortState": vrPpSrseStpPortState,
       "vrPpSrseStpTypeOper": vrPpSrseStpTypeOper,
       "vrPpSrseDesignatedCost": vrPpSrseDesignatedCost,
       "vrPpSrsePathCostOper": vrPpSrsePathCostOper,
       "vrPpSrseDesignatedBridge": vrPpSrseDesignatedBridge,
       "vrPpSrseDesignatedPort": vrPpSrseDesignatedPort,
       "vrPpSrseForwardTransitions": vrPpSrseForwardTransitions,
       "vrPpSrseBlockingDiscards": vrPpSrseBlockingDiscards,
       "vrPpSrseDesignatedRoot": vrPpSrseDesignatedRoot,
       "vrPpSrseStatsTable": vrPpSrseStatsTable,
       "vrPpSrseStatsEntry": vrPpSrseStatsEntry,
       "vrPpSrseBadAbstractDiscards": vrPpSrseBadAbstractDiscards,
       "vrPpSrseTinygramFramesIn": vrPpSrseTinygramFramesIn,
       "vrPpSrseTinygramFramesOut": vrPpSrseTinygramFramesOut,
       "vrPpSrseInFilterDiscards": vrPpSrseInFilterDiscards,
       "vrPpSrseOutFilterDiscards": vrPpSrseOutFilterDiscards,
       "vrPpSrseSrProvTable": vrPpSrseSrProvTable,
       "vrPpSrseSrProvEntry": vrPpSrseSrProvEntry,
       "vrPpSrseHopCount": vrPpSrseHopCount,
       "vrPpSrseExploreFrameTreatment": vrPpSrseExploreFrameTreatment,
       "vrPpSrseLanId": vrPpSrseLanId,
       "vrPpSrseInternalLanId": vrPpSrseInternalLanId,
       "vrPpSrseBridgeNum": vrPpSrseBridgeNum,
       "vrPpSrseLargestFrame": vrPpSrseLargestFrame,
       "vrPpSrseSteSpanMode": vrPpSrseSteSpanMode,
       "vrPpSrseAreRdLimit": vrPpSrseAreRdLimit,
       "vrPpSrseSteRdLimit": vrPpSrseSteRdLimit,
       "vrPpSrseSrStatsTable": vrPpSrseSrStatsTable,
       "vrPpSrseSrStatsEntry": vrPpSrseSrStatsEntry,
       "vrPpSrseSpecInFrames": vrPpSrseSpecInFrames,
       "vrPpSrseSpecOutFrames": vrPpSrseSpecOutFrames,
       "vrPpSrseApeInFrames": vrPpSrseApeInFrames,
       "vrPpSrseApeOutFrames": vrPpSrseApeOutFrames,
       "vrPpSrseSteInFrames": vrPpSrseSteInFrames,
       "vrPpSrseSteOutFrames": vrPpSrseSteOutFrames,
       "vrPpSrseSegmentMismatchDiscards": vrPpSrseSegmentMismatchDiscards,
       "vrPpSrseDupSegmentDiscards": vrPpSrseDupSegmentDiscards,
       "vrPpSrseHopCountExceededDiscards": vrPpSrseHopCountExceededDiscards,
       "vrPpSrseDupLanIdOrTreeErrors": vrPpSrseDupLanIdOrTreeErrors,
       "vrPpSrseLanIdMismatches": vrPpSrseLanIdMismatches,
       "vrPpSrseStaticDiscards": vrPpSrseStaticDiscards,
       "vrPpSrseDynamicDiscards": vrPpSrseDynamicDiscards,
       "vrPpTbse": vrPpTbse,
       "vrPpTbseRowStatusTable": vrPpTbseRowStatusTable,
       "vrPpTbseRowStatusEntry": vrPpTbseRowStatusEntry,
       "vrPpTbseRowStatus": vrPpTbseRowStatus,
       "vrPpTbseComponentName": vrPpTbseComponentName,
       "vrPpTbseStorageType": vrPpTbseStorageType,
       "vrPpTbseIndex": vrPpTbseIndex,
       "vrPpTbseProvTable": vrPpTbseProvTable,
       "vrPpTbseProvEntry": vrPpTbseProvEntry,
       "vrPpTbseTranslateIpx": vrPpTbseTranslateIpx,
       "vrPpTbseFragmentIp": vrPpTbseFragmentIp,
       "vrPpTbseServiceClass": vrPpTbseServiceClass,
       "vrPpTbseConvertArpMacAddress": vrPpTbseConvertArpMacAddress,
       "vrPpTbsePortNum": vrPpTbsePortNum,
       "vrPpTbseOutboundFrameMediaType": vrPpTbseOutboundFrameMediaType,
       "vrPpTbseTbProvTable": vrPpTbseTbProvTable,
       "vrPpTbseTbProvEntry": vrPpTbseTbProvEntry,
       "vrPpTbseSecureOption": vrPpTbseSecureOption,
       "vrPpTbseStpProvTable": vrPpTbseStpProvTable,
       "vrPpTbseStpProvEntry": vrPpTbseStpProvEntry,
       "vrPpTbseAdminStatus": vrPpTbseAdminStatus,
       "vrPpTbsePortStateStpControl": vrPpTbsePortStateStpControl,
       "vrPpTbseStpTypeProv": vrPpTbseStpTypeProv,
       "vrPpTbsePortPriority": vrPpTbsePortPriority,
       "vrPpTbsePathCost": vrPpTbsePathCost,
       "vrPpTbsePathCostMethod": vrPpTbsePathCostMethod,
       "vrPpTbseDIProvTable": vrPpTbseDIProvTable,
       "vrPpTbseDIProvEntry": vrPpTbseDIProvEntry,
       "vrPpTbseDomainNum": vrPpTbseDomainNum,
       "vrPpTbsePreserveDomain": vrPpTbsePreserveDomain,
       "vrPpTbseStateTable": vrPpTbseStateTable,
       "vrPpTbseStateEntry": vrPpTbseStateEntry,
       "vrPpTbseAdminState": vrPpTbseAdminState,
       "vrPpTbseOperationalState": vrPpTbseOperationalState,
       "vrPpTbseUsageState": vrPpTbseUsageState,
       "vrPpTbseOperStatusTable": vrPpTbseOperStatusTable,
       "vrPpTbseOperStatusEntry": vrPpTbseOperStatusEntry,
       "vrPpTbseSnmpOperStatus": vrPpTbseSnmpOperStatus,
       "vrPpTbseOperTable": vrPpTbseOperTable,
       "vrPpTbseOperEntry": vrPpTbseOperEntry,
       "vrPpTbsePortName": vrPpTbsePortName,
       "vrPpTbseUpTime": vrPpTbseUpTime,
       "vrPpTbseDownTime": vrPpTbseDownTime,
       "vrPpTbseBridgingMode": vrPpTbseBridgingMode,
       "vrPpTbseBridgePortConfig": vrPpTbseBridgePortConfig,
       "vrPpTbseBridgePortType": vrPpTbseBridgePortType,
       "vrPpTbseIfIndex": vrPpTbseIfIndex,
       "vrPpTbseDelayExceededDiscards": vrPpTbseDelayExceededDiscards,
       "vrPpTbseMtuExceededDiscards": vrPpTbseMtuExceededDiscards,
       "vrPpTbseTbOperTable": vrPpTbseTbOperTable,
       "vrPpTbseTbOperEntry": vrPpTbseTbOperEntry,
       "vrPpTbseMaxInfo": vrPpTbseMaxInfo,
       "vrPpTbseBadVerifyDiscards": vrPpTbseBadVerifyDiscards,
       "vrPpTbseUnicastNoMatches": vrPpTbseUnicastNoMatches,
       "vrPpTbseStaticEntryDiscards": vrPpTbseStaticEntryDiscards,
       "vrPpTbseDynamicEntryDiscards": vrPpTbseDynamicEntryDiscards,
       "vrPpTbseLearningDiscards": vrPpTbseLearningDiscards,
       "vrPpTbseInDiscards": vrPpTbseInDiscards,
       "vrPpTbseInFrames": vrPpTbseInFrames,
       "vrPpTbseOutFrames": vrPpTbseOutFrames,
       "vrPpTbseStpOperTable": vrPpTbseStpOperTable,
       "vrPpTbseStpOperEntry": vrPpTbseStpOperEntry,
       "vrPpTbseStpPortState": vrPpTbseStpPortState,
       "vrPpTbseStpTypeOper": vrPpTbseStpTypeOper,
       "vrPpTbseDesignatedCost": vrPpTbseDesignatedCost,
       "vrPpTbsePathCostOper": vrPpTbsePathCostOper,
       "vrPpTbseDesignatedBridge": vrPpTbseDesignatedBridge,
       "vrPpTbseDesignatedPort": vrPpTbseDesignatedPort,
       "vrPpTbseForwardTransitions": vrPpTbseForwardTransitions,
       "vrPpTbseBlockingDiscards": vrPpTbseBlockingDiscards,
       "vrPpTbseDesignatedRoot": vrPpTbseDesignatedRoot,
       "vrPpTbseStatsTable": vrPpTbseStatsTable,
       "vrPpTbseStatsEntry": vrPpTbseStatsEntry,
       "vrPpTbseBadAbstractDiscards": vrPpTbseBadAbstractDiscards,
       "vrPpTbseTinygramFramesIn": vrPpTbseTinygramFramesIn,
       "vrPpTbseTinygramFramesOut": vrPpTbseTinygramFramesOut,
       "vrPpTbseInFilterDiscards": vrPpTbseInFilterDiscards,
       "vrPpTbseOutFilterDiscards": vrPpTbseOutFilterDiscards,
       "vrPpSrsg": vrPpSrsg,
       "vrPpSrsgRowStatusTable": vrPpSrsgRowStatusTable,
       "vrPpSrsgRowStatusEntry": vrPpSrsgRowStatusEntry,
       "vrPpSrsgRowStatus": vrPpSrsgRowStatus,
       "vrPpSrsgComponentName": vrPpSrsgComponentName,
       "vrPpSrsgStorageType": vrPpSrsgStorageType,
       "vrPpSrsgIndex": vrPpSrsgIndex,
       "vrPpSrsgProvTable": vrPpSrsgProvTable,
       "vrPpSrsgProvEntry": vrPpSrsgProvEntry,
       "vrPpSrsgTranslateIpx": vrPpSrsgTranslateIpx,
       "vrPpSrsgFragmentIp": vrPpSrsgFragmentIp,
       "vrPpSrsgServiceClass": vrPpSrsgServiceClass,
       "vrPpSrsgConvertArpMacAddress": vrPpSrsgConvertArpMacAddress,
       "vrPpSrsgPortNum": vrPpSrsgPortNum,
       "vrPpSrsgOutboundFrameMediaType": vrPpSrsgOutboundFrameMediaType,
       "vrPpSrsgStpProvTable": vrPpSrsgStpProvTable,
       "vrPpSrsgStpProvEntry": vrPpSrsgStpProvEntry,
       "vrPpSrsgAdminStatus": vrPpSrsgAdminStatus,
       "vrPpSrsgPortStateStpControl": vrPpSrsgPortStateStpControl,
       "vrPpSrsgStpTypeProv": vrPpSrsgStpTypeProv,
       "vrPpSrsgPortPriority": vrPpSrsgPortPriority,
       "vrPpSrsgPathCost": vrPpSrsgPathCost,
       "vrPpSrsgPathCostMethod": vrPpSrsgPathCostMethod,
       "vrPpSrsgDIProvTable": vrPpSrsgDIProvTable,
       "vrPpSrsgDIProvEntry": vrPpSrsgDIProvEntry,
       "vrPpSrsgDomainNum": vrPpSrsgDomainNum,
       "vrPpSrsgPreserveDomain": vrPpSrsgPreserveDomain,
       "vrPpSrsgStateTable": vrPpSrsgStateTable,
       "vrPpSrsgStateEntry": vrPpSrsgStateEntry,
       "vrPpSrsgAdminState": vrPpSrsgAdminState,
       "vrPpSrsgOperationalState": vrPpSrsgOperationalState,
       "vrPpSrsgUsageState": vrPpSrsgUsageState,
       "vrPpSrsgOperStatusTable": vrPpSrsgOperStatusTable,
       "vrPpSrsgOperStatusEntry": vrPpSrsgOperStatusEntry,
       "vrPpSrsgSnmpOperStatus": vrPpSrsgSnmpOperStatus,
       "vrPpSrsgOperTable": vrPpSrsgOperTable,
       "vrPpSrsgOperEntry": vrPpSrsgOperEntry,
       "vrPpSrsgPortName": vrPpSrsgPortName,
       "vrPpSrsgUpTime": vrPpSrsgUpTime,
       "vrPpSrsgDownTime": vrPpSrsgDownTime,
       "vrPpSrsgBridgingMode": vrPpSrsgBridgingMode,
       "vrPpSrsgBridgePortConfig": vrPpSrsgBridgePortConfig,
       "vrPpSrsgBridgePortType": vrPpSrsgBridgePortType,
       "vrPpSrsgIfIndex": vrPpSrsgIfIndex,
       "vrPpSrsgDelayExceededDiscards": vrPpSrsgDelayExceededDiscards,
       "vrPpSrsgMtuExceededDiscards": vrPpSrsgMtuExceededDiscards,
       "vrPpSrsgStpOperTable": vrPpSrsgStpOperTable,
       "vrPpSrsgStpOperEntry": vrPpSrsgStpOperEntry,
       "vrPpSrsgStpPortState": vrPpSrsgStpPortState,
       "vrPpSrsgStpTypeOper": vrPpSrsgStpTypeOper,
       "vrPpSrsgDesignatedCost": vrPpSrsgDesignatedCost,
       "vrPpSrsgPathCostOper": vrPpSrsgPathCostOper,
       "vrPpSrsgDesignatedBridge": vrPpSrsgDesignatedBridge,
       "vrPpSrsgDesignatedPort": vrPpSrsgDesignatedPort,
       "vrPpSrsgForwardTransitions": vrPpSrsgForwardTransitions,
       "vrPpSrsgBlockingDiscards": vrPpSrsgBlockingDiscards,
       "vrPpSrsgDesignatedRoot": vrPpSrsgDesignatedRoot,
       "vrPpSrsgStatsTable": vrPpSrsgStatsTable,
       "vrPpSrsgStatsEntry": vrPpSrsgStatsEntry,
       "vrPpSrsgBadAbstractDiscards": vrPpSrsgBadAbstractDiscards,
       "vrPpSrsgTinygramFramesIn": vrPpSrsgTinygramFramesIn,
       "vrPpSrsgTinygramFramesOut": vrPpSrsgTinygramFramesOut,
       "vrPpSrsgInFilterDiscards": vrPpSrsgInFilterDiscards,
       "vrPpSrsgOutFilterDiscards": vrPpSrsgOutFilterDiscards,
       "vrPpSrsgSrProvTable": vrPpSrsgSrProvTable,
       "vrPpSrsgSrProvEntry": vrPpSrsgSrProvEntry,
       "vrPpSrsgHopCount": vrPpSrsgHopCount,
       "vrPpSrsgExploreFrameTreatment": vrPpSrsgExploreFrameTreatment,
       "vrPpSrsgLanId": vrPpSrsgLanId,
       "vrPpSrsgInternalLanId": vrPpSrsgInternalLanId,
       "vrPpSrsgBridgeNum": vrPpSrsgBridgeNum,
       "vrPpSrsgLargestFrame": vrPpSrsgLargestFrame,
       "vrPpSrsgSteSpanMode": vrPpSrsgSteSpanMode,
       "vrPpSrsgAreRdLimit": vrPpSrsgAreRdLimit,
       "vrPpSrsgSteRdLimit": vrPpSrsgSteRdLimit,
       "vrPpSrsgSrStatsTable": vrPpSrsgSrStatsTable,
       "vrPpSrsgSrStatsEntry": vrPpSrsgSrStatsEntry,
       "vrPpSrsgSpecInFrames": vrPpSrsgSpecInFrames,
       "vrPpSrsgSpecOutFrames": vrPpSrsgSpecOutFrames,
       "vrPpSrsgApeInFrames": vrPpSrsgApeInFrames,
       "vrPpSrsgApeOutFrames": vrPpSrsgApeOutFrames,
       "vrPpSrsgSteInFrames": vrPpSrsgSteInFrames,
       "vrPpSrsgSteOutFrames": vrPpSrsgSteOutFrames,
       "vrPpSrsgSegmentMismatchDiscards": vrPpSrsgSegmentMismatchDiscards,
       "vrPpSrsgDupSegmentDiscards": vrPpSrsgDupSegmentDiscards,
       "vrPpSrsgHopCountExceededDiscards": vrPpSrsgHopCountExceededDiscards,
       "vrPpSrsgDupLanIdOrTreeErrors": vrPpSrsgDupLanIdOrTreeErrors,
       "vrPpSrsgLanIdMismatches": vrPpSrsgLanIdMismatches,
       "vrPpSrsgStaticDiscards": vrPpSrsgStaticDiscards,
       "vrPpSrsgDynamicDiscards": vrPpSrsgDynamicDiscards,
       "vrPpTbsg": vrPpTbsg,
       "vrPpTbsgRowStatusTable": vrPpTbsgRowStatusTable,
       "vrPpTbsgRowStatusEntry": vrPpTbsgRowStatusEntry,
       "vrPpTbsgRowStatus": vrPpTbsgRowStatus,
       "vrPpTbsgComponentName": vrPpTbsgComponentName,
       "vrPpTbsgStorageType": vrPpTbsgStorageType,
       "vrPpTbsgIndex": vrPpTbsgIndex,
       "vrPpTbsgProvTable": vrPpTbsgProvTable,
       "vrPpTbsgProvEntry": vrPpTbsgProvEntry,
       "vrPpTbsgTranslateIpx": vrPpTbsgTranslateIpx,
       "vrPpTbsgFragmentIp": vrPpTbsgFragmentIp,
       "vrPpTbsgServiceClass": vrPpTbsgServiceClass,
       "vrPpTbsgConvertArpMacAddress": vrPpTbsgConvertArpMacAddress,
       "vrPpTbsgPortNum": vrPpTbsgPortNum,
       "vrPpTbsgOutboundFrameMediaType": vrPpTbsgOutboundFrameMediaType,
       "vrPpTbsgTbProvTable": vrPpTbsgTbProvTable,
       "vrPpTbsgTbProvEntry": vrPpTbsgTbProvEntry,
       "vrPpTbsgSecureOption": vrPpTbsgSecureOption,
       "vrPpTbsgStpProvTable": vrPpTbsgStpProvTable,
       "vrPpTbsgStpProvEntry": vrPpTbsgStpProvEntry,
       "vrPpTbsgAdminStatus": vrPpTbsgAdminStatus,
       "vrPpTbsgPortStateStpControl": vrPpTbsgPortStateStpControl,
       "vrPpTbsgStpTypeProv": vrPpTbsgStpTypeProv,
       "vrPpTbsgPortPriority": vrPpTbsgPortPriority,
       "vrPpTbsgPathCost": vrPpTbsgPathCost,
       "vrPpTbsgPathCostMethod": vrPpTbsgPathCostMethod,
       "vrPpTbsgDIProvTable": vrPpTbsgDIProvTable,
       "vrPpTbsgDIProvEntry": vrPpTbsgDIProvEntry,
       "vrPpTbsgDomainNum": vrPpTbsgDomainNum,
       "vrPpTbsgPreserveDomain": vrPpTbsgPreserveDomain,
       "vrPpTbsgStateTable": vrPpTbsgStateTable,
       "vrPpTbsgStateEntry": vrPpTbsgStateEntry,
       "vrPpTbsgAdminState": vrPpTbsgAdminState,
       "vrPpTbsgOperationalState": vrPpTbsgOperationalState,
       "vrPpTbsgUsageState": vrPpTbsgUsageState,
       "vrPpTbsgOperStatusTable": vrPpTbsgOperStatusTable,
       "vrPpTbsgOperStatusEntry": vrPpTbsgOperStatusEntry,
       "vrPpTbsgSnmpOperStatus": vrPpTbsgSnmpOperStatus,
       "vrPpTbsgOperTable": vrPpTbsgOperTable,
       "vrPpTbsgOperEntry": vrPpTbsgOperEntry,
       "vrPpTbsgPortName": vrPpTbsgPortName,
       "vrPpTbsgUpTime": vrPpTbsgUpTime,
       "vrPpTbsgDownTime": vrPpTbsgDownTime,
       "vrPpTbsgBridgingMode": vrPpTbsgBridgingMode,
       "vrPpTbsgBridgePortConfig": vrPpTbsgBridgePortConfig,
       "vrPpTbsgBridgePortType": vrPpTbsgBridgePortType,
       "vrPpTbsgIfIndex": vrPpTbsgIfIndex,
       "vrPpTbsgDelayExceededDiscards": vrPpTbsgDelayExceededDiscards,
       "vrPpTbsgMtuExceededDiscards": vrPpTbsgMtuExceededDiscards,
       "vrPpTbsgTbOperTable": vrPpTbsgTbOperTable,
       "vrPpTbsgTbOperEntry": vrPpTbsgTbOperEntry,
       "vrPpTbsgMaxInfo": vrPpTbsgMaxInfo,
       "vrPpTbsgBadVerifyDiscards": vrPpTbsgBadVerifyDiscards,
       "vrPpTbsgUnicastNoMatches": vrPpTbsgUnicastNoMatches,
       "vrPpTbsgStaticEntryDiscards": vrPpTbsgStaticEntryDiscards,
       "vrPpTbsgDynamicEntryDiscards": vrPpTbsgDynamicEntryDiscards,
       "vrPpTbsgLearningDiscards": vrPpTbsgLearningDiscards,
       "vrPpTbsgInDiscards": vrPpTbsgInDiscards,
       "vrPpTbsgInFrames": vrPpTbsgInFrames,
       "vrPpTbsgOutFrames": vrPpTbsgOutFrames,
       "vrPpTbsgStpOperTable": vrPpTbsgStpOperTable,
       "vrPpTbsgStpOperEntry": vrPpTbsgStpOperEntry,
       "vrPpTbsgStpPortState": vrPpTbsgStpPortState,
       "vrPpTbsgStpTypeOper": vrPpTbsgStpTypeOper,
       "vrPpTbsgDesignatedCost": vrPpTbsgDesignatedCost,
       "vrPpTbsgPathCostOper": vrPpTbsgPathCostOper,
       "vrPpTbsgDesignatedBridge": vrPpTbsgDesignatedBridge,
       "vrPpTbsgDesignatedPort": vrPpTbsgDesignatedPort,
       "vrPpTbsgForwardTransitions": vrPpTbsgForwardTransitions,
       "vrPpTbsgBlockingDiscards": vrPpTbsgBlockingDiscards,
       "vrPpTbsgDesignatedRoot": vrPpTbsgDesignatedRoot,
       "vrPpTbsgStatsTable": vrPpTbsgStatsTable,
       "vrPpTbsgStatsEntry": vrPpTbsgStatsEntry,
       "vrPpTbsgBadAbstractDiscards": vrPpTbsgBadAbstractDiscards,
       "vrPpTbsgTinygramFramesIn": vrPpTbsgTinygramFramesIn,
       "vrPpTbsgTinygramFramesOut": vrPpTbsgTinygramFramesOut,
       "vrPpTbsgInFilterDiscards": vrPpTbsgInFilterDiscards,
       "vrPpTbsgOutFilterDiscards": vrPpTbsgOutFilterDiscards,
       "vrPpSrcl": vrPpSrcl,
       "vrPpSrclRowStatusTable": vrPpSrclRowStatusTable,
       "vrPpSrclRowStatusEntry": vrPpSrclRowStatusEntry,
       "vrPpSrclRowStatus": vrPpSrclRowStatus,
       "vrPpSrclComponentName": vrPpSrclComponentName,
       "vrPpSrclStorageType": vrPpSrclStorageType,
       "vrPpSrclIndex": vrPpSrclIndex,
       "vrPpSrclNs": vrPpSrclNs,
       "vrPpSrclNsRowStatusTable": vrPpSrclNsRowStatusTable,
       "vrPpSrclNsRowStatusEntry": vrPpSrclNsRowStatusEntry,
       "vrPpSrclNsRowStatus": vrPpSrclNsRowStatus,
       "vrPpSrclNsComponentName": vrPpSrclNsComponentName,
       "vrPpSrclNsStorageType": vrPpSrclNsStorageType,
       "vrPpSrclNsIndex": vrPpSrclNsIndex,
       "vrPpSrclNsProvTable": vrPpSrclNsProvTable,
       "vrPpSrclNsProvEntry": vrPpSrclNsProvEntry,
       "vrPpSrclNsIncomingFilter": vrPpSrclNsIncomingFilter,
       "vrPpSrclNsOutgoingFilter": vrPpSrclNsOutgoingFilter,
       "vrPpSrclProvTable": vrPpSrclProvTable,
       "vrPpSrclProvEntry": vrPpSrclProvEntry,
       "vrPpSrclTranslateIpx": vrPpSrclTranslateIpx,
       "vrPpSrclFragmentIp": vrPpSrclFragmentIp,
       "vrPpSrclServiceClass": vrPpSrclServiceClass,
       "vrPpSrclConvertArpMacAddress": vrPpSrclConvertArpMacAddress,
       "vrPpSrclPortNum": vrPpSrclPortNum,
       "vrPpSrclOutboundFrameMediaType": vrPpSrclOutboundFrameMediaType,
       "vrPpSrclStpProvTable": vrPpSrclStpProvTable,
       "vrPpSrclStpProvEntry": vrPpSrclStpProvEntry,
       "vrPpSrclAdminStatus": vrPpSrclAdminStatus,
       "vrPpSrclPortStateStpControl": vrPpSrclPortStateStpControl,
       "vrPpSrclStpTypeProv": vrPpSrclStpTypeProv,
       "vrPpSrclPortPriority": vrPpSrclPortPriority,
       "vrPpSrclPathCost": vrPpSrclPathCost,
       "vrPpSrclPathCostMethod": vrPpSrclPathCostMethod,
       "vrPpSrclDIProvTable": vrPpSrclDIProvTable,
       "vrPpSrclDIProvEntry": vrPpSrclDIProvEntry,
       "vrPpSrclDomainNum": vrPpSrclDomainNum,
       "vrPpSrclPreserveDomain": vrPpSrclPreserveDomain,
       "vrPpSrclStateTable": vrPpSrclStateTable,
       "vrPpSrclStateEntry": vrPpSrclStateEntry,
       "vrPpSrclAdminState": vrPpSrclAdminState,
       "vrPpSrclOperationalState": vrPpSrclOperationalState,
       "vrPpSrclUsageState": vrPpSrclUsageState,
       "vrPpSrclOperStatusTable": vrPpSrclOperStatusTable,
       "vrPpSrclOperStatusEntry": vrPpSrclOperStatusEntry,
       "vrPpSrclSnmpOperStatus": vrPpSrclSnmpOperStatus,
       "vrPpSrclOperTable": vrPpSrclOperTable,
       "vrPpSrclOperEntry": vrPpSrclOperEntry,
       "vrPpSrclPortName": vrPpSrclPortName,
       "vrPpSrclUpTime": vrPpSrclUpTime,
       "vrPpSrclDownTime": vrPpSrclDownTime,
       "vrPpSrclBridgingMode": vrPpSrclBridgingMode,
       "vrPpSrclBridgePortConfig": vrPpSrclBridgePortConfig,
       "vrPpSrclBridgePortType": vrPpSrclBridgePortType,
       "vrPpSrclIfIndex": vrPpSrclIfIndex,
       "vrPpSrclDelayExceededDiscards": vrPpSrclDelayExceededDiscards,
       "vrPpSrclMtuExceededDiscards": vrPpSrclMtuExceededDiscards,
       "vrPpSrclStpOperTable": vrPpSrclStpOperTable,
       "vrPpSrclStpOperEntry": vrPpSrclStpOperEntry,
       "vrPpSrclStpPortState": vrPpSrclStpPortState,
       "vrPpSrclStpTypeOper": vrPpSrclStpTypeOper,
       "vrPpSrclDesignatedCost": vrPpSrclDesignatedCost,
       "vrPpSrclPathCostOper": vrPpSrclPathCostOper,
       "vrPpSrclDesignatedBridge": vrPpSrclDesignatedBridge,
       "vrPpSrclDesignatedPort": vrPpSrclDesignatedPort,
       "vrPpSrclForwardTransitions": vrPpSrclForwardTransitions,
       "vrPpSrclBlockingDiscards": vrPpSrclBlockingDiscards,
       "vrPpSrclDesignatedRoot": vrPpSrclDesignatedRoot,
       "vrPpSrclStatsTable": vrPpSrclStatsTable,
       "vrPpSrclStatsEntry": vrPpSrclStatsEntry,
       "vrPpSrclBadAbstractDiscards": vrPpSrclBadAbstractDiscards,
       "vrPpSrclTinygramFramesIn": vrPpSrclTinygramFramesIn,
       "vrPpSrclTinygramFramesOut": vrPpSrclTinygramFramesOut,
       "vrPpSrclInFilterDiscards": vrPpSrclInFilterDiscards,
       "vrPpSrclOutFilterDiscards": vrPpSrclOutFilterDiscards,
       "vrPpSrclSrProvTable": vrPpSrclSrProvTable,
       "vrPpSrclSrProvEntry": vrPpSrclSrProvEntry,
       "vrPpSrclHopCount": vrPpSrclHopCount,
       "vrPpSrclExploreFrameTreatment": vrPpSrclExploreFrameTreatment,
       "vrPpSrclLanId": vrPpSrclLanId,
       "vrPpSrclInternalLanId": vrPpSrclInternalLanId,
       "vrPpSrclBridgeNum": vrPpSrclBridgeNum,
       "vrPpSrclLargestFrame": vrPpSrclLargestFrame,
       "vrPpSrclSteSpanMode": vrPpSrclSteSpanMode,
       "vrPpSrclAreRdLimit": vrPpSrclAreRdLimit,
       "vrPpSrclSteRdLimit": vrPpSrclSteRdLimit,
       "vrPpSrclSrStatsTable": vrPpSrclSrStatsTable,
       "vrPpSrclSrStatsEntry": vrPpSrclSrStatsEntry,
       "vrPpSrclSpecInFrames": vrPpSrclSpecInFrames,
       "vrPpSrclSpecOutFrames": vrPpSrclSpecOutFrames,
       "vrPpSrclApeInFrames": vrPpSrclApeInFrames,
       "vrPpSrclApeOutFrames": vrPpSrclApeOutFrames,
       "vrPpSrclSteInFrames": vrPpSrclSteInFrames,
       "vrPpSrclSteOutFrames": vrPpSrclSteOutFrames,
       "vrPpSrclSegmentMismatchDiscards": vrPpSrclSegmentMismatchDiscards,
       "vrPpSrclDupSegmentDiscards": vrPpSrclDupSegmentDiscards,
       "vrPpSrclHopCountExceededDiscards": vrPpSrclHopCountExceededDiscards,
       "vrPpSrclDupLanIdOrTreeErrors": vrPpSrclDupLanIdOrTreeErrors,
       "vrPpSrclLanIdMismatches": vrPpSrclLanIdMismatches,
       "vrPpSrclStaticDiscards": vrPpSrclStaticDiscards,
       "vrPpSrclDynamicDiscards": vrPpSrclDynamicDiscards,
       "vrBr": vrBr,
       "vrBrRowStatusTable": vrBrRowStatusTable,
       "vrBrRowStatusEntry": vrBrRowStatusEntry,
       "vrBrRowStatus": vrBrRowStatus,
       "vrBrComponentName": vrBrComponentName,
       "vrBrStorageType": vrBrStorageType,
       "vrBrIndex": vrBrIndex,
       "vrBrPte": vrBrPte,
       "vrBrPteRowStatusTable": vrBrPteRowStatusTable,
       "vrBrPteRowStatusEntry": vrBrPteRowStatusEntry,
       "vrBrPteRowStatus": vrBrPteRowStatus,
       "vrBrPteComponentName": vrBrPteComponentName,
       "vrBrPteStorageType": vrBrPteStorageType,
       "vrBrPteDomainNumIndex": vrBrPteDomainNumIndex,
       "vrBrPtePortNameIndex": vrBrPtePortNameIndex,
       "vrBrPteModeIndex": vrBrPteModeIndex,
       "vrBrPteOperTable": vrBrPteOperTable,
       "vrBrPteOperEntry": vrBrPteOperEntry,
       "vrBrPteMacType": vrBrPteMacType,
       "vrBrPteStpState": vrBrPteStpState,
       "vrBrPteStpType": vrBrPteStpType,
       "vrBrPteFilterPoints": vrBrPteFilterPoints,
       "vrBrPtePortPointsTo": vrBrPtePortPointsTo,
       "vrBrPteSpOperTable": vrBrPteSpOperTable,
       "vrBrPteSpOperEntry": vrBrPteSpOperEntry,
       "vrBrPteLanId": vrBrPteLanId,
       "vrBrPteInternalLanId": vrBrPteInternalLanId,
       "vrBrPteBridgeNum": vrBrPteBridgeNum,
       "vrBrNs": vrBrNs,
       "vrBrNsRowStatusTable": vrBrNsRowStatusTable,
       "vrBrNsRowStatusEntry": vrBrNsRowStatusEntry,
       "vrBrNsRowStatus": vrBrNsRowStatus,
       "vrBrNsComponentName": vrBrNsComponentName,
       "vrBrNsStorageType": vrBrNsStorageType,
       "vrBrNsIndex": vrBrNsIndex,
       "vrBrNsAte": vrBrNsAte,
       "vrBrNsAteRowStatusTable": vrBrNsAteRowStatusTable,
       "vrBrNsAteRowStatusEntry": vrBrNsAteRowStatusEntry,
       "vrBrNsAteRowStatus": vrBrNsAteRowStatus,
       "vrBrNsAteComponentName": vrBrNsAteComponentName,
       "vrBrNsAteStorageType": vrBrNsAteStorageType,
       "vrBrNsAteEntryNumberIndex": vrBrNsAteEntryNumberIndex,
       "vrBrNsAteProvTable": vrBrNsAteProvTable,
       "vrBrNsAteProvEntry": vrBrNsAteProvEntry,
       "vrBrNsAteDomainNum": vrBrNsAteDomainNum,
       "vrBrNsAteFirstMacAddress": vrBrNsAteFirstMacAddress,
       "vrBrNsAteFirstMacAddressMask": vrBrNsAteFirstMacAddressMask,
       "vrBrNsAteSecondMacAddress": vrBrNsAteSecondMacAddress,
       "vrBrNsAteSecondMacAddressMask": vrBrNsAteSecondMacAddressMask,
       "vrBrNsAteDirection": vrBrNsAteDirection,
       "vrBrNsAteFilterName": vrBrNsAteFilterName,
       "vrBrNsProvTable": vrBrNsProvTable,
       "vrBrNsProvEntry": vrBrNsProvEntry,
       "vrBrNsFirstFilter": vrBrNsFirstFilter,
       "vrBrNsLastFilter": vrBrNsLastFilter,
       "vrBrTb": vrBrTb,
       "vrBrTbRowStatusTable": vrBrTbRowStatusTable,
       "vrBrTbRowStatusEntry": vrBrTbRowStatusEntry,
       "vrBrTbRowStatus": vrBrTbRowStatus,
       "vrBrTbComponentName": vrBrTbComponentName,
       "vrBrTbStorageType": vrBrTbStorageType,
       "vrBrTbIndex": vrBrTbIndex,
       "vrBrTbStp": vrBrTbStp,
       "vrBrTbStpRowStatusTable": vrBrTbStpRowStatusTable,
       "vrBrTbStpRowStatusEntry": vrBrTbStpRowStatusEntry,
       "vrBrTbStpRowStatus": vrBrTbStpRowStatus,
       "vrBrTbStpComponentName": vrBrTbStpComponentName,
       "vrBrTbStpStorageType": vrBrTbStpStorageType,
       "vrBrTbStpIndex": vrBrTbStpIndex,
       "vrBrTbStpProvTable": vrBrTbStpProvTable,
       "vrBrTbStpProvEntry": vrBrTbStpProvEntry,
       "vrBrTbStpStpMode": vrBrTbStpStpMode,
       "vrBrTbStpProtocolSpec": vrBrTbStpProtocolSpec,
       "vrBrTbStpPriority": vrBrTbStpPriority,
       "vrBrTbStpBridgeMaxAge": vrBrTbStpBridgeMaxAge,
       "vrBrTbStpBridgeHelloTime": vrBrTbStpBridgeHelloTime,
       "vrBrTbStpBridgeForwardDelay": vrBrTbStpBridgeForwardDelay,
       "vrBrTbStpOperTable": vrBrTbStpOperTable,
       "vrBrTbStpOperEntry": vrBrTbStpOperEntry,
       "vrBrTbStpBridgeId": vrBrTbStpBridgeId,
       "vrBrTbStpRootPortName": vrBrTbStpRootPortName,
       "vrBrTbStpTimeSinceTopologyChange": vrBrTbStpTimeSinceTopologyChange,
       "vrBrTbStpTopologyChangeDetect": vrBrTbStpTopologyChangeDetect,
       "vrBrTbStpTopologyChanges": vrBrTbStpTopologyChanges,
       "vrBrTbStpDesignatedRoot": vrBrTbStpDesignatedRoot,
       "vrBrTbStpRootCost": vrBrTbStpRootCost,
       "vrBrTbStpMaxAge": vrBrTbStpMaxAge,
       "vrBrTbStpAgingTimeOper": vrBrTbStpAgingTimeOper,
       "vrBrTbStpHelloTime": vrBrTbStpHelloTime,
       "vrBrTbStpHoldTime": vrBrTbStpHoldTime,
       "vrBrTbStpFwdDelay": vrBrTbStpFwdDelay,
       "vrBrTbSte": vrBrTbSte,
       "vrBrTbSteRowStatusTable": vrBrTbSteRowStatusTable,
       "vrBrTbSteRowStatusEntry": vrBrTbSteRowStatusEntry,
       "vrBrTbSteRowStatus": vrBrTbSteRowStatus,
       "vrBrTbSteComponentName": vrBrTbSteComponentName,
       "vrBrTbSteStorageType": vrBrTbSteStorageType,
       "vrBrTbSteAddressIndex": vrBrTbSteAddressIndex,
       "vrBrTbSteReceivePortIndex": vrBrTbSteReceivePortIndex,
       "vrBrTbSteProvTable": vrBrTbSteProvTable,
       "vrBrTbSteProvEntry": vrBrTbSteProvEntry,
       "vrBrTbSteStatus": vrBrTbSteStatus,
       "vrBrTbSteAtgtTable": vrBrTbSteAtgtTable,
       "vrBrTbSteAtgtEntry": vrBrTbSteAtgtEntry,
       "vrBrTbSteAtgtValue": vrBrTbSteAtgtValue,
       "vrBrTbSteAtgtRowStatus": vrBrTbSteAtgtRowStatus,
       "vrBrTbFte": vrBrTbFte,
       "vrBrTbFteRowStatusTable": vrBrTbFteRowStatusTable,
       "vrBrTbFteRowStatusEntry": vrBrTbFteRowStatusEntry,
       "vrBrTbFteRowStatus": vrBrTbFteRowStatus,
       "vrBrTbFteComponentName": vrBrTbFteComponentName,
       "vrBrTbFteStorageType": vrBrTbFteStorageType,
       "vrBrTbFteAddressIndex": vrBrTbFteAddressIndex,
       "vrBrTbFteDomainNumIndex": vrBrTbFteDomainNumIndex,
       "vrBrTbFteOperTable": vrBrTbFteOperTable,
       "vrBrTbFteOperEntry": vrBrTbFteOperEntry,
       "vrBrTbFtePort": vrBrTbFtePort,
       "vrBrTbFteAgeOfEntry": vrBrTbFteAgeOfEntry,
       "vrBrTbFtePeerAddressInfo": vrBrTbFtePeerAddressInfo,
       "vrBrTbFteStatus": vrBrTbFteStatus,
       "vrBrTbNcFte": vrBrTbNcFte,
       "vrBrTbNcFteRowStatusTable": vrBrTbNcFteRowStatusTable,
       "vrBrTbNcFteRowStatusEntry": vrBrTbNcFteRowStatusEntry,
       "vrBrTbNcFteRowStatus": vrBrTbNcFteRowStatus,
       "vrBrTbNcFteComponentName": vrBrTbNcFteComponentName,
       "vrBrTbNcFteStorageType": vrBrTbNcFteStorageType,
       "vrBrTbNcFteAddressIndex": vrBrTbNcFteAddressIndex,
       "vrBrTbNcFteDomainNumIndex": vrBrTbNcFteDomainNumIndex,
       "vrBrTbNcFteOperTable": vrBrTbNcFteOperTable,
       "vrBrTbNcFteOperEntry": vrBrTbNcFteOperEntry,
       "vrBrTbNcFtePort": vrBrTbNcFtePort,
       "vrBrTbNcFteAgeOfEntry": vrBrTbNcFteAgeOfEntry,
       "vrBrTbNcFtePeerAddressInfo": vrBrTbNcFtePeerAddressInfo,
       "vrBrTbNcFteStatus": vrBrTbNcFteStatus,
       "vrBrTbProvTable": vrBrTbProvTable,
       "vrBrTbProvEntry": vrBrTbProvEntry,
       "vrBrTbFwdTableNumEntries": vrBrTbFwdTableNumEntries,
       "vrBrTbAgingTime": vrBrTbAgingTime,
       "vrBrTbStatsTable": vrBrTbStatsTable,
       "vrBrTbStatsEntry": vrBrTbStatsEntry,
       "vrBrTbLearnedEntryDiscards": vrBrTbLearnedEntryDiscards,
       "vrBrTbTotalForwardingTableEntries": vrBrTbTotalForwardingTableEntries,
       "vrBrTbNumFtEntriesFree": vrBrTbNumFtEntriesFree,
       "vrBrTbNumFtEntriesDenied": vrBrTbNumFtEntriesDenied,
       "vrBrSrb": vrBrSrb,
       "vrBrSrbRowStatusTable": vrBrSrbRowStatusTable,
       "vrBrSrbRowStatusEntry": vrBrSrbRowStatusEntry,
       "vrBrSrbRowStatus": vrBrSrbRowStatus,
       "vrBrSrbComponentName": vrBrSrbComponentName,
       "vrBrSrbStorageType": vrBrSrbStorageType,
       "vrBrSrbIndex": vrBrSrbIndex,
       "vrBrSrbStp": vrBrSrbStp,
       "vrBrSrbStpRowStatusTable": vrBrSrbStpRowStatusTable,
       "vrBrSrbStpRowStatusEntry": vrBrSrbStpRowStatusEntry,
       "vrBrSrbStpRowStatus": vrBrSrbStpRowStatus,
       "vrBrSrbStpComponentName": vrBrSrbStpComponentName,
       "vrBrSrbStpStorageType": vrBrSrbStpStorageType,
       "vrBrSrbStpIndex": vrBrSrbStpIndex,
       "vrBrSrbStpProvTable": vrBrSrbStpProvTable,
       "vrBrSrbStpProvEntry": vrBrSrbStpProvEntry,
       "vrBrSrbStpStpMode": vrBrSrbStpStpMode,
       "vrBrSrbStpProtocolSpec": vrBrSrbStpProtocolSpec,
       "vrBrSrbStpPriority": vrBrSrbStpPriority,
       "vrBrSrbStpBridgeMaxAge": vrBrSrbStpBridgeMaxAge,
       "vrBrSrbStpBridgeHelloTime": vrBrSrbStpBridgeHelloTime,
       "vrBrSrbStpBridgeForwardDelay": vrBrSrbStpBridgeForwardDelay,
       "vrBrSrbStpOperTable": vrBrSrbStpOperTable,
       "vrBrSrbStpOperEntry": vrBrSrbStpOperEntry,
       "vrBrSrbStpBridgeId": vrBrSrbStpBridgeId,
       "vrBrSrbStpRootPortName": vrBrSrbStpRootPortName,
       "vrBrSrbStpTimeSinceTopologyChange": vrBrSrbStpTimeSinceTopologyChange,
       "vrBrSrbStpTopologyChangeDetect": vrBrSrbStpTopologyChangeDetect,
       "vrBrSrbStpTopologyChanges": vrBrSrbStpTopologyChanges,
       "vrBrSrbStpDesignatedRoot": vrBrSrbStpDesignatedRoot,
       "vrBrSrbStpRootCost": vrBrSrbStpRootCost,
       "vrBrSrbStpMaxAge": vrBrSrbStpMaxAge,
       "vrBrSrbStpAgingTimeOper": vrBrSrbStpAgingTimeOper,
       "vrBrSrbStpHelloTime": vrBrSrbStpHelloTime,
       "vrBrSrbStpHoldTime": vrBrSrbStpHoldTime,
       "vrBrSrbStpFwdDelay": vrBrSrbStpFwdDelay,
       "vrBrSrbLte": vrBrSrbLte,
       "vrBrSrbLteRowStatusTable": vrBrSrbLteRowStatusTable,
       "vrBrSrbLteRowStatusEntry": vrBrSrbLteRowStatusEntry,
       "vrBrSrbLteRowStatus": vrBrSrbLteRowStatus,
       "vrBrSrbLteComponentName": vrBrSrbLteComponentName,
       "vrBrSrbLteStorageType": vrBrSrbLteStorageType,
       "vrBrSrbLteLanIdIndex": vrBrSrbLteLanIdIndex,
       "vrBrSrbLteDomainNumIndex": vrBrSrbLteDomainNumIndex,
       "vrBrSrbLteOperTable": vrBrSrbLteOperTable,
       "vrBrSrbLteOperEntry": vrBrSrbLteOperEntry,
       "vrBrSrbLtePortName": vrBrSrbLtePortName,
       "vrBrSrbLteAgeOfEntry": vrBrSrbLteAgeOfEntry,
       "vrBrSrbLtePeerMACAddress": vrBrSrbLtePeerMACAddress,
       "vrBrSrbLteTypeOfEntry": vrBrSrbLteTypeOfEntry,
       "vrBrSrbProvTable": vrBrSrbProvTable,
       "vrBrSrbProvEntry": vrBrSrbProvEntry,
       "vrBrSrbLanIdTableNumEntries": vrBrSrbLanIdTableNumEntries,
       "vrBrSrbAgingTime": vrBrSrbAgingTime,
       "vrBrSrbBridgeLfMode": vrBrSrbBridgeLfMode,
       "vrBrSrbStatsTable": vrBrSrbStatsTable,
       "vrBrSrbStatsEntry": vrBrSrbStatsEntry,
       "vrBrSrbTotalLanIdTableEntries": vrBrSrbTotalLanIdTableEntries,
       "vrBrSrbNumLanIdtEntriesFree": vrBrSrbNumLanIdtEntriesFree,
       "vrBrSrbNumLanIdtEntriesDenied": vrBrSrbNumLanIdtEntriesDenied,
       "vrBrAdminControlTable": vrBrAdminControlTable,
       "vrBrAdminControlEntry": vrBrAdminControlEntry,
       "vrBrAdminStatus": vrBrAdminStatus,
       "vrBrStateTable": vrBrStateTable,
       "vrBrStateEntry": vrBrStateEntry,
       "vrBrAdminState": vrBrAdminState,
       "vrBrOperationalState": vrBrOperationalState,
       "vrBrUsageState": vrBrUsageState,
       "vrBrOperStatusTable": vrBrOperStatusTable,
       "vrBrOperStatusEntry": vrBrOperStatusEntry,
       "vrBrSnmpOperStatus": vrBrSnmpOperStatus,
       "vrBrOperTable": vrBrOperTable,
       "vrBrOperEntry": vrBrOperEntry,
       "vrBrBridgeAddress": vrBrBridgeAddress,
       "vrBrNumPorts": vrBrNumPorts,
       "vrBrType": vrBrType,
       "cB": cB,
       "cBRowStatusTable": cBRowStatusTable,
       "cBRowStatusEntry": cBRowStatusEntry,
       "cBRowStatus": cBRowStatus,
       "cBComponentName": cBComponentName,
       "cBStorageType": cBStorageType,
       "cBIndex": cBIndex,
       "cBAdminControlTable": cBAdminControlTable,
       "cBAdminControlEntry": cBAdminControlEntry,
       "cBSnmpAdminStatus": cBSnmpAdminStatus,
       "cBIfEntryTable": cBIfEntryTable,
       "cBIfEntryEntry": cBIfEntryEntry,
       "cBIfAdminStatus": cBIfAdminStatus,
       "cBIfIndex": cBIfIndex,
       "cBMpTable": cBMpTable,
       "cBMpEntry": cBMpEntry,
       "cBLinkToProtocolPort": cBLinkToProtocolPort,
       "cBOperTable": cBOperTable,
       "cBOperEntry": cBOperEntry,
       "cBMacAddress": cBMacAddress,
       "cBStateTable": cBStateTable,
       "cBStateEntry": cBStateEntry,
       "cBAdminState": cBAdminState,
       "cBOperationalState": cBOperationalState,
       "cBUsageState": cBUsageState,
       "cBOperStatusTable": cBOperStatusTable,
       "cBOperStatusEntry": cBOperStatusEntry,
       "cBSnmpOperStatus": cBSnmpOperStatus,
       "pB": pB,
       "pBRowStatusTable": pBRowStatusTable,
       "pBRowStatusEntry": pBRowStatusEntry,
       "pBRowStatus": pBRowStatus,
       "pBComponentName": pBComponentName,
       "pBStorageType": pBStorageType,
       "pBIndex": pBIndex,
       "pBAdminControlTable": pBAdminControlTable,
       "pBAdminControlEntry": pBAdminControlEntry,
       "pBSnmpAdminStatus": pBSnmpAdminStatus,
       "pBIfEntryTable": pBIfEntryTable,
       "pBIfEntryEntry": pBIfEntryEntry,
       "pBIfAdminStatus": pBIfAdminStatus,
       "pBIfIndex": pBIfIndex,
       "pBMpTable": pBMpTable,
       "pBMpEntry": pBMpEntry,
       "pBLinkToProtocolPort": pBLinkToProtocolPort,
       "pBOperTable": pBOperTable,
       "pBOperEntry": pBOperEntry,
       "pBMacAddress": pBMacAddress,
       "pBStateTable": pBStateTable,
       "pBStateEntry": pBStateEntry,
       "pBAdminState": pBAdminState,
       "pBOperationalState": pBOperationalState,
       "pBUsageState": pBUsageState,
       "pBOperStatusTable": pBOperStatusTable,
       "pBOperStatusEntry": pBOperStatusEntry,
       "pBSnmpOperStatus": pBSnmpOperStatus,
       "bridgeMIB": bridgeMIB,
       "bridgeGroup": bridgeGroup,
       "bridgeGroupBE": bridgeGroupBE,
       "bridgeGroupBE01": bridgeGroupBE01,
       "bridgeGroupBE01A": bridgeGroupBE01A,
       "bridgeCapabilities": bridgeCapabilities,
       "bridgeCapabilitiesBE": bridgeCapabilitiesBE,
       "bridgeCapabilitiesBE01": bridgeCapabilitiesBE01,
       "bridgeCapabilitiesBE01A": bridgeCapabilitiesBE01A}
)
