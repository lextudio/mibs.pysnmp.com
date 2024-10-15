# SNMP MIB module (FSM7326-QOS-DIFFSERV-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSM7326-QOS-DIFFSERV-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:34 2024
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
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IfDirection",
    "IndexInteger",
    "IndexIntegerNextFree")

(fsm7326QOS,) = mibBuilder.importSymbols(
    "FSM7326-QOS-MIB",
    "fsm7326QOS")

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

fsm7326QOSDiffServExtensions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3)
)
fsm7326QOSDiffServExtensions.setRevisions(
        ("2003-11-10 12:00",)
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



# MIB Managed Objects in the order of their OIDs

_AgentDiffServMIBObjects_ObjectIdentity = ObjectIdentity
agentDiffServMIBObjects = _AgentDiffServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1)
)
_AgentDiffServClassifier_ObjectIdentity = ObjectIdentity
agentDiffServClassifier = _AgentDiffServClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1)
)
_AgentDiffServAuxMfClfrNextFree_Type = IndexIntegerNextFree
_AgentDiffServAuxMfClfrNextFree_Object = MibScalar
agentDiffServAuxMfClfrNextFree = _AgentDiffServAuxMfClfrNextFree_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 1),
    _AgentDiffServAuxMfClfrNextFree_Type()
)
agentDiffServAuxMfClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrNextFree.setStatus("current")
_AgentDiffServAuxMfClfrTable_Object = MibTable
agentDiffServAuxMfClfrTable = _AgentDiffServAuxMfClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrTable.setStatus("current")
_AgentDiffServAuxMfClfrEntry_Object = MibTableRow
agentDiffServAuxMfClfrEntry = _AgentDiffServAuxMfClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1)
)
agentDiffServAuxMfClfrEntry.setIndexNames(
    (0, "FSM7326-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServAuxMfClfrId"),
)
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrEntry.setStatus("current")
_AgentDiffServAuxMfClfrId_Type = IndexInteger
_AgentDiffServAuxMfClfrId_Object = MibTableColumn
agentDiffServAuxMfClfrId = _AgentDiffServAuxMfClfrId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 1),
    _AgentDiffServAuxMfClfrId_Type()
)
agentDiffServAuxMfClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrId.setStatus("current")
_AgentDiffServAuxMfClfrDstAddr_Type = IpAddress
_AgentDiffServAuxMfClfrDstAddr_Object = MibTableColumn
agentDiffServAuxMfClfrDstAddr = _AgentDiffServAuxMfClfrDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 2),
    _AgentDiffServAuxMfClfrDstAddr_Type()
)
agentDiffServAuxMfClfrDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstAddr.setStatus("current")


class _AgentDiffServAuxMfClfrDstMask_Type(IpAddress):
    """Custom type agentDiffServAuxMfClfrDstMask based on IpAddress"""
    defaultValue = 0


_AgentDiffServAuxMfClfrDstMask_Object = MibTableColumn
agentDiffServAuxMfClfrDstMask = _AgentDiffServAuxMfClfrDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 3),
    _AgentDiffServAuxMfClfrDstMask_Type()
)
agentDiffServAuxMfClfrDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstMask.setStatus("current")
_AgentDiffServAuxMfClfrSrcAddr_Type = IpAddress
_AgentDiffServAuxMfClfrSrcAddr_Object = MibTableColumn
agentDiffServAuxMfClfrSrcAddr = _AgentDiffServAuxMfClfrSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 4),
    _AgentDiffServAuxMfClfrSrcAddr_Type()
)
agentDiffServAuxMfClfrSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcAddr.setStatus("current")


class _AgentDiffServAuxMfClfrSrcMask_Type(IpAddress):
    """Custom type agentDiffServAuxMfClfrSrcMask based on IpAddress"""
    defaultValue = 0


_AgentDiffServAuxMfClfrSrcMask_Object = MibTableColumn
agentDiffServAuxMfClfrSrcMask = _AgentDiffServAuxMfClfrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 12),
    _AgentDiffServAuxMfClfrTos_Type()
)
agentDiffServAuxMfClfrTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrTos.setStatus("current")


class _AgentDiffServAuxMfClfrTosMask_Type(OctetString):
    """Custom type agentDiffServAuxMfClfrTosMask based on OctetString"""
    defaultValue = 0

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AgentDiffServAuxMfClfrTosMask_Type.__name__ = "OctetString"
_AgentDiffServAuxMfClfrTosMask_Object = MibTableColumn
agentDiffServAuxMfClfrTosMask = _AgentDiffServAuxMfClfrTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 13),
    _AgentDiffServAuxMfClfrTosMask_Type()
)
agentDiffServAuxMfClfrTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrTosMask.setStatus("current")
_AgentDiffServAuxMfClfrDstMac_Type = MacAddress
_AgentDiffServAuxMfClfrDstMac_Object = MibTableColumn
agentDiffServAuxMfClfrDstMac = _AgentDiffServAuxMfClfrDstMac_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 14),
    _AgentDiffServAuxMfClfrDstMac_Type()
)
agentDiffServAuxMfClfrDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstMac.setStatus("current")


class _AgentDiffServAuxMfClfrDstMacMask_Type(MacAddress):
    """Custom type agentDiffServAuxMfClfrDstMacMask based on MacAddress"""
    defaultValue = 0


