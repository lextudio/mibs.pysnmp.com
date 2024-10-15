# SNMP MIB module (FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:05 2024
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

(IfDirection,
 IndexInteger,
 IndexIntegerNextFree,
 diffServMeterEntry) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IfDirection",
    "IndexInteger",
    "IndexIntegerNextFree",
    "diffServMeterEntry")

(fastPathQOS,) = mibBuilder.importSymbols(
    "FASTPATH-QOS-MIB",
    "fastPathQOS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

fastPathQOSDiffServExtensions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6)
)
fastPathQOSDiffServExtensions.setRevisions(
        ("2007-05-23 00:00",
         "2004-06-30 00:00",
         "2003-11-21 00:00",
         "2001-11-01 09:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpPrecedence(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Cos(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class CosOrAny(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class VlanIdOrAny(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )



class EtypeOrAny(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1536, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_AgentDiffServMIBObjects_ObjectIdentity = ObjectIdentity
agentDiffServMIBObjects = _AgentDiffServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1)
)
_AgentDiffServClassifier_ObjectIdentity = ObjectIdentity
agentDiffServClassifier = _AgentDiffServClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1)
)
_AgentDiffServAuxMfClfrNextFree_Type = IndexIntegerNextFree
_AgentDiffServAuxMfClfrNextFree_Object = MibScalar
agentDiffServAuxMfClfrNextFree = _AgentDiffServAuxMfClfrNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 1),
    _AgentDiffServAuxMfClfrNextFree_Type()
)
agentDiffServAuxMfClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrNextFree.setStatus("current")
_AgentDiffServAuxMfClfrTable_Object = MibTable
agentDiffServAuxMfClfrTable = _AgentDiffServAuxMfClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrTable.setStatus("current")
_AgentDiffServAuxMfClfrEntry_Object = MibTableRow
agentDiffServAuxMfClfrEntry = _AgentDiffServAuxMfClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1)
)
agentDiffServAuxMfClfrEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServAuxMfClfrId"),
)
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrEntry.setStatus("current")
_AgentDiffServAuxMfClfrId_Type = IndexInteger
_AgentDiffServAuxMfClfrId_Object = MibTableColumn
agentDiffServAuxMfClfrId = _AgentDiffServAuxMfClfrId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 1),
    _AgentDiffServAuxMfClfrId_Type()
)
agentDiffServAuxMfClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrId.setStatus("current")
_AgentDiffServAuxMfClfrDstAddr_Type = IpAddress
_AgentDiffServAuxMfClfrDstAddr_Object = MibTableColumn
agentDiffServAuxMfClfrDstAddr = _AgentDiffServAuxMfClfrDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 2),
    _AgentDiffServAuxMfClfrDstAddr_Type()
)
agentDiffServAuxMfClfrDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstAddr.setStatus("current")


class _AgentDiffServAuxMfClfrDstMask_Type(IpAddress):
    """Custom type agentDiffServAuxMfClfrDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_AgentDiffServAuxMfClfrDstMask_Object = MibTableColumn
agentDiffServAuxMfClfrDstMask = _AgentDiffServAuxMfClfrDstMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 3),
    _AgentDiffServAuxMfClfrDstMask_Type()
)
agentDiffServAuxMfClfrDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstMask.setStatus("current")
_AgentDiffServAuxMfClfrSrcAddr_Type = IpAddress
_AgentDiffServAuxMfClfrSrcAddr_Object = MibTableColumn
agentDiffServAuxMfClfrSrcAddr = _AgentDiffServAuxMfClfrSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 4),
    _AgentDiffServAuxMfClfrSrcAddr_Type()
)
agentDiffServAuxMfClfrSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcAddr.setStatus("current")


class _AgentDiffServAuxMfClfrSrcMask_Type(IpAddress):
    """Custom type agentDiffServAuxMfClfrSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_AgentDiffServAuxMfClfrSrcMask_Object = MibTableColumn
agentDiffServAuxMfClfrSrcMask = _AgentDiffServAuxMfClfrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 5),
    _AgentDiffServAuxMfClfrSrcMask_Type()
)
agentDiffServAuxMfClfrSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcMask.setStatus("current")


