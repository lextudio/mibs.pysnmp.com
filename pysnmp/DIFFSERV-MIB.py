# SNMP MIB module (DIFFSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DIFFSERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:21 2024
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

(Dscp,
 DscpOrAny) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp",
    "DscpOrAny")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(BurstSize,) = mibBuilder.importSymbols(
    "INTEGRATED-SERVICES-MIB",
    "BurstSize")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(AutonomousType,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

diffServMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 97)
)
diffServMib.setRevisions(
        ("2002-02-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IndexInteger(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IndexIntegerNextFree(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class IfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DiffServMIBObjects_ObjectIdentity = ObjectIdentity
diffServMIBObjects = _DiffServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1)
)
_DiffServDataPath_ObjectIdentity = ObjectIdentity
diffServDataPath = _DiffServDataPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 1)
)
_DiffServDataPathTable_Object = MibTable
diffServDataPathTable = _DiffServDataPathTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 1, 1)
)
if mibBuilder.loadTexts:
    diffServDataPathTable.setStatus("current")
_DiffServDataPathEntry_Object = MibTableRow
diffServDataPathEntry = _DiffServDataPathEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 1, 1, 1)
)
diffServDataPathEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFFSERV-MIB", "diffServDataPathIfDirection"),
)
if mibBuilder.loadTexts:
    diffServDataPathEntry.setStatus("current")
_DiffServDataPathIfDirection_Type = IfDirection
_DiffServDataPathIfDirection_Object = MibTableColumn
diffServDataPathIfDirection = _DiffServDataPathIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 1, 1, 1, 1),
    _DiffServDataPathIfDirection_Type()
)
diffServDataPathIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServDataPathIfDirection.setStatus("current")
_DiffServDataPathStart_Type = RowPointer
_DiffServDataPathStart_Object = MibTableColumn
diffServDataPathStart = _DiffServDataPathStart_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 1, 1, 1, 2),
    _DiffServDataPathStart_Type()
)
diffServDataPathStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServDataPathStart.setStatus("current")


class _DiffServDataPathStorage_Type(StorageType):
    """Custom type diffServDataPathStorage based on StorageType"""


_DiffServDataPathStorage_Object = MibTableColumn
diffServDataPathStorage = _DiffServDataPathStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 1, 1, 1, 3),
    _DiffServDataPathStorage_Type()
)
diffServDataPathStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServDataPathStorage.setStatus("current")
_DiffServDataPathStatus_Type = RowStatus
_DiffServDataPathStatus_Object = MibTableColumn
diffServDataPathStatus = _DiffServDataPathStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 1, 1, 1, 4),
    _DiffServDataPathStatus_Type()
)
diffServDataPathStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServDataPathStatus.setStatus("current")
_DiffServClassifier_ObjectIdentity = ObjectIdentity
diffServClassifier = _DiffServClassifier_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 2)
)
_DiffServClfrNextFree_Type = IndexIntegerNextFree
_DiffServClfrNextFree_Object = MibScalar
diffServClfrNextFree = _DiffServClfrNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 1),
    _DiffServClfrNextFree_Type()
)
diffServClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClfrNextFree.setStatus("current")
_DiffServClfrTable_Object = MibTable
diffServClfrTable = _DiffServClfrTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 2)
)
if mibBuilder.loadTexts:
    diffServClfrTable.setStatus("current")
_DiffServClfrEntry_Object = MibTableRow
diffServClfrEntry = _DiffServClfrEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 2, 1)
)
diffServClfrEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServClfrId"),
)
if mibBuilder.loadTexts:
    diffServClfrEntry.setStatus("current")
_DiffServClfrId_Type = IndexInteger
_DiffServClfrId_Object = MibTableColumn
diffServClfrId = _DiffServClfrId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 2, 1, 1),
    _DiffServClfrId_Type()
)
diffServClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClfrId.setStatus("current")


class _DiffServClfrStorage_Type(StorageType):
    """Custom type diffServClfrStorage based on StorageType"""


_DiffServClfrStorage_Object = MibTableColumn
diffServClfrStorage = _DiffServClfrStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 2, 1, 2),
    _DiffServClfrStorage_Type()
)
diffServClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrStorage.setStatus("current")
_DiffServClfrStatus_Type = RowStatus
_DiffServClfrStatus_Object = MibTableColumn
diffServClfrStatus = _DiffServClfrStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 2, 1, 3),
    _DiffServClfrStatus_Type()
)
diffServClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrStatus.setStatus("current")
_DiffServClfrElementNextFree_Type = IndexIntegerNextFree
_DiffServClfrElementNextFree_Object = MibScalar
diffServClfrElementNextFree = _DiffServClfrElementNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 3),
    _DiffServClfrElementNextFree_Type()
)
diffServClfrElementNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClfrElementNextFree.setStatus("current")
_DiffServClfrElementTable_Object = MibTable
diffServClfrElementTable = _DiffServClfrElementTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4)
)
if mibBuilder.loadTexts:
    diffServClfrElementTable.setStatus("current")
_DiffServClfrElementEntry_Object = MibTableRow
diffServClfrElementEntry = _DiffServClfrElementEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1)
)
diffServClfrElementEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServClfrId"),
    (0, "DIFFSERV-MIB", "diffServClfrElementId"),
)
if mibBuilder.loadTexts:
    diffServClfrElementEntry.setStatus("current")
_DiffServClfrElementId_Type = IndexInteger
_DiffServClfrElementId_Object = MibTableColumn
diffServClfrElementId = _DiffServClfrElementId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1, 1),
    _DiffServClfrElementId_Type()
)
diffServClfrElementId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClfrElementId.setStatus("current")


class _DiffServClfrElementPrecedence_Type(Unsigned32):
    """Custom type diffServClfrElementPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServClfrElementPrecedence_Type.__name__ = "Unsigned32"
_DiffServClfrElementPrecedence_Object = MibTableColumn
diffServClfrElementPrecedence = _DiffServClfrElementPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1, 2),
    _DiffServClfrElementPrecedence_Type()
)
diffServClfrElementPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrElementPrecedence.setStatus("current")
_DiffServClfrElementNext_Type = RowPointer
_DiffServClfrElementNext_Object = MibTableColumn
diffServClfrElementNext = _DiffServClfrElementNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1, 3),
    _DiffServClfrElementNext_Type()
)
diffServClfrElementNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrElementNext.setStatus("current")
_DiffServClfrElementSpecific_Type = RowPointer
_DiffServClfrElementSpecific_Object = MibTableColumn
diffServClfrElementSpecific = _DiffServClfrElementSpecific_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1, 4),
    _DiffServClfrElementSpecific_Type()
)
diffServClfrElementSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrElementSpecific.setStatus("current")


class _DiffServClfrElementStorage_Type(StorageType):
    """Custom type diffServClfrElementStorage based on StorageType"""


_DiffServClfrElementStorage_Object = MibTableColumn
diffServClfrElementStorage = _DiffServClfrElementStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1, 5),
    _DiffServClfrElementStorage_Type()
)
diffServClfrElementStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrElementStorage.setStatus("current")
_DiffServClfrElementStatus_Type = RowStatus
_DiffServClfrElementStatus_Object = MibTableColumn
diffServClfrElementStatus = _DiffServClfrElementStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 4, 1, 6),
    _DiffServClfrElementStatus_Type()
)
diffServClfrElementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClfrElementStatus.setStatus("current")
_DiffServMultiFieldClfrNextFree_Type = IndexIntegerNextFree
_DiffServMultiFieldClfrNextFree_Object = MibScalar
diffServMultiFieldClfrNextFree = _DiffServMultiFieldClfrNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 5),
    _DiffServMultiFieldClfrNextFree_Type()
)
diffServMultiFieldClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrNextFree.setStatus("current")
_DiffServMultiFieldClfrTable_Object = MibTable
diffServMultiFieldClfrTable = _DiffServMultiFieldClfrTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6)
)
if mibBuilder.loadTexts:
    diffServMultiFieldClfrTable.setStatus("current")
_DiffServMultiFieldClfrEntry_Object = MibTableRow
diffServMultiFieldClfrEntry = _DiffServMultiFieldClfrEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1)
)
diffServMultiFieldClfrEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServMultiFieldClfrId"),
)
if mibBuilder.loadTexts:
    diffServMultiFieldClfrEntry.setStatus("current")
_DiffServMultiFieldClfrId_Type = IndexInteger
_DiffServMultiFieldClfrId_Object = MibTableColumn
diffServMultiFieldClfrId = _DiffServMultiFieldClfrId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 1),
    _DiffServMultiFieldClfrId_Type()
)
diffServMultiFieldClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrId.setStatus("current")
_DiffServMultiFieldClfrAddrType_Type = InetAddressType
_DiffServMultiFieldClfrAddrType_Object = MibTableColumn
diffServMultiFieldClfrAddrType = _DiffServMultiFieldClfrAddrType_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 2),
    _DiffServMultiFieldClfrAddrType_Type()
)
diffServMultiFieldClfrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrAddrType.setStatus("current")
_DiffServMultiFieldClfrDstAddr_Type = InetAddress
_DiffServMultiFieldClfrDstAddr_Object = MibTableColumn
diffServMultiFieldClfrDstAddr = _DiffServMultiFieldClfrDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 3),
    _DiffServMultiFieldClfrDstAddr_Type()
)
diffServMultiFieldClfrDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrDstAddr.setStatus("current")


class _DiffServMultiFieldClfrDstPrefixLength_Type(InetAddressPrefixLength):
    """Custom type diffServMultiFieldClfrDstPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_DiffServMultiFieldClfrDstPrefixLength_Object = MibTableColumn