_AgentDiffServAuxMfClfrDstMacMask_Object = MibTableColumn
agentDiffServAuxMfClfrDstMacMask = _AgentDiffServAuxMfClfrDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 15),
    _AgentDiffServAuxMfClfrDstMacMask_Type()
)
agentDiffServAuxMfClfrDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrDstMacMask.setStatus("current")
_AgentDiffServAuxMfClfrSrcMac_Type = MacAddress
_AgentDiffServAuxMfClfrSrcMac_Object = MibTableColumn
agentDiffServAuxMfClfrSrcMac = _AgentDiffServAuxMfClfrSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 16),
    _AgentDiffServAuxMfClfrSrcMac_Type()
)
agentDiffServAuxMfClfrSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrSrcMac.setStatus("current")


class _AgentDiffServAuxMfClfrSrcMacMask_Type(MacAddress):
    """Custom type agentDiffServAuxMfClfrSrcMacMask based on MacAddress"""
    defaultValue = 0


_AgentDiffServAuxMfClfrSrcMacMask_Object = MibTableColumn
agentDiffServAuxMfClfrSrcMacMask = _AgentDiffServAuxMfClfrSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 18),
    _AgentDiffServAuxMfClfrVlanId_Type()
)
agentDiffServAuxMfClfrVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrVlanId.setStatus("current")


class _AgentDiffServAuxMfClfrStorage_Type(StorageType):
    """Custom type agentDiffServAuxMfClfrStorage based on StorageType"""


_AgentDiffServAuxMfClfrStorage_Object = MibTableColumn
agentDiffServAuxMfClfrStorage = _AgentDiffServAuxMfClfrStorage_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 19),
    _AgentDiffServAuxMfClfrStorage_Type()
)
agentDiffServAuxMfClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrStorage.setStatus("current")
_AgentDiffServAuxMfClfrStatus_Type = RowStatus
_AgentDiffServAuxMfClfrStatus_Object = MibTableColumn
agentDiffServAuxMfClfrStatus = _AgentDiffServAuxMfClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 1, 2, 1, 20),
    _AgentDiffServAuxMfClfrStatus_Type()
)
agentDiffServAuxMfClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServAuxMfClfrStatus.setStatus("current")
_AgentDiffServAction_ObjectIdentity = ObjectIdentity
agentDiffServAction = _AgentDiffServAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2)
)
_AgentDiffServCosMarkActTable_Object = MibTable
agentDiffServCosMarkActTable = _AgentDiffServCosMarkActTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    agentDiffServCosMarkActTable.setStatus("current")
_AgentDiffServCosMarkActEntry_Object = MibTableRow
agentDiffServCosMarkActEntry = _AgentDiffServCosMarkActEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2, 2, 1)
)
agentDiffServCosMarkActEntry.setIndexNames(
    (0, "FSM7326-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServCosMarkActCos"),
)
if mibBuilder.loadTexts:
    agentDiffServCosMarkActEntry.setStatus("current")
_AgentDiffServCosMarkActCos_Type = Cos
_AgentDiffServCosMarkActCos_Object = MibTableColumn
agentDiffServCosMarkActCos = _AgentDiffServCosMarkActCos_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2, 2, 1, 1),
    _AgentDiffServCosMarkActCos_Type()
)
agentDiffServCosMarkActCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServCosMarkActCos.setStatus("current")
_AgentDiffServIpPrecMarkActTable_Object = MibTable
agentDiffServIpPrecMarkActTable = _AgentDiffServIpPrecMarkActTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    agentDiffServIpPrecMarkActTable.setStatus("current")
_AgentDiffServIpPrecMarkActEntry_Object = MibTableRow
agentDiffServIpPrecMarkActEntry = _AgentDiffServIpPrecMarkActEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2, 4, 1)
)
agentDiffServIpPrecMarkActEntry.setIndexNames(
    (0, "FSM7326-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServIpPrecMarkActPrecedence"),
)
if mibBuilder.loadTexts:
    agentDiffServIpPrecMarkActEntry.setStatus("current")
_AgentDiffServIpPrecMarkActPrecedence_Type = IpPrecedence
_AgentDiffServIpPrecMarkActPrecedence_Object = MibTableColumn
agentDiffServIpPrecMarkActPrecedence = _AgentDiffServIpPrecMarkActPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 3, 1, 2, 4, 1, 1),
    _AgentDiffServIpPrecMarkActPrecedence_Type()
)
agentDiffServIpPrecMarkActPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServIpPrecMarkActPrecedence.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSM7326-QOS-DIFFSERV-EXTENSIONS-MIB",
    **{"IpPrecedence": IpPrecedence,
       "Cos": Cos,
       "CosOrAny": CosOrAny,
       "VlanIdOrAny": VlanIdOrAny,
       "fsm7326QOSDiffServExtensions": fsm7326QOSDiffServExtensions,
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
       "agentDiffServAction": agentDiffServAction,
       "agentDiffServCosMarkActTable": agentDiffServCosMarkActTable,
       "agentDiffServCosMarkActEntry": agentDiffServCosMarkActEntry,
       "agentDiffServCosMarkActCos": agentDiffServCosMarkActCos,
       "agentDiffServIpPrecMarkActTable": agentDiffServIpPrecMarkActTable,
       "agentDiffServIpPrecMarkActEntry": agentDiffServIpPrecMarkActEntry,
       "agentDiffServIpPrecMarkActPrecedence": agentDiffServIpPrecMarkActPrecedence}
)