class _AgentDiffServAuxMfClfrProtocol_Type(Unsigned32):
    """Custom type agentDiffServAuxMfClfrProtocol based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDiffServAuxMfClfrProtocol_Type.__name__ = "Unsigned32"
_AgentDiffServAuxMfClfrProtocol_Object = MibTableColumn
agentDiffServAuxMfClfrProtocol = _AgentDiffServAuxMfClfrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 6),
    _AgentDiffServAuxMfClfrProtocol_Type()
)
agentDiffServAuxMfClfrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrProtocol.setStatus("current")


class _AgentDiffServAuxMfClfrDstL4PortMin_Type(InetPortNumber):
    """Custom type agentDiffServAuxMfClfrDstL4PortMin based on InetPortNumber"""
    defaultValue = 0


_AgentDiffServAuxMfClfrDstL4PortMin_Object = MibTableColumn
agentDiffServAuxMfClfrDstL4PortMin = _AgentDiffServAuxMfClfrDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 7),
    _AgentDiffServAuxMfClfrDstL4PortMin_Type()
)
agentDiffServAuxMfClfrDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstL4PortMin.setStatus("current")


class _AgentDiffServAuxMfClfrDstL4PortMax_Type(InetPortNumber):
    """Custom type agentDiffServAuxMfClfrDstL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_AgentDiffServAuxMfClfrDstL4PortMax_Object = MibTableColumn
agentDiffServAuxMfClfrDstL4PortMax = _AgentDiffServAuxMfClfrDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 8),
    _AgentDiffServAuxMfClfrDstL4PortMax_Type()
)
agentDiffServAuxMfClfrDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstL4PortMax.setStatus("current")


class _AgentDiffServAuxMfClfrSrcL4PortMin_Type(InetPortNumber):
    """Custom type agentDiffServAuxMfClfrSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_AgentDiffServAuxMfClfrSrcL4PortMin_Object = MibTableColumn
agentDiffServAuxMfClfrSrcL4PortMin = _AgentDiffServAuxMfClfrSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 9),
    _AgentDiffServAuxMfClfrSrcL4PortMin_Type()
)
agentDiffServAuxMfClfrSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcL4PortMin.setStatus("current")


class _AgentDiffServAuxMfClfrSrcL4PortMax_Type(InetPortNumber):
    """Custom type agentDiffServAuxMfClfrSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_AgentDiffServAuxMfClfrSrcL4PortMax_Object = MibTableColumn
agentDiffServAuxMfClfrSrcL4PortMax = _AgentDiffServAuxMfClfrSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 10),
    _AgentDiffServAuxMfClfrSrcL4PortMax_Type()
)
agentDiffServAuxMfClfrSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcL4PortMax.setStatus("current")


class _AgentDiffServAuxMfClfrCos_Type(CosOrAny):
    """Custom type agentDiffServAuxMfClfrCos based on CosOrAny"""
    defaultValue = -1


_AgentDiffServAuxMfClfrCos_Object = MibTableColumn
agentDiffServAuxMfClfrCos = _AgentDiffServAuxMfClfrCos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 11),
    _AgentDiffServAuxMfClfrCos_Type()
)
agentDiffServAuxMfClfrCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrCos.setStatus("current")


class _AgentDiffServAuxMfClfrTos_Type(OctetString):
    """Custom type agentDiffServAuxMfClfrTos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AgentDiffServAuxMfClfrTos_Type.__name__ = "OctetString"
_AgentDiffServAuxMfClfrTos_Object = MibTableColumn
agentDiffServAuxMfClfrTos = _AgentDiffServAuxMfClfrTos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 12),
    _AgentDiffServAuxMfClfrTos_Type()
)
agentDiffServAuxMfClfrTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrTos.setStatus("current")


class _AgentDiffServAuxMfClfrTosMask_Type(OctetString):
    """Custom type agentDiffServAuxMfClfrTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AgentDiffServAuxMfClfrTosMask_Type.__name__ = "OctetString"