diffServMultiFieldClfrDstPrefixLength = _DiffServMultiFieldClfrDstPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 4),
    _DiffServMultiFieldClfrDstPrefixLength_Type()
)
diffServMultiFieldClfrDstPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrDstPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrDstPrefixLength.setUnits("bits")
_DiffServMultiFieldClfrSrcAddr_Type = InetAddress
_DiffServMultiFieldClfrSrcAddr_Object = MibTableColumn
diffServMultiFieldClfrSrcAddr = _DiffServMultiFieldClfrSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 5),
    _DiffServMultiFieldClfrSrcAddr_Type()
)
diffServMultiFieldClfrSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrSrcAddr.setStatus("current")


class _DiffServMultiFieldClfrSrcPrefixLength_Type(InetAddressPrefixLength):
    """Custom type diffServMultiFieldClfrSrcPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_DiffServMultiFieldClfrSrcPrefixLength_Object = MibTableColumn
diffServMultiFieldClfrSrcPrefixLength = _DiffServMultiFieldClfrSrcPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 6),
    _DiffServMultiFieldClfrSrcPrefixLength_Type()
)
diffServMultiFieldClfrSrcPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrSrcPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrSrcPrefixLength.setUnits("bits")


class _DiffServMultiFieldClfrDscp_Type(DscpOrAny):
    """Custom type diffServMultiFieldClfrDscp based on DscpOrAny"""
    defaultValue = -1


_DiffServMultiFieldClfrDscp_Object = MibTableColumn
diffServMultiFieldClfrDscp = _DiffServMultiFieldClfrDscp_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 7),
    _DiffServMultiFieldClfrDscp_Type()
)
diffServMultiFieldClfrDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrDscp.setStatus("current")


class _DiffServMultiFieldClfrFlowId_Type(Unsigned32):
    """Custom type diffServMultiFieldClfrFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_DiffServMultiFieldClfrFlowId_Type.__name__ = "Unsigned32"
_DiffServMultiFieldClfrFlowId_Object = MibTableColumn
diffServMultiFieldClfrFlowId = _DiffServMultiFieldClfrFlowId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 8),
    _DiffServMultiFieldClfrFlowId_Type()
)
diffServMultiFieldClfrFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrFlowId.setStatus("current")


class _DiffServMultiFieldClfrProtocol_Type(Unsigned32):
    """Custom type diffServMultiFieldClfrProtocol based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiffServMultiFieldClfrProtocol_Type.__name__ = "Unsigned32"
_DiffServMultiFieldClfrProtocol_Object = MibTableColumn
diffServMultiFieldClfrProtocol = _DiffServMultiFieldClfrProtocol_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 9),
    _DiffServMultiFieldClfrProtocol_Type()
)
diffServMultiFieldClfrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrProtocol.setStatus("current")


class _DiffServMultiFieldClfrDstL4PortMin_Type(InetPortNumber):
    """Custom type diffServMultiFieldClfrDstL4PortMin based on InetPortNumber"""
    defaultValue = 0


_DiffServMultiFieldClfrDstL4PortMin_Object = MibTableColumn
diffServMultiFieldClfrDstL4PortMin = _DiffServMultiFieldClfrDstL4PortMin_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 10),
    _DiffServMultiFieldClfrDstL4PortMin_Type()
)
diffServMultiFieldClfrDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrDstL4PortMin.setStatus("current")


class _DiffServMultiFieldClfrDstL4PortMax_Type(InetPortNumber):
    """Custom type diffServMultiFieldClfrDstL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_DiffServMultiFieldClfrDstL4PortMax_Object = MibTableColumn
diffServMultiFieldClfrDstL4PortMax = _DiffServMultiFieldClfrDstL4PortMax_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 11),
    _DiffServMultiFieldClfrDstL4PortMax_Type()
)
diffServMultiFieldClfrDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrDstL4PortMax.setStatus("current")


class _DiffServMultiFieldClfrSrcL4PortMin_Type(InetPortNumber):
    """Custom type diffServMultiFieldClfrSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_DiffServMultiFieldClfrSrcL4PortMin_Object = MibTableColumn
diffServMultiFieldClfrSrcL4PortMin = _DiffServMultiFieldClfrSrcL4PortMin_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 12),
    _DiffServMultiFieldClfrSrcL4PortMin_Type()
)
diffServMultiFieldClfrSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrSrcL4PortMin.setStatus("current")


class _DiffServMultiFieldClfrSrcL4PortMax_Type(InetPortNumber):
    """Custom type diffServMultiFieldClfrSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_DiffServMultiFieldClfrSrcL4PortMax_Object = MibTableColumn
diffServMultiFieldClfrSrcL4PortMax = _DiffServMultiFieldClfrSrcL4PortMax_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 13),
    _DiffServMultiFieldClfrSrcL4PortMax_Type()
)
diffServMultiFieldClfrSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrSrcL4PortMax.setStatus("current")


class _DiffServMultiFieldClfrStorage_Type(StorageType):
    """Custom type diffServMultiFieldClfrStorage based on StorageType"""


_DiffServMultiFieldClfrStorage_Object = MibTableColumn
diffServMultiFieldClfrStorage = _DiffServMultiFieldClfrStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 14),
    _DiffServMultiFieldClfrStorage_Type()
)
diffServMultiFieldClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrStorage.setStatus("current")
_DiffServMultiFieldClfrStatus_Type = RowStatus
_DiffServMultiFieldClfrStatus_Object = MibTableColumn
diffServMultiFieldClfrStatus = _DiffServMultiFieldClfrStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 2, 6, 1, 15),
    _DiffServMultiFieldClfrStatus_Type()
)
diffServMultiFieldClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMultiFieldClfrStatus.setStatus("current")
_DiffServMeter_ObjectIdentity = ObjectIdentity
diffServMeter = _DiffServMeter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 3)
)
_DiffServMeterNextFree_Type = IndexIntegerNextFree
_DiffServMeterNextFree_Object = MibScalar
diffServMeterNextFree = _DiffServMeterNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 1),
    _DiffServMeterNextFree_Type()
)
diffServMeterNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServMeterNextFree.setStatus("current")
_DiffServMeterTable_Object = MibTable
diffServMeterTable = _DiffServMeterTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2)
)
if mibBuilder.loadTexts:
    diffServMeterTable.setStatus("current")
_DiffServMeterEntry_Object = MibTableRow
diffServMeterEntry = _DiffServMeterEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1)
)
diffServMeterEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServMeterId"),
)
if mibBuilder.loadTexts:
    diffServMeterEntry.setStatus("current")
_DiffServMeterId_Type = IndexInteger
_DiffServMeterId_Object = MibTableColumn
diffServMeterId = _DiffServMeterId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1, 1),
    _DiffServMeterId_Type()
)
diffServMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMeterId.setStatus("current")


class _DiffServMeterSucceedNext_Type(RowPointer):
    """Custom type diffServMeterSucceedNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServMeterSucceedNext_Object = MibTableColumn
diffServMeterSucceedNext = _DiffServMeterSucceedNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1, 2),
    _DiffServMeterSucceedNext_Type()
)
diffServMeterSucceedNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterSucceedNext.setStatus("current")


class _DiffServMeterFailNext_Type(RowPointer):
    """Custom type diffServMeterFailNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServMeterFailNext_Object = MibTableColumn
diffServMeterFailNext = _DiffServMeterFailNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1, 3),
    _DiffServMeterFailNext_Type()
)
diffServMeterFailNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterFailNext.setStatus("current")
_DiffServMeterSpecific_Type = RowPointer
_DiffServMeterSpecific_Object = MibTableColumn
diffServMeterSpecific = _DiffServMeterSpecific_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1, 4),
    _DiffServMeterSpecific_Type()
)
diffServMeterSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterSpecific.setStatus("current")


class _DiffServMeterStorage_Type(StorageType):
    """Custom type diffServMeterStorage based on StorageType"""


_DiffServMeterStorage_Object = MibTableColumn
diffServMeterStorage = _DiffServMeterStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1, 5),
    _DiffServMeterStorage_Type()
)
diffServMeterStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStorage.setStatus("current")
_DiffServMeterStatus_Type = RowStatus
_DiffServMeterStatus_Object = MibTableColumn
diffServMeterStatus = _DiffServMeterStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 3, 2, 1, 6),
    _DiffServMeterStatus_Type()
)
diffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStatus.setStatus("current")
_DiffServTBParam_ObjectIdentity = ObjectIdentity
diffServTBParam = _DiffServTBParam_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 4)
)
_DiffServTBParamNextFree_Type = IndexIntegerNextFree
_DiffServTBParamNextFree_Object = MibScalar
diffServTBParamNextFree = _DiffServTBParamNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 1),
    _DiffServTBParamNextFree_Type()
)
diffServTBParamNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTBParamNextFree.setStatus("current")
_DiffServTBParamTable_Object = MibTable
diffServTBParamTable = _DiffServTBParamTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2)
)
if mibBuilder.loadTexts:
    diffServTBParamTable.setStatus("current")
