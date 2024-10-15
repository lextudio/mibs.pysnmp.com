# SNMP MIB module (DOCS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:02 2024
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

(docsIfMib,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 7)
)
docsQosMIB.setRevisions(
        ("2001-11-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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
        *(("downstream", 1),
          ("upstream", 2))
    )



class BitRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class SchedulingType(Integer32, TextualConvention):
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
        *(("bestEffort", 2),
          ("nonRealTimePollingService", 3),
          ("realTimePollingService", 4),
          ("undefined", 1),
          ("unsolictedGrantService", 6),
          ("unsolictedGrantServiceWithAD", 5))
    )



# MIB Managed Objects in the order of their OIDs

_DocsQosMIBObjects_ObjectIdentity = ObjectIdentity
docsQosMIBObjects = _DocsQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1)
)
_DocsQosPktClassTable_Object = MibTable
docsQosPktClassTable = _DocsQosPktClassTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1)
)
if mibBuilder.loadTexts:
    docsQosPktClassTable.setStatus("current")
_DocsQosPktClassEntry_Object = MibTableRow
docsQosPktClassEntry = _DocsQosPktClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1)
)
docsQosPktClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsQosPktClassEntry.setStatus("current")


class _DocsQosPktClassId_Type(Integer32):
    """Custom type docsQosPktClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsQosPktClassId_Type.__name__ = "Integer32"
_DocsQosPktClassId_Object = MibTableColumn
docsQosPktClassId = _DocsQosPktClassId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 1),
    _DocsQosPktClassId_Type()
)
docsQosPktClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosPktClassId.setStatus("current")
_DocsQosPktClassDirection_Type = IfDirection
_DocsQosPktClassDirection_Object = MibTableColumn
docsQosPktClassDirection = _DocsQosPktClassDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 2),
    _DocsQosPktClassDirection_Type()
)
docsQosPktClassDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDirection.setStatus("current")


class _DocsQosPktClassPriority_Type(Integer32):
    """Custom type docsQosPktClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosPktClassPriority_Type.__name__ = "Integer32"
_DocsQosPktClassPriority_Object = MibTableColumn
docsQosPktClassPriority = _DocsQosPktClassPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 3),
    _DocsQosPktClassPriority_Type()
)
docsQosPktClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassPriority.setStatus("current")


class _DocsQosPktClassIpTosLow_Type(OctetString):
    """Custom type docsQosPktClassIpTosLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosPktClassIpTosLow_Type.__name__ = "OctetString"
_DocsQosPktClassIpTosLow_Object = MibTableColumn
docsQosPktClassIpTosLow = _DocsQosPktClassIpTosLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 4),
    _DocsQosPktClassIpTosLow_Type()
)
docsQosPktClassIpTosLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpTosLow.setStatus("current")


class _DocsQosPktClassIpTosHigh_Type(OctetString):
    """Custom type docsQosPktClassIpTosHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosPktClassIpTosHigh_Type.__name__ = "OctetString"
_DocsQosPktClassIpTosHigh_Object = MibTableColumn
docsQosPktClassIpTosHigh = _DocsQosPktClassIpTosHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 5),
    _DocsQosPktClassIpTosHigh_Type()
)
docsQosPktClassIpTosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpTosHigh.setStatus("current")


class _DocsQosPktClassIpTosMask_Type(OctetString):
    """Custom type docsQosPktClassIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosPktClassIpTosMask_Type.__name__ = "OctetString"
_DocsQosPktClassIpTosMask_Object = MibTableColumn
docsQosPktClassIpTosMask = _DocsQosPktClassIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 6),
    _DocsQosPktClassIpTosMask_Type()
)
docsQosPktClassIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpTosMask.setStatus("current")


class _DocsQosPktClassIpProtocol_Type(Integer32):
    """Custom type docsQosPktClassIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 258),
    )


_DocsQosPktClassIpProtocol_Type.__name__ = "Integer32"
_DocsQosPktClassIpProtocol_Object = MibTableColumn
docsQosPktClassIpProtocol = _DocsQosPktClassIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 7),
    _DocsQosPktClassIpProtocol_Type()
)
docsQosPktClassIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpProtocol.setStatus("current")
_DocsQosPktClassIpSourceAddr_Type = IpAddress
_DocsQosPktClassIpSourceAddr_Object = MibTableColumn
docsQosPktClassIpSourceAddr = _DocsQosPktClassIpSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 8),
    _DocsQosPktClassIpSourceAddr_Type()
)
docsQosPktClassIpSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpSourceAddr.setStatus("deprecated")
_DocsQosPktClassIpSourceMask_Type = IpAddress
_DocsQosPktClassIpSourceMask_Object = MibTableColumn
docsQosPktClassIpSourceMask = _DocsQosPktClassIpSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 9),
    _DocsQosPktClassIpSourceMask_Type()
)
docsQosPktClassIpSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpSourceMask.setStatus("deprecated")
_DocsQosPktClassIpDestAddr_Type = IpAddress
_DocsQosPktClassIpDestAddr_Object = MibTableColumn
docsQosPktClassIpDestAddr = _DocsQosPktClassIpDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 10),
    _DocsQosPktClassIpDestAddr_Type()
)
docsQosPktClassIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpDestAddr.setStatus("deprecated")
_DocsQosPktClassIpDestMask_Type = IpAddress
_DocsQosPktClassIpDestMask_Object = MibTableColumn
docsQosPktClassIpDestMask = _DocsQosPktClassIpDestMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 11),
    _DocsQosPktClassIpDestMask_Type()
)
docsQosPktClassIpDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpDestMask.setStatus("deprecated")


class _DocsQosPktClassSourcePortStart_Type(Integer32):
    """Custom type docsQosPktClassSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosPktClassSourcePortStart_Type.__name__ = "Integer32"
_DocsQosPktClassSourcePortStart_Object = MibTableColumn
docsQosPktClassSourcePortStart = _DocsQosPktClassSourcePortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 12),
    _DocsQosPktClassSourcePortStart_Type()
)
docsQosPktClassSourcePortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassSourcePortStart.setStatus("current")


class _DocsQosPktClassSourcePortEnd_Type(Integer32):
    """Custom type docsQosPktClassSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosPktClassSourcePortEnd_Type.__name__ = "Integer32"
_DocsQosPktClassSourcePortEnd_Object = MibTableColumn
docsQosPktClassSourcePortEnd = _DocsQosPktClassSourcePortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 13),
    _DocsQosPktClassSourcePortEnd_Type()
)
docsQosPktClassSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassSourcePortEnd.setStatus("current")


class _DocsQosPktClassDestPortStart_Type(Integer32):
    """Custom type docsQosPktClassDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosPktClassDestPortStart_Type.__name__ = "Integer32"
_DocsQosPktClassDestPortStart_Object = MibTableColumn
docsQosPktClassDestPortStart = _DocsQosPktClassDestPortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 14),
    _DocsQosPktClassDestPortStart_Type()
)
docsQosPktClassDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestPortStart.setStatus("current")


class _DocsQosPktClassDestPortEnd_Type(Integer32):
    """Custom type docsQosPktClassDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosPktClassDestPortEnd_Type.__name__ = "Integer32"
_DocsQosPktClassDestPortEnd_Object = MibTableColumn
docsQosPktClassDestPortEnd = _DocsQosPktClassDestPortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 15),
    _DocsQosPktClassDestPortEnd_Type()
)
docsQosPktClassDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestPortEnd.setStatus("current")
_DocsQosPktClassDestMacAddr_Type = MacAddress
_DocsQosPktClassDestMacAddr_Object = MibTableColumn
docsQosPktClassDestMacAddr = _DocsQosPktClassDestMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 16),
    _DocsQosPktClassDestMacAddr_Type()
)
docsQosPktClassDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestMacAddr.setStatus("current")
_DocsQosPktClassDestMacMask_Type = MacAddress
_DocsQosPktClassDestMacMask_Object = MibTableColumn
docsQosPktClassDestMacMask = _DocsQosPktClassDestMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 17),
    _DocsQosPktClassDestMacMask_Type()
)
docsQosPktClassDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestMacMask.setStatus("current")
_DocsQosPktClassSourceMacAddr_Type = MacAddress
_DocsQosPktClassSourceMacAddr_Object = MibTableColumn
docsQosPktClassSourceMacAddr = _DocsQosPktClassSourceMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 18),
    _DocsQosPktClassSourceMacAddr_Type()
)
docsQosPktClassSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassSourceMacAddr.setStatus("current")


class _DocsQosPktClassEnetProtocolType_Type(Integer32):
    """Custom type docsQosPktClassEnetProtocolType based on Integer32"""
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
        *(("all", 4),
          ("dsap", 2),
          ("ethertype", 1),
          ("mac", 3),
          ("none", 0))
    )


_DocsQosPktClassEnetProtocolType_Type.__name__ = "Integer32"
_DocsQosPktClassEnetProtocolType_Object = MibTableColumn
docsQosPktClassEnetProtocolType = _DocsQosPktClassEnetProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 19),
    _DocsQosPktClassEnetProtocolType_Type()
)
docsQosPktClassEnetProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassEnetProtocolType.setStatus("current")


class _DocsQosPktClassEnetProtocol_Type(Integer32):
    """Custom type docsQosPktClassEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosPktClassEnetProtocol_Type.__name__ = "Integer32"
_DocsQosPktClassEnetProtocol_Object = MibTableColumn
docsQosPktClassEnetProtocol = _DocsQosPktClassEnetProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 20),
    _DocsQosPktClassEnetProtocol_Type()
)
docsQosPktClassEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassEnetProtocol.setStatus("current")
_DocsQosPktClassUserPriApplies_Type = TruthValue
_DocsQosPktClassUserPriApplies_Object = MibTableColumn
docsQosPktClassUserPriApplies = _DocsQosPktClassUserPriApplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 21),
    _DocsQosPktClassUserPriApplies_Type()
)
docsQosPktClassUserPriApplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassUserPriApplies.setStatus("obsolete")


class _DocsQosPktClassUserPriLow_Type(Integer32):
    """Custom type docsQosPktClassUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosPktClassUserPriLow_Type.__name__ = "Integer32"
_DocsQosPktClassUserPriLow_Object = MibTableColumn
docsQosPktClassUserPriLow = _DocsQosPktClassUserPriLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 22),
    _DocsQosPktClassUserPriLow_Type()
)
docsQosPktClassUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassUserPriLow.setStatus("current")


class _DocsQosPktClassUserPriHigh_Type(Integer32):
    """Custom type docsQosPktClassUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosPktClassUserPriHigh_Type.__name__ = "Integer32"
_DocsQosPktClassUserPriHigh_Object = MibTableColumn
docsQosPktClassUserPriHigh = _DocsQosPktClassUserPriHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 23),
    _DocsQosPktClassUserPriHigh_Type()
)
docsQosPktClassUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassUserPriHigh.setStatus("current")


class _DocsQosPktClassVlanId_Type(Integer32):
    """Custom type docsQosPktClassVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DocsQosPktClassVlanId_Type.__name__ = "Integer32"
_DocsQosPktClassVlanId_Object = MibTableColumn
docsQosPktClassVlanId = _DocsQosPktClassVlanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 24),
    _DocsQosPktClassVlanId_Type()
)
docsQosPktClassVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassVlanId.setStatus("current")