_AgentDiffServAuxMfClfrTosMask_Object = MibTableColumn
agentDiffServAuxMfClfrTosMask = _AgentDiffServAuxMfClfrTosMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 13),
    _AgentDiffServAuxMfClfrTosMask_Type()
)
agentDiffServAuxMfClfrTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrTosMask.setStatus("current")
_AgentDiffServAuxMfClfrDstMac_Type = MacAddress
_AgentDiffServAuxMfClfrDstMac_Object = MibTableColumn
agentDiffServAuxMfClfrDstMac = _AgentDiffServAuxMfClfrDstMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 14),
    _AgentDiffServAuxMfClfrDstMac_Type()
)
agentDiffServAuxMfClfrDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstMac.setStatus("current")
_AgentDiffServAuxMfClfrDstMacMask_Type = MacAddress
_AgentDiffServAuxMfClfrDstMacMask_Object = MibTableColumn
agentDiffServAuxMfClfrDstMacMask = _AgentDiffServAuxMfClfrDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 15),
    _AgentDiffServAuxMfClfrDstMacMask_Type()
)
agentDiffServAuxMfClfrDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstMacMask.setStatus("current")
_AgentDiffServAuxMfClfrSrcMac_Type = MacAddress
_AgentDiffServAuxMfClfrSrcMac_Object = MibTableColumn
agentDiffServAuxMfClfrSrcMac = _AgentDiffServAuxMfClfrSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 16),
    _AgentDiffServAuxMfClfrSrcMac_Type()
)
agentDiffServAuxMfClfrSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcMac.setStatus("current")
_AgentDiffServAuxMfClfrSrcMacMask_Type = MacAddress
_AgentDiffServAuxMfClfrSrcMacMask_Object = MibTableColumn
agentDiffServAuxMfClfrSrcMacMask = _AgentDiffServAuxMfClfrSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 17),
    _AgentDiffServAuxMfClfrSrcMacMask_Type()
)
agentDiffServAuxMfClfrSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcMacMask.setStatus("current")


class _AgentDiffServAuxMfClfrVlanId_Type(VlanIdOrAny):
    """Custom type agentDiffServAuxMfClfrVlanId based on VlanIdOrAny"""
    defaultValue = -1


_AgentDiffServAuxMfClfrVlanId_Object = MibTableColumn
agentDiffServAuxMfClfrVlanId = _AgentDiffServAuxMfClfrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 18),
    _AgentDiffServAuxMfClfrVlanId_Type()
)
agentDiffServAuxMfClfrVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrVlanId.setStatus("obsolete")


class _AgentDiffServAuxMfClfrStorage_Type(StorageType):
    """Custom type agentDiffServAuxMfClfrStorage based on StorageType"""


_AgentDiffServAuxMfClfrStorage_Object = MibTableColumn
agentDiffServAuxMfClfrStorage = _AgentDiffServAuxMfClfrStorage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 19),
    _AgentDiffServAuxMfClfrStorage_Type()
)
agentDiffServAuxMfClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrStorage.setStatus("current")
_AgentDiffServAuxMfClfrStatus_Type = RowStatus
_AgentDiffServAuxMfClfrStatus_Object = MibTableColumn
agentDiffServAuxMfClfrStatus = _AgentDiffServAuxMfClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 20),
    _AgentDiffServAuxMfClfrStatus_Type()
)
agentDiffServAuxMfClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrStatus.setStatus("current")


class _AgentDiffServAuxMfClfrCos2_Type(CosOrAny):
    """Custom type agentDiffServAuxMfClfrCos2 based on CosOrAny"""
    defaultValue = -1


_AgentDiffServAuxMfClfrCos2_Object = MibTableColumn
agentDiffServAuxMfClfrCos2 = _AgentDiffServAuxMfClfrCos2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 21),
    _AgentDiffServAuxMfClfrCos2_Type()
)
agentDiffServAuxMfClfrCos2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrCos2.setStatus("current")


class _AgentDiffServAuxMfClfrEtypeVal1_Type(EtypeOrAny):
    """Custom type agentDiffServAuxMfClfrEtypeVal1 based on EtypeOrAny"""
    defaultValue = 0


_AgentDiffServAuxMfClfrEtypeVal1_Object = MibTableColumn
agentDiffServAuxMfClfrEtypeVal1 = _AgentDiffServAuxMfClfrEtypeVal1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 22),
    _AgentDiffServAuxMfClfrEtypeVal1_Type()
)
agentDiffServAuxMfClfrEtypeVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrEtypeVal1.setStatus("current")


class _AgentDiffServAuxMfClfrEtypeVal2_Type(EtypeOrAny):
    """Custom type agentDiffServAuxMfClfrEtypeVal2 based on EtypeOrAny"""
    defaultValue = 0


_AgentDiffServAuxMfClfrEtypeVal2_Object = MibTableColumn
agentDiffServAuxMfClfrEtypeVal2 = _AgentDiffServAuxMfClfrEtypeVal2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 23),
    _AgentDiffServAuxMfClfrEtypeVal2_Type()
)
agentDiffServAuxMfClfrEtypeVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrEtypeVal2.setStatus("current")