_DiffServTBParamEntry_Object = MibTableRow
diffServTBParamEntry = _DiffServTBParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1)
)
diffServTBParamEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServTBParamId"),
)
if mibBuilder.loadTexts:
    diffServTBParamEntry.setStatus("current")
_DiffServTBParamId_Type = IndexInteger
_DiffServTBParamId_Object = MibTableColumn
diffServTBParamId = _DiffServTBParamId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 1),
    _DiffServTBParamId_Type()
)
diffServTBParamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServTBParamId.setStatus("current")
_DiffServTBParamType_Type = AutonomousType
_DiffServTBParamType_Object = MibTableColumn
diffServTBParamType = _DiffServTBParamType_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 2),
    _DiffServTBParamType_Type()
)
diffServTBParamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBParamType.setStatus("current")


class _DiffServTBParamRate_Type(Unsigned32):
    """Custom type diffServTBParamRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServTBParamRate_Type.__name__ = "Unsigned32"
_DiffServTBParamRate_Object = MibTableColumn
diffServTBParamRate = _DiffServTBParamRate_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 3),
    _DiffServTBParamRate_Type()
)
diffServTBParamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBParamRate.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBParamRate.setUnits("kilobits per second")
_DiffServTBParamBurstSize_Type = BurstSize
_DiffServTBParamBurstSize_Object = MibTableColumn
diffServTBParamBurstSize = _DiffServTBParamBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 4),
    _DiffServTBParamBurstSize_Type()
)
diffServTBParamBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBParamBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBParamBurstSize.setUnits("Bytes")


class _DiffServTBParamInterval_Type(Unsigned32):
    """Custom type diffServTBParamInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServTBParamInterval_Type.__name__ = "Unsigned32"
_DiffServTBParamInterval_Object = MibTableColumn
diffServTBParamInterval = _DiffServTBParamInterval_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 5),
    _DiffServTBParamInterval_Type()
)
diffServTBParamInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBParamInterval.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBParamInterval.setUnits("microseconds")


class _DiffServTBParamStorage_Type(StorageType):
    """Custom type diffServTBParamStorage based on StorageType"""


_DiffServTBParamStorage_Object = MibTableColumn
diffServTBParamStorage = _DiffServTBParamStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 6),
    _DiffServTBParamStorage_Type()
)
diffServTBParamStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBParamStorage.setStatus("current")
_DiffServTBParamStatus_Type = RowStatus
_DiffServTBParamStatus_Object = MibTableColumn
diffServTBParamStatus = _DiffServTBParamStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 4, 2, 1, 7),
    _DiffServTBParamStatus_Type()
)
diffServTBParamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBParamStatus.setStatus("current")
_DiffServAction_ObjectIdentity = ObjectIdentity
diffServAction = _DiffServAction_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 5)
)
_DiffServActionNextFree_Type = IndexIntegerNextFree
_DiffServActionNextFree_Object = MibScalar
diffServActionNextFree = _DiffServActionNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 1),
    _DiffServActionNextFree_Type()
)
diffServActionNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionNextFree.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1)
)
diffServActionEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServActionId"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")
_DiffServActionId_Type = IndexInteger
_DiffServActionId_Object = MibTableColumn
diffServActionId = _DiffServActionId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1, 1),
    _DiffServActionId_Type()
)
diffServActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServActionId.setStatus("current")
_DiffServActionInterface_Type = InterfaceIndexOrZero
_DiffServActionInterface_Object = MibTableColumn
diffServActionInterface = _DiffServActionInterface_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1, 2),
    _DiffServActionInterface_Type()
)
diffServActionInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionInterface.setStatus("current")


class _DiffServActionNext_Type(RowPointer):
    """Custom type diffServActionNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServActionNext_Object = MibTableColumn
diffServActionNext = _DiffServActionNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1, 3),
    _DiffServActionNext_Type()
)
diffServActionNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionNext.setStatus("current")
_DiffServActionSpecific_Type = RowPointer
_DiffServActionSpecific_Object = MibTableColumn
diffServActionSpecific = _DiffServActionSpecific_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1, 4),
    _DiffServActionSpecific_Type()
)
diffServActionSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionSpecific.setStatus("current")


class _DiffServActionStorage_Type(StorageType):
    """Custom type diffServActionStorage based on StorageType"""


_DiffServActionStorage_Object = MibTableColumn
diffServActionStorage = _DiffServActionStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1, 5),
    _DiffServActionStorage_Type()
)
diffServActionStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStorage.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 2, 1, 6),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")
_DiffServDscpMarkActTable_Object = MibTable
diffServDscpMarkActTable = _DiffServDscpMarkActTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 3)
)
if mibBuilder.loadTexts:
    diffServDscpMarkActTable.setStatus("current")
_DiffServDscpMarkActEntry_Object = MibTableRow
diffServDscpMarkActEntry = _DiffServDscpMarkActEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 3, 1)
)
diffServDscpMarkActEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServDscpMarkActDscp"),
)
if mibBuilder.loadTexts:
    diffServDscpMarkActEntry.setStatus("current")
_DiffServDscpMarkActDscp_Type = Dscp
_DiffServDscpMarkActDscp_Object = MibTableColumn
diffServDscpMarkActDscp = _DiffServDscpMarkActDscp_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 3, 1, 1),
    _DiffServDscpMarkActDscp_Type()
)
diffServDscpMarkActDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServDscpMarkActDscp.setStatus("current")
_DiffServCountActNextFree_Type = IndexIntegerNextFree
_DiffServCountActNextFree_Object = MibScalar
diffServCountActNextFree = _DiffServCountActNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 4),
    _DiffServCountActNextFree_Type()
)
diffServCountActNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActNextFree.setStatus("current")
_DiffServCountActTable_Object = MibTable
diffServCountActTable = _DiffServCountActTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5)
)
if mibBuilder.loadTexts:
    diffServCountActTable.setStatus("current")
_DiffServCountActEntry_Object = MibTableRow
diffServCountActEntry = _DiffServCountActEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5, 1)
)
diffServCountActEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServCountActId"),
)
if mibBuilder.loadTexts:
    diffServCountActEntry.setStatus("current")
_DiffServCountActId_Type = IndexInteger
_DiffServCountActId_Object = MibTableColumn
diffServCountActId = _DiffServCountActId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5, 1, 1),
    _DiffServCountActId_Type()
)
diffServCountActId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServCountActId.setStatus("current")
_DiffServCountActOctets_Type = Counter64
_DiffServCountActOctets_Object = MibTableColumn
diffServCountActOctets = _DiffServCountActOctets_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5, 1, 2),
    _DiffServCountActOctets_Type()
)
diffServCountActOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActOctets.setStatus("current")
_DiffServCountActPkts_Type = Counter64
_DiffServCountActPkts_Object = MibTableColumn
diffServCountActPkts = _DiffServCountActPkts_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5, 1, 3),
    _DiffServCountActPkts_Type()
)
diffServCountActPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActPkts.setStatus("current")


class _DiffServCountActStorage_Type(StorageType):
    """Custom type diffServCountActStorage based on StorageType"""


_DiffServCountActStorage_Object = MibTableColumn
diffServCountActStorage = _DiffServCountActStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5, 1, 4),
    _DiffServCountActStorage_Type()
)
diffServCountActStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServCountActStorage.setStatus("current")
_DiffServCountActStatus_Type = RowStatus
_DiffServCountActStatus_Object = MibTableColumn
diffServCountActStatus = _DiffServCountActStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 5, 5, 1, 5),
    _DiffServCountActStatus_Type()
)
diffServCountActStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServCountActStatus.setStatus("current")
_DiffServAlgDrop_ObjectIdentity = ObjectIdentity
diffServAlgDrop = _DiffServAlgDrop_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 6)
)
_DiffServAlgDropNextFree_Type = IndexIntegerNextFree
_DiffServAlgDropNextFree_Object = MibScalar
diffServAlgDropNextFree = _DiffServAlgDropNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 1),
    _DiffServAlgDropNextFree_Type()
)
diffServAlgDropNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropNextFree.setStatus("current")
_DiffServAlgDropTable_Object = MibTable
diffServAlgDropTable = _DiffServAlgDropTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2)
)
if mibBuilder.loadTexts:
    diffServAlgDropTable.setStatus("current")
_DiffServAlgDropEntry_Object = MibTableRow
diffServAlgDropEntry = _DiffServAlgDropEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1)
)
diffServAlgDropEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServAlgDropId"),
)
if mibBuilder.loadTexts:
    diffServAlgDropEntry.setStatus("current")
_DiffServAlgDropId_Type = IndexInteger
_DiffServAlgDropId_Object = MibTableColumn
diffServAlgDropId = _DiffServAlgDropId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 1),
    _DiffServAlgDropId_Type()
)
diffServAlgDropId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAlgDropId.setStatus("current")


class _DiffServAlgDropType_Type(Integer32):
    """Custom type diffServAlgDropType based on Integer32"""
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
        *(("alwaysDrop", 5),
          ("headDrop", 3),
          ("other", 1),
          ("randomDrop", 4),
          ("tailDrop", 2))
    )


_DiffServAlgDropType_Type.__name__ = "Integer32"
_DiffServAlgDropType_Object = MibTableColumn
diffServAlgDropType = _DiffServAlgDropType_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 2),
    _DiffServAlgDropType_Type()
)
diffServAlgDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropType.setStatus("current")
_DiffServAlgDropNext_Type = RowPointer
_DiffServAlgDropNext_Object = MibTableColumn
diffServAlgDropNext = _DiffServAlgDropNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 3),
    _DiffServAlgDropNext_Type()
)
diffServAlgDropNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropNext.setStatus("current")
_DiffServAlgDropQMeasure_Type = RowPointer
_DiffServAlgDropQMeasure_Object = MibTableColumn
diffServAlgDropQMeasure = _DiffServAlgDropQMeasure_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 4),
    _DiffServAlgDropQMeasure_Type()
)
diffServAlgDropQMeasure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropQMeasure.setStatus("current")


class _DiffServAlgDropQThreshold_Type(Unsigned32):
    """Custom type diffServAlgDropQThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServAlgDropQThreshold_Type.__name__ = "Unsigned32"