class _DocsQosPktClassState_Type(Integer32):
    """Custom type docsQosPktClassState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DocsQosPktClassState_Type.__name__ = "Integer32"
_DocsQosPktClassState_Object = MibTableColumn
docsQosPktClassState = _DocsQosPktClassState_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 25),
    _DocsQosPktClassState_Type()
)
docsQosPktClassState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassState.setStatus("current")
_DocsQosPktClassPkts_Type = Counter32
_DocsQosPktClassPkts_Object = MibTableColumn
docsQosPktClassPkts = _DocsQosPktClassPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 26),
    _DocsQosPktClassPkts_Type()
)
docsQosPktClassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassPkts.setStatus("current")


class _DocsQosPktClassBitMap_Type(Bits):
    """Custom type docsQosPktClassBitMap based on Bits"""
    namedValues = NamedValues(
        *(("activationState", 1),
          ("destMac", 12),
          ("destPortEnd", 11),
          ("destPortStart", 10),
          ("ethertype", 14),
          ("ipDestAddr", 6),
          ("ipDestMask", 7),
          ("ipProtocol", 3),
          ("ipSourceAddr", 4),
          ("ipSourceMask", 5),
          ("ipTos", 2),
          ("rulePriority", 0),
          ("sourceMac", 13),
          ("sourcePortEnd", 9),
          ("sourcePortStart", 8),
          ("userPri", 15),
          ("vlanId", 16))
    )

_DocsQosPktClassBitMap_Type.__name__ = "Bits"
_DocsQosPktClassBitMap_Object = MibTableColumn
docsQosPktClassBitMap = _DocsQosPktClassBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 27),
    _DocsQosPktClassBitMap_Type()
)
docsQosPktClassBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassBitMap.setStatus("current")
_DocsQosPktClassInetSourceAddrType_Type = InetAddressType
_DocsQosPktClassInetSourceAddrType_Object = MibTableColumn
docsQosPktClassInetSourceAddrType = _DocsQosPktClassInetSourceAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 28),
    _DocsQosPktClassInetSourceAddrType_Type()
)
docsQosPktClassInetSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetSourceAddrType.setStatus("current")
_DocsQosPktClassInetSourceAddr_Type = InetAddress
_DocsQosPktClassInetSourceAddr_Object = MibTableColumn
docsQosPktClassInetSourceAddr = _DocsQosPktClassInetSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 29),
    _DocsQosPktClassInetSourceAddr_Type()
)
docsQosPktClassInetSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetSourceAddr.setStatus("current")
_DocsQosPktClassInetSourceMaskType_Type = InetAddressType
_DocsQosPktClassInetSourceMaskType_Object = MibTableColumn
docsQosPktClassInetSourceMaskType = _DocsQosPktClassInetSourceMaskType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 30),
    _DocsQosPktClassInetSourceMaskType_Type()
)
docsQosPktClassInetSourceMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetSourceMaskType.setStatus("current")
_DocsQosPktClassInetSourceMask_Type = InetAddress
_DocsQosPktClassInetSourceMask_Object = MibTableColumn
docsQosPktClassInetSourceMask = _DocsQosPktClassInetSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 31),
    _DocsQosPktClassInetSourceMask_Type()
)
docsQosPktClassInetSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetSourceMask.setStatus("current")
_DocsQosPktClassInetDestAddrType_Type = InetAddressType
_DocsQosPktClassInetDestAddrType_Object = MibTableColumn
docsQosPktClassInetDestAddrType = _DocsQosPktClassInetDestAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 32),
    _DocsQosPktClassInetDestAddrType_Type()
)
docsQosPktClassInetDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetDestAddrType.setStatus("current")
_DocsQosPktClassInetDestAddr_Type = InetAddress
_DocsQosPktClassInetDestAddr_Object = MibTableColumn
docsQosPktClassInetDestAddr = _DocsQosPktClassInetDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 33),
    _DocsQosPktClassInetDestAddr_Type()
)
docsQosPktClassInetDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetDestAddr.setStatus("current")
_DocsQosPktClassInetDestMaskType_Type = InetAddressType
_DocsQosPktClassInetDestMaskType_Object = MibTableColumn
docsQosPktClassInetDestMaskType = _DocsQosPktClassInetDestMaskType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 34),
    _DocsQosPktClassInetDestMaskType_Type()
)
docsQosPktClassInetDestMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetDestMaskType.setStatus("current")
_DocsQosPktClassInetDestMask_Type = InetAddress
_DocsQosPktClassInetDestMask_Object = MibTableColumn
docsQosPktClassInetDestMask = _DocsQosPktClassInetDestMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 1, 1, 35),
    _DocsQosPktClassInetDestMask_Type()
)
docsQosPktClassInetDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassInetDestMask.setStatus("current")
_DocsQosParamSetTable_Object = MibTable
docsQosParamSetTable = _DocsQosParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2)
)
if mibBuilder.loadTexts:
    docsQosParamSetTable.setStatus("current")
_DocsQosParamSetEntry_Object = MibTableRow
docsQosParamSetEntry = _DocsQosParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1)
)
docsQosParamSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS-MIB", "docsQosParamSetType"),
)
if mibBuilder.loadTexts:
    docsQosParamSetEntry.setStatus("current")
_DocsQosParamSetServiceClassName_Type = DisplayString
_DocsQosParamSetServiceClassName_Object = MibTableColumn
docsQosParamSetServiceClassName = _DocsQosParamSetServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 4),
    _DocsQosParamSetServiceClassName_Type()
)
docsQosParamSetServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetServiceClassName.setStatus("current")


class _DocsQosParamSetPriority_Type(Integer32):
    """Custom type docsQosParamSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosParamSetPriority_Type.__name__ = "Integer32"
_DocsQosParamSetPriority_Object = MibTableColumn
docsQosParamSetPriority = _DocsQosParamSetPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 5),
    _DocsQosParamSetPriority_Type()
)
docsQosParamSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetPriority.setStatus("current")
_DocsQosParamSetMaxTrafficRate_Type = BitRate
_DocsQosParamSetMaxTrafficRate_Object = MibTableColumn
docsQosParamSetMaxTrafficRate = _DocsQosParamSetMaxTrafficRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 6),
    _DocsQosParamSetMaxTrafficRate_Type()
)
docsQosParamSetMaxTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTrafficRate.setStatus("current")
_DocsQosParamSetMaxTrafficBurst_Type = Unsigned32
_DocsQosParamSetMaxTrafficBurst_Object = MibTableColumn
docsQosParamSetMaxTrafficBurst = _DocsQosParamSetMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 7),
    _DocsQosParamSetMaxTrafficBurst_Type()
)
docsQosParamSetMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTrafficBurst.setStatus("current")
_DocsQosParamSetMinReservedRate_Type = BitRate
_DocsQosParamSetMinReservedRate_Object = MibTableColumn
docsQosParamSetMinReservedRate = _DocsQosParamSetMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 8),
    _DocsQosParamSetMinReservedRate_Type()
)
docsQosParamSetMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMinReservedRate.setStatus("current")


class _DocsQosParamSetMinReservedPkt_Type(Integer32):
    """Custom type docsQosParamSetMinReservedPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetMinReservedPkt_Type.__name__ = "Integer32"
_DocsQosParamSetMinReservedPkt_Object = MibTableColumn
docsQosParamSetMinReservedPkt = _DocsQosParamSetMinReservedPkt_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 9),
    _DocsQosParamSetMinReservedPkt_Type()
)
docsQosParamSetMinReservedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMinReservedPkt.setStatus("current")


class _DocsQosParamSetActiveTimeout_Type(Integer32):
    """Custom type docsQosParamSetActiveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetActiveTimeout_Type.__name__ = "Integer32"
_DocsQosParamSetActiveTimeout_Object = MibTableColumn
docsQosParamSetActiveTimeout = _DocsQosParamSetActiveTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 10),
    _DocsQosParamSetActiveTimeout_Type()
)
docsQosParamSetActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetActiveTimeout.setUnits("seconds")


class _DocsQosParamSetAdmittedTimeout_Type(Integer32):
    """Custom type docsQosParamSetAdmittedTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetAdmittedTimeout_Type.__name__ = "Integer32"
_DocsQosParamSetAdmittedTimeout_Object = MibTableColumn
docsQosParamSetAdmittedTimeout = _DocsQosParamSetAdmittedTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 11),
    _DocsQosParamSetAdmittedTimeout_Type()
)
docsQosParamSetAdmittedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetAdmittedTimeout.setUnits("seconds")


class _DocsQosParamSetMaxConcatBurst_Type(Integer32):
    """Custom type docsQosParamSetMaxConcatBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetMaxConcatBurst_Type.__name__ = "Integer32"
_DocsQosParamSetMaxConcatBurst_Object = MibTableColumn
docsQosParamSetMaxConcatBurst = _DocsQosParamSetMaxConcatBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 12),
    _DocsQosParamSetMaxConcatBurst_Type()
)
docsQosParamSetMaxConcatBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxConcatBurst.setStatus("current")
_DocsQosParamSetSchedulingType_Type = SchedulingType
_DocsQosParamSetSchedulingType_Object = MibTableColumn
docsQosParamSetSchedulingType = _DocsQosParamSetSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 13),
    _DocsQosParamSetSchedulingType_Type()
)
docsQosParamSetSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetSchedulingType.setStatus("current")
_DocsQosParamSetNomPollInterval_Type = Unsigned32
_DocsQosParamSetNomPollInterval_Object = MibTableColumn
docsQosParamSetNomPollInterval = _DocsQosParamSetNomPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 15),
    _DocsQosParamSetNomPollInterval_Type()
)
docsQosParamSetNomPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetNomPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetNomPollInterval.setUnits("microseconds")
_DocsQosParamSetTolPollJitter_Type = Unsigned32
_DocsQosParamSetTolPollJitter_Object = MibTableColumn
docsQosParamSetTolPollJitter = _DocsQosParamSetTolPollJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 16),
    _DocsQosParamSetTolPollJitter_Type()
)
docsQosParamSetTolPollJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTolPollJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetTolPollJitter.setUnits("microseconds")


class _DocsQosParamSetUnsolicitGrantSize_Type(Integer32):
    """Custom type docsQosParamSetUnsolicitGrantSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetUnsolicitGrantSize_Type.__name__ = "Integer32"
_DocsQosParamSetUnsolicitGrantSize_Object = MibTableColumn
docsQosParamSetUnsolicitGrantSize = _DocsQosParamSetUnsolicitGrantSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 17),
    _DocsQosParamSetUnsolicitGrantSize_Type()
)
docsQosParamSetUnsolicitGrantSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetUnsolicitGrantSize.setStatus("current")
_DocsQosParamSetNomGrantInterval_Type = Unsigned32
_DocsQosParamSetNomGrantInterval_Object = MibTableColumn
docsQosParamSetNomGrantInterval = _DocsQosParamSetNomGrantInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 18),
    _DocsQosParamSetNomGrantInterval_Type()
)
docsQosParamSetNomGrantInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetNomGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetNomGrantInterval.setUnits("microseconds")
_DocsQosParamSetTolGrantJitter_Type = Unsigned32
_DocsQosParamSetTolGrantJitter_Object = MibTableColumn
docsQosParamSetTolGrantJitter = _DocsQosParamSetTolGrantJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 19),
    _DocsQosParamSetTolGrantJitter_Type()
)
docsQosParamSetTolGrantJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTolGrantJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetTolGrantJitter.setUnits("microseconds")


class _DocsQosParamSetGrantsPerInterval_Type(Integer32):
    """Custom type docsQosParamSetGrantsPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DocsQosParamSetGrantsPerInterval_Type.__name__ = "Integer32"
_DocsQosParamSetGrantsPerInterval_Object = MibTableColumn
docsQosParamSetGrantsPerInterval = _DocsQosParamSetGrantsPerInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 20),
    _DocsQosParamSetGrantsPerInterval_Type()
)
docsQosParamSetGrantsPerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetGrantsPerInterval.setStatus("current")


class _DocsQosParamSetTosAndMask_Type(OctetString):
    """Custom type docsQosParamSetTosAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosParamSetTosAndMask_Type.__name__ = "OctetString"
_DocsQosParamSetTosAndMask_Object = MibTableColumn
docsQosParamSetTosAndMask = _DocsQosParamSetTosAndMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 21),
    _DocsQosParamSetTosAndMask_Type()
)
docsQosParamSetTosAndMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTosAndMask.setStatus("current")


class _DocsQosParamSetTosOrMask_Type(OctetString):
    """Custom type docsQosParamSetTosOrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosParamSetTosOrMask_Type.__name__ = "OctetString"