class _AgentDiffServAuxMfClfrVlanIdMin_Type(Unsigned32):
    """Custom type agentDiffServAuxMfClfrVlanIdMin based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentDiffServAuxMfClfrVlanIdMin_Type.__name__ = "Unsigned32"
_AgentDiffServAuxMfClfrVlanIdMin_Object = MibTableColumn
agentDiffServAuxMfClfrVlanIdMin = _AgentDiffServAuxMfClfrVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 24),
    _AgentDiffServAuxMfClfrVlanIdMin_Type()
)
agentDiffServAuxMfClfrVlanIdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrVlanIdMin.setStatus("current")


class _AgentDiffServAuxMfClfrVlanIdMax_Type(Unsigned32):
    """Custom type agentDiffServAuxMfClfrVlanIdMax based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentDiffServAuxMfClfrVlanIdMax_Type.__name__ = "Unsigned32"
_AgentDiffServAuxMfClfrVlanIdMax_Object = MibTableColumn
agentDiffServAuxMfClfrVlanIdMax = _AgentDiffServAuxMfClfrVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 25),
    _AgentDiffServAuxMfClfrVlanIdMax_Type()
)
agentDiffServAuxMfClfrVlanIdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrVlanIdMax.setStatus("current")


class _AgentDiffServAuxMfClfrVlanId2Min_Type(Unsigned32):
    """Custom type agentDiffServAuxMfClfrVlanId2Min based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentDiffServAuxMfClfrVlanId2Min_Type.__name__ = "Unsigned32"
_AgentDiffServAuxMfClfrVlanId2Min_Object = MibTableColumn
agentDiffServAuxMfClfrVlanId2Min = _AgentDiffServAuxMfClfrVlanId2Min_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 26),
    _AgentDiffServAuxMfClfrVlanId2Min_Type()
)
agentDiffServAuxMfClfrVlanId2Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrVlanId2Min.setStatus("current")


class _AgentDiffServAuxMfClfrVlanId2Max_Type(Unsigned32):
    """Custom type agentDiffServAuxMfClfrVlanId2Max based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentDiffServAuxMfClfrVlanId2Max_Type.__name__ = "Unsigned32"
_AgentDiffServAuxMfClfrVlanId2Max_Object = MibTableColumn
agentDiffServAuxMfClfrVlanId2Max = _AgentDiffServAuxMfClfrVlanId2Max_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 27),
    _AgentDiffServAuxMfClfrVlanId2Max_Type()
)
agentDiffServAuxMfClfrVlanId2Max.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrVlanId2Max.setStatus("current")
_AgentDiffServAction_ObjectIdentity = ObjectIdentity
agentDiffServAction = _AgentDiffServAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2)
)
_AgentDiffServCosMarkActTable_Object = MibTable
agentDiffServCosMarkActTable = _AgentDiffServCosMarkActTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    agentDiffServCosMarkActTable.setStatus("current")
_AgentDiffServCosMarkActEntry_Object = MibTableRow
agentDiffServCosMarkActEntry = _AgentDiffServCosMarkActEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 2, 1)
)
agentDiffServCosMarkActEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServCosMarkActCos"),
)
if mibBuilder.loadTexts:
    agentDiffServCosMarkActEntry.setStatus("current")
_AgentDiffServCosMarkActCos_Type = Cos
_AgentDiffServCosMarkActCos_Object = MibTableColumn
agentDiffServCosMarkActCos = _AgentDiffServCosMarkActCos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 2, 1, 1),
    _AgentDiffServCosMarkActCos_Type()
)
agentDiffServCosMarkActCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServCosMarkActCos.setStatus("current")
_AgentDiffServIpPrecMarkActTable_Object = MibTable
agentDiffServIpPrecMarkActTable = _AgentDiffServIpPrecMarkActTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    agentDiffServIpPrecMarkActTable.setStatus("current")
_AgentDiffServIpPrecMarkActEntry_Object = MibTableRow
agentDiffServIpPrecMarkActEntry = _AgentDiffServIpPrecMarkActEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 4, 1)
)
agentDiffServIpPrecMarkActEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServIpPrecMarkActPrecedence"),
)
if mibBuilder.loadTexts:
    agentDiffServIpPrecMarkActEntry.setStatus("current")
_AgentDiffServIpPrecMarkActPrecedence_Type = IpPrecedence
_AgentDiffServIpPrecMarkActPrecedence_Object = MibTableColumn
agentDiffServIpPrecMarkActPrecedence = _AgentDiffServIpPrecMarkActPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 4, 1, 1),
    _AgentDiffServIpPrecMarkActPrecedence_Type()
)
agentDiffServIpPrecMarkActPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServIpPrecMarkActPrecedence.setStatus("current")
_AgentDiffServCos2MarkActTable_Object = MibTable
agentDiffServCos2MarkActTable = _AgentDiffServCos2MarkActTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 5)
)
if mibBuilder.loadTexts:
    agentDiffServCos2MarkActTable.setStatus("current")