_DiffServAlgDropQThreshold_Object = MibTableColumn
diffServAlgDropQThreshold = _DiffServAlgDropQThreshold_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 5),
    _DiffServAlgDropQThreshold_Type()
)
diffServAlgDropQThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropQThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diffServAlgDropQThreshold.setUnits("Bytes")
_DiffServAlgDropSpecific_Type = RowPointer
_DiffServAlgDropSpecific_Object = MibTableColumn
diffServAlgDropSpecific = _DiffServAlgDropSpecific_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 6),
    _DiffServAlgDropSpecific_Type()
)
diffServAlgDropSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropSpecific.setStatus("current")
_DiffServAlgDropOctets_Type = Counter64
_DiffServAlgDropOctets_Object = MibTableColumn
diffServAlgDropOctets = _DiffServAlgDropOctets_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 7),
    _DiffServAlgDropOctets_Type()
)
diffServAlgDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropOctets.setStatus("current")
_DiffServAlgDropPkts_Type = Counter64
_DiffServAlgDropPkts_Object = MibTableColumn
diffServAlgDropPkts = _DiffServAlgDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 8),
    _DiffServAlgDropPkts_Type()
)
diffServAlgDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropPkts.setStatus("current")
_DiffServAlgRandomDropOctets_Type = Counter64
_DiffServAlgRandomDropOctets_Object = MibTableColumn
diffServAlgRandomDropOctets = _DiffServAlgRandomDropOctets_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 9),
    _DiffServAlgRandomDropOctets_Type()
)
diffServAlgRandomDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgRandomDropOctets.setStatus("current")
_DiffServAlgRandomDropPkts_Type = Counter64
_DiffServAlgRandomDropPkts_Object = MibTableColumn
diffServAlgRandomDropPkts = _DiffServAlgRandomDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 10),
    _DiffServAlgRandomDropPkts_Type()
)
diffServAlgRandomDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgRandomDropPkts.setStatus("current")


class _DiffServAlgDropStorage_Type(StorageType):
    """Custom type diffServAlgDropStorage based on StorageType"""


_DiffServAlgDropStorage_Object = MibTableColumn
diffServAlgDropStorage = _DiffServAlgDropStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 11),
    _DiffServAlgDropStorage_Type()
)
diffServAlgDropStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropStorage.setStatus("current")
_DiffServAlgDropStatus_Type = RowStatus
_DiffServAlgDropStatus_Object = MibTableColumn
diffServAlgDropStatus = _DiffServAlgDropStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 2, 1, 12),
    _DiffServAlgDropStatus_Type()
)
diffServAlgDropStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropStatus.setStatus("current")
_DiffServRandomDropNextFree_Type = IndexIntegerNextFree
_DiffServRandomDropNextFree_Object = MibScalar
diffServRandomDropNextFree = _DiffServRandomDropNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 3),
    _DiffServRandomDropNextFree_Type()
)
diffServRandomDropNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServRandomDropNextFree.setStatus("current")
_DiffServRandomDropTable_Object = MibTable
diffServRandomDropTable = _DiffServRandomDropTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4)
)
if mibBuilder.loadTexts:
    diffServRandomDropTable.setStatus("current")
_DiffServRandomDropEntry_Object = MibTableRow
diffServRandomDropEntry = _DiffServRandomDropEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1)
)
diffServRandomDropEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServRandomDropId"),
)
if mibBuilder.loadTexts:
    diffServRandomDropEntry.setStatus("current")
_DiffServRandomDropId_Type = IndexInteger
_DiffServRandomDropId_Object = MibTableColumn
diffServRandomDropId = _DiffServRandomDropId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 1),
    _DiffServRandomDropId_Type()
)
diffServRandomDropId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServRandomDropId.setStatus("current")


class _DiffServRandomDropMinThreshBytes_Type(Unsigned32):
    """Custom type diffServRandomDropMinThreshBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServRandomDropMinThreshBytes_Type.__name__ = "Unsigned32"
_DiffServRandomDropMinThreshBytes_Object = MibTableColumn
diffServRandomDropMinThreshBytes = _DiffServRandomDropMinThreshBytes_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 2),
    _DiffServRandomDropMinThreshBytes_Type()
)
diffServRandomDropMinThreshBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshBytes.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshBytes.setUnits("bytes")


class _DiffServRandomDropMinThreshPkts_Type(Unsigned32):
    """Custom type diffServRandomDropMinThreshPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServRandomDropMinThreshPkts_Type.__name__ = "Unsigned32"
_DiffServRandomDropMinThreshPkts_Object = MibTableColumn
diffServRandomDropMinThreshPkts = _DiffServRandomDropMinThreshPkts_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 3),
    _DiffServRandomDropMinThreshPkts_Type()
)
diffServRandomDropMinThreshPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshPkts.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshPkts.setUnits("packets")


class _DiffServRandomDropMaxThreshBytes_Type(Unsigned32):
    """Custom type diffServRandomDropMaxThreshBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServRandomDropMaxThreshBytes_Type.__name__ = "Unsigned32"
_DiffServRandomDropMaxThreshBytes_Object = MibTableColumn
diffServRandomDropMaxThreshBytes = _DiffServRandomDropMaxThreshBytes_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 4),
    _DiffServRandomDropMaxThreshBytes_Type()
)
diffServRandomDropMaxThreshBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshBytes.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshBytes.setUnits("bytes")


class _DiffServRandomDropMaxThreshPkts_Type(Unsigned32):
    """Custom type diffServRandomDropMaxThreshPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServRandomDropMaxThreshPkts_Type.__name__ = "Unsigned32"
_DiffServRandomDropMaxThreshPkts_Object = MibTableColumn
diffServRandomDropMaxThreshPkts = _DiffServRandomDropMaxThreshPkts_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 5),
    _DiffServRandomDropMaxThreshPkts_Type()
)
diffServRandomDropMaxThreshPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshPkts.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshPkts.setUnits("packets")


class _DiffServRandomDropProbMax_Type(Unsigned32):
    """Custom type diffServRandomDropProbMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DiffServRandomDropProbMax_Type.__name__ = "Unsigned32"
_DiffServRandomDropProbMax_Object = MibTableColumn
diffServRandomDropProbMax = _DiffServRandomDropProbMax_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 6),
    _DiffServRandomDropProbMax_Type()
)
diffServRandomDropProbMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropProbMax.setStatus("current")


class _DiffServRandomDropWeight_Type(Unsigned32):
    """Custom type diffServRandomDropWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DiffServRandomDropWeight_Type.__name__ = "Unsigned32"
_DiffServRandomDropWeight_Object = MibTableColumn
diffServRandomDropWeight = _DiffServRandomDropWeight_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 7),
    _DiffServRandomDropWeight_Type()
)
diffServRandomDropWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropWeight.setStatus("current")