_DocsQosParamSetTosOrMask_Object = MibTableColumn
docsQosParamSetTosOrMask = _DocsQosParamSetTosOrMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 22),
    _DocsQosParamSetTosOrMask_Type()
)
docsQosParamSetTosOrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTosOrMask.setStatus("current")
_DocsQosParamSetMaxLatency_Type = Unsigned32
_DocsQosParamSetMaxLatency_Object = MibTableColumn
docsQosParamSetMaxLatency = _DocsQosParamSetMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 23),
    _DocsQosParamSetMaxLatency_Type()
)
docsQosParamSetMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMaxLatency.setUnits("microseconds")


class _DocsQosParamSetType_Type(Integer32):
    """Custom type docsQosParamSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("admitted", 2),
          ("provisioned", 3))
    )


_DocsQosParamSetType_Type.__name__ = "Integer32"
_DocsQosParamSetType_Object = MibTableColumn
docsQosParamSetType = _DocsQosParamSetType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 24),
    _DocsQosParamSetType_Type()
)
docsQosParamSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosParamSetType.setStatus("current")


class _DocsQosParamSetRequestPolicyOct_Type(OctetString):
    """Custom type docsQosParamSetRequestPolicyOct based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsQosParamSetRequestPolicyOct_Type.__name__ = "OctetString"
_DocsQosParamSetRequestPolicyOct_Object = MibTableColumn
docsQosParamSetRequestPolicyOct = _DocsQosParamSetRequestPolicyOct_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 25),
    _DocsQosParamSetRequestPolicyOct_Type()
)
docsQosParamSetRequestPolicyOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetRequestPolicyOct.setStatus("current")


class _DocsQosParamSetBitMap_Type(Bits):
    """Custom type docsQosParamSetBitMap based on Bits"""
    namedValues = NamedValues(
        *(("activeTimeout", 5),
          ("admittedTimeout", 6),
          ("grantsPerInterval", 15),
          ("maxConcatBurst", 7),
          ("maxLatency", 17),
          ("maxTrafficBurst", 2),
          ("maxTrafficRate", 1),
          ("minReservedPkt", 4),
          ("minReservedRate", 3),
          ("nomGrantInterval", 13),
          ("nomPollInterval", 10),
          ("requestPolicy", 9),
          ("schedulingType", 8),
          ("tolGrantJitter", 14),
          ("tolPollJitter", 11),
          ("tosOverwrite", 16),
          ("trafficPriority", 0),
          ("unsolicitGrantSize", 12))
    )

_DocsQosParamSetBitMap_Type.__name__ = "Bits"
_DocsQosParamSetBitMap_Object = MibTableColumn
docsQosParamSetBitMap = _DocsQosParamSetBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 2, 1, 26),
    _DocsQosParamSetBitMap_Type()
)
docsQosParamSetBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetBitMap.setStatus("current")
_DocsQosServiceFlowTable_Object = MibTable
docsQosServiceFlowTable = _DocsQosServiceFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowTable.setStatus("current")
_DocsQosServiceFlowEntry_Object = MibTableRow
docsQosServiceFlowEntry = _DocsQosServiceFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1)
)
docsQosServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowEntry.setStatus("current")


class _DocsQosServiceFlowId_Type(Unsigned32):
    """Custom type docsQosServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosServiceFlowId_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowId_Object = MibTableColumn
docsQosServiceFlowId = _DocsQosServiceFlowId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 1),
    _DocsQosServiceFlowId_Type()
)
docsQosServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceFlowId.setStatus("current")


class _DocsQosServiceFlowProvisionedParamSetIndex_Type(Unsigned32):
    """Custom type docsQosServiceFlowProvisionedParamSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceFlowProvisionedParamSetIndex_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowProvisionedParamSetIndex_Object = MibTableColumn
docsQosServiceFlowProvisionedParamSetIndex = _DocsQosServiceFlowProvisionedParamSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 3),
    _DocsQosServiceFlowProvisionedParamSetIndex_Type()
)
docsQosServiceFlowProvisionedParamSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowProvisionedParamSetIndex.setStatus("obsolete")


class _DocsQosServiceFlowAdmittedParamSetIndex_Type(Unsigned32):
    """Custom type docsQosServiceFlowAdmittedParamSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceFlowAdmittedParamSetIndex_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowAdmittedParamSetIndex_Object = MibTableColumn
docsQosServiceFlowAdmittedParamSetIndex = _DocsQosServiceFlowAdmittedParamSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 4),
    _DocsQosServiceFlowAdmittedParamSetIndex_Type()
)
docsQosServiceFlowAdmittedParamSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowAdmittedParamSetIndex.setStatus("obsolete")


class _DocsQosServiceFlowActiveParamSetIndex_Type(Unsigned32):
    """Custom type docsQosServiceFlowActiveParamSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceFlowActiveParamSetIndex_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowActiveParamSetIndex_Object = MibTableColumn
docsQosServiceFlowActiveParamSetIndex = _DocsQosServiceFlowActiveParamSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 5),
    _DocsQosServiceFlowActiveParamSetIndex_Type()
)
docsQosServiceFlowActiveParamSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowActiveParamSetIndex.setStatus("obsolete")


class _DocsQosServiceFlowSID_Type(Unsigned32):
    """Custom type docsQosServiceFlowSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsQosServiceFlowSID_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowSID_Object = MibTableColumn
docsQosServiceFlowSID = _DocsQosServiceFlowSID_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 6),
    _DocsQosServiceFlowSID_Type()
)
docsQosServiceFlowSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowSID.setStatus("current")
_DocsQosServiceFlowDirection_Type = IfDirection
_DocsQosServiceFlowDirection_Object = MibTableColumn
docsQosServiceFlowDirection = _DocsQosServiceFlowDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 7),
    _DocsQosServiceFlowDirection_Type()
)
docsQosServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowDirection.setStatus("current")
_DocsQosServiceFlowPrimary_Type = TruthValue
_DocsQosServiceFlowPrimary_Object = MibTableColumn
docsQosServiceFlowPrimary = _DocsQosServiceFlowPrimary_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 8),
    _DocsQosServiceFlowPrimary_Type()
)
docsQosServiceFlowPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPrimary.setStatus("current")


class _DocsQosServiceFlowActiveTimeout_Type(Integer32):
    """Custom type docsQosServiceFlowActiveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceFlowActiveTimeout_Type.__name__ = "Integer32"
_DocsQosServiceFlowActiveTimeout_Object = MibTableColumn
docsQosServiceFlowActiveTimeout = _DocsQosServiceFlowActiveTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 9),
    _DocsQosServiceFlowActiveTimeout_Type()
)
docsQosServiceFlowActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowActiveTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsQosServiceFlowActiveTimeout.setUnits("seconds")


class _DocsQosServiceFlowAdmittedTimeout_Type(Integer32):
    """Custom type docsQosServiceFlowAdmittedTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceFlowAdmittedTimeout_Type.__name__ = "Integer32"
_DocsQosServiceFlowAdmittedTimeout_Object = MibTableColumn
docsQosServiceFlowAdmittedTimeout = _DocsQosServiceFlowAdmittedTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 10),
    _DocsQosServiceFlowAdmittedTimeout_Type()
)
docsQosServiceFlowAdmittedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowAdmittedTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsQosServiceFlowAdmittedTimeout.setUnits("seconds")
_DocsQosServiceFlowSchedulingType_Type = SchedulingType
_DocsQosServiceFlowSchedulingType_Object = MibTableColumn
docsQosServiceFlowSchedulingType = _DocsQosServiceFlowSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 11),
    _DocsQosServiceFlowSchedulingType_Type()
)
docsQosServiceFlowSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowSchedulingType.setStatus("obsolete")


class _DocsQosServiceFlowRequestPolicy_Type(OctetString):
    """Custom type docsQosServiceFlowRequestPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsQosServiceFlowRequestPolicy_Type.__name__ = "OctetString"
_DocsQosServiceFlowRequestPolicy_Object = MibTableColumn
docsQosServiceFlowRequestPolicy = _DocsQosServiceFlowRequestPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 12),
    _DocsQosServiceFlowRequestPolicy_Type()
)
docsQosServiceFlowRequestPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowRequestPolicy.setStatus("obsolete")


class _DocsQosServiceFlowTosAndMask_Type(OctetString):
    """Custom type docsQosServiceFlowTosAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosServiceFlowTosAndMask_Type.__name__ = "OctetString"
_DocsQosServiceFlowTosAndMask_Object = MibTableColumn
docsQosServiceFlowTosAndMask = _DocsQosServiceFlowTosAndMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 13),
    _DocsQosServiceFlowTosAndMask_Type()
)
docsQosServiceFlowTosAndMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowTosAndMask.setStatus("obsolete")


class _DocsQosServiceFlowTosOrMask_Type(OctetString):
    """Custom type docsQosServiceFlowTosOrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosServiceFlowTosOrMask_Type.__name__ = "OctetString"
_DocsQosServiceFlowTosOrMask_Object = MibTableColumn
docsQosServiceFlowTosOrMask = _DocsQosServiceFlowTosOrMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 3, 1, 14),
    _DocsQosServiceFlowTosOrMask_Type()
)
docsQosServiceFlowTosOrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowTosOrMask.setStatus("obsolete")
_DocsQosServiceFlowStatsTable_Object = MibTable
docsQosServiceFlowStatsTable = _DocsQosServiceFlowStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowStatsTable.setStatus("current")
_DocsQosServiceFlowStatsEntry_Object = MibTableRow
docsQosServiceFlowStatsEntry = _DocsQosServiceFlowStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1)
)
docsQosServiceFlowStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowStatsEntry.setStatus("current")
_DocsQosServiceFlowPkts_Type = Counter32
_DocsQosServiceFlowPkts_Object = MibTableColumn
docsQosServiceFlowPkts = _DocsQosServiceFlowPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 1),
    _DocsQosServiceFlowPkts_Type()
)
docsQosServiceFlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPkts.setStatus("current")
_DocsQosServiceFlowOctets_Type = Counter32
_DocsQosServiceFlowOctets_Object = MibTableColumn
docsQosServiceFlowOctets = _DocsQosServiceFlowOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 2),
    _DocsQosServiceFlowOctets_Type()
)
docsQosServiceFlowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowOctets.setStatus("current")
_DocsQosServiceFlowTimeCreated_Type = TimeStamp
_DocsQosServiceFlowTimeCreated_Object = MibTableColumn
docsQosServiceFlowTimeCreated = _DocsQosServiceFlowTimeCreated_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 3),
    _DocsQosServiceFlowTimeCreated_Type()
)
docsQosServiceFlowTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowTimeCreated.setStatus("current")
_DocsQosServiceFlowTimeActive_Type = Counter32
_DocsQosServiceFlowTimeActive_Object = MibTableColumn
docsQosServiceFlowTimeActive = _DocsQosServiceFlowTimeActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 4),
    _DocsQosServiceFlowTimeActive_Type()
)
docsQosServiceFlowTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowTimeActive.setUnits("seconds")
_DocsQosServiceFlowPHSUnknowns_Type = Counter32
_DocsQosServiceFlowPHSUnknowns_Object = MibTableColumn
docsQosServiceFlowPHSUnknowns = _DocsQosServiceFlowPHSUnknowns_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 5),
    _DocsQosServiceFlowPHSUnknowns_Type()
)
docsQosServiceFlowPHSUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPHSUnknowns.setStatus("current")
_DocsQosServiceFlowPolicedDropPkts_Type = Counter32
_DocsQosServiceFlowPolicedDropPkts_Object = MibTableColumn
docsQosServiceFlowPolicedDropPkts = _DocsQosServiceFlowPolicedDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 6),
    _DocsQosServiceFlowPolicedDropPkts_Type()
)
docsQosServiceFlowPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPolicedDropPkts.setStatus("current")
_DocsQosServiceFlowPolicedDelayPkts_Type = Counter32
_DocsQosServiceFlowPolicedDelayPkts_Object = MibTableColumn
docsQosServiceFlowPolicedDelayPkts = _DocsQosServiceFlowPolicedDelayPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 4, 1, 7),
    _DocsQosServiceFlowPolicedDelayPkts_Type()
)
docsQosServiceFlowPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPolicedDelayPkts.setStatus("current")
_DocsQosUpstreamStatsTable_Object = MibTable
docsQosUpstreamStatsTable = _DocsQosUpstreamStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 5)
)
if mibBuilder.loadTexts:
    docsQosUpstreamStatsTable.setStatus("current")