_AgentDiffServCos2MarkActEntry_Object = MibTableRow
agentDiffServCos2MarkActEntry = _AgentDiffServCos2MarkActEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 5, 1)
)
agentDiffServCos2MarkActEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServCos2MarkActCos"),
)
if mibBuilder.loadTexts:
    agentDiffServCos2MarkActEntry.setStatus("current")
_AgentDiffServCos2MarkActCos_Type = Cos
_AgentDiffServCos2MarkActCos_Object = MibTableColumn
agentDiffServCos2MarkActCos = _AgentDiffServCos2MarkActCos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 5, 1, 1),
    _AgentDiffServCos2MarkActCos_Type()
)
agentDiffServCos2MarkActCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServCos2MarkActCos.setStatus("current")
_AgentDiffServAssignQueueNextFree_Type = IndexIntegerNextFree
_AgentDiffServAssignQueueNextFree_Object = MibScalar
agentDiffServAssignQueueNextFree = _AgentDiffServAssignQueueNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 6),
    _AgentDiffServAssignQueueNextFree_Type()
)
agentDiffServAssignQueueNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServAssignQueueNextFree.setStatus("current")
_AgentDiffServAssignQueueTable_Object = MibTable
agentDiffServAssignQueueTable = _AgentDiffServAssignQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7)
)
if mibBuilder.loadTexts:
    agentDiffServAssignQueueTable.setStatus("current")
_AgentDiffServAssignQueueEntry_Object = MibTableRow
agentDiffServAssignQueueEntry = _AgentDiffServAssignQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1)
)
agentDiffServAssignQueueEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServAssignQueueIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServAssignQueueEntry.setStatus("current")
_AgentDiffServAssignQueueIndex_Type = IndexInteger
_AgentDiffServAssignQueueIndex_Object = MibTableColumn
agentDiffServAssignQueueIndex = _AgentDiffServAssignQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 1),
    _AgentDiffServAssignQueueIndex_Type()
)
agentDiffServAssignQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServAssignQueueIndex.setStatus("current")