class _DiffServRandomDropSamplingRate_Type(Unsigned32):
    """Custom type diffServRandomDropSamplingRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_DiffServRandomDropSamplingRate_Type.__name__ = "Unsigned32"
_DiffServRandomDropSamplingRate_Object = MibTableColumn
diffServRandomDropSamplingRate = _DiffServRandomDropSamplingRate_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 8),
    _DiffServRandomDropSamplingRate_Type()
)
diffServRandomDropSamplingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropSamplingRate.setStatus("current")


class _DiffServRandomDropStorage_Type(StorageType):
    """Custom type diffServRandomDropStorage based on StorageType"""


_DiffServRandomDropStorage_Object = MibTableColumn
diffServRandomDropStorage = _DiffServRandomDropStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 9),
    _DiffServRandomDropStorage_Type()
)
diffServRandomDropStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropStorage.setStatus("current")
_DiffServRandomDropStatus_Type = RowStatus
_DiffServRandomDropStatus_Object = MibTableColumn
diffServRandomDropStatus = _DiffServRandomDropStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 6, 4, 1, 10),
    _DiffServRandomDropStatus_Type()
)
diffServRandomDropStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropStatus.setStatus("current")
_DiffServQueue_ObjectIdentity = ObjectIdentity
diffServQueue = _DiffServQueue_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 7)
)
_DiffServQNextFree_Type = IndexIntegerNextFree
_DiffServQNextFree_Object = MibScalar
diffServQNextFree = _DiffServQNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 1),
    _DiffServQNextFree_Type()
)
diffServQNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServQNextFree.setStatus("current")
_DiffServQTable_Object = MibTable
diffServQTable = _DiffServQTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2)
)
if mibBuilder.loadTexts:
    diffServQTable.setStatus("current")
_DiffServQEntry_Object = MibTableRow
diffServQEntry = _DiffServQEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1)
)
diffServQEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServQId"),
)
if mibBuilder.loadTexts:
    diffServQEntry.setStatus("current")
_DiffServQId_Type = IndexInteger
_DiffServQId_Object = MibTableColumn
diffServQId = _DiffServQId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1, 1),
    _DiffServQId_Type()
)
diffServQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServQId.setStatus("current")
_DiffServQNext_Type = RowPointer
_DiffServQNext_Object = MibTableColumn
diffServQNext = _DiffServQNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1, 2),
    _DiffServQNext_Type()
)
diffServQNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQNext.setStatus("current")
_DiffServQMinRate_Type = RowPointer
_DiffServQMinRate_Object = MibTableColumn
diffServQMinRate = _DiffServQMinRate_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1, 3),
    _DiffServQMinRate_Type()
)
diffServQMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQMinRate.setStatus("current")
_DiffServQMaxRate_Type = RowPointer
_DiffServQMaxRate_Object = MibTableColumn
diffServQMaxRate = _DiffServQMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1, 4),
    _DiffServQMaxRate_Type()
)
diffServQMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQMaxRate.setStatus("current")


class _DiffServQStorage_Type(StorageType):
    """Custom type diffServQStorage based on StorageType"""


_DiffServQStorage_Object = MibTableColumn
diffServQStorage = _DiffServQStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1, 5),
    _DiffServQStorage_Type()
)
diffServQStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQStorage.setStatus("current")
_DiffServQStatus_Type = RowStatus
_DiffServQStatus_Object = MibTableColumn
diffServQStatus = _DiffServQStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 7, 2, 1, 6),
    _DiffServQStatus_Type()
)
diffServQStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQStatus.setStatus("current")
_DiffServScheduler_ObjectIdentity = ObjectIdentity
diffServScheduler = _DiffServScheduler_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 1, 8)
)
_DiffServSchedulerNextFree_Type = IndexIntegerNextFree
_DiffServSchedulerNextFree_Object = MibScalar
diffServSchedulerNextFree = _DiffServSchedulerNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 1),
    _DiffServSchedulerNextFree_Type()
)
diffServSchedulerNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServSchedulerNextFree.setStatus("current")
_DiffServSchedulerTable_Object = MibTable
diffServSchedulerTable = _DiffServSchedulerTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2)
)
if mibBuilder.loadTexts:
    diffServSchedulerTable.setStatus("current")
_DiffServSchedulerEntry_Object = MibTableRow
diffServSchedulerEntry = _DiffServSchedulerEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1)
)
diffServSchedulerEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServSchedulerId"),
)
if mibBuilder.loadTexts:
    diffServSchedulerEntry.setStatus("current")
_DiffServSchedulerId_Type = IndexInteger
_DiffServSchedulerId_Object = MibTableColumn
diffServSchedulerId = _DiffServSchedulerId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 1),
    _DiffServSchedulerId_Type()
)
diffServSchedulerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServSchedulerId.setStatus("current")


class _DiffServSchedulerNext_Type(RowPointer):
    """Custom type diffServSchedulerNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServSchedulerNext_Object = MibTableColumn
diffServSchedulerNext = _DiffServSchedulerNext_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 2),
    _DiffServSchedulerNext_Type()
)
diffServSchedulerNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerNext.setStatus("current")
_DiffServSchedulerMethod_Type = AutonomousType
_DiffServSchedulerMethod_Object = MibTableColumn
diffServSchedulerMethod = _DiffServSchedulerMethod_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 3),
    _DiffServSchedulerMethod_Type()
)
diffServSchedulerMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerMethod.setStatus("current")


class _DiffServSchedulerMinRate_Type(RowPointer):
    """Custom type diffServSchedulerMinRate based on RowPointer"""
    defaultValue = (0, 0)


_DiffServSchedulerMinRate_Object = MibTableColumn
diffServSchedulerMinRate = _DiffServSchedulerMinRate_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 4),
    _DiffServSchedulerMinRate_Type()
)
diffServSchedulerMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerMinRate.setStatus("current")


class _DiffServSchedulerMaxRate_Type(RowPointer):
    """Custom type diffServSchedulerMaxRate based on RowPointer"""
    defaultValue = (0, 0)


_DiffServSchedulerMaxRate_Object = MibTableColumn
diffServSchedulerMaxRate = _DiffServSchedulerMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 5),
    _DiffServSchedulerMaxRate_Type()
)
diffServSchedulerMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerMaxRate.setStatus("current")


class _DiffServSchedulerStorage_Type(StorageType):
    """Custom type diffServSchedulerStorage based on StorageType"""


_DiffServSchedulerStorage_Object = MibTableColumn
diffServSchedulerStorage = _DiffServSchedulerStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 6),
    _DiffServSchedulerStorage_Type()
)
diffServSchedulerStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerStorage.setStatus("current")
_DiffServSchedulerStatus_Type = RowStatus
_DiffServSchedulerStatus_Object = MibTableColumn
diffServSchedulerStatus = _DiffServSchedulerStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 2, 1, 7),
    _DiffServSchedulerStatus_Type()
)
diffServSchedulerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerStatus.setStatus("current")
_DiffServMinRateNextFree_Type = IndexIntegerNextFree
_DiffServMinRateNextFree_Object = MibScalar
diffServMinRateNextFree = _DiffServMinRateNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 3),
    _DiffServMinRateNextFree_Type()
)
diffServMinRateNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServMinRateNextFree.setStatus("current")
_DiffServMinRateTable_Object = MibTable
diffServMinRateTable = _DiffServMinRateTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4)
)
if mibBuilder.loadTexts:
    diffServMinRateTable.setStatus("current")
_DiffServMinRateEntry_Object = MibTableRow
diffServMinRateEntry = _DiffServMinRateEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1)
)
diffServMinRateEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServMinRateId"),
)
if mibBuilder.loadTexts:
    diffServMinRateEntry.setStatus("current")
_DiffServMinRateId_Type = IndexInteger
_DiffServMinRateId_Object = MibTableColumn
diffServMinRateId = _DiffServMinRateId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1, 1),
    _DiffServMinRateId_Type()
)
diffServMinRateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMinRateId.setStatus("current")


class _DiffServMinRatePriority_Type(Unsigned32):
    """Custom type diffServMinRatePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServMinRatePriority_Type.__name__ = "Unsigned32"
_DiffServMinRatePriority_Object = MibTableColumn
diffServMinRatePriority = _DiffServMinRatePriority_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1, 2),
    _DiffServMinRatePriority_Type()
)
diffServMinRatePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMinRatePriority.setStatus("current")


class _DiffServMinRateAbsolute_Type(Unsigned32):
    """Custom type diffServMinRateAbsolute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServMinRateAbsolute_Type.__name__ = "Unsigned32"
_DiffServMinRateAbsolute_Object = MibTableColumn
diffServMinRateAbsolute = _DiffServMinRateAbsolute_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1, 3),
    _DiffServMinRateAbsolute_Type()
)
diffServMinRateAbsolute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMinRateAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    diffServMinRateAbsolute.setUnits("kilobits per second")


class _DiffServMinRateRelative_Type(Unsigned32):
    """Custom type diffServMinRateRelative based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServMinRateRelative_Type.__name__ = "Unsigned32"
_DiffServMinRateRelative_Object = MibTableColumn
diffServMinRateRelative = _DiffServMinRateRelative_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1, 4),
    _DiffServMinRateRelative_Type()
)
diffServMinRateRelative.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMinRateRelative.setStatus("current")


class _DiffServMinRateStorage_Type(StorageType):
    """Custom type diffServMinRateStorage based on StorageType"""


_DiffServMinRateStorage_Object = MibTableColumn
diffServMinRateStorage = _DiffServMinRateStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1, 5),
    _DiffServMinRateStorage_Type()
)
diffServMinRateStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMinRateStorage.setStatus("current")
_DiffServMinRateStatus_Type = RowStatus
_DiffServMinRateStatus_Object = MibTableColumn
diffServMinRateStatus = _DiffServMinRateStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 4, 1, 6),
    _DiffServMinRateStatus_Type()
)
diffServMinRateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMinRateStatus.setStatus("current")
_DiffServMaxRateNextFree_Type = IndexIntegerNextFree
_DiffServMaxRateNextFree_Object = MibScalar
diffServMaxRateNextFree = _DiffServMaxRateNextFree_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 5),
    _DiffServMaxRateNextFree_Type()
)
diffServMaxRateNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServMaxRateNextFree.setStatus("current")
_DiffServMaxRateTable_Object = MibTable
diffServMaxRateTable = _DiffServMaxRateTable_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6)
)
if mibBuilder.loadTexts:
    diffServMaxRateTable.setStatus("current")
_DiffServMaxRateEntry_Object = MibTableRow
diffServMaxRateEntry = _DiffServMaxRateEntry_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1)
)
diffServMaxRateEntry.setIndexNames(
    (0, "DIFFSERV-MIB", "diffServMaxRateId"),
    (0, "DIFFSERV-MIB", "diffServMaxRateLevel"),
)
if mibBuilder.loadTexts:
    diffServMaxRateEntry.setStatus("current")
_DiffServMaxRateId_Type = IndexInteger
_DiffServMaxRateId_Object = MibTableColumn
diffServMaxRateId = _DiffServMaxRateId_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 1),
    _DiffServMaxRateId_Type()
)
diffServMaxRateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMaxRateId.setStatus("current")


class _DiffServMaxRateLevel_Type(Unsigned32):
    """Custom type diffServMaxRateLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DiffServMaxRateLevel_Type.__name__ = "Unsigned32"