_DocsQosUpstreamStatsEntry_Object = MibTableRow
docsQosUpstreamStatsEntry = _DocsQosUpstreamStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 5, 1)
)
docsQosUpstreamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosSID"),
)
if mibBuilder.loadTexts:
    docsQosUpstreamStatsEntry.setStatus("current")


class _DocsQosSID_Type(Integer32):
    """Custom type docsQosSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsQosSID_Type.__name__ = "Integer32"
_DocsQosSID_Object = MibTableColumn
docsQosSID = _DocsQosSID_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 5, 1, 1),
    _DocsQosSID_Type()
)
docsQosSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosSID.setStatus("current")
_DocsQosUpstreamFragments_Type = Counter32
_DocsQosUpstreamFragments_Object = MibTableColumn
docsQosUpstreamFragments = _DocsQosUpstreamFragments_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 5, 1, 2),
    _DocsQosUpstreamFragments_Type()
)
docsQosUpstreamFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpstreamFragments.setStatus("current")
_DocsQosUpstreamFragDiscards_Type = Counter32
_DocsQosUpstreamFragDiscards_Object = MibTableColumn
docsQosUpstreamFragDiscards = _DocsQosUpstreamFragDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 5, 1, 3),
    _DocsQosUpstreamFragDiscards_Type()
)
docsQosUpstreamFragDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpstreamFragDiscards.setStatus("current")
_DocsQosUpstreamConcatBursts_Type = Counter32
_DocsQosUpstreamConcatBursts_Object = MibTableColumn
docsQosUpstreamConcatBursts = _DocsQosUpstreamConcatBursts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 5, 1, 4),
    _DocsQosUpstreamConcatBursts_Type()
)
docsQosUpstreamConcatBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpstreamConcatBursts.setStatus("current")
_DocsQosDynamicServiceStatsTable_Object = MibTable
docsQosDynamicServiceStatsTable = _DocsQosDynamicServiceStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6)
)
if mibBuilder.loadTexts:
    docsQosDynamicServiceStatsTable.setStatus("current")
_DocsQosDynamicServiceStatsEntry_Object = MibTableRow
docsQosDynamicServiceStatsEntry = _DocsQosDynamicServiceStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1)
)
docsQosDynamicServiceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosIfDirection"),
)
if mibBuilder.loadTexts:
    docsQosDynamicServiceStatsEntry.setStatus("current")
_DocsQosIfDirection_Type = IfDirection
_DocsQosIfDirection_Object = MibTableColumn
docsQosIfDirection = _DocsQosIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 1),
    _DocsQosIfDirection_Type()
)
docsQosIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosIfDirection.setStatus("current")
_DocsQosDSAReqs_Type = Counter32
_DocsQosDSAReqs_Object = MibTableColumn
docsQosDSAReqs = _DocsQosDSAReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 2),
    _DocsQosDSAReqs_Type()
)
docsQosDSAReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSAReqs.setStatus("current")
_DocsQosDSARsps_Type = Counter32
_DocsQosDSARsps_Object = MibTableColumn
docsQosDSARsps = _DocsQosDSARsps_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 3),
    _DocsQosDSARsps_Type()
)
docsQosDSARsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSARsps.setStatus("current")
_DocsQosDSAAcks_Type = Counter32
_DocsQosDSAAcks_Object = MibTableColumn
docsQosDSAAcks = _DocsQosDSAAcks_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 4),
    _DocsQosDSAAcks_Type()
)
docsQosDSAAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSAAcks.setStatus("current")
_DocsQosDSCReqs_Type = Counter32
_DocsQosDSCReqs_Object = MibTableColumn
docsQosDSCReqs = _DocsQosDSCReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 5),
    _DocsQosDSCReqs_Type()
)
docsQosDSCReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSCReqs.setStatus("current")
_DocsQosDSCRsps_Type = Counter32
_DocsQosDSCRsps_Object = MibTableColumn
docsQosDSCRsps = _DocsQosDSCRsps_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 6),
    _DocsQosDSCRsps_Type()
)
docsQosDSCRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSCRsps.setStatus("current")
_DocsQosDSCAcks_Type = Counter32
_DocsQosDSCAcks_Object = MibTableColumn
docsQosDSCAcks = _DocsQosDSCAcks_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 7),
    _DocsQosDSCAcks_Type()
)
docsQosDSCAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSCAcks.setStatus("current")
_DocsQosDSDReqs_Type = Counter32
_DocsQosDSDReqs_Object = MibTableColumn
docsQosDSDReqs = _DocsQosDSDReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 8),
    _DocsQosDSDReqs_Type()
)
docsQosDSDReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSDReqs.setStatus("current")
_DocsQosDSDRsps_Type = Counter32
_DocsQosDSDRsps_Object = MibTableColumn
docsQosDSDRsps = _DocsQosDSDRsps_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 9),
    _DocsQosDSDRsps_Type()
)
docsQosDSDRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSDRsps.setStatus("current")
_DocsQosDynamicAdds_Type = Counter32
_DocsQosDynamicAdds_Object = MibTableColumn
docsQosDynamicAdds = _DocsQosDynamicAdds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 10),
    _DocsQosDynamicAdds_Type()
)
docsQosDynamicAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicAdds.setStatus("current")
_DocsQosDynamicAddFails_Type = Counter32
_DocsQosDynamicAddFails_Object = MibTableColumn
docsQosDynamicAddFails = _DocsQosDynamicAddFails_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 11),
    _DocsQosDynamicAddFails_Type()
)
docsQosDynamicAddFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicAddFails.setStatus("current")
_DocsQosDynamicChanges_Type = Counter32
_DocsQosDynamicChanges_Object = MibTableColumn
docsQosDynamicChanges = _DocsQosDynamicChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 12),
    _DocsQosDynamicChanges_Type()
)
docsQosDynamicChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicChanges.setStatus("current")
_DocsQosDynamicChangeFails_Type = Counter32
_DocsQosDynamicChangeFails_Object = MibTableColumn
docsQosDynamicChangeFails = _DocsQosDynamicChangeFails_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 13),
    _DocsQosDynamicChangeFails_Type()
)
docsQosDynamicChangeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicChangeFails.setStatus("current")
_DocsQosDynamicDeletes_Type = Counter32
_DocsQosDynamicDeletes_Object = MibTableColumn
docsQosDynamicDeletes = _DocsQosDynamicDeletes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 14),
    _DocsQosDynamicDeletes_Type()
)
docsQosDynamicDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicDeletes.setStatus("current")
_DocsQosDynamicDeleteFails_Type = Counter32
_DocsQosDynamicDeleteFails_Object = MibTableColumn
docsQosDynamicDeleteFails = _DocsQosDynamicDeleteFails_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 15),
    _DocsQosDynamicDeleteFails_Type()
)
docsQosDynamicDeleteFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicDeleteFails.setStatus("current")
_DocsQosDCCReqs_Type = Counter32
_DocsQosDCCReqs_Object = MibTableColumn
docsQosDCCReqs = _DocsQosDCCReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 16),
    _DocsQosDCCReqs_Type()
)
docsQosDCCReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCReqs.setStatus("current")
_DocsQosDCCRsps_Type = Counter32
_DocsQosDCCRsps_Object = MibTableColumn
docsQosDCCRsps = _DocsQosDCCRsps_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 17),
    _DocsQosDCCRsps_Type()
)
docsQosDCCRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCRsps.setStatus("current")
_DocsQosDCCAcks_Type = Counter32
_DocsQosDCCAcks_Object = MibTableColumn
docsQosDCCAcks = _DocsQosDCCAcks_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 18),
    _DocsQosDCCAcks_Type()
)
docsQosDCCAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCAcks.setStatus("current")
_DocsQosDCCs_Type = Counter32
_DocsQosDCCs_Object = MibTableColumn
docsQosDCCs = _DocsQosDCCs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 19),
    _DocsQosDCCs_Type()
)
docsQosDCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCs.setStatus("current")
_DocsQosDCCFails_Type = Counter32
_DocsQosDCCFails_Object = MibTableColumn
docsQosDCCFails = _DocsQosDCCFails_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 20),
    _DocsQosDCCFails_Type()
)
docsQosDCCFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCFails.setStatus("current")
_DocsQosDCCRspDeparts_Type = Counter32
_DocsQosDCCRspDeparts_Object = MibTableColumn
docsQosDCCRspDeparts = _DocsQosDCCRspDeparts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 21),
    _DocsQosDCCRspDeparts_Type()
)
docsQosDCCRspDeparts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCRspDeparts.setStatus("current")
_DocsQosDCCRspArrives_Type = Counter32
_DocsQosDCCRspArrives_Object = MibTableColumn
docsQosDCCRspArrives = _DocsQosDCCRspArrives_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 6, 1, 22),
    _DocsQosDCCRspArrives_Type()
)
docsQosDCCRspArrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCRspArrives.setStatus("current")
_DocsQosServiceFlowLogTable_Object = MibTable
docsQosServiceFlowLogTable = _DocsQosServiceFlowLogTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTable.setStatus("current")
_DocsQosServiceFlowLogEntry_Object = MibTableRow
docsQosServiceFlowLogEntry = _DocsQosServiceFlowLogEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1)
)
docsQosServiceFlowLogEntry.setIndexNames(
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowLogIndex"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowLogEntry.setStatus("current")
_DocsQosServiceFlowLogIndex_Type = Unsigned32
_DocsQosServiceFlowLogIndex_Object = MibTableColumn
docsQosServiceFlowLogIndex = _DocsQosServiceFlowLogIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 1),
    _DocsQosServiceFlowLogIndex_Type()
)
docsQosServiceFlowLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogIndex.setStatus("current")
_DocsQosServiceFlowLogIfIndex_Type = InterfaceIndex
_DocsQosServiceFlowLogIfIndex_Object = MibTableColumn
docsQosServiceFlowLogIfIndex = _DocsQosServiceFlowLogIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 2),
    _DocsQosServiceFlowLogIfIndex_Type()
)
docsQosServiceFlowLogIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogIfIndex.setStatus("current")


class _DocsQosServiceFlowLogSFID_Type(Unsigned32):
    """Custom type docsQosServiceFlowLogSFID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosServiceFlowLogSFID_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowLogSFID_Object = MibTableColumn