class _AgentDiffServAssignQueueQnum_Type(Unsigned32):
    """Custom type agentDiffServAssignQueueQnum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServAssignQueueQnum_Type.__name__ = "Unsigned32"
_AgentDiffServAssignQueueQnum_Object = MibTableColumn
agentDiffServAssignQueueQnum = _AgentDiffServAssignQueueQnum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 2),
    _AgentDiffServAssignQueueQnum_Type()
)
agentDiffServAssignQueueQnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAssignQueueQnum.setStatus("current")


class _AgentDiffServAssignQueueStorage_Type(StorageType):
    """Custom type agentDiffServAssignQueueStorage based on StorageType"""


_AgentDiffServAssignQueueStorage_Object = MibTableColumn
agentDiffServAssignQueueStorage = _AgentDiffServAssignQueueStorage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 3),
    _AgentDiffServAssignQueueStorage_Type()
)
agentDiffServAssignQueueStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAssignQueueStorage.setStatus("current")
_AgentDiffServAssignQueueStatus_Type = RowStatus
_AgentDiffServAssignQueueStatus_Object = MibTableColumn
agentDiffServAssignQueueStatus = _AgentDiffServAssignQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 4),
    _AgentDiffServAssignQueueStatus_Type()
)
agentDiffServAssignQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAssignQueueStatus.setStatus("current")
_AgentDiffServRedirectNextFree_Type = IndexIntegerNextFree
_AgentDiffServRedirectNextFree_Object = MibScalar
agentDiffServRedirectNextFree = _AgentDiffServRedirectNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 8),
    _AgentDiffServRedirectNextFree_Type()
)
agentDiffServRedirectNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServRedirectNextFree.setStatus("current")
_AgentDiffServRedirectTable_Object = MibTable
agentDiffServRedirectTable = _AgentDiffServRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9)
)
if mibBuilder.loadTexts:
    agentDiffServRedirectTable.setStatus("current")
_AgentDiffServRedirectEntry_Object = MibTableRow
agentDiffServRedirectEntry = _AgentDiffServRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1)
)
agentDiffServRedirectEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServRedirectId"),
)
if mibBuilder.loadTexts:
    agentDiffServRedirectEntry.setStatus("current")
_AgentDiffServRedirectId_Type = IndexInteger
_AgentDiffServRedirectId_Object = MibTableColumn
agentDiffServRedirectId = _AgentDiffServRedirectId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 1),
    _AgentDiffServRedirectId_Type()
)
agentDiffServRedirectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServRedirectId.setStatus("current")
_AgentDiffServRedirectIntf_Type = InterfaceIndex
_AgentDiffServRedirectIntf_Object = MibTableColumn
agentDiffServRedirectIntf = _AgentDiffServRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 2),
    _AgentDiffServRedirectIntf_Type()
)
agentDiffServRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServRedirectIntf.setStatus("current")


class _AgentDiffServRedirectStorage_Type(StorageType):
    """Custom type agentDiffServRedirectStorage based on StorageType"""


_AgentDiffServRedirectStorage_Object = MibTableColumn
agentDiffServRedirectStorage = _AgentDiffServRedirectStorage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 3),
    _AgentDiffServRedirectStorage_Type()
)
agentDiffServRedirectStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServRedirectStorage.setStatus("current")
_AgentDiffServRedirectStatus_Type = RowStatus
_AgentDiffServRedirectStatus_Object = MibTableColumn
agentDiffServRedirectStatus = _AgentDiffServRedirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 4),
    _AgentDiffServRedirectStatus_Type()
)
agentDiffServRedirectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServRedirectStatus.setStatus("current")
_AgentDiffServMirrorNextFree_Type = IndexIntegerNextFree
_AgentDiffServMirrorNextFree_Object = MibScalar
agentDiffServMirrorNextFree = _AgentDiffServMirrorNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 10),
    _AgentDiffServMirrorNextFree_Type()
)
agentDiffServMirrorNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServMirrorNextFree.setStatus("current")
_AgentDiffServMirrorTable_Object = MibTable
agentDiffServMirrorTable = _AgentDiffServMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11)
)
if mibBuilder.loadTexts:
    agentDiffServMirrorTable.setStatus("current")
_AgentDiffServMirrorEntry_Object = MibTableRow
agentDiffServMirrorEntry = _AgentDiffServMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1)
)
agentDiffServMirrorEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServMirrorId"),
)
if mibBuilder.loadTexts:
    agentDiffServMirrorEntry.setStatus("current")
_AgentDiffServMirrorId_Type = IndexInteger
_AgentDiffServMirrorId_Object = MibTableColumn
agentDiffServMirrorId = _AgentDiffServMirrorId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 1),
    _AgentDiffServMirrorId_Type()
)
agentDiffServMirrorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServMirrorId.setStatus("current")
_AgentDiffServMirrorIntf_Type = InterfaceIndex
_AgentDiffServMirrorIntf_Object = MibTableColumn
agentDiffServMirrorIntf = _AgentDiffServMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 2),
    _AgentDiffServMirrorIntf_Type()
)
agentDiffServMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServMirrorIntf.setStatus("current")


class _AgentDiffServMirrorStorage_Type(StorageType):
    """Custom type agentDiffServMirrorStorage based on StorageType"""


_AgentDiffServMirrorStorage_Object = MibTableColumn
agentDiffServMirrorStorage = _AgentDiffServMirrorStorage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 3),
    _AgentDiffServMirrorStorage_Type()
)
agentDiffServMirrorStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServMirrorStorage.setStatus("current")
_AgentDiffServMirrorStatus_Type = RowStatus
_AgentDiffServMirrorStatus_Object = MibTableColumn
agentDiffServMirrorStatus = _AgentDiffServMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 4),
    _AgentDiffServMirrorStatus_Type()
)
agentDiffServMirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServMirrorStatus.setStatus("current")
_AgentDiffServMeter_ObjectIdentity = ObjectIdentity
agentDiffServMeter = _AgentDiffServMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3)
)
_AgentDiffServColorAwareTable_Object = MibTable
agentDiffServColorAwareTable = _AgentDiffServColorAwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    agentDiffServColorAwareTable.setStatus("current")
_AgentDiffServColorAwareEntry_Object = MibTableRow
agentDiffServColorAwareEntry = _AgentDiffServColorAwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    agentDiffServColorAwareEntry.setStatus("current")


class _AgentDiffServColorAwareLevel_Type(Integer32):
    """Custom type agentDiffServColorAwareLevel based on Integer32"""
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
        *(("conform", 1),
          ("exceed", 2),
          ("unused", 3))
    )


_AgentDiffServColorAwareLevel_Type.__name__ = "Integer32"
_AgentDiffServColorAwareLevel_Object = MibTableColumn
agentDiffServColorAwareLevel = _AgentDiffServColorAwareLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1, 1),
    _AgentDiffServColorAwareLevel_Type()
)
agentDiffServColorAwareLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServColorAwareLevel.setStatus("current")


class _AgentDiffServColorAwareMode_Type(Integer32):
    """Custom type agentDiffServColorAwareMode based on Integer32"""
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
        *(("awarecos", 2),
          ("awarecos2", 3),
          ("awareipdscp", 4),
          ("awareipprec", 5),
          ("awareunused", 6),
          ("blind", 1))
    )


_AgentDiffServColorAwareMode_Type.__name__ = "Integer32"
_AgentDiffServColorAwareMode_Object = MibTableColumn
agentDiffServColorAwareMode = _AgentDiffServColorAwareMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1, 2),
    _AgentDiffServColorAwareMode_Type()
)
agentDiffServColorAwareMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServColorAwareMode.setStatus("current")


class _AgentDiffServColorAwareValue_Type(Unsigned32):
    """Custom type agentDiffServColorAwareValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentDiffServColorAwareValue_Type.__name__ = "Unsigned32"