_DiffServMaxRateLevel_Object = MibTableColumn
diffServMaxRateLevel = _DiffServMaxRateLevel_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 2),
    _DiffServMaxRateLevel_Type()
)
diffServMaxRateLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMaxRateLevel.setStatus("current")


class _DiffServMaxRateAbsolute_Type(Unsigned32):
    """Custom type diffServMaxRateAbsolute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServMaxRateAbsolute_Type.__name__ = "Unsigned32"
_DiffServMaxRateAbsolute_Object = MibTableColumn
diffServMaxRateAbsolute = _DiffServMaxRateAbsolute_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 3),
    _DiffServMaxRateAbsolute_Type()
)
diffServMaxRateAbsolute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMaxRateAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    diffServMaxRateAbsolute.setUnits("kilobits per second")


class _DiffServMaxRateRelative_Type(Unsigned32):
    """Custom type diffServMaxRateRelative based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DiffServMaxRateRelative_Type.__name__ = "Unsigned32"
_DiffServMaxRateRelative_Object = MibTableColumn
diffServMaxRateRelative = _DiffServMaxRateRelative_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 4),
    _DiffServMaxRateRelative_Type()
)
diffServMaxRateRelative.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMaxRateRelative.setStatus("current")
_DiffServMaxRateThreshold_Type = BurstSize
_DiffServMaxRateThreshold_Object = MibTableColumn
diffServMaxRateThreshold = _DiffServMaxRateThreshold_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 5),
    _DiffServMaxRateThreshold_Type()
)
diffServMaxRateThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMaxRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diffServMaxRateThreshold.setUnits("Bytes")


class _DiffServMaxRateStorage_Type(StorageType):
    """Custom type diffServMaxRateStorage based on StorageType"""


_DiffServMaxRateStorage_Object = MibTableColumn
diffServMaxRateStorage = _DiffServMaxRateStorage_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 6),
    _DiffServMaxRateStorage_Type()
)
diffServMaxRateStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMaxRateStorage.setStatus("current")
_DiffServMaxRateStatus_Type = RowStatus
_DiffServMaxRateStatus_Object = MibTableColumn
diffServMaxRateStatus = _DiffServMaxRateStatus_Object(
    (1, 3, 6, 1, 2, 1, 97, 1, 8, 6, 1, 7),
    _DiffServMaxRateStatus_Type()
)
diffServMaxRateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMaxRateStatus.setStatus("current")
_DiffServMIBConformance_ObjectIdentity = ObjectIdentity
diffServMIBConformance = _DiffServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 2)
)
_DiffServMIBCompliances_ObjectIdentity = ObjectIdentity
diffServMIBCompliances = _DiffServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 2, 1)
)
_DiffServMIBGroups_ObjectIdentity = ObjectIdentity
diffServMIBGroups = _DiffServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 2, 2)
)
_DiffServMIBAdmin_ObjectIdentity = ObjectIdentity
diffServMIBAdmin = _DiffServMIBAdmin_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3)
)
_DiffServTBMeters_ObjectIdentity = ObjectIdentity
diffServTBMeters = _DiffServTBMeters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1)
)
_DiffServTBParamSimpleTokenBucket_ObjectIdentity = ObjectIdentity
diffServTBParamSimpleTokenBucket = _DiffServTBParamSimpleTokenBucket_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 1)
)
if mibBuilder.loadTexts:
    diffServTBParamSimpleTokenBucket.setStatus("current")
_DiffServTBParamAvgRate_ObjectIdentity = ObjectIdentity
diffServTBParamAvgRate = _DiffServTBParamAvgRate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 2)
)
if mibBuilder.loadTexts:
    diffServTBParamAvgRate.setStatus("current")
_DiffServTBParamSrTCMBlind_ObjectIdentity = ObjectIdentity
diffServTBParamSrTCMBlind = _DiffServTBParamSrTCMBlind_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 3)
)
if mibBuilder.loadTexts:
    diffServTBParamSrTCMBlind.setStatus("current")
_DiffServTBParamSrTCMAware_ObjectIdentity = ObjectIdentity
diffServTBParamSrTCMAware = _DiffServTBParamSrTCMAware_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 4)
)
if mibBuilder.loadTexts:
    diffServTBParamSrTCMAware.setStatus("current")
_DiffServTBParamTrTCMBlind_ObjectIdentity = ObjectIdentity
diffServTBParamTrTCMBlind = _DiffServTBParamTrTCMBlind_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 5)
)
if mibBuilder.loadTexts:
    diffServTBParamTrTCMBlind.setStatus("current")
_DiffServTBParamTrTCMAware_ObjectIdentity = ObjectIdentity
diffServTBParamTrTCMAware = _DiffServTBParamTrTCMAware_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 6)
)
if mibBuilder.loadTexts:
    diffServTBParamTrTCMAware.setStatus("current")
_DiffServTBParamTswTCM_ObjectIdentity = ObjectIdentity
diffServTBParamTswTCM = _DiffServTBParamTswTCM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 1, 7)
)
if mibBuilder.loadTexts:
    diffServTBParamTswTCM.setStatus("current")
_DiffServSchedulers_ObjectIdentity = ObjectIdentity
diffServSchedulers = _DiffServSchedulers_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 2)
)
_DiffServSchedulerPriority_ObjectIdentity = ObjectIdentity
diffServSchedulerPriority = _DiffServSchedulerPriority_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 2, 1)
)
if mibBuilder.loadTexts:
    diffServSchedulerPriority.setStatus("current")
_DiffServSchedulerWRR_ObjectIdentity = ObjectIdentity
diffServSchedulerWRR = _DiffServSchedulerWRR_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 2, 2)
)
if mibBuilder.loadTexts:
    diffServSchedulerWRR.setStatus("current")
_DiffServSchedulerWFQ_ObjectIdentity = ObjectIdentity
diffServSchedulerWFQ = _DiffServSchedulerWFQ_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 97, 3, 2, 3)
)
if mibBuilder.loadTexts:
    diffServSchedulerWFQ.setStatus("current")

# Managed Objects groups

diffServMIBDataPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 1)
)
diffServMIBDataPathGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServDataPathStart"),
        ("DIFFSERV-MIB", "diffServDataPathStorage"),
        ("DIFFSERV-MIB", "diffServDataPathStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBDataPathGroup.setStatus("current")

diffServMIBClfrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 2)
)
diffServMIBClfrGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServClfrNextFree"),
        ("DIFFSERV-MIB", "diffServClfrStorage"),
        ("DIFFSERV-MIB", "diffServClfrStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBClfrGroup.setStatus("current")

diffServMIBClfrElementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 3)
)
diffServMIBClfrElementGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServClfrElementNextFree"),
        ("DIFFSERV-MIB", "diffServClfrElementPrecedence"),
        ("DIFFSERV-MIB", "diffServClfrElementNext"),
        ("DIFFSERV-MIB", "diffServClfrElementSpecific"),
        ("DIFFSERV-MIB", "diffServClfrElementStorage"),
        ("DIFFSERV-MIB", "diffServClfrElementStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBClfrElementGroup.setStatus("current")

diffServMIBMultiFieldClfrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 4)
)
diffServMIBMultiFieldClfrGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServMultiFieldClfrNextFree"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrAddrType"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrDstAddr"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrDstPrefixLength"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrFlowId"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrSrcAddr"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrSrcPrefixLength"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrDscp"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrProtocol"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrDstL4PortMin"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrDstL4PortMax"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrSrcL4PortMin"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrSrcL4PortMax"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrStorage"),
        ("DIFFSERV-MIB", "diffServMultiFieldClfrStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBMultiFieldClfrGroup.setStatus("current")

diffServMIBMeterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 5)
)
diffServMIBMeterGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServMeterNextFree"),
        ("DIFFSERV-MIB", "diffServMeterSucceedNext"),
        ("DIFFSERV-MIB", "diffServMeterFailNext"),
        ("DIFFSERV-MIB", "diffServMeterSpecific"),
        ("DIFFSERV-MIB", "diffServMeterStorage"),
        ("DIFFSERV-MIB", "diffServMeterStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBMeterGroup.setStatus("current")

diffServMIBTBParamGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 6)
)
diffServMIBTBParamGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServTBParamNextFree"),
        ("DIFFSERV-MIB", "diffServTBParamType"),
        ("DIFFSERV-MIB", "diffServTBParamRate"),
        ("DIFFSERV-MIB", "diffServTBParamBurstSize"),
        ("DIFFSERV-MIB", "diffServTBParamInterval"),
        ("DIFFSERV-MIB", "diffServTBParamStorage"),
        ("DIFFSERV-MIB", "diffServTBParamStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBTBParamGroup.setStatus("current")

diffServMIBActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 7)
)
diffServMIBActionGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServActionNextFree"),
        ("DIFFSERV-MIB", "diffServActionNext"),
        ("DIFFSERV-MIB", "diffServActionSpecific"),
        ("DIFFSERV-MIB", "diffServActionStorage"),
        ("DIFFSERV-MIB", "diffServActionInterface"),
        ("DIFFSERV-MIB", "diffServActionStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBActionGroup.setStatus("current")

diffServMIBDscpMarkActGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 8)
)
diffServMIBDscpMarkActGroup.setObjects(
    ("DIFFSERV-MIB", "diffServDscpMarkActDscp")
)
if mibBuilder.loadTexts:
    diffServMIBDscpMarkActGroup.setStatus("current")

diffServMIBCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 9)
)
diffServMIBCounterGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServCountActOctets"),
        ("DIFFSERV-MIB", "diffServCountActPkts"),
        ("DIFFSERV-MIB", "diffServAlgDropOctets"),
        ("DIFFSERV-MIB", "diffServAlgDropPkts"),
        ("DIFFSERV-MIB", "diffServAlgRandomDropOctets"),
        ("DIFFSERV-MIB", "diffServAlgRandomDropPkts"),
        ("DIFFSERV-MIB", "diffServCountActStorage"),
        ("DIFFSERV-MIB", "diffServCountActStatus"),
        ("DIFFSERV-MIB", "diffServCountActNextFree"))
)
if mibBuilder.loadTexts:
    diffServMIBCounterGroup.setStatus("current")

diffServMIBAlgDropGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 10)
)
diffServMIBAlgDropGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServAlgDropNextFree"),
        ("DIFFSERV-MIB", "diffServAlgDropType"),
        ("DIFFSERV-MIB", "diffServAlgDropNext"),
        ("DIFFSERV-MIB", "diffServAlgDropQMeasure"),
        ("DIFFSERV-MIB", "diffServAlgDropQThreshold"),
        ("DIFFSERV-MIB", "diffServAlgDropSpecific"),
        ("DIFFSERV-MIB", "diffServAlgDropStorage"),
        ("DIFFSERV-MIB", "diffServAlgDropStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBAlgDropGroup.setStatus("current")

diffServMIBRandomDropGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 11)
)
diffServMIBRandomDropGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServRandomDropNextFree"),
        ("DIFFSERV-MIB", "diffServRandomDropMinThreshBytes"),
        ("DIFFSERV-MIB", "diffServRandomDropMinThreshPkts"),
        ("DIFFSERV-MIB", "diffServRandomDropMaxThreshBytes"),
        ("DIFFSERV-MIB", "diffServRandomDropMaxThreshPkts"),
        ("DIFFSERV-MIB", "diffServRandomDropProbMax"),
        ("DIFFSERV-MIB", "diffServRandomDropWeight"),
        ("DIFFSERV-MIB", "diffServRandomDropSamplingRate"),
        ("DIFFSERV-MIB", "diffServRandomDropStorage"),
        ("DIFFSERV-MIB", "diffServRandomDropStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBRandomDropGroup.setStatus("current")

diffServMIBQGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 12)
)
diffServMIBQGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServQNextFree"),
        ("DIFFSERV-MIB", "diffServQNext"),
        ("DIFFSERV-MIB", "diffServQMinRate"),
        ("DIFFSERV-MIB", "diffServQMaxRate"),
        ("DIFFSERV-MIB", "diffServQStorage"),
        ("DIFFSERV-MIB", "diffServQStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBQGroup.setStatus("current")

diffServMIBSchedulerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 13)
)
diffServMIBSchedulerGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServSchedulerNextFree"),
        ("DIFFSERV-MIB", "diffServSchedulerNext"),
        ("DIFFSERV-MIB", "diffServSchedulerMethod"),
        ("DIFFSERV-MIB", "diffServSchedulerMinRate"),
        ("DIFFSERV-MIB", "diffServSchedulerMaxRate"),
        ("DIFFSERV-MIB", "diffServSchedulerStorage"),
        ("DIFFSERV-MIB", "diffServSchedulerStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBSchedulerGroup.setStatus("current")

diffServMIBMinRateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 14)
)
diffServMIBMinRateGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServMinRateNextFree"),
        ("DIFFSERV-MIB", "diffServMinRatePriority"),
        ("DIFFSERV-MIB", "diffServMinRateAbsolute"),
        ("DIFFSERV-MIB", "diffServMinRateRelative"),
        ("DIFFSERV-MIB", "diffServMinRateStorage"),
        ("DIFFSERV-MIB", "diffServMinRateStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBMinRateGroup.setStatus("current")

diffServMIBMaxRateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 97, 2, 2, 15)
)
diffServMIBMaxRateGroup.setObjects(
      *(("DIFFSERV-MIB", "diffServMaxRateNextFree"),
        ("DIFFSERV-MIB", "diffServMaxRateAbsolute"),
        ("DIFFSERV-MIB", "diffServMaxRateRelative"),
        ("DIFFSERV-MIB", "diffServMaxRateThreshold"),
        ("DIFFSERV-MIB", "diffServMaxRateStorage"),
        ("DIFFSERV-MIB", "diffServMaxRateStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBMaxRateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diffServMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 97, 2, 1, 1)
)
if mibBuilder.loadTexts:
    diffServMIBFullCompliance.setStatus(
        "current"
    )

diffServMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 97, 2, 1, 2)
)
if mibBuilder.loadTexts:
    diffServMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIFFSERV-MIB",
    **{"IndexInteger": IndexInteger,
       "IndexIntegerNextFree": IndexIntegerNextFree,
       "IfDirection": IfDirection,
       "diffServMib": diffServMib,
       "diffServMIBObjects": diffServMIBObjects,
       "diffServDataPath": diffServDataPath,
       "diffServDataPathTable": diffServDataPathTable,
       "diffServDataPathEntry": diffServDataPathEntry,
       "diffServDataPathIfDirection": diffServDataPathIfDirection,
       "diffServDataPathStart": diffServDataPathStart,
       "diffServDataPathStorage": diffServDataPathStorage,
       "diffServDataPathStatus": diffServDataPathStatus,
       "diffServClassifier": diffServClassifier,
       "diffServClfrNextFree": diffServClfrNextFree,
       "diffServClfrTable": diffServClfrTable,
       "diffServClfrEntry": diffServClfrEntry,
       "diffServClfrId": diffServClfrId,
       "diffServClfrStorage": diffServClfrStorage,
       "diffServClfrStatus": diffServClfrStatus,
       "diffServClfrElementNextFree": diffServClfrElementNextFree,
       "diffServClfrElementTable": diffServClfrElementTable,
       "diffServClfrElementEntry": diffServClfrElementEntry,
       "diffServClfrElementId": diffServClfrElementId,
       "diffServClfrElementPrecedence": diffServClfrElementPrecedence,
       "diffServClfrElementNext": diffServClfrElementNext,
       "diffServClfrElementSpecific": diffServClfrElementSpecific,
       "diffServClfrElementStorage": diffServClfrElementStorage,
       "diffServClfrElementStatus": diffServClfrElementStatus,
       "diffServMultiFieldClfrNextFree": diffServMultiFieldClfrNextFree,
       "diffServMultiFieldClfrTable": diffServMultiFieldClfrTable,
       "diffServMultiFieldClfrEntry": diffServMultiFieldClfrEntry,
       "diffServMultiFieldClfrId": diffServMultiFieldClfrId,
       "diffServMultiFieldClfrAddrType": diffServMultiFieldClfrAddrType,
       "diffServMultiFieldClfrDstAddr": diffServMultiFieldClfrDstAddr,
       "diffServMultiFieldClfrDstPrefixLength": diffServMultiFieldClfrDstPrefixLength,
       "diffServMultiFieldClfrSrcAddr": diffServMultiFieldClfrSrcAddr,
       "diffServMultiFieldClfrSrcPrefixLength": diffServMultiFieldClfrSrcPrefixLength,
       "diffServMultiFieldClfrDscp": diffServMultiFieldClfrDscp,
       "diffServMultiFieldClfrFlowId": diffServMultiFieldClfrFlowId,
       "diffServMultiFieldClfrProtocol": diffServMultiFieldClfrProtocol,
       "diffServMultiFieldClfrDstL4PortMin": diffServMultiFieldClfrDstL4PortMin,
       "diffServMultiFieldClfrDstL4PortMax": diffServMultiFieldClfrDstL4PortMax,
       "diffServMultiFieldClfrSrcL4PortMin": diffServMultiFieldClfrSrcL4PortMin,
       "diffServMultiFieldClfrSrcL4PortMax": diffServMultiFieldClfrSrcL4PortMax,
       "diffServMultiFieldClfrStorage": diffServMultiFieldClfrStorage,
       "diffServMultiFieldClfrStatus": diffServMultiFieldClfrStatus,
       "diffServMeter": diffServMeter,
       "diffServMeterNextFree": diffServMeterNextFree,
       "diffServMeterTable": diffServMeterTable,
       "diffServMeterEntry": diffServMeterEntry,
       "diffServMeterId": diffServMeterId,
       "diffServMeterSucceedNext": diffServMeterSucceedNext,
       "diffServMeterFailNext": diffServMeterFailNext,
       "diffServMeterSpecific": diffServMeterSpecific,
       "diffServMeterStorage": diffServMeterStorage,
       "diffServMeterStatus": diffServMeterStatus,
       "diffServTBParam": diffServTBParam,
       "diffServTBParamNextFree": diffServTBParamNextFree,
       "diffServTBParamTable": diffServTBParamTable,
       "diffServTBParamEntry": diffServTBParamEntry,
       "diffServTBParamId": diffServTBParamId,
       "diffServTBParamType": diffServTBParamType,
       "diffServTBParamRate": diffServTBParamRate,
       "diffServTBParamBurstSize": diffServTBParamBurstSize,
       "diffServTBParamInterval": diffServTBParamInterval,
       "diffServTBParamStorage": diffServTBParamStorage,
       "diffServTBParamStatus": diffServTBParamStatus,
       "diffServAction": diffServAction,
       "diffServActionNextFree": diffServActionNextFree,
       "diffServActionTable": diffServActionTable,
       "diffServActionEntry": diffServActionEntry,
       "diffServActionId": diffServActionId,
       "diffServActionInterface": diffServActionInterface,
       "diffServActionNext": diffServActionNext,
       "diffServActionSpecific": diffServActionSpecific,
       "diffServActionStorage": diffServActionStorage,
       "diffServActionStatus": diffServActionStatus,
       "diffServDscpMarkActTable": diffServDscpMarkActTable,
       "diffServDscpMarkActEntry": diffServDscpMarkActEntry,
       "diffServDscpMarkActDscp": diffServDscpMarkActDscp,
       "diffServCountActNextFree": diffServCountActNextFree,
       "diffServCountActTable": diffServCountActTable,
       "diffServCountActEntry": diffServCountActEntry,
       "diffServCountActId": diffServCountActId,
       "diffServCountActOctets": diffServCountActOctets,
       "diffServCountActPkts": diffServCountActPkts,
       "diffServCountActStorage": diffServCountActStorage,
       "diffServCountActStatus": diffServCountActStatus,
       "diffServAlgDrop": diffServAlgDrop,
       "diffServAlgDropNextFree": diffServAlgDropNextFree,
       "diffServAlgDropTable": diffServAlgDropTable,
       "diffServAlgDropEntry": diffServAlgDropEntry,
       "diffServAlgDropId": diffServAlgDropId,
       "diffServAlgDropType": diffServAlgDropType,
       "diffServAlgDropNext": diffServAlgDropNext,
       "diffServAlgDropQMeasure": diffServAlgDropQMeasure,
       "diffServAlgDropQThreshold": diffServAlgDropQThreshold,
       "diffServAlgDropSpecific": diffServAlgDropSpecific,
       "diffServAlgDropOctets": diffServAlgDropOctets,
       "diffServAlgDropPkts": diffServAlgDropPkts,
       "diffServAlgRandomDropOctets": diffServAlgRandomDropOctets,
       "diffServAlgRandomDropPkts": diffServAlgRandomDropPkts,
       "diffServAlgDropStorage": diffServAlgDropStorage,
       "diffServAlgDropStatus": diffServAlgDropStatus,
       "diffServRandomDropNextFree": diffServRandomDropNextFree,
       "diffServRandomDropTable": diffServRandomDropTable,
       "diffServRandomDropEntry": diffServRandomDropEntry,
       "diffServRandomDropId": diffServRandomDropId,
       "diffServRandomDropMinThreshBytes": diffServRandomDropMinThreshBytes,
       "diffServRandomDropMinThreshPkts": diffServRandomDropMinThreshPkts,
       "diffServRandomDropMaxThreshBytes": diffServRandomDropMaxThreshBytes,
       "diffServRandomDropMaxThreshPkts": diffServRandomDropMaxThreshPkts,
       "diffServRandomDropProbMax": diffServRandomDropProbMax,
       "diffServRandomDropWeight": diffServRandomDropWeight,
       "diffServRandomDropSamplingRate": diffServRandomDropSamplingRate,
       "diffServRandomDropStorage": diffServRandomDropStorage,
       "diffServRandomDropStatus": diffServRandomDropStatus,
       "diffServQueue": diffServQueue,
       "diffServQNextFree": diffServQNextFree,
       "diffServQTable": diffServQTable,
       "diffServQEntry": diffServQEntry,
       "diffServQId": diffServQId,
       "diffServQNext": diffServQNext,
       "diffServQMinRate": diffServQMinRate,
       "diffServQMaxRate": diffServQMaxRate,
       "diffServQStorage": diffServQStorage,
       "diffServQStatus": diffServQStatus,
       "diffServScheduler": diffServScheduler,
       "diffServSchedulerNextFree": diffServSchedulerNextFree,
       "diffServSchedulerTable": diffServSchedulerTable,
       "diffServSchedulerEntry": diffServSchedulerEntry,
       "diffServSchedulerId": diffServSchedulerId,
       "diffServSchedulerNext": diffServSchedulerNext,
       "diffServSchedulerMethod": diffServSchedulerMethod,
       "diffServSchedulerMinRate": diffServSchedulerMinRate,
       "diffServSchedulerMaxRate": diffServSchedulerMaxRate,
       "diffServSchedulerStorage": diffServSchedulerStorage,
       "diffServSchedulerStatus": diffServSchedulerStatus,
       "diffServMinRateNextFree": diffServMinRateNextFree,
       "diffServMinRateTable": diffServMinRateTable,
       "diffServMinRateEntry": diffServMinRateEntry,
       "diffServMinRateId": diffServMinRateId,
       "diffServMinRatePriority": diffServMinRatePriority,
       "diffServMinRateAbsolute": diffServMinRateAbsolute,
       "diffServMinRateRelative": diffServMinRateRelative,
       "diffServMinRateStorage": diffServMinRateStorage,
       "diffServMinRateStatus": diffServMinRateStatus,
       "diffServMaxRateNextFree": diffServMaxRateNextFree,
       "diffServMaxRateTable": diffServMaxRateTable,
       "diffServMaxRateEntry": diffServMaxRateEntry,
       "diffServMaxRateId": diffServMaxRateId,
       "diffServMaxRateLevel": diffServMaxRateLevel,
       "diffServMaxRateAbsolute": diffServMaxRateAbsolute,
       "diffServMaxRateRelative": diffServMaxRateRelative,
       "diffServMaxRateThreshold": diffServMaxRateThreshold,
       "diffServMaxRateStorage": diffServMaxRateStorage,
       "diffServMaxRateStatus": diffServMaxRateStatus,
       "diffServMIBConformance": diffServMIBConformance,
       "diffServMIBCompliances": diffServMIBCompliances,
       "diffServMIBFullCompliance": diffServMIBFullCompliance,
       "diffServMIBReadOnlyCompliance": diffServMIBReadOnlyCompliance,
       "diffServMIBGroups": diffServMIBGroups,
       "diffServMIBDataPathGroup": diffServMIBDataPathGroup,
       "diffServMIBClfrGroup": diffServMIBClfrGroup,
       "diffServMIBClfrElementGroup": diffServMIBClfrElementGroup,
       "diffServMIBMultiFieldClfrGroup": diffServMIBMultiFieldClfrGroup,
       "diffServMIBMeterGroup": diffServMIBMeterGroup,
       "diffServMIBTBParamGroup": diffServMIBTBParamGroup,
       "diffServMIBActionGroup": diffServMIBActionGroup,
       "diffServMIBDscpMarkActGroup": diffServMIBDscpMarkActGroup,
       "diffServMIBCounterGroup": diffServMIBCounterGroup,
       "diffServMIBAlgDropGroup": diffServMIBAlgDropGroup,
       "diffServMIBRandomDropGroup": diffServMIBRandomDropGroup,
       "diffServMIBQGroup": diffServMIBQGroup,
       "diffServMIBSchedulerGroup": diffServMIBSchedulerGroup,
       "diffServMIBMinRateGroup": diffServMIBMinRateGroup,
       "diffServMIBMaxRateGroup": diffServMIBMaxRateGroup,
       "diffServMIBAdmin": diffServMIBAdmin,
       "diffServTBMeters": diffServTBMeters,
       "diffServTBParamSimpleTokenBucket": diffServTBParamSimpleTokenBucket,
       "diffServTBParamAvgRate": diffServTBParamAvgRate,
       "diffServTBParamSrTCMBlind": diffServTBParamSrTCMBlind,
       "diffServTBParamSrTCMAware": diffServTBParamSrTCMAware,
       "diffServTBParamTrTCMBlind": diffServTBParamTrTCMBlind,
       "diffServTBParamTrTCMAware": diffServTBParamTrTCMAware,
       "diffServTBParamTswTCM": diffServTBParamTswTCM,
       "diffServSchedulers": diffServSchedulers,
       "diffServSchedulerPriority": diffServSchedulerPriority,
       "diffServSchedulerWRR": diffServSchedulerWRR,
       "diffServSchedulerWFQ": diffServSchedulerWFQ}
)