docsQosServiceFlowLogSFID = _DocsQosServiceFlowLogSFID_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 3),
    _DocsQosServiceFlowLogSFID_Type()
)
docsQosServiceFlowLogSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogSFID.setStatus("current")
_DocsQosServiceFlowLogCmMac_Type = MacAddress
_DocsQosServiceFlowLogCmMac_Object = MibTableColumn
docsQosServiceFlowLogCmMac = _DocsQosServiceFlowLogCmMac_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 4),
    _DocsQosServiceFlowLogCmMac_Type()
)
docsQosServiceFlowLogCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogCmMac.setStatus("current")
_DocsQosServiceFlowLogPkts_Type = Counter32
_DocsQosServiceFlowLogPkts_Object = MibTableColumn
docsQosServiceFlowLogPkts = _DocsQosServiceFlowLogPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 5),
    _DocsQosServiceFlowLogPkts_Type()
)
docsQosServiceFlowLogPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPkts.setStatus("current")
_DocsQosServiceFlowLogOctets_Type = Counter32
_DocsQosServiceFlowLogOctets_Object = MibTableColumn
docsQosServiceFlowLogOctets = _DocsQosServiceFlowLogOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 6),
    _DocsQosServiceFlowLogOctets_Type()
)
docsQosServiceFlowLogOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogOctets.setStatus("current")
_DocsQosServiceFlowLogTimeDeleted_Type = TimeStamp
_DocsQosServiceFlowLogTimeDeleted_Object = MibTableColumn
docsQosServiceFlowLogTimeDeleted = _DocsQosServiceFlowLogTimeDeleted_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 7),
    _DocsQosServiceFlowLogTimeDeleted_Type()
)
docsQosServiceFlowLogTimeDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeDeleted.setStatus("current")
_DocsQosServiceFlowLogTimeCreated_Type = TimeStamp
_DocsQosServiceFlowLogTimeCreated_Object = MibTableColumn
docsQosServiceFlowLogTimeCreated = _DocsQosServiceFlowLogTimeCreated_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 8),
    _DocsQosServiceFlowLogTimeCreated_Type()
)
docsQosServiceFlowLogTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeCreated.setStatus("current")
_DocsQosServiceFlowLogTimeActive_Type = Counter32
_DocsQosServiceFlowLogTimeActive_Object = MibTableColumn
docsQosServiceFlowLogTimeActive = _DocsQosServiceFlowLogTimeActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 9),
    _DocsQosServiceFlowLogTimeActive_Type()
)
docsQosServiceFlowLogTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeActive.setUnits("seconds")
_DocsQosServiceFlowLogDirection_Type = IfDirection
_DocsQosServiceFlowLogDirection_Object = MibTableColumn
docsQosServiceFlowLogDirection = _DocsQosServiceFlowLogDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 11),
    _DocsQosServiceFlowLogDirection_Type()
)
docsQosServiceFlowLogDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogDirection.setStatus("current")
_DocsQosServiceFlowLogPrimary_Type = TruthValue
_DocsQosServiceFlowLogPrimary_Object = MibTableColumn
docsQosServiceFlowLogPrimary = _DocsQosServiceFlowLogPrimary_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 12),
    _DocsQosServiceFlowLogPrimary_Type()
)
docsQosServiceFlowLogPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPrimary.setStatus("current")
_DocsQosServiceFlowLogServiceClassName_Type = DisplayString
_DocsQosServiceFlowLogServiceClassName_Object = MibTableColumn
docsQosServiceFlowLogServiceClassName = _DocsQosServiceFlowLogServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 13),
    _DocsQosServiceFlowLogServiceClassName_Type()
)
docsQosServiceFlowLogServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogServiceClassName.setStatus("current")
_DocsQosServiceFlowLogPolicedDropPkts_Type = Counter32
_DocsQosServiceFlowLogPolicedDropPkts_Object = MibTableColumn
docsQosServiceFlowLogPolicedDropPkts = _DocsQosServiceFlowLogPolicedDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 14),
    _DocsQosServiceFlowLogPolicedDropPkts_Type()
)
docsQosServiceFlowLogPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPolicedDropPkts.setStatus("current")
_DocsQosServiceFlowLogPolicedDelayPkts_Type = Counter32
_DocsQosServiceFlowLogPolicedDelayPkts_Object = MibTableColumn
docsQosServiceFlowLogPolicedDelayPkts = _DocsQosServiceFlowLogPolicedDelayPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 15),
    _DocsQosServiceFlowLogPolicedDelayPkts_Type()
)
docsQosServiceFlowLogPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPolicedDelayPkts.setStatus("current")


class _DocsQosServiceFlowLogControl_Type(Integer32):
    """Custom type docsQosServiceFlowLogControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_DocsQosServiceFlowLogControl_Type.__name__ = "Integer32"
_DocsQosServiceFlowLogControl_Object = MibTableColumn
docsQosServiceFlowLogControl = _DocsQosServiceFlowLogControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 7, 1, 16),
    _DocsQosServiceFlowLogControl_Type()
)
docsQosServiceFlowLogControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogControl.setStatus("current")
_DocsQosServiceClassTable_Object = MibTable
docsQosServiceClassTable = _DocsQosServiceClassTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8)
)
if mibBuilder.loadTexts:
    docsQosServiceClassTable.setStatus("current")
_DocsQosServiceClassEntry_Object = MibTableRow
docsQosServiceClassEntry = _DocsQosServiceClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1)
)
docsQosServiceClassEntry.setIndexNames(
    (0, "DOCS-QOS-MIB", "docsQosServiceClassName"),
)
if mibBuilder.loadTexts:
    docsQosServiceClassEntry.setStatus("current")


class _DocsQosServiceClassName_Type(DisplayString):
    """Custom type docsQosServiceClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DocsQosServiceClassName_Type.__name__ = "DisplayString"
_DocsQosServiceClassName_Object = MibTableColumn
docsQosServiceClassName = _DocsQosServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 1),
    _DocsQosServiceClassName_Type()
)
docsQosServiceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceClassName.setStatus("current")


class _DocsQosServiceClassParamSetIndex_Type(Unsigned32):
    """Custom type docsQosServiceClassParamSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosServiceClassParamSetIndex_Type.__name__ = "Unsigned32"
_DocsQosServiceClassParamSetIndex_Object = MibTableColumn
docsQosServiceClassParamSetIndex = _DocsQosServiceClassParamSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 2),
    _DocsQosServiceClassParamSetIndex_Type()
)
docsQosServiceClassParamSetIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassParamSetIndex.setStatus("obsolete")
_DocsQosServiceClassStatus_Type = RowStatus
_DocsQosServiceClassStatus_Object = MibTableColumn
docsQosServiceClassStatus = _DocsQosServiceClassStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 3),
    _DocsQosServiceClassStatus_Type()
)
docsQosServiceClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassStatus.setStatus("current")


class _DocsQosServiceClassPriority_Type(Integer32):
    """Custom type docsQosServiceClassPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosServiceClassPriority_Type.__name__ = "Integer32"
_DocsQosServiceClassPriority_Object = MibTableColumn
docsQosServiceClassPriority = _DocsQosServiceClassPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 4),
    _DocsQosServiceClassPriority_Type()
)
docsQosServiceClassPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassPriority.setStatus("current")


class _DocsQosServiceClassMaxTrafficRate_Type(BitRate):
    """Custom type docsQosServiceClassMaxTrafficRate based on BitRate"""
    defaultValue = 0


_DocsQosServiceClassMaxTrafficRate_Object = MibTableColumn
docsQosServiceClassMaxTrafficRate = _DocsQosServiceClassMaxTrafficRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 5),
    _DocsQosServiceClassMaxTrafficRate_Type()
)
docsQosServiceClassMaxTrafficRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTrafficRate.setStatus("current")


class _DocsQosServiceClassMaxTrafficBurst_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxTrafficBurst based on Unsigned32"""
    defaultValue = 1522


_DocsQosServiceClassMaxTrafficBurst_Object = MibTableColumn
docsQosServiceClassMaxTrafficBurst = _DocsQosServiceClassMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 6),
    _DocsQosServiceClassMaxTrafficBurst_Type()
)
docsQosServiceClassMaxTrafficBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTrafficBurst.setStatus("current")


class _DocsQosServiceClassMinReservedRate_Type(BitRate):
    """Custom type docsQosServiceClassMinReservedRate based on BitRate"""
    defaultValue = 0


_DocsQosServiceClassMinReservedRate_Object = MibTableColumn
docsQosServiceClassMinReservedRate = _DocsQosServiceClassMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 7),
    _DocsQosServiceClassMinReservedRate_Type()
)
docsQosServiceClassMinReservedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMinReservedRate.setStatus("current")


class _DocsQosServiceClassMinReservedPkt_Type(Integer32):
    """Custom type docsQosServiceClassMinReservedPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassMinReservedPkt_Type.__name__ = "Integer32"
_DocsQosServiceClassMinReservedPkt_Object = MibTableColumn
docsQosServiceClassMinReservedPkt = _DocsQosServiceClassMinReservedPkt_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 8),
    _DocsQosServiceClassMinReservedPkt_Type()
)
docsQosServiceClassMinReservedPkt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMinReservedPkt.setStatus("current")


class _DocsQosServiceClassMaxConcatBurst_Type(Integer32):
    """Custom type docsQosServiceClassMaxConcatBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassMaxConcatBurst_Type.__name__ = "Integer32"
_DocsQosServiceClassMaxConcatBurst_Object = MibTableColumn
docsQosServiceClassMaxConcatBurst = _DocsQosServiceClassMaxConcatBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 9),
    _DocsQosServiceClassMaxConcatBurst_Type()
)
docsQosServiceClassMaxConcatBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxConcatBurst.setStatus("current")


class _DocsQosServiceClassNomPollInterval_Type(Unsigned32):
    """Custom type docsQosServiceClassNomPollInterval based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassNomPollInterval_Object = MibTableColumn
docsQosServiceClassNomPollInterval = _DocsQosServiceClassNomPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 10),
    _DocsQosServiceClassNomPollInterval_Type()
)
docsQosServiceClassNomPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassNomPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassNomPollInterval.setUnits("microseconds")


class _DocsQosServiceClassTolPollJitter_Type(Unsigned32):
    """Custom type docsQosServiceClassTolPollJitter based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassTolPollJitter_Object = MibTableColumn
docsQosServiceClassTolPollJitter = _DocsQosServiceClassTolPollJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 11),
    _DocsQosServiceClassTolPollJitter_Type()
)
docsQosServiceClassTolPollJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTolPollJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassTolPollJitter.setUnits("microseconds")


class _DocsQosServiceClassUnsolicitGrantSize_Type(Integer32):
    """Custom type docsQosServiceClassUnsolicitGrantSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassUnsolicitGrantSize_Type.__name__ = "Integer32"
_DocsQosServiceClassUnsolicitGrantSize_Object = MibTableColumn
docsQosServiceClassUnsolicitGrantSize = _DocsQosServiceClassUnsolicitGrantSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 12),
    _DocsQosServiceClassUnsolicitGrantSize_Type()
)
docsQosServiceClassUnsolicitGrantSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassUnsolicitGrantSize.setStatus("current")


class _DocsQosServiceClassNomGrantInterval_Type(Unsigned32):
    """Custom type docsQosServiceClassNomGrantInterval based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassNomGrantInterval_Object = MibTableColumn
docsQosServiceClassNomGrantInterval = _DocsQosServiceClassNomGrantInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 13),
    _DocsQosServiceClassNomGrantInterval_Type()
)
docsQosServiceClassNomGrantInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassNomGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassNomGrantInterval.setUnits("microseconds")


class _DocsQosServiceClassTolGrantJitter_Type(Unsigned32):
    """Custom type docsQosServiceClassTolGrantJitter based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassTolGrantJitter_Object = MibTableColumn
docsQosServiceClassTolGrantJitter = _DocsQosServiceClassTolGrantJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 14),
    _DocsQosServiceClassTolGrantJitter_Type()
)
docsQosServiceClassTolGrantJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTolGrantJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassTolGrantJitter.setUnits("microseconds")


class _DocsQosServiceClassGrantsPerInterval_Type(Integer32):
    """Custom type docsQosServiceClassGrantsPerInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DocsQosServiceClassGrantsPerInterval_Type.__name__ = "Integer32"
_DocsQosServiceClassGrantsPerInterval_Object = MibTableColumn
docsQosServiceClassGrantsPerInterval = _DocsQosServiceClassGrantsPerInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 15),
    _DocsQosServiceClassGrantsPerInterval_Type()
)
docsQosServiceClassGrantsPerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassGrantsPerInterval.setStatus("current")


class _DocsQosServiceClassMaxLatency_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxLatency based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassMaxLatency_Object = MibTableColumn
docsQosServiceClassMaxLatency = _DocsQosServiceClassMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 16),
    _DocsQosServiceClassMaxLatency_Type()
)
docsQosServiceClassMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxLatency.setUnits("microseconds")


class _DocsQosServiceClassActiveTimeout_Type(Integer32):
    """Custom type docsQosServiceClassActiveTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassActiveTimeout_Type.__name__ = "Integer32"
_DocsQosServiceClassActiveTimeout_Object = MibTableColumn
docsQosServiceClassActiveTimeout = _DocsQosServiceClassActiveTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 17),
    _DocsQosServiceClassActiveTimeout_Type()
)
docsQosServiceClassActiveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassActiveTimeout.setUnits("seconds")