_AgentDiffServColorAwareValue_Object = MibTableColumn
agentDiffServColorAwareValue = _AgentDiffServColorAwareValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1, 3),
    _AgentDiffServColorAwareValue_Type()
)
agentDiffServColorAwareValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServColorAwareValue.setStatus("current")
_AgentDiffServMIBAdmin_ObjectIdentity = ObjectIdentity
agentDiffServMIBAdmin = _AgentDiffServMIBAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 2)
)
_AgentDiffServTBMeters_ObjectIdentity = ObjectIdentity
agentDiffServTBMeters = _AgentDiffServTBMeters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 2, 1)
)
_AgentDiffServTBParamSimpleTokenBucketAware_ObjectIdentity = ObjectIdentity
agentDiffServTBParamSimpleTokenBucketAware = _AgentDiffServTBParamSimpleTokenBucketAware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentDiffServTBParamSimpleTokenBucketAware.setStatus("current")
diffServMeterEntry.registerAugmentions(
    ("FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB",
     "agentDiffServColorAwareEntry")
)
agentDiffServColorAwareEntry.setIndexNames(*diffServMeterEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB",
    **{"IpPrecedence": IpPrecedence,
       "Cos": Cos,
       "CosOrAny": CosOrAny,
       "VlanIdOrAny": VlanIdOrAny,
       "EtypeOrAny": EtypeOrAny,
       "fastPathQOSDiffServExtensions": fastPathQOSDiffServExtensions,
       "agentDiffServMIBObjects": agentDiffServMIBObjects,
       "agentDiffServClassifier": agentDiffServClassifier,
       "agentDiffServAuxMfClfrNextFree": agentDiffServAuxMfClfrNextFree,
       "agentDiffServAuxMfClfrTable": agentDiffServAuxMfClfrTable,
       "agentDiffServAuxMfClfrEntry": agentDiffServAuxMfClfrEntry,
       "agentDiffServAuxMfClfrId": agentDiffServAuxMfClfrId,
       "agentDiffServAuxMfClfrDstAddr": agentDiffServAuxMfClfrDstAddr,
       "agentDiffServAuxMfClfrDstMask": agentDiffServAuxMfClfrDstMask,
       "agentDiffServAuxMfClfrSrcAddr": agentDiffServAuxMfClfrSrcAddr,
       "agentDiffServAuxMfClfrSrcMask": agentDiffServAuxMfClfrSrcMask,
       "agentDiffServAuxMfClfrProtocol": agentDiffServAuxMfClfrProtocol,
       "agentDiffServAuxMfClfrDstL4PortMin": agentDiffServAuxMfClfrDstL4PortMin,
       "agentDiffServAuxMfClfrDstL4PortMax": agentDiffServAuxMfClfrDstL4PortMax,
       "agentDiffServAuxMfClfrSrcL4PortMin": agentDiffServAuxMfClfrSrcL4PortMin,
       "agentDiffServAuxMfClfrSrcL4PortMax": agentDiffServAuxMfClfrSrcL4PortMax,
       "agentDiffServAuxMfClfrCos": agentDiffServAuxMfClfrCos,
       "agentDiffServAuxMfClfrTos": agentDiffServAuxMfClfrTos,
       "agentDiffServAuxMfClfrTosMask": agentDiffServAuxMfClfrTosMask,
       "agentDiffServAuxMfClfrDstMac": agentDiffServAuxMfClfrDstMac,
       "agentDiffServAuxMfClfrDstMacMask": agentDiffServAuxMfClfrDstMacMask,
       "agentDiffServAuxMfClfrSrcMac": agentDiffServAuxMfClfrSrcMac,
       "agentDiffServAuxMfClfrSrcMacMask": agentDiffServAuxMfClfrSrcMacMask,
       "agentDiffServAuxMfClfrVlanId": agentDiffServAuxMfClfrVlanId,
       "agentDiffServAuxMfClfrStorage": agentDiffServAuxMfClfrStorage,
       "agentDiffServAuxMfClfrStatus": agentDiffServAuxMfClfrStatus,
       "agentDiffServAuxMfClfrCos2": agentDiffServAuxMfClfrCos2,
       "agentDiffServAuxMfClfrEtypeVal1": agentDiffServAuxMfClfrEtypeVal1,
       "agentDiffServAuxMfClfrEtypeVal2": agentDiffServAuxMfClfrEtypeVal2,
       "agentDiffServAuxMfClfrVlanIdMin": agentDiffServAuxMfClfrVlanIdMin,
       "agentDiffServAuxMfClfrVlanIdMax": agentDiffServAuxMfClfrVlanIdMax,
       "agentDiffServAuxMfClfrVlanId2Min": agentDiffServAuxMfClfrVlanId2Min,
       "agentDiffServAuxMfClfrVlanId2Max": agentDiffServAuxMfClfrVlanId2Max,
       "agentDiffServAction": agentDiffServAction,
       "agentDiffServCosMarkActTable": agentDiffServCosMarkActTable,
       "agentDiffServCosMarkActEntry": agentDiffServCosMarkActEntry,
       "agentDiffServCosMarkActCos": agentDiffServCosMarkActCos,
       "agentDiffServIpPrecMarkActTable": agentDiffServIpPrecMarkActTable,
       "agentDiffServIpPrecMarkActEntry": agentDiffServIpPrecMarkActEntry,
       "agentDiffServIpPrecMarkActPrecedence": agentDiffServIpPrecMarkActPrecedence,
       "agentDiffServCos2MarkActTable": agentDiffServCos2MarkActTable,
       "agentDiffServCos2MarkActEntry": agentDiffServCos2MarkActEntry,
       "agentDiffServCos2MarkActCos": agentDiffServCos2MarkActCos,
       "agentDiffServAssignQueueNextFree": agentDiffServAssignQueueNextFree,
       "agentDiffServAssignQueueTable": agentDiffServAssignQueueTable,
       "agentDiffServAssignQueueEntry": agentDiffServAssignQueueEntry,
       "agentDiffServAssignQueueIndex": agentDiffServAssignQueueIndex,
       "agentDiffServAssignQueueQnum": agentDiffServAssignQueueQnum,
       "agentDiffServAssignQueueStorage": agentDiffServAssignQueueStorage,
       "agentDiffServAssignQueueStatus": agentDiffServAssignQueueStatus,
       "agentDiffServRedirectNextFree": agentDiffServRedirectNextFree,
       "agentDiffServRedirectTable": agentDiffServRedirectTable,
       "agentDiffServRedirectEntry": agentDiffServRedirectEntry,
       "agentDiffServRedirectId": agentDiffServRedirectId,
       "agentDiffServRedirectIntf": agentDiffServRedirectIntf,
       "agentDiffServRedirectStorage": agentDiffServRedirectStorage,
       "agentDiffServRedirectStatus": agentDiffServRedirectStatus,
       "agentDiffServMirrorNextFree": agentDiffServMirrorNextFree,
       "agentDiffServMirrorTable": agentDiffServMirrorTable,
       "agentDiffServMirrorEntry": agentDiffServMirrorEntry,
       "agentDiffServMirrorId": agentDiffServMirrorId,
       "agentDiffServMirrorIntf": agentDiffServMirrorIntf,
       "agentDiffServMirrorStorage": agentDiffServMirrorStorage,
       "agentDiffServMirrorStatus": agentDiffServMirrorStatus,
       "agentDiffServMeter": agentDiffServMeter,
       "agentDiffServColorAwareTable": agentDiffServColorAwareTable,
       "agentDiffServColorAwareEntry": agentDiffServColorAwareEntry,
       "agentDiffServColorAwareLevel": agentDiffServColorAwareLevel,
       "agentDiffServColorAwareMode": agentDiffServColorAwareMode,
       "agentDiffServColorAwareValue": agentDiffServColorAwareValue,
       "agentDiffServMIBAdmin": agentDiffServMIBAdmin,
       "agentDiffServTBMeters": agentDiffServTBMeters,
       "agentDiffServTBParamSimpleTokenBucketAware": agentDiffServTBParamSimpleTokenBucketAware}
)