class _DocsQosServiceClassAdmittedTimeout_Type(Integer32):
    """Custom type docsQosServiceClassAdmittedTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassAdmittedTimeout_Type.__name__ = "Integer32"
_DocsQosServiceClassAdmittedTimeout_Object = MibTableColumn
docsQosServiceClassAdmittedTimeout = _DocsQosServiceClassAdmittedTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 18),
    _DocsQosServiceClassAdmittedTimeout_Type()
)
docsQosServiceClassAdmittedTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassAdmittedTimeout.setUnits("seconds")


class _DocsQosServiceClassSchedulingType_Type(SchedulingType):
    """Custom type docsQosServiceClassSchedulingType based on SchedulingType"""


_DocsQosServiceClassSchedulingType_Object = MibTableColumn
docsQosServiceClassSchedulingType = _DocsQosServiceClassSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 19),
    _DocsQosServiceClassSchedulingType_Type()
)
docsQosServiceClassSchedulingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassSchedulingType.setStatus("current")


class _DocsQosServiceClassRequestPolicy_Type(OctetString):
    """Custom type docsQosServiceClassRequestPolicy based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsQosServiceClassRequestPolicy_Type.__name__ = "OctetString"
_DocsQosServiceClassRequestPolicy_Object = MibTableColumn
docsQosServiceClassRequestPolicy = _DocsQosServiceClassRequestPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 20),
    _DocsQosServiceClassRequestPolicy_Type()
)
docsQosServiceClassRequestPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassRequestPolicy.setStatus("current")


class _DocsQosServiceClassTosAndMask_Type(OctetString):
    """Custom type docsQosServiceClassTosAndMask based on OctetString"""
    defaultHexValue = "FF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosServiceClassTosAndMask_Type.__name__ = "OctetString"
_DocsQosServiceClassTosAndMask_Object = MibTableColumn
docsQosServiceClassTosAndMask = _DocsQosServiceClassTosAndMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 21),
    _DocsQosServiceClassTosAndMask_Type()
)
docsQosServiceClassTosAndMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTosAndMask.setStatus("current")


class _DocsQosServiceClassTosOrMask_Type(OctetString):
    """Custom type docsQosServiceClassTosOrMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosServiceClassTosOrMask_Type.__name__ = "OctetString"
_DocsQosServiceClassTosOrMask_Object = MibTableColumn
docsQosServiceClassTosOrMask = _DocsQosServiceClassTosOrMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 22),
    _DocsQosServiceClassTosOrMask_Type()
)
docsQosServiceClassTosOrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTosOrMask.setStatus("current")


class _DocsQosServiceClassDirection_Type(IfDirection):
    """Custom type docsQosServiceClassDirection based on IfDirection"""


_DocsQosServiceClassDirection_Object = MibTableColumn
docsQosServiceClassDirection = _DocsQosServiceClassDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 8, 1, 23),
    _DocsQosServiceClassDirection_Type()
)
docsQosServiceClassDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassDirection.setStatus("current")
_DocsQosServiceClassPolicyTable_Object = MibTable
docsQosServiceClassPolicyTable = _DocsQosServiceClassPolicyTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 9)
)
if mibBuilder.loadTexts:
    docsQosServiceClassPolicyTable.setStatus("current")
_DocsQosServiceClassPolicyEntry_Object = MibTableRow
docsQosServiceClassPolicyEntry = _DocsQosServiceClassPolicyEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 9, 1)
)
docsQosServiceClassPolicyEntry.setIndexNames(
    (0, "DOCS-QOS-MIB", "docsQosServiceClassPolicyIndex"),
)
if mibBuilder.loadTexts:
    docsQosServiceClassPolicyEntry.setStatus("current")


class _DocsQosServiceClassPolicyIndex_Type(Integer32):
    """Custom type docsQosServiceClassPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsQosServiceClassPolicyIndex_Type.__name__ = "Integer32"
_DocsQosServiceClassPolicyIndex_Object = MibTableColumn
docsQosServiceClassPolicyIndex = _DocsQosServiceClassPolicyIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 9, 1, 1),
    _DocsQosServiceClassPolicyIndex_Type()
)
docsQosServiceClassPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceClassPolicyIndex.setStatus("current")
_DocsQosServiceClassPolicyName_Type = DisplayString
_DocsQosServiceClassPolicyName_Object = MibTableColumn
docsQosServiceClassPolicyName = _DocsQosServiceClassPolicyName_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 9, 1, 2),
    _DocsQosServiceClassPolicyName_Type()
)
docsQosServiceClassPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassPolicyName.setStatus("current")


class _DocsQosServiceClassPolicyRulePriority_Type(Integer32):
    """Custom type docsQosServiceClassPolicyRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosServiceClassPolicyRulePriority_Type.__name__ = "Integer32"
_DocsQosServiceClassPolicyRulePriority_Object = MibTableColumn
docsQosServiceClassPolicyRulePriority = _DocsQosServiceClassPolicyRulePriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 9, 1, 3),
    _DocsQosServiceClassPolicyRulePriority_Type()
)
docsQosServiceClassPolicyRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassPolicyRulePriority.setStatus("current")
_DocsQosServiceClassPolicyStatus_Type = RowStatus
_DocsQosServiceClassPolicyStatus_Object = MibTableColumn
docsQosServiceClassPolicyStatus = _DocsQosServiceClassPolicyStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 9, 1, 4),
    _DocsQosServiceClassPolicyStatus_Type()
)
docsQosServiceClassPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassPolicyStatus.setStatus("current")
_DocsQosPHSTable_Object = MibTable
docsQosPHSTable = _DocsQosPHSTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10)
)
if mibBuilder.loadTexts:
    docsQosPHSTable.setStatus("current")
_DocsQosPHSEntry_Object = MibTableRow
docsQosPHSEntry = _DocsQosPHSEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1)
)
docsQosPHSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsQosPHSEntry.setStatus("current")


class _DocsQosPHSField_Type(OctetString):
    """Custom type docsQosPHSField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsQosPHSField_Type.__name__ = "OctetString"
_DocsQosPHSField_Object = MibTableColumn
docsQosPHSField = _DocsQosPHSField_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1, 2),
    _DocsQosPHSField_Type()
)
docsQosPHSField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSField.setStatus("current")


class _DocsQosPHSMask_Type(OctetString):
    """Custom type docsQosPHSMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsQosPHSMask_Type.__name__ = "OctetString"
_DocsQosPHSMask_Object = MibTableColumn
docsQosPHSMask = _DocsQosPHSMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1, 3),
    _DocsQosPHSMask_Type()
)
docsQosPHSMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSMask.setStatus("current")


class _DocsQosPHSSize_Type(Integer32):
    """Custom type docsQosPHSSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosPHSSize_Type.__name__ = "Integer32"
_DocsQosPHSSize_Object = MibTableColumn
docsQosPHSSize = _DocsQosPHSSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1, 4),
    _DocsQosPHSSize_Type()
)
docsQosPHSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSSize.setStatus("current")
_DocsQosPHSVerify_Type = TruthValue
_DocsQosPHSVerify_Object = MibTableColumn
docsQosPHSVerify = _DocsQosPHSVerify_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1, 5),
    _DocsQosPHSVerify_Type()
)
docsQosPHSVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSVerify.setStatus("current")


class _DocsQosPHSClassifierIndex_Type(Integer32):
    """Custom type docsQosPHSClassifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsQosPHSClassifierIndex_Type.__name__ = "Integer32"
_DocsQosPHSClassifierIndex_Object = MibTableColumn
docsQosPHSClassifierIndex = _DocsQosPHSClassifierIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1, 6),
    _DocsQosPHSClassifierIndex_Type()
)
docsQosPHSClassifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSClassifierIndex.setStatus("obsolete")


class _DocsQosPHSIndex_Type(Integer32):
    """Custom type docsQosPHSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsQosPHSIndex_Type.__name__ = "Integer32"
_DocsQosPHSIndex_Object = MibTableColumn
docsQosPHSIndex = _DocsQosPHSIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 10, 1, 7),
    _DocsQosPHSIndex_Type()
)
docsQosPHSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSIndex.setStatus("current")
_DocsQosCmtsMacToSrvFlowTable_Object = MibTable
docsQosCmtsMacToSrvFlowTable = _DocsQosCmtsMacToSrvFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 11)
)
if mibBuilder.loadTexts:
    docsQosCmtsMacToSrvFlowTable.setStatus("current")
_DocsQosCmtsMacToSrvFlowEntry_Object = MibTableRow
docsQosCmtsMacToSrvFlowEntry = _DocsQosCmtsMacToSrvFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 11, 1)
)
docsQosCmtsMacToSrvFlowEntry.setIndexNames(
    (0, "DOCS-QOS-MIB", "docsQosCmtsCmMac"),
    (0, "DOCS-QOS-MIB", "docsQosCmtsServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosCmtsMacToSrvFlowEntry.setStatus("current")
_DocsQosCmtsCmMac_Type = MacAddress
_DocsQosCmtsCmMac_Object = MibTableColumn
docsQosCmtsCmMac = _DocsQosCmtsCmMac_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 11, 1, 1),
    _DocsQosCmtsCmMac_Type()
)
docsQosCmtsCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsCmMac.setStatus("current")


class _DocsQosCmtsServiceFlowId_Type(Unsigned32):
    """Custom type docsQosCmtsServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosCmtsServiceFlowId_Type.__name__ = "Unsigned32"
_DocsQosCmtsServiceFlowId_Object = MibTableColumn
docsQosCmtsServiceFlowId = _DocsQosCmtsServiceFlowId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 11, 1, 2),
    _DocsQosCmtsServiceFlowId_Type()
)
docsQosCmtsServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsServiceFlowId.setStatus("current")
_DocsQosCmtsIfIndex_Type = InterfaceIndex
_DocsQosCmtsIfIndex_Object = MibTableColumn
docsQosCmtsIfIndex = _DocsQosCmtsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 1, 11, 1, 3),
    _DocsQosCmtsIfIndex_Type()
)
docsQosCmtsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIfIndex.setStatus("current")
_DocsQosNotification_ObjectIdentity = ObjectIdentity
docsQosNotification = _DocsQosNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 2)
)
_DocsQosConformance_ObjectIdentity = ObjectIdentity
docsQosConformance = _DocsQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3)
)
_DocsQosGroups_ObjectIdentity = ObjectIdentity
docsQosGroups = _DocsQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1)
)
_DocsQosCompliances_ObjectIdentity = ObjectIdentity
docsQosCompliances = _DocsQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 2)
)

# Managed Objects groups

docsQosBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 1)
)
docsQosBaseGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosPktClassDirection"),
        ("DOCS-QOS-MIB", "docsQosPktClassPriority"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpTosLow"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpTosHigh"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpTosMask"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpProtocol"),
        ("DOCS-QOS-MIB", "docsQosPktClassSourcePortStart"),
        ("DOCS-QOS-MIB", "docsQosPktClassSourcePortEnd"),
        ("DOCS-QOS-MIB", "docsQosPktClassDestPortStart"),
        ("DOCS-QOS-MIB", "docsQosPktClassDestPortEnd"),
        ("DOCS-QOS-MIB", "docsQosPktClassDestMacAddr"),
        ("DOCS-QOS-MIB", "docsQosPktClassDestMacMask"),
        ("DOCS-QOS-MIB", "docsQosPktClassSourceMacAddr"),
        ("DOCS-QOS-MIB", "docsQosPktClassEnetProtocolType"),
        ("DOCS-QOS-MIB", "docsQosPktClassEnetProtocol"),
        ("DOCS-QOS-MIB", "docsQosPktClassUserPriLow"),
        ("DOCS-QOS-MIB", "docsQosPktClassUserPriHigh"),
        ("DOCS-QOS-MIB", "docsQosPktClassVlanId"),
        ("DOCS-QOS-MIB", "docsQosPktClassState"),
        ("DOCS-QOS-MIB", "docsQosPktClassPkts"),
        ("DOCS-QOS-MIB", "docsQosPktClassBitMap"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetSourceAddrType"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetSourceAddr"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetSourceMaskType"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetSourceMask"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetDestAddrType"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetDestAddr"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetDestMaskType"),
        ("DOCS-QOS-MIB", "docsQosPktClassInetDestMask"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowSID"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowDirection"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowPrimary"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowPkts"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowOctets"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowTimeCreated"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowTimeActive"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowPHSUnknowns"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowPolicedDropPkts"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowPolicedDelayPkts"),
        ("DOCS-QOS-MIB", "docsQosDSAReqs"),
        ("DOCS-QOS-MIB", "docsQosDSARsps"),
        ("DOCS-QOS-MIB", "docsQosDSAAcks"),
        ("DOCS-QOS-MIB", "docsQosDSCReqs"),
        ("DOCS-QOS-MIB", "docsQosDSCRsps"),
        ("DOCS-QOS-MIB", "docsQosDSCAcks"),
        ("DOCS-QOS-MIB", "docsQosDSDReqs"),
        ("DOCS-QOS-MIB", "docsQosDSDRsps"),
        ("DOCS-QOS-MIB", "docsQosDynamicAdds"),
        ("DOCS-QOS-MIB", "docsQosDynamicAddFails"),
        ("DOCS-QOS-MIB", "docsQosDynamicChanges"),
        ("DOCS-QOS-MIB", "docsQosDynamicChangeFails"),
        ("DOCS-QOS-MIB", "docsQosDynamicDeletes"),
        ("DOCS-QOS-MIB", "docsQosDynamicDeleteFails"),
        ("DOCS-QOS-MIB", "docsQosDCCReqs"),
        ("DOCS-QOS-MIB", "docsQosDCCRsps"),
        ("DOCS-QOS-MIB", "docsQosDCCAcks"),
        ("DOCS-QOS-MIB", "docsQosDCCs"),
        ("DOCS-QOS-MIB", "docsQosDCCFails"),
        ("DOCS-QOS-MIB", "docsQosPHSField"),
        ("DOCS-QOS-MIB", "docsQosPHSMask"),
        ("DOCS-QOS-MIB", "docsQosPHSSize"),
        ("DOCS-QOS-MIB", "docsQosPHSVerify"),
        ("DOCS-QOS-MIB", "docsQosPHSIndex"))
)
if mibBuilder.loadTexts:
    docsQosBaseGroup.setStatus("current")

docsQosParamSetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 2)
)
docsQosParamSetGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosParamSetServiceClassName"),
        ("DOCS-QOS-MIB", "docsQosParamSetPriority"),
        ("DOCS-QOS-MIB", "docsQosParamSetMaxTrafficRate"),
        ("DOCS-QOS-MIB", "docsQosParamSetMaxTrafficBurst"),
        ("DOCS-QOS-MIB", "docsQosParamSetMinReservedRate"),
        ("DOCS-QOS-MIB", "docsQosParamSetMinReservedPkt"),
        ("DOCS-QOS-MIB", "docsQosParamSetActiveTimeout"),
        ("DOCS-QOS-MIB", "docsQosParamSetAdmittedTimeout"),
        ("DOCS-QOS-MIB", "docsQosParamSetMaxConcatBurst"),
        ("DOCS-QOS-MIB", "docsQosParamSetSchedulingType"),
        ("DOCS-QOS-MIB", "docsQosParamSetNomPollInterval"),
        ("DOCS-QOS-MIB", "docsQosParamSetTolPollJitter"),
        ("DOCS-QOS-MIB", "docsQosParamSetUnsolicitGrantSize"),
        ("DOCS-QOS-MIB", "docsQosParamSetNomGrantInterval"),
        ("DOCS-QOS-MIB", "docsQosParamSetTolGrantJitter"),
        ("DOCS-QOS-MIB", "docsQosParamSetGrantsPerInterval"),
        ("DOCS-QOS-MIB", "docsQosParamSetTosAndMask"),
        ("DOCS-QOS-MIB", "docsQosParamSetTosOrMask"),
        ("DOCS-QOS-MIB", "docsQosParamSetMaxLatency"),
        ("DOCS-QOS-MIB", "docsQosParamSetRequestPolicyOct"),
        ("DOCS-QOS-MIB", "docsQosParamSetBitMap"))
)
if mibBuilder.loadTexts:
    docsQosParamSetGroup.setStatus("current")

docsQosCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 3)
)
docsQosCmtsGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosUpstreamFragments"),
        ("DOCS-QOS-MIB", "docsQosUpstreamFragDiscards"),
        ("DOCS-QOS-MIB", "docsQosUpstreamConcatBursts"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogIfIndex"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogSFID"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogCmMac"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogPkts"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogOctets"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogTimeDeleted"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogTimeCreated"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogTimeActive"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogDirection"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogPrimary"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogServiceClassName"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogPolicedDropPkts"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogPolicedDelayPkts"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowLogControl"),
        ("DOCS-QOS-MIB", "docsQosCmtsIfIndex"))
)
if mibBuilder.loadTexts:
    docsQosCmtsGroup.setStatus("current")

docsQosSrvClassPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 4)
)
docsQosSrvClassPolicyGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosServiceClassPolicyName"),
        ("DOCS-QOS-MIB", "docsQosServiceClassPolicyRulePriority"),
        ("DOCS-QOS-MIB", "docsQosServiceClassPolicyStatus"))
)
if mibBuilder.loadTexts:
    docsQosSrvClassPolicyGroup.setStatus("current")

docsQosServiceClassGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 5)
)
docsQosServiceClassGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosServiceClassStatus"),
        ("DOCS-QOS-MIB", "docsQosServiceClassPriority"),
        ("DOCS-QOS-MIB", "docsQosServiceClassMaxTrafficRate"),
        ("DOCS-QOS-MIB", "docsQosServiceClassMaxTrafficBurst"),
        ("DOCS-QOS-MIB", "docsQosServiceClassMinReservedRate"),
        ("DOCS-QOS-MIB", "docsQosServiceClassMinReservedPkt"),
        ("DOCS-QOS-MIB", "docsQosServiceClassMaxConcatBurst"),
        ("DOCS-QOS-MIB", "docsQosServiceClassNomPollInterval"),
        ("DOCS-QOS-MIB", "docsQosServiceClassTolPollJitter"),
        ("DOCS-QOS-MIB", "docsQosServiceClassUnsolicitGrantSize"),
        ("DOCS-QOS-MIB", "docsQosServiceClassNomGrantInterval"),
        ("DOCS-QOS-MIB", "docsQosServiceClassTolGrantJitter"),
        ("DOCS-QOS-MIB", "docsQosServiceClassGrantsPerInterval"),
        ("DOCS-QOS-MIB", "docsQosServiceClassMaxLatency"),
        ("DOCS-QOS-MIB", "docsQosServiceClassActiveTimeout"),
        ("DOCS-QOS-MIB", "docsQosServiceClassAdmittedTimeout"),
        ("DOCS-QOS-MIB", "docsQosServiceClassSchedulingType"),
        ("DOCS-QOS-MIB", "docsQosServiceClassRequestPolicy"),
        ("DOCS-QOS-MIB", "docsQosServiceClassTosAndMask"),
        ("DOCS-QOS-MIB", "docsQosServiceClassTosOrMask"),
        ("DOCS-QOS-MIB", "docsQosServiceClassDirection"))
)
if mibBuilder.loadTexts:
    docsQosServiceClassGroup.setStatus("current")

docsQosDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 6)
)
docsQosDeprecatedGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosPktClassIpSourceAddr"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpSourceMask"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpDestAddr"),
        ("DOCS-QOS-MIB", "docsQosPktClassIpDestMask"))
)
if mibBuilder.loadTexts:
    docsQosDeprecatedGroup.setStatus("deprecated")

docsQosObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 1, 7)
)
docsQosObsoleteGroup.setObjects(
      *(("DOCS-QOS-MIB", "docsQosPktClassUserPriApplies"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowProvisionedParamSetIndex"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowAdmittedParamSetIndex"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowActiveParamSetIndex"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowActiveTimeout"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowAdmittedTimeout"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowSchedulingType"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowRequestPolicy"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowTosAndMask"),
        ("DOCS-QOS-MIB", "docsQosServiceFlowTosOrMask"),
        ("DOCS-QOS-MIB", "docsQosServiceClassParamSetIndex"),
        ("DOCS-QOS-MIB", "docsQosPHSClassifierIndex"))
)
if mibBuilder.loadTexts:
    docsQosObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    docsQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-QOS-MIB",
    **{"IfDirection": IfDirection,
       "BitRate": BitRate,
       "SchedulingType": SchedulingType,
       "docsQosMIB": docsQosMIB,
       "docsQosMIBObjects": docsQosMIBObjects,
       "docsQosPktClassTable": docsQosPktClassTable,
       "docsQosPktClassEntry": docsQosPktClassEntry,
       "docsQosPktClassId": docsQosPktClassId,
       "docsQosPktClassDirection": docsQosPktClassDirection,
       "docsQosPktClassPriority": docsQosPktClassPriority,
       "docsQosPktClassIpTosLow": docsQosPktClassIpTosLow,
       "docsQosPktClassIpTosHigh": docsQosPktClassIpTosHigh,
       "docsQosPktClassIpTosMask": docsQosPktClassIpTosMask,
       "docsQosPktClassIpProtocol": docsQosPktClassIpProtocol,
       "docsQosPktClassIpSourceAddr": docsQosPktClassIpSourceAddr,
       "docsQosPktClassIpSourceMask": docsQosPktClassIpSourceMask,
       "docsQosPktClassIpDestAddr": docsQosPktClassIpDestAddr,
       "docsQosPktClassIpDestMask": docsQosPktClassIpDestMask,
       "docsQosPktClassSourcePortStart": docsQosPktClassSourcePortStart,
       "docsQosPktClassSourcePortEnd": docsQosPktClassSourcePortEnd,
       "docsQosPktClassDestPortStart": docsQosPktClassDestPortStart,
       "docsQosPktClassDestPortEnd": docsQosPktClassDestPortEnd,
       "docsQosPktClassDestMacAddr": docsQosPktClassDestMacAddr,
       "docsQosPktClassDestMacMask": docsQosPktClassDestMacMask,
       "docsQosPktClassSourceMacAddr": docsQosPktClassSourceMacAddr,
       "docsQosPktClassEnetProtocolType": docsQosPktClassEnetProtocolType,
       "docsQosPktClassEnetProtocol": docsQosPktClassEnetProtocol,
       "docsQosPktClassUserPriApplies": docsQosPktClassUserPriApplies,
       "docsQosPktClassUserPriLow": docsQosPktClassUserPriLow,
       "docsQosPktClassUserPriHigh": docsQosPktClassUserPriHigh,
       "docsQosPktClassVlanId": docsQosPktClassVlanId,
       "docsQosPktClassState": docsQosPktClassState,
       "docsQosPktClassPkts": docsQosPktClassPkts,
       "docsQosPktClassBitMap": docsQosPktClassBitMap,
       "docsQosPktClassInetSourceAddrType": docsQosPktClassInetSourceAddrType,
       "docsQosPktClassInetSourceAddr": docsQosPktClassInetSourceAddr,
       "docsQosPktClassInetSourceMaskType": docsQosPktClassInetSourceMaskType,
       "docsQosPktClassInetSourceMask": docsQosPktClassInetSourceMask,
       "docsQosPktClassInetDestAddrType": docsQosPktClassInetDestAddrType,
       "docsQosPktClassInetDestAddr": docsQosPktClassInetDestAddr,
       "docsQosPktClassInetDestMaskType": docsQosPktClassInetDestMaskType,
       "docsQosPktClassInetDestMask": docsQosPktClassInetDestMask,
       "docsQosParamSetTable": docsQosParamSetTable,
       "docsQosParamSetEntry": docsQosParamSetEntry,
       "docsQosParamSetServiceClassName": docsQosParamSetServiceClassName,
       "docsQosParamSetPriority": docsQosParamSetPriority,
       "docsQosParamSetMaxTrafficRate": docsQosParamSetMaxTrafficRate,
       "docsQosParamSetMaxTrafficBurst": docsQosParamSetMaxTrafficBurst,
       "docsQosParamSetMinReservedRate": docsQosParamSetMinReservedRate,
       "docsQosParamSetMinReservedPkt": docsQosParamSetMinReservedPkt,
       "docsQosParamSetActiveTimeout": docsQosParamSetActiveTimeout,
       "docsQosParamSetAdmittedTimeout": docsQosParamSetAdmittedTimeout,
       "docsQosParamSetMaxConcatBurst": docsQosParamSetMaxConcatBurst,
       "docsQosParamSetSchedulingType": docsQosParamSetSchedulingType,
       "docsQosParamSetNomPollInterval": docsQosParamSetNomPollInterval,
       "docsQosParamSetTolPollJitter": docsQosParamSetTolPollJitter,
       "docsQosParamSetUnsolicitGrantSize": docsQosParamSetUnsolicitGrantSize,
       "docsQosParamSetNomGrantInterval": docsQosParamSetNomGrantInterval,
       "docsQosParamSetTolGrantJitter": docsQosParamSetTolGrantJitter,
       "docsQosParamSetGrantsPerInterval": docsQosParamSetGrantsPerInterval,
       "docsQosParamSetTosAndMask": docsQosParamSetTosAndMask,
       "docsQosParamSetTosOrMask": docsQosParamSetTosOrMask,
       "docsQosParamSetMaxLatency": docsQosParamSetMaxLatency,
       "docsQosParamSetType": docsQosParamSetType,
       "docsQosParamSetRequestPolicyOct": docsQosParamSetRequestPolicyOct,
       "docsQosParamSetBitMap": docsQosParamSetBitMap,
       "docsQosServiceFlowTable": docsQosServiceFlowTable,
       "docsQosServiceFlowEntry": docsQosServiceFlowEntry,
       "docsQosServiceFlowId": docsQosServiceFlowId,
       "docsQosServiceFlowProvisionedParamSetIndex": docsQosServiceFlowProvisionedParamSetIndex,
       "docsQosServiceFlowAdmittedParamSetIndex": docsQosServiceFlowAdmittedParamSetIndex,
       "docsQosServiceFlowActiveParamSetIndex": docsQosServiceFlowActiveParamSetIndex,
       "docsQosServiceFlowSID": docsQosServiceFlowSID,
       "docsQosServiceFlowDirection": docsQosServiceFlowDirection,
       "docsQosServiceFlowPrimary": docsQosServiceFlowPrimary,
       "docsQosServiceFlowActiveTimeout": docsQosServiceFlowActiveTimeout,
       "docsQosServiceFlowAdmittedTimeout": docsQosServiceFlowAdmittedTimeout,
       "docsQosServiceFlowSchedulingType": docsQosServiceFlowSchedulingType,
       "docsQosServiceFlowRequestPolicy": docsQosServiceFlowRequestPolicy,
       "docsQosServiceFlowTosAndMask": docsQosServiceFlowTosAndMask,
       "docsQosServiceFlowTosOrMask": docsQosServiceFlowTosOrMask,
       "docsQosServiceFlowStatsTable": docsQosServiceFlowStatsTable,
       "docsQosServiceFlowStatsEntry": docsQosServiceFlowStatsEntry,
       "docsQosServiceFlowPkts": docsQosServiceFlowPkts,
       "docsQosServiceFlowOctets": docsQosServiceFlowOctets,
       "docsQosServiceFlowTimeCreated": docsQosServiceFlowTimeCreated,
       "docsQosServiceFlowTimeActive": docsQosServiceFlowTimeActive,
       "docsQosServiceFlowPHSUnknowns": docsQosServiceFlowPHSUnknowns,
       "docsQosServiceFlowPolicedDropPkts": docsQosServiceFlowPolicedDropPkts,
       "docsQosServiceFlowPolicedDelayPkts": docsQosServiceFlowPolicedDelayPkts,
       "docsQosUpstreamStatsTable": docsQosUpstreamStatsTable,
       "docsQosUpstreamStatsEntry": docsQosUpstreamStatsEntry,
       "docsQosSID": docsQosSID,
       "docsQosUpstreamFragments": docsQosUpstreamFragments,
       "docsQosUpstreamFragDiscards": docsQosUpstreamFragDiscards,
       "docsQosUpstreamConcatBursts": docsQosUpstreamConcatBursts,
       "docsQosDynamicServiceStatsTable": docsQosDynamicServiceStatsTable,
       "docsQosDynamicServiceStatsEntry": docsQosDynamicServiceStatsEntry,
       "docsQosIfDirection": docsQosIfDirection,
       "docsQosDSAReqs": docsQosDSAReqs,
       "docsQosDSARsps": docsQosDSARsps,
       "docsQosDSAAcks": docsQosDSAAcks,
       "docsQosDSCReqs": docsQosDSCReqs,
       "docsQosDSCRsps": docsQosDSCRsps,
       "docsQosDSCAcks": docsQosDSCAcks,
       "docsQosDSDReqs": docsQosDSDReqs,
       "docsQosDSDRsps": docsQosDSDRsps,
       "docsQosDynamicAdds": docsQosDynamicAdds,
       "docsQosDynamicAddFails": docsQosDynamicAddFails,
       "docsQosDynamicChanges": docsQosDynamicChanges,
       "docsQosDynamicChangeFails": docsQosDynamicChangeFails,
       "docsQosDynamicDeletes": docsQosDynamicDeletes,
       "docsQosDynamicDeleteFails": docsQosDynamicDeleteFails,
       "docsQosDCCReqs": docsQosDCCReqs,
       "docsQosDCCRsps": docsQosDCCRsps,
       "docsQosDCCAcks": docsQosDCCAcks,
       "docsQosDCCs": docsQosDCCs,
       "docsQosDCCFails": docsQosDCCFails,
       "docsQosDCCRspDeparts": docsQosDCCRspDeparts,
       "docsQosDCCRspArrives": docsQosDCCRspArrives,
       "docsQosServiceFlowLogTable": docsQosServiceFlowLogTable,
       "docsQosServiceFlowLogEntry": docsQosServiceFlowLogEntry,
       "docsQosServiceFlowLogIndex": docsQosServiceFlowLogIndex,
       "docsQosServiceFlowLogIfIndex": docsQosServiceFlowLogIfIndex,
       "docsQosServiceFlowLogSFID": docsQosServiceFlowLogSFID,
       "docsQosServiceFlowLogCmMac": docsQosServiceFlowLogCmMac,
       "docsQosServiceFlowLogPkts": docsQosServiceFlowLogPkts,
       "docsQosServiceFlowLogOctets": docsQosServiceFlowLogOctets,
       "docsQosServiceFlowLogTimeDeleted": docsQosServiceFlowLogTimeDeleted,
       "docsQosServiceFlowLogTimeCreated": docsQosServiceFlowLogTimeCreated,
       "docsQosServiceFlowLogTimeActive": docsQosServiceFlowLogTimeActive,
       "docsQosServiceFlowLogDirection": docsQosServiceFlowLogDirection,
       "docsQosServiceFlowLogPrimary": docsQosServiceFlowLogPrimary,
       "docsQosServiceFlowLogServiceClassName": docsQosServiceFlowLogServiceClassName,
       "docsQosServiceFlowLogPolicedDropPkts": docsQosServiceFlowLogPolicedDropPkts,
       "docsQosServiceFlowLogPolicedDelayPkts": docsQosServiceFlowLogPolicedDelayPkts,
       "docsQosServiceFlowLogControl": docsQosServiceFlowLogControl,
       "docsQosServiceClassTable": docsQosServiceClassTable,
       "docsQosServiceClassEntry": docsQosServiceClassEntry,
       "docsQosServiceClassName": docsQosServiceClassName,
       "docsQosServiceClassParamSetIndex": docsQosServiceClassParamSetIndex,
       "docsQosServiceClassStatus": docsQosServiceClassStatus,
       "docsQosServiceClassPriority": docsQosServiceClassPriority,
       "docsQosServiceClassMaxTrafficRate": docsQosServiceClassMaxTrafficRate,
       "docsQosServiceClassMaxTrafficBurst": docsQosServiceClassMaxTrafficBurst,
       "docsQosServiceClassMinReservedRate": docsQosServiceClassMinReservedRate,
       "docsQosServiceClassMinReservedPkt": docsQosServiceClassMinReservedPkt,
       "docsQosServiceClassMaxConcatBurst": docsQosServiceClassMaxConcatBurst,
       "docsQosServiceClassNomPollInterval": docsQosServiceClassNomPollInterval,
       "docsQosServiceClassTolPollJitter": docsQosServiceClassTolPollJitter,
       "docsQosServiceClassUnsolicitGrantSize": docsQosServiceClassUnsolicitGrantSize,
       "docsQosServiceClassNomGrantInterval": docsQosServiceClassNomGrantInterval,
       "docsQosServiceClassTolGrantJitter": docsQosServiceClassTolGrantJitter,
       "docsQosServiceClassGrantsPerInterval": docsQosServiceClassGrantsPerInterval,
       "docsQosServiceClassMaxLatency": docsQosServiceClassMaxLatency,
       "docsQosServiceClassActiveTimeout": docsQosServiceClassActiveTimeout,
       "docsQosServiceClassAdmittedTimeout": docsQosServiceClassAdmittedTimeout,
       "docsQosServiceClassSchedulingType": docsQosServiceClassSchedulingType,
       "docsQosServiceClassRequestPolicy": docsQosServiceClassRequestPolicy,
       "docsQosServiceClassTosAndMask": docsQosServiceClassTosAndMask,
       "docsQosServiceClassTosOrMask": docsQosServiceClassTosOrMask,
       "docsQosServiceClassDirection": docsQosServiceClassDirection,
       "docsQosServiceClassPolicyTable": docsQosServiceClassPolicyTable,
       "docsQosServiceClassPolicyEntry": docsQosServiceClassPolicyEntry,
       "docsQosServiceClassPolicyIndex": docsQosServiceClassPolicyIndex,
       "docsQosServiceClassPolicyName": docsQosServiceClassPolicyName,
       "docsQosServiceClassPolicyRulePriority": docsQosServiceClassPolicyRulePriority,
       "docsQosServiceClassPolicyStatus": docsQosServiceClassPolicyStatus,
       "docsQosPHSTable": docsQosPHSTable,
       "docsQosPHSEntry": docsQosPHSEntry,
       "docsQosPHSField": docsQosPHSField,
       "docsQosPHSMask": docsQosPHSMask,
       "docsQosPHSSize": docsQosPHSSize,
       "docsQosPHSVerify": docsQosPHSVerify,
       "docsQosPHSClassifierIndex": docsQosPHSClassifierIndex,
       "docsQosPHSIndex": docsQosPHSIndex,
       "docsQosCmtsMacToSrvFlowTable": docsQosCmtsMacToSrvFlowTable,
       "docsQosCmtsMacToSrvFlowEntry": docsQosCmtsMacToSrvFlowEntry,
       "docsQosCmtsCmMac": docsQosCmtsCmMac,
       "docsQosCmtsServiceFlowId": docsQosCmtsServiceFlowId,
       "docsQosCmtsIfIndex": docsQosCmtsIfIndex,
       "docsQosNotification": docsQosNotification,
       "docsQosConformance": docsQosConformance,
       "docsQosGroups": docsQosGroups,
       "docsQosBaseGroup": docsQosBaseGroup,
       "docsQosParamSetGroup": docsQosParamSetGroup,
       "docsQosCmtsGroup": docsQosCmtsGroup,
       "docsQosSrvClassPolicyGroup": docsQosSrvClassPolicyGroup,
       "docsQosServiceClassGroup": docsQosServiceClassGroup,
       "docsQosDeprecatedGroup": docsQosDeprecatedGroup,
       "docsQosObsoleteGroup": docsQosObsoleteGroup,
       "docsQosCompliances": docsQosCompliances,
       "docsQosCompliance": docsQosCompliance}
)
